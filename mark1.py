#!/usr/bin/env python

from util import send_answer

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

if __name__ == '__main__':
    mark1 = MarkI(6)
    encoded = mark1.encode('Strong NE Winds!')
    send_answer(encoded, '/14f7ca5f6ff1a5afb9032aa5e533ad95')
