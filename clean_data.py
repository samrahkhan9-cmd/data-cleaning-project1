import pandas as pd

# 1. Load your Excel file into Python
df = pd.read_excel('Dataset for Data Analytics.xlsx')

print("--- ORIGINAL DATA INFO ---")
print(df.info())  # Shows column types and missing values

# 2. Identify missing values
print("\n--- MISSING VALUES PER COLUMN ---")
print(df.isnull().sum())

# Clean missing values (Option A: Drop rows with blanks)
# df = df.dropna() 
# Clean missing values (Option B: Fill blanks with a default value like 0 or 'Unknown')
df = df.fillna('Unknown') 

# 3. Remove duplicates
duplicate_count = df.duplicated().sum()
print(f"\nFound {duplicate_count} duplicate rows. Removing them...")
df = df.drop_duplicates()

# 4. Correct data formats
# Fix a Date column (replace 'Date_Column' with your actual column name)
# df['Date_Column'] = pd.to_datetime(df['Date_Column'])

# Fix a Number column to integer (replace 'Age_Column' with your actual column name)
# df['Age_Column'] = df['Age_Column'].astype(int)

# 5. Save your perfectly clean data to a brand new Excel file
df.to_excel('cleaned_output.xlsx', index=False)
print("\nSuccess! Your cleaned file is saved as 'cleaned_output.xlsx'")
