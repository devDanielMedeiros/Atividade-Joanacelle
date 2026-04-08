a = int(input("Digite um número inteiro: "))
if (0 < a < 10 ):
    print("pequeno")
elif (10 <= a < 100):
    print("médio")
elif (100 <= a < 1000):
    print("grande")
else:
    print("valor negativo")
