import pandas as pd

df = pd.read_excel("students.csv.xlsx")

print("First 5 Records")
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicates")
print(df.duplicated().sum())

print("\nStatistics")
print(df.describe())