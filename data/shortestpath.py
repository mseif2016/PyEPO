#!/usr/bin/env python
# coding: utf-8

import numpy as np

def genData(num_data, num_features, grid, deg=1, noise_width=0, seed=135):
    """
    generate synthetic data and features for shortest path
    Args:
        num_data: number of data points
        num_features: dimension of features
        grid: size of grid network
        deg: a fixed positive integer parameter
    """
    # set seed
    np.random.seed(seed)
    # number of data points
    n = num_data
    # dimension of features
    p = num_features
    # dimension of the cost vector
    d = (grid[0] - 1) * grid[1] + (grid[1] - 1) * grid[0]
    # random matrix parameter B*
    B = np.random.binomial(1, 0.5, (d,p))
    # positive integer parameter
    assert type(deg) is int, 'deg = {} should be int.'.format(deg)
    assert deg > 0, 'deg = {} should be positive.'.format(deg)
    # feature vectors
    x = np.random.normal(0, 1, (n,p))
    # cost vectors
    c = np.zeros((n,d))
    for i in range(n):
        # cost without noise
        ci = ((np.dot(B, x[i].reshape(p,1)) + 3).T / np.sqrt(p)) ** deg + 1
        # noise
        epislon = np.random.uniform(1-noise_width, 1+noise_width)
        ci *= epislon
        c[i,:] = ci

    return x, c
