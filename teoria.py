from functools import reduce
##Filtrar os numeros da lista
def problema(numeros):
    #Dobrar cada número
    dobro = list(map(lambda x: x * 2, numeros))

    # Filtrar números pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    #Soma total
    soma_total = reduce(lambda acc, x: acc + x, numeros, 0)

    #Média
    media = soma_total / len(numeros) if numeros else 0

    return dobro, pares, soma_total, media

# Exemplo de uso
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6]

    print("Solução Funcional:")
    res_funcional = problema(numeros)
    print(f"Dobro: {res_funcional[0]}")
    print(f"Pares: {res_funcional[1]}")
    print(f"Soma total: {res_funcional[2]}")
    print(f"Média: {res_funcional[3]}")

# Vantagens da programação funcional:
# Menor quantidade de código: Uso de map, filter e reduce simplifica a manipulação de dados.
# Leitura clara: Expressões lambda tornam o propósito de cada operação mais evidente.
# Modularidade: Cada operação é independente e reutilizável.
