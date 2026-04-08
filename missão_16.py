a = input("Digite qualquer coisa: ")
a = type(a)
if (type(a) == float) or (type(a) == int):
    print("O quadrado do número é: ", a**2)
else:
    print("O tipo do valor digitado é: ", a)
    
