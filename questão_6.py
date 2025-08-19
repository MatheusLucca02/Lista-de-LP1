# Questão 6 - Identificação de numeros primos

def numeros_primos(numero):

    if numero <= 1:
        return False

    for x in range(2, numero):

        if numero % x == 0:
            return False

    return True


# Testando a função
print(f"O número 17 é primo ? {numeros_primos(17)}")
print(f"O número 27 é primo ? {numeros_primos(27)}")
print(f"O número 2 é primo ? {numeros_primos(2)}")
print(f"O número 5 é primo ? {numeros_primos(5)}")
print(f"O número 10 é primo ? {numeros_primos(10)}")
