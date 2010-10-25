#!/usr/bin/env python

from mark1 import MarkI
from mark2 import MarkII
from util import send_answer

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
        result = super(MarkIV, self).encodeLetter(partial)
        self.setting = self.cipher.index(result) * 2
        return result

if __name__ == '__main__':
    mark4 = MarkIV(4, 7)
    encoded = mark4.encode('The white cliffs of Alghero are visible at night')
    send_answer(encoded, '/36d80eb0c50b49a509b49f2424e8c805')
