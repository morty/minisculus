#!/usr/bin/env python

from mark1 import MarkI
from mark2 import MarkII
from util import send_answer

class MarkIV(MarkI):
    def __init__(self, setting_1, setting_2):
        self.wheels = MarkII(setting_1, setting_2)
        self.setting = 0

    def encodeLetter(self, letter):
        partial = self.wheels.encode(letter)
        result = super(MarkIV, self).encodeLetter(partial)
        self.setting = self.cipher.index(letter) * 2
        return result

    def decodeLetter(self, letter):
        partial = super(MarkIV, self).decodeLetter(letter)
        result = self.wheels.decode(partial)
        self.setting = self.cipher.index(result) * 2
        return result

if __name__ == '__main__':
    mark4 = MarkIV(4, 7)
    encoded = mark4.encode('The white cliffs of Alghero are visible at night')
    send_answer(encoded, '/36d80eb0c50b49a509b49f2424e8c805')

    mark4 = MarkIV(7, 2)
    decoded = mark4.decode("""WZyDsL3u'0TfxP06RtSSF 'DbzhdyFIAu2 zF f5KE"SOQTNA8A"NCKPOKG5D9GSQE'M86IGFMKE6'K4pEVPK!bv83I""")
    send_answer(decoded, '/4baecf8ca3f98dc13eeecbac263cd3ed')

    for i in range(10):
        for j in range(10):
            mark4 = MarkIV(i, j)
            decoded = mark4.decode("""QT4e8MJYVhkls.27BL9,.MSqYSi'IUpAJKWg9Ul9p4o8oUoGy'ITd4d0AJVsLQp4kKJB2rz4dxfahwUa"Wa.MS!k4hs2yY3k8ymnla.MOTxJ6wBM7sC0srXmyAAMl9t"Wk4hs2yYTtH0vwUZp4a"WhB2u,o6.!8Zt"Wf,,eh5tk8WXv9UoM99w2Vr4!.xqA,5MSpWl9p4kJ2oUg'6evkEiQhC'd5d4k0qA'24nEqhtAQmy37il9p4o8vdoVr!xWSkEDn?,iZpw24kF"fhGJZMI8nkI""")
            if 'FURLIN' in decoded and 'BUNKER' in decoded:
                print decoded
                print "%d, %d" % (i, j)
