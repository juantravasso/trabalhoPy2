n = int(input("Quantos números gostaria de inserir? "))

maior = None
menor = None

for i in range(n):
    numero = float(input(f"Digite o número {i + 1}: "))

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
