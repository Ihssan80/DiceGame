## Table of Contents
- [Overview](#overview)
- [Techniques Used](#techniques-used)
- [Functions and Variables](#functions-and-variables)
- [Discount Rate and Threshold Tuning with Results](#discount-rate-and-threshold-tuning-with-results)

## Overview
The `MyAgent` class is a custom agent for playing a dice game. It inherits from the `DiceGameAgent` class and implements the value iteration algorithm to find the best policy for the game.

## Techniques Used
The `MyAgent` class utilizes the following techniques:

1. **Value Iteration**: The agent uses the value iteration algorithm to find the best policy for the dice game. Value iteration is an iterative process that calculates the value state function for each state in the game.

2. **Discount Rate**: The agent incorporates a discount rate to account for the difference in the value of rewards received at different time steps. The discount rate, denoted by `discount_rate`, determines the weightage given to future rewards.

3. **Threshold**: The agent uses a threshold value, denoted by `threshold`, to determine convergence during the value iteration process.

## Functions and Variables

### Class Initialization

#### `__init__(self, game, discount_rate=0.9, threshold=0.1)`

- **Parameters**:
    - `game`: The dice game instance that the agent will play.
    - `discount_rate`: The discount rate used in the value iteration algorithm. (Default: 0.9)
    - `threshold`: The convergence threshold for the value iteration algorithm. (Default: 0.1)

The `__init__` function initializes the `MyAgent` object. It sets the discount rate, threshold, and initializes the dictionaries for states values and best policy. It also calls the superclass constructor and initializes the state values using the `__initialize_states_values` function. Finally, it invokes the `__value_iteration` function to find the best policy.

### Private Methods

#### `__initialize_states_values(self)`

This private method initializes the state values for each state in the game to zero. It iterates over all states and sets their corresponding values to zero in the `_states_values` dictionary.

#### `__value_iteration(self)`

This private method implements the value iteration algorithm to find the best policy. It iteratively updates the state values until convergence is achieved. For each state, it calculates the value state function by considering all possible actions and their resulting states. The best action for each state is chosen based on the maximum value state function. The method updates the `_best_policy` dictionary with the best action for each state.

### Public Method

#### `play(self, state)`

- **Parameters**:
    - `state`: The current state of the game.

This method returns the best action (policy) to take in the given state. It retrieves the best policy from the `_best_policy` dictionary based on the provided state.

## Discount Rate and Threshold Tuning with Results

Below are some outputs from executing `MyAgent`:

- Testing basic rules falls between (12.2 and 14) with a total time less than 0.3 seconds.
- Testing extended rules scores in the range of 4 and 4.5 with a total time of zero seconds.

Here are some examples:

### Testing basic rules (1)

- Game 0 score: 11
- Game 1 score: 14

##### Game 2 score: 13
##### Game 3 score: 11
##### Game 4 score: 13
##### Game 5 score: 13
##### Game 6 score: 12
##### Game 7 score: 12
##### Game 8 score: 16
##### Game 9 score: 11

###### Average score: 12.6
###### Total time: 0.2031 seconds


Testing basic rules. (2)

##### Game 0 score: 11
##### Game 1 score: 15
##### Game 2 score: 18
##### Game 3 score: 12
##### Game 4 score: 14
##### Game 5 score: 10
##### Game 6 score: 15
##### Game 7 score: 17
##### Game 8 score: 15
##### Game 9 score: 12



###### Average score: 13.9
###### Total time: 0.1562 seconds




Testing extended rules – two three-sided dice. (1)

##### Game 0 score: 5
##### Game 1 score: 6
##### Game 2 score: 4
##### Game 3 score: 4
##### Game 4 score: 4
##### Game 5 score: 2
##### Game 6 score: 3
##### Game 7 score: 4
##### Game 8 score: 5
##### Game 9 score: 6

###### Average score: 4.3
###### Average time: 0.00000 seconds


Testing extended rules – two three-sided dice. (2)

##### Game 0 score: 3
##### Game 1 score: 4
##### Game 2 score: 4
##### Game 3 score: 4
##### Game 4 score: 4
##### Game 5 score: 4
##### Game 6 score: 4
##### Game 7 score: 4
##### Game 8 score: 5
##### Game 9 score: 5

###### Average score: 4.1
###### Average time: 0.00000 seconds