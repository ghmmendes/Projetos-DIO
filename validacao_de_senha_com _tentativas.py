# Objetivo: Crie uma senha e permita apenas 3 tentativas para o usuário acertar.
senha_correta = "python123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite uma senha: ")

    if senha == senha_correta:
        print("Acesso concedido")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você possui {tentativas} tentativas restantes")

    if tentativas == 0:
        print("Tentativas excedidas")
        break
