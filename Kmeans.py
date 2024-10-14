import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from adjustText import adjust_text

iris_data = pd.read_csv("iris.csv")
# print(iris_data.head())

# select data
sepal_data = iris_data[['sepal.length', 'sepal.width']]
# print(sepal_data.head())

# standardization
scaler = StandardScaler().fit(sepal_data)
std_sepal_data = scaler.transform(sepal_data)
# print(std_sepal_data)

# model
kmeans = KMeans(n_clusters=3).fit(std_sepal_data)

# model data
labels = kmeans.labels_
# print(labels)
centroids = kmeans.cluster_centers_
# print(centroids)

# test data
test_data = np.array([[4.6, 3.0, 1.5, 0.2], [6.2, 3.0,4.1,1.2]])
std_test_sepal_data = scaler.transform(test_data[:, [0,1]])
# print(std_test_sepal_data)

# prediction
prediction = kmeans.predict(std_test_sepal_data)
print(prediction)

v_short = list(iris_data['v_short'])

# plot
plt.title("Scatter plot of Sepal data")
plt.scatter(std_sepal_data[:, 0], std_sepal_data[:, 1], c = labels.astype(float), alpha=0.5)
plt.scatter(std_test_sepal_data[:, 0], std_test_sepal_data[:, 1], c = "black")
plt.scatter(centroids[:, 0], centroids[:, 1], c="red", alpha=0.8)
for i, txt in enumerate(prediction):
    plt.annotate(txt, (std_test_sepal_data[:, 0][i], std_test_sepal_data[:, 1][i]))

annotations = []
for i,(label, letter) in enumerate(zip(labels, v_short)):
    annotations.append(plt.annotate(xy = (std_sepal_data[:, 0][i],std_sepal_data[:, 1][i]), text = '{},{}'.format(label, letter)))
adjust_text(annotations, arrowprops = dict(arrowstyle="->"))
plt.show()


