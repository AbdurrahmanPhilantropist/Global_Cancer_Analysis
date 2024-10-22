# Cancer Deaths Data Analysis

## Project Overview
This project analyzes cancer death data across 195 countries and over 20 different types of cancer, using data from the year 2021. The analysis focuses on understanding global trends in cancer mortality, exploring correlations between population size and cancer deaths, and identifying the top countries and cancer types with the highest death tolls. Insights from this analysis aim to guide healthcare interventions and resource allocation, especially in regions requiring the most attention.

## Dataset Information
- **Number of records**: 10,000+
- **Features**:
  - `Country`: The name of the country.
  - `Cancer_Type`: Type of cancer (e.g., lung cancer, breast cancer, etc.).
  - `Total_Deaths`: Total number of deaths caused by cancer in the country.
  - `Population_Size`: Population of the country.
  - `Year`: The year the data was collected (2021).

## Data Cleaning and Preprocessing
- Resolved 5% missing values by filling them with median values for both `Total_Deaths` and `Population_Size`.
- Ensured correct data types for each feature (e.g., `Total_Deaths` and `Population_Size` as float).
- No significant outliers were found that could impact the analysis.

## Key Analyses
### 1. Top 10 Countries by Cancer Deaths
The analysis identifies the top 10 countries with the highest cancer deaths, showing that Spain, the USA, and Vietnam account for 40% of total global cancer deaths.

### 2. Distribution of Cancer Deaths by Type
We explored which cancer types contributed the most to total deaths globally. We found out that Lung, Pancreatic and Cervical Cancer leads the global death by type.


## Results
1. **Top Countries**: Spain, the USA and Vietnam were the countries with the highest cancer mortality rates.
2. **Top Cancer Types**: The most common cancer types were lung, Pancreatic, and Cervical cancer.


## Files Included
- `cancer_deaths_dataset.csv`: The dataset used for analysis.
- `top_10_countries.csv`: CSV file containing the top 10 countries by cancer deaths.
- `README_Analysis.txt`: Summary of findings from the data analysis.

## How to Run the Analysis
1. Clone this repository to your local machine.
2. Install the required Python libraries using `pip`:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Open the Jupyter Notebook or Python script provided to explore the data and visualizations.

## Future Work
- Further investigation into the impact of healthcare infrastructure and cancer screening programs on mortality rates.
- Predictive modeling to forecast cancer deaths in coming years using machine learning techniques.
- Regional focus analysis (e.g., Sub-Saharan Africa and South Asia) for targeted healthcare interventions.

---

This README provides a clear and concise description of the project, including its objectives, key analyses, and instructions for running the code.
