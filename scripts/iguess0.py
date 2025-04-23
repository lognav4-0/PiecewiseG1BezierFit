import numpy as np
import matplotlib.pyplot as plt

from pltC import pltC
from defk import defk
from tang import tang
from ctpts import ctpts
from knots import knots
from distEJL import distEJL
from automatic_knots import automatic_knots



def iguess0(Q,k):
    r, m = Q.shape
    n = automatic_knots(Q)
    # Q = datapoints (2xm)
    # n = The number of knotpoints
    # k = default knot positions (indices 1...m)
    if k is None:
        k = defk(m, n)  # Calls for default knot position.
    dpkpc = k  # Position of knot points passed globally.
    P = knots(Q, k)  # call to compute the knotpoints.
    print("Knots: ", P.T)
    dt = distEJL(P, n)  # Call to compute the distance between successive knot points.
    ang = tang(Q, k)  # Call to compute the angles for the unit tangent vectors.
    C = ctpts(P, ang, dt)  # Call to compute the control points for the curve.
    CT = C.T
    print("Control: ", CT)

    unique_control = CT[~np.isin(CT, P).all(axis=1)]

    # Keep the second and penultimate point
    ctrl_pts = np.concatenate((unique_control[1:2], unique_control[-2:-1]))
    # Removing commun points
    # Removing the first and last point
    ctrl_pts = np.array(unique_control)
    print("ctrl_pts =", ctrl_pts)
    return ctrl_pts
    