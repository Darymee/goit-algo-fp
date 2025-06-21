items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(name)
            total_cost += data['cost']
            total_calories += data['calories']

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[names[i - 1]]
        for w in range(budget + 1):
            if item['cost'] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - item['cost']] + item['calories'])

    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= items[names[i - 1]]['cost']

    selected_items.reverse()
    total_cost = sum(items[item]['cost'] for item in selected_items)
    total_calories = sum(items[item]['calories'] for item in selected_items)

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

budget = 100
print("Greedy Algorithm Result:")
print(greedy_algorithm(items, budget))

print("\nDynamic Programming Result:")
print(dynamic_programming(items, budget))
