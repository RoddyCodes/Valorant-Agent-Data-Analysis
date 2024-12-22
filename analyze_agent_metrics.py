import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered Ascendant rank dataset
ascendant_data = pd.read_csv('ascendant_data.csv')

# Calculate average performance metrics by agent
metrics = ['kdr', 'avg_dmg_delta', 'acs']
agent_metrics = ascendant_data.groupby('agent')[metrics].mean()

# Display agent performance metrics
print("Agent Performance Metrics:")
print(agent_metrics)

# Visualize K/D Ratio
plt.figure(figsize=(10, 6))
sns.barplot(x=agent_metrics.index, y=agent_metrics['kdr'], palette="coolwarm")
plt.title("K/D Ratio by Agent in Ascendant Rank")
plt.ylabel("K/D Ratio")
plt.xlabel("Agent")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('agent_kdr.png')
plt.show()

# Visualize Average Damage Delta
plt.figure(figsize=(10, 6))
sns.barplot(x=agent_metrics.index, y=agent_metrics['avg_dmg_delta'], palette="Blues")
plt.title("Average Damage Delta by Agent in Ascendant Rank")
plt.ylabel("Average Damage Delta")
plt.xlabel("Agent")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('agent_avg_dmg_delta.png')
plt.show()

# Visualize ACS (Average Combat Score)
plt.figure(figsize=(10, 6))
sns.barplot(x=agent_metrics.index, y=agent_metrics['acs'], palette="Greens")
plt.title("Average Combat Score (ACS) by Agent in Ascendant Rank")
plt.ylabel("ACS")
plt.xlabel("Agent")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('agent_acs.png')
plt.show()
