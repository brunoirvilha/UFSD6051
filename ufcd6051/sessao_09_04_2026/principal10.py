# ciclo de entrada

while True:
    # dados de entrada:
    sensor_de_humidade = 10
    planta2 = 2
    temporizador = 3

    # processamento:
    if sensor_de_humidade < 20 and planta2 == 2 and temporizador > 3:
        ligar_bomba = True
    else:
        ligar_bomba = False