a = int(input("Digite um número inteiro: "))
if (a > 0) and (a % 2 == 0) and (a % 3 != 0):
    print("O número é multiplo de 2 e 3.")
elif (a % 2 == 0) or (a % 3 == 0):
    print("Um dos números é múltiplo de 2 ou 3.")
else:
    print("O número não é compatível.")
