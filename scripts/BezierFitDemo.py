import numpy as np
from iguess0 import iguess0



def read_points_from_file(file_path):
            path_coords = np.empty((0, 2))
            with open(file_path, 'r') as f:
                for line in f:
                    x, y = line.strip().split(',')
                    point = np.array([[float(x), float(y)]])
                    path_coords = np.append(path_coords, point, axis=0)
            return path_coords


def BezierFitDemo():
    # Demonstrate two different Bezier curve fits
    # Array Q is the set of data points to which we want to fit
    # a piecewise G1 continuous cubic Bezier curve
    # (Replace Q with your data.  You will need to adjust n = number of knots)

    
    k = None
    n = None
            
    Q = read_points_from_file(file_path="/home/henrique/lognav_ws/src/lognav/teach_and_repeat/src/PiecewiseG1BezierFit/scripts/test_path.txt")
    
    Qt = Q.T
    ctrl_pts = iguess0(Qt, n, k)
    print(f"Qt = {Qt}")
    print(f"ctrl_pts bezier  = {ctrl_pts}")
    return ctrl_pts
    
    
if __name__ == '__main__':
    BezierFitDemo()