# -*- coding: utf-8 -*-  comando para poder rodar o código com string

#input = entrada de dados do usuário (prompt no js)
#valor1 =  int(input ('digite o valor 1:'))
#valor2 = int(input ('digite o valor 2:'))
#resultado = valor1 + valor2

#if resultado >= 10 and resultado <=12:
 #   print ('valor está entre 10 e 12')

#elif resultado == 13:
 #   print('opa opa, é 13')

#else:
 #   print('Não fizemos nenhum cálculo com o seu valor')

#valor1 = float(input('Digite o valor 1:'))
#3valor2 = float(input('Digite o valor 2:'))

#soma = valor1 + valor2
#subtracao = valor1 - valor2
#divisao = valor1 / valor2
#modulo = valor1 % valor2
#multiplicacao = valor1 * valor2

#print('Resultado soma' + soma)
#print('Resultado subtração' + subtracao)
#print('Resultado divisão' + divisao)
#print('Resultado resto da divisão' + modulo)
#print('Resultado multiplicação' + multiplicacao)



#nome = str(input('Qual o seu nome?'))
#idade = int(input('Qual a sua idade?'))

#if idade >= 18:
#    print('pode entrar' + nome)
#elif idade <= 11:
#   print('Menor de idade. Você ainda é criança')    
#else:
#    print('Menor de idade')



#lista1 = ['gabriel', 40 , 'full stack', True, 3.9]
#print(lista1)

#dicionario guarda uma chave e o valor dela
#dicionario1 = {'nome': 'gabriel'}

#Como uma lista, mas não deixa sobreescrever o arquivo
#tupla1 = ('oi', 2, 'tchau')

#range: mostra o intervalor entre os valores colocados
#for i in range(10):
#    print(i)


#WHILE
#number = 0
#while number < 10:
#    print(number)
#    number = number+1


#FUNÇÃO
import datetime

dias_de_nasc = datetime.date(day=2, year=1935, month=2)

def calcular_dias_de_vida(data):
    if data is None:
        error = 'ops'
        return error
    hoje = datetime.date.today()
    dias_de_vida = hoje - data
    return dias_de_vida

retorno = calcular_dias_de_vida(dias_de_nasc)
print(retorno)

