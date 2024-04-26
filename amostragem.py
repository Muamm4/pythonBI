import matplotlib.pyplot as plt
import numpy as np


tamanho_populacao = 10000
np.random.seed(2000)
dados_populacao = np.random.normal(loc=100, scale=10, size=tamanho_populacao)

print(dados_populacao)
# plt.hist(dados_populacao)
# plt.xlabel("Altura arvores")
# plt.ylabel("Quantidade de arvores")
# plt.title("Histograma")


tamanho_amostra = 20
qtd_simulacoes = 10
medias_amostras = []
for x in range(qtd_simulacoes):
    media_amostra = np.random.choice(dados_populacao, size=tamanho_amostra).mean()
    print(media_amostra)
    medias_amostras.append(media_amostra)
medias_amostras = np.array(medias_amostras)

print(medias_amostras)

plt.hist(
    x=medias_amostras,
    bins="auto",
    color="#0705ba",
    alpha=0.7,
    rwidth=0.85,
    density=True,
)
plt.grid(axis="y", alpha=0.80)
plt.xlabel("Médias das alturas das amostras")
plt.ylabel("Frequência de ocorrência")
plt.title("Histograma das Médias das Amostras")
plt.show()
