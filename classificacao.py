porco1 =    [1,1,0]
porco2 =    [1,1,0]
porco3 =    [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados =[porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
marcacoes = [1,1,1,-1,-1,-1]

from  sklearn.naive_bayes import MultinomialNB

cachorroTeste = [0,0,1]
porcoTeste =    [1,1,0]
porcoTeste2 =   [0,1,0]

dataset = [cachorroTeste, porcoTeste, porcoTeste2]

graoundTruth = [-1,1,1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
resultado = modelo.predict(dataset)
print(resultado)
print (graoundTruth)

diferenca = graoundTruth - resultado

print (diferenca)

acertos = [d for d in diferenca if d==0]

taxaAcertos = len(acertos) / len(graoundTruth) * 100

print(taxaAcertos, " %")
