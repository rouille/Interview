from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

from interview.algorithm.knn import KNNClassifier, KNNRegressor


def test_knn_classifier():
    data = load_breast_cancer(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(
        data[0], data[1], test_size=1 / 3, random_state=0
    )

    model = {
        "reference": KNeighborsClassifier(n_neighbors=3),
        "actual": KNNClassifier(3),
    }
    predict = {}
    for k in model.keys():
        model[k].fit(x_train, y_train)
        predict[k] = model[k].predict(x_test)

    assert accuracy_score(y_test, predict["reference"]) == accuracy_score(
        y_test, predict["actual"]
    )
    assert all([r == a for r, a in zip(predict["reference"], predict["actual"])])


def test_knn_regressor():
    data = load_diabetes(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(
        data[0], data[1], test_size=1 / 3, random_state=0
    )

    model = {
        "reference": KNeighborsRegressor(n_neighbors=3),
        "actual": KNNRegressor(3),
    }
    predict = {}
    for k in model.keys():
        model[k].fit(x_train, y_train)
        predict[k] = model[k].predict(x_test)

    assert all([r == a for r, a in zip(predict["reference"], predict["actual"])])
