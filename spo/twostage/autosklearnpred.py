#!/usr/bin/env python
# coding: utf-8
"""
Two-stage model with Scikit-learn predictor
"""

import numpy as np
from autosklearn.regression import AutoSklearnRegressor


class autoSklearnPred:
    """
    Two-stage prediction and optimization with auto-sklearn.

    Args:
        omodel (optModel): optimization model
    """

    def __init__(self, omodel):
        self.predictor = AutoSklearnRegressor(time_left_for_this_task=600,
                                              per_run_time_limit=30)
        self.optimizer = omodel
        self.trained = False

    def fit(self, x, c):
        """
        A method to fit training data

        Args:
            x (ndarray): features
            c (ndarray): costs for objective fucntion
        """
        if not (len(c.shape) == 2 and c.shape[-1] == self.optimizer.num_cost):
            raise ValueError("Dimension of cost does not macth.")
        self.predictor.fit(x, c)
        self.trained = True

    def predict(self, x):
        """
        A method to predict

        Args:
            x (ndarray): features

        Returns:
            ndarray: predicted cost
        """
        if not self.trained:
            raise RuntimeError("Model is not fitted yet.")
        cp = self.predictor.predict(x)
        return np.array(cp)