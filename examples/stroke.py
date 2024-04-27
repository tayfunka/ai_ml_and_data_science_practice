from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

from tensorflow.keras.activations import relu, sigmoid

df = pd.read_csv('stroke-data.csv')

# Drop:
df = df.dropna(subset=['bmi'])
df = df[df['smoking_status'] != 'Unknown']
df = df.drop(columns=['work_type'])

# Map
gender_map = {'Male': 0, 'Female': 1}
df['gender'] = df['gender'].map(gender_map)
df = df.dropna(subset='gender')

smoking_status_map = {'smokes': 3, 'formerly smoked': 2, 'never smoked': 1}
df['smoking_status'] = df['smoking_status'].map(smoking_status_map)

ever_married_map = {'Yes': 1, 'No': 0}
df['ever_married'] = df['ever_married'].map(ever_married_map)
1, 0,
residence_type_map = {'Urban': 0, 'Rural': 1}
df['Residence_type'] = df['Residence_type'].map(residence_type_map)

df = df.to_numpy()
np.random.shuffle(df)

# for i in df.columns:
#     print(df[f'{i}'].unique())

dataset_X = df[:, 1:-1]
dataset_y = df[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    dataset_X, dataset_y, test_size=0.2)

# Model:
model = Sequential(name='Strokes')

model.add(Input((X_train.shape[1], )))
model.add(Dense(24, activation=relu, name='Hidden-1'))
model.add(Dense(24, activation=relu, name='Hidden-2'))
model.add(Dense(1, activation=sigmoid, name='Output'))
model.summary()


model.compile(optimizer='rmsprop', loss='binary_crossentropy',
              metrics=['binary_accuracy'])
hist = model.fit(X_train, y_train, batch_size=32,
                 epochs=300, validation_split=0.2)

plt.figure(figsize=(14, 6))
plt.title('Epoch - Loss Graph', pad=10, fontsize=14)
plt.xticks(range(0, 300, 10))
plt.plot(hist.epoch, hist.history['loss'])
plt.plot(hist.epoch, hist.history['val_loss'])
plt.legend(['Loss', 'Validation Loss'])
plt.show()

plt.figure(figsize=(14, 6))
plt.title('Epoch - Binary Accuracy Graph', pad=10, fontsize=14)
plt.xticks(range(0, 300, 10))
plt.plot(hist.epoch, hist.history['binary_accuracy'])
plt.plot(hist.epoch, hist.history['val_binary_accuracy'])
plt.legend(['Accuracy', 'Binary Accuracy'])
plt.show()

# Test
eval_result = model.evaluate(X_test, y_test, batch_size=32)

for i in range(len(eval_result)):
    print(f'{model.metrics_names[i]}: {eval_result[i]}')


predict_dataset = np.array([[0, 67, 1, 1, 1, 0, 228.69, 36.6, 2
                             ]])
predict_result = model.predict(predict_dataset)
print(predict_result)


# https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset/data
