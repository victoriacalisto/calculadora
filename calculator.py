num1 = 0
num2 = 0
result = 0
op   = ''

while True:
    print("Bem vindo a calculadora, vamos lá. Digite 2 numeros de cada vez para começarmos e depois digite o simbolo da operação que deseja fazer.")
    num1 = float(input('Digite o primeiro numero: '))
    op   = input('Digite a operação para ser feita:')
    num2 = float(input('Digite o segundo numero: '))

    if op == '+':
        result = num1 + num2 
    elif op == '-':
         result = num1 - num2 
    elif op == '*':
        result = num1 * num2 
    elif op == '/':
        result = num1 / num2 
    else: 
        print("Operacao nao reconhecida")

    print('{} {} {} = {}' .format(num1, op, num2, result))



    