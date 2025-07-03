# Peça para o usuário digitar um texto. Conte quantas vogais existem nesse texto.
# Dica:
VOGAIS = "AEIOU"
texto = input("Digite um texto: ")
soma = 0

for letras in texto:
    if letras.upper() in VOGAIS:
        soma += 1

print(f"Número de vogais: {soma}")