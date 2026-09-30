import pandas as pd

# Load the East African music data
data = pd.read_csv("data/music_data.csv")

print("======================================")
print(" EAST AFRICAN MUSIC DATA ANALYZER")
print("======================================")

# Show the music data
print(data)

# Show the number of artists in the dataset
print("\nNumber of artists:", len(data))sss