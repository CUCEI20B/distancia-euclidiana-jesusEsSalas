import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    print(distancia)

distancia_euclidiana(500, 500, 200, 200)