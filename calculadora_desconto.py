def main():
    nome_produto = "Camiseta"
    preco_original = 50.00
    desconto = 0.20  # 20% de desconto

    preco_com_desconto = preco_original * (1 - desconto)

    print("="*40)
    print(f"{'Produto':<20}: {nome_produto}")
    print(f"{'Preço original':<20}: R$ {preco_original:>2.2f}")
    print(f"{'Desconto':<20}: {desconto * 100:>7.0f}%")
    print(f"{'Preço com desconto':<20}: R$ {preco_com_desconto:>2.2f}")
    print("="*40)


main()