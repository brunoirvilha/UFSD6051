#correca do teste

#ciclo principal

while True:
    #dados de entrada
    #respostas do teste em percentagem
    resposta1 = 25  #valor pode ir de 0%a 100%
    resposta2 = 25  #valor pode ir de 0%a 100%
    resposta3 = 25  #valor pode ir de 0%a 100%
    resposta4 = 25  #valor pode ir de 0%a 100%

    #nota final = resposta1 + resposta2 + resposta3 + resposta4
    #processamento

    while True:
        if resposta1 + resposta2 + resposta3 + resposta4 == 100:
            print("Nota final: ", resposta1 + resposta2 + resposta3 + resposta4)
            break
        else:
            print("As respostas devem totalizar 100%")
            break   