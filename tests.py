#!/usr/bin/env python

import unittest

from mark1 import MarkI
from mark2 import MarkII
from mark4 import MarkIV

class TestMarkI(unittest.TestCase):
    def setUp(self):
        self.mark1 = MarkI(5)

    def testFirstExample(self):
        self.assertEquals(self.mark1.encode('a'), 'f')
        self.assertEquals(self.mark1.encode('c'), 'h')

    def testEncodeBang(self):
        self.assertEquals(self.mark1.encode('!'), '1')

    def testEncodeString(self):
        self.assertEquals(self.mark1.encode('X7w'), 'cC,')

class TestMarkII(unittest.TestCase):
    def testExample(self):
        mark2 = MarkII(2, 5)
        self.assertEquals(mark2.encode('a'), 'S')
        self.assertEquals(mark2.encode('b'), 'T')
        self.assertEquals(mark2.encode('c'), 'U')
        self.assertEquals(mark2.encode('abc'), 'STU')

class TestMarkIV(unittest.TestCase):
    def setUp(self):
        self.mark2 = MarkII(4, 7)
        self.mark4 = MarkIV(4, 7)

    def testGetSetting(self):
        self.assertEquals(0, self.mark4.get_setting())

    def testIncrementSetting(self):
        self.mark4.increment_setting(5)
        self.assertEquals(5, self.mark4.get_setting())

    def testInitialEncode(self):
        self.assertEquals(self.mark4.encode('H'), 
                          self.mark2.encode('H'),
                          "Initial encoding of MarkIV should be the same as the MarkII")

    def testSecondEncode(self):
        self.assertNotEquals(self.mark4.encode('HE'), 
                             self.mark2.encode('HE'),
                             "Second encoding of MarkIV should be different from the MarkII")

if __name__ == '__main__':
    unittest.main()
