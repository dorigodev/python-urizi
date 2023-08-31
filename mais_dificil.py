nome = input("Digite seu nome:")
altura = float(input("Digite sua altura em Centimetros: "))*0.01
peso = float(input("Digite seu peso em Kilos: "))
imc = round(peso/(altura**2), 2)

if imc < 16:
	classi = "Magreza grave"
elif imc < 17:
	classi = "Magreza moderada"
elif imc < 18.5:
	classi = "Magreza leve"
elif imc < 25:
	classi = "Saudável"
elif imc < 30:
	classi = "Sobrepeso"
elif imc < 35:
	classi = "Obesidade Grau I"
elif imc < 40:
	classi = "Obesidade Grau II (severa)"
else:
	classi = "Obesidade Grau III (mórbida)"

print(f'O seu nome é {nome}, sua altura é {round(altura, 2)} metros, seu peso é {peso}kg, seu IMC é {imc}, e sua classificação é {classi}')