a = int(input("Digite um número inteiro: "))
if (a % 2) == 0 and (a > 0):
    print("O número é par e positivo. ")
elif (a % 2) == 0 and (a < 0):
    print("O número é par e negativo. ")
elif (a % 2) != 0 and (a > 0):
    print("O número é ímpar e positivo. ")
elif (a % 2) != 0 and (a < 0):
    print("O número é ímpar e negativo. ")
