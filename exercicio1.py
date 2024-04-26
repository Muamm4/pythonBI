import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

amostra = pd.read_csv("./conteudo/wine_dataset.csv")

arq = amostra.head()
y = amostra["style"]
x = amostra.drop("style", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

modelo = GaussianNB()
modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_teste, y_teste)

print("Acurácia: ", resultado, "\n")

real = y_teste[200:207]
# print(real)

pre = modelo.predict((x_teste[200:207]))
# print(pre)

for index_i, value_i in enumerate(pre):
    for index_j, value_j in enumerate(real):
        if index_i == index_j:
            print('TESTE: ', index_i + 1)
            if value_i == value_j:
                print("predict: ", value_i)
                print("real: ", value_j)
                print("Result: Correct")
            else:
                print("predict: ", value_i)
                print("real: ", value_j)
                print("Result: Wrong")
            print()