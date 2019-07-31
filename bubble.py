from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
 
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
  
def desenhaGrafico(x,y,y2,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,y2, label = "Melhor Tempo 2")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
  
def desenhaGrafico2(x,y,y2,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,y2, label = "Melhor Tempo 2")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph2.png')



def bubble(v):
    while(True):
        changed=False

        for i in range(len(v) - 1):

            if v[i] > v[i+1]:
                v[i],v[i+1]=v[i+1],v[i]
                changed=True

        if(changed==False):
            break
    return v

k=geraLista(20)
print(k)
print(bubble(k))

listas=[]
x2 = [1000,2000,5000,10000]
y = []
y2= []
for i in range(4):
  listas.append(geraLista(x2[i]))

for i in range(4):
  y.append(timeit.timeit("bubble({})".format(listas[i]),setup="from __main__ import bubble",number=1)) 
  y2.append(timeit.timeit("bubble({})".format(listas[i]),setup="from __main__ import bubble",number=1)) 

desenhaGrafico(x2,y,y2)
y=[]
y2=[]

for i in range(4):
  y.append(timeit.timeit("bubble({})".format(listas[i]),setup="from __main__ import bubble",number=1)) 
  y2.append(timeit.timeit("bubble({})".format(listas[i]),setup="from __main__ import bubble",number=1))

desenhaGrafico2(x2,y2,y)
