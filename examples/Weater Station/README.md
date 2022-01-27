# A Complete Battery-Free Weather Station Example Project

This is a self contained example project.
It uses BFree as a battery-free weather station that periodically sends temperature and humidity data over LoRa to a constantly powered receiver.


## Metro M0 Express BFree firmware
Contains the pre-compiled firmware `.elf` for the modified version of CircuitPython (https://github.com/TUDSSL/BFree-core/releases).
This only has to be flashed to the Metro M0 Express once.
Additionally it contains a `lib` directory of unmodified Python libraries for the specific version of CircuitPyhton used by BFree.

## Test Code
Contains a small test program that can be used to verify that BFree is correctly restoring the Python program after a power-failure.

## Receiver
Contains the Pyhthon code for the receiver that should be connected to the PC
![Receiver](img/Receiver.png)

## Battery-Free Transmitter
The BFree Python program that collects sensor data, computes the average of `N` samples, and broadcasts the result over LoRa.

![Transmitter](img/Battery-Free-Transmitter-complete.png)

