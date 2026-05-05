# operações com numeros
# *

iva = 1.23
preco = 10

preco_com_iva = preco * iva
print(preco_com_iva)

# media
# +/
segunda = 25
terca = 15
quarta = 14
quinta = 7
sexta = 10
numero_de_dias = 5
media = (segunda + terca + quarta + quinta + sexta) / numero_de_dias
print(media)

testar_numero_de_vendas = quarta -media
#verificar se o dia foi bom
if testar_numero_de_vendas > media:
    print("O dia foi bom") 
else:    print("O dia foi ruim")