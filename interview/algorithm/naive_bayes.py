from collections import Counter

import numpy as np


class NaiveBayes:
    """Naive Bayes methods are a set of supervised learning algorithms based on
    applying Bayes’ theorem with the “naive” assumption of conditional independence
    between every pair of features given the value of the class variable.
    """

    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.classes = None

    def fit(self, x_train, y_train):
        """Store training dataset.

        :param list x_train: training dataset. Each training example has several
            features.
        :param list y_train: outcomes of training dataset.
        """
        self.x_train = x_train
        self.y_train = y_train
        self.classes = list(set(y_train))

    def arrange(self):
        """Group training examples by class

        :return: (*dict*) -- dictionary giving training examples for each class.
        """
        return {c: self.x_train[np.where(self.y_train == c)] for c in self.classes}

    def calculate_prior(self):
        """The prior, P(y), of each class can be calculated as the relative frequency
        of the class in the training set.

        :return: (*dict*) -- dictionary giving relative frequency of each class in
            training set.
        """
        return {k: v / len(self.y_train) for k, v in Counter(self.y_train).items()}

    def predict(self, x_test):
        """Predict outcome.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        :raises NotImplementedError: method is implemented in child classes.
        """
        raise NotImplementedError("Implemented in child classes")


class GaussianNaiveBayes(NaiveBayes):
    """Implements the Gaussian Naive Bayes algorithm for classification. The
    likelihood of the features is assumed to be Gaussian.
    """

    def __init__(self):
        super().__init__()

    def mean(self):
        """Calculate mean of features for each class.

        :return: (*dict*) -- keys are classes' name, values are features' mean.
        """
        return {c: np.mean(f, axis=0) for c, f in self.arrange().items()}

    def variance(self):
        """Calculate variance of features for each class.

        :return: (*dict*) -- keys are classes' name, values are features' variance.
        """
        return {c: np.var(f, axis=0) for c, f in self.arrange().items()}

    def log_likelihood(self, example, mean, var):
        """Calculate probability of observing the example. The feature is assumed to be
        Gaussian distributed.

        :param float example: example of a feature.
        :return: (*numpy.ndarray*) -- probability of example.
        """
        return -0.5 * (pow(example - mean, 2) / var + np.log(2 * np.pi * var))

    def predict(self, x_test):
        """Predict test examples using Maximum A Posteriori (MAP) estimation.

        :param list x_test: test dataset. Each test example has the same number of
            features than a training example.
        """
        mean = self.mean()
        var = self.variance()
        prior = self.calculate_prior()
        prediction = []
        for example in x_test:
            log_posterior = [
                np.log(prior[c])
                + np.sum(
                    [
                        self.log_likelihood(f, mean[c][i], var[c][i])
                        for i, f in enumerate(example)
                    ]
                )
                for c in self.classes
            ]
            prediction.append(self.classes[np.argmax(log_posterior)])

        return prediction
