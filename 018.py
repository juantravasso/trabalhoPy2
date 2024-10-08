n = int(input("Quantos produtos você gostaria de inserir? "))

if n <= 0:
    print("A quantidade de produtos deve ser maior que zero. Programa finalizado.")
else:
    for i in range(n):
        print(f"\nProduto {i+1}:")

        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade vendida: "))

        preco_total = preco * quantidade

        print(f"O produto {nome} (Código: {codigo}) teve um total de vendas de: R$ {preco_total:.2f}")