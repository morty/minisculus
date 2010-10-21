#!/usr/bin/env python

import unittest

from mark1 import MarkI
from util import send_answer

class MarkII(object):
    def __init__(self, setting_1, setting_2):
        self.wheel_1 = MarkI(setting_1)
        self.wheel_2 = MarkI(setting_2 * -2)

    def encode(self, message):
        return self.wheel_2.encode(self.wheel_1.encode(message))

class TestMarkII(unittest.TestCase):
    def testExample(self):
        mark2 = MarkII(2, 5)
        self.assertEquals(mark2.encode('a'), 'S')
        self.assertEquals(mark2.encode('b'), 'T')
        self.assertEquals(mark2.encode('c'), 'U')
        self.assertEquals(mark2.encode('abc'), 'STU')

if __name__ == '__main__':
    #unittest.main()
    mark2 = MarkII(9, 3)
    encoded = mark2.encode('The Desert Fox will move 30 tanks to Calais at dawn')
    send_answer(encoded, '/2077f244def8a70e5ea758bd8352fcd8')
