# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Light Up all Neopixels Burple (grow light color)"""
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    cp.pixels[0] = (214, 83, 211)
    cp.pixels[1] = (84, 64, 205)
    cp.pixels[2] = (214, 83, 211)
    cp.pixels[3] = (84, 64, 205)
    cp.pixels[4] = (214, 83, 211)
    cp.pixels[5] = (284, 64, 205)
    cp.pixels[6] = (214, 83, 211)
    cp.pixels[7] = (84, 64, 205)
    cp.pixels[8] = (214, 83, 211)
    cp.pixels[9] = (84, 64, 205)
