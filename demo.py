"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""

import numpy as np
from algorithm.softmax import softmax
from algorithm.epsilon_greedy import epsilon_greedy
import matplotlib.pyplot as plt

def simulator(algorithm, arg, mean_arms, std=1, num_sim=2000, num_steps=1000):
	correctness = np.zeros(num_steps)
	optimal_indx = np.argmax(mean_arms)
	for current_sim in xrange(num_sim):
		alg = algorithm(arg, len(mean_arms))
		for t in xrange(num_steps):
			arm_indx = alg.choose_arm()
			reward = np.random.normal(mean_arms[arm_indx], std)
			alg.update_rewards(reward, arm_indx)
			# Measuring correctness
			if optimal_indx == arm_indx:
				correctness[t] += 1
	return np.divide(correctness, num_sim) * 100

def line_plot(data_arrays, xlabel, ylabel, labels, title, f):
	plt.suptitle(title, fontsize=14)
	plots = []
	for data in data_arrays:
		plot, = plt.plot(data)
		plots.append(plot)
	plt.legend(plots, labels, loc=2)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.savefig(f, format="png")
	plt.clf()


if __name__ == '__main__':
	mean_arms = [-2,-1,0,1,2]
	data_arrays = []
	data_arrays.append(simulator(epsilon_greedy, 0.1, mean_arms))
	data_arrays.append(simulator(epsilon_greedy, 0.01, mean_arms))
	data_arrays.append(simulator(softmax, 1 ,mean_arms))
	data_arrays.append(simulator(softmax, 10 ,mean_arms))

	line_plot(data_arrays, 'Steps', 'Average percent optimal action', ['Epsilon greedy: 0.1', 'Epsilon greedy: 0.01','Softmax: 1', 'Softmax: 10'], 'N-Armed Bandit', open('q3-2.png','wb'))
