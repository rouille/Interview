from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from interview.algorithm.naive_bayes import GaussianNaiveBayes


def test_naive_bayes():
    data = load_iris(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(
        data[0], data[1], test_size=0.5, random_state=0
    )

    model = {
        "reference": GaussianNB(),
        "actual": GaussianNaiveBayes(),
    }
    predict = {}
    for k in model.keys():
        model[k].fit(x_train, y_train)
        predict[k] = model[k].predict(x_test)

    assert accuracy_score(y_test, predict["reference"]) == accuracy_score(
        y_test, predict["actual"]
    )
    assert all([r == a for r, a in zip(predict["reference"], predict["actual"])])
