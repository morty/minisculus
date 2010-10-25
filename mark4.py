#!/usr/bin/env python

from mark1 import MarkI
from mark2 import MarkII

class MarkIV(MarkI):
    def __init__(self, setting_1, setting_2):
        self.wheels = MarkII(setting_1, setting_2)
        self.setting = 0

    def get_setting(self):
        return self.setting

    def increment_setting(self, increment_value):
        self.setting += increment_value

    def encodeLetter(self, letter):
        partial = self.wheels.encode(letter)
        result = MarkI(self.setting).encode(partial)
        self.setting = self.cipher.index(result)
        return result
