#!/usr/bin/env python

import unittest

from mark1 import MarkI
from mark2 import MarkII

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

if __name__ == '__main__':
    unittest.main()
