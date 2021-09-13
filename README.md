# BFree

This is the official public repository for a **battery-free** prototping platform with [CircuitPython](https://circuitpython.org/) for the [Adafruit Metro M0 Express](https://www.adafruit.com/product/3505).
This repository contains all the sources needed to get started using CircuitPython without any batteries!

## Project Overview

### Rationale
Batteries are bad for the environment, and many embedded applications do not rely on a constant flow of energy. However, just connecting an energy-harvesting source to a microcontroller does not fully solve the problem. Energy from harvested sources is not constant and maybe not enough to continuously run the device, so we have to buffer some energy (typically in a capacitor). When a certain amount of energy is collected, the system activates for some seconds.

It would be problematic if the program would start from the beginning every time the system restarts. Going into a sleep mode might also be problematic, as you never know when the energy returns.

**This work focuses on continuing a Python application where it left off when the system restarts after a power failure, called intermittent-computing**
We achieve this without any involvement from the user or any modifications to the Python code!

All the magic happens internally in our modified version of the CircuitPython interpreter ([added as a submodule in software/BFree-core](https://github.com/TUDSSL/BFree-core)), which works together with our [BFree shield](hardware/BFree-shield). Everything is entirely open-source and accessible through this GitHub repository.

<img src="https://github.com/TUDSSL/BFree/blob/main/doc-images/bfree-overview.jpg">
  
The above figure presents: (A) the BFree hardware shield; (B) example Python code executed on the [Adafruit Metro M0 Express board](https://www.adafruit.com/product/3505) with the BFree shield; (C) the BFree shield with Adafruit Metro M0 Express board running a battery-free temperature measurement station; (D) the BFree system in the wild.

## How it works
For the user (maybe you!), the intermittent-computing aspect is entirely invisible. Internally, the modified CircuitPython interpreter communicates with the BFree shield and decides when to make a so-called "checkpoint." A checkpoint is a snapshot of the program at that point. When the system runs out of power and eventually starts back up, this is the point where the program will resume. The system always continues from the last *successful* checkpoint.
A checkpoint is created by sending the state of the interpreter (such as the current position in the program, the value of the variables, the state of the peripherals, etc.) to the BFree shield, which stores it in non-volatile memory (FRAM). For more details, please check out the complete paper at: https://dl.acm.org/doi/abs/10.1145/3432191 or https://research.tudelft.nl/en/publications/bfree-enabling-battery-free-sensor-prototyping-with-python

## Getting Started
To ditch all the batteries for your next CircuitPython project using BFree you need five things:
1. An [Adafruit Metro M0 Express board](https://www.adafruit.com/product/3505) 
2. A working [BFree shield](hardware/BFree-shield) programmed with the software in [software/nvm-controller](software/nvm-controller).
3. A build of the modified CircuitPyhton interpreter [BFree-core](https://github.com/TUDSSL/BFree-core))
4. An energy harvesting source (such as a small solar panel)
5. A buffer capacitor

The BFree shield is a simple shield-like PCB that mainly holds an MSP430 microcontroller onboard FRAM for non-volatile storage and energy harvesting circuitry. The modified CircuitPython interpreter (BFree-core) can be built and uploaded the same way as the vanilla CircuitPython. For this, we would like to refer you to the [excellent CircuitPython build instructions](https://learn.adafruit.com/building-circuitpython/build-circuitpython). Don't forget to use https://github.com/TUDSSL/BFree-core instead of https://github.com/adafruit/circuitpython.git

### Building the Hardware
All the EAGLE design files and a component list needed to build the BFree shield are availible in (hardware/BFree-shield)[hardware/BFree-shield].

### Building the BFree Shield Software
The [BFree shield sofware](https://github.com/TUDSSL/BFree/tree/main/software/nvm-controller) is build using [MSP430-gcc](https://www.ti.com/tool/MSP430-GCC-OPENSOURCE). To build it install the msp430-gcc toolchain in `/opt` or change the [msp430-toolchain.cmake](software/nvm-controller/msp430-toolchain.cmake) file to point to the toolchain.
Navigate to `software/nvm-controller/`; then it's as simple as running:
```
$ ./configure
$ cd build && make
```
And an elf file named `NVM-Controller.elf` will be generated in `software/nvm-controller/build/` which you can upload to the BFree shield using an MSP430 programmer, or using a MSP430 LaunchPad.

### Building the BFree Core Software
*Note: BFree Core has to be compiled using arm-gcc version 9! (not any higher version), this is due to a limitation in the original CircuitPython project*
To build the BFree version of CircuitPython, navigate to BFree-core and execute the following.
```
$ git submodule update --init --recursive
$ cd ports/atmel-samd
$ make BOARD=metro_m0_express
```
A `firmware.uf2` file will be generated in `ports/atmel-samd/build-metro_m0_express/` which can be uploaded to the Metro M0 Express board by [flashing it using the UF2 Bootloader](https://learn.adafruit.com/installing-circuitpython-on-samd21-boards/installing-circuitpython).

*Note that this is Beta software, so it's recommended to only flash BFree core if you also own a [J-Link](https://www.segger.com/products/debug-probes/j-link/models/j-link-edu/) programmer to recover the device if a bug occurs that prevents the system from entering the bootloader mode!*


## How to Operate BFree
**Just like a regular Metro M0 Express with CircuitPython!**

There is just one caveat when using peripheral devices (such as a sensor) that have a state that is reset when the system reboots. BFree can not know this, it will restore the peripheral interface (such as SPI), but it will not reinitialize the device.
Therefore the only change you need to make to your Python code *if* you have such a peripheral is to add the reinitialization just before the usage of the device. An example of this can be seen in [the LoRa application](https://github.com/TUDSSL/BFree/blob/a541a0d664f71f19883a6698cdb7067a455fbf71/software/applications-and-benchmarks/imwut-app-lora/main.py#L36)

## List of Known Issues
List of all known issues is listed in the [Issues](https://github.com/TUDSSL/BFree/issues) list of this project. If you found a bug or you would like to enhance BFree: [please contribute](#How-to-Contribute-to-this-Project) - we look forward to your pull requests!

## How to Contribute to this Project
We look forward to your contributions, improvements, additions and changes. Please follow the standard GitHub flow for code contributions. In macro terms this means the following.

1. Fork the master branch of this repository; make sure that your fork will be up to date with the latest master branch.
2. Create an issue here with a new feature or a bug report.
3. Perform changes on your local branch and push them to your forked clone.
4. Create a pull request referencing the issue it covers and wait for our response.


## Frequently Asked Questions

## How to Cite This Work

The results of this project have been published in a peer-reviewed academic publication (from which all technical figures in this file originate). Details of the publication are as follows.

* **Authors and the project team:** [Vito Kortbeek](https://www.vitokortbeek.com/), [Abu Bakar](http://www.abubakar.info/), [Stefany Cruz](https://www.linkedin.com/in/stefany-cruz-1386b4147/), [Kasim Sinan Yildirim](https://sinanyil81.github.io/), [Przemysław Pawełczak](http://www.pawelczak.net/), [Josiah Hester](https://josiahhester.com/)
* **Publication title:** _BFree: Enabling Battery-Free Sensor Prototyping with Python_
* **Pulication venue:** [Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Volume X, Issue Y, Z X]() and [Proceedings of ACM UbiComp 2021](https://ubicomp.org/ubicomp2021/)
* **Link to publication:** [to be added] (Open Access)
* **Link to ACM UbiComp 2021 conference presentation video:** [to be added]

To cite this publication please use the following BiBTeX entry.

```
@article{kortbeek:imwut:2020:bfree,
  title = {BFree: Enabling Battery-Free Sensor Prototyping with Python},
  author = {Vito {Kortbeek} and Abu {Bakar} and Stefany {Cruz} and Kas{\i}m Sinan {Y{\i}ld{\i}r{\i}m} and Przemys{\l}aw {Pawe{\l}czak} and Josiah {Hester}},
  journal = {Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.},
  volume = {},
  number = {},
  pages = {--},
  year = {2020},
  publisher = {ACM}
}
```

## Acknowledgments

This research project was supported by [Netherlands Organisation for Scientific Research](https://www.nwo.nl/en), partly funded by the [Dutch Ministry of Economic Affairs and Climate Policy](https://www.government.nl/ministries/ministry-of-economic-affairs-and-climate-policy), through [TTW Perspective program ZERO (P15-06)](https://www.zero-program.nl/) within Project P4, and by the [National Science Foundation](https://www.nsf.org/) through grants [CNS-1850496](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1850496), [CNS-2032408](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2032408) and [CNS-2038853](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2038853). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

BFree was designed at [Northwestern University](https://www.northwestern.edu) in the US and [Delft University of Technology](https://www.tudelft.nl) in the Netherlands, whose both support is also greatly acknowledged. 

<a href="https://www.northwestern.edu"><img src="https://github.com/TUDSSL/BFree/blob/main/doc-images/northwestern_logo.jpg" width="300px"></a><a href="https://www.tudelft.nl"><img src="https://github.com/TUDSSL/BFree/blob/main/doc-images/tudelft_logo.png" width="300px"></a>

## Copyright

Copyright (C) 2020 TU Delft Embedded and Networked Systems Group/Sustainable Systems Laboratory.

MIT Licence. See [license](master/LICENSE) file for details.
