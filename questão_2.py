
# Questão 2 - FATORIAL


fatorial = 1
numero = int(
    input("Digite um numero inteiro positivo para o calculo fatorial: "))


if numero == 0:
    print(f"O fatorial de {numero} eh 1")
elif numero < 0:
    print("Entrada inválida, escolha um numeoro inteiro positivo ")
else:

    for x in range(1, numero+1):
        fatorial = fatorial*x

    print(f" O fatorial de {numero} eh {fatorial} ")
