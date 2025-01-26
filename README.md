# Dual-Channel Signal Generator for ESP32

This project generates two sine waves on the ESP32’s built-in DAC channels using timer-based interrupts. You can dynamically change each channel’s frequency, amplitude, and phase offset via the Serial Monitor.  
based on DDS (Direct Digital Synthesis)  


## Features
Dual-channel sine generation: Outputs on DAC channel 1 (GPIO25) and DAC channel 2 (GPIO26).  
Adjustable:
- Frequency: freq1 and freq2 (in Hz) (float).  
- Amplitude: ampFac1 and ampFac2 (int) from 0 to 256 corresponds to 0 to 3,3V on the DACs.  
- Phase offset: phaseOffsetDeg (in degrees) for channel 2. (float)  


## Usage

Usage
Once the code is uploaded and running:

Open the Serial Monitor at 115200 baud without line ending.
Send the following format to set frequencies, phase offset, and amplitudes:

Example:

```c
40,40,0,256,256
```
The program will respond with the set parameters:
```c
F1: 40
F2: 40
Phaseoffset: 0
Amplitude1: 256
Amplitude2: 256
```

This sets:
freq1 = 40 Hz,
freq2 = 40 Hz,
phaseOffsetDeg = 0°,
ampFac1 = 256,
ampFac2 = 256  
You can probe GPIO25 and GPIO26 with an oscilloscope or other measuring equipment to see the resulting waveforms.






## Getting Started
#### Hardware Requirements:
ESP32 board with DAC (e.g., ESP32 DevKitC).


#### Software Requirements:
Arduino IDE (or PlatformIO / another environment) with ESP32 board support installed.
Make sure you have the ESP32 core libraries (driver/dac.h, driver/timer.h) available via the Arduino IDE.

Clone or download this repository.
Open the .ino file in the Arduino IDE.
Select your ESP32 board under Tools > Board.
Upload the sketch to your ESP32.

## Contributing
If you find a bug feel free to open a issue.  
Pull requests are welcome.

## Customization
Sample Rate: Adjust SAMPLE_RATE (default 40000.0f) in the code if you need a different sampling frequency.  
Timer Divider: For finer control of the timer clock, you can modify TIMER_DIVIDER.  
Sine Table: The size (TABLE_SIZE) and content of the sine lookup table can be changed to suit different waveform shapes or precision needs.

## Known Limitations
The maximum sampling rate and output frequency are bounded by the ESP32 hardware capabilities and the Arduino environment overhead.
For higher frequencies the sine wave will have a lower resolution.  
For very high frequencies (close to or above half of the sampling rate), aliasing and distortions will occur.  
Amplitude factors are only supported between 0 and 256.

## License

[MIT](https://choosealicense.com/licenses/mit/)