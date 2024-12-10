import numpy as np


def mirror_descent(x_0, update_function, f, max_num_iter, tol=None, x_true=None, **kwargs):
    """Runs mirror descent for a specific problem until convergence or the maximum number of iterations is met.

    :param x_0: Numpy 1-D array containing the initial guess
    :param update_function: (function)
    :param max_num_iter:
    :param tol:
    :param x_true:
    :return:
    """

    check_convergence = (tol is not None) * (x_true is not None)

    x = x_0

    num_iterations = 0

    x_values = np.zeros((max_num_iter, len(x)))
    function_values = np.zeros((max_num_iter, ))

    for iteration in range(max_num_iter):
        x = update_function(iteration, x, **kwargs)
        x_values[iteration] = x
        function_values[iteration] = f(x)
        if check_convergence:
            relative_error = np.linalg.norm(x - x_true) / np.linalg.norm(x_true)
            if relative_error < tol:
                x_values = x_values[:iteration]
                break

    return x_values, function_values


def negative_entropy_step_size(iteration, x, f_derivative):
    return np.sqrt(2) / (np.linalg.norm(f_derivative(x), ord=np.inf) * np.sqrt(iteration+1))


def negative_entropy_update(iteration, x, **kwargs):
    assert ('f_derivative' in kwargs.keys())

    f_derivative = kwargs['f_derivative']

    f_prime = f_derivative(x)

    step_size = negative_entropy_step_size(iteration, x, f_derivative)

    exponential_factor = np.exp(-step_size * f_prime)

    x_new_not_normalized = np.multiply(x, exponential_factor)

    x_new = x_new_not_normalized / np.sum(x_new_not_normalized)

    return x_new
