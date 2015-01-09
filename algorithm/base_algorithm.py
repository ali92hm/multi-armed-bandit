"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""
import numpy as np

class algorithm(object):
	def __init__(self, num_arms, alpha):
		self.alpha = alpha
		self.num_arms = num_arms
		self.rewards = np.zeros(num_arms)

	def choose_arm(self):
		pass

	def update_rewards(self,  new_reward, arm_indx):
		self.rewards[arm_indx] += self.alpha * (new_reward - self.rewards[arm_indx])