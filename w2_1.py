
# encode - decode
text = """
Hatay’da 2019’da beton kalitesine yönelik yapılan saha araştırmasında, rastgele incelenen 525 binadan sadece 6’sının yönetmeliğe uygun inşa edildiği, her 3 binadan 1’inde korozyon saptandığı, sadece 16 yapının beton basınç dayanıklılığının standart ölçüde olduğu belirtiliyor.
525 binanın 6’sı kurallara uygun
MERT İNAN İstanbul - Depremin yıktığı Hatay’da 4 yıl önce İskenderun Teknik Üniversitesi İnşaat Mühendisliği Bölümü’nden Prof.Dr. Murat Bikçe ile Nilay Sabahoğlu tarafından gerçekleştirilen araştırma, olası depremde yaşanacak felaketi de önceden haber vermiş. Kentsel dönüşüm kapsamına alımış binaların beton numunelerinin incelenmesiyle gerçelkeştirilen araştırmada, her 3 yapından 1’inde korozyon (metalin oksitlenmesi, aşınması, paslanması) tespit edilirken, sadece 16 yapının beton basınç dayanımının standartlara uygun olduğu saptanmış.
ARAŞTIRMADAN VERİLER
Araştırma kapsamında incelemeye alınan binaların, yaşı, projeleri, beton basınç dayanımı, donatı tipi ve korozyon oranına yönelik tespit ve testler yapılırken, incelenen 25 yapıdan sadece yüzde 6.4’ünün projesinin olduğu bilgisine yer verildi. 1 Nisan 2019’a kadar 6306 sayılı Kanun kapsamında “Riskli yapı” olarak değerlendirilerek kentsel dönüşüme girmiş binaların 525’inin beton kalitesinin incelendiği çalışmada, elde edilen sonuçlar şöyle kayda geçmiş:
‘KOROZYON SAPTANDI’
“İncelenen binaların yüzde 37.33’ünde donatının korozyona uğradığı belirlenirken, bu binaların yüzde 68.1’lik gibi büyük bir kısmının 1975-90 yılları arasında olmasının yanı sıra, yüzde 2.6’lık gibi bir oranın yakın tarihte (2000-2015) arasında inşa edildiği saptandı. İncelenen betonarme binaların Afet Bölgelerinde Yapılacak Binalar Hakkında Yönetmeliği’nde en düşük beton sınıfı C20 iken, Türkiye Bina Deprem Yönetmeliği’nde bu sınıf en az C25’e yükseltilmiştir. İncelenen yapılardan Türkiye Bina Deprem Yönetmeliği hükümlerini sağlayan yalnızca 6 adet bina bulunmuştur.”
Ya Birinci Dünya Savaşı hiç yaşanmamış olsaydı? Strateji oyunu tarihi senaryoları simüle ediyor 
Tarihsel Strateji Oyunu
50 yıl önce nükleer bir sığınağa araba koydular. Sonra onu almak i̇çin geri geldiler
Trips-Shop.com
  by Taboola 
İlginizi çekebilir
Prof.Dr. Çelik: İstanbuldaki yapı stokunda ciddi bir sorunumuz var
Prof.Dr. Çelik: İstanbul'daki yapı stokunda ciddi bir sorunumuz var
Kahramanmaraşta 4.3 şiddetinde deprem
Kahramanmaraş'ta 4.3 şiddetinde deprem
Depremde ölen George Nuri Dagenhamı yasa boğdu
Depremde ölen 'George' Nuri Dagenham'ı yasa boğdu!
‘AZ KATLILAR DA RİSKLİ’

İncelemeye alınan 525 yapı numunesinden büyük çoğunluğunun, ortalama basınç dayanımlarının, ilgili standart ve yönetmelik şartlarını sağlamadığı belirtilen araştırmada ayrıca şu tespitlere yer veriliyor:

“Hatay’da riskli bina olarak tespit edilmiş rastgele seçilen 525 adet betonarme binanın istatistiksel değerlendirilmesi sonucu yapıların yüzde 88.1’lik kısmının 1970-95 arasında inşa edildiği ve bunların beton basınç dayanımlarının 5-15 MPa aralığında olduğu, yalnızca 16 adet binada basınç dayanımlarının 20-30 MPa aralığına girdiği, riskli olarak belirlenen yapıların büyük çoğunluğunun 1-2 katlı yapılar olduğu, incelenen binaların yüzde 37.3’ünde donatı korozyonu tespit edildiği, görülmüştür. Hatay aktif fayların etkisinde olması nedeniyle, can ve mal kayıplarını minimize edebilmek için mevcut yapıların değerlendirilmesi ve depreme dayanıklı hale dönüştürülmesi oldukça önemlidir. Yeni yapılacak yapıların da güncel deprem yönetmeliği ve standartları sağladığı kontrol edilerek denetlenmelidir.” tespitleri yer alıyor.


Prof.Dr. Murat Bikçe ile Nilay Sabahoğlu tarafından yapılan araştırmada aktif fayların etkisindeki Hatay’da can ve mal kayıplarını azaltmak için yapıların acilen depreme dayanıklı hale dönüştürülmesi konusunda da uyarılar yer alıyor.

525 binanın 6’sı kurallara uygun
‘BETON KALİTESİ DÜŞÜK’

Araştırma kapsamında 1960-2005 yılları arasında 5-15 MPa, yani düşük beton basınç dayanımlı binalar inşa edildiği vurgulanarak şu ifadelere yer veriliyor: “Hazır beton ilk olarak Almanya’da 1903 yılında ortaya çıkmasına rağmen, Türkiye’de 1976 yılından sonra kullanılmaya başlanmıştır. Ülkemizde hazır beton sektörünün başladığı yıldan sonra bile, olması gereken kalitede basınç dayanımları üretilmemiştir. Yıllara göre beton basınç dayanımında artış beklenirken, bu durumun pek de gerçekleşmediği anlaşılmaktadır.”
"""

"""
karakterler = set(list(text))
for c in karakterler:
	print(c, text.count(c))
"""


def findFreq( text: str ) -> dict:
	freq = {}
	for c in text:
		if c not in freq:
			freq[c] = 0
		freq[c] += 1.0 # / len(text)
	for c in freq:
		freq[c] = freq[c] / len(text)
	return freq


context = """
Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi
27 Şubat 2023 09:42Güncel Haberler
Son dakika: Kahramanmaraş merkezli meydana gelen depremlerde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi. Bölgedeki son durumu aktaran AFAD Başkanı Yunus Sezer, "Şu ana kadar 10 bine yakın artçı sarsıntı gerçekleşmiş durumda. 21 bine yakın binada arama kurtarma çalışmaları tamamlandı. Şu anda 8 bin 182 arama kurtarma personeli çalışmalara eşlik etmektedir" dedi. Öte yandan bölgede 287 tane çadır kent kurulurken, 10 binin üzerinde konteyner kurulumu ise devam ediyor.

6 Şubat'ta Kahramanmaraş merkezli meydana gelen 7.7 ve 7.6 büyüklüğündeki depremler nedeniyle 10 ilde büyük yıkıma neden oldu. Depremlerde çok sayıda bina yıkılırken, binlerce vatandaşımız hayatını kaybetti.

HAYATINI KAYBEDENLERİN SAYISI ARTIYOR
AFAD Başkanı Yunus Sezer, 6 Şubat'ta meydana gelen Kahramanmaraş merkezli depremlerde hayatını kaybedenlerin sayısının 44 bin 374 olduğunu bildirdi.


Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

9 BİN 990 ARTÇI SARSINTI GERÇEKLEŞTİ
Sezer, AFAD Başkanlığında düzenlediği basın toplantısında, depremin üzerinden 21 gün geçtiğini, bu süreçte hem 5 üzerinde depremler olduğunu hem de çok sayıda artçı sarsıntılar yaşandığını hatırlattı. Şu ana kadar 9 bin 990 artçı sarsıntı yaşandığını, bölgede toparlanma ve iyileşme sürecinin devam ettiğini dile getiren Sezer, "21 bine yakın binada arama kurtarma çalışmaları tamamlandı. Şu anda tamamen enkaz kaldırma çalışmalarına yoğunlaşmış durumdayız." diye konuştu.

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

230 BİNE YAKIN PERSONEL ÇALIŞMALARA DEVAM EDİYOR
Sezer, iyileştirme çalışmaları kapsamında, çadır, konteyner ve kalıcı konutların yapılmasına yönelik yoğun çalışmaların devam ettiğinin altını çizerek, sözlerine şöyle devam etti: "Bütün adımlar, hayatın bir an önce normalleşmesi adına yapılmaktadır. Maalesef bu süreç içerisinde 44 bin 374 insanımızı kaybetmiş durumdayız. Allah'tan rahmet diliyorum, milletimizin başı sağ olsun. Yoğun bir çalışma devam ediyor. Şu anda 8 bin 182 arama kurtarma personeli, yapılan enkaz çalışmalarına ve orada diğer yapılan çalışmalara eşlik etmektedir, 230 bine yakın bir personelimiz de şu anda çalışmalara devam ediyor.

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

78 UÇAK, 116 HELİKOPTERLE 13 BİN 771 SEFER DÜZENLENDİ
Uluslararası arama kurtarmadan da şu anda 1180 personel yine insani yardım faaliyetlerine destek vermeye çalışıyor. İl ve ilçelerimizde enkaz çalışmaları sürdürülüyor. Şu anda 12 bin 171 iş makinesi bölgede aktif bir şekilde bulunmaktadır. Hava araçlarını, hem insani yardım hem çadır göndermek üzere yoğun bir şekilde kullanıyoruz. Köylerimize ve deprem bölgesindeki en ücra noktalara kadar ulaşmaya çalışıyoruz. Hava, kara, kuvvetleri, sahil güvenlik, emniyet, jandarma ve deniz kuvvelerimize ait hava unsurları yoğun bir şekilde bu bölgede faaliyet yürütmektedir."

Sezer, şu anda 78 uçak, 116 helikopterle 13 bin 771 sefer düzenlendiğine işaret etti.

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

297 ÇADIR KENT KURULMUŞ DURUMDA
Barınma kapsamında çadır kentleri yoğun şekilde kurduklarının altını çizen Sezer, "Bu artçılar nedeniyle bireysel çadır talepleri de yoğun bir şekilde devam ediyor. Bölgeye günlük ortalama 10 binin üzerinde çadır sevk ediyoruz ve bunu en ücra noktalara kadar ulaştırıyoruz. Şu anda 287 tane çadır kentimiz var bölgede. Sadece çadır kentler kurmuyoruz, bunları sosyal donatılarıyla beraber her türlü psikososyal desteğin de verileceği şekilde düzenli alanlar oluşturulmaya çalışılıyor. " bilgisini paylaştı.

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

100 BİN ÜZERİNDE KOYTEYNER KISA SÜREDE FAALİYETE GEÇECEK
Sezer, 100 binin üzerinde konteyneri kısa sürede faaliyete geçirmeyi hedeflediklerine dikkati çekerek, sözlerini şöyle sürdürdü: "Bununla ilgili olarak da 143 alan şu an itibarıyla tespit edilmiş ve bunlardan 97'sinde alt yapı çalışmaları yoğun bir şekilde devam ediyor. Hatta 4 tanesi de dün itibarıyla bitirildi. Belirttiğim 97'sinde de altyapı çalışmaları yüzde 50'lere yakın bir oranda bitmiş durumda. 10 binin üzerinde konteynerin bölgede kurulum çalışmaları devam ediyor.

Afet bölgesinde barındırılan kişi sayısı olarak da 1 milyon 531 bin 283 afetten etkilenen vatandaşımız buradaki afet bölgelerinde çadırlarda, konteyner kentlerde, kamu misafirhaneleri ve uygun alanlarda misafir edilmektedir. Afet bölgesi dışında da tahliye ettiğimiz 563 bin afetzede vatandaşımız var. Bunlar da bulundukları illerde valiliklerin koordinasyonunda AFAD ve diğer birimlerle beraber oluşturulan komisyonlar marifetiyle hem barınma hem de diğer ihtiyaçlar karşılanacak şekilde çalışmalarımız devam ediyor."

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

918 BİN VATANDAŞA 10 BİN LİRALIK ÖDEMELER YAPILDI
Afetzedelere yapılan yardımlar konusunda Sezer, "Nakdi yardımlar konusunda 918 bin vatandaşımıza 10 bin liralık ödemeler yapıldı" dedi.

HATAY'DA ART ARDA DEPREMLER
Öte yandan, Kahramanmaraş merkezli depremlerde ağır hasar alan Hatay, 20 Şubat Pazartesi akşamı 6.4 ve 5.8 ile sallandı. Bu depremlerde hasarlı binalardan eşya almak isteyenlerin de aralarında olduğu 6 kişi yaşamını yitirdi, çok sayıda kişi ise yaralandı.

Son Dakika: Depremde hayatını kaybedenlerin sayısı 44 bin 374'e yükseldi

HASARLI BİNALARA GİRİŞLER İZNE TABİ OLACAK
Bu gelişmenin ardından AFAD tarafından hazırlanan genelgede, afet bölgesinde "yıkık" ve "acil yıktırılacak yapı" niteliğinde olduğu belirlenen yapılara kısa süreliğine de olsa girilmesi ve eşya alınmasının kesinlikle yasak olduğu belirtildi. Ağır hasarlı tüm yapılara giriş izni ve eşya alımının, Çevre, Şehircilik ve İklim Değişikliği Bakanlığınca görevlendirilen uzmanların raporu doğrultusunda değerlendirileceği ifade edilen genelgede, binası "ağır hasarlı" olarak belirlenmiş, 30 günlük süre içerisinde bina hasar durumuna itiraz etmeyecek vatandaşların eşyalarını alabilmelerinin, yapılarıyla ilgili uzmanlarca oluşturulacak tahliye raporuna uygun şekilde planlanacağı aktarıldı.

DEPREM BÖLGESİNDE İŞTEN ÇIKARMA YASAĞI
Cumhurbaşkanı Erdoğan'ın imzasıyla Resmi Gazete'de yayımlanan karara göre, deprem felaketi sebebiyle OHAL ilan edilen illerde istihdamın korunmasına yönelik tedbirler kapsamında işverenlere işten çıkarma yasağı getirildi. Yine kararnameye göre depremden etkilenen ve OHAL kapsamında bulunan kentlerdeki işverenler, işyerlerinin ağır ya da orta hasarlı olduğunu belgelemeleri durumunda, 'uygunluk tespiti' beklenmeksizin kısa çalışma ödeneğinden de yararlanabilecek.


Depremde harabeye dönen evi için gelen raporu görünce öfkeden deliye döndü: Vicdansızlar
27 Şubat 2023 00:05Güncel Haberler

Kahramanmaraş merkezli depremlerin ardından başlatılan hasar tespit çalışması devam ederken, bölgedeki bir vatandaş dikkat çeken bir iddiada bulundu. Depremde duvarları göçen ve yapısal bozulmalar olan bir binaya az hasarlı raporu verildiği öne sürülürken, apartman sakini bir vatandaş, "Vicdansızlar, bu bina hafif hasarlı olabilir mi? Sen çocuğunu, eşini, anneni burada bırakabilir misin?" sözleriyle tepki gösterdi.

Merkez üssü Kahramanmaraş olan 7.7 ve 7.6 büyüklüğündeki depremlerde 44 binden fazla vatandaşımız yaşamını yitirirken, 11 şehirde çok sayıda bina yerle bir oldu. Depremlerin ardından bölgede hasar tespit çalışmaları başlatılırken, dikkat çeken bir iddia ortaya atıldı.

Depremde hasar gören binaya verilen rapor vatandaşı çileden çıkardı: Sen çocuğunu, eşini burada bırakabilir misin?

"VİCDANSIZLAR, BU BİNA HAFİF HASARLI OLABİLİR Mİ?"
Show Haber'de yer alan habere göre, Muzaffer Çelik isimli vatandaş, yaşadığı apartmanın depremde ağır hasar aldığını ancak buna rağmen binaya az hasarlı raporu verildiğini iddia etti. Rapora itiraz eden Çelik, "Yetkililer geldi, bu binaya 'hafif hasarlı' raporu verdi. Vicdansızlar, bu bina hafif hasarlı olabilir mi? Sen çocuğunu, eşini, anneni burada bırakabilir misin?" sözleriyle tepki gösterdi.

REKLAM

ads by AdMatic

Depremde hasar gören binaya verilen rapor vatandaşı çileden çıkardı: Sen çocuğunu, eşini burada bırakabilir misin?

BİNA İÇİNDE VE DIŞINDA GÖÇMELER VAR
Görüntülerde ise binanın dış cephesinin duvarlarının göçtüğü ve bina içinde de göçükler ve yapısal bozulmalar olduğu görüldü.

2 il için korkutan deprem tahmin Belediye Başkanı söyledi şehrin yüzde 60-70'ini bırakmaz
2 il için korkutan deprem tahmin Belediye Başkanı söyledi şehrin yüzde 60-70'ini bırakmaz
Manisa Büyükşehir Belediye Başkanı Cengiz Ergün, Kahramanmaraş merkezli meydana gelen deprem felaketlerinin tüm Türkiye’yi derinden yaraladığını belirterek, korkutan bir tahminde bulundu. "30 senelik, 40 senelik, 50 senelik binaların o günün şartlarında ne şekilde yapıldığını hepimiz biliyoruz" diyen Ergün, "Bugün, Manisa merkezinde bunu baz aldığımızda Allah korusun bu şiddette bir deprem ne İzmir’in yarısını bırakır ne Manisa’nın yüzde 60’ını 70’ini bırakır" ifadelerini kullandı.
Abone ol
Manisa Büyükşehir Belediye Başkanı Cengiz Ergün, Milliyetçi Hareket Partisi İl Başkanı Cüneyt Tosuner ve yönetimini ziyaret etti. Başkan Ergün’e ziyaretinde Manisa Büyükşehir Belediye Meclisi MHP Grup Başkanvekili Mehmet Güzgülü, Büyükşehir Belediye Meclis Üyesi Mehmet Palabıyık eşlik etti. Başkan Ergün, il başkanı ve yönetim kurulu üyelerine yeni görevlerinin hayırlı olması dileklerini iletirken, başarılar diledi.

Kahramanmaraş’ta meydana gelen depremlerin ardından yapılan ve planlanan yardımlar hakkında fikir alışverişinde bulunulurken, Manisa Büyükşehir Belediyesi olarak yapılan yardımların devam edeceğini söyleyen Başkan Ergün, hayatını kaybedenlere yüce Allah’tan rahmet, ailelerine ve yakınlarına başsağlığı, yaralılara acil şifalar diledi. Belediye Başkanı Cengiz Ergün parti teşkilatı ile de bir araya geldi.

Deprem ne İzmir’in yarısını bırakır ne Manisa’nın yüzde 60’ını 70’ini bırakır
Kahramanmaraş merkezli meydana gelen deprem felaketlerinin tüm Türkiye’yi derinden yaraladığını belirten Ergün, “Rabbim bir daha böyle acılar yaşatmasın. Devletimiz güçlüdür, el birliğiyle hep beraber bunun da üstesinden geleceğimize inancımız sonsuz. Binlerce insanımızı kaybetmiş olmamız bizim için büyük bir acı. Bu sadece o bölgedeki illerimizin değil, 81 ilimizin de gerçeği. Tabi ki yılların getirdiği bir birikim var. 30 senelik, 40 senelik, 50 senelik binaların o günün şartlarında ne şekilde yapıldığını hepimiz biliyoruz. Rabbim diğer şehirlerimize böyle bir acı göstermesin. Bugün, Manisa merkezinde bunu baz aldığımızda Allah korusun bu şiddette bir deprem ne İzmir’in yarısını bırakır ne Manisa’nın yüzde 60’ını 70’ini bırakır. Ama bundan sonraki süreç için iyi bir planlamanın başlangıcını geçtiğimiz hafta içerisinde verdik. Celal Bayar Üniversitesi İnşaat Mühendisliği bölümü hocalarımızla bir komisyon oluşturduk. Komisyonun çalışmalarını başlattık.

Çevre, Şehircilik ve İklim Değişikliği İl Müdürlüğünü dahil ederek hatta İnşaat Mühendisleri Odası’ndan da destek alarak el birliğiyle Manisa’nın röntgenini çekme noktasında çalışmalara başladık. Dün de yaptığımız görüşmelerde belli başlıklar belirlendi. Bu başlıklar nezdinde tamamen Büyükşehir’in imkanları dahilinde ücretlerini ödemek suretiyle bir master planını hayata geçirelim düşüncesindeyiz. Tabii ki sadece röntgen çekmek değil, bundan sonraki süreçlerde bu inşaatların planlı bir şekilde yapımlarındaki kontrol ve takip de çok önemli. Yapı denetimlerinin burada kanun nezdindeki yetkilerini kullanması gibi birçok madde var. Bu dönüşüm kolay değil. Her şeyden önce insanların evini yıkması ve bunun karşılığında binlerce insanın da kiraya çıkması gibi getirdiği konular var. Bu, bir iki senede olacak şeyler değil. Süreç içerisinde çözülecek” ifadelerini kullandı.

"""





chars = ['P', '0', 'H', 'K', 's', 'ö', 'u', 'g', 'c', 'k', '9', ' ', 't', 'v', '-', 'Y', 'ğ', 'Z', '?', 'z', '6', 'A', '2', 'o', 'm', '.', 'R', 'Ü', 'G', 'M', 'V', ',', 'Ç', 'ç', ')', 'h', 'ş', 'n', 'I', 'S', '‘', 'T', '”', "'", 'E', 'y', 'L', 'Ş', '8', 'C', '5', 'b', 'a', '\n', '3', 'ü', 'l', '’', 'r', '!', '̇', ':', '(', 'D', 'j', 'O', 'N', 'e', 'p', 'ı', '1', 'f', 'i', '4', 'İ', '7', 'B', 'd', '“']
import random
mapper = {i:None for i in chars}
for m in mapper:
	c = random.choice(chars)
	chars.remove(c)
	mapper[m] =c

print(mapper)

new_text = ""
for t in text: new_text += mapper[t]


encoded = findFreq(new_text)
general = findFreq(context)

encoded = [(k, v) for k, v in sorted(encoded.items(), key=lambda item: item[1], reverse=True)]
general = [(k, v) for k, v in sorted(general.items(), key=lambda item: item[1], reverse=True)]

"""
a = (36.345643, 26.345353)
a = [2,3,4]
a = {"key": "value"}
a = {3,4,5}
"""

print(encoded[0:10])
print(general[0:10])

print(mapper)
remapper = {}
for i in range(len(encoded)-10):
	e = encoded[i][0]
	g = general[i][0]
	remapper[e] = g

regenerated = ""
for n in new_text:
	if n in remapper:
		regenerated += remapper[n]

print(regenerated)




