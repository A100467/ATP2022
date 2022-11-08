#listaAlunos = [aluno1, aluno2, etc]
#aluno = (id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)
import csv
import matplotlib as plt

def leAlunos(filename):
    file = open(filename,encoding="UTF8")
    csv_file = csv.reader(file,delimiter=",") 
    file.readline()
    listaAlunos = []
    for aluno in csv_file:
        listaAlunos.append(tuple(aluno))
    file.close()
    return listaAlunos

listaAlunos=leAlunos("alunos.csv")

def distribCurso(listaAluno):
    dictCurso = {}
    for _,_,curso,*_ in listaAluno:
        if curso in dictCurso.keys():
            dictCurso[curso] += 1
        else:
            dictCurso[curso] = 1
    return dictCurso


def mediaNotas(listaAluno):
    listaMedias = []
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4 in listaAluno:
        media = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))/4   
        if 1 <= media < 4:
            aluno=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"E")
        elif 4 <= media < 8:
            aluno=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"D")
        elif 8 <= media < 12:
            aluno=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"C")
        elif 12 <= media < 16:
            aluno=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"B")
        elif 16 <= media <= 20:           
            aluno=(id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"A") 
    listaMedias.append(aluno)
    return listaMedias


def distribEscalão(listaAlunos):
    dictEscaloes = {}
    for aluno in listaAlunos:
        _,_,_,_,_,_,_,_,escalao = aluno
        if escalao in dictEscaloes.keys():
            dictEscaloes[escalao] = dictEscaloes[escalao] + 1
        else:
            dictEscaloes[escalao] = 1
    return dictEscaloes


def graf(distrib):
    plt.bar(distrib.keys(), distrib.values(), color= "green", width= 0.2)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Gráfico da distribuição")
    plt.ylabel("Número de alunos")
    plt.show()
    return



def menuGráficos():
    print("MENU DE GRÁFICOS")
    menugraf = ("""
1 - Distribuição por Curso
2 - Distribuição por Escalão
0 - Sair
Opção: """)
    opcao = int(input("Introduza a opcao pretendida."))
    while opcao != 0:
        if opcao == 1:
            graf(distribCurso(listaAlunos))
        elif opcao == 2:
            graf(distribEscalão(listaAlunos))
    if opcao == 0:
        print("Escolheu sair do menu.")

