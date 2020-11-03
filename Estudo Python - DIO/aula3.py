""" 1
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('Maior valor é {}'.format(a))
elif b > a and b > c:
    print('Maior valor é {}'.format(b))
else: 
    print('Maior valor é {}'.format(c))
print('Finish')
"""

""" 2

num = int(input('Digite um valor para saber se ele é PAR ou IMPAR: '))
resto = num % 2
if resto == 0:
    print('Este numero é PAR')
else:
    print('Este número é IMPAR')
"""

nota1 = int(input('Digite a primeira nota: '))
if nota1 > 10:
    nota1 = int(input('Por favor, digite uma nota abaixo de 10: '))
nota2 = int(input('Digite a segunda nota: '))
if nota2 > 10:
    int(input('Você digitou uma nota errada. Informe a nota menor de 10. '))
media = (nota1 + nota2) / 2
print(f'A média entre as notas {nota1} e {nota2} é {media}')
