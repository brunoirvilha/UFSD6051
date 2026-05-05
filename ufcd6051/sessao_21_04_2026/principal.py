# ciclo principal
while True:
    # dados de entrada
    # janela com valores em percentagem
    janela1 = 50 #valor pode ir de 0%a 100%
    janela2 = 40 #alor pode ir de 0%a 100%

    #processamento
    
    # janela> 10 significa que quero verificar
    #se a janela naõ está totalmente fechada
    if janela1 > 10 and janela1 < 90:
        print("A janela 1 está ok")
    else:
        print("A janela 1 erro")

     # janela 2


    if janela2 > 10 and janela2 < 90:
        print("A janela 2 está ok")
    else:
        print("A janela 2 erro")