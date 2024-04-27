# =============================================================================
# çok kullanılan aktivasyon fonksiyonlarından biri de "linear" aktivasyon
# fonksiyonudur. Bu fonksiyon y = x ya da f(x) = x fonksiyonudur. Yani "linear"
# fonksiyonu girdi ile aynı değeri üretir. Bu aktivasyon fonksiyonu "regresyon
# problemlerinde (lojistik olmayan regresyon problemlerinde)" çıktı katmanında
# kullanılmaktadır. Lojistik olmayan regresyon problemleri çıktı olarak bir sınıf
# bilgisi değil gerçek bir değer bulmaya çalışan problemlerdir. Örneğin bir evin
# fiyatının kestirilmesi.
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.activations import linear
x_1 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
result = linear(x_1)
print(result)  # [1. 2. 3. 4. 5.]


def linear_1(x):
    return x


x = np.linspace(-10, 10, 100)
y = linear(x)

plt.title('Linear Function', fontsize=14, fontweight='bold', pad=20)
axis = plt.gca()
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['top'].set_color(None)
axis.spines['right'].set_color(None)
axis.set_ylim(-10, 10)
plt.plot(x, y)
