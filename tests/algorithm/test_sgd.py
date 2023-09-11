import numpy as np
import pytest

from interview.algorithm.sgd import SGD


def ssr_gradient(x, y, beta):
    """Gradient of the sum of squared residuals (SSR) for linear regression."""
    error = np.matmul(x, beta) - y
    gradient = np.matmul(x.T, error) / y.shape[0]

    return gradient


def ols(x, y):
    """Ordinary least squares to analytically estimate the linear regression parameters
    and the variance-covariance matrix of the estimates."""
    beta_hat = np.matmul(
        np.matmul(
            np.linalg.inv(np.matmul(np.array(x).transpose(), np.array(x))),
            x.transpose(),
        ),
        y,
    )
    # Use sample variance to estimate variance of the error
    error = y - np.matmul(x, beta_hat)
    var_error = sum(error**2) / (y.shape[0] - x.shape[1])
    cov_beta_hat = var_error * np.linalg.inv(np.matmul(x.transpose(), x))

    return beta_hat, cov_beta_hat


def test_sgd_linear_regression(capfd):
    n, k = 100, 2
    beta = np.array([1, 1, 10])
    x = np.concatenate([np.ones((n, 1)), np.random.randn(n, k)], axis=1)
    y = np.matmul(x, beta) + np.random.randn(n)

    sgd = SGD(
        learning_rate=0.01,
        decay_rate=0.8,
        max_iteration=10000,
        batch_size=10,
        seed=0,
        tolerance=1e-6,
    )
    sgd.fit(ssr_gradient, x, y, n_var=3)
    beta_sgd = sgd.get_params()

    beta_hat, cov_beta_hat = ols(x, y)
    for i in range(k + 1):
        assert (
            beta_hat[i] - np.sqrt(cov_beta_hat[i, i])
            <= beta_sgd[i]
            <= beta_hat[i] + np.sqrt(cov_beta_hat[i, i])
        )
    sgd.print_fit_info()
    out, err = capfd.readouterr()
    assert out == "max iteration reached\n"
