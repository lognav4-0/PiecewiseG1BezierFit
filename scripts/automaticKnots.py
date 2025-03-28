import numpy as np

def load_points_of_file(file):
    # Load data of text file 
    Q = np.loadtxt(file, delimiter=',')
    return Q

def automaticKnots(Q, space_between_knots = 1.0):  
    points_num = len(Q)  # Points number (matrix rows)
    total_distance = 0   # It starts at 0 because it has not been traversed yet.

    # Euclidian distance between points
    for i in range(points_num - 1):  
        p1, p2 = Q[i], Q[i + 1]  
        total_distance += np.linalg.norm(p2 - p1)  

    # Calculates the number of nodes based on the total distance
    n = int(total_distance / space_between_knots)
    
    return n