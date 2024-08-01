def greedy_algorithm(items, budget):
    # Sort items based on the ratio of calories to cost in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(item)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Initialize the dynamic programming table
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, data in items.items():
        cost = data['cost']
        calories = data['calories']
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [item]

    return item_selection[budget], dp[budget]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Example budget
    budget = 110

    # Call the greedy algorithm
    greedy_items, greedy_total_cost, greedy_total_calories = greedy_algorithm(items, budget)
    print(f"Greedy algorithm selected items: {greedy_items}")
    print(f"Total cost: {greedy_total_cost}, Total calories: {greedy_total_calories}\n")

    # Call the dynamic programming algorithm
    dp_items, dp_total_calories = dynamic_programming(items, budget)
    dp_total_cost = sum(items[item]['cost'] for item in dp_items)
    print(f"Dynamic programming selected items: {dp_items}")
    print(f"Total cost: {dp_total_cost}, Total calories: {dp_total_calories}\n")


if __name__ == "__main__":
    main()
