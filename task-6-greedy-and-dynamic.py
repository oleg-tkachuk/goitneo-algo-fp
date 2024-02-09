from tabulate import tabulate

items = {
    "Pizza": {"cost": 50, "calories": 300},
    "Hamburger": {"cost": 40, "calories": 250},
    "Hot-dog": {"cost": 30, "calories": 200},
    "Pepsi": {"cost": 10, "calories": 100},
    "Cola": {"cost": 15, "calories": 220},
    "Potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, attrs in sorted_items:
        if total_cost + attrs['cost'] <= budget:
            selected_items.append(item)
            total_cost += attrs['cost']
            total_calories += attrs['calories']

    return selected_items


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)

    for i in range(1, budget + 1):
        for item, attrs in items.items():
            if attrs['cost'] <= i:
                dp[i] = max(dp[i], dp[i - attrs['cost']] + attrs['calories'])

    selected_items = []
    i = budget
    while i > 0:
        for item, attrs in items.items():
            if attrs['cost'] <= i and dp[i] == dp[i - attrs['cost']] + attrs['calories']:
                selected_items.append(item)
                i -= attrs['cost']
                break

    return selected_items


def format_output(selected_items, items):
    table_data = []
    total_calories = 0
    total_cost = 0
    for item in selected_items:
        table_data.append([item, items[item]['cost'], items[item]['calories']])
        total_calories += items[item]['calories']
        total_cost += items[item]['cost']
    table_data.append(["", "", ""])
    table_data.append(["TOTAL:", total_cost, total_calories])
    print(tabulate(table_data, headers=["Item", "Cost", "Calories"]))


def main():
    budget = 100

    print(f"*** GoIT Neo Algo Final Project ***")

    print("\nTask 6 - Food | Greedy Algorithm\n")
    selected_items = greedy_algorithm(items, budget)
    format_output(selected_items, items)

    print("\nTask 6 - Food | Dynamic Programming\n")
    selected_items = dynamic_programming(items, budget)
    format_output(selected_items, items)


if __name__ == "__main__":
    main()
