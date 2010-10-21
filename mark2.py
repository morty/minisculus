#!/usr/bin/env python

import unittest

from mark1 import MarkI

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
    unittest.main()
