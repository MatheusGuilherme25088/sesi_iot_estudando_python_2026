a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("O triângulo é equilátero")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Esses comprimentos não formam um triângulo")
