import pandas as pd

# Create a sample DataFrame
data = {
    'Order Date': ['2023-01-05', '2023-02-12', '2023-02-20', '2023-03-10', '2023-04-15',
                   '2023-05-01', '2023-06-07', '2023-07-19', '2023-08-02', '2023-09-09'],
    'Product Name': ['Laptop Stand', 'Office Chair', 'Noise Cancelling', 'Desk Lamp', 'Smartphone',
                     'Office Desk', 'Wireless Mouse', 'Tablet', 'Ergonomic Chair', 'Laptop'],
    'Category': ['Accessories', 'Furniture', 'Electronics', 'Accessories', 'Electronics',
                 'Furniture', 'Accessories', 'Electronics', 'Furniture', 'Electronics'],
    'Sales': [120.50, 250.00, 99.99, 45.75, 499.99, 350.00, 30.00, 300.00, 275.00, 999.99],
    'Quantity': [2, 1, 1, 3, 1, 2, 5, 2, 1, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ecommerce_sales.csv', index=False)

print("ecommerce_sales.csv file has been created!")
