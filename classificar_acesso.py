from carregar_dados import ler_arquivo_csv


X,Y = ler_arquivo_csv()

treino_dados = X[:40]
treino_marcacoes = Y[:40]

teste_dados = X[-40:]
teste_marcacoes = Y[-40:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferenca = resultado - teste_marcacoes

acertos = [ d for d in diferenca if d == 0]

taxaAcertos = len (acertos) / len (teste_marcacoes) *100

print(taxaAcertos)
