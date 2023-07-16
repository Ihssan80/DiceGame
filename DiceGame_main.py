"""
Part 1 :



"""

from abc import ABC, abstractmethod
from dice_game import DiceGame
import numpy as np


class DiceGameAgent(ABC):
    def __init__(self, game):
        """
               Initializes a DiceGameAgent object.

               Args:
                   game (DiceGame): The dice game object.
        """

        self.game = game

    @abstractmethod
    def play(self, state):
        pass


class AlwaysHoldAgent(DiceGameAgent):
    def play(self, state):
        """
        Plays the game by always holding the dice.

        Args:
            state: The current state of the game.

        Returns:
            The action of holding the dice.
        """


        return (0, 1, 2)


class PerfectionistAgent(DiceGameAgent):
    def play(self, state):

        """
               Plays the game based on a specific strategy.

               Args:
                   state: The current state of the game.

               Returns:
                   The chosen action based on the strategy.
        """

        if state == (1, 1, 1) or state == (1, 1, 6):
            return (0, 1, 2)
        else:
            return ()


def play_game_with_agent(agent, game, verbose=False):
    """
        Plays the dice game with a given agent.

        Args:
            agent (DiceGameAgent): The agent to play the game.
            game (DiceGame): The dice game object.
            verbose (bool): Whether to print verbose output.

        Returns:
            The final score of the game.
    """

    state = game.reset()

    if (verbose): print(f"Testing agent: \n\t{type(agent).__name__}")
    if (verbose): print(f"Starting dice: \n\t{state}\n")

    game_over = False
    actions = 0
    while not game_over:
        action = agent.play(state)
        actions += 1

        if (verbose): print(f"Action {actions}: \t{action}")
        _, state, game_over = game.roll(action)
        if (verbose and not game_over): print(f"Dice: \t\t{state}")

    if (verbose): print(f"\nFinal dice: {state}, score: {game.score}")

    return game.score


def main():
    # random seed makes the results deterministic
    # change the number to see different results
    #  or delete the line to make it change each time it is run
    np.random.seed(1)

    game = DiceGame()

    agent1 = AlwaysHoldAgent(game)
    play_game_with_agent(agent1, game, verbose=True)

    print("\n")

    agent2 = PerfectionistAgent(game)
    play_game_with_agent(agent2, game, verbose=True)


if __name__ == "__main__":
    main()

"""
Part 2:


"""

import math
# Myagent Class will inherit from the class DiceGameAgent
class MyAgent(DiceGameAgent):

    def __init__(self, game, discount_rate=0.9, threshold=0.1):
        """
                Initializes a MyAgent object.

                Args:
                    game (DiceGame): The dice game object.
                    discount_rate (float): The discount rate for the value iteration algorithm.
                    threshold (float): The convergence threshold for the value iteration algorithm.
        """

        self._discount_rate = discount_rate  # discount_rate is initiated and will be used to find value state function.
        self._threshold = threshold  # threshold is initiated and will be used to find the best policy.

        self._states_values = {}  # states values is disctionary that represents all states values functions
        self._best_ploicy = {}  # best policy is disctionary that represents best policy per state.

        # Call the superclass constructor (set self.game = game)
        super().__init__(game)

        self.__initialize_states_values()

        self.__value_iteration()

    def __initialize_states_values(self):
        """
        Initializes the value state function for each state to zero.
        """
        for state in self.game.states:
            self._states_values[state] = 0

    def __value_iteration(self):

        """
        Performs the value iteration algorithm to find the best policy.
        """
        delta = math.inf
        while delta > self._threshold:
            delta = 0

            # get the best policy per state by calculating value state function.
            for state in self._states_values.keys():
                old_v = self._states_values[state]
                best_v = 0

                for action in self.game.actions:
                    states, game_over, reward, probabilities = self.game.get_next_states(action, state)
                    # calculate the value state fuction
                    new_v = 0
                    for new_s, new_p in zip(states, probabilities):
                        if game_over:
                            new_v += new_p * (reward + self._discount_rate * self.game.final_score(state))
                        else:
                            new_v += new_p * (reward + self._discount_rate * self._states_values[new_s])

                    if new_v > best_v:  # assign new_value to best_value if it is higher than the current value.
                        best_v = new_v
                        self._best_policy[state] = action

                self._states_values[state] = best_v

                delta = max(delta, abs(old_v - best_v))

    def play(self, state):
        """
               Plays the game using the best policy found by value iteration.

               Args:
                   state: The current state of the game.

               Returns:
                   The chosen action based on the best policy.
        """
        return self._best_policy[state]

