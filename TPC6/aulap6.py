import csv
import matplotlib.pyplot as plt

def leobras(filename):
    file = open(filename,encoding="UTF8")
    file.readline()      
    csv_file = csv.reader(file,delimiter=";") 
    lista = []
    for obra in csv_file:
        lista.append(tuple(obra)) 
    return (lista)
#(2)
def tamanhoObras(obras):
    return len(obras)
#(1)
def imprime(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Composição':15} |")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")


def ordem1(tuplo):        
    return tuplo[0]

def ordem2(tuplo):
    return tuplo[1]
#(3)
def titAno(obras):
    lista = []                                        
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))
    lista.sort(key = ordem1)
    return lista

#(4)
def titAno_2(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))
    lista.sort(key = lambda tuplo: tuplo[1])
    return lista
#(5)
def titporAno(obras):
    dict = {}
    for nome, _, ano, *_ in obras:
        if ano in dict.keys():
            dict[ano].append(nome)
        else:
            dict[ano] = [nome]
    return dict
#(6)
def ordemCompositores(obras):
    listaCompositores = []
    for _, _, _, _, compositor, *_ in obras:
        listaCompositores.append(compositor)
    listaCompositores.sort()
    return listaCompositores
#(7)
def distPeriodo(obras):
    dict = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dict.keys():  
            dict[periodo] += 1
        else:
            dict[periodo] = 1
    return dict
#(8)
def distAno(obras):         
    dict = {}                      
    for _, _, ano, _, *_ in obras: 
        if ano in dict.keys():        
            dict[ano] += 1 
        else:
            dict[ano] = 1      
    return dict 
#(9)
def distCompositor(obras):
    dict = {}
    for _, _, _, _, compositor, *_ in obras:
        if compositor in dict.keys():  
            dict[compositor] += 1
        else:
            dict[compositor] = 1
    return dict

def distplot(distrib):
    plt.bar(distrib.keys(), distrib.values(), color = 'green')
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.title("Gráfico da distribuição das obras")
    plt.show()
    return
#(10)
def desenhograficos(obras):
    print( """ Menu de gráficos
    1) Distribuição das obras por período
    2) Distribuição das obras por ano
    3) Distribuição das obras por compositor
    """)
    opc = int(input("Introduza o valor correspondente ao gráfico de deseja observar."))
    if opc == 1:
        distplot(distPeriodo(obras))
    elif opc == 2:
        distplot(distAno(obras))
    elif opc == 3:
        distplot(distCompositor(obras))
#(11)
def titPorCompositor(obras):
    listaCompositores = []
    dic = {}
    for nome, _, _, _, compositor, *_ in obras:
        if compositor in dic:
            dic[compositor].append(nome)
        else:
            dic[compositor] = [nome]
    for comp in dic:
        listaCompositores.append((comp,dic[comp]))
    return listaCompositores
