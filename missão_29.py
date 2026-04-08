a = int(input("Digite um número inteiro: "))
if a % 5 == 0:
    if a > 50:
        print("multiplo alto")
    elif a < 50:
        print("multiplo baixo")
else:
    print("não é múltiplo de 5")
