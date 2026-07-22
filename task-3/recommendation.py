import pandas as pd

# Load dataset
import os
import pandas as pd

current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "movies.csv")

movies = pd.read_csv(csv_path)

print("=" * 50)
print(" AI Movie Recommendation System ")
print("=" * 50)

print("\nAvailable Genres:")
genres = sorted(movies["Genre"].unique())

for i, genre in enumerate(genres, start=1):
    print(f"{i}. {genre}")

choice = input("\nEnter your favorite genre: ").strip()

recommendations = movies[
    movies["Genre"].str.lower() == choice.lower()
]

print("\nRecommended Movies:\n")

if len(recommendations) == 0:
    print("Sorry! No recommendations found.")
else:
    for movie in recommendations["Title"]:
        print("⭐", movie)