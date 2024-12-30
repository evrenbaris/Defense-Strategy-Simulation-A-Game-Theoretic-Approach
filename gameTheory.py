import random
import matplotlib.pyplot as plt

# Define strategies
class Strategy:
    def decide(self, opponent_previous_move):
        pass

class Attack(Strategy):
    def decide(self, opponent_previous_move):
        return 'Attack'

class Defend(Strategy):
    def decide(self, opponent_previous_move):
        return 'Defend'

class Diplomacy(Strategy):
    def decide(self, opponent_previous_move):
        return 'Diplomacy'

class RandomStrategy(Strategy):
    def decide(self, opponent_previous_move):
        return random.choice(['Attack', 'Defend', 'Diplomacy'])

# Game rules
PAYOFFS = {
    ('Attack', 'Attack'): (0, 0),
    ('Attack', 'Defend'): (1, 0),
    ('Attack', 'Diplomacy'): (3, -1),
    ('Defend', 'Attack'): (0, 1),
    ('Defend', 'Defend'): (0, 0),
    ('Defend', 'Diplomacy'): (1, 1),
    ('Diplomacy', 'Attack'): (-1, 3),
    ('Diplomacy', 'Defend'): (1, 1),
    ('Diplomacy', 'Diplomacy'): (2, 2)
}

class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.score = 0
        self.previous_move = None

    def make_move(self, opponent_previous_move):
        move = self.strategy.decide(opponent_previous_move)
        self.previous_move = move
        return move

# Simulate a match
def simulate_match(player1, player2, rounds=1):
    for _ in range(rounds):
        move1 = player1.make_move(player2.previous_move)
        move2 = player2.make_move(player1.previous_move)
        payoff1, payoff2 = PAYOFFS[(move1, move2)]
        player1.score += payoff1
        player2.score += payoff2

# Defense Strategy Simulation
def defense_strategy_simulation(total_rounds=5):
    print("\nDefense Strategy Simulation")

    user_player = None
    opponent_player = None

    for round_num in range(1, total_rounds + 1):
        print("\nRound", round_num)
        print("Choose your strategy: \n1. Attack \n2. Defend \n3. Diplomacy \n4. RandomStrategy")
        user_choice = int(input("Enter the number of your strategy: "))

        strategies = [Attack, Defend, Diplomacy, RandomStrategy]
        user_strategy = strategies[user_choice - 1]()

        if round_num == 1:
            print("Opponent's strategy is RandomStrategy.")
            opponent_strategy = RandomStrategy()
            user_player = Player(user_strategy)
            opponent_player = Player(opponent_strategy)
        else:
            user_player.strategy = user_strategy

        simulate_match(user_player, opponent_player, rounds=1)
        print(f"After round {round_num}: Your Score: {user_player.score}, Opponent's Score: {opponent_player.score}")
        print(f"Your move this round: {user_player.previous_move}, Opponent's move: {opponent_player.previous_move}")

    print("\nFinal Results:")
    print(f"Your Total Score: {user_player.score}")
    print(f"Opponent's Total Score: {opponent_player.score}")

    if user_player.score > opponent_player.score:
        print("Congratulations! You are the overall winner!")
    elif user_player.score < opponent_player.score:
        print("Opponent is the overall winner. Better luck next time!")
    else:
        print("It's a tie! Well played.")

# Main
if __name__ == "__main__":
    defense_strategy_simulation(total_rounds=5)
