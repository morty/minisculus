#!/usr/bin/env python

import unittest

class MarkI(object):
    def __init__(self, setting):
        self.setting = setting

    def encode(self, letter):
        return chr(ord(letter) + self.setting)

class TestMarkI(unittest.TestCase):
    def testFirstExample(self):
        mark1 = MarkI(5)
        self.assertEquals(mark1.encode('a'), 'f')
        self.assertEquals(mark1.encode('c'), 'h')

if __name__ == '__main__':
    unittest.main()
