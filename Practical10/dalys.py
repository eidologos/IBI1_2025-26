import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the DALYs dataset
dalys_data = pd.read_csv("/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical10/dalys-rate-from-all-causes.csv")

# Show first 5 rows
print("\n=== First 5 rows ===")
print(dalys_data.head(5))

# Show data structure
print("\n=== Data info ===")
dalys_data.info()

# Show summary statistics
print("\n=== Summary statistics ===")
print(dalys_data.describe())

# Show Year and DALYs (columns 3 and 4) for first 10 rows
first10_year_dalys = dalys_data.iloc[0:10, [2, 3]]
print("\n=== First 10 rows: Year & DALYs ===")
print(first10_year_dalys)

# Find year with maximum DALYs in Afghanistan's first 10 entries
afg_10 = dalys_data.iloc[0:10]
max_afg_year = afg_10.loc[afg_10['DALYs'].idxmax(), 'Year']
print("\nYear with maximum DALYs in Afghanistan's first 10 records:", max_afg_year)

# Boolean indexing for columns
cols_bool = [True, True, False, True]
bool_selection = dalys_data.iloc[0:3, cols_bool]
print("\n=== Boolean column selection ===")
print(bool_selection)

# Extract all data for Zimbabwe
zimbabwe = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe']
print("\n=== Zimbabwe data ===")
print(zimbabwe[['Year', 'DALYs']])

# First and last year for Zimbabwe
zim_first = zimbabwe['Year'].min()
zim_last = zimbabwe['Year'].max()
print("First and last year for Zimbabwe:", zim_first, "-", zim_last)

# ----------------------
# 5 Comparing across countries
# ----------------------
# Extract 2019 data
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

# Find countries with maximum and minimum DALYs in 2019
max_country = data_2019.loc[data_2019['DALYs'].idxmax(), 'Entity']
min_country = data_2019.loc[data_2019['DALYs'].idxmin(), 'Entity']
print("\nCountry with maximum DALYs in 2019:", max_country)
print("Country with minimum DALYs in 2019:", min_country)

# Plot DALYs over time for the lowest country
country_data = dalys_data[dalys_data['Entity'] == min_country]
plt.figure(figsize=(10, 5))
plt.plot(country_data['Year'], country_data['DALYs'], 'bo-', markersize=4)
plt.title(f'DALYs over time in {min_country} (2019 minimum)')
plt.xlabel('Year')
plt.ylabel('DALYs rate')
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ----------------------
# 6 Additional analysis question
# ----------------------
# Boxplot of global DALYs in 2019
plt.figure(figsize=(8, 4))
plt.boxplot(data_2019['DALYs'], vert=False, widths=0.6)
plt.title('2019 Global DALYs Distribution')
plt.xlabel('DALYs rate')
plt.tight_layout()
plt.show()

# Calculate range of DALYs in 2019
dalys_range = data_2019['DALYs'].max() - data_2019['DALYs'].min()
print("\nRange of DALYs across all countries in 2019:", round(dalys_range, 2))