import numpy as np


class SGD:
    """Batch Stochastic Gradien Descent iterative optimization process. It is one of
    the most used methods for identifying the parameters of the model that minimize the
    cost function in machine learning algorithms.

    :param float learning_rate: factor controlling the magnitude of the vector update.
    :param float decay_rate: factor setting contribution of the previous update.
    :param float max_iteration: number of iterations.
    :param float batch_size: size of minibatches.
    :param float tolerance: minimal allowed movement in each iteration.
    :param int seed: seed to randomly select observations for minibatches.
    """

    def __init__(
        self,
        learning_rate=0.01,
        decay_rate=0,
        max_iteration=1000,
        batch_size=1,
        tolerance=1e-3,
        seed=None,
    ):
        self.learning_rate = learning_rate
        self.decay_rate = decay_rate
        self.max_iteration = max_iteration
        self.batch_size = batch_size
        self.tolerance = tolerance
        self.seed = seed

        self.var = None
        self.info = {"iteration": self.max_iteration}

    def fit(self, gradient, x, y, n_var, var=None):
        """Perform gradient descent

        :param func gradient: gradient of the cost function.
        :param np.ndarray x: observation inputs.
        :param np.ndarray y: outputs.
        :param int n_var: number of decision variables.
        :param np.ndarray var: starting value of decision variables.
        """
        rng = np.random.default_rng(self.seed)
        self.var = rng.normal(size=n_var) if var is None else np.array(var)

        n = x.shape[0]
        diff = 0
        for i in range(1, self.max_iteration + 1):
            idx = rng.permutation(n)
            x, y = x[idx], y[idx]
            for start in range(0, n, self.batch_size):
                stop = start + self.batch_size
                x_batch, y_batch = x[start:stop], y[start:stop]
                grad = np.array(gradient(x_batch, y_batch, self.var))
                diff = self.decay_rate * diff - self.learning_rate * grad

                if np.linalg.norm(grad) < self.tolerance:
                    self.info["iteration"] = i
                    break

                self.var += diff

    def get_params(self):
        """Get parameters of that minimize the cost function

        :return: (*np.ndarray*) -- value of paramters
        """
        return self.var

    def print_fit_info(self):
        """Get information on the fit."""
        if self.info["iteration"] != self.max_iteration:
            print(f"tolerance met after {self.info['iteration']} iteration")
        else:
            print("max iteration reached")
