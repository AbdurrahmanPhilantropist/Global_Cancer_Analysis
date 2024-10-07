import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Ensure you have the dataset CSV file in the same directory or provide the correct path
df = pd.read_csv('global_cancer_mortality_2021.csv')

# Display the first few rows of the dataset
print(df.head())

# 1. Data Cleaning
# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Handling missing values (e.g., fill with median or drop rows)
df.fillna(df.median(numeric_only=True), inplace=True)

# Ensure consistent column names (e.g., fixing potential typos)
df.columns = df.columns.str.strip().str.replace('Leukamia', 'Leukemia')

# 2. Exploratory Data Analysis (EDA)
# Top 10 countries by cancer mortality
top_10_countries = df.groupby('Country')['Total Deaths'].sum().nlargest(10)
print("Top 10 countries with highest cancer mortality:\n", top_10_countries)

# Correlation between population and cancer deaths
correlation = df['Population'].corr(df['Total Deaths'])
print(f"Correlation between population and cancer deaths: {correlation}")

# Visualize the top 10 countries with highest cancer deaths
plt.figure(figsize=(10, 6))
top_10_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries by Cancer Mortality (2021)')
plt.ylabel('Total Deaths')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_10_countries_by_cancer_mortality.png')  # Save the figure
plt.show()

# 3. Visualization of cancer types across countries
plt.figure(figsize=(12, 8))
sns.heatmap(df.pivot_table(index='Country', columns='Cancer Type', values='Total Deaths'), cmap='YlGnBu')
plt.title('Cancer Deaths by Type and Country (2021)')
plt.xlabel('Cancer Type')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('cancer_deaths_heatmap.png')  # Save the figure
plt.show()

# 4. Insights based on analysis
high_risk_countries = df[df['Total Deaths'] > 50000]['Country'].unique()
print("High-risk countries (total deaths > 50,000):", high_risk_countries)

# Save the cleaned dataset for further analysis or sharing
df.to_csv('cleaned_cancer_mortality_2021.csv', index=False)
