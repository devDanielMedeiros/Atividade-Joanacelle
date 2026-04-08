a = input("digite qualquer coisa: ")
print("O tipo primitivo desse valor é", type(a))
try:
    a = int(a)
    print("O valor é do tipo inteiro")
except ValueError:
    print("valor nao numérico")
