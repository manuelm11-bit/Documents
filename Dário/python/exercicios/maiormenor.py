Num1 = int(input("Digite o numero 1: "))
Num2 = int(input("Digite o numero 2: "))
Num3 = int(input("Digite o numero 3: "))

if Num1 == Num2:
    print("os numeros 1 e 2 são iguais")

if Num1 == Num3:
    print("os numeros 1 e 3 são iguais")

if Num2 == Num1:
    print("os numeros 2 e 1 são iguais")

if Num2 == Num3:
    print("os numeros 2 e 3 são iguais")

if Num3 == Num1:
    print("os numeros 3 e 1 são iguais")

if Num3 == Num2:
    print("os numeros 3 e 2 são iguais")

else:
    numero_maior= max(Num1, Num2, Num3)
    numero_menor= min(Num1, Num2, Num3)

print(f"O maior numero é o {numero_maior}")
print(f"O menor numero é o {numero_menor}")