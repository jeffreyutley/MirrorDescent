import MirrorDescent
import numpy as np
import demo_utils
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


"""Implements example 9.10 from Chapter 9 of ``First-Order Methods in Optimization`` by Amir Beck, where the
function f is chosen to be f(x) = ||Ax - b||_2 and the set C is chosen to be the simplex in R^n."""

# size of the problem
n = 10

# random linear system whose solution is in the simplex
np.random.seed(0)
F = np.random.normal(size=(n, n))
A = np.dot(F, F.T) + 0.1*np.identity(n)         # symmetric positive-definite matrix
b = np.random.normal(size=(n, ))
y = np.linalg.solve(A, b)
epsilon = 2 * np.abs(np.min(y))
sigma = np.sum(y + epsilon)
b = (b + epsilon * np.dot(A, np.ones(n))) / sigma
y = (y + epsilon) / sigma
y_new = np.linalg.solve(A, b)                   # solution


# objective function
def f(x):
    return np.linalg.norm(np.dot(A, x) - b, ord=1)


# derivative of objective function
def f_derivative(x):
    error = np.dot(A, x) - b
    n = len(error)
    sign = np.zeros((n, ))

    for idx in range(n):
        if error[idx] > 0:
            sign[idx] = 1
        elif error[idx] < 0:
            sign[idx] = -1
        else:
            sign[idx] = 0

    return np.dot(A.T, sign)


# random initial guess
x_0 = np.abs(np.random.normal(size=(n, )))
x_0 /= np.sum(x_0)

num_iter = 1_000_000

# run Mirror descent with negative entropy Bergman distance L_1 norm
mirror_descent_values, function_values = MirrorDescent.mirror_descent(x_0, MirrorDescent.negative_entropy_update, f,
                                                                      num_iter, f_derivative=f_derivative)

# find derivative value norms and absolute errors at each mirror descent value:
derivative_2_norms = np.zeros((num_iter,))
derivative_1_norms = np.zeros((num_iter, ))
absolute_errors = np.zeros((num_iter, ))
for idx in range(derivative_2_norms.shape[0]):
    derivative_2_norms[idx] = np.linalg.norm(f_derivative(mirror_descent_values[idx]))
    derivative_1_norms[idx] = np.linalg.norm(f_derivative(mirror_descent_values[idx]), ord=1)
    absolute_errors[idx] = np.linalg.norm(mirror_descent_values[idx] - y_new)

# plot of function values
plt.plot(function_values)
plt.title("Values $\\|Ax^{(k)}-b\\|_1$ from Mirror Descent")
plt.xlabel("k")
plt.ylabel("$\\|Ax^{(k)}-b\\|_1$")
plt.yscale('log')
plt.xscale('log')
plt.savefig('./output/Example_9.19_function_values.png')

# plot of 2-norm of derivative values
matplotlib.rcParams['agg.path.chunksize'] = 10000
plt.figure()
plt.plot(derivative_2_norms)
plt.title("Derivative Values $\\|\\nabla_x f(x^{(k)})\\|_2 = \\|A^T sign(Ax^{(k)}-b)\\|_2$ from Mirror Descent")
plt.xlabel("k")
plt.ylabel("$\\|\\nabla_x f(x^{(k)})\\|_2$")
plt.yscale('log')
plt.xscale('log')
plt.savefig('./output/Example_9.19_derivative_2_norms.png')

# plot of 1-norm of derivative values
matplotlib.rcParams['agg.path.chunksize'] = 10000
plt.figure()
plt.plot(derivative_1_norms)
plt.title("Derivative Values $\\|\\nabla_x f(x^{(k)})\\|_1 = \\|A^T sign(Ax^{(k)}-b)\\|_1$ from Mirror Descent")
plt.xlabel("k")
plt.ylabel("$\\|\\nabla_x f(x^{(k)})\\|_1$")
plt.yscale('log')
plt.xscale('log')
plt.savefig('./output/Example_9.19_derivative_1_norms.png')

# plot of the 2-norm of the absolute errors
matplotlib.rcParams['agg.path.chunksize'] = 10000
plt.figure()
plt.plot(absolute_errors)
plt.title("Absolute Errors $\\|x^{(k)} - x_*\\|_2$ from Mirror Descent")
plt.xlabel("k")
plt.ylabel("$\\|x^{(k)} - x_*\\|_2$")
plt.yscale('log')
plt.xscale('log')
plt.savefig('./output/Example_9.19_absolute_errors.png')
