import sys 

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Aceita apenas numeros")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Erro: Zero não é divisivel")
    sys.exit(1)

print(f"{x} dividido por {y} é : {result}")
