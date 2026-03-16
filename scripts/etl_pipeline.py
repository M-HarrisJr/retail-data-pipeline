import pandas as pd

# Extract
print("Loading raw dataset...")
df = pd.read_csv('../data/raw_sales_data.csv')

# Transform
print("Cleaning data...")
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])

print("Generating regional sales summary...")
sales_by_region = df.groupby('region').agg(
    total_sales=('sales', 'sum'),
    total_quantity=('quantity', 'sum')
).reset_index()

print("Generating product performance summary...")
product_performance = df.groupby('product').agg(
    total_sales=('sales', 'sum'),
    units_sold=('quantity', 'sum')
).reset_index()

# Load
sales_by_region.to_csv('../outputs/sales_by_region.csv', index=False)
product_performance.to_csv('../outputs/product_performance.csv', index=False)

print("ETL pipeline completed successfully.")
