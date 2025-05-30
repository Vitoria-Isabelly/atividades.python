def soma(a,b):
    return a+b

def subitrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

num1 = float(input("digite o valor 1:"))
num2 = float(input("digite o valor 2:"))

print('digite a operaçao que voce quer realizar ,+,-,/,*:')

option = input()

if option=='+':
    soma(num1,num2)
elif option=='-':
    subitrair(num1,num2)
elif option=="*":
    multiplicar(num1,num2)
elif option=="/":
    dividir(num1,num2)


print("soma:", soma(num1,num2))
print("subtrair:", subitrair(num1,num2))
print("multiplicar:", multiplicar(num1,num2))
print("dividir:", dividir(num1,num2))