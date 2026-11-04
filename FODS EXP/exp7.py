import pandas as pd

df = pd.DataFrame({
    'Customer': [101, 102, 101, 103],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Tablet'],
    'Quantity': [2, 3, 4, 1],
    'Date': pd.to_datetime(['2026-01-05', '2026-01-10',
                            '2026-01-15', '2026-01-20'])
})

print(df.groupby('Customer').size())
print(df.groupby('Product')['Quantity'].mean())
print(df['Date'].min())
print(df['Date'].max())
