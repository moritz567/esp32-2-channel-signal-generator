#include <Arduino.h>
#include <driver/dac.h>
#include <driver/timer.h>

static const float SAMPLE_RATE = 40000.0f;    // Abtastrate, z.B. 40 kHz
static const int   TIMER_DIVIDER = 2;         // 80 MHz / 2 = 40 MHz Timer-Clock

volatile float freq1 = 40.0f;        // Frequenz für Kanal 1 (Hz)
volatile float freq2 = 40.0f;        // Frequenz für Kanal 2 (Hz)
volatile float phaseOffsetDeg = 0.0f; // Phasenoffset für Kanal 2 (in Grad)

// Amplitudenfaktoren (integer), z. B. 0..256 => 0..1.0
volatile uint16_t ampFac1     = 256;  // 256 => 1.0
volatile uint16_t ampFac2     = 256;  // 256 => 1.0

// DDS-Parameter
volatile uint32_t phaseAcc1 = 0;     // Phasenakkumulator Kanal 1
volatile uint32_t phaseAcc2 = 0;     // Phasenakkumulator Kanal 2
volatile uint32_t inc1     = 0;
volatile uint32_t inc2     = 0;
volatile uint32_t phaseOffset = 0;   // Phasenoffset (berechnet aus Grad)

// Sinus-Lookup-Tabelle (256 Einträge, Wertebereich 0-255)
#define TABLE_SIZE 256
uint8_t sineTable[TABLE_SIZE];


// Timer-Interrupt Service Routine
bool IRAM_ATTR onTimer(void *arg) {
  phaseAcc1 += inc1;
  phaseAcc2 += inc2;

  // Phasenoffset für Kanal 2 berücksichtigen
  uint32_t phase2 = phaseAcc2 + phaseOffset;

  // ==Kanal1==  
  unsigned int rawSine1 = sineTable[phaseAcc1 >> 24]; // Tabelle abfragen (oberste 8 Bits für Index)
  int wave1 = (int)rawSine1 - 128;                                                                                                                                                                                
  wave1 = (wave1 * ampFac1) >> 8; //Faktor multiplizieren dann durch 256 teilen
  wave1 += 128;
  // if (wave1 < 0)   wave1 = 0; //braucht man nur vllt zur Sicherheit um Abstürze zu vermeiden
  // if (wave1 > 255) wave1 = 255;

  // ==Kanal2==
  unsigned int rawSine2 = sineTable[phase2 >> 24];  // tableWert - Amplitude (0-255)
  int wave2 = (int)rawSine2 - 128;            //auf Bereich -128 bis +127 herabsetzten, (um 0 zentrieren)                                                                                                                                                                
  wave2 = (wave2 * ampFac2) >> 8;             //Faktor multiplizieren dann durch 256 teilen
  wave2 += 128;                               //wieder auf Bereich 0-255 anheben

  // DAC-Ausgabe
  dac_output_voltage(DAC_CHANNEL_1, wave1); // GPIO25
  dac_output_voltage(DAC_CHANNEL_2, wave2); // GPIO26

  return false; // Kein Yield benötigt
}



void updateDDS() {
  // Inkremente berechnen
  inc1 = (uint32_t)(freq1 * (4294967296.0 / SAMPLE_RATE)); //SAMPLE_RATE = 40000
  inc2 = (uint32_t)(freq2 * (4294967296.0 / SAMPLE_RATE));

  //Phasenoffset in 32-Bit-Fixpoint
  phaseOffset = (uint32_t)(
    (phaseOffsetDeg * M_PI / 180.0) * 
    (4294967296.0 / (2.0 * M_PI))
  );

  // Akkus zurücksetzen -> Neustart in Phase
  phaseAcc1 = 0;
  phaseAcc2 = 0;
}




void setup() {
  Serial.begin(115200);
  // Sinus-Tabelle erstellen
  for (int i = 0; i < TABLE_SIZE; i++) {
    sineTable[i] = 128 + 127 * sin(2 * M_PI * i / TABLE_SIZE + M_PI / 2); // Werte zwischen 0 und 255
  }

  // DAC initialisieren
  dac_output_enable(DAC_CHANNEL_1);
  dac_output_enable(DAC_CHANNEL_2);

  // Timer konfigurieren
  timer_config_t config = {
    .alarm_en = TIMER_ALARM_EN,
    .counter_en = TIMER_PAUSE,
    .intr_type = TIMER_INTR_LEVEL,
    .counter_dir = TIMER_COUNT_UP,
    .auto_reload = TIMER_AUTORELOAD_EN,
    .divider = TIMER_DIVIDER
  };
  timer_init(TIMER_GROUP_0, TIMER_0, &config);
  timer_set_counter_value(TIMER_GROUP_0, TIMER_0, 0);

  // Timer-Interrupt registrieren
  timer_enable_intr(TIMER_GROUP_0, TIMER_0);
  timer_isr_callback_add(TIMER_GROUP_0, TIMER_0, onTimer, NULL, ESP_INTR_FLAG_IRAM);

  // Abtast-Periode einstellen:
  // Timer-Clock = 80 MHz / TIMER_DIVIDER = 40 MHz
  // => 1 Takt = 25 ns
  // => Abtastintervall = 1/SAMPLE_RATE = z.B. 1/40000 s = 25 µs = 25000 ns
  // => 25000 ns / 25 ns = 1000 Takte
  uint32_t alarmVal = (uint32_t)( (40e6f / SAMPLE_RATE) + 0.5f );
  timer_set_alarm_value(TIMER_GROUP_0, TIMER_0, alarmVal);

  // DDS-Variablen initialisieren
  updateDDS();

  // Timer starten 
  timer_start(TIMER_GROUP_0, TIMER_0);

  Serial.println("DDS gestartet");
}

void loop() {
  // Frequenz oder Phase per Serial ändern (optional)
  //Eingabe: 40,40,0,255,255 //f1,f2,phase,amp1,amp2
  if (Serial.available() > 0) {
    float f1 = Serial.parseFloat(); //Frequenz DAC Kanal1
    float f2 = Serial.parseFloat(); //Frequenz DAC Kanal2
    phaseOffsetDeg = Serial.parseFloat(); //Pahsenversatz Kanal2
    ampFac1 = Serial.parseInt();
    ampFac2 = Serial.parseInt();


    // Auf sinnvolle Werte prüfen
    if (f1 < 0.1f) f1 = 0.1f;
    if (f2 < 0.1f) f2 = 0.1f;

    freq1 = f1;
    freq2 = f2;

    // Aktualisieren
    updateDDS();

    Serial.print("F1: ");
    Serial.println(freq1);
    Serial.print("F2: ");
    Serial.println(freq2);
    Serial.print("Phasenoffset: ");
    Serial.println(phaseOffsetDeg);
    Serial.print("Amplitude1: ");
    Serial.println(ampFac1);
    Serial.print("Amplitude2: ");
    Serial.println(ampFac2);
  }
}