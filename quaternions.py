import math
import matplotlib.pyplot as plt

class Quaternion:
    def __init__(self, real, i, j, k):
        self.real = real
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return '%d + %di + %dj + %dk' % (self.real, self.i, self.j, self.k)

    def conjugate(self):
        conjugate = Quaternion(self.real, -1*self.i, -1*self.j, -1*self.k)
        return conjugate

    def norm(self):
        norm = math.sqrt((self.real)**2 + (self.i)**2 + (self.j)**2 + (self.k)**2)
        return norm

    def __add__(self, other):
        return Quaternion(self.real+other.real, self.i+other.i, self.j+other.j, self.k+other.k)

    def __sub__(self,other):
        return Quaternion(self.real-other.real, self.i-other.i, self.j-other.j, self.k-other.k)

    def __mul__(self, other):
        if type(other)==type(self):
            real = self.real*other.real - self.i*other.i - self.j*other.j - self.k*other.k
            i = self.real*other.i + self.i*other.real + self.j*other.k - self.k*other.j
            j = self.real*other.j - self.i*other.k + self.j*other.real + self.k*other.i
            k = self.real*other.k + self.i*other.j - self.j*other.i + self.k*other.real
            return Quaternion(real,i,j,k)
        elif type(other)==type(1) or type(other)==type(1.0): #right scalar mult
            return Quaternion(self.real*other, self.i*other, self.j*other, self.k*other)

    def __rmul__(self, other): #left scalar mult
        return self.__mul__(other)

    def __div__(self, other):
        if self.norm() != 0:
            if type(other)==type(self):
                real = (self.real*other.real + self.i*other.i + self.j*other.j + self.k*other.k)/(other.norm()**2)
                i = (self.real*other.i - self.i*other.real - self.j*other.k + self.k*other.j)/(other.norm()**2)
                j = (self.real*other.j - self.i*other.k + self.j*other.real + self.k*other.i)/(other.norm()**2)
                k = (self.real*other.k + self.i*other.j - self.j*other.i + self.k*other.real)/(other.norm()**2)
                return Quaternion(real,i,j,k)
            elif type(other)==type(1) or type(other)==type(1.0):
                return Quaternion(self.real/other, self.i/other, self.j/other, self.k/other)

    def versor(self):
        return self/self.norm()

    def inverse(self):
        return self.conjugate()/(self.norm()**2)

    def make_list(self):
        l = [self.real, self.i, self.j, self.k]
        return l




