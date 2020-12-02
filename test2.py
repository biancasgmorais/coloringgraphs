import numpy
import random
import time
import sys
import matplotlib.pyplot

#temporização
ini = time.time()

#variaveis
tam = 300 #tamanho do vetor de cores e da matriz de adjacencia
colors = 100 #quantidade de cores dentro do vetor de cores
contador = 0 #contador de iterações da função subida de encosta
contador2 = 0 #contador de iterações da função reinicio aleatorio
matriz = numpy.random.randint(2, size=(tam, tam))
#matriz = ([0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]) #matriz de adjacencia
paint = [] #vetor de cores
iteracao_randomrestart = [] #vetor de iterações da função reinicio aleatorio para plotagem
custo_iteracao_randomrestart =[] #vetor da qualidade de cada iteração na função reinicio aleatorio

class node:
    def __init__(self, matriz, cust, paint): 
        self.matriz = matriz
        self.cust = cust
        self.paint = paint

def initialstate(): #estado inicial - a matriz não precisa ser mudada, então basta adicionar o global
    global tam
    global matriz
    global paint
    global colors
    paint = [] #é necessario inicia-lo zerado pois ele estava adicionando valores qndo era reusado
    for i in range(tam):
        paint.append(random.randint(0, colors-1)) #vetor de cores é aleatorio
    return (node(matriz, 0, paint))

def cria_estrutura():  #cria estrutura vazia
    global matriz
    global paint
    return(node(matriz, 0, paint))

def getResultado(s): #verifica a qualidade da resposta
    global tam
    qualidade = 0
    for i in range(tam):
        for j in range(tam):
            if(s.matriz[i][j] == 1):
                if(s.paint[i] != s.paint[j]):
                    qualidade += 1
    s.cust = qualidade
    return s

def copia(s): #copia uma estrutura para outra
    global tam
    novo = cria_estrutura()
    for i in range(tam):
        for j in range(tam):
            novo.matriz[i][j] = s.matriz[i][j]
    novo.paint = copia2(s.paint)
    novo.cust = s.cust
    return novo

def copia2(queue): #copia lista
    novo2 = []
    for i in range(0,len(queue)):
        novo2.append(queue[i])
    return novo2


def getVizinho(s):  #olha cada um dos vizinhos e escolhe o melhor
    global tam
    global colors
    queue = []
    aux = copia(s)
    aux2 = cria_estrutura()
    paint2 = copia2(s.paint)

    for i in range(0,tam):
        queue.append( paint2[0:i] + [(paint2[i] + 1) % colors] + paint2[i + 1:])
        queue.append( paint2[0:i] + [(paint2[i] - 1) % colors] + paint2[i + 1:])

    x = cria_estrutura()
    x.paint = copia2(queue[0])
    x = getResultado(x)

    for i in range(0,len(queue)):
        aux2.paint = queue[i]
        aux2 = getResultado(aux2)
        if(aux2.cust >= x.cust):
            x = copia(aux2)
    
    return x

def hillclimb(s): #subida de encosta
    atual = copia(s)
    atual = getResultado(atual)
    global contador
    
    while True:
        vizinho = getVizinho(atual)

        if(getResultado(vizinho).cust <= atual.cust):
            return atual

        else:
            atual = copia(vizinho)
    

def random_restart(): #reinicio aleatorio
    global custo_iteracao_randomrestart
    global contador2
    contador2 = 0
    maximolocal = 0
    atual = 0
    global iteracao_randomrestart

    x = initialstate()
    current = hillclimb(x)
    atual = current.cust
    
    print('\nMatriz de adjacencia') #É a mesma matriz de adjacencia para todos
    print(current.matriz)

    print('\nMatriz de cores inicial')
    print(current.paint)

    #timer: muda o tempo necessário no end_time
    end_time = time.time() + 600 #10 minutos e para
    countTimer = 0
    sleepTime = 0.000

    while time.time() < end_time: #esse while vai rodar durante 10 minutos e retornar o maior resultados de todos os estados
        #iniciais aleatorios obtidos
        time.sleep(sleepTime)

        if(maximolocal >= atual):
            
            custo_iteracao_randomrestart.append(maximolocal) #adiciona o custo obtido em cada iteração
            atual = maximolocal #atual é substituido pelo maior
            maximolocal = 0
            #conta e adiciona a uma lista quantas iterações
            contador2 += 1
            iteracao_randomrestart.append(contador2)
            #continua até os 10 min acabar
            continue
            
        else:

            x2 = initialstate() #cria um novo estado inicial, com a mesma matriz de adjacencia e um novo vetor aleatorio de cores
            current2 = hillclimb(x2) #atual2 recebe os novos dados da subida de encosta para esse novo vetor de cores
            maximolocal = current2.cust #maximo local encontrado
            #contador do timer
            countTimer += sleepTime
            
            
    print('\nO maximo global encontrado dentro de 10 minutos foi: %d' %atual)


#função de reinicio aleatorio
random_restart()
#fim função reinicio aleatorio
fim = time.time()

print('\nTempo de execução: %d' %(fim-ini))
print('\nQuantidade de iterações da função SUBIDA DE ENCOSTA COM REINICIO ALEATORIO: %d' %contador2)

########plot##########

#o eixoy é um vetor adapatado ente 0 ao final do tempo de execução com passos do tempo total de execução dividido pela quantidade
#de iterações
eixoy = numpy.arange(0, (fim-ini), (fim-ini)/contador2) 

#Titulo e labels
matplotlib.pyplot.title('Iteração/Tempo')
matplotlib.pyplot.xlabel('Iterações')
matplotlib.pyplot.ylabel('Tempo')
#plota
matplotlib.pyplot.plot(iteracao_randomrestart, eixoy)
#exibe
matplotlib.pyplot.show()

#iterações e custo
#Titulo e labels
#eixoy2 = numpy.arange(0, len(iteracao_randomrestart), len(iteracao_randomrestart)/len(custo_iteracao_randomrestart)) 
matplotlib.pyplot.title('Iteração/Custo')
matplotlib.pyplot.xlabel('Iteração')
matplotlib.pyplot.ylabel('Custo')
#plota
matplotlib.pyplot.plot(iteracao_randomrestart, custo_iteracao_randomrestart)
#exibe
matplotlib.pyplot.show()
