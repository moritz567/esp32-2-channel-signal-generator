#include <Arduino.h>
#include <driver/dac.h>
#include <driver/timer.h>

static const float SAMPLE_RATE = 40000.0f;    // Sample rate, e.g. 40 kHz
static const int   TIMER_DIVIDER = 2;         // 80 MHz / 2 = 40 MHz timer clock

volatile float freq1 = 40.0f;         // Frequency for channel 1 [Hz]
volatile float freq2 = 40.0f;         // Frequency für channel 2 [Hz]
volatile float phaseOffsetDeg = 0.0f; // Phase offset for channel 2 (in degrees)

// Amplitude factors (integer), 0..256
//0V = 0    3,3V = 256
volatile uint16_t ampFac1 = 256;
volatile uint16_t ampFac2 = 256;

// DDS parameters
volatile uint32_t phaseAcc1 = 0;     // Phase accumulator for channel 1
volatile uint32_t phaseAcc2 = 0;     // Phase accumulator for channel 2
volatile uint32_t inc1     = 0;
volatile uint32_t inc2     = 0;
volatile uint32_t phaseOffset = 0;   // Phase offset (calculated from degrees)

// Sine lookup table (256 entries, value range 0-255)
#define TABLE_SIZE 256
uint8_t sineTable[TABLE_SIZE];


// Timer interrupt service routine (ISR)
bool IRAM_ATTR onTimer(void *arg) {
  phaseAcc1 += inc1;
  phaseAcc2 += inc2;

  // Take the phase offset for channel 2 into account
  uint32_t phase2 = phaseAcc2 + phaseOffset;

  // == Channel 1 ==
  unsigned int rawSine1 = sineTable[phaseAcc1 >> 24]; // Lookup table (top 8 bits for index)
  int wave1 = (int)rawSine1 - 128;                                                                                                                                                                                
  wave1 = (wave1 * ampFac1) >> 8; // Multiply by factor then divide by 256
  wave1 += 128;

  // == Channel 2 ==
  unsigned int rawSine2 = sineTable[phase2 >> 24];  // Table value - amplitude (0-255)
  int wave2 = (int)rawSine2 - 128;                  // Shift to range -128 to +127 (center around 0)                                                                                                                                                                
  wave2 = (wave2 * ampFac2) >> 8;                   // Multiply by factor then divide by 256
  wave2 += 128;                                     // Shift back to range 0-255

  // DAC output
  dac_output_voltage(DAC_CHANNEL_1, wave1); // GPIO25
  dac_output_voltage(DAC_CHANNEL_2, wave2); // GPIO26

  return false;
}



void updateDDS() {
  // Calculate increments
  inc1 = (uint32_t)(freq1 * (4294967296.0 / SAMPLE_RATE)); //SAMPLE_RATE = 40000
  inc2 = (uint32_t)(freq2 * (4294967296.0 / SAMPLE_RATE));

  // Phase offset in 32-bit fixed point
  phaseOffset = (uint32_t)(
    (phaseOffsetDeg * M_PI / 180.0) * 
    (4294967296.0 / (2.0 * M_PI))
  );

  // Reset accumulators -> restart in phase
  phaseAcc1 = 0;
  phaseAcc2 = 0;
}




void setup() {
  Serial.begin(115200);
  // Create the sine table
  for (int i = 0; i < TABLE_SIZE; i++) {
    sineTable[i] = 128 + 127 * sin(2 * M_PI * i / TABLE_SIZE + M_PI / 2); // Values between 0 and 255
  }

  // Initialize DAC
  dac_output_enable(DAC_CHANNEL_1);
  dac_output_enable(DAC_CHANNEL_2);

  // Configure Timer
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

  // register Timer interrupt
  timer_enable_intr(TIMER_GROUP_0, TIMER_0);
  timer_isr_callback_add(TIMER_GROUP_0, TIMER_0, onTimer, NULL, ESP_INTR_FLAG_IRAM);

  // Set the sampling period:
  // Timer clock = 80 MHz / TIMER_DIVIDER = 40 MHz
  // => 1 clock cycle = 25 ns
  // => sampling interval = 1 / SAMPLE_RATE = e.g. 1/40000 s = 25 µs = 25000 ns
  // => 25000 ns / 25 ns = 1000 clock cycles
  uint32_t alarmVal = (uint32_t)( (40e6f / SAMPLE_RATE) + 0.5f );
  timer_set_alarm_value(TIMER_GROUP_0, TIMER_0, alarmVal);

  // Initialize DDS variables
  updateDDS();

  // start Timer
  timer_start(TIMER_GROUP_0, TIMER_0);

  Serial.println("DDS started");
}

void loop() {
  // Change frequency or phase via Serial (optional)
  // Input e.g: 40,40,0,255,255 // f1, f2, phase, amp1, amp2
  if (Serial.available() > 0) {
    float f1 = Serial.parseFloat(); // Frequency DAC channel 1
    float f2 = Serial.parseFloat(); // Frequency DAC channel 2
    phaseOffsetDeg = Serial.parseFloat(); // Phase offset channel 2
    ampFac1 = Serial.parseInt();
    ampFac2 = Serial.parseInt();


    // Check for reasonable values
    if (f1 < 0.1f) f1 = 0.1f;
    if (f2 < 0.1f) f2 = 0.1f;

    freq1 = f1;
    freq2 = f2;

    updateDDS();

    Serial.print("F1: ");
    Serial.println(freq1);
    Serial.print("F2: ");
    Serial.println(freq2);
    Serial.print("Phaseoffset: ");
    Serial.println(phaseOffsetDeg);
    Serial.print("Amplitude1: ");
    Serial.println(ampFac1);
    Serial.print("Amplitude2: ");
    Serial.println(ampFac2);
  }
}