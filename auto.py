import pandas as pd

# Load the CSV file
df = pd.read_csv('departments_split.csv')

# Combine the two columns
df['Department'] = df['Part1'].fillna('') + ' ' + df['Part2'].fillna('')

# Strip any extra whitespace
df['Department'] = df['Department'].str.strip()

# Drop the original columns
df.drop(['Part1', 'Part2'], axis=1, inplace=True)

# Save to a new CSV file
df.to_csv('cleaned_departments.csv', index=False)

print("✅ Cleaned department names saved to 'cleaned_departments.csv'")
