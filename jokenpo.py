import random

s = input('Vamos jogar Jokenpô? Digite 1 para SIM ou 2 para NÃO')
rodada = 1

maos = ['PEDRA', 'PAPEL', 'TESOURA']

while rodada == 1:
    if s == '1':
        mao_player = int(input('Escolha uma opção: 1. Pedra, 2. Papel, 3. Tesoura'))
        mao_cpu = random.randint(1,4)
        if mao_player == 1 or mao_player == 2 or mao_player == 3:
            if mao_player == mao_cpu:
                print(f'Voce escolheu {maos[mao_player - 1]}, CPU escolheu {maos[mao_cpu - 1]}.')
                print('Empate!')
                rodada = int(input('Digite 1 para jogar de novo!'))
            elif mao_player == 1 and mao_cpu == 3:
                print(f'Voce escolheu {maos[mao_player - 1]}, CPU escolheu {maos[mao_cpu - 1]}.')
                print('Voce venceu!')
                rodada = int(input('Digite 1 para jogar de novo!'))
            elif mao_player == 2 and mao_cpu == 1:
                print(f'Voce escolheu {maos[mao_player - 1]}, CPU escolheu {maos[mao_cpu - 1]}.')
                print('Voce venceu!')
                rodada = int(input('Digite 1 para jogar de novo!'))
            elif mao_player == 3 and mao_cpu == 2:
                print(f'Voce escolheu {maos[mao_player - 1]}, CPU escolheu {maos[mao_cpu - 1]}.')
                print('Voce venceu!')
                rodada = int(input('Digite 1 para jogar de novo!'))
            else:
                print(f'Voce escolheu {maos[mao_player - 1]}, CPU escolheu {maos[mao_cpu - 1]}.')
                print('Voce perdeu!')
                rodada = int(input('Digite 1 para jogar de novo!'))
        else:
            print('Digite apenas 1, 2 ou 3!')
            rodada = 1
    elif s == '2':
        rodada = 2
    else:
        print('Digite apenas 1 ou 2')
        s = input('Vamos jogar Jokenpô? Digite 1 para SIM ou 2 para Não: ')
        rodada = 1
if rodada != 1:
    print('Fim do programa!')