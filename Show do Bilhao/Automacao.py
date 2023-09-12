# AUTOMAÇÃO, ANDAMENTO DO JOGO!

from time import sleep
import Descricao as d
import Questoes as p
import Gerador as g

def automacao_do_jogo(nome,n,respondidas,quant1,quant2,quant3,quant4,quant5,quant6,quant7):
    jogando=True
    while jogando==True:
        lista=d.premiacao(n)
        print('')
        print(f'Vamos para a Pergunta {n} que vale R$ {lista[3]}')
        sleep(3)
        print('-'*50)
        elimina=0
        pergunta=0
        while pergunta in respondidas:
            pergunta=g.gerarnumero()
            # print(pergunta) // VERIFICANDO QUAL PERGUNTA O ALGORITMO ALEATÓRIO ESCOLHEU PARA RESPONDER
        resposta=p.questao(nome,n,respondidas,pergunta,lista,elimina,quant1,quant2,quant3,quant4,quant5,quant6,quant7)
        if resposta==[False,True]: # NÃO PARAR , MAS CONTINUO
            respondidas.append(pergunta)
            # print(respondidas) // VERIFICANDO A LISTA DE PERGUNTAS JA RESPONDIDAS
            n+=1

            if n==2:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Pular] X 3')
                input('Pressione ENTER para continuar...')
                quant1+=3

            elif n==3:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Dica] X 3')
                input('Pressione ENTER para continuar...')
                quant2+=3

            elif n==4 or n==13:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Cartas]')
                input('Pressione ENTER para continuar...')
                quant3+=1

            elif n==7:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Blindar]')
                input('Pressione ENTER para continuar...')
                quant4+=1

            elif n==10:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Clonar]')
                input('Pressione ENTER para continuar...')
                quant5+=1

            elif n==19:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Descobrir]')
                input('Pressione ENTER para continuar...')
                quant6+=1

            elif n==19:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Dica]')
                input('Pressione ENTER para continuar...')
                quant2+=1

            elif n==20:
                print('')
                print('===> Parabéns você desbloqueou uma nova ajuda: [Pular]')
                input('Pressione ENTER para continuar...')
                quant1+=1

            elif n==27:
                print('')
                print('===> FORCA: Se você tiver alguma ajuda deve escolher uma para ficar, o resto será descartado!')
                input('Pressione ENTER para continuar...')
                forca=p.forca(quant1,quant2,quant3,quant4,quant5,quant6,quant7)
                quant1,quant2,quant3,quant4,quant5,quant6,quant7=forca[0],forca[1],forca[2],forca[3],forca[4],forca[5],forca[6]

            elif n==30:
                quant1,quant2,quant3,quant4,quant5,quant6,quant7=0,0,0,0,0,0,0
                print('')
                print('PERGUNTA FINAL: Parabéns por chegar na pergunta de 1 Bilhão de Reais!')
                sleep(2)
                print('Mas a partir de agora, as coisas mudam...')
                sleep(2)
                print('Todas as suas ajudas serão anuladas!')
                sleep(2)
                print('Agora é Tudo ou Nada...')
                sleep(2)
                print('E você quem decidirá o Final')
                sleep(2)
                input('Pressione ENTER para continuar...')

            if n==31:
                jogando=False
                resultado_final=lista[3]
                print('')
                print('PARABÉNS VOCÊ ACABA DE GANHAR 1 BILHÃO DE REAIS!!!')

        elif resposta==[False,False]: # NÃO PARAR , MAS ERREI
            jogando=False
            resultado_final=lista[1]
        elif resposta==[True,False]: # PARAR O JOGO , NÃO CONTINUAR
            jogando=False
            resultado_final=lista[2]
        
    return resultado_final