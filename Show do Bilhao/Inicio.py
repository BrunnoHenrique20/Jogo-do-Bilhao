# CRIAR um Sistema de QUIZ utilizando essas variáveis abaixo:
# CRIAR um questionário de Perguntas e Respostas
# Designar Opções de Ajuda para responder perguntas e validar quando elas ja tenham sido utilizadas nas outras perguntas
# Descrição sobre Ajudas

# PROBLEMAS ENCONTRADOS: Ao acertar uma questão as ajudas voltam novamente para o menu de ajudas!
# FALTA IMPLEMENTAR: Blindar, Clonar, Descobrir, Coringa[Ajuda do Descobrir]
# AJUDAS JÁ IMPLEMENTADAS E FUNCIONANDO: Pular, Dica, Cartas, Automação nas questões finais

# ESSE ARQUIVO É O PRINCIPAL QUE DEVE SER EXECUTADO PRIMEIRO!

from time import sleep
import Descricao as d
import Automacao as a

def iniciar():
    print('='*30+' SHOW DO BILHÃO '+'='*30)
    print('')
    print('A => Iniciar Jogo')
    print('B => Ajuda')
    inicia=''
    while inicia not in ['A','B']:
        inicia=input('Digite a opção correspondente: ').upper()
    return inicia


def iniciar_2(inicia):
    while inicia=='B':
        menu='X'
        while menu=='A' or menu=='B' or menu=='C' or menu=='X':
            menu = d.info_menu()
            if menu=='A':
                d.info_A()
            if menu=='B':
                d.info_B()
            if menu=='C':
                d.info_C()
        if menu=='D':
            inicia='A'

    if inicia=='A':
        nome=''
        while len(nome)==0:
            nome=input('Digite o seu Nome: ')
            if len(nome)>20:
                print('ERRO: Nome muito longo digite até 20 caracteres!')
                nome=''
            if not nome.isalpha():
                print('ERRO: Digite apenas Letras (MAX: 20 caracteres)!')
                nome=''

        print('Iniciando Jogo...')
        sleep(2)
        n=1
        respondidas=[0]
        quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,0,0,0,0
        placar = a.automacao_do_jogo(nome,n,respondidas,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
        print('')
        print(f'PLACAR FINAL: {nome} | R$ {placar}')


inicia=iniciar()
iniciar_2(inicia)