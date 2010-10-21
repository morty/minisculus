#!/usr/bin/env python

import unittest
import httplib
import json

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

    def encode(self, message):
        return "".join(self.encodeLetter(x) for x in message)

    def encodeLetter(self, letter):
        index = (self.cipher.index(letter) + self.setting) % len(self.cipher)
        return self.cipher[index]

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

if __name__ == '__main__':
    #unittest.main()
    mark1 = MarkI(6)
    encoded = mark1.encode('Strong NE Winds!')
    body = json.dumps({'answer': encoded})
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

    conn = httplib.HTTPConnection('minisculus.edendevelopment.co.uk')
    conn.request('PUT', '/14f7ca5f6ff1a5afb9032aa5e533ad95', body, headers)
    resp = conn.getresponse()
    if resp.status == 303:
        print "New location = %s" % resp.getheader('location')
    else:
        print "Error"