""" PAYOFFS OF STRATEGIES """

import numpy as np

# payoffs at maturity

def long_call(S, K):
    return np.maximum(S-K, 0)

def short_call(S, K):
    return np.minimum(K-S, 0)

def long_put(S, K):
    return np.maximum(K-S, 0)

def short_put(S,K):
    return np.minimum(S-K, 0)