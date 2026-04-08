a = int(input("Digite um número inteiro: "))
if 1 <= a <= 100:
    if a % 2 == 0:
        print("o numero é par e está no intervalo")
    else:        
        print("impar no intervalo")
else:    
    print("o numero não esta no intervalo")
