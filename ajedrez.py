
casillas_vacias = "[ ]"
casillas_llenas = "[x]"
tablero_3 = []

for i in range(1, 9): #del 1 al 8
    fila = []
    if i == 1:
        for x in range(8):
            fila.append(casillas_llenas)
    elif i == 2:
        for x in range(8):
            fila.append(casillas_llenas)
    elif i == 7:
        for x in range(8):
            fila.append(casillas_llenas)
    elif i == 8:
        for x in range(8):
            fila.append(casillas_llenas)
    else :
        for x in range(8):
            fila.append(casillas_vacias)

    tablero_3.append(fila)

for fila in tablero_3:
    print(fila)
