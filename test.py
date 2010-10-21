#!/usr/bin/env python

import unittest

class MarkI(object):
    cipher = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        ".", ",", "?", "!", "'", "\"", " "
    ]

    def __init__(self, setting):
        self.setting = setting

    def encode(self, letter):
        index = (self.cipher.index(letter) + self.setting) % len(self.cipher)
        return self.cipher[index]

class TestMarkI(unittest.TestCase):
    def testFirstExample(self):
        mark1 = MarkI(5)
        self.assertEquals(mark1.encode('a'), 'f')
        self.assertEquals(mark1.encode('c'), 'h')

    def testEncodeBang(self):
        mark1 = MarkI(5)
        self.assertEquals(mark1.encode('!'), '1')

if __name__ == '__main__':
    unittest.main()
