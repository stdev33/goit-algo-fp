import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_rolls):
    # Initialize a dictionary to store the count of each possible sum
    sums_count = {i: 0 for i in range(2, 13)}

    # Simulate rolling two dice
    for _ in range(num_rolls):
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        roll_sum = roll_1 + roll_2
        sums_count[roll_sum] += 1

    # Calculate the probabilities based on the number of rolls
    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}

    return probabilities


def plot_probabilities(probabilities, analytical_probabilities):
    sums = list(probabilities.keys())
    monte_carlo_probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_carlo_probs, color='skyblue', label='Monte Carlo Simulation')

    analytical_probs = [analytical_probabilities[sum_] for sum_ in sums]
    plt.plot(sums, analytical_probs, color='red', marker='o', linestyle='--', label='Analytical Calculation')

    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Monte Carlo Simulation vs Analytical Probabilities')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # Number of simulations
    num_rolls = 100000

    monte_carlo_probabilities = monte_carlo_simulation(num_rolls)

    # Analytical probabilities
    analytical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }

    print("Monte Carlo Probabilities:")
    for sum_, prob in monte_carlo_probabilities.items():
        print(f"Sum {sum_}: {prob:.2%}")

    plot_probabilities(monte_carlo_probabilities, analytical_probabilities)


if __name__ == "__main__":
    main()
