import pandas as pd

df = pd.DataFrame({
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi'],
    'Bedrooms': [3, 5, 6, 2],
    'Area': [1500, 2500, 3000, 1200],
    'Price': [30, 50, 60, 25]
})

print(df.groupby('Location')['Price'].mean())
print(df[df['Bedrooms'] > 4])
print(df.loc[df['Area'].idxmax()])
