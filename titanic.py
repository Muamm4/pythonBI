import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('./conteudo/titanic.csv')

# print(df.head())

 # Analise Exploratoria Inicial
 
print(df.describe().round(1))

plt.hist(df['Sex'])
plt.xlabel("Categoria");
plt.ylabel("Quantidade");
plt.hist(x=df['Sex'],bins='auto', color='green',alpha=0.7,rwidth=0.35, density=True)
plt.grid(axis='y', alpha=0.75)
plt.xlabel("Categória");
plt.ylabel("Quantidade");
plt.title("Histograma de Sobreviventes");
plt.show()
