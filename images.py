import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = 'data_arjun.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()

# Clean column names for better readability
data.columns = data.columns.str.strip().str.replace('\n', '').str.replace(' ', '_').str.replace('.', '').str.lower()

# Drop columns that are completely empty
cleaned_data = data.dropna(axis=1, how='all')

# Show the cleaned column names and the first few rows to ensure everything looks correct
cleaned_data.head(), cleaned_data.columns

# Convert 'dob' to datetime and calculate age if not present
cleaned_data['dob'] = pd.to_datetime(cleaned_data['dob'], errors='coerce')
cleaned_data['age_at_procedure'] = cleaned_data['age_at_procedure'].fillna((pd.Timestamp.now() - cleaned_data['dob']).dt.days // 365)

# Plot 1: Distribution of patients' ages
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_data['age_at_procedure'].dropna(), bins=20, kde=True, color='skyblue')
plt.title("Distribution of Patients' Ages")
plt.xlabel("Age at Procedure")
plt.ylabel("Frequency")
plt.show()

# Plot 2: Ethnicity breakdown
plt.figure(figsize=(10, 6))
ethnicity_counts = cleaned_data['ethnicity'].value_counts()
sns.barplot(x=ethnicity_counts.index, y=ethnicity_counts.values, palette='viridis')
plt.title("Ethnicity Breakdown")
plt.xlabel("Ethnicity")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.show()

# Plot 3: Correlation between different medical factors
# Selecting numerical columns for correlation
numerical_cols = cleaned_data.select_dtypes(include=['float64', 'int64']).drop(columns=['code']).corr()

plt.figure(figsize=(12, 8))
sns.heatmap(numerical_cols, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Between Different Medical Factors")
plt.show()