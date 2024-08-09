# estrutura
#def nome_da_função(argumento1, argumento2):
#   x = ação que será realizada
#   return x

# ou se for um número indefinido de argumentos
#def nome_da_função(*argumentos):

# ou para argumentos que vêm em formato de dicionário
#def minha_funcao(**kwargs):
# exemplo:

# def preco_final(preco, **adicionais):
#     print(adicionais)
#     if 'desconto' in adicionais:
#         preco *= (1 - adicionais['desconto'])
#     if 'garantia_extra' in adicionais:
#         preco += adicionais['garantia_extra'] 
#     if 'imposto' in adicionais:
#         preco *= (1 + adicionais['imposto'])
#     return preco

# ordem dos argumentos a ser seguida
# def minha_funcao(arg1, arg2, arg3, arg4, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):

#passar todos valores de iterable em uma função usando map
# dicionario = {'vinho':540, 'cerveja':320, 'coca':642, 'pepsi':100}
# resultado = list(map(calculo, dicionario.values()))

# tratamento completo utilizado em funções
# try:
#     tente fazer isso
# except ErroEspecífico:
#     deu esse erro aqui que era esperado 
# else:
#     caso não dê o erro esperado, rode isso.
# finally:
#     independente do que acontecer, faça isso.


# EXERCÍCIO 1

# preco = 1500
# custo = 400
# lucro = 785

# def cal_imposto (preço, lucro, custo):
#     return preço - (custo + lucro)

# print (cal_imposto(preco, custo, lucro))


# EXERCICIO 2

# clientes_devedores = [('462.286.561-65',14405,24),('251.569.170-81',16027,1),('297.681.579-21',8177,28),('790.223.154-40',9585,10),('810.442.219-10',18826,29),('419.210.299-79',11421,15),('908.507.760-43',12445,24),('911.238.364-17',1345,4),('131.115.339-28',11625,8),('204.169.467-27',5364,22),('470.806.376-11',932,29),('938.608.980-69',13809,19)]

# meu código abaixo:

# def filtrar(lista):
#     valor = 1000
#     dias = 20
#     tam = len(lista) 
#     empty = [] 
#     for i in range(tam):
#         cpf, divida, dia = lista[i]
#         if divida >= valor and dia >= dias:
#             empty.append(cpf)
#         else:
#             pass
#     return print(empty)
# filtrar(clientes_devedores)

# def melhorando(lista):
#     vazio = []
#     for item in clientes_devedores:
#         cpf, divida, dia = item
#         if divida >= 1000 and dia >=20:
#             vazio.append(cpf)
#     return print(vazio)
# melhorando(clientes_devedores)


# EXERCICIO 3

# meta = 10000
# vendas = {
#     'João': 15000,
#     'Julia': 27000,
#     'Marcus': 9900,
#     'Maria': 3750,
#     'Ana': 10300,
#     'Alon': 7870,
# }
# def separador(vendas):
#     winners = []
#     for item in vendas:
#         if vendas[item] > 10000:
#             winners.append(item)
#     return print('vencedores são {} e porcentagem total é {:.2%}'.format(winners, len(item)/len(winners)))

# separador(vendas)
