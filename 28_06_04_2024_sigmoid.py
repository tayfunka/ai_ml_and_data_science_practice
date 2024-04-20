# =============================================================================
# İkili sınıflandırma problemlerinde çıktı katmanında en fazla kullanılan
# aktivasyon fonksiyonu "sigmoid" denilen fonksiyondur.
# "diabetes" örneğindeki çıktı katmanında sigmoid fonksiyonunu kullanmıştı.
# İkili sınıflandırma problemlerindeki çıktı katmanında tek bir nöron bulunur.
# Bu nörounun da aktivasyon fonksiyonu "sigmoid" olur.
# Sigmoid fonksiyona "lojistik (logistic)" fonksiyonu da denilmektedir.
# Fonksiyonun matematiksel ifadesi şöyledir:
#   y = 1 / (1 + e ** -x)
# Burada e değeri 2.71828... biçiminde irrasyonel bir değerdir.
# Yukarıdaki kesrin pay ve paydası e ** x ile çarpılırsa fonksiyon şu şekilde de
# ifade edilebilir:
# y = e ** x / (1 + e ** x)
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.activations import sigmoid

# =============================================================================
# def sigmoid(x):
#     return np.e ** x / (1 + np.e ** x)
# =============================================================================

x = np.linspace(-10, 10, 1000)
y = sigmoid(x).numpy()

plt.title('Sigmoid (Logistic) Function',
          fontsize=14, pad=20, fontweight='bold')
axis = plt.gca()
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['top'].set_color(None)
axis.spines['right'].set_color(None)

axis.set_ylim(-1, 1)

plt.plot(x, y)
plt.show()

# =============================================================================
# "sigmoid" isminin verilmesinin nedeni S şekline benzemesinden dolayıdır.
# Sigmoid eğrisi x = 0 için 0.5 değerini veren x pozitif yönde arttıkça 1 değerine
# hızla yaklaşan, x negatif yönde arttıkça 0 değerine hızla yaklaşan bir eğridir.
# Sigmoid fonksiyonunun (0, 1) arasında bir değer verdiğine dikkat ediniz.
# x değeri artıkça eğri 1'e yaklaşır ancak hiçbir zaman 1 olmaz.
# x değeri azaldıkça eğri 0'a yaklaşır ancak hiçbir zaman 0 olmaz.
# Sigmoid fonksiyonu makine öğrenmesinde ve istatistikte belli bir gerçek değeri
# 0 ile 1 arasına hapsetmek için sıkça kullanılmaktadır. Sigmoid çıktısı aslında
# bir bakımdan kestirimin 1 olma olasılığını vermektedir. Tabii biz kestirimde
# bulunurken kesin bir yargı belirteceğimiz için eğrinin orta noktası olan 0.5
# değerini referans alırız. Ağın ürettiği değer 0.5'ten büyükse bunu 1 gibi,
# 0.5'ten küçükse 0 gibi değerlendiririz.
# =============================================================================
