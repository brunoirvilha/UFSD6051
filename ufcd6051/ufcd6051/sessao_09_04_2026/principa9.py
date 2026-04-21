# ciclo de entrada

while True:
    #dados de entrada:
    sensor_luminosidade1 = 90
    sensor_luminosidade2 = 80
    sensor_luminosidade3 = 70   
    sensor_luminosidade4 = 60
    
    #processamento:
    if sensor_luminosidade1 <20 or sensor_luminosidade2 <20 or sensor_luminosidade3 <20 or sensor_luminosidade4 <20:
        liar_luz = True
    else:
        liar_luz = False