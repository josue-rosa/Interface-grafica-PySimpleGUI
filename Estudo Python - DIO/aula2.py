
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}. \nSubtração: {subtracao}. \nMultiplicação: {multiplicacao}. \nDivisao: {divisao}. \nResto: {resto}'.format(soma=soma, subtracao=subtracao, resto=resto, multiplicacao=multiplicacao, divisao=divisao))

print(resultado)
