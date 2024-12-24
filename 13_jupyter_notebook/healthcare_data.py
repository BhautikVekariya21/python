import pandas as pd

# Sample healthcare dataset
data = {
    'Admission Date': ['2023-01-05', '2023-02-12', '2023-03-20', '2023-04-10', '2023-05-01',
                       '2023-06-07', '2023-07-15', '2023-08-05', '2023-09-12', '2023-10-20'],
    'Patient ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Diagnosis': ['Cardiac Arrest', 'Diabetes', 'Pneumonia', 'Cancer', 'Cardiac Arrest',
                  'Diabetes', 'Cancer', 'Pneumonia', 'Cardiac Arrest', 'Diabetes'],
    'Treatment Cost': [15000, 5000, 12000, 25000, 15000, 5000, 25000, 12000, 15000, 5000],
    'Age': [60, 45, 70, 55, 65, 50, 75, 68, 63, 47]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('healthcare_data.csv', index=False)

print("healthcare_data.csv file has been created!")
