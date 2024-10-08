maior = float('-inf')
menor = float('inf')

for i in range(200):
    numero = float(input(f"Digite o {i+1}º número: "))

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")