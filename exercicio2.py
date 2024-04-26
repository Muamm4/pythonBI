from sklearn.cluster import KMeans
import numpy as num
import matplotlib.pyplot as plt

num1 = num.random.randint(25,40, size=(10))
num2 = num.random.randint(10,20, size=(10))
dados = list(zip(num2, num1))
print(dados)

kmeans = KMeans(n_clusters=3,random_state=0)

kmeans.fit(dados)

plt.xlabel("x")
plt.ylabel("y")
plt.title("K-means - 3 Clusters")
plt.scatter(num2, num1, c=kmeans.labels_, cmap='rainbow')
plt.show()