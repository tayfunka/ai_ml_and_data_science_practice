import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import numpy as np

TRAINING_RATIO = 0.8

df = pd.read_csv('datasets/diabetes.csv')

si = SimpleImputer(strategy='mean', missing_values=0)

df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = si.fit_transform(
    df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])

dataset = df.to_numpy()

np.random.shuffle(dataset)

dataset_x = dataset[:, :-1]
dataset_y = dataset[:, -1]

# training_len = round(len(dataset) * 0.8)

# training_dataset_x = dataset_x[:training_len]
# training_dataset_y = dataset_y[:training_len]

# test_dataset_x = dataset_x[training_len:]
# test_dataset_y = dataset_y[training_len:]

training_dataset_x, test_dataset_x, training_dataset_y, test_dataset_y = train_test_split(
    dataset_x, dataset_y, test_size=0.2, shuffle=True)
