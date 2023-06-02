import random

import numpy as np


class KMeans:
    """The k-means algorithm is a unsupervised clustering algorithm that segments a
    dataset into k-groups based on similarity of the features of the data points.

    :param int k: number of clusters.
    """

    def __init__(self, k):
        self.k = k

    def fit(self, x_train):
        """Calculate centroids using sampling based on an empirical probability
        distribution of the points’ contribution to the overall inertia:

            + Select first centroid randomly from one of the data points.
            + Calculate the sum of the distances between each data point and centroids.
            + Select next centroid randomly, with probability proportional to the total
              distance to the centroids.
            + Repeat until all centroids have been initialized.

        param list x_train: training dataset. Each training example has several
            features.
        """

        self.centroid = [random.choice(x_train)]
        for _ in range(self.k - 1):
            distance = np.sum(
                [
                    [self.euclidean_distance(c, e) for c in self.centroid]
                    for e in x_train
                ],
                axis=1,
            )
            self.centroid += random.choices(x_train, weights=distance)

    def predict(self, x_test):
        """Predict the closest cluster each example in test dataset belongs to.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        :return: (*list*) -- the index of closest cluster.
        """
        distance = [
            [self.euclidean_distance(c, e) for c in self.centroid] for e in x_test
        ]
        return np.argmin(distance, axis=1)

    @staticmethod
    def euclidean_distance(a, b):
        """Calculate euclidean distance between two points.

        :param list a: first point.
        :param list b: second point.
        :return: (*float*) -- euclidean distance.
        """
        return np.sqrt(np.sum(np.square([i - j for i, j in zip(a, b)])))
