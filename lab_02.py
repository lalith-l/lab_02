import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

df = pd.read_csv("Automobile.csv")
print("--- Initial Data Information ---")
print(df.info())
print("\nMissing values before any action:")
print(df.isnull().sum())

df = df.drop('horsepower', axis=1)

print("\n--- After Deleting 'horsepower' Column ---")
print(df.info())
print("\nMissing values after deletion:")
print(df.isnull().sum())

numerical_cols = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'model_year']

for col in numerical_cols:
    median_val = df[col].median()
    df[col].fillna(median_val, inplace=True)

print("\n--- After Imputing Missing Values with Median ---")
print(df.info())
print("\nMissing values after imputation:")
print(df.isnull().sum())
print("\nFirst 5 rows of the cleaned data:")
print(df.head())

numerical_features_to_scale = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'model_year']
minmax_scaler = MinMaxScaler()
df_minmax = df.copy()
df_minmax[numerical_features_to_scale] = minmax_scaler.fit_transform(df_minmax[numerical_features_to_scale])

print("\n--- Data after Min-Max Scaling (first 5 rows) ---")
print(df_minmax.head())

standard_scaler = StandardScaler()
df_standard = df.copy()
df_standard[numerical_features_to_scale] = standard_scaler.fit_transform(df_standard[numerical_features_to_scale])

print("\n--- Data after Standardization (first 5 rows) ---")
print(df_standard.head())
print("\n Analysis: Min-Max vs. Standardization ")
print("For this dataset, Standardization makes more sense than Min-Max scaling.")
print("The 'weight' and 'displacement' features likely have a wide range of values and might contain outliers, as is common with real-world car data.")
print("Standardization is less sensitive to these outliers because it scales the data based on the mean and standard deviation, rather than the minimum and maximum values.")
print("This prevents a few extreme values from compressing the entire dataset into a small range.")
print("By centering the data around zero, standardization helps algorithms that assume a normal distribution perform more effectively, leading to a more robust model.")