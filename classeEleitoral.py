idade = int(input(f"Insira aqui sua idade: "))

if idade == 16 or idade == 17 or idade >= 66:
    print(f"Sua classe eleitoral é: Eleitor facultativo")

elif idade > 18:
    print(f"Sua classe eleitoral é: Eleitor obrigatório")

else:
    print(f"Sua classe eleitoral é: Não eleitor")