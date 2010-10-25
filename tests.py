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

    def testQuestionOne(self):
        mark1 = MarkI(6)
        self.assertEquals(mark1.encode('Strong NE Winds!'), 'Yzxutm5TK5cotjy2')

    def testDecodeLetter(self):
        self.assertEquals(self.mark1.decode('f'), 'a')
        self.assertEquals(self.mark1.decode('h'), 'c')
        self.assertEquals(self.mark1.decode('1'), '!')

    def testDecodeString(self):
        self.assertEquals(self.mark1.decode('cC,'), 'X7w')
        

class TestMarkII(unittest.TestCase):
    def setUp(self):
        self.mark2 = MarkII(2, 5)

    def testExample(self):
        self.assertEquals(self.mark2.encode('a'), 'S')
        self.assertEquals(self.mark2.encode('b'), 'T')
        self.assertEquals(self.mark2.encode('c'), 'U')
        self.assertEquals(self.mark2.encode('abc'), 'STU')

    def testQuestionTwo(self):
        mark2 = MarkII(9, 3)
        self.assertEquals(mark2.encode('The Desert Fox will move 30 tanks to Calais at dawn'),
                          'Wkh2Ghvhuw2Ir.2zloo2pryh2632wdqnv2wr2Fdodlv2dw2gdzq')

    def testDecodeLetter(self):
        self.assertEquals(self.mark2.decode('S'), 'a')
        self.assertEquals(self.mark2.decode('T'), 'b')
        self.assertEquals(self.mark2.decode('U'), 'c')
        self.assertEquals(self.mark2.decode('STU'), 'abc')

class TestMarkIV(unittest.TestCase):
    def setUp(self):
        self.mark2 = MarkII(4, 7)
        self.mark4 = MarkIV(4, 7)

    def testInitialEncode(self):
        self.assertEquals(self.mark4.encode('H'), 
                          self.mark2.encode('H'),
                          "Initial encoding of MarkIV should be the same as the MarkII")

    def testSecondEncode(self):
        self.assertNotEquals(self.mark4.encode('HE'), 
                             self.mark2.encode('HE'),
                             "Second encoding of MarkIV should be different from the MarkII")

    def testQuestionThree(self):
        self.assertEquals(self.mark4.encode('The white cliffs of Alghero are visible at night'),
                          'JMl0kBp?20QixoivSc.2"vvmls8KOk"0jA,4kgt0OmUb,pm.')

if __name__ == '__main__':
    unittest.main()
