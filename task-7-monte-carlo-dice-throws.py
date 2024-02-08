import random
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import Counter


def monte_carlo_dice_throws(throws):
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(throws)]
    sums_count = Counter(sums)
    probabilities = {sum_val: count /
                     throws for sum_val, count in sums_count.items()}

    return dict(sorted(probabilities.items()))


def print_probabilities(probabilities):
    table = []
    for sum_val, prob in probabilities.items():
        table.append([sum_val, prob])
    print(tabulate(table, headers=["Sum", "Probability"], tablefmt="grid",))


def draw_probabilities(probabilities):
    plt.figure(figsize=(10, 6))
    plt.bar(probabilities.keys(), probabilities.values(), color='skyblue')
    plt.xlabel('Sum of numbers on cubes')
    plt.ylabel('Probability')
    plt.title('Probability of sums when rolling two dice (Monte Carlo method)')
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--')
    plt.show()


def main():
    throws = 1000000

    print(f"*** GoIT Neo Algo Final Project ***")
    print("\nTask 7 - Monte Carlo method for dice throws\n")
    probabilities = monte_carlo_dice_throws(throws)
    print_probabilities(probabilities)
    draw_probabilities(probabilities)


if __name__ == "__main__":
    main()
