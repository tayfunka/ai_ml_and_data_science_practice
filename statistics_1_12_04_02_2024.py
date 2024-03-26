from scipy.stats import mode
import pandas as pd
import numpy as np

# mean() - aritmetik ortalama
iris_df = pd.read_csv('datasets/iris.csv')

# Kategorik sütunların ortalaması alınamayacağı için:
iris_df_numeric_columns = iris_df.iloc[:, 1:5]

# Tüm sütunların ortalaması:
# axis değeri 0 ise sütunların, 1 ise satırların ortalaması alınır.
# axis değeri default değeri = 0
result = iris_df_numeric_columns.mean(axis=0)

# Spesifik bir Series nesnesinin aritmetik ortalaması için:
sepalLengthCm_s = iris_df_numeric_columns['SepalLengthCm']
sepalLengthCm_mean = sepalLengthCm_s.mean()

# DataFrame.median() - ortadaki değer
# Herhangi bir sütunun median değeri:
sepalWidthCm_s = iris_df_numeric_columns['SepalWidthCm']
SepalWidthCm_median = sepalWidthCm_s.median()

# DataFrame nesnesinin median değeri:
# DataFrame' deki tüm sütunların median değeri:
iris_df_median = iris_df_numeric_columns.median()

# mode() - en çok yinelenen değer:
# scipy.stats mode ile:
petalLengthCm_s = iris_df_numeric_columns['PetalLengthCm']
petalLengthCm_s_scipy_mode = mode(petalLengthCm_s,)

# pandas mode ile:
iris_df_mode = iris_df.mode().iloc[0]

# Standart sapma - np.std()
# Değerler ortalamaya yakınsa std düşük, değilse yüksektir:
# mean1'deki değerler mean2' deki deperlerden ortalamaya daha yakın
np_array1 = np.array([2, 5, 7, 5, 5, 4, 5, 5, 6, 6])
mean1 = np.mean(np_array1)  # 5.0
std1 = np.std(np_array1)  # 1.2649110640673518
print(f'mean1: {mean1}, std1: {std1}')

np_array2 = np.array([1, 5, 7, 1, 9, 4, 5, 5, 6, 7])
mean2 = np.mean(np_array2)  # 5.0
std2 = np.std(np_array2)  # 2.4083189157584592
print(f'mean2: {mean2}, std2: {std2}')

# Buradaki tüm değeler ortalamaya yakın olduğu için std 0'dır.
np_array3 = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
mean3 = np.mean(np_array3)  # 5.0
std3 = np.std(np_array3)  # 0.0
print(f'mean3: {mean3}, std3: {std3}')
