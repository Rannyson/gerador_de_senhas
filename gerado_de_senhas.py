import random

cor = '\033[1;36;42m'
sem ='\033[m'
print ("Gerador De Senhas")

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%^&*().?0123456789'

numero = input('Quantas senhas você quer gerar: ')
numero = int (numero)

tamanho = input('Qual tamanha da sua senha: ')

tamanho = int(tamanho)

print('\nEssas foram as senhas geradas:')

for s in range (numero):
    senhas = ''
    for c in range (tamanho):
        senhas += random.choice(caracteres)
    print(f"senhas {s+1} : {cor}{senhas}{sem}")