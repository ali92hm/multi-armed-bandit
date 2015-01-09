"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""
import numpy as np
from base_algorithm import algorithm

class epsilon_greedy(algorithm):
	def __init__(self, epsilon, num_arms, alpha=0.1):
		super(epsilon_greedy, self).__init__(num_arms, alpha)
		self.epsilon = epsilon

	def choose_arm(self):
		if np.random.rand() > self.epsilon:
			return np.argmax(self.rewards)
		else:
			return np.random.randint(self.num_arms) 