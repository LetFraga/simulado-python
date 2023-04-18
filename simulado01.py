v1 = float(input(f"Digite o primeiro valor: "))
v2 = float(input(f"Digite o segundo valor: "))
v3 = float(input(f"Digite o terceiro valor: "))

print(f"A ordem lida é: {v1}, {v2} e {v3}")

#Ordem Crescente:
if v1 <= v2 and v1 <= v3 and v2 <= v3:
    print(f"A ordem crescente é: {v1}, {v2}, e {v3}")
elif v1 <= v2 and v1 <= v3 and v3 <= v2:
    print(f"A ordem crescente é: {v1}, {v3}, e {v2}")
elif v2 <= v1 and v2 <= v3 and v1 <= v3:
    print(f"A ordem crescente é: {v2}, {v1}, e {v3}")
elif v2 <= v1 and v2 <= v3 and v3 <= v1:
    print(f"A ordem crescente é: {v2}, {v3}, e {v1}")
elif v3 <= v1 and v3 <= v3 and v1 <= v2:
    print(f"A ordem crescente é: {v3}, {v1}, e {v2}")
elif v3 <= v1 and v3 <= v2 and v2 <= v1:
    print(f"A ordem crescente é: {v3}, {v2}, e {v1}")

#Ordem Decrescente:
if v1 >= v2 and v1 >= v3 and v2 >= v3:
    print(f"A ordem decrescente é: {v1}, {v2}, e {v3}")
elif v1 >= v2 and v1 >= v3 and v3 >= v2:
        print(f"A ordem decrescente é: {v1}, {v3}, e {v2}")
elif v2 >= v1 and v2 >= v3 and v1 >= v3:
        print(f"A ordem decrescente é: {v2}, {v1}, e {v3}")
elif v2 >= v1 and v2 >= v3 and v3 >= v1:
        print(f"A ordem decrescente é: {v2}, {v3}, e {v1}")
elif v3 >= v1 and v3 >= v2 and v1 >= v2:
        print(f"A ordem decrescente é: {v3}, {v1}, e {v2}")
elif v3 >= v1 and v3 >= v2 and v2 >= v1:
        print(f"A ordem decrescente é: {v3}, {v2}, e {v1}")
