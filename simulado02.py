numero = 0
somaN = 0
escolha = "s"
pos = 0
neg = 0

while escolha == "s" or escolha == "S":
    numero = float(input(f"Digite um número: "))
    somaN += numero
    escolha = input(f"Deseja cadastrar mais números? (s ou n) ")

    if numero >= 0:
        pos += numero
    else:
        neg += numero

print(f"A soma dos números positivos é: {pos}")
print(f"A soma dos números negativos é: {neg}")
print(f"A soma das duas parciais é: {pos + neg}")