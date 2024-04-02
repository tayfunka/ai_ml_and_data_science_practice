import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
# =============================================================================
# Bir önceki derste normal dağılımda temel 4 işlem önemlidir.
# =============================================================================

# =============================================================================
# İlk işlem belli bir x değeri için x' in solunda kalan alanı elde etmek.
# Yani kümülatif dağılım fonksiyonunun verdiği değeri elde etmek
# Bu işlem cdf metodu ile yapılmaktadır.
# Vektörel işlemler de yapılabilir.
# =============================================================================

result1 = norm.cdf([0.5, 1, 1.25])
print(result1)  # [0.69146246 0.84134475 0.89435023]

# =============================================================================
# Temel işlemlerden ikincisi iki x değeri arasındaki alanı elde etmek.
# Sağdaki x değeri soldaki x değerinden çıkarılır.
# =============================================================================

result2 = norm.cdf(0.7) - norm.cdf(0.4)
print(result2)

# =============================================================================
# Temel işlemlerden üçüncüsü ilk işlemin tersini yapmak.
# Yani bir alan veriliyorsa bu alana denk gelen x değerini bulmak.
# Kümülatif olasılığın bilindiği durumda bu olasılığa karşı gelen x değeri.
# Bu işlem için ppf metodu ile yapılmaktadır. (inv_cdf)
# Yani median değerini verir. Örneğin:
# Ortalama(loc) = 100, std = 15 olan bir dağılımda, 0.5 bize 100 değerini verir.
# Çünkü 0.5 bu dağılımın ortasındadır ve ortalama = 100' e eşittir.
# =============================================================================
result3 = norm.ppf(0.5, 100, 15)
print(result3)  # 100.0

# =============================================================================
# Temel işlemlerin dördüncüsü ise x değerinin Gaus eğrisindeki Y değerini verir.
# Yani x noktasının eğri üzerindeki y noktasını verir.
# Bu işlem pdf metodu ile yapılmaktadır. (probability density function)
# pdf(x, loc=0, scale=1)
# =============================================================================

x = np.linspace(-5, 5, 100)
y = norm.pdf(x)
# plt.title('Standart Normal Dağılım Fonskiyonu')
# plt.plot(x, y)

x2 = np.full(200, 0)  # 200 tane 0 oluştur
yend = norm.pdf(0)  # orta noktası 0 olan değerin eğrideki tepe noktası
y2 = np.linspace(0, yend, 200)  # 0' dan tepe noktasına doğru oluştur
# plt.plot(x2, y2, linestyle='--')

# =============================================================================
# rvs metodu normal dağılıma ilişkin rassal sayı üretir.
# revs(loc=0, scale=1, size=1)
# Aşağıdaki örnekte normal dağılım çubukları elde edilecektir:
# ort = 100, std = 15 olan 10000 tane değer
# =============================================================================

x3 = norm.rvs(100, 15, 10000)
# plt.hist(x3, bins=20)

# =============================================================================
# Normal dağılımda ortalamadan birer standart sapma arasındaki bölgenin olasılığı
# yani P{mu - sigma < x < mu + sigma} olasığılı 0.68 civarındadır.
# =============================================================================

MU = 0
STD = 1
plt.figure(figsize=(15, 8))
x4 = np.linspace(-5, 5, 100)  # noktaları oluştur
y4 = norm.pdf(x4, MU, STD)  # noktaların y değerlerini elde et
plt.plot(x4, y4)

x4 = np.linspace(MU - STD, MU + STD, 1000)
y4 = norm.pdf(x4)
plt.fill_between(x4, y4)
plt.show()
