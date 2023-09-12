# DESCRIÇÕES E TEXTOS!

def info_menu():
    print('='*30+' MENU DE AJUDA '+'='*30)
    print('')
    print('A => Como Funciona')
    print('B => Sobre as Ajudas')
    print('C => Tabela de Premios')
    print('D => Iniciar Jogo')
    escolha=''
    while escolha not in ['A','B','C','D']:
        escolha=input('Digite a opção correspondente: ').upper()
    return escolha

def info_A():
    print('-'*50)
    print('O Show do Bilhão é um Jogo de perguntas e respostas onde você avança de nivel cada vez que escolhe uma alternativa e acerta uma questão')
    print('A qualquer momento no andamento do jogo você pode parar para pegar o prêmio já ganho ou utilizar algumas ajudas disponíveis')
    print('(Para saber mais sobre as Ajudas disponívels selecione a opção B no menu de ajuda)')
    print('As ajudas são limitadas, cada ajuda exige um nível para ser desbloqueada para utilizar')
    print('Um exemplo disso é a Clonagem que pode ser utilizada a partir da 10º pergunta')
    print('Na última pergunta de número 30 valendo 1 Bilhão de Reais não será possível utilizar nenhuma Ajuda')
    print('')
    input('Aperte ENTER para voltar...')

def info_B():
    print('-'*50)
    print('AJUDA 1 = Pular (X3) [Desbloqueia na 2º Pergunta]')
    print('AJUDA 2 = Dicas (X3) [Desbloqueia na 3º Pergunta]')
    print('AJUDA 3 = Cartas (Eliminar 1,2 ou 3 alternativas) [Desbloqueia na 4º Pergunta]')
    print('AJUDA 4 = Blindagem (Se você errar uma pergunta, você permanece no jogo, vale apenas para a questão atual) [Desbloqueia na 7º Pergunta]')
    print('AJUDA 5 = Clonar (Duplica uma ajuda que você tem disponivel) [Desbloqueia na 10º Pergunta]')
    print('AJUDA 6 = Cartas (Eliminar 1,2 ou 3 alternativas) [Desbloqueia na 13º Pergunta]')
    print('AJUDA 7 = Descobrir (Descubra uma ajuda aprimorada) [Desbloqueia na 16º Pergunta]')
    # DESCOBRIR = Pular (x2) | Dica (x2) | Premio Final X2 | Carta Coringa (50% de chance de Eliminar 3 alternativas ou Nada)
    print('AJUDA 8 = Dica [Desbloqueia na 19º Pergunta]')
    print('AJUDA 9 = Pular [Desbloqueia na 20º Pergunta]')
    print('FORCA = Descarte todas as suas ajudas e fique apenas com 1 [Ativo na 27º Pergunta]')
    print('Questão 30 SEM AJUDAS!')
    print('')
    input('Aperte ENTER para voltar...')

def info_C():
    print('='*30+' TABELA DE PRÊMIOS '+'='*30)
    print('')
    print('PERGUNTA 1: ERRAR = 0 | PARAR = 0 | ACERTAR = 1 MIL')
    print('PERGUNTA 2: ERRAR = 250 | PARAR = 1 MIL | ACERTAR = 2 MIL')
    print('PERGUNTA 3: ERRAR = 500 | PARAR = 2 MIL | ACERTAR = 3 MIL')
    print('PERGUNTA 4: ERRAR = 750 | PARAR = 3 MIL | ACERTAR = 4 MIL')
    print('PERGUNTA 5: ERRAR = 1 MIL | PARAR = 4 MIL | ACERTAR = 5 MIL')
    print('PERGUNTA 6: ERRAR = 1.250 | PARAR = 5 MIL | ACERTAR = 10 MIL')
    print('PERGUNTA 7: ERRAR = 2.5 MIL | PARAR = 10 MIL | ACERTAR = 20 MIL')
    print('PERGUNTA 8: ERRAR = 5 MIL | PARAR = 20 MIL | ACERTAR = 30 MIL')
    print('PERGUNTA 9: ERRAR = 7.5 MIL | PARAR = 30 MIL | ACERTAR = 40 MIL')
    print('PERGUNTA 10: ERRAR = 10 MIL | PARAR = 40 MIL | ACERTAR = 50 MIL')
    print('PERGUNTA 11: ERRAR = 12.5 MIL | PARAR = 50 MIL | ACERTAR = 75 MIL')
    print('PERGUNTA 12: ERRAR = 17.5 MIL | PARAR = 75 MIL | ACERTAR = 100 MIL')
    print('PERGUNTA 13: ERRAR = 25 MIL | PARAR = 100 MIL | ACERTAR = 200 MIL')
    print('PERGUNTA 14: ERRAR = 50 MIL | PARAR = 200 MIL | ACERTAR = 300 MIL')
    print('PERGUNTA 15: ERRAR = 75 MIL | PARAR = 300 MIL | ACERTAR = 400 MIL')
    print('PERGUNTA 16: ERRAR = 100 MIL | PARAR = 400 MIL | ACERTAR = 500 MIL')
    print('PERGUNTA 17: ERRAR = 125 MIL | PARAR = 500 MIL | ACERTAR = 750 MIL')
    print('PERGUNTA 18: ERRAR = 175 MIL | PARAR = 750 MIL | ACERTAR = 1 MILHÃO')
    print('PERGUNTA 19: ERRAR = 250 MIL | PARAR = 1 MILHÃO | ACERTAR = 1.5 MILHÃO')
    print('PERGUNTA 20: ERRAR = 400 MIL | PARAR = 1.5 MILHÃO | ACERTAR = 2 MILHÕES')
    print('PERGUNTA 21: ERRAR = 500 MIL | PARAR = 2 MILHÕES | ACERTAR = 2.5 MILHÕES')
    print('PERGUNTA 22: ERRAR = 600 MIL | PARAR = 2.5 MILHÕES | ACERTAR = 3 MILHÕES')
    print('PERGUNTA 23: ERRAR = 750 MIL | PARAR = 3 MILHÕES | ACERTAR = 4 MILHÕES')
    print('PERGUNTA 24: ERRAR = 1 MILHÃO | PARAR = 4 MILHÕES | ACERTAR = 5 MILHÕES')
    print('PERGUNTA 25: ERRAR = 1.25 MILHÃO | PARAR = 5 MILHÕES | ACERTAR = 10 MILHÕES')
    print('PERGUNTA 26: ERRAR = 2.5 MILHÕES | PARAR = 10 MILHÕES | ACERTAR = 20 MILHÕES')
    print('PERGUNTA 27: ERRAR = 5 MILHÕES | PARAR = 20 MILHÕES | ACERTAR = 50 MILHÕES')
    print('PERGUNTA 28: ERRAR = 12.5 MILHÕES | PARAR = 50 MILHÕES | ACERTAR = 100 MILHÕES')
    print('PERGUNTA 29: ERRAR = 25 MILHÕES | PARAR = 100 MILHÕES | ACERTAR = 500 MILHÕES')
    print('PERGUNTA 30 (SEM AJUDA): ERRAR = 0 | PARAR = 500 MILHÕES | ACERTAR = 1 BILHÃO')
    print('')
    input('Aperte ENTER para voltar...')


def premiacao(n):
    if n==1:
        premio=1000
        desc_perca='ZERO'
        desc_parar='ZERO'
        desc_premio='1 MIL'
    if n==2:
        premio=2000
        desc_perca='250'
        desc_parar='1 MIL'
        desc_premio='2 MIL'
    if n==3:
        premio=3000
        desc_perca='500'
        desc_parar='2 MIL'
        desc_premio='3 MIL'
    if n==4:
        premio=4000
        desc_perca='750'
        desc_parar='3 MIL'
        desc_premio='4 MIL'
    if n==5:
        premio=5000
        desc_perca='1 MIL'
        desc_parar='4 MIL'
        desc_premio='5 MIL'
    if n==6:
        premio=1000
        desc_perca='1.250'
        desc_parar='5 MIL'
        desc_premio='10 MIL'
    if n==7:
        premio=2000
        desc_perca='2.5 MIL'
        desc_parar='10 MIL'
        desc_premio='20 MIL'
    if n==8:
        premio=3000
        desc_perca='5 MIL'
        desc_parar='20 MIL'
        desc_premio='30 MIL'
    if n==9:
        premio=4000
        desc_perca='7.5 MIL'
        desc_parar='30 MIL'
        desc_premio='40 MIL'
    if n==10:
        premio=5000
        desc_perca='10 MIL'
        desc_parar='40 MIL'
        desc_premio='50 MIL'
    if n==11:
        premio=1000
        desc_perca='12.5 MIL'
        desc_parar='50 MIL'
        desc_premio='75 MIL'
    if n==12:
        premio=2000
        desc_perca='17.5 MIL'
        desc_parar='75 MIL'
        desc_premio='100 MIL'
    if n==13:
        premio=3000
        desc_perca='25 MIL'
        desc_parar='100 MIL'
        desc_premio='200 MIL'
    if n==14:
        premio=4000
        desc_perca='50 MIL'
        desc_parar='200 MIL'
        desc_premio='300 MIL'
    if n==15:
        premio=5000
        desc_perca='75 MIL'
        desc_parar='300 MIL'
        desc_premio='400 MIL'
    if n==16:
        premio=1000
        desc_perca='100 MIL'
        desc_parar='400 MIL'
        desc_premio='500 MIL'
    if n==17:
        premio=2000
        desc_perca='125 MIL'
        desc_parar='500 MIL'
        desc_premio='750 MIL'
    if n==18:
        premio=3000
        desc_perca='175 MIL'
        desc_parar='750 MIL'
        desc_premio='1 MILHÃO'
    if n==19:
        premio=4000
        desc_perca='250 MIL'
        desc_parar='1 MILHÃO'
        desc_premio='1.5 MILHÃO'
    if n==20:
        premio=5000
        desc_perca='400 MIL'
        desc_parar='1.5 MILHÃO'
        desc_premio='2 MILHÕES'
    if n==21:
        premio=1000
        desc_perca='500 MIL'
        desc_parar='2 MILHÕES'
        desc_premio='2.5 MILHÕES'
    if n==22:
        premio=2000
        desc_perca='600 MIL'
        desc_parar='2.5 MILHÕES'
        desc_premio='3 MILHÕES'
    if n==23:
        premio=3000
        desc_perca='750 MIL'
        desc_parar='3 MILHÕES'
        desc_premio='4 MILHÕES'
    if n==24:
        premio=4000
        desc_perca='1 MILHÃO'
        desc_parar='4 MILHÕES'
        desc_premio='5 MILHÕES'
    if n==25:
        premio=5000
        desc_perca='1.25 MILHÃO'
        desc_parar='5 MILHÕES'
        desc_premio='10 MILHÕES'
    if n==26:
        premio=1000
        desc_perca='2.5 MILHÕES'
        desc_parar='10 MILHÕES'
        desc_premio='20 MILHÕES'
    if n==27:
        premio=2000
        desc_perca='5 MILHÕES'
        desc_parar='20 MILHÕES'
        desc_premio='50 MILHÕES'
    if n==28:
        premio=3000
        desc_perca='12.5 MILHÕES'
        desc_parar='50 MILHÕES'
        desc_premio='100 MILHÕES'
    if n==29:
        premio=4000
        desc_perca='25 MILHÕES'
        desc_parar='100 MILHÕES'
        desc_premio='500 MILHÕES'
    if n==30:
        premio=5000
        desc_perca='ZERO'
        desc_parar='500 MILHÕES'
        desc_premio='1 BILHÃO'

    desc_placar=[premio,desc_perca,desc_parar,desc_premio]
    return desc_placar