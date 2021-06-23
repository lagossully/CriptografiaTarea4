import socket
import math
import random
from random import shuffle
import sys
from time import time


class PrivateKey(object):
    def __init__(self, p, q, n):
        self.l = (p-1) * (q-1)
    def __repr__(self):
        return '<PrivateKey: %s %s>' % (self.l)

class PublicKey(object):

    def from_n(cls, n):
        return cls(n)
    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1
    def __repr__(self):
        return '<PublicKey: %s>' % self.n

    


host = '127.0.0.1'
port = 50557
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))