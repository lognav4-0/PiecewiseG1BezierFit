import numpy as np
import matplotlib.pyplot as plt

from pltC import pltC
from defk import defk
from tang import tang
from ctpts import ctpts
from knots import knots
from distEJL import distEJL
from automaticKnots import automaticKnots


def iguess0(Q, space_between_knots):
    r, m = Q.shape

    # Q = datapoints (2xm)
    # n = The number of knotpoints
    # k = default knot positions (indices 1...m)
    n = automaticKnots(Q, space_between_knots)  # Agora 'n' é calculado automaticamente
    k = np.linspace(0, m - 1, n, dtype=int)  # Distribuir 'n' nós ao longo dos índices de Q
      # Guardar a posição dos pontos dos nós
    dpkpc = k  # Position of knot points passed globally.
    P = knots(Q, k)  # call to compute the knotpoints.
    print("Knots: ", P.T)
    dt = distEJL(P, n)  # Call to compute the distance between successive knot points.
    ang = tang(Q, k)  # Call to compute the angles for the unit tangent vectors.
    C = ctpts(P, ang, dt)  # Call to compute the control points for the curve.
    CT = C.T
    print("Control: ", CT)

    unique_control = CT[~np.isin(CT, P).all(axis=1)]

    # Manter o segundo e penúltimo ponto
    ctrl_pts = np.concatenate((unique_control[1:2], unique_control[-2:-1]))

    # Removendo os pontos comuns
    # Removendo o primeiro e último ponto
    ctrl_pts = np.array(unique_control)
    

    pltC(C, Q, P)  # Call to plot the initial guess curve, its control polygon, and points in Q.
    plt.gcf()
    plt.title('Plot of Initial Guess curve')
    plt.show()

    # Assemble the composite vector of the initial guess curve parameters
    #IG = np.concatenate((P[0], P[1], ang, dt[0], dt[1]))
    nonzero_ang = np.nonzero(ang)[0]
    IG = np.concatenate((P[0, :], P[1, :], ang[nonzero_ang], dt[0, :], dt[1, :]), axis=0)
    # 3 termos de P, 3 termos de P, 3 termos de ang, 2 termos de dt
    return IG, k, dpkpc

