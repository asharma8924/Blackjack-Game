How to Use

1.Run the Script: Execute the script in a Python environment. Make sure you have Python installed on your system.
python blackjack_simulation.py

2.Simulations: The script will run a specified number of simulations (defined in the script) and display the results, showing the number of wins for the player and the dealer.

Code Structure

initialize_deck(): Initializes and shuffles a standard deck of 52 playing cards.
calculate_total(hand): Calculates the total value of a hand according to Blackjack rules.
play_round(): Simulates a single round of Blackjack, allowing the player to hit or stay.
run_simulations(num_simulations): Runs multiple simulations and compares results.
Example
# Example: Run 100 simulations
run_simulations(100)
This will output the number of player wins and dealer wins after 100 simulations.

