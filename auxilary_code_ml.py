import numpy as np
from sklearn import datasets
import pickle
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target
    np.unique(iris_y)

    # Split iris data in train and test data
    # A random permutation, to split the data randomly
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    # Create and fit a nearest-neighbor classifier
    knn_model = KNeighborsClassifier()
    knn_model.fit(iris_X_train, iris_y_train)

    # save the knn_model to disk
    filename = 'Our_Trained_knn_model.sav'
    pickle.dump(knn_model, open(filename, 'wb'))

    # load the model from disk
    filename = 'Our_Trained_knn_model.sav'
    knn_model_reloaded = pickle.load(open(filename, 'rb'))
    knn_model_reloaded = knn_model

    prediction = knn_model_reloaded.predict(iris_X_test)

    print(iris_y_test)
