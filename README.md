#Multi Armed Bandit

This is the algorithm for multi-armed-bandit problem using epsilon_greedy and softmax that tries to maximize the reward given the Gaussian mean of the distributions.


##Usage

###Compilation/Install
```bash
git clone https://github.com/A92hm/multi-armed-bandit.git
```

###Execution
The library code is under the algorithm folder.
But to see how to use the algorithm you can look at the demo.py script.
```bash
python demo.py
```

##Dependencies
* [Python2.7](https://www.python.org/download/releases/2.7/)
* [Numpy](http://www.numpy.org/)
* [Matplotlib](http://matplotlib.org/)

##Structure
    algorithm
    ├── LICENSE
    ├── demo.py                     - Demo of the algorithm in use
    └── algorithm                   - Algorithm implementation
        ├── base_algorithm.py       - Base class for the algorithms
        ├── epsilon_greedy.py       - Epsilon-greedy algorithm
        └── softmax.py              - Softmax algorithm

##Potential Bugs:
* Not known.

##To do
*
* gitignore


##License
[MIT license](http://opensource.org/licenses/MIT)