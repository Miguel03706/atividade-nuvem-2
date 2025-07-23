def main():
    distancia = 300 # Km
    combustivel_utilizado = 25 # Litros

    consumo_medio = distancia / combustivel_utilizado # km/l

    print("="*40)
    print(f"{'Relatório de Consumo':^40}")
    print("="*40)
    print(f"{'Distância percorrida':<25}: {distancia:>5.2f} km")
    print(f"{'Combustível utilizado':<25}: {combustivel_utilizado:>4.2f} litros")
    print(f"{'Consumo médio':<25}: {consumo_medio:>4.2f} km/l")
    print("="*40)

main()
