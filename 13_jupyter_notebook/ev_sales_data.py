import pandas as pd

# Sample EV sales dataset
data = {
    'Sale Date': ['2023-01-05', '2023-02-12', '2023-03-20', '2023-04-10', '2023-05-01',
                  '2023-06-07', '2023-07-15', '2023-08-05', '2023-09-12', '2023-10-20'],
    'Customer ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'EV Model': ['Tesla Model 3', 'Nissan Leaf', 'BMW i3', 'Tesla Model X', 'Tesla Model 3',
                 'Nissan Leaf', 'BMW i3', 'Tesla Model X', 'Tesla Model 3', 'Nissan Leaf'],
    'Sales Price': [35000, 25000, 45000, 75000, 35000, 25000, 45000, 75000, 35000, 25000],
    'Age': [30, 45, 60, 35, 32, 50, 55, 40, 33, 47]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ev_sales_data.csv', index=False)

print("ev_sales_data.csv file has been created!")
