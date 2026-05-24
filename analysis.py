import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix.csv")

# Display First 5 Rows
print(df.head())

# Dataset Information
print(df.info())

# Check Missing Values
print(df.isnull().sum())

# Fill Missing Values
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Not Available')

# Remove Remaining Null Values
df = df.dropna()

# Remove Duplicate Rows
df = df.drop_duplicates()

# Convert Date Column
df['date_added'] = pd.to_datetime(df['date_added'])

# -------------------------------
# Visualization 1
# Movies vs TV Shows
# -------------------------------

plt.figure(figsize=(6,5))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows")

plt.show()

# -------------------------------
# Visualization 2
# Top 10 Countries
# -------------------------------

top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))

top_countries.plot(kind='bar')

plt.title("Top 10 Countries")

plt.xlabel("Country")
plt.ylabel("Count")

plt.show()

# -------------------------------
# Visualization 3
# Release Year Trend
# -------------------------------

release_year = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12,6))

release_year.plot()

plt.title("Netflix Releases Per Year")

plt.xlabel("Year")
plt.ylabel("Count")

plt.show()

# Save Cleaned Dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("Project Completed Successfully")