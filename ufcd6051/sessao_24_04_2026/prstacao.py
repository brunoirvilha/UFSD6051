# credito habitacao
#100000 euros:
# taxa de juro anual: 1.39%
# prazo: 480 meses

# valor da prestação mensal
# valor total pago
# valor total pago em juros

valor_emprestimo = 100000
taxa_juros_anual = 1.39
prazo_meses = 480
taxa_juros_mensal = taxa_juros_anual / 12 / 100
prestacao_mensal = 100000 * 1.39 / (1 - (1 + 1.39) ** -480)

total_pago = 314 * 480