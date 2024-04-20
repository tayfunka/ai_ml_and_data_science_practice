# =============================================================================
# Çok kullanılan bir aktivasyon fonksiyonu da "hiperbolik tanjant" fonksiyonudur.
# Bu fonksiyona kısaca "tanh" fonksiyonu denilmektedir. Fonksiyonun matematiksel
# ifadesi şöyledir:
#   f(x) = (e ** (2 * x) - 1) / (e ** (2 * x) + 1)
#
# Fonksiyonun sigmoid fonksiyonuna benzediğine ancak üstel ifadenin x yerine
# 2 * x olduğuna dikkat ediniz.
#
# Tanh fonksiyonu sigmoid fonksiyonunun (-1, +1) arası değer veren biçimi gibidir.
# Fonksiyon yine S şekli biçimindedir. Ancak noktası x = 0'dadır.
#
# Tanh fonksiyonu saklı katmanlarda ya da çıktı katmanlarında da kullanılabilmektedir.
# Eskiden bu fonksiyon saklı katmanlara çok yoğun kullanılıyordu. Ancak artık
# saklı katmanlarda daha çok relu fonksiyonu tercih edilmektedir. Fakat tanh
# fonksiyonunun daha iyi sonuç verdiği modeller de söz konusu olmaktadır.

# tanh fonksiyonu Keras'ta tensorflow.keras.activations modülünde tanh ismiyle
# de bulunmaktadır.
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.activations import tanh
# =============================================================================
# def tanh(x):
#     return (np.e ** (2 * x) - 1) / (np.e ** (2 * x) + 1)
# =============================================================================

x = np.linspace(-10, 10, 1000)
y = tanh(x).numpy()

plt.title('Hiperbolik Tanjant (tanh) Fonksiyonunun Grafiği',
          fontsize=14, pad=20, fontweight='bold')
axis = plt.gca()
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['top'].set_color(None)
axis.spines['right'].set_color(None)

axis.set_ylim(-1, 1)

plt.plot(x, y)
plt.show()
