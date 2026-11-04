import pandas as pd

df = pd.DataFrame({
    'Product': ['Pen', 'Book', 'Pen', 'Bag', 'Book', 'Pencil'],
    'Quantity': [10, 20, 15, 5, 10, 25]
})

print(df.groupby('Product')['Quantity'].sum().nlargest(5))
