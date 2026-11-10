valor_total = 0
nome_cliente = input("Digite o nome do cliente: ")
nome_vendedor = input("Digite o nome do vendedor: ")
itemVendido = input("Digite o nome do produto comprado: ")
contador = float(input("Qual o valor do produto comprado (pra sair digite 0):"))
possuiMais = input("Possui mais itens? (s/n) ")
print(f"Bem-Vindo(a) {nome_vendedor}.")

#Valor dos produtos
vestido = 330,00
casaco = 300,00
blusa = 110,00
calca = 250,00

while possuiMais == "s":
    produtoComprado = input("Digite o produto comprado: ")
    possuiMais = input("Possui mais itens? (s/n) ")

while contador != 0 :
    valor_total += contador
    contador = float(input("Qual o valor do produto comprado (caso não possua mais produto, digite pra sair 0):"))

    

if valor_total < 0:
    print(f"Valor total (R${valor_total}) inválido.")
elif valor_total > 300 :
    desconto = valor_total * 0.15
    valorFinal = valor_total - desconto
    print(f"O valor total da compra do produto {itemVendido}, do cliente {nome_cliente}, sem o desconto é de R${valor_total}. {nome_cliente} ganhou um desconto de 15% do(a) vendedor(a) {nome_vendedor}, sua compra ficou no valor de R${valorFinal}.")
elif valor_total <= 300 and valor_total >= 150 :
    desconto = valor_total * 0.10
    valorFinal = valor_total - desconto
    print(f"O valor total da compra do produto {itemVendido}, do cliente {nome_cliente}, sem o desconto é de R${valor_total}. {nome_cliente} ganhou um desconto de 10% do(a) vendedor(a) {nome_vendedor}, sua compra ficou no valor de R${valorFinal}.")
else:
    print(f"O valor total da compra de {nome_cliente} (R${valor_total}), não possui direito a desconto. Vendedor da compra: {nome_vendedor}.")