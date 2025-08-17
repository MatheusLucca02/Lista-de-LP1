# questão 3 - Soma de 5 valores

lista_numeros = []
for x in range(0, 5):

    numero = int(input("Digite um numero : "))
    lista_numeros.append(numero)

print(f"A soma desses 5 numeros eh: {sum(lista_numeros)}")
