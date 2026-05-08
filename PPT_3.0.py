from random import randint
from os import system, name
from time import sleep

def limpar():
    
    if name == 'nt':
        system('cls')
    
    else:
        system('clear')
        
limpar()

jogadas = 0
vitorias = 0
derrotas = 0
empates = 0

regras = {

    'rock':      ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],

    'gun':       ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],

    'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],

    'devil':     ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],

    'dragon':    ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],

    'water':     ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],

    'air':       ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],

    'paper':     ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],

    'sponge':    ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],

    'wolf':      ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],

    'tree':      ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],

    'human':     ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],

    'snake':     ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],

    'scissors':  ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],

    'fire':      ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
}

i = (
'rock',
'gun',
'lightning',
'devil',
'dragon',
'water',
'air',
'paper',
'sponge',
'wolf',
'tree',
'human',
'snake',
'scissors',
'fire'
)

while True:
    limpar()
    
    print('\033[1;32m' + '=' * 40)
    print('\033[1;34mSEJA BEM VINDO AO JO KEN PO 3.0')
    print('\033[1;32m' + '=' * 40)
    print(' ')
    
    computador = randint(0, len(i)-1)

#painel de escolha
    print('\033[1;37m' '=' *30)

    print("""\033[1;31m           Escolha:
\033[1;31m{0}\033[1;37m rock
\033[1;31m{1}\033[1;37m gun
\033[1;31m{2}\033[1;37m lightning
\033[1;31m{3}\033[1;37m devil
\033[1;31m{4}\033[1;37m dragon
\033[1;31m{5}\033[1;37m water
\033[1;31m{6}\033[1;37m air
\033[1;31m{7}\033[1;37m paper
\033[1;31m{8}\033[1;37m sponge
\033[1;31m{9}\033[1;37m wolf
\033[1;31m{10}\033[1;37m tree
\033[1;31m{11}\033[1;37m human
\033[1;31m{12}\033[1;37m snake
\033[1;31m{13}\033[1;37m scissors
\033[1;31m{14}\033[1;37m fire""")
    
    print('\033[1;37m' '=' *30)
    

    try:
        jogador = int(input('informe sua escolha: '))
    
    except ValueError:
        limpar()
        sleep(0.3)
        print('\033[1;31mErro\033[1;37m: Entrada \033[1;31minvalida\033[1;37m. Digite um numero\033[1;31m!')
        sleep(2)
        continue
    
    if jogador < 0 or jogador > len(i) - 1:
        limpar()
        sleep(0.3)
        print('\033[1;31mjogada INVALIDA')
        sleep(2)
        continue

    escolha_jogador = i[jogador]
    escolha_pc = i[computador]

    limpar()
    print(f'Voce escolheu \033[1;31m{i[jogador]}')
    sleep(0.7)
    print('\033[1;37mJO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!!')
    print('')
    jogadas += 1
    
    if escolha_jogador == escolha_pc:
        empates += 1
        input('\033[1;37mO jogo resultou em empate, aperte \033[1;31mENTER\033[1;37m para continuar')

    elif escolha_pc in regras[escolha_jogador]:
        print('\033[1;37mVitoria do \033[1;34mJOGADOR')
        print(f'\033[1;37mO jogador\033[1;37m jogou \033[1;31m{escolha_jogador.upper()}\033[1;37m e o computador\033[1;37m jogou \033[1;31m{escolha_pc.upper()}')
        vitorias += 1

    else:
        print('\033[1;37mVitoria do \033[1;34mCOMPUTADOR')
        print(f'\033[1;37mO jogador\033[1;37m jogou \033[1;31m{escolha_jogador.upper()}\033[1;37m e o computador\033[1;37m jogou \033[1;31m{escolha_pc.upper()}')
        derrotas += 1

    continuar = str(input('\033[1;37mDigite {\033[1;31ms\033[1;37m/\033[1;31msim\033[1;37m} se deseja jogar novamente, ou \033[1;31mENTER\033[1;37m para finalizar: ')).lower().strip()
    
    continuar = continuar.replace(" ", "")
    
    if continuar in ('s', 'sim'):
        continue

    else:
        break
    
#estatisticas de jogo      
limpar()
print('\033[1;31mjogo fechado')
print('\033[1;37m' + '=' *40)

if vitorias >= 8:
    print(f'Parabens cara\033[1;31m!!\033[m, voce ganhou \033[1;32m{vitorias}\033[mx, isso é para poucos\033[1;31m!')
    
elif vitorias <= 2 and derrotas >= 7:
    print(f'Voce não jogou nada \033[1;31mbem\033[m, voce perdeu \033[1;31m{derrotas}\033[mx')

print(f'Voce jogou \033[1;33m{jogadas}\033[1;37mx')
print(f'\033[1;37mTeve \033[1;32m{vitorias}\033[1;37m vitorias\033[1;37m, \033[1;31m{derrotas}\033[1;37m derrotas e \033[1;34m{empates}\033[1;37m empates')
