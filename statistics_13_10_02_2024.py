''' x
    Bir deney sonucunda oluşacak durum baştan tam olarak belirlenemiyorsa böyle deneylere "rassal deney (random experiment)"
    denilmektedir. Örneğin bir paranın atılması deneyinde para "yazı" ya da "tura" gelebilir. O halde "paranın atılması" 
    rassal bir deneydir. Benzer biçimde bir zarın atılması, bir at yarışında hangi atın birinci olacağı gibi deneyler rassal 
    deneylerdir. Bir deneyin sonucu öndecen bilinebiliyorsa bu tür deneylere "deterministik deneyler" de denilmektedir. 
    Bazı bilimlerdeki süreçler deterministiktir. Ancak bazı bilimlerdeki süreçlerin sonucunda oluşacak durumlar önceden 
    tam olarak kestirilememektedir. Önceden sonucu tam olarak kestirilemeyen süreçlere "olasılıksal (probabilistic)" ya da 
    "stokastik (stochastic)" süreçler denilmektedir. 

    Deterministik süreçlerle olasılıksal süreçler aslında üzerinde çok düşünülmüş konulardandır. Kimilerine göre olasılıksal 
    süreç diye bir şey yoktur. Her şey deterministiktir. Bir sürecin olasılıksal olması sadece "bizim onun sonucunu belirle-   
    yemememizden" kaynaklanmaktır. Örneğin paranın atılması sırasındaki tüm bilgilere sahip olsak artık bu deneyin sonucu
    olasılıksal değil deterministik hale gelecektir. Tabii evrende kaotik bir süreçler söz konusudur. Yani bir olay başka bir
    olayı etkilemekte ve küçük değişiklikler büyük sonuçlara yol açabilmektedir. Buna feslefede "kaos teorisi" halk arasında
    da "kelebek etkisi" denilmektedir. Eğer evrende mutlak bir determinizm varsa evren reset konumuna alındığında yine bugüne
    her şey kurulu bir biçimde gelecektir.
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Bir rassal deney sonucunda oluşabilecek tüm olası durumların kümesine "örnek uzayı (sample space)" denilmektedir. Örneğin 
    bir paranın atılması deneyinde örnek uzayı S = { Yazı, Tura} biçimindedir. Biz zarın atılması deneyindeki örnek uzayı ise
    S = {1, 2, 3, 4, 5, 6} biçimindedir. İki zarın atılmasındaki örnek uzayı S = {(1, 1), (1, 2), (6, 5), (6, 6)} biçimindedir.

    Örnek uzayın her bir alt kümesine "olay (event)" denilmektedir. Örneğin bir zarın atılmasındaki bazı olaylar şunlar olabilir:

    E1 = {1, 3}
    E2 = {3, 4, 5}
    E3 = {6}

    Bir kümenin bütün alt kümelerine o kümenin "kuvvet kümesi (power set)" denilmektedir. Bir rassal deneydeki bütün olaylar
    kuvvet kümesi içerisindeki olaylardır. Bir kümenin tüm alt kümelerinin sayısı 2 ** n tanedir. 

    Örnek uzayın tek elemanlı olaylarına (yani alt kğmelerine) "basit olay (simple events)" denilmektedir. Örneğin paranın 
    atılması deneyindeki basit olaylar {Yazı} ve {Tura} biçimindedir. 
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Olasılığın (probablity) değişik tanımları yapılabilmektedir. Olasılığın en yaygın tanımlarından birisi "göreli sıklık 
    (relative frequency)" tanımıdır. Bu tanıma göre bir rassal olay çok sayıda yinelendikçe elde edilen olasılık değeri belli
    bir değere yakınsamaya başlar. Örneğin bir paranın 100 kere atılmasında 50 kere yazı 50 tura gelmeyebilir. Ancak para sonsuz
    sayıda atılırsa (ya da çok fazla sayıda atılırsa) tura gelme sayısının paranın atılma sayısına oranı 0.5'e yakınsayacaktır.
    Buna istatistike "büyük sayılar yasası (law of large numbers)" da denilmektedir. 

    Aşağıdaki örnekte bir para değişik miktarlarda yazı tura biçiminde atılmıştır. Elde edilen oranlar gitgide 0.5'e yakınsayacaktır.
    Programın çalıştırılmasıyla şu değerler elde edilmiştir:

    head = 0.4, tail = 0.6
    head = 0.5, tail = 0.5
    head = 0.479, tail = 0.521
    head = 0.4977, tail = 0.5023
    head = 0.50005, tail = 0.49995
    head = 0.500075, tail = 0.499925
    head = 0.5002417, tail = 0.4997583
    head = 0.49997078, tail = 0.50002922
#----------------------------------------------------------------------------------------------------------------------------

'''
import random

HEAD = 1


def head_tail(n):
    head = tail = 0

    for _ in range(n):
        val = random.randint(0, 1)
        if val == HEAD:
            head += 1
        else:
            tail += 1

    return head / n, tail / n


head, tail = head_tail(10)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(100)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(1000)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(10_000)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(100_000)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(1_000_000)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(10_000_000)
print(f'head = {head}, tail = {tail}')

head, tail = head_tail(100_000_000)
print(f'head = {head}, tail = {tail}')

# ----------------------------------------------------------------------------------------------------------------------------

'''
    Olasılığın temel matematiksel teorisi Kolmogorov tarafından oluşturulmuştur. Kolmogorov üç aksiyom kabul edildiğinde bütün
    olasılık kurallarının teoremiispat biçiminde açıklanabileceğini göstermiştir. Kolmogorov'un üç aksiyomu şöyledir:

    1) Örnek uzayının olsılığı 1'dir. Yani P(S) = 1'dir. Buradan olasılığın en yüksek değerinin 1 olacağını ve tüm örnek uzayının 
    olma olasılığının 1 olduğunu anlamalıyız. Örneğin bir zarın atılmasındaki örnek uzayı {1, 2, 3, 4, 5, 6} biçimindedir. 
    P({1, 2, 3, 4, 5, 6}) = 1'dir. Buradaki P({1, 2, 3, 4, 5, 6}) bir zarın 1 ya da 2 ya da 3 ya da 4 ya da 5 ya da 6 gelme olasılığı 
    anlamındadır. 

    2) Herhangi bir olayın olasılığı 0 ya da 0'dan büyüktür. Yani P(E) >= 0'dır. Burada olasılığın en düşük değerinin 0 olduğu 
    belirtilmektedir. O halde olasılık değeri 0 iel 1 arasındadır. 

    3) Bir kümenin olasılığı demek rassal deney sonucunda o kümenin herhangi elemanının oluşma olasılığı demektir. Örneğin 
    zarın atılmasındaki P({3, 5}) olasılığı zarın üç ya da 5 gelme olasılığı anlamına gelir. İki küme ayrıksa (yani ortak elemanları)
    yoksa Bu iki kğmenin birleşimlerinin olasılığı bu iki kğmenin olaıslık toplamlarına eşittir. Yani E1 ve E2 iki olay 
    olmak üzere eğer bu iki olay ayrıksa (yani E1 ⋂ E2 = ∅ ise) P{E1 ∪ E2} = P{E1} + P{E2}'dir.

    Bu üç kural kabul edildiğinde kümeler teorisi, permütasyon, kombinasyon gibi işlemlerle tüm olasılk formülleri elde edilebilmektedir.
#----------------------------------------------------------------------------------------------------------------------------
 
#----------------------------------------------------------------------------------------------------------------------------
    Olasılıkta ve istatistikte en çok kullanılan temel kavramlardan biri "rassal değişken (random variable)" denilen kavramdır. 
    Her ne kadar "rassal değişken" isminde bir "değişken" geçiyorsa da aslında rassal değişken bir fonksiyon belirtmektedir. 
    Rassal değişken bir rassal deney ile ilgilidir. Bir rassal deneyde örnek uzayın her bir elemanını (yani basit olayını)
    reel bir değere eşleyen bir fonksiyon belirtmektedir. Rassal değişkenler genellikle "sözel biçimde" ifade edilirler. 
    Ancak bir fonksiyon belirtirler. Rassal değişkenler matematiksel gösterimlerde genellikle büyük harflerle belirtilmektedir. 
    Örneğin:

    - R rassal değişkeni "iki zar atıldığında zaarların üzrindeki sayıların toplamını" belirtiyor olsun. Burada aslında R 
    bir fonksiyondur. Örnek uzayın her bir elemanını bir değere eşlemektedir. Matematiksel gösterimle R rassal değişkeni
    şöyle belirtilebilir:

    R: S -> R

    Burada R'nin  örnek uzayından R'ye bir fonksiyon belirttiği anlaşılmaıdır. Burada R fonksiyonu aşağıdaki gibi eşleme 
    yapmaktadır:

    (1, 1) -> 2
    (1, 2) -> 3
    (1, 3) -> 4
    ...
    (6, 5) -> 11
    (6, 6) -> 12

    K rassal değişkeni "rastgele seçilen bir kişinin kilosunu belirtiyor" olsun. Bu durumda örnek uzayı aslında dünyaki 
    tüm insanlardır. Burada K fonksiyonu da her insanı onun kilosuna eşleyen bir fonksiyondur. 

    C rassal değişkeni "rastgele seçilen bir rengin RGB değerlerinin ortalamasını" belirtiyor olsun. Bu duurmda her rengin
    bir RGB ortalaması vardır. Bu fonksiyon belli bir rengi alıp onun ortalamasını belirten bir sayıya eşlemektedir. 

    Rassal değişkenler kümeler üzerinde işlemler yapmak yerine gerçek sayılar üzerinde işlem yapmamızı sağlayan, anlatımlarda
    ve gösterimlerde kolaylık sağlayan bir kavramdır. 
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Her rassal değişkenin belli bir değer almasının bir olsaılığı vardır. Örneğin "iki zarın atılması deneyinde üste gelen sayılar
    toplamına ilişkin" R rassal değişkenini düşünelim. P(R = 5) demek S örnek uzayındaki 5 değerini veren kümenin olsılığı demektir. 
    Yani P(R = 5) ile aslında P({(1, 4), (4, 1) (2, 3), (3, 2)}) aynı anlamdadır. Buradaki P({(1, 4), (4, 1) (2, 3), (3, 2)}) olasılığın
    "bu değerlerden herhangi birinin oluşmasına yönelik" olasılık olduğunu anımsayınız. Bu olasılığın değeri 1/9'dur.

    Bir rassal değişkenin olasılığı belirtilirken P harfi olsılığı anlatmaktadır. Ancak bu P harfinden sonra bzı kişiler normal 
    parantezleri bazı kişiler küme parantezlerini tercih ederler. Yani örneğin bazı kişiler P(R = 5) gibi bir gösterimi tercih
    derken bazı kişiler P{R = 5} gösterimini tercih etmektedir. Küme parantezli gösterim aslında "R = 5" ifadesinin bir küme 
    belirttiğini ve bu kümenin olasılığının hesaplanmak istediğini" belirtmesi açısından daha doğal gibi gözükmektedir. 

    K rassal değişkeni rastgele seçilen bir insanın kilosunu belirtiyor olsun. Bu durumda K aslında tüm insanları tek tek 
    onların kilolarına eşleyen bir fonksiyondur. O halde P{K < 60} olasılığı aslında "rastgele seçilen bir kişinin kilosunun 
    60'tan küçük olması olasılığı" anlamına gelmektedir. 
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Rassal değişkenler tıpkı matematiksel diğer fonksiyonlarda olduğu gibi "kesikli (discrete)" ya da "sürekli (continuous)" 
    olabilmektedir. eğer bir rassal değişken (yani fonksiyon) teorik olarak belli bir aralıkta tüm gerçek sayı değerlerini 
    alabiliyorsa böyle rassal değişkenlere "sürekli (continous)" rassal değişkenler denilmektedir. Ancak bir rassal değişken
    belli bir aralıkta yalnızca belli gerçek sayı değerlerini alabiliyorsa bu rassal değişkenlere "kesikli (discrete)" rassal
    değişkenler denilmektedir. Örneğin "iki zarın atılmasında üste gelen sayılar toplamını belirten R rassal değişkeni" kesiklidir. 
    Çünkü yalnızca belli değerleri alabilmektedir. Ancak "rastgele seçilen bir kişinin kilosunu belirten" K rassal değişkeni
    süreklidir. Çünkü teorik olarak belli bir aralıkta tüm gerçek değerleri alabilir. (Biz kişilerin kilolarını yuvarlayarak ifade
    etmekteyiz. Ancak aslında onların kiloları belli aralıktaki tüm gerçek değerlerden biri olabilir.)

    Sürekli rassal değişkenlerin noktasal olasılıkları 0'dır. Örneğin "rastgele seçilen kişinin kilosunu" belirten K rassal
    değişkeni söz konusu olsun. P{K = 67} gibi bir olasılık aslında 0'dır. Çünkü gerçek sayı ekseninde sonsuz tane nokta vardır. 
    67 yalnızca bu sonsuz noktadan bir tanesini belirtir. Sayı / sonsuz da 0'dır. Ancak sürekli rassal değişkenlerin aralıksal
    olasılıkları 0 olmak zorunda değildir. Yani örneğin P{66 < K < 67} olasılığı 0 değildir. Burada {66 < K < 67} kümesinin de 
    elemanlarının sonsuz sayıda olduğuna dikkat ediniz. Artık bu hesap matematikte "limit, türev, integral" konularıyla 
    ilişkili hale gelmektedir. Sürekli rassal değişkenlerin aralıksal olasılıklarını belirtirken aralıklardaki '=' sembolünün 
    bir anlamının olmayacağına dikkat ediniz. Örneğin P{66 < K < 67} ile P{66 <= K <= 67} arasında aslında bir fark yoktur. 
    Bu konuda da kişiler farklı gösterimleri tercih edebilmektedir. Bazı kişiler bir tarafa '=' sembolünü koyup diğer tarafa
    koymamaktadır. Örneğin P{66 <= K < 67} gibi. Ancak bu '=' sembollerinin sürekli rassal değişkenlerde bir etkisi yoktur.
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Yapay zeka ve makine öğrenmesinde sürekli rassal değişkenler daha fazla karşımıza çıkmaktadır. Bu nednele biz sürekli rassal 
    değişkenler ve onların olasılıkları üzerinde biraz daha duracağız. 

    Sürekli bir rassal değişkenin aralıksal olasılıklarını hesaplama aslında bir "intergral" hesabı akla getirmektedir. İşte 
    sürekli rassal değişkenlrin aralıksal olasılıklarının hesaplanması için kullanılan fonksiyonlara "olasılık yoğunluk 
    fonksiyonları (probability density functions)" denilmektedir. Birisi bize bir rassal değişkenin belli bir aralıktaki 
    olasılığını soruyorsa o kişiin bize o rassal değişkene ilişkin "olasılık yoğunluk fonksiyonunu" vermiş olması gerekir. 
    Biz de örneğin P{x0 < X < x1} olasılığını x0'dan x1'e f(x)'in integrali ile elde ederiz. 

    Bir fonksiyonun olasılık yoğunluk fonksiyonu olabilmesi için -sonsuzdan + sonsuze integralinin (yani tüm eğri altında kalan
    alanın) 1 olması gerekir. Bir rassal değişkenin olasılık yoğunluk fonksiyonuna "o rassal değişkenin dağılımı" da denilmektedir.
#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------
    Pekiyi mademki bizim bir rassal değişkenin aralıksla olasılığını elde etmek için bir olasılık yoğunluk fonksiyonuna ihtiyacımız
    var o halde bu fonksiyonu nasıl elde edeceğiz? İşte pek çok rassal değişkenin olasılık yoğunluk fonksiyonunun bazı kalıplara
    uyduğu görülmektedir. Örneğin doğadaki pek çok olgunun (boy gibi, kilo gibi, zeka gibi) olasılık yoğunluk fonksiyonu 
    "normal dağılım" denilen eğriye uymaktadır. Normal dağılım eğrisine "Gauss eğrisi" ya da "çan eğrisi" de denilmektedir. 
    Ancak yukarıda da belirttiğimiz gibi aslında çeşitli olaylara uygulanabilecek değişik olasılık yoğunluk fonksiyonu kalıpları
    belirlenmiştir. Tabii bu eğriler birer kalıptır. Dolayısıyla bazı parametrelere de sahiptir. Örneğin sonsuz sayıda Gauss eğrisi
    oluşturulabilir. Gauss eğtisinin iki öenmli parametrik bilgisi "orta noktasını belirten "ortalama" ve zayıflığını ya da 
    şişmanlığını belirten "standart sapma" değeridir. 
    
    Bu durumda örneğin sürekli rassal değişkenlerle ilgili bir soru şöyle olabilir: "Kişlerin zekaları ortalaması 100 standart 
    sapması 15 olan normal dağılıma uygundur. Rastgele seçilen bir kişinin zekasının 120 ile 130 arasında olma olasılıı nedir?" 
    Burada bize rassal değişkenin olasılık yoğunluk fonklsiyonu parametreleriyle verilmiştir. Bizim de bu olasılığı hesaplamak
    için tek yapacağımız şey 120'den 130'a fonksiyonun integralini almaktır. 

    Pekiyi rassal değişkenimiz başkaları tarafından belirlenen herhangi bir kalıba uymuyorsa ne yapabiliriz? Bir rassal 
    değişkenin olasılık yoğunluk fonksiyonunun sıfırdan çıkarılması biraz zahmetli bir işlemdir. Kümülatif olasılıklar yardımıyla
    olasılık yoğunluk fonksiyonları tatmin edici bir biçimde elde edilebilmektedir. Ancak yukarıda da belirttiğimiz gibi
    aslında pek çok olay zaten tespit edilmiş çeşitli kalıplara uymaktadır.

'''
