from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import Sequential
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd

df = pd.read_csv('datasets/diabetes.csv')


si = SimpleImputer(strategy='mean', missing_values=0)

df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = si.fit_transform(
    df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])

dataset = df.to_numpy()

dataset_x = dataset[:, :-1]
dataset_y = dataset[:, -1]


training_dataset_x, test_dataset_x, training_dataset_y, test_dataset_y = train_test_split(
    dataset_x, dataset_y, test_size=0.2)


model = Sequential(name='Diabetes')

model.add(Input((training_dataset_x.shape[1],)))
model.add(Dense(16, activation='relu', name='Hidden-1'))
model.add(Dense(16, activation='relu', name='Hidden-2'))
model.add(Dense(1, activation='sigmoid', name='Output'))
model.summary()

model.compile(optimizer='rmsprop', loss='binary_crossentropy',
              metrics=['binary_accuracy'])
model.fit(training_dataset_x, training_dataset_y,
          batch_size=32, epochs=100, validation_split=0.2)
eval_result = model.evaluate(test_dataset_x, test_dataset_y, batch_size=32)

for i in range(len(eval_result)):
    print(f'{model.metrics_names[i]}: {eval_result[i]}')


hidden1 = model.layers[0]
weights, bias = hidden1.get_weights()


print(type(weights))
# list

print(weights[0].shape)
# (8, 16)

# Ağırlıklar önceki katman ile sonraki katmanın matris çarpımı ile elde
# edilir.
# 8 X 16 = 128 adet ağırlık değeri vardır.
# =============================================================================
print(weights[1])
# (16, )

# Her nöronda 1 adet bias değeri bulunur.
# Nöron sayısı kadar bias değeri vardır. Modeldeki "Hidden-1" katmanında
# 16 adet nöron bulunduğu için 16 adet bias değeri elde edilir.
# =============================================================================

# =============================================================================
# 5. girdi nöronunun ilk katmanının 9. nöronuna bağlantısındaki w değeri:
# =============================================================================
w = weights[5, 9]
print(w)
