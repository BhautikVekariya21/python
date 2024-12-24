import pandas as pd

# Sample AI tools usage dataset
data = {
    'Usage Date': ['2023-01-05', '2023-02-12', '2023-03-20', '2023-04-10', '2023-05-01',
                   '2023-06-07', '2023-07-15', '2023-08-05', '2023-09-12', '2023-10-20'],
    'User ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'AI Tool': ['GPT-4', 'DALL-E', 'GPT-4', 'BERT', 'GPT-4', 'DALL-E', 'BERT', 'GPT-4', 'DALL-E', 'GPT-4'],
    'Usage Frequency': [15, 8, 20, 12, 15, 8, 10, 25, 18, 30],
    'Industry': ['Healthcare', 'Finance', 'Healthcare', 'Education', 'Finance', 'Education', 'Healthcare', 'Finance', 'Education', 'Healthcare'],
    'Age': [45, 60, 30, 50, 40, 55, 60, 47, 38, 62]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('ai_tools_usage_data.csv', index=False)

print("ai_tools_usage_data.csv file has been created!")
