import statistics
import numpy as np
import matplotlib.pyplot as plt


def gauss(x, mu=0, std=1):
    return 1 / (std * np.sqrt(2 * np.pi)) * np.e ** (-0.5 * ((x - mu) / std) ** 2)


def draw_gauss(mu=0, std=1):
    x = np.linspace(-5 * std + mu, 5 * std + mu, 1000)
    y = gauss(x, mu, std)

    mu_y = gauss(mu, mu, std)

    plt.figure(figsize=(10, 4))
    plt.title('Gauss Function', pad=10, fontweight='bold')
    axis = plt.gca()

    axis.set_ylim([-mu_y * 1.1, mu_y * 1.1])
    axis.set_xlim([-5 * std + mu, 5 * std + mu])
    axis.set_xticks(np.arange(-4 * std + mu, 5 * std + mu, std))
    # axis.set_yticks(np.round(np.arange(-mu_y, mu_y, mu_y / 10), 2))
    axis.spines['left'].set_position('center')
    axis.spines['top'].set_color(None)
    axis.spines['bottom'].set_position('center')
    axis.spines['right'].set_color(None)
    axis.plot(x, y)
    plt.show()

# draw_gauss(10, 15)

# =============================================================================
# Normal Dağılım ile İlgili İşlemler
# NormalDist nesnesi yaratılırken ortalama ve standart sapma değerleri girilir.
# Ortalama için sıfır, standart sapma için 1 default değerleri kullanılmaktadır.
# =============================================================================


nd = statistics.NormalDist()

# =============================================================================
# cdf (cummulative distribution function) metodu x için eğrinin solunda kalan
# toplam alanı yani kümülatif olasılığı vermektedir.
# Örneğin standart normal dağılımda x = 0'ın solunda alan 0.5'tir.
# Çünkü toplam alan 1'dir ve 0 tam ortadadır. Sağ ve sol 0.5' e eşittir.
# =============================================================================

result = nd.cdf(0)
print(result)  # 0.5

# =============================================================================
# ort = 100, std = 15 olan bir normal dağılımda P{120 < x < 130} olasılığını
# aşağıdaki gibi elde edebiliriz (Rastgele biri seçildiğinde zekasının 120 ile
# 130 arasında olma olasılığı):
# =============================================================================

nd2 = statistics.NormalDist(100, 15)
result2 = nd2.cdf(130) - nd2.cdf(120)
print(result2)  # - 0.06 - yüzde 6

# =============================================================================
# Rastgele seçilen birinin zekasının 140' dan büyük olma olasılığı nedir:
# (Zekası 140'dan büyük olanlar toplumun % kaçını oluşuturur?)
# Bu normal dağılımdaki P{X > 140} olasılığıdır. X ekseninde belli bir noktanın
# sağındaki kümülatif alan sorulmaktadır. Bu alanı veren doğrudan bir fonksiyon
# olmadığı için bu işlem 1 - F(140) biçiminde ele alınarak sonuç elde edilebilir.
# =============================================================================

nd3 = statistics.NormalDist(100, 15)
result3 = 1 - nd3.cdf(140)
print(result3)  # 0.003 - binde 3


# =============================================================================
# Belli bir kümülatif olasılık değeri için x değerinin bulunması işlemi de
# NormalDist sınıfının inv_cdf metoduyla yapılmaktadır.
# Örneğin standart normal dağılımda 0.99 olan kümülatif olasılığın Z değeri
# aşağıdaki gibi bulunabilir.
# (ort=100, std=15 olan zeka dağılımnda insanların %70' i hangi puan altındadır.):
# =============================================================================

nd4 = statistics.NormalDist(100, 15)
result4 = nd4.inv_cdf(0.7)
print(result4)


# =============================================================================
# Bir x değeri için Gauss fonksiyonunda ona karşı gelen y değeri sınıfın pdf
# metoduyla elde edilmektedir.
# Örneğin x = 0 için standart normal dağılımda Gauss fonksiyonu değerini
# aşağıdaki gibi elde edebiliriz:
# =============================================================================

nd5 = statistics.NormalDist()
result5 = nd5.pdf(0)
print(result5)
