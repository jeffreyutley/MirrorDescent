import MirrorDescent
import numpy as np
import demo_utils
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

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
    return np.linalg.norm(np.dot(A, x) - b)


# derivative of objective function
def f_derivative(x):
    return np.dot(A.T, np.dot(A, x) - b)


# random initial guess
x_0 = np.abs(np.random.normal(size=(n, )))
x_0 /= np.sum(x_0)

# run Mirror descent with negative entropy Bergman distance L_1 norm
mirror_descent_values, function_values = MirrorDescent.mirror_descent(x_0, MirrorDescent.negative_entropy_update, f,
                                                                      1_000_000, f_derivative=f_derivative)

plt.plot(function_values)
plt.title("Values $\\|Ax^{(k)}-b\\|$ from Mirror Descent")
plt.xlabel("k")
plt.ylabel("$\\|Ax^{(k)}-b\\|$")
plt.yscale('log')
plt.xscale('log')
plt.show()
