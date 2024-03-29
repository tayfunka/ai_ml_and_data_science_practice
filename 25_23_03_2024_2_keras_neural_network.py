import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense
TRAINING_RATIO = 0.8

df = pd.read_csv('datasets/diabetes.csv')

si = SimpleImputer(strategy='mean', missing_values=0)

df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = si.fit_transform(
    df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])

dataset = df.to_numpy()

np.random.shuffle(dataset)

dataset_x = dataset[:, :-1]
dataset_y = dataset[:, -1]


training_dataset_x, test_dataset_x, training_dataset_y, test_dataset_y = train_test_split(
    dataset_x, dataset_y, test_size=0.2, shuffle=True)

# =============================================================================
# Bir model nesnesi oluşturulmalıdır. Ağa her eklenen katman sona eklenir.
# Ağ, katmanların sırasıyla eklenmesiyle oluşturulur.
# name parametresiyle modele bir isim de verilebilir.
# =============================================================================

model = Sequential(name='Diabetes')

# =============================================================================
# Girdi katmanındaki nöron sayısı dataset içindeki sütun sayısı kadardır.
# Input sınıfının __init__ methodunun birinci parametresi tuple olmalıdır.
# =============================================================================

model.add(Input((training_dataset_x.shape[1],), name='Input'))

# =============================================================================
# Katman nesnelerinin model nesnesine eklenmesi gerekir.
# Dense katman modele eklendiğinde önceki katmandaki tüm nöronların çıktıları
# eklenen katmandaki nöronlara girdi yapılır.
# Önceki katmandaki nöron sayısı = k
# Modele eklenecek Dense katmanı nöron sayısı = n
# k * n + n tane yeni parametre (tahmin edilecek parametre) eklemiş olur.
# k * n tane ayarlanması gereken w değerleri ve n tane ayarlanması gereken bias
# değerleri söz konusudur.
# Bir nörondaki w değerlerinin o nörona giren nöron sayısı kadardır.
# Bias değerleri her nöron için bir tanedir.
# =============================================================================

model.add(Dense(16, activation='relu', name='Hidden-1'))

# =============================================================================
# Katman nesnesinin model nesnesine eklenmesi için Sequential sınıfının add
# metodu kullanılır.
# =============================================================================

model.add(Dense(16, activation='relu', name='Hidden-2'))

# =============================================================================
# Hidden katmanları eklendikten sonra çıkış katmanı add kullanarak eklenir.
# İkili sınıflandırma (0 ya da 1) problemlerinde ağın çıktı katmanının
# aktivasyon fonksiyonu sigmoid fonksiyonuna ilişkin olması gerekir.
# Çıktıda tek bir nöron bulunur. Çıktı 0 ile 1 değeri arasındadır.
# Çıktı 1' e yakınsa çıktı = 1, 0' a yakınsa çıktı = 0 olduğu kabul edilir.
# =============================================================================

model.add(Dense(1, activation='sigmoid', name='Output'))

# =============================================================================
# Ağın özet bilgisi Sequential sınıfının summary metodu ile elde edilir.
# Bu bilgiler eğitilebilir parametre sayısını da içerir.
# =============================================================================

model.summary()

# =============================================================================
# Hidden-1 (Dense) Shape = (None, 16), Trainable Params = 144
# Hidden-2 (Dense) Shape = (None, 16), Trainable Params = 272
# Output (Dense) Shape = (None, 1), Trainable Paramas = 17
# Hidden-1 Katmanındaki parametre sayısı = 144.
# 144 değeri şu şekilde elde edilmiştir
# Ağın girdi sayısı (Datasetteki sütun sayısı = 8) *
# Hidden-1 katmanındaki nöron sayısı = 16 +
# Eklenen katmandaki nöronların bias değeri = 16
# = 8 * 16 + 16
# Hidden 2 Katmanındaki parametre sayısı = 244.
# 144 değeri şu şekilde elde edilmiştir:
# Hidden1 katmanındaki nöron sayısı = 16 *
# Hidden2 katmanındaki nöron sayısı = 16 +
# Eklenen katmandaki nöronların bias değeri
# = 16 * 16 + 16 = 272
# Çıktı katmanındaki parametre sayısı = 17.
# 17 değeri şu şekilde elde edilmiştir:
# Hidden 2 katmanındaki nöron sayısı = 16 *
# Eklenen çıktı katmanındaki nöron sayısı = 1
# + çıktı katmanındaki bias değeri = 1
# = 16 * 1 + 1 = 17
# =============================================================================

# =============================================================================
# Model oluşturulduktan sonra modelin derlenmesi (compile) gerekir.
# Bu işlem Sequential sınıfının compile metoduyla yapılmaktadır.
# en önemli iki parametre "loss fonksiyonu" ve "optimizasyon algoritması"dır.
# Eğitim sırasında ağın ürettiği değelerin gerçek değerlere yaklaştırılması için
# w ve bias değerlerinin nasıl güncelleneceğine ilişkin algoritmalara
# "optimizasyon algoritmaları" denilmektedir.
# Matematiksel optimizasyon işlemlerinde belli bir fonksiyonun minimize edilmesi
# istenir. minimize edilecek bu fonksiyona "loss fonksiyonu" denilmektedir.
# =============================================================================
