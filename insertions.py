import pandas as pd

file_path = "C:/Users/AKARSH RAJ M H/OneDrive/Desktop/resurvey/Bengaluru_House_Data.csv"
df = pd.read_csv(file_path)

df.dropna(inplace=True)
df.drop(columns=['area_type', 'availability', 'society', 'balcony'], inplace=True)
df['size'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else x)
df = df[df['bath'] < 20]
df = df[df['price'] < 20000000]
df = df[df['size'] < 10]
df = df[df['total_sqft'].notnull()]
df['price_lakhs'] = df['price'] / 100000  

def convert_sqft_to_num(x):
    try:
        return float(x)
    except:
        tokens = str(x).split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
df.dropna(subset=['total_sqft'], inplace=True)
df = df[df['total_sqft'] / df['size'] > 300]
df['price_per_sqft'] = df['price_lakhs'] * 100000 / df['total_sqft']
df['price_per_sqft'] = df['price_per_sqft'].apply(lambda x: round(x, 2))
df['location'] = df['location'].str.strip()
location_stats = df['location'].value_counts()
locations_less_than_10 = location_stats[location_stats < 10]
df['location'] = df['location'].apply(lambda x: 'other' if x in locations_less_than_10 else x)
df.reset_index(drop=True, inplace=True)

for _, row in df.head(int(len(df)/2)).iterrows():  
    stmt = f"""INSERT INTO properties (location, size, total_sqft, bath, price_lakhs, price_per_sqft) VALUES (
    '{row['location'].replace("'", "''")}',
    {int(row['size'])},
    {row['total_sqft']:.2f},
    {int(row['bath'])},
    {row['price_lakhs']:.2f},
    {row['price_per_sqft']:.2f}
);"""
    print(stmt)
