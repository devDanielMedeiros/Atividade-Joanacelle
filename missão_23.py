a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite mais um número inteiro: "))

restoDivisao = [a % 3, b % 3, c % 3]

restoDivisao.sort(reverse=True)
print(f"Os números em ordem decrescente de acordo com o resto da divisão por 3 são: {restoDivisao}")
