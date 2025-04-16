import numpy as np

def load_points_of_file(file):
    # Carrega os dados do arquivo de texto
    Q = np.loadtxt(file, delimiter=',', ndmin=2)
    return Q

def automatic_knots(Q, space_between_knots = 1):  
    points_num = len(Q)  # Número de pontos (linhas da matriz)
    total_distance = 0   # Começa em 0 porque ainda não foi percorrida

    # Distância euclidiana entre os pontos
    for i in range(points_num - 1):  
        p1, p2 = Q[i], Q[i + 1]  
        total_distance += np.linalg.norm(p2 - p1)  

    # Calcula o número de nós baseado na distância total
    n = int(round(total_distance / space_between_knots))
    
    
    return n

