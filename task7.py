import random
import matplotlib.pyplot as plt

n_simulations = 100000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(n_simulations):
    dice_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[dice_sum] += 1

sum_probabilities = {s: count / n_simulations for s, count in sum_counts.items()}

theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

sums = list(sum_probabilities.keys())
experimental = [sum_probabilities[s] for s in sums]
theoretical = [theoretical_probabilities[s] for s in sums]

plt.figure(figsize=(10, 5))
plt.bar(sums, experimental, width=0.4, label='Монте-Карло', align='edge')
plt.bar(sums, theoretical, width=-0.4, label='Теоретична', align='edge')
plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()
