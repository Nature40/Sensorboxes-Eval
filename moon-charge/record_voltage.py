#!/usr/bin/env python3

import struct
from smbus import SMBus


import sys
import time

MAX17040_I2C_ADDR = 0x36


class MAX17040():
    def __init__(self, smbus: SMBus, i2c_addr=MAX17040_I2C_ADDR, **kwargs):
        self.smbus = smbus
        self.i2c_addr = i2c_addr

    @property
    def voltage(self):
        read = self.smbus.read_word_data(self.i2c_addr, 2)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        return swapped * 1.25 / 1000 / 16

    @property
    def capacity(self):
        read = self.smbus.read_word_data(self.i2c_addr, 4)
        swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        return swapped / 256


if __name__ == "__main__":
    bus = SMBus(1)
    max17040 = MAX17040(bus)
    print("ts,voltage,capacity")
    while True:
        print(f"{time.time()},{max17040.voltage},{max17040.capacity}")
        time.sleep(10)
