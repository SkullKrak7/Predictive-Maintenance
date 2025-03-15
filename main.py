import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.preprocessing import LabelEncoder

#load data
df = pd.read_csv("predictive_maintenance.csv")
print("Initial Data Shape:", df.shape)
print(df.head())

#drop unnecessary columns
df.drop(columns=['UDI', 'Product ID'], inplace=True)
print("Data Shape after dropping useless columns:", df.shape)

#handle missing values
print("Missing Values Before Drop:")
print(df.isna().sum())
df.dropna(inplace=True)
print("Missing Values After Drop:")
print(df.isna().sum())

#make a histogram for frequency distribution
df.hist(figsize=(12, 6))
plt.show()

#perform one-hot encoding on type column
df = pd.get_dummies(df, columns=['Type'], drop_first=True)

#perform label encoding on failure type column
label_encoder = LabelEncoder()
df['Failure Type'] = label_encoder.fit_transform(df['Failure Type'])

