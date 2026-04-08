a = int(input("Digite um número: "))
if (a ** (1/2)) % 1 == 0:
    raiz = int(a ** (1/2))
    print(f"A raiz quadrada de {a} é: {raiz}")
else:
    print(f"{a} não é um quadrado perfeito.")
