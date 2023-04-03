---
title: Building the Debug probe
description: Talking through building my debug probe
publishedDate: 2023/01/04
lastEdited: 2023/03/04
---
# Going off piece.
The video guide i'm following uses an Arduino Mega compatible board. However I don't have one of those, so instead I'm building my own solution with a Raspberry Pi Pico with CircuitPython instead

# Challenges presented by using this stack
## Hardware
* GPIO pins only take upto 3.3v, the 6502 runs on and uses 5v
* There is no easy way to plug stuff in

## Software
* CircuitPython doesn't support Hardware Interupts

# Fixing these challenges
## Hardware
### Not supporting 5v
I'm going to solve this issue by employing an army of LM1117 This will work because we don't need to worry about what is on those pins. we only care about if those pins are powered or not powered

### No easy way to plug stuff in
I'm going to solve this by building a custom PCB allowing me to have it wired how it should be and have the outputs be accessible via female headers

## Software
### Circuitpython doesn't support hardware interupts
Because I'm already reading the clock pin for signal, I can do a simple check at the top of the loop, with 1 condition which is to continue if that pin is powered. else continue the loop

# Schematics
## V1
![V1](https://8bitproject.sean.cyou/images/probe-schematics/v1.png)

## V2
![V2](https://8bitproject.sean.cyou/images/probe-schematics/v2.png)

# PCB
## V1
![V1](https://8bitproject.sean.cyou/images/probe-pcbs/v1.png)

# IMPORTANT EDIT
I recently went to put this into production. But after checking the price I have decided it would be more economically friendly to buy an arduino mega clone