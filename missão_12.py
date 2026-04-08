a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
soma = a + b
if (a > b):
    print("O número", a, "é maior que o número", b)
elif (b > a):
    print("O número", b, "é maior que o número", a)
else:    print("Os números são iguais.")
print("A soma dos números é:", soma,"e o maior número é:", max(a, b))
