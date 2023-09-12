# Aqui estão listadas os identificadores (setas) que apontam para alternativas de cada questão
# Além disso estão listados todas as funções de Ajudas

from time import sleep
import Gerador as g
from Alternativas import QUESTOES

def questao(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7):
    if pergunta==1:    
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q1()
    elif pergunta==2:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q2()
    elif pergunta==3:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q3()
    elif pergunta==4:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q4()
    elif pergunta==5:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q5()
    elif pergunta==6:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q6()
    elif pergunta==7:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q7()
    elif pergunta==8:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q8()
    elif pergunta==9:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q9()
    elif pergunta==10:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q10()
    elif pergunta==11:    
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q11()
    elif pergunta==12:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q12()
    elif pergunta==13:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q13()
    elif pergunta==14:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q14()
    elif pergunta==15:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q15()
    elif pergunta==16:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q16()
    elif pergunta==17:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q17()
    elif pergunta==18:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q18()
    elif pergunta==19:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q19()
    elif pergunta==20:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q20()
    elif pergunta==21:    
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q21()
    elif pergunta==22:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q22()
    elif pergunta==23:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q23()
    elif pergunta==24:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q24()
    elif pergunta==25:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q25()
    elif pergunta==26:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q26()
    elif pergunta==27:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q27()
    elif pergunta==28:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q28()
    elif pergunta==29:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q29()
    elif pergunta==30:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q30()
    elif pergunta==31:    
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q31()
    elif pergunta==32:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q32()
    elif pergunta==33:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q33()
    elif pergunta==34:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q34()
    elif pergunta==35:
        quest, alt_a, alt_b, alt_c, alt_d = QUESTOES.q35()
    
    print(f'{quest}')

    if pergunta in [3,6,8,13,16,18,22,25,33] and elimina==0:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [3,6,8,13,16,18,22,25,33] and elimina==1:
        print(f'{alt_a}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [3,6,8,13,16,18,22,25,33] and elimina==2:
        print(f'{alt_a}')
        print(f'{alt_c}')
    elif pergunta in [3,6,8,13,16,18,22,25,33] and elimina==3:
        print(f'{alt_a}')


    if pergunta in [1,7,11,12,17,23,27,29] and elimina==0:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [1,7,11,12,17,23,27,29] and elimina==1:
        print(f'{alt_b}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [1,7,11,12,17,23,27,29] and elimina==2:
        print(f'{alt_b}')
        print(f'{alt_d}')
    elif pergunta in [1,7,11,12,17,23,27,29] and elimina==3:
        print(f'{alt_b}')


    if pergunta in [4,5,10,14,15,24,30,31,32] and elimina==0:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [4,5,10,14,15,24,30,31,32] and elimina==1:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_c}')
    elif pergunta in [4,5,10,14,15,24,30,31,32] and elimina==2:
        print(f'{alt_a}')
        print(f'{alt_c}')
    elif pergunta in [4,5,10,14,15,24,30,31,32] and elimina==3:
        print(f'{alt_c}')


    if pergunta in [2,9,19,20,21,26,28,34,35] and elimina==0:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_c}')
        print(f'{alt_d}')
    elif pergunta in [2,9,19,20,21,26,28,34,35] and elimina==1:
        print(f'{alt_a}')
        print(f'{alt_b}')
        print(f'{alt_d}')
    elif pergunta in [2,9,19,20,21,26,28,34,35] and elimina==2:
        print(f'{alt_a}')
        print(f'{alt_d}')
    elif pergunta in [2,9,19,20,21,26,28,34,35] and elimina==3:
        print(f'{alt_d}')

    
    print('')
    print(f'ERRAR ({lista[1]}) | PARAR ({lista[2]}) | ACERTAR ({lista[3]})')
    print('')
    if quant1==0 and quant2==0 and quant3==0 and quant4==0 and quant5==0 and quant6==0 and quant7==0:
        print('P) PARAR')
    else:
        print('0) Usar Ajuda | P) PARAR')
    print('')
    opc=''

    if elimina==0:
        while opc not in ['A','B','C','D','P','0']:
            opc=input('Selecione a opção correspondente: ').upper()
    
    elif elimina==1:
        if pergunta in [3,6,8,13,16,18,22,25,33]:
            while opc not in ['A','C','D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()
        
        elif pergunta in [1,7,11,12,17,23,27,29]:
            while opc not in ['B','C','D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [4,5,10,14,15,24,30,31,32]:
            while opc not in ['A','B','C','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [2,9,19,20,21,26,28,34,35]:
            while opc not in ['A','B','D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

    elif elimina==2:
        if pergunta in [3,6,8,13,16,18,22,25,33]:
            while opc not in ['A','C','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [1,7,11,12,17,23,27,29]:
            while opc not in ['B','D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [4,5,10,14,15,24,30,31,32]:
            while opc not in ['A','C','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [2,9,19,20,21,26,28,34,35]:
            while opc not in ['A','D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

    elif elimina==3:
        if pergunta in [3,6,8,13,16,18,22,25,33]:
            while opc not in ['A','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [1,7,11,12,17,23,27,29]:
            while opc not in ['B','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [4,5,10,14,15,24,30,31,32]:
            while opc not in ['C','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()

        elif pergunta in [2,9,19,20,21,26,28,34,35]:
            while opc not in ['D','P','0']:
                opc=input('Selecione a opção correspondente: ').upper()


    if opc=='P':
        se=''
        while se not in ['S','N']:
            se=input(f'Tem certeza que você quer PARAR (S/N)? ').upper()
        if se=='S':
            resposta=[True,False]
            return resposta
        elif se=='N':
            while opc not in ['A','B','C','D','0']:
                opc=input('Selecione a alternativa correspondente ou 0 para usar ajuda: ').upper()

    if pergunta in [3,6,8,13,16,18,22,25,33]:
        if opc=='A':
            print('!!! RESPOSTA CORRETA !!!')
            resposta=[False,True]
        elif opc in ['B','C','D']:
            print('XXX RESPOSTA ERRADA XXX')
            resposta=[False,False]

    if pergunta in [1,7,11,12,17,23,27,29]:
        if opc=='B':
            print('!!! RESPOSTA CORRETA !!!')
            resposta=[False,True]
        elif opc in ['A','C','D']:
            print('XXX RESPOSTA ERRADA XXX')
            resposta=[False,False]

    if pergunta in [4,5,10,14,15,24,30,31,32]:
        if opc=='C':
            print('!!! RESPOSTA CORRETA !!!')
            resposta=[False,True]
        elif opc in ['A','B','D']:
            print('XXX RESPOSTA ERRADA XXX')
            resposta=[False,False]

    if pergunta in [2,9,19,20,21,26,28,34,35]:
        if opc=='D':
            print('!!! RESPOSTA CORRETA !!!')
            resposta=[False,True]
        elif opc in ['A','B','C']:
            print('XXX RESPOSTA ERRADA XXX')
            resposta=[False,False]

    if opc=='0':
        resposta = menu_ajuda(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
        
    sleep(1)
    return resposta

def menu_ajuda(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7):
    print('-'*50)
    print('Ajudas disponíveis:')
    print('-'*50)
    if quant1>0:
        print('A => '+'[Pular] '*quant1)
    if quant2>0:
        print('B => '+'[Dica] '*quant2)
    if quant3>0:
        print('C => '+'[Cartas] '*quant3)
    if quant4>0:
        print('D => '+'[Blindar] '*quant4)
    if quant5>0:
        print('E => '+'[Clonar] '*quant5)
    if quant6>0:
        print('F => '+'[Descobrir] '*quant6)
    if quant7>0:
        print('G => '+'[Coringa] '*quant7)
    print('H => Voltar')
    print('')
    escolha=''
    while escolha not in ['A','B','C','D','E','F','G','H']:
        escolha=input('Selecione a opção correspondente: ').upper()
        
        if escolha=='A' and quant1==0:
            escolha=''
        if escolha=='B' and quant2==0:
            escolha=''
        if escolha=='C' and quant3==0:
            escolha=''
        if escolha=='D' and quant4==0:
            escolha=''
        if escolha=='E' and quant5==0:
            escolha=''
        if escolha=='F' and quant6==0:
            escolha=''
        if escolha=='G' and quant7==0:
            escolha=''
        if escolha=='H':
            resposta = questao(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
            return resposta

        
    if escolha=='A':
        quant1-=1
        pergunta = pular(respondidas,pergunta)
    if escolha=='B':
        quant2-=1
        ler_dica(pergunta)
    if escolha=='C':
        quant3-=1
        elimina = cartas(elimina)
    if escolha=='D':
        quant4-=1
        blindar()
    if escolha=='E':
        quant5-=1
        clonar()
    if escolha=='F':
        quant6-=1
        descobrir()
    if escolha=='G':
        quant7-=1
        coringa()

    resposta = questao(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
    return resposta

def pular(respondidas,pergunta):
    respondidas.append(pergunta)
    while pergunta in respondidas:
        pergunta=g.gerarnumero()
    print('')
    print('Você PULOU essa questão...')
    sleep(1)
    return pergunta


def ler_dica(pergunta):
    print('')
    if pergunta==1:
        print('Dica escrita da Pergunta 01')
    elif pergunta==2:
        print('Dica escrita da Pergunta 02')
    elif pergunta==3:
        print('Dica escrita da Pergunta 03')
    elif pergunta==4:
        print('Dica escrita da Pergunta 04')
    elif pergunta==5:
        print('Dica escrita da Pergunta 05')
    elif pergunta==6:
        print('Dica escrita da Pergunta 06')
    elif pergunta==7:
        print('Dica escrita da Pergunta 07')
    elif pergunta==8:
        print('Dica escrita da Pergunta 08')
    elif pergunta==9:
        print('Dica escrita da Pergunta 09')
    elif pergunta==10:
        print('Dica escrita da Pergunta 10')
    elif pergunta==11:
        print('Dica escrita da Pergunta 11')
    elif pergunta==12:
        print('Dica escrita da Pergunta 12')
    elif pergunta==13:
        print('Dica escrita da Pergunta 13')
    elif pergunta==14:
        print('Dica escrita da Pergunta 14')
    elif pergunta==15:
        print('Dica escrita da Pergunta 15')
    elif pergunta==16:
        print('Dica escrita da Pergunta 16')
    elif pergunta==17:
        print('Dica escrita da Pergunta 17')
    elif pergunta==18:
        print('Dica escrita da Pergunta 18')
    elif pergunta==19:
        print('Dica escrita da Pergunta 19')
    elif pergunta==20:
        print('Dica escrita da Pergunta 20')
    elif pergunta==21:
        print('Dica escrita da Pergunta 21')
    elif pergunta==22:
        print('Dica escrita da Pergunta 22')
    elif pergunta==23:
        print('Dica escrita da Pergunta 23')
    elif pergunta==24:
        print('Dica escrita da Pergunta 24')
    elif pergunta==25:
        print('Dica escrita da Pergunta 25')
    elif pergunta==26:
        print('Dica escrita da Pergunta 26')
    elif pergunta==27:
        print('Dica escrita da Pergunta 27')
    elif pergunta==28:
        print('Dica escrita da Pergunta 28')
    elif pergunta==29:
        print('Dica escrita da Pergunta 29')
    elif pergunta==30:
        print('Dica escrita da Pergunta 30')
    elif pergunta==31:
        print('Dica escrita da Pergunta 31')
    elif pergunta==32:
        print('Dica escrita da Pergunta 32')
    elif pergunta==33:
        print('Dica escrita da Pergunta 33')
    elif pergunta==34:
        print('Dica escrita da Pergunta 34')
    elif pergunta==35:
        print('Dica escrita da Pergunta 35')
    
    print('')
    sleep(1)
    input('Pressione ENTER para continuar...')


def forca(quant1,quant2,quant3,quant4,quant5,quant6,quant7):
    print('-'*50)
    print('Escolha qual ajuda quer manter com você no jogo:')
    print('-'*50)
    if quant1>0:
        print('A => '+'[Pular] '*quant1)
    if quant2>0:
        print('B => '+'[Dica] '*quant2)
    if quant3>0:
        print('C => '+'[Cartas] '*quant3)
    if quant4>0:
        print('D => '+'[Blindar] '*quant4)
    if quant5>0:
        print('E => '+'[Clonar] '*quant5)
    if quant6>0:
        print('F => '+'[Descobrir] '*quant6)
    if quant7>0:
        print('G => '+'[Coringa] '*quant7)
    if quant1==0 and quant2==0 and quant3==0 and quant4==0 and quant5==0 and quant6==0 and quant7==0:
        print('Parece que você não tem ajudas disponíveis, o jogo continuará normalmente...')
        sleep(3)
    if quant1>0 or quant2>0 or quant3>0 or quant4>0 or quant5>0 or quant6>0 or quant7>0:
        opc=''
        while opc not in ['A','B','C','D','E','F','G']:
            opc=input('Selecione a opção correspondente: ').upper()
            if quant1==0 and opc=='A':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant2==0 and opc=='B':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant3==0 and opc=='C':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant4==0 and opc=='D':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant5==0 and opc=='E':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant6==0 and opc=='F':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
            elif quant7==0 and opc=='G':
                # print('OPÇÃO INVÁLIDA!')
                opc=''
        if opc=='A':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=1,0,0,0,0,0,0
        elif opc=='B':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,1,0,0,0,0,0
        elif opc=='C':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,1,0,0,0,0
        elif opc=='D':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,1,0,0,0
        elif opc=='E':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,0,1,0,0
        elif opc=='F':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,0,0,1,0
        elif opc=='G':
            forca=quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,0,0,0,1
        print('')
        print('Sua ajuda foi escolhida, prosseguindo com o jogo...')
        sleep(3)
        return forca


def cartas(elimina):
    print('')
    opc=''
    while opc not in ['J','Q','K']:
        opc=input('Selecione uma carta [J] [Q] [K]: ').upper()
    if opc=='J':
        print('[J] => Elimina uma alternativa!')
        elimina=1
    elif opc=='Q':
        print('[Q] => Elimina duas alternativa!!')
        elimina=2
    elif opc=='K':
        print('[K] => Elimina três alternativas!!!')
        elimina=3
    input('Pressione ENTER para continuar...')
    return elimina

def blindar():
    pass

def clonar():
    pass

def descobrir():
    pass

def coringa():
    pass



# def placar_final(nome,n,respondidas,quant1,quant2,quant3,quant4,quant5,quant6,quant7):
#     a.automacao_do_jogo(nome,n,respondidas,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
#     print('')
#     print(f'PLACAR FINAL: {nome} | R$ placar')