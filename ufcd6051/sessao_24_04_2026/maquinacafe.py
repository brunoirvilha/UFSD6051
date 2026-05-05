config  = {
    "produtos" : {
        "cafe": {
            "preco": 0.5,
            "tem palheta": True,
            "nivel de acucar": 2,
            "tem copo": True,
            "botao_cafe":"periferico_1",
        },
        "café longo": {
            "preco": 0.5,
        },
        "chá": {
            "preco": 0.5,
            "tem palheta": True,
            "nivel de acucar": 2,
            "tem copo": True,
             "botao_cha":"periferico_2",
        },
        "capuccino": {
            "preco": 0.5,
            "tem palheta": True,
            "nivel de acucar": 2,
            "tem copo": True,
             "botao_capuccino":"periferico_3",
        },
        "chocolate quente": {
            "preco": 0.5,
            "tem palheta": True,
            "nivel de acucar": 2,
            "tem copo": True,
             "botao_chocolate_quente":"periferico_4",
        }
        }
    }




config["produtos"]
config["produtos"]["café"]

config_da_maquina = {
    "velocidade"
}

#ciclo principal
while True:
    # dados de entrada
    velocidade_da_maquina = config_da_maquina["velocidade"]

    # processamento
    if botao_cafe and dinheiro_certo:
        if config["produtos"][cafe]["tem_copo"]:
            colocar_copo()
        else nao_colocar_copo()

    if botao_cafe_longo and dinheiro_certo:
        if config["produtos"][cafe_longo]["tem_copo"]:
            colocar_copo()
        else nao_colocar_copo()
    
    if botao_cha and dinheiro_certo:
        if config["produtos"][cha]["tem_copo"]:
            colocar_copo()
        else nao_colocar_copo()
    
    if botao_capuccino and dinheiro_certo:
        if config["produtos"][capuccino]["tem_copo"]:
            colocar_copo()
        else nao_colocar_copo()
    
    if botao_chocolate_quente and dinheiro_certo:
        if config["produtos"][chocolate_quente]["tem_copo"]:
            colocar_copo()
        else nao_colocar_copo()
    
    
    
    
    
    
    
    :
        def colocar_copos():
            """codigo para pedir a maquina para tirar o copo """
            print("tirara o copo")
            ")"""