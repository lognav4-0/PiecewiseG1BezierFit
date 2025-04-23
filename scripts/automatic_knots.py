import numpy as np

def load_points_of_file(file):
    #Load data of text file
    Q = np.loadtxt(file, delimiter=',', ndmin=2)
    return Q

def automatic_knots(Q, space_between_knots = 1):  
    points_num = len(Q)  # Number of points
    total_distance = 0  

    # Euclidian distance between points
    for i in range(points_num - 1):  
        p1, p2 = Q[i], Q[i + 1]  
        total_distance += np.linalg.norm(p2 - p1)  

    # Calculates the number of nodes based on the total distance
    n = int(round(total_distance / space_between_knots))
     
    return n

