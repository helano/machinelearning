import pandas as pd

from collections import Counter


dados = pd.read_csv('buscas.csv')

X_DF = dados[['home', 'busca', 'logado']]
Y_DF = dados['comprou']
XDummies_DF = pd.get_dummies(X_DF)
YDummies_DF = Y_DF

X = XDummies_DF.values
Y = YDummies_DF.values

porcentagem_dados_treino = 0.9

quantidade_dados_treino = int (porcentagem_dados_treino * len(Y))
quantidade_dados_teste = int (len(Y) - quantidade_dados_treino)

dados_treino = X[:quantidade_dados_treino]
marcacoes_treino = Y[:quantidade_dados_treino]

dados_teste = X[-quantidade_dados_teste:]
marcacoes_teste = Y[-quantidade_dados_teste:]

chuta_1 = len(Y[Y==1])
chuta_0 = len(Y[Y==0])

acerto_base = 0
taxa_acerto_base = max(Counter(marcacoes_teste).values()) / len(marcacoes_teste) * 100.0

print("dados treino", len(dados_treino))
print("marcacoes treino", len(marcacoes_treino ))
print("dados teste", len(dados_teste))
print("marcacoes teste", len(marcacoes_teste))

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados_treino, marcacoes_treino)



resultado = modelo.predict(dados_teste)

diferenca = resultado == marcacoes_teste

acertos = sum(diferenca)

taxaAcertos =acertos*100.0/len(marcacoes_teste)

print("taxa e acertos base ", taxa_acerto_base)
print("taxa  de acerto MultinomialNB ", taxaAcertos)
