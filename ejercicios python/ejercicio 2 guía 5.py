matriz = [[0 for i in range(4)] for i in range(4)]

for i in range(4):
    matriz[i][4 - 1 - i] = 1

for fila in matriz:
    print(fila)