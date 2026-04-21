#ciclo principal
while True:
    #dados de entrada:
    interrupetor_A = False
    interrupetor_B = True
    
    #processamento
    if(not interrupetor_A and interrupetor_B) or (interrupetor_A and not interrupetor_B):
        ligar_luz = True
    else:
        ligar_luz = False
    if interrupetor_A ^interrupetor_B:
        ligar_luz = True
     else:
        ligar_luz = False