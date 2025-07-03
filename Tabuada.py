# Imprima a tabuada do 5, de 1 a 10, usando for.
tabuada = range(1, 11)
multi = int(input("Insira o número que deseja verificar a tabuada: "))

for numero in tabuada:
    print(f"{multi} x {numero} = {multi * numero}")

print()