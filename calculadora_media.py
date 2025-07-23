def main():
    nota_1 = 7.5
    nota_2 = 8.0
    nota_3 = 6.5

    media = (nota_1 + nota_2 + nota_3) / 3

    print("="*30)
    print(f"{'Notas do aluno':^30}")
    print("="*30)
    print(f"{'Nota 1':<20}: {nota_1:.2f}")
    print(f"{'Nota 2':<20}: {nota_2:.2f}")
    print(f"{'Nota 3':<20}: {nota_3:.2f}")
    print("-"*30)
    print(f"{'Média das notas':<20}: {media:.2f}")
    print("="*30)


main()
