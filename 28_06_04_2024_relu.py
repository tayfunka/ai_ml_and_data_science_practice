# =============================================================================
# Saklı katmanlardaki aktivasyon fonksiyonları için bazı seçenekler vardır.
# Özellikle son yıllarda saklı katmanlarda en fazla tercih edilen aktivasyon
# fonksiyonu "relu (rectified linear unit)" denilen aktivasyon fonksiyonudur.
# Bu fonksiyona İngilizce "rectifier" da denilmektedir. Relu fonksiyonu:
#     x >= 0  ise y = x
#     x < 0   ise y = 0
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.activations import relu

# =============================================================================
# def relu(x):
#   return np.maximum(x, 0)
#
# =============================================================================

x = np.linspace(-10, 10, 1000)
# y = relu(x)
y = relu(x).numpy()

plt.title('Relu Function', fontsize=14, fontweight='bold', pad=20)
axis = plt.gca()
axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['top'].set_color(None)
axis.spines['right'].set_color(None)
axis.set_ylim(-10, 10)
plt.plot(x, y, color='red')
plt.show()
