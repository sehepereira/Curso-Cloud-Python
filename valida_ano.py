#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

print("Digite o seu nome completo:")
nome = input ("")
Atual = 2023
controle = 1
AnoValido = 0

while (controle != 0):
    print("Digite o seu ano de nascimento:")
    Ano = input ("")
    
    if (Ano.isdigit()):
        AnoValido = (int)(Ano)
        if (AnoValido >= 1922 and AnoValido <= 2021):
            controle = 0
        else: 
            print("Digite um ano entre 1922 e 2021")
    else:
        print("Digite um ano valido")

Idade = Atual - AnoValido
print("A sua idade é:" + ((str)(Idade)) + "")