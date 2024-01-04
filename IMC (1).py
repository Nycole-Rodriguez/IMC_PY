from os import system

peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))

imc =  peso / altura**2

print("O seu imc: %f" % imc)

if(imc < 18.5):
    print("Abaixo do peso")
elif(imc < 25):
    print("Peso normal")
elif(imc < 30):
    print("Sobrepeso")
elif(imc < 35):
    print("Obessidade Grau 1")
elif(imc < 40):
    print("Obessidade Grau 2")
else:
    print("Obessidade Grau 3")
    
system("pause")