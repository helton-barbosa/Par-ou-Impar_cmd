import random

valor_inicial = 1
valor_final = 5
num_pc = 0
num_humano = 0
valor = 0

par_impar = input("Escolha (p) para Par ou escolha (i) para Ímpar: ")
num_pc = random.randrange(valor_inicial, valor_final)

if par_impar == 'i':
    mao = "Ímpar"
else:
    mao = "Par"

num_humano = int(input("Digite um valor entre 1 e 5: "))
valor = num_pc + num_humano

if (valor % 2) == 0 and (par_impar == 'p'):
    print(f"Deu {valor}. Você pediu {mao} e venceu!")
elif (valor % 2) != 0 and (par_impar == 'i'):
    print(f"Deu {valor}. Você pediu {mao} e venceu!")
else:
    print(f"Deu {valor}. Você pediu {mao} e perdeu.")