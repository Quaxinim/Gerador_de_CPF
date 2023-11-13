import re
import sys

# Variaveis Essenciais
cpf_enviado_cliente = ''
nove_digitos_processado = []
multiplicador = 10
lista_digito_processado = []
somatorio = 0
digito_1 = 0

entrada_cpf = input('Digite seu cpf: ')
cpf_enviado_cliente = re.sub(r'[^0-9]', '', entrada_cpf)

# Testa a entrada e conclui se ela é repetida ou não
entrada_repetida = entrada_cpf == (entrada_cpf[0] * len(entrada_cpf))

if entrada_repetida:
    print('Dados sequenciais não são permitidos')
    sys.exit()

nove_digitos = (cpf_enviado_cliente[:9])

# Multiplica todos os 9 digitos por 10, 9, 8, 7, 6, 5, 4, 3 e 2 e coloca na lista
for digito_atual in nove_digitos:
    lista_digito_processado.append(int(digito_atual) * multiplicador)
    multiplicador -= 1
# Soma todos os digitos dentro da lista
for digito_lista_atual in lista_digito_processado:
    somatorio += digito_lista_atual

# Multiplica o somatorio por 10 e obtem o resto da divisão da conta anterior por 11
digito_1 = (somatorio * 10) % 11

# Operador ternario para testar se o digito é maior ou menor que 9
digito_1 = digito_1 if digito_1 <= 9 else 0

print('O primeiro digito é:', digito_1)


# Reseta o multiplicador e somatorio
multiplicador = 11
somatorio = 0

lista_digito_2 = []
lista_digito_2_mult = []

# Adiciona todos os numeros do cpf a outra lista, coloca o digito 1 no final e multiplica tudo
for digito_atual in nove_digitos:
    lista_digito_2.append(int(digito_atual))
lista_digito_2.append(digito_1)

# Coleta os numeros do cpf, multiplica todos eles por 11, 10, 9, 8, 7, 6, 5, 4, 3 e 2
for digito_atual in lista_digito_2:
    lista_digito_2_mult.append(int(digito_atual) * multiplicador)
    multiplicador -= 1

# Soma todos os numeros dentro da lista
for digito_atual in lista_digito_2_mult:
    somatorio += digito_atual

# Guarda o valor do digito 2
digito_2 = (somatorio * 10) % 11

# Operador ternario para testar se o digito é maior ou menor que 9
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'O segundo digito é: {digito_2}')

cpf_gerado_calc = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_cliente == cpf_gerado_calc:
    print(f'\033[32mO cpf {cpf_enviado_cliente} é valido!\033[m')
else:
    print(f'\033[31mO cpf {cpf_enviado_cliente} invalido!\033[m')
