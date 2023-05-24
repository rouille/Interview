from collections import Counter

import numpy as np


class KNN:
    """The k-nearest neighbors algorithm is a non-parametric, supervised learning
    model, which uses proximity to make classifications or regression. In both cases,
    the input consists of the k closest training examples in a data set.

    :param int k: number of neighbor to consider for classification/regression.
    """

    def __init__(self, k):
        self.k = k

    def fit(self, x_train, y_train):
        """Store training dataset.

        :param list x_train: training dataset. Each training example has several
            features.
        :param list y_train: outcomes of training dataset.
        """
        self.x_train = x_train
        self.y_train = y_train

    def find_neighbors(self, x):
        """Find k-nearest training examples for a test example.

        :param list x: test example.
        :return: (*tuple*) -- closest neighbors. First element is an array of size k
            enclosing the features of the closest neighbors. Second element in array of
            size k enclosing the outcome of the closest neighbors.
        """
        distance = [self.euclidean_distance(x, e) for e in self.x_train]

        id = np.argsort(distance)
        return (self.x_train[id][: self.k], self.y_train[id][: self.k])

    def predict(self, x_test):
        """Predict outcome.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        :raises NotImplementedError: method is implemented in child classes.
        """
        raise NotImplementedError("Implemented in child classes")

    @staticmethod
    def euclidean_distance(a, b):
        """Calculate euclidean distance between two points.

        :param list a: first point.
        :param list b: second point.
        :return: (*float*) -- euclidean distance.
        """
        return np.sqrt(np.sum(np.square([i - j for i, j in zip(a, b)])))


class KNNClassifier(KNN):
    """k-nearest neighbors classifier.

    :param int k: number of neighbor to consider for classification.
    """

    def __init__(self, k):
        super().__init__(k)

    def predict(self, x_test):
        """Predict test examples using most common outcome among k-nearest neighbors.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        """
        neighbors = [self.find_neighbors(e)[1] for e in x_test]
        return [Counter(n).most_common(1)[0][0] for n in neighbors]


class KNNRegressor(KNN):
    """k-nearest neighbors regressor.

    :param int k: number of neighbor to consider for regression.
    """

    def __init__(self, k):
        super().__init__(k)

    def predict(self, x_test):
        """Predict test examples by calculating the mean of the outcomes of the
        k-nearest neighbors.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        """
        neighbors = [self.find_neighbors(e)[1] for e in x_test]
        return [np.mean(n) for n in neighbors]
