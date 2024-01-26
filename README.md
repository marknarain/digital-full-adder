# digital-full-adder

Full Adder in Digital Logic

## Overview

I started designing this digital full adder shortly after learning about logic gates. In the beginning I started by drawing a full adder using XOR-gates and and-gates. The next step was to replace all gates with NAND-gates, so I drew a full adder using 9 NAND-gates. After drawing the whole logic with NAND-gates, I designed the circuit using the circuit simulator of HTL Braunau. I have included KiCad files, files for the circuit simulator (link in requirements) and other pictures.

<img src="/full-adder-top.jpg" alt="top-full" width="500" height="auto">

## Module 1: Bipolar transistors:

I built the first module of the full adder using bipolar transistors.
You can find the CircuitSim, the KiCad files and pictures in the folder Transistors.

Materials:
- 19x BC547C: NPN General Purpose Amplifier
-  9x Resistor (10kΩ)
-  3x Resistor (330kΩ)
- 18x Resistor (100kΩ)
-  3x LED (5mm, red)
-  3x Sliding switch
- Copper wire
- Pin headers (angled, 2-row)

<img src="/Transistors/picture-top.jpg" alt="top-transistors" width="auto" height="300"><img src="/Transistors/circuit-diagramm.png" alt="top-transistors" width="auto" height="300">

## Module 2: NAND Gates (74HC 00)

The second module is made by using NAND-Gates. This module can be connected to module 1 or the power supply directly by using the pin headers. 

Materials:
- 3x 74HC00: Quadruple 2-input NAND-gates
- 3x Resistor (330kΩ)
- 3x LED (5mm, red)
- 2x Sliding switch
- Pin headers (angled, 2-row)

<img src="/74HC00/image-top.jpg" alt="top-74HC00" width="auto" height="300"><img src="/74HC00/circuit-diagramm.png" alt="circuit-74HC00" width="auto" height="300">

## Module 3: 4-Bit Binary Full Adder (74HCT283E)

The third module cosist of one 4-Bit Binary Full Adder. 

Materials:
- 1x 74HCT283E: 4-Bit Binary Full Adder with Fast Carry
- 3x Resistor (330kΩ)
- 3x LED (5mm, red)
- 2x Sliding switch
- Pin headers (angled, 2-row)

<img src="/74HCT283E/image-top.jpg" alt="top-74HC00" width="auto" height="300">

## Module 4: Raspberry Pi Pico (RP2040)

Module number 4 is one Raspberry Pi Pico. The code is wirtten in micropython. You can find it underneath the materials. Although using a Raspberry Pi for a single module of a full adder is overkill, I still thought that it'd be a nice extension 🙂.

Materials:
- Raspberry Pi Pico (RP2040)
- 3x Resistor (330kΩ)
- 3x LED (5mm, red)
- 2x Sliding switch
- Pin headers (angled, 2-row)

You can view a simulation of the circuit using this [link](https://wokwi.com/projects/387899070806177793)

Python code:

````Python
from machine import Pin

a = Pin(2, Pin.IN, Pin.PULL_DOWN)
b = Pin(3, Pin.IN, Pin.PULL_DOWN)
cin = Pin(4, Pin.IN, Pin.PULL_DOWN)

s = Pin(9, Pin.OUT)
cout = Pin(10, Pin.OUT)

while True:
    sum_val = a.value() + b.value() + cin.value()
    s.value(sum_val & 1)
    cout.value(sum_val >> 1)
````

<img src="/RP2040/circuit.png" alt="top-74HC00" width="auto" height="300">

## Power supply

The power supply of this device consits of:
- 1x Battery holder
- 1x 9V Battery
- 2x Capacitor (100nF)
- 2x Capacitor (100µF)
- 1x Voltage regulator (-5V, MC7905)
- 2x Sliding switch
- Pin headers (angled, 2-row)

I didn't have a positive voltage regulator (MC7805) at home, so I used the negative one (MC7905).

<img src="/Power supply/power-supply.jpg" alt="top-power" width="auto" height="300"><img src="/Power supply/circuit-diagramm.png" alt="top-power" width="auto" height="300">

## More modules to come...

- FPGA
- MOSFET transistors
- ...

## Requirements

- [KiCad Schematic Editor](https://www.kicad.org/download/)
- [Circuit simulator](https://services01.htl-braunau.at/CircuitSim/)

## Links

Home page: [marknarain.com](https://marknarain.com)
