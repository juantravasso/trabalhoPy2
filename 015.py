n = int(input("Quantos números você deseja digitar? "))

if n <= 0:
    print("A quantidade de números deve ser maior que zero. Programa finalizado.")
else:
    maior = float('-inf')
    menor = float('inf')

    for i in range(n):
        numero = float(input(f"Digite o {i+1}º número: "))

        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    if maior == menor:
        print("Todos os números digitados são iguais.")
    else:
        print(f"O maior número digitado foi: {maior}")
        print(f"O menor número digitado foi: {menor}")