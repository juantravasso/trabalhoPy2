n = int(input("Quantos números gostaria de inserir? "))

maior = None
menor = None

for i in range(n):
    numero = float(input(f"Digite o número {i + 1}: "))

    if numero <= 0:
        print("Você digitou um número negativo ou zero. O programa será finalizado.")
        break

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

if maior is not None and menor is not None:
    print(f"O maior número digitado é: {maior}")
    print(f"O menor número digitado é: {menor}")