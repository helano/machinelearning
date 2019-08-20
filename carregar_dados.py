import csv

def ler_arquivo_csv():

    dados = []
    marcacoes =[]

    arquivo = open ('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, funciona, contato, comprou in leitor:
        dados.append([int(home), int(funciona), int(contato)])
        marcacoes.append(int(comprou))

    return dados, marcacoes
