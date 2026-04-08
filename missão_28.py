a = input("digite qualquer coisa: ")

try: 
    if a == int(a):
        print(f"o dobro do valor é {a*2}")
    elif a == float(a):
        print("a metade do valor é", a/2)
except ValueError:
    print("tipo invalido")

    # nao consegui fazer a questao 28, tentei de varias formas, mas nao consegui chegar a uma resposta correta, se puder me ajudar a entender o que esta errado, agradeço.
