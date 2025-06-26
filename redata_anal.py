import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings("ignore")

pd.set_option('display.max_columns', None)
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

DATA_PATH = 'C:/Users/AKARSH RAJ M H/OneDrive/Desktop/resurv/resurvey/Bengaluru_House_Data.csv'
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Data file not found at {DATA_PATH}. Please check the path.")
df = pd.read_csv(DATA_PATH)

print("\n--- Dataset Info ---")
print(df.info())
print("\n--- First 5 rows ---")
print(df.head())
print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Cleaning Data ---")
df.dropna(inplace=True)
df.drop(columns=['area_type', 'availability', 'society', 'balcony'], inplace=True)
df['size'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else x)
df = df[df['bath'] < 20]
df = df[df['price'] < 20000000]
df = df[df['size'] < 10]
df = df[df['total_sqft'].notnull()]
df['price'] = df['price'] / 100000

def convert_sqft_to_num(x):
    try:
        return float(x)
    except:
        tokens = x.split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
df.dropna(subset=['total_sqft'], inplace=True)
df = df[df['total_sqft'] / df['size'] > 300]
df['price_per_sqft'] = df['price'] * 100000 / df['total_sqft']
df['price_per_sqft'] = df['price_per_sqft'].apply(lambda x: round(x, 2))

df['location'] = df['location'].apply(lambda x: x.strip())
df['location'] = df['location'].str.replace('^\\s+|\\s+$', '', regex=True)

print("\n--- Unique Locations ---")
print(len(df['location'].unique()))
print("\n--- Top 10 Locations ---")
print(df['location'].value_counts().head(10))

location_stats = df['location'].value_counts()
locations_less_than_10 = location_stats[location_stats < 10]
df['location'] = df['location'].apply(lambda x: 'other' if x in locations_less_than_10 else x)
df['location'] = df['location'].apply(lambda x: x.strip())
df['location'] = df['location'].str.replace('^\\s+|\\s+$', '', regex=True)

def plot_bhk_distribution():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='size', data=df, order=sorted(df['size'].value_counts().index))
    plt.title("Distribution of BHK")
    plt.xlabel("BHK")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_price_distribution():
    plt.figure(figsize=(8, 6))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title("Price Distribution (Lakh INR)")
    plt.xlabel("Price (Lakh)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def plot_location_distribution():
    top_locations = df['location'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_locations.index, y=top_locations.values)
    plt.title("Top 10 Locations by Count")
    plt.xticks(rotation=45)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

print("\n--- Data Cleaning Completed ---")
print("\n--- Data Visualization ---")
plot_bhk_distribution()
plot_price_distribution()
plot_location_distribution()
