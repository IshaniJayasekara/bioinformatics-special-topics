
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris_data = load_iris()

labels = iris_data.target

# stadardize iris dataset
scaler = StandardScaler().fit(iris_data.data[:, 0:4])
std_iris_data = scaler.transform(iris_data.data[:, 0:4])

# separate sepal data
std_sepal_data = std_iris_data[:, [0,1]]

# model
knn = KNeighborsClassifier(n_neighbors=3).fit(std_sepal_data, labels)

# test data
test_data = np.array([[4.6, 3.0, 1.5, 0.2],[6.2, 3.0,4.1,1.2]])

# std test data
std_test_data = scaler.transform(test_data)

# std sepal data
std_test_sepal_data = std_test_data[:,[0,1]]

# prediction
prediction = knn.predict(std_test_sepal_data)
print(prediction)

prob_predict = knn.predict_proba(std_test_sepal_data)
print(prob_predict)

species_name = iris_data.target_names[prediction]
print(species_name)

neighbor_distances, neighbor_indices = knn.kneighbors(std_test_sepal_data)
print(neighbor_indices)

neighbor_data = iris_data.data[neighbor_indices]
print(neighbor_data)

neighbors_labels = iris_data.target[neighbor_indices]
print(neighbors_labels)

neighbor_species = iris_data.target_names[neighbors_labels]
print(neighbor_species)

