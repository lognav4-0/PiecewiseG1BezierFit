#!/usr/bin/env python3
print("aqui")
from iguess0 import iguess0

def BezierFitDemo(Q, n):
    k = None
    print("Q: ", Q)
    print("n: ", n)
    Qt = Q.T
    print("Qt: ", Qt)
    ctrl_pts = iguess0(Qt, n, k)
    return ctrl_pts

if __name__ == '__main__':
    BezierFitDemo()