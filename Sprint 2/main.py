def calcula_soma(a,b):
    soma = a+b
    return soma

def calcula_subtracao(a,b):
    sub = a-b
    return sub

def calcula_multiplicacao(a,b):
    return a * b

def calcula_divisao(a,b):
    return a / b

def calcula_potenciacao(a,b):
    return

def calcula_radiciacao(a,b):
    return

def calcula_divisao_inteira(a,b):
    return  

def calcula_resto(a,b):
    return

def calcula_percentual(a,b):
    return

print("Bem vindo à calculadora do Time 2!")
operacao = int(input("Digite o número da operação desejada:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Radiciação\n7 - Divisão inteira\n8 - Resto da divisão\n9 - Percentual\n0 - Sair\n"))

while operacao != 0:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == 1:
        resultado = calcula_soma(a,b)
    elif operacao == 2:
        resultado = calcula_subtracao(a,b)
    elif operacao == 3:
        resultado = calcula_multiplicacao(a,b)
    elif operacao == 4: 
        resultado = calcula_divisao(a,b)
    elif operacao == 5:
        resultado = calcula_potenciacao(a,b)
    elif operacao == 6:
        resultado = calcula_radiciacao(a,b)
    elif operacao == 7:   
        resultado = calcula_divisao_inteira(a,b)
    elif operacao == 8:
        resultado = calcula_resto(a,b)
    else:
        resultado = calcula_percentual(a,b)

    print(f"O resultado da operação é: {resultado}")

    operacao = int(input("\nDigite o número da operação desejada:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\n6 - Radiciação\n7 - Divisão inteira\n8 - Resto da divisão\n9 - Percentual\n0 - Sair\n"))

