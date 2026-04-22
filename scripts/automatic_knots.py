import numpy as np

def load_points_of_file(file):
    #Load data of text file
    Q = np.loadtxt(file, delimiter=',', ndmin=2)
    return Q

def automatic_knots(Q, space_between_knots = 1):  
    if Q.ndim != 2:
        raise ValueError("Expected a 2D array of points")

    points_num = Q.shape[1] if Q.shape[0] == 2 else Q.shape[0]
    if points_num < 5:
        raise ValueError(f"Need at least 5 points to fit the Bezier curve, got {points_num}")

    if Q.shape[0] == 2:
        segments = np.diff(Q, axis=1)
        segment_lengths = np.linalg.norm(segments, axis=0)
    else:
        segments = np.diff(Q, axis=0)
        segment_lengths = np.linalg.norm(segments, axis=1)

    total_distance = np.sum(segment_lengths)

    # Calculate the number of knot points from the actual path length.
    n = int(round(total_distance / space_between_knots))
    n = max(2, min(points_num, n))

    return n

