def main():
    valor_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    valor_dolares = valor_reais / taxa_dolar
    valor_euros = valor_reais / taxa_euro

    print(f"Valor em Reais: R$ {valor_reais:.2f}")
    print(f"Valor em Dólares: $ {valor_dolares:.2f}")
    print(f"Valor em Euros: € {valor_euros:.2f}")

main()