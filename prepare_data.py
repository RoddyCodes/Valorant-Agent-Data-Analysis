import pandas as pd

# Load the dataset
valorant_data = pd.read_csv('valorant_games.csv')

# Filter for Ascendant ranks
ascendant_data = valorant_data[valorant_data['rank'].isin(['Ascendant 1', 'Ascendant 2'])]

# Save the filtered data for further analysis
ascendant_data.to_csv('ascendant_data.csv', index=False)
print("Filtered data saved as 'ascendant_data.csv'.")
