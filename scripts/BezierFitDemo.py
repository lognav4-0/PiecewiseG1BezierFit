import numpy as np
from iguess0 import iguess0

def BezierFitDemo(Q):
    k = None
    Qt = Q.T
    ctrl_pts = iguess0(Qt, k)
    return ctrl_pts
if __name__ == '__main__':
    BezierFitDemo()