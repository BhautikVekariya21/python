import pandas as pd

# Sample chemical production dataset
data = {
    'Production Date': ['2023-01-05', '2023-02-12', '2023-03-20', '2023-04-10', '2023-05-01',
                        '2023-06-07', '2023-07-15', '2023-08-05', '2023-09-12', '2023-10-20'],
    'Customer ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product': ['Sulfuric Acid', 'Ammonia', 'Methanol', 'Acetone', 'Sulfuric Acid',
                'Ammonia', 'Methanol', 'Acetone', 'Sulfuric Acid', 'Ammonia'],
    'Production Volume': [5000, 2000, 3000, 1500, 5000, 2000, 3000, 1500, 5000, 2000],
    'Production Cost': [10000, 8000, 12000, 6000, 10000, 8000, 12000, 6000, 10000, 8000],
    'Age': [45, 60, 30, 50, 40, 55, 60, 47, 38, 62]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('chemical_production_data.csv', index=False)

print("chemical_production_data.csv file has been created!")
