import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered Ascendant rank dataset
ascendant_data = pd.read_csv('ascendant_data.csv')

# Calculate win rates by agent
ascendant_agent_win_rates = (
    ascendant_data.groupby('agent')['outcome']
    .apply(lambda x: (x == 'Win').mean())
    .sort_values(ascending=False)
)

# Display win rates
print("Win Rates by Agent:")
print(ascendant_agent_win_rates)

# Visualize win rates
plt.figure(figsize=(10, 6))
sns.barplot(x=ascendant_agent_win_rates.index, y=ascendant_agent_win_rates.values, palette="viridis")
plt.title("Win Rates of Agents in Ascendant Rank")
plt.ylabel("Win Rate")
plt.xlabel("Agent")
plt.ylim(0, 1)  # Set y-axis range
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('agent_win_rates.png')
plt.show()
