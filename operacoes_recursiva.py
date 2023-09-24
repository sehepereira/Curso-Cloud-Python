# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

controle = 1;
while (controle != 0):
    print("Digite qual a operação desejada\n")
    print("1 - SOMA\n")
    print("2 - SUBTRACAO\n")
    print("3 - MULTIPLICACAO\n")
    print("4 - DIVISAO\n")
    print("0 - Sair\n")
    operacao = input (":")

    if (operacao == "0"):
        break

    valor1 = (int)(input ("Digite o primeiro valor:"))
    valor2 = (int)(input ("Digite o segundo valor:"))
    valor = 0
    opcao_invalida = 0

    def soma (valor1, valor2):
        return (valor1 + valor2)

    def subtracao (valor1, valor2):
        return (valor1 - valor2)

    def multiplicacao (valor1, valor2):
        return (valor1 * valor2)

    def divisao (valor1, valor2):
        return (valor1 / valor2)

    match operacao:
        case "1":
            valor = soma(valor1, valor2)
        case "2":
            valor = subtracao(valor1, valor2)
        case "3":
            valor = multiplicacao(valor1, valor2)
        case "4":
            valor = divisao(valor1, valor2)
        case _:
            opcao_invalida = 1
            print("Essa opção não existe")

    if (opcao_invalida == 0):
        print(valor)

print("Obrigado por utilizar nossa calculadora")