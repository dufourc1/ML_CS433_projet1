'''
functions to implement least squares using gradient descent, stochastic gradient descent or normal equation

All functions return (w,loss), which is the last weight vector of the method and the corresponding loss
'''

import numpy as np

from costs import *
from gradient_descent import *
from stochastic_gradient_descent import *
from data_utility import *

#************************************************
#LEAST SQUARES
#------------------------------------------------

def least_squares_GD(y, tx, initial_w, max_iters, gamma):
    # Define parameters to store w and loss
    w = initial_w
    for n_iter in range(max_iters):
        # compute loss, gradient
        grad, err = compute_gradient(y, tx, w)
        loss = calculate_mse(err)
        # gradient w by descent update
        w = w - gamma * grad
        #print("Gradient Descent({bi}/{ti}): loss={l}, w0={w0}, w1={w1}".format(bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    return (w,loss)

def least_squares_SGD(y, tx, initial_w,max_iters, gamma):

    return (w,loss)

def least_squares(y, tx):
    """
    Calculate the least squares solution.
    Returns w.
    """
    w = np.linalg.solve(tx.T.dot(tx),tx.T.dot(y))

    return w, compute_mse(error(y,tx,w))

#**************************************************
# RIDGE REGRESSION
#--------------------------------------------------

def ridge_regression(y, tx, lambda_):
    """implement ridge regression.
    Returns w."""
    a = tx.T.dot(tx) + 2*tx.shape[0]*lambda_*np.identity(tx.shape[1])

    return np.linalg.solve(a,tx.T.dot(y))

#**************************************************
# CROSS VALIDATION
#--------------------------------------------------

def cross_validation(y, x, k_indices, k, lambda_, degree):
    """return the loss of ridge regression."""

    # get k'th subgroup in test, others in train: DONE
    x_te = x[k_indices[k]]
    x_te = x[k_indices[k]]
    y_te = y[k_indices[k]]
    k_complement = np.ravel(np.vstack([k_indices[:k],k_indices[k+1:]]))
    x_tr = x[k_complement]
    y_tr = y[k_complement]

    # form data with polynomial degree: DONE
    x_te = build_poly(x_te, degree)
    x_tr = build_poly(x_tr, degree)

    # ridge regression: DONE
    w = ridge_regression(y_tr, x_tr, lambda_)

    # calculate the loss for train and test data: DONE
    loss_tr = compute_RMSE(y_tr, x_tr, w)
    loss_te = compute_RMSE(y_te, x_te, w)

    return loss_tr, loss_te
