from qcommon import Q, write

US = "Üst solunum yolları"
AS = "Alt solunum yolları"
AP = "Akciğerler ve plevra"

questions = [
# ------------------------------------------------------------------ Üst solunum yolları
Q("fv", US, """12 yaşında çocuk burnunu kaşıdıktan sonra başlayan burun kanamasıyla getiriliyor; kanama
burnun ön kısmından ve basıyla duruyor. Kanamanın en olası kaynağı neresidir?""",
  "Septumun ön-alt kısmındaki Kiesselbach (Little) alanı",
  ["A. sphenopalatina'nın burun boşluğuna girdiği arka bölge", "Concha nasalis media'nın mukozası",
   "Sinus maxillaris'in ostiumu", "A. carotis interna'nın kavernöz bölümü"],
  """Burun kanamalarının yaklaşık %90'ı septumun ön-alt kısmındaki zengin anastomoz ağından olur; burada
  a. sphenopalatina, a. ethmoidalis anterior, a. palatina major ve a. labialis superior'un septal dalları
  birleşir. Arka kanamalar a. sphenopalatina kaynaklıdır ve daha ağır seyreder.""",
  e=["cavitas-nasi"]),

Q("f", US, "Ductus nasolacrimalis burun boşluğunun neresine açılır?",
  "Meatus nasi inferior",
  ["Meatus nasi medius", "Meatus nasi superior", "Recessus sphenoethmoidalis", "Hiatus semilunaris"],
  """Gözyaşı kesesinden inen nazolakrimal kanal alt konkanın altındaki meatus nasi inferior'a açılır; ağzında
  Hasner kapakçığı vardır. Ağlarken burnun akması bu bağlantıdandır.""",
  e=["cavitas-nasi", "apparatus-lacrimalis", "concha-nasalis-inferior"]),

Q("t", US, "Paranazal sinüslerin burun boşluğuna açıldığı yerlerle ilgili hangisi yanlıştır?",
  "Sinus sphenoidalis – meatus nasi medius",
  ["Sinus maxillaris – meatus nasi medius (hiatus semilunaris)", "Sinus frontalis – meatus nasi medius",
   "Cellulae ethmoidales posteriores – meatus nasi superior", "Ductus nasolacrimalis – meatus nasi inferior"],
  """Sfenoid sinüs üst konkanın arka-üstündeki recessus sphenoethmoidalis'e açılır. Frontal, maksiller ve ön
  etmoid hücreler orta meatusa (ostiomeatal kompleks), arka etmoid hücreler üst meatusa açılır.""",
  e=["sinus-paranasales", "cavitas-nasi"]),

Q("fv", US, """Üst azı dişinden kanal tedavisi gören hastada tek taraflı kötü kokulu burun akıntısı ve yanakta
ağrı gelişiyor. En olası tutulum hangi sinüstedir ve neden?""",
  "Sinus maxillaris; üst azı dişlerinin kökleri sinüs tabanına çok yakındır.",
  ["Sinus frontalis; dişlerle doğrudan bağlantılıdır.", "Sinus sphenoidalis; diş kökleri bu sinüse uzanır.",
   "Cellulae ethmoidales; alveol kemiği etmoid kemiğin parçasıdır.", "Sinus maxillaris; ostiumu sinüsün tabanındadır."],
  """Maksiller sinüs en büyük paranazal sinüstür ve tabanı üst 1–2. büyük azı dişlerinin kökleriyle komşudur;
  odontojenik sinüzit bu nedenle burada görülür. Ostiumu sinüsün yüksek bir noktasında olduğu için drenaj
  yerçekimine ters yöndedir.""",
  e=["sinus-paranasales", "maxilla", "dentes"]),

Q("f", US, "Ses tellerini açan (abdüksiyona getiren) tek gırtlak kası hangisidir?",
  "M. cricoarytenoideus posterior",
  ["M. cricoarytenoideus lateralis", "M. cricothyroideus", "M. arytenoideus transversus", "M. thyroarytenoideus"],
  """Posterior krikoaritenoid kas aritenoid kıkırdakların processus muscularis'ini arkaya-içe çekerek ses
  tellerini açar ve rima glottidis'i genişletir. Bu kasın iki taraflı felci hava yolunu tehdit eder.""",
  e=["mm-laryngis", "larynx"]),

Q("tv", US, """Tiroidektomi sonrası profesyonel şarkıcı hasta konuşabiliyor ancak yüksek perdeli sesleri
çıkaramıyor ve sesi çabuk yoruluyor. Ameliyat sırasında hangi damarın bağlanması sırasında hangi sinir
yaralanmıştır?""",
  "A. thyroidea superior – n. laryngeus superior'un dış dalı",
  ["A. thyroidea inferior – n. laryngeus recurrens", "A. thyroidea ima – n. vagus",
   "V. thyroidea media – n. laryngeus recurrens", "A. thyroidea superior – n. laryngeus superior'un iç dalı"],
  """N. laryngeus externus a. thyroidea superior ile birlikte seyreder ve ses tellerini geren m. cricothyroideus'u
  innerve eder. Arter bezin üst kutbuna yakın bağlanırsa sinir korunur. İç dal duyusaldır; yaralanması
  aspirasyon riskini artırır.""",
  e=["mm-laryngis", "glandula-thyroidea", "n-vagus"]),

Q("tv", US, """Total tiroidektomi sonrası ekstübe edilen hastada inspiratuvar stridor ve ciddi solunum sıkıntısı
gelişiyor; konuşması zayıf. Laringoskopide iki ses telinin orta hatta yakın durduğu görülüyor. En olası
neden nedir?""",
  "İki taraflı n. laryngeus recurrens yaralanması",
  ["Tek taraflı n. laryngeus recurrens yaralanması", "İki taraflı n. laryngeus externus yaralanması",
   "N. hypoglossus yaralanması", "N. phrenicus yaralanması"],
  """Rekürren sinirler m. cricoarytenoideus posterior dahil tüm iç gırtlak kaslarını (cricothyroideus hariç)
  innerve eder. İki taraflı hasarda abduktör kaybı nedeniyle ses telleri orta hatta kalır, glottis daralır
  ve acil trakeostomi gerekebilir. Tek taraflı hasar ses kısıklığı yapar.""",
  e=["mm-laryngis", "n-vagus", "glandula-thyroidea"]),

Q("t", US, "Membrana thyrohyoidea'yı a. laryngea superior ile birlikte delerek gırtlağa giren sinir hangisidir?",
  "N. laryngeus superior'un iç dalı (n. laryngeus internus)",
  ["N. laryngeus recurrens", "N. laryngeus superior'un dış dalı", "N. hypoglossus", "N. glossopharyngeus"],
  """İç dal ses tellerinin üstündeki gırtlak mukozasının ve piriform girintinin duyusunu alır; yabancı cisimle
  oluşan öksürük refleksinin afferent koludur. Dış dal ise membranı delmez, m. cricothyroideus'a iner.""",
  e=["larynx", "n-vagus", "cartilagines-laryngis"]),

Q("fv", US, """Restoranda yemek yerken boğulan ve konuşamayan, entübasyonu başarısız olan hastaya acil cerrahi
hava yolu açılacak. Kesi boyunda hangi yapıdan yapılır?""",
  "Tiroid kıkırdak ile krikoid kıkırdak arasındaki lig. cricothyroideum medianum",
  ["Tiroid kıkırdak ile hyoid kemik arasındaki membrana thyrohyoidea", "Tiroid bezinin isthmusu",
   "Krikoid kıkırdağın kendisi", "1. ve 2. trakea halkaları arasındaki bağ"],
  """Krikotiroid membran deri altında kolayca ele gelir, büyük damarlardan uzaktır ve ses tellerinin altındadır.
  Krikotiroidotomi acil durumlarda trakeostomiden daha hızlı ve güvenlidir.""",
  e=["cartilagines-laryngis", "larynx"]),

Q("t", US, "Küçük çocuklarda üst hava yolunun en dar yeri neresidir?",
  "Krikoid kıkırdak düzeyindeki subglottik bölge",
  ["Rima glottidis", "Gırtlak girişi (aditus laryngis)", "Trakeanın bifurkasyonu", "Nazofarinks"],
  """Erişkinde hava yolunun en dar yeri ses yarığıdır; çocukta ise tam halka olan krikoid kıkırdak düzeyidir.
  Bu nedenle çocuklarda subglottik ödem (krup) ve entübasyon tüpü seçimi önemlidir.""",
  e=["larynx", "cartilagines-laryngis", "plicae-vocales"]),

Q("fv", US, """3 yaşında aşısız çocuk yüksek ateş, salya akıtma, boğuk ses ve öne eğilerek oturma ile getiriliyor;
yan boyun grafisinde 'başparmak işareti' görülüyor. Tutulan yapı hangisidir?""",
  "Epiglottis",
  ["Tonsilla palatina", "Trakea", "Ses telleri", "Tonsilla pharyngea"],
  """Akut epiglottit (çoğunlukla H. influenzae tip b) epiglotu ödemli ve kırmızı yapar; hava yolu hızla
  tıkanabilir. Muayene sırasında boğaza dil basacağıyla bakılmamalı, hava yolu kontrollü ortamda güvenceye
  alınmalıdır.""",
  e=["epiglottis", "larynx"]),

Q("f", US, "Solunum yolunda tam halka biçiminde olan tek kıkırdak hangisidir?",
  "Cartilago cricoidea",
  ["Cartilago thyroidea", "Epiglottis", "Trakea halkaları", "Cartilago arytenoidea"],
  """Krikoid kıkırdak arkada geniş lamina, önde dar kemer biçiminde tam bir halkadır ve C6 düzeyindedir.
  Trakea kıkırdakları ise arkası açık C biçimli halkalardır.""",
  e=["cartilagines-laryngis"]),

Q("t", US, "Ses telleri (plicae vocales) ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Zengin lenfatik ağa sahip oldukları için glottik kanserler erken lenf nodu metastazı yapar.",
  ["Serbest kenarları çok katlı yassı epitelle örtülüdür.", "İçlerinde lig. vocale ve m. vocalis bulunur.",
   "Ses telleri arasındaki aralık rima glottidis'tir.", "Üstlerindeki kıvrımlar plicae vestibulares'tir."],
  """Ses telleri lenfatikten çok fakirdir; bu nedenle glottik kanserler geç metastaz yapar ve erken ses kısıklığı
  nedeniyle erken tanınır. Supraglottik kanserler ise zengin lenfatik ağ nedeniyle erken boyun metastazı
  yapar.""",
  e=["plicae-vocales", "larynx"]),

# ------------------------------------------------------------------ Alt solunum yolları
Q("f", AS, "Trakea nerede başlar ve hangi düzeyde ikiye ayrılır?",
  "C6 düzeyinde krikoid kıkırdağın altında başlar; T4–T5 düzeyinde (angulus sterni) ikiye ayrılır.",
  ["C3 düzeyinde hyoid altında başlar; T10 düzeyinde ikiye ayrılır.", "C4 düzeyinde tiroid kıkırdak altında başlar; T2 düzeyinde ikiye ayrılır.",
   "C7 düzeyinde başlar; T8 düzeyinde ikiye ayrılır.", "C6 düzeyinde başlar; T12 düzeyinde ikiye ayrılır."],
  """Trakea 10–12 cm uzunluğundadır. Bifurkasyon angulus sterni düzlemindedir; içte karina adı verilen sırt
  bulunur. Derin inspirasyonda bifurkasyon bir omur kadar aşağı iner.""",
  e=["trachea", "sternum"]),

Q("t", AS, "Trakeostomide tiroid bezinin hangi bölümü genellikle 2.–4. trakea halkalarının önünde bulunur ve kenara çekilir veya kesilir?",
  "Isthmus glandulae thyroideae",
  ["Lobus pyramidalis", "Sağ lobun üst kutbu", "Paratiroid bezleri", "Sol lobun alt kutbu"],
  """Tiroid isthmusu genellikle 2.–4. trakea halkalarının önündedir. Trakeostomide isthmus yukarı çekilir veya
  bölünür. Bazı kişilerde orta hatta a. thyroidea ima bulunur ve kanama riski taşır.""",
  e=["trachea", "glandula-thyroidea"]),

Q("fv", AS, """Fıstık yerken öksüren 4 yaşında çocukta sağ akciğerde solunum sesleri azalmış. Yabancı cismin
neden en sık sağ ana bronşa kaçtığını en iyi açıklayan hangisidir?""",
  "Sağ ana bronş daha geniş, daha kısa ve trakeanın devamı gibi daha dik seyreder.",
  ["Sol ana bronş aort kemeri tarafından tamamen kapatılmıştır.", "Sağ ana bronşun kıkırdak halkası yoktur.",
   "Sağ akciğer daha yukarıda yer alır.", "Karina sağa doğru eğimlidir ve sol bronşu kapatır."],
  """Sağ ana bronş trakeayla yaklaşık 25°, sol ana bronş ise 45° açı yapar. Sağ bronş daha geniş ve kısa
  olduğundan aspire edilen cisimler ve aşırı ilerletilen entübasyon tüpleri çoğunlukla sağa girer.""",
  e=["bronchi", "trachea"]),

Q("tv", AS, """Alkol entoksikasyonu ile sırtüstü yatarken kusan hastada birkaç gün sonra aspirasyon pnömonisi
gelişiyor. Bu pozisyonda aspirasyonun en sık gittiği segment hangisidir?""",
  "Sağ alt lobun superior segmenti (BVI)",
  ["Sağ orta lobun medial segmenti", "Sol üst lobun lingular segmenti", "Sağ alt lobun anterior bazal segmenti", "Sol üst lobun anterior segmenti"],
  """Sırtüstü yatarken en bağımlı (aşağıda kalan) bronşlar alt lobların superior segment bronşları ve üst lobun
  posterior segment bronşudur; sağ bronşun dikliği nedeniyle sağ taraf daha sık tutulur. Ayakta veya otururken
  aspirasyon sağ alt lobun bazal segmentlerine gider.""",
  e=["segmenta-bronchopulmonalia", "bronchi"]),

Q("f", AS, "Bronkopulmoner segment ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Segmental bronş ve pulmoner arter dalı segmentin ortasında, pulmoner venler segmentler arasında seyreder.",
  ["Pulmoner venler segmentin merkezinde, arterler segmentler arasında seyreder.", "Sağ akciğerde 8 segment vardır.",
   "Segmentler arasında bağ dokusu bölmesi yoktur.", "Her segmentin kendi ana bronşu vardır."],
  """Segment, kendi segmental bronşu ve arterine sahip, cerrahi olarak çıkarılabilir birimdir. Segmentler arası
  düzlemi intersegmental venler belirler. Sağ akciğerde 10, solda 8–10 segment bulunur.""",
  e=["segmenta-bronchopulmonalia"]),

# ------------------------------------------------------------------ Akciğerler ve plevra
Q("f", AP, "Sağ akciğerin fissürleri ve lob sayısı ile ilgili hangisi doğrudur?",
  "Oblik ve horizontal fissür ile üç loba ayrılır; horizontal fissür önde 4. kaburga kıkırdağı hizasındadır.",
  ["Yalnızca oblik fissür ile iki loba ayrılır.", "Horizontal fissür 6. kaburga hizasındadır.",
   "Lingula sağ akciğerdedir.", "Oblik fissür önde 2. kaburga hizasında sonlanır."],
  """Sağ akciğer üst, orta ve alt loblardan oluşur. Oblik fissür arkada T3–T4 dikensi çıkıntısı hizasından
  başlayıp önde 6. kaburga kıkırdağına iner; horizontal fissür 4. kaburga kıkırdağı boyunca uzanır. Sol
  akciğerde horizontal fissür yoktur.""",
  e=["pulmo-dexter", "pulmones"]),

Q("f", AP, "Sol akciğere özgü yapılar hangisinde birlikte verilmiştir?",
  "Incisura cardiaca ve lingula",
  ["Horizontal fissür ve orta lob", "Eparteriyel bronş ve ara bronş", "V. azygos izi ve horizontal fissür", "Üç lob ve iki fissür"],
  """Sol akciğerin ön kenarında kalbin oluşturduğu incisura cardiaca ve altında dil biçimli lingula bulunur.
  Lingula sağ orta lobun karşılığıdır ve kendi segmental bronşlarına sahiptir.""",
  e=["pulmo-sinister"]),

Q("t", AP, "Sağ akciğer hilusunda en üstte yer alan yapı hangisidir?",
  "Üst lob (eparteriyel) bronşu",
  ["A. pulmonalis dextra", "V. pulmonalis superior", "V. pulmonalis inferior", "Lig. pulmonale"],
  """Sağ üst lob bronşu ana bronştan pulmoner arterin üstünde ayrılır (eparteriyel bronş). Sol hilusta ise
  en üstte pulmoner arter bulunur. Her iki tarafta pulmoner venler en önde ve en altta yer alır.""",
  e=["hilum-pulmonis", "bronchi"]),

Q("t", AP, "Akciğer dokusunu besleyen bronşiyal arterlerle ilgili hangisi doğrudur?",
  "Sol bronşiyal arterler doğrudan inen aortadan, sağ bronşiyal arter çoğunlukla 3. arka interkostal arterden çıkar.",
  ["Pulmoner arterin dallarıdır.", "A. subclavia'nın ilk dalıdır.", "Yalnızca deoksijenize kan taşır.", "A. thoracica interna'dan çıkar."],
  """Bronşiyal arterler sistemik dolaşımın parçasıdır ve bronş duvarlarını, visseral plevrayı ve bağ dokusunu
  besler. Hemoptizinin büyük kısmı bu arterlerden kaynaklanır ve embolizasyonla tedavi edilebilir.""",
  e=["hilum-pulmonis", "aorta", "pulmones"]),

Q("t", AP, "Parietal plevranın alt sınırı midklavikular, midaksiller ve paravertebral hatlarda sırasıyla hangi kaburgaların hizasındadır?",
  "8, 10 ve 12. kaburgalar",
  ["6, 8 ve 10. kaburgalar", "7, 9 ve 11. kaburgalar", "10, 12 ve T12 omuru", "4, 6 ve 8. kaburgalar"],
  """Akciğerin alt kenarı sakin solunumda 6, 8 ve 10. kaburgaları izler; plevra iki kaburga daha aşağıya
  (8, 10, 12) iner. Aradaki boşluk recessus costodiaphragmaticus'tur. Plevra arkada 12. kaburganın altına
  uzanabildiğinden böbrek cerrahisinde yaralanabilir.""",
  e=["pleura", "pulmones", "costae"]),

Q("fv", AP, """Ayakta çekilen grafide plevral efüzyon saptanan hastaya torasentez yapılacak. Sıvı en önce
nerede birikir ve iğne nereden girilmelidir?""",
  "Recessus costodiaphragmaticus'ta; arka aksiller hatta efüzyon düzeyinin altında, kaburganın üst kenarından",
  ["Recessus costomediastinalis'te; sternum kenarından", "Plevra kubbesinde; klavikula üstünden",
   "Lig. pulmonale çevresinde; paravertebral hattan kaburganın alt kenarından", "Fissura obliqua içinde; midklavikular hattan"],
  """Kostodiyafragmatik girinti ayakta duranlarda plevra boşluğunun en alçak yeridir. İğne genellikle arka aksiller
  hatta, efüzyonun bir-iki aralık altında ve kaburganın üst kenarından ilerletilerek interkostal damar-sinir
  paketi korunur.""",
  e=["pleura", "costae"]),

Q("t", AP, "Plevranın innervasyonu ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Diyafram plevrasının merkezî kısmındaki tahriş ağrıyı omuz ucuna yansıtır (n. phrenicus).",
  ["Visseral plevra ağrıya çok duyarlıdır.", "Kostal plevra n. vagus ile innerve edilir.",
   "Mediastinal plevra interkostal sinirlerle innerve edilir.", "Plevral ağrı her zaman göbek çevresine yansır."],
  """Parietal plevranın kostal kısmı ve diyafram plevrasının çevresi interkostal sinirlerle (lokalize ağrı),
  mediastinal ve merkezî diyafram plevrası n. phrenicus ile innerve edilir. Visseral plevra otonom lifler alır
  ve ağrıya duyarsızdır.""",
  e=["pleura", "n-phrenicus", "n-intercostales"]),

Q("tv", AP, """Kaza sonrası pnömotoraks gelişen erişkin hastaya göğüs tüpü takılacak. Yaralanma riskini en aza
indiren 'güvenli üçgen'in sınırları hangisidir?""",
  "M. pectoralis major'un dış kenarı, m. latissimus dorsi'nin ön kenarı ve meme başı (5. interkostal aralık) düzeyi",
  ["Klavikula, sternum ve 2. kaburga", "M. trapezius, skapula iç kenarı ve 7. kaburga",
   "Linea alba, kaburga kavsi ve göbek", "M. serratus anterior, m. teres major ve klavikula"],
  """Güvenli üçgende tüp genellikle 4. veya 5. interkostal aralıktan, ön aksiller hatta veya hemen arkasında
  yerleştirilir. Bu bölge büyük damarlardan, a. thoracica interna'dan ve diyaframdan uzaktır; tüp kaburganın
  üst kenarından geçirilir.""",
  e=["pleura", "mm-intercostales", "m-latissimus-dorsi"]),

Q("f", AP, "Akciğer zirvesi (apex pulmonis) ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Plevra kubbesiyle birlikte klavikulanın iç 1/3'ünün 2–3 cm üstüne kadar boyna uzanır.",
  ["Klavikulanın altında kalır ve boyna uzanmaz.", "Sternum arkasında orta hatta yer alır.",
   "T10 omuru düzeyindedir.", "Diyaframın hemen üstündedir."],
  """Akciğer apeksi ve plevra kubbesi (cupula pleurae) boyun tabanına uzanır; m. scalenus anterior ve a. subclavia
  ile komşudur. Boyun yaralanmalarında, subklavyen ven kateterizasyonunda ve supraklaviküler blokta pnömotoraks
  gelişebilir.""",
  e=["pulmones", "pleura", "clavicula"]),

Q("f", AP, "Lig. pulmonale nedir?",
  "Akciğer kökünü saran plevranın aşağı doğru uzanan çift katlı kıvrımı",
  ["Akciğeri diyaframa bağlayan fibröz bant", "Trakeayı sternuma bağlayan bağ", "Visseral plevranın fissür içindeki bölümü", "Bronşları birbirine bağlayan kıkırdak bağ"],
  """Akciğer kökünde parietal plevra visseral plevraya devam ederken kökün altında boş bir manşet gibi aşağı sarkar;
  bu çift katlı kıvrım lig. pulmonale'dir. Alt lob rezeksiyonlarında kesilmesi gerekir; içinde küçük lenf
  düğümleri bulunabilir.""",
  e=["pleura", "hilum-pulmonis"]),

Q("fv", AP, """Kilo kaybı ve myastenia gravis tanısı olan hastanın göğüs BT'sinde ön mediastende kitle var. En
olası tanı hangisidir?""",
  "Timoma",
  ["Nörojenik tümör (schwannom)", "Bronkojenik kist", "Özofagus leiomiyomu", "Aort anevrizması"],
  """Ön mediasten kitlelerinin akılda kalması için '4T' kullanılır: timoma, teratom (germ hücreli tümörler),
  tiroid (retrosternal guatr) ve 'terrible' lenfoma. Myastenia gravis hastalarının bir kısmında timoma bulunur.
  Arka mediastende en sık nörojenik tümörler görülür.""",
  e=["mediastinum", "thymus"]),

Q("t", AP, "Aşağıdaki yapılardan hangisi arka mediastende bulunmaz?",
  "N. phrenicus",
  ["Ductus thoracicus", "Aorta descendens", "V. azygos", "Truncus sympathicus"],
  """N. phrenicus perikard ile mediastinal plevra arasında, akciğer kökünün önünden geçer ve orta mediastende yer alır.
  Arka mediastende inen aorta, özofagus, vagus gövdeleri, ductus thoracicus, azigos sistemi ve sempatik gövdeler bulunur.""",
  e=["mediastinum", "n-phrenicus", "ductus-thoracicus"]),
]

write("respiratory", questions)
