v1 = float(input(f"Insira o primeiro valor: "))
v2 = float(input(f"Insira o segundo valor: "))

op = input(f"Qual operação deverá ser feita? ")

if op.lower()[0] == "a" or op == "soma" or op == "Soma":
    print(f"A soma dos valores é de {v1 + v2}")

elif op.lower()[0] == "s":
    print(f"A subtração dos valores é: {v1 - v2}")

elif op.lower()[0] == "d":
    print(f"A divisão dos valores é: {v1 / v2}")

elif op.lower()[0] == "m":
    print(f"A multiplicação dos valores é {v1 * v2}")

else:
    print(f"Essa calculadora somente realiza operações básicas.")