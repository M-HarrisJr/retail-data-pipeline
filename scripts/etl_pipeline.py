import pandas as pd

df = pd.read_csv('../data/raw_sales_data.csv')

df = df.dropna()
df['date'] = pd.to_datetime(df['date'])

sales_summary = df.groupby('region').agg({
    'sales': 'sum',
    'quantity': 'sum'
}).reset_index()

sales_summary.to_csv('../outputs/sales_summary.csv', index=False)

print("ETL pipeline ran full cycle.")
