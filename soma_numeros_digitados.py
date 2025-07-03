# Objetivo: Peça números ao usuário e vá somando até ele digitar 0.
contador = 1
soma = 0

while contador != 0:
    contador = int(input("Digite um número (0 para sair): "))
    
    if contador != 0:
        soma += contador

print(f"Soma total dos números inseridos: {soma}")