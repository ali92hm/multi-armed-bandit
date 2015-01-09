"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""
import numpy as np
from base_algorithm import algorithm

class softmax(algorithm):
	def __init__(self, tau, num_arms, alpha=0.1):
		super(softmax, self).__init__(num_arms, alpha)
		self.tau = tau
		self.tau_func = np.vectorize(lambda i: np.exp(i/self.tau))

	def choose_arm(self):
		exponet_values = self.tau_func(self.rewards)
		probabilities = np.divide(exponet_values, np.sum(exponet_values))
		rand = np.random.rand()
		cumulative_prob = 0.0
		for i in xrange(len(probabilities)):
			cumulative_prob += probabilities[i]
			if cumulative_prob > rand:
				return i