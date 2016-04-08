# -*- coding:utf-8 -*-

class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        if lena!=lenb:
            return False
        ss = A+A
        if B in ss:
            return True
        else:
            return False

m = Rotation()
h = m.chkRotation('sdfg',4,'ffgs',4)
print h