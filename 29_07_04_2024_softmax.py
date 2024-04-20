# =============================================================================
# Çok karşılaşılan bir aktivasyon fonksiyonu da "softmax" isimli fonksiyondur.
# Softmax fonksiyonu çok sınıflı sınıflandırma problemlerinde çıktı katmanlarında
# kullanılmaktadır.
#
# Örneğin bir resmin "elma", "armut", "kayısı" resimlerinden hangisi olduğunu
# anlamak için kullanılan sınıflandırma modeli çok sınıflı bir sınıflandırma modelidir.
# Buna istatistikte "çok sınıflı lojistik regresyon (multinomial logistic regression)"
# da denilmektedir.
#
# Bu tür problemlerde sinir ağında sınıf sayısı kadar nöron bulundurulur.
#
# Örneğin yukarıdaki "elma", "armut", "kayısı" resim sınıflandırma probleminde
# ağın çıktısında 3 nöron bulunacaktır.
# =============================================================================

# =============================================================================
# Çıktı katmanındaki tüm nöronların aktivasyon fonksiyonları "softmax" yapılırsa
# tüm çıktı katmanındaki nöronların çıktı değerlerinin toplamı her zaman 1 olur.
# Böylece çıktı katmanındaki nöronların çıktı değerleri ilgili sınıfın olasılığını
# belirtir hale gelir. Toplamı 1 olan çıktıların en yüksek değerine bakılır ve
# sınıflandırmanın o sınıfı kestirdiğini kabul ederiz.
#
# Örneğin yukarıdaki "elma", "armut", "kayısı" sınıflandırma probleminde ağın
# çıktı katmanındaki nöronların çıktı değerlerinin şöyle olduğunu varsayılırsa:
#
#   Elma Nöronunun Çıktısı ---> 0.2
#   Armut Nöronunun Çıktısı ---> 0.2
#   Kayısı Nöronunun Çıktısı ---> 0.6
#
# En büyük çıktı 0.6 olan kayısı nöronuna ilişkindir. O halde biz bu kestirimin
# "kayısı" olduğuna karar veririz.
# =============================================================================
# Softmax fonksiyonu bir grup değer için o grup değerlere bağlı olarak şöyle
# hesaplanmaktadır:
#     softmax(x) = np.e ** x / np.sum(np.e ** x)
#
# Burada gruptaki değerler x vektörüyle temsil edilmektedir. Fonksiyonda
# değerlerinin e tabanına göre kuvvetleri x değerlerinin e tabanına göre
# kuvvetlerinin toplamına bölünmüştür.
# Bu işlemden gruptaki eleman sayısı kadar değer elde edilecektir ve bu değer-
# lerin toplamı 1 olacaktır.
# =============================================================================

from tensorflow.keras.activations import softmax
import tensorflow as tf
import numpy as np


def softmax_1(x):
    return np.e ** x / np.sum(np.e ** x)


x = np.array([3, 6, 4, 1, 7])
sm = softmax_1(x)

print(np.sum(sm))  # Toplamında 1 elde ederiz.

# =============================================================================
# softmax fonksiyonu Keras'ta tensorflow.keras.activations modülünde softmax
# ismiyle de bulunmaktadır. Ancak bu fonksiyonu kullanırken girdinin Tensorflow'
# daki bir Tensor nesnesi biçiminde ve iki boyutlu olarak verilmiş olması
# gerekmektedir. Tensorflow kütüphanesindeki aktivasyon fonksiyonları dışarıdan
# değil Tensorflow içerisinden kullanılsın diye tasarlanmıştır.
#
# Bu nedenle softmax gibi bazı fonksiyonlarda NumPy dizisi verilemez. Ayrıca
# Tensorflow'daki bu aktivasyon fonksiyonları birden fazla değer üzerinde
# de bir Tensor olarak işlem yapabilmektedir. (softmax fonksiyonunda aslında bir
# değer bir grup değerden oluştuğu için girdi olarak da iki boyutlu bir Tensor
# istenmektedir.) Örneğin:
# =============================================================================

x = np.array([[1, 2, 3, 4, 5]], dtype=np.float64)
t = tf.convert_to_tensor(x)  # tensor nesnesine dönüştür.
result = softmax(t)

print(result)
# <tf.Tensor: shape=(1, 5), dtype=float64,numpy=array([[0.01165623, 0.03168492,
#                                                       0.08612854, 0.23412166,
#                                                       0.63640865]])>
