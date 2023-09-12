# Função Random: Seleciona aleatoriamente a próxima pergunta entre as perguntas 1 e 35
# Se for adicionar mais perguntas deve-se mudar o número final para a quantidade total de perguntas

import random

def gerarnumero():
    # numero_aleatorio = random.sample(range(x,y),k=1)
    num = random.randint(1,35)
    return num