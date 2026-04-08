a = input("digite qualquer coisa: ")
# isso aqui a senhorita nao passou nao
try: 
    a = int(a)
    if (a > 10):
        print("alto")
    else:        
        print("baixo")
except ValueError:
    print("entrada invalida")
