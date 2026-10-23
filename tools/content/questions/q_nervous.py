from qcommon import Q, write

BE = "Beyin"
BS = "Beyin sapı ve beyincik"
OM = "Omurilik ve zarlar"
KS = "Kranial sinirler"
SS = "Spinal sinirler ve pleksuslar"
OT = "Otonom sinir sistemi"

questions = [
# ------------------------------------------------------------------ Beyin
Q("tv", BE, """Sağ elini kullanan 62 yaşındaki hasta inme sonrası ne söylendiğini anlıyor; ancak konuşması
kesik kesik, zorlanarak ve az sözcükle. Yazması da bozuk. Lezyon büyük olasılıkla nerededir?""",
  "Sol gyrus frontalis inferior (Broca alanı, BA 44–45)",
  ["Sol gyrus temporalis superior'un arka kısmı (Wernicke alanı)", "Sağ gyrus frontalis inferior",
   "Sol gyrus angularis", "Sol gyrus precentralis'in üst kısmı"],
  """Broca afazisi (motor/ekspresif afazi) baskın hemisferin inferior frontal girusunun pars opercularis ve
  triangularis'inin hasarıyla olur: konuşma akıcı değil, anlama görece korunmuş. Genellikle MCA üst
  dalının tıkanmasıyla görülür ve karşı tarafta yüz–kol güçsüzlüğü eşlik edebilir.""",
  ["Akıcı ama anlamsız konuşma ve anlama bozukluğu yapar.", "Baskın olmayan hemisfer; konuşmanın tonlamasını (prozodi) etkiler.",
   "Gerstmann sendromu yapar.", "Bacağın motor alanıdır."],
  e=["lobus-frontalis", "cerebrum"]),

Q("tv", BE, """İnme geçiren hasta akıcı ama anlamsız konuşuyor, uydurma sözcükler kullanıyor ve basit komutları
anlamıyor; hatasının farkında değil. Lezyon nerededir?""",
  "Sol gyrus temporalis superior'un arka kısmı (Wernicke alanı, BA 22)",
  ["Sol gyrus frontalis inferior", "Fasciculus arcuatus", "Sol lobus occipitalis", "Sağ gyrus temporalis superior"],
  """Wernicke (duyusal/reseptif) afazisinde konuşma akıcıdır ancak içerik bozuktur (parafazi, neolojizm);
  dili anlama ve tekrarlama bozulur. Lezyon baskın hemisferin süperior temporal girusunun arka bölümündedir.""",
  e=["lobus-temporalis", "cerebrum"]),

Q("t", BE, "Konuşmanın akıcı, anlamanın iyi olduğu ancak söyleneni tekrarlamanın belirgin bozuk olduğu afazi tipinde hasar nerededir?",
  "Fasciculus arcuatus",
  ["Corpus callosum", "Capsula interna'nın arka bacağı", "Gyrus precentralis", "Hippocampus"],
  """İletim (kondüksiyon) afazisi Wernicke ile Broca alanlarını bağlayan fasciculus arcuatus'un (çoğunlukla
  supramarjinal girus düzeyinde) hasarıyla oluşur. Anlama ve akıcılık korunur, tekrarlama bozulur.""",
  e=["cerebrum", "lobus-parietalis"]),

Q("tv", BE, """Hastada ani başlayan sol bacakta belirgin güçsüzlük ve his kaybı var; kol ve yüz görece
korunmuş. Tıkanan arter hangisidir?""",
  "Sağ a. cerebri anterior",
  ["Sağ a. cerebri media", "Sol a. cerebri anterior", "Sağ a. cerebri posterior", "Baziler arter"],
  """Bacak ve ayağın motor-duyusal temsil alanı hemisferin medial yüzündeki parasantral lobüldedir ve
  a. cerebri anterior tarafından beslenir. ACA tıkanmasında karşı tarafta bacak ağırlıklı tutulum olur.
  MCA tıkanması ise yüz ve kol ağırlıklıdır.""",
  e=["gyrus-precentralis", "circulus-arteriosus"]),

Q("tv", BE, """65 yaşında sağ elini kullanan hastada sağ yüz ve kolda belirgin güçsüzlük ve his kaybı ile
konuşma bozukluğu var; bacak daha hafif etkilenmiş. Tıkanan arter hangisidir?""",
  "Sol a. cerebri media",
  ["Sol a. cerebri anterior", "Sağ a. cerebri media", "Sol a. cerebri posterior", "Sol a. choroidea anterior"],
  """MCA hemisferin dış yüzünü, dolayısıyla yüz ve kolun motor-duyusal alanlarını ve baskın hemisferde
  dil alanlarını besler. Sol MCA tıkanması sağda yüz–kol ağırlıklı hemiparezi, hemihipoestezi ve afazi yapar.""",
  e=["gyrus-precentralis", "gyrus-postcentralis", "circulus-arteriosus"]),

Q("t", BE, "A. cerebri posterior tıkanmasında görülen tipik görme alanı defekti hangisidir?",
  "Karşı tarafta makula korunmalı homonim hemianopsi",
  ["Bitemporal hemianopsi", "Aynı tarafta tek gözde körlük", "Binazal hemianopsi", "Karşı tarafta üst kadranopsi"],
  """PCA oksipital lobu (primer görme korteksini) besler. Tıkanmasında karşı görme alanında homonim
  hemianopsi olur; makulanın temsil edildiği oksipital kutup MCA'dan da kollateral aldığı için merkezî
  görme çoğunlukla korunur.""",
  e=["lobus-occipitalis", "circulus-arteriosus"]),

Q("f", BE, "Primer görme korteksi (Brodmann 17) nerede yer alır?",
  "Lobus occipitalis'te sulcus calcarinus'un iki yanında",
  ["Gyrus temporalis superior'da", "Gyrus postcentralis'te", "Lobus frontalis'in alt yüzünde", "Corpus geniculatum laterale içinde"],
  """Primer görme korteksi oksipital lobun medial yüzünde, kalkarin oluğun üst (cuneus) ve alt (gyrus
  lingualis) dudaklarındadır. Üst dudak alt görme alanını, alt dudak üst görme alanını temsil eder.""",
  e=["lobus-occipitalis", "n-opticus"]),

Q("f", BE, "Primer işitme korteksi (Brodmann 41–42) nerededir?",
  "Gyri temporales transversi (Heschl girusları)",
  ["Gyrus angularis", "Gyrus cinguli", "Gyrus parahippocampalis", "Gyrus precentralis'in alt ucu"],
  """Primer işitme alanı lateral oluğun tabanında, süperior temporal girusun üst yüzündeki transvers temporal
  (Heschl) giruslardadır. Her kulaktan gelen bilgi iki taraflı temsil edildiğinden tek taraflı kortikal
  hasar sağırlık yapmaz.""",
  e=["lobus-temporalis", "n-vestibulocochlearis"]),

Q("f", BE, "Primer somatosensoriyel korteks hangi Brodmann alanlarına karşılık gelir?",
  "3, 1, 2 (gyrus postcentralis)",
  ["4 (gyrus precentralis)", "6 (premotor alan)", "17 (sulcus calcarinus)", "22 (gyrus temporalis superior)"],
  """Postsantral girus vücudun karşı yarısından gelen dokunma, ağrı, ısı ve propriosepsiyon bilgisini alır
  ve somatotopik düzenlidir (duyusal homunkulus). Bilgi talamusun VPL ve VPM çekirdeklerinden gelir.""",
  e=["gyrus-postcentralis", "lobus-parietalis"]),

Q("t", BE, "Agrafi, akalkuli, parmak agnozisi ve sağ–sol ayrımı bozukluğundan oluşan Gerstmann sendromunda lezyon nerededir?",
  "Baskın hemisferin gyrus angularis'i",
  ["Baskın olmayan hemisferin lobus parietalis superior'u", "Baskın hemisferin gyrus frontalis inferior'u",
   "Corpus callosum'un splenium'u", "Baskın hemisferin hippocampus'u"],
  """Gerstmann sendromu baskın (genellikle sol) parietal lobun alt kısmında, angular girus lezyonlarında
  görülür. Baskın olmayan parietal lob hasarı ise karşı tarafı ihmal (hemineglect) ve apraksiler yapar.""",
  e=["lobus-parietalis"]),

Q("tv", BE, """Sağ hemisfer inmesi geçiren hasta yemeğinin yalnızca sağ yarısını yiyor, sol tarafındaki kişileri
fark etmiyor ve sol kolunun kendisine ait olmadığını söylüyor. Lezyon hangi lobdadır?""",
  "Sağ lobus parietalis",
  ["Sol lobus parietalis", "Sağ lobus occipitalis", "Sağ lobus frontalis", "Sol lobus temporalis"],
  """Karşı tarafın ihmali (hemispatial neglect) ve anozognozi en sık baskın olmayan (sağ) parietal lob
  lezyonlarında görülür; çünkü sağ hemisfer uzayın her iki yarısına, sol hemisfer ise ağırlıklı olarak
  sağ yarısına dikkat eder.""",
  e=["lobus-parietalis"]),

Q("f", BE, "Kişilik değişikliği, uygunsuz davranış, planlama ve yargılama bozukluğu en çok hangi bölgenin hasarında görülür?",
  "Prefrontal korteks",
  ["Lobus occipitalis", "Cerebellum'un vermis'i", "Gyrus postcentralis", "Corpus geniculatum mediale"],
  """Prefrontal korteks yürütücü işlevlerden, sosyal davranıştan ve kişilikten sorumludur. Frontal lob
  hasarlı hastalar apati veya dürtüsellik, perseverasyon ve sosyal uygunsuzluk gösterebilir.""",
  e=["lobus-frontalis"]),

Q("f", BE, "Tat duyusunun kortikal merkezi olarak kabul edilen ve viseral duyularla ilgili lob hangisidir?",
  "Insula (ve komşu frontal operkulum)",
  ["Lobus occipitalis", "Gyrus cinguli", "Gyrus precentralis", "Cuneus"],
  """Insula lateral oluğun derininde, operkulumların altında saklı kalan loptur. Ön kısmı primer tat
  korteksini içerir; ayrıca ağrı, iç organ duyuları ve otonom yanıtlarla ilişkilidir. MCA dallarıyla beslenir.""",
  e=["insula"]),

Q("f", BE, "Yeni bilgilerin uzun süreli belleğe aktarılmasında kritik rol oynayan ve Alzheimer hastalığında erken atrofiye uğrayan yapı hangisidir?",
  "Hippocampus",
  ["Corpus amygdaloideum", "Nucleus caudatus", "Thalamus'un pulvinar'ı", "Cerebellum"],
  """Hippocampus temporal lobun medialinde, lateral ventrikülün alt boynuzunun tabanındadır. İki taraflı
  hasarında anterograd amnezi olur. Papez devresinin parçasıdır: hippocampus → fornix → corpus
  mamillare → anterior talamus → gyrus cinguli → hippocampus.""",
  e=["hippocampus", "systema-limbicum"]),

Q("t", BE, "İki taraflı amigdala hasarına bağlı Klüver–Bucy sendromunda aşağıdakilerden hangisi beklenmez?",
  "Aşırı korku ve saldırganlık",
  ["Hiperoralite (her şeyi ağzına götürme)", "Hiperseksüalite", "Uysallık, korkunun kaybı", "Görsel agnozi"],
  """Amigdala korku ve duygusal öğrenmenin merkezidir. İki taraflı medial temporal hasarda korku ve
  saldırganlık azalır, hasta uysallaşır; hiperoralite, hiperseksüalite ve görsel agnozi görülür.""",
  e=["corpus-amygdaloideum", "systema-limbicum"]),

Q("f", BE, "İki serebral hemisferi birbirine bağlayan en büyük komissür hangisidir?",
  "Corpus callosum",
  ["Commissura anterior", "Fornix", "Capsula interna", "Commissura posterior"],
  """Corpus callosum yaklaşık 200 milyon akson içeren beyaz cevher köprüsüdür; rostrum, genu, gövde ve
  splenium bölümleri vardır. Kesilmesinde ('split-brain') iki hemisfer arasındaki bilgi aktarımı bozulur.""",
  e=["corpus-callosum"]),

Q("tv", BE, """Hipertansif hastada ani başlayan, karşı tarafta yüz, kol ve bacağı eşit tutan saf motor
hemiparezi var; duyu, görme ve konuşma normal. Lakün enfarktı en olası nerededir?""",
  "Capsula interna'nın arka bacağı",
  ["Gyrus postcentralis", "Lobus occipitalis", "Cerebellum'un hemisferi", "Corpus callosum'un genu'su"],
  """Kortikospinal ve kortikobulber lifler capsula interna'nın arka bacağında birbirine çok yakın seyreder;
  küçük bir enfarkt bile karşı tarafta yüz–kol–bacağı eşit tutar. Bu bölge MCA'nın lentikülostriat
  dallarıyla beslenir; bu dallar hipertansiyonda hasara açıktır.""",
  e=["nuclei-basales", "cerebrum"]),

Q("t", BE, "Parkinson hastalığında dejenere olan dopaminerjik nöronlar nerededir?",
  "Substantia nigra'nın pars compacta'sı (mesencephalon)",
  ["Nucleus caudatus", "Nucleus subthalamicus", "Globus pallidus internus", "Nucleus ruber"],
  """Substantia nigra pars compacta'daki dopaminerjik nöronlar striatuma (nigrostriatal yol) uzanır.
  Kayıplarında bradikinezi, rijidite ve istirahat tremoru gelişir. Huntington'da nucleus caudatus atrofisi,
  hemiballismusta nucleus subthalamicus lezyonu görülür.""",
  e=["mesencephalon", "nuclei-basales"]),

Q("tv", BE, """Hipertansif hastada aniden sol kol ve bacağında şiddetli, savurucu, istemsiz hareketler başlıyor.
Lezyon nerededir?""",
  "Sağ nucleus subthalamicus",
  ["Sol nucleus subthalamicus", "Sağ nucleus caudatus", "Sağ substantia nigra", "Sol cerebellum hemisferi"],
  """Hemiballismus karşı taraftaki nucleus subthalamicus lezyonunda görülür; bu çekirdek normalde
  globus pallidus internus'u uyararak hareketi frenler. Bazal ganglion lezyonları karşı tarafta bulgu verir.""",
  e=["nuclei-basales"]),

Q("t", BE, "Görme yolunda bulunan talamus çekirdeği hangisidir?",
  "Corpus geniculatum laterale",
  ["Corpus geniculatum mediale", "Nucleus ventralis posterolateralis", "Nucleus anterior thalami", "Nucleus ventralis lateralis"],
  """Optik trakt lifleri LGN'de sinaps yapar; buradan optik radyasyon oksipital kortekse gider. MGN işitme,
  VPL vücut duyusu, VPM yüz duyusu ve tat, VL serebellum ve bazal ganglionlardan gelen motor bilgi,
  anterior çekirdek ise Papez devresi ile ilgilidir.""",
  e=["thalamus", "n-opticus"]),

Q("t", BE, "Yüzden gelen duyuları (n. trigeminus) ve tat liflerini kortekse ileten talamus çekirdeği hangisidir?",
  "Nucleus ventralis posteromedialis (VPM)",
  ["Nucleus ventralis posterolateralis (VPL)", "Pulvinar", "Nucleus medialis dorsalis", "Corpus geniculatum mediale"],
  """Trigeminal lemniskus ve solitar çekirdekten gelen tat lifleri VPM'de, vücuttan gelen medial lemniskus
  ve spinotalamik lifler VPL'de sonlanır. Talamus lezyonlarında karşı tarafta hemianestezi ve talamik
  ağrı (Dejerine–Roussy) görülebilir.""",
  e=["thalamus", "n-trigeminus"]),

Q("t", BE, "Antidiüretik hormonu (ADH) başlıca sentezleyen hipotalamus çekirdeği hangisidir?",
  "Nucleus supraopticus",
  ["Nucleus suprachiasmaticus", "Nucleus arcuatus", "Nucleus ventromedialis", "Corpus mamillare"],
  """ADH en çok supraoptik, oksitosin en çok paraventriküler çekirdekte yapılır; ikisi de aksonlarla
  neurohypophysis'e taşınır. Suprakiazmatik çekirdek sirkadiyen ritmi, ventromedial çekirdek tokluğu,
  lateral hipotalamus açlığı düzenler.""",
  e=["hypothalamus", "hypophysis"]),

Q("t", BE, "Wernicke–Korsakoff sendromunda (tiamin eksikliği) karakteristik olarak hasar gören hipotalamik yapı hangisidir?",
  "Corpora mamillaria",
  ["Nucleus suprachiasmaticus", "Eminentia mediana", "Nucleus paraventricularis", "Tuber cinereum"],
  """Kronik alkolizm ve tiamin eksikliğinde mamiller cisimler, talamusun medial çekirdekleri ve periakuaduktal
  gri cevherde hasar olur. Papez devresinin bozulması Korsakoff amnezisini ve konfabülasyonu açıklar.""",
  e=["hypothalamus", "systema-limbicum"]),

Q("tv", BE, """Yenidoğanda baş çevresi hızla büyüyor. MR'da lateral ventriküller ve 3. ventrikül genişlemiş,
4. ventrikül normal boyutta. Tıkanıklık en olası nerededir?""",
  "Aqueductus mesencephali (Sylvius kanalı)",
  ["Foramen interventriculare (Monro)", "Apertura mediana (Magendie)", "Granulationes arachnoideae", "Canalis centralis"],
  """BOS lateral ventriküllerden Monro deliği ile 3. ventriküle, Sylvius kanalı ile 4. ventriküle, oradan
  Magendie ve Luschka delikleriyle subaraknoid aralığa geçer. 4. ventrikül normalken 3. ventrikül genişse
  tıkanıklık aqueductus'tadır (konjenital akuadukt stenozu).""",
  e=["ventriculi-cerebri", "mesencephalon"]),

Q("f", BE, "Beyin-omurilik sıvısı (BOS) başlıca nerede üretilir ve nerede emilir?",
  "Plexus choroideus'ta üretilir, granulationes arachnoideae ile dural venöz sinüslere emilir.",
  ["Granulationes arachnoideae'de üretilir, plexus choroideus'ta emilir.", "Ependim hücrelerinde üretilir, lenf damarlarına emilir.",
   "Pia mater'de üretilir, canalis centralis'te emilir.", "Plexus choroideus'ta üretilir, 4. ventrikülde emilir."],
  """Erişkinde günde yaklaşık 500 ml BOS üretilir; herhangi bir anda yaklaşık 150 ml bulunur. Emilim
  çoğunlukla sinus sagittalis superior'a uzanan araknoid granülasyonlarla olur. Emilim bozukluğu iletişimli
  hidrosefaliye yol açar.""",
  e=["ventriculi-cerebri", "meninges", "sinus-durae-matris"]),

# ------------------------------------------------------------------ Beyin sapı ve beyincik
Q("tv", BS, """Hastada sağ gözde pitozis, midriyazis ve gözün aşağı-dışa kayması ile birlikte sol kol ve bacakta
güçsüzlük var. Lezyon en olası nerededir?""",
  "Sağ mesencephalon'un ventral kısmı (Weber sendromu)",
  ["Sol mesencephalon'un ventral kısmı", "Sağ pons'un ventral kısmı", "Sol medulla oblongata'nın medial kısmı", "Sağ capsula interna"],
  """Weber sendromunda orta beynin ventralinde n. oculomotorius lifleri ve pedunculus cerebri birlikte
  tutulur: aynı tarafta III felci, karşı tarafta hemiparezi. Kortikospinal lifler medullada çaprazlaştığı
  için beyin sapı lezyonları 'çapraz' bulgu verir.""",
  e=["mesencephalon", "n-oculomotorius"]),

Q("tv", BS, """Ani baş dönmesi ve bulantıyla başvuran hastada sol yüzde ve sağ gövde–ekstremitelerde ağrı ve ısı
duyusu kaybı, ses kısıklığı, yutma güçlüğü, solda Horner sendromu ve sol tarafta ataksi var. Dil
hareketleri normal. Tıkanan arter hangisidir?""",
  "Sol a. cerebelli inferior posterior (veya sol a. vertebralis)",
  ["Sol a. spinalis anterior", "Baziler arter", "Sol a. cerebelli superior", "Sağ a. cerebri posterior"],
  """Lateral medüller (Wallenberg) sendromda spinal trigeminal çekirdek (aynı taraf yüz), spinotalamik yol
  (karşı taraf gövde), nucleus ambiguus (disfaji, disfoni), inen sempatik lifler (Horner), vestibüler
  çekirdekler ve alt serebellar pedinkül tutulur. Medial yerleşimli XII çekirdeği korunur.""",
  e=["medulla-oblongata", "a-vertebralis", "n-vagus"]),

Q("t", BS, "Medial medüller sendromda (a. spinalis anterior tıkanması) aşağıdaki bulgulardan hangisi beklenmez?",
  "Aynı tarafta yüzde ağrı ve ısı duyusu kaybı",
  ["Karşı tarafta hemiparezi", "Karşı tarafta propriosepsiyon ve vibrasyon kaybı",
   "Dilin dışarı çıkarılınca lezyon tarafına sapması", "Aynı tarafta dil kaslarında atrofi"],
  """Medial medulla piramidi (karşı hemiparezi), medial lemniskusu (karşı derin duyu kaybı) ve
  n. hypoglossus'u (aynı taraf dil felci) içerir. Spinal trigeminal çekirdek lateral medulladadır ve
  Wallenberg sendromunda etkilenir.""",
  e=["medulla-oblongata", "n-hypoglossus"]),

Q("f", BS, "Aşağıdaki kranial sinirlerden hangisinin motor çekirdeği pons'ta bulunur?",
  "N. abducens",
  ["N. oculomotorius", "N. trochlearis", "N. glossopharyngeus", "N. hypoglossus"],
  """III ve IV mesensefalonda; V (motor), VI ve VII ponsta; IX, X ve XII medullada çekirdeğe sahiptir.
  VIII'in çekirdekleri ponto-medüller bileşkededir.""",
  e=["pons", "n-abducens"]),

Q("t", BS, "4. ventrikülün tabanındaki colliculus facialis'i oluşturan yapılar hangileridir?",
  "N. abducens çekirdeği ve onu dolanan n. facialis lifleri",
  ["N. hypoglossus çekirdeği ve n. vagus'un dorsal çekirdeği", "N. trochlearis lifleri ve nucleus ruber",
   "Vestibüler çekirdekler ve n. cochlearis lifleri", "Locus coeruleus ve nucleus solitarius"],
  """Fasiyal motor lifler pons içinde abducens çekirdeğinin etrafını dolanarak iç dizi (genu internum)
  yapar ve 4. ventrikül tabanında kabarıklık oluşturur. Bu bölgedeki lezyon aynı tarafta VI ve VII felcini
  birlikte yapar.""",
  e=["pons", "n-facialis", "n-abducens"]),

Q("tv", BS, """Hasta ayakta dururken ve yürürken iki yana savruluyor, ayaklarını açarak yürüyor; ancak oturup
kollarını kullanırken belirgin dismetri yok. Lezyon en olası nerededir?""",
  "Vermis cerebelli",
  ["Sağ serebellar hemisfer", "Sol serebellar hemisfer", "Nucleus dentatus", "Capsula interna"],
  """Vermis ve paravermal bölge gövde ve aksiyal kasların koordinasyonunu sağlar; lezyonunda gövde ataksisi
  ve geniş tabanlı yürüyüş olur (ör. alkol). Hemisfer lezyonları aynı taraf ekstremitede dismetri,
  intansiyonel tremor ve disdiadokokinezi yapar.""",
  e=["cerebellum"]),

Q("t", BS, "Pons çekirdeklerinden serebellum'a giden (pontoserebellar) lifleri taşıyan yapı hangisidir?",
  "Pedunculus cerebellaris medius",
  ["Pedunculus cerebellaris superior", "Pedunculus cerebellaris inferior", "Velum medullare superius", "Lemniscus medialis"],
  """Orta serebellar pedinkül (brachium pontis) en büyük pedinküldür ve tamamen pontoserebellar (afferent)
  liflerden oluşur. Üst pedinkül esas olarak serebellumdan çıkan (efferent) lifleri, alt pedinkül ise
  omurilik ve olivadan gelen lifleri taşır.""",
  e=["cerebellum", "pons"]),

Q("t", BS, "Serebellar korteksin tek çıkış nöronu olan ve inhibitör (GABAerjik) yapıdaki hücre hangisidir?",
  "Purkinje hücresi",
  ["Granül hücresi", "Golgi hücresi", "Sepet hücresi", "Yosunsu lif"],
  """Purkinje hücrelerinin aksonları derin serebellar çekirdeklere (dentatus, emboliformis, globosus,
  fastigii) ve vestibüler çekirdeklere giderek onları inhibe eder. Serebellumdan asıl çıkışı derin
  çekirdekler, en büyüğü nucleus dentatus, sağlar.""",
  e=["cerebellum"]),

Q("f", BS, "Kortikospinal liflerin büyük kısmı nerede çaprazlaşır?",
  "Medulla oblongata'nın alt ucunda (decussatio pyramidum)",
  ["Pons'ta", "Mesencephalon'da", "Capsula interna'da", "Omuriliğin her segmentinde"],
  """Kortikospinal liflerin yaklaşık %85–90'ı piramidlerin alt ucunda çaprazlaşarak lateral kortikospinal
  yolu oluşturur. Çaprazlaşmayan lifler ön kortikospinal yolda iner ve segmental düzeyde karşıya geçer.""",
  e=["medulla-oblongata", "tractus-spinales"]),

Q("tv", BS, """Baziler arter trombozu sonrası hasta tamamen bilinçli; ancak kollarını, bacaklarını, yüzünü
hareket ettiremiyor ve konuşamıyor. Yalnızca gözlerini yukarı-aşağı hareket ettirip kırpabiliyor. Bu
tablo hangisidir?""",
  "Kilitlenme (locked-in) sendromu – ventral pons lezyonu",
  ["Koma – retiküler aktive edici sistem lezyonu", "Akinetik mutizm – frontal lob lezyonu",
   "Weber sendromu – orta beyin lezyonu", "Wallenberg sendromu – lateral medulla lezyonu"],
  """Ventral pons lezyonunda kortikospinal ve kortikobulber yollar kesilir; dorsal ponstaki retiküler
  formasyon korunduğundan bilinç yerindedir. Dikey göz hareketleri ve göz kırpma orta beyin tarafından
  kontrol edildiği için korunur.""",
  e=["pons", "a-vertebralis"]),

Q("f", BS, "Mesencephalon'da bulunan ve serebellumdan gelen lifleri alan kırmızı renkli çekirdek hangisidir?",
  "Nucleus ruber",
  ["Substantia nigra", "Locus coeruleus", "Nucleus olivaris inferior", "Nucleus dentatus"],
  """Nucleus ruber üst serebellar pedinkülden lif alır ve rubrospinal yol ile üst ekstremite fleksörlerini
  etkiler. Zengin kanlanması ve demir içeriği nedeniyle taze kesitte pembemsi görünür.""",
  e=["mesencephalon", "cerebellum"]),

# ------------------------------------------------------------------ Omurilik ve zarlar
Q("f", OM, "Erişkinde omuriliğin alt ucu (conus medullaris) genellikle hangi düzeyde sonlanır?",
  "L1–L2",
  ["T10–T11", "L3–L4", "L5–S1", "S2"],
  """Gelişim sırasında omurga omurilikten hızlı büyüdüğü için erişkinde conus medullaris L1–L2 düzeyindedir
  (yenidoğanda yaklaşık L3). Altında cauda equina ve filum terminale bulunur. Dura kesesi S2 düzeyinde sonlanır.""",
  e=["medulla-spinalis", "cauda-equina"]),

Q("fv", OM, "Erişkinde lomber ponksiyon için en uygun ve güvenli aralık hangisidir?",
  "L3–L4 veya L4–L5 aralığı",
  ["T12–L1 aralığı", "L1–L2 aralığı", "S2–S3 aralığı", "T10–T11 aralığı"],
  """İki crista iliaca'nın en yüksek noktalarını birleştiren çizgi (Tuffier çizgisi) yaklaşık L4 dikensi
  çıkıntısından geçer. Omurilik L1–L2'de bittiğinden L3–L4 veya L4–L5'ten girilen iğne yalnızca cauda equina
  köklerini iter.""",
  e=["medulla-spinalis", "cauda-equina", "vertebrae-lumbales"]),

Q("t", OM, "Lomber ponksiyonda iğnenin epidural aralığa girmeden önce geçtiği son bağ hangisidir?",
  "Lig. flavum",
  ["Lig. supraspinale", "Lig. interspinale", "Lig. longitudinale posterius", "Lig. denticulatum"],
  """İğne sırasıyla deri, deri altı, lig. supraspinale, lig. interspinale ve lig. flavum'u geçerek epidural
  aralığa, ardından dura ve araknoidi geçerek subaraknoid aralığa ulaşır. Lig. flavum'da direnç kaybı
  epidural anestezide yol göstericidir.""",
  e=["ligg-columnae", "meninges"]),

Q("tv", OM, """Sırtından bıçaklanan hastada sağda T10 altında motor felç ve derin duyu (vibrasyon,
pozisyon) kaybı, solda ise yaklaşık T12 altından başlayan ağrı ve ısı duyusu kaybı var. Lezyon hangisidir?""",
  "Omuriliğin sağ yarısının kesisi (Brown-Séquard sendromu)",
  ["Omuriliğin sol yarısının kesisi", "Ön spinal arter sendromu", "Santral kord sendromu", "Arka kord sendromu"],
  """Hemiseksiyonda aynı tarafta kortikospinal yol (motor felç) ve dorsal kolon (derin duyu) tutulur. Ağrı ve
  ısı lifleri girdikleri segmentin 1–2 üstünde karşıya geçtiği için karşı tarafta, lezyonun birkaç
  segment altından başlayan ağrı-ısı kaybı olur.""",
  e=["medulla-spinalis", "tractus-spinales"]),

Q("f", OM, "Alt ekstremiteden gelen ince dokunma ve propriosepsiyon bilgisini taşıyan yol hangisidir?",
  "Fasciculus gracilis",
  ["Fasciculus cuneatus", "Tractus spinothalamicus lateralis", "Tractus spinocerebellaris anterior", "Tractus corticospinalis lateralis"],
  """Dorsal kolonlarda medial yerleşimli fasciculus gracilis alt gövde ve bacaktan, lateral yerleşimli
  fasciculus cuneatus (T6 üzeri) üst gövde ve koldan bilgi taşır. Lifler aynı tarafta yükselir ve
  medullada (nucleus gracilis/cuneatus) sinaps yapıp çaprazlaşarak medial lemniskusu oluşturur.""",
  e=["tractus-spinales", "medulla-spinalis"]),

Q("tv", OM, """Ellerini sıcak sobaya yaktığı hâlde fark etmeyen hastada her iki omuz ve kolda 'pelerin'
tarzında ağrı ve ısı duyusu kaybı var; dokunma ve pozisyon duyusu korunmuş. En olası tanı hangisidir?""",
  "Servikal siringomiyeli",
  ["Tabes dorsalis", "Brown-Séquard sendromu", "B12 eksikliğine bağlı subakut kombine dejenerasyon", "Ön spinal arter tıkanması"],
  """Siringomiyelide santral kanal genişler ve ilk olarak commissura alba anterior'da çaprazlaşan spinotalamik
  lifler etkilenir; bu nedenle ilgili segmentlerde iki taraflı, 'pelerin' biçiminde ağrı-ısı kaybı olur.
  Dorsal kolonlar korunur (disosiye duyu kaybı).""",
  e=["medulla-spinalis", "tractus-spinales"]),

Q("t", OM, "Ön spinal arter tıkanmasında aşağıdakilerden hangisi genellikle korunur?",
  "Vibrasyon ve pozisyon duyusu",
  ["Lezyon altında motor güç", "Ağrı ve ısı duyusu", "İdrar ve gaita kontrolü", "Lezyon düzeyindeki alt motor nöron işlevleri"],
  """A. spinalis anterior omuriliğin ön üçte ikisini besler: ön boynuzlar, kortikospinal ve spinotalamik yollar
  etkilenir. Dorsal kolonlar arka spinal arterlerden beslendiği için vibrasyon ve propriosepsiyon korunur.""",
  e=["medulla-spinalis", "tractus-spinales"]),

Q("t", OM, "B12 vitamini eksikliğine bağlı subakut kombine dejenerasyonda tutulan yollar hangileridir?",
  "Dorsal kolonlar ve lateral kortikospinal yollar",
  ["Spinotalamik yollar ve ön boynuzlar", "Yalnızca ön boynuz motor nöronları", "Spinoserebellar yollar ve arka kökler",
   "Commissura alba anterior ve lateral boynuzlar"],
  """B12 eksikliğinde miyelin sentezi bozulur ve özellikle dorsal kolonlar (derin duyu kaybı, ataksi) ile
  lateral kortikospinal yollar (spastisite, Babinski) birlikte etkilenir.""",
  e=["tractus-spinales", "medulla-spinalis"]),

Q("tv", OM, """Başına beyzbol sopasıyla vurulan genç kısa süre bayılıp kendine geliyor, saatler sonra bilinci
bozuluyor. BT'de suturaları aşmayan bikonveks (mercek biçimli) kanama görülüyor. Kanama hangi
aralıktadır ve kaynağı nedir?""",
  "Epidural aralık – a. meningea media",
  ["Subdural aralık – köprü venler", "Subaraknoid aralık – anevrizma", "Epidural aralık – sinus sagittalis superior",
   "Beyin parankimi – lentikülostriat arterler"],
  """Epidural hematom kafatası ile dura arasında, genellikle arteriyel kanamayla oluşur; dura suturalara sıkı
  yapıştığı için kanama suturaları aşmaz ve mercek biçimlidir. Subdural hematom köprü venlerin yırtılmasıyla
  oluşur, hilal biçimlidir ve suturaları aşar; yaşlılarda ve alkoliklerde sıktır.""",
  e=["meninges", "os-temporale"]),

Q("fv", OM, "Hayatının en şiddetli baş ağrısıyla başvuran hastada BOS kanlı ve ksantokromik. En sık neden hangisidir?",
  "Circulus arteriosus cerebri'deki sakküler (berry) anevrizmanın yırtılması",
  ["Köprü venlerin yırtılması", "A. meningea media'nın yırtılması", "Sinus cavernosus trombozu", "Plexus choroideus kanaması"],
  """Travmatik olmayan subaraknoid kanamanın en sık nedeni Willis poligonu çevresindeki anevrizmalardır;
  en sık ön komünikan arter bileşkesinde görülür. Kan subaraknoid aralıkta BOS ile karışır.""",
  e=["meninges", "circulus-arteriosus"]),

Q("f", OM, "Omuriliği her iki yanda dura mater'e bağlayan, pia mater'in dişli uzantıları hangisidir?",
  "Ligg. denticulata",
  ["Filum terminale", "Lig. flavum", "Septum cervicale intermedium", "Lig. coccygeum"],
  """Pia mater her yanda yaklaşık 21 dişli uzantı (lig. denticulatum) yapar; bunlar araknoidi delip duraya
  tutunur ve omuriliği dura kesesi içinde asılı tutar. Filum terminale ise conus medullaris'ten koksikse uzanır.""",
  e=["meninges", "medulla-spinalis"]),

Q("t", OM, "Omurga kanalındaki epidural aralık için aşağıdakilerden hangisi doğrudur?",
  "Yağ dokusu ve plexus venosus vertebralis internus içerir.",
  ["BOS ile doludur.", "Kafatası içindeki epidural aralıkla serbestçe devamlıdır.",
   "Pia mater ile araknoid arasındadır.", "Omurilik ile birlikte L1'de sonlanır."],
  """Spinal epidural aralık dura ile omur kanalının periostu arasındadır ve yağ ile kapaksız iç vertebral
  venöz pleksusu (Batson) içerir. Kafatasında dura periosta yapışık olduğu için normalde epidural aralık
  yoktur; aralık foramen magnum'da sona erer. Bu venler pelvis ve meme kanserlerinin omurgaya yayılmasına
  aracılık eder.""",
  e=["meninges", "ligg-columnae"]),

Q("fv", OM, """Masif lomber disk hernisi olan hastada perine ve iç uyluklarda 'eyer' tarzında his kaybı, idrar
retansiyonu ve anal sfinkter tonusunda azalma var. Bu acil durum hangisidir?""",
  "Cauda equina sendromu",
  ["Conus medullaris'in tek taraflı basısı", "Brown-Séquard sendromu", "Piriformis sendromu", "Meralgia paresthetica"],
  """L1–L2 altındaki sinir kökleri (cauda equina) sıkışınca sakral köklerin innerve ettiği perine derisi,
  mesane ve anal sfinkter etkilenir. Acil cerrahi dekompresyon gerektirir.""",
  e=["cauda-equina", "discus-intervertebralis"]),

# ------------------------------------------------------------------ Kranial sinirler
Q("t", KS, "Duyusal bilgisini kortekse ulaştırmadan önce talamusta sinaps yapmayan tek duyu hangisidir?",
  "Koku",
  ["Görme", "İşitme", "Tat", "Dokunma"],
  """Koku lifleri bulbus olfactorius'ta sinaps yapar; tractus olfactorius doğrudan piriform korteks ve
  amigdala gibi alanlara uzanır. Diğer duyular kortekse ulaşmadan önce talamusta aktarılır.""",
  e=["n-olfactorius", "organum-olfactus"]),

Q("fv", KS, """Baş ağrısı ve görme bozukluğu olan hastada her iki gözün dış (temporal) görme alanlarında
kayıp var. Hipofiz adenomu düşünülüyor. Bası yapılan yapı hangisidir?""",
  "Chiasma opticum",
  ["Tractus opticus", "N. opticus", "Radiatio optica", "Corpus geniculatum laterale"],
  """Optik kiazmada her iki retinanın nazal yarısından gelen lifler çaprazlaşır; bu lifler temporal görme
  alanlarını taşır. Aşağıdan gelen hipofiz tümörü bu lifleri sıkıştırarak bitemporal hemianopsi yapar.""",
  e=["n-opticus", "hypophysis"]),

Q("t", KS, "Sağ tractus opticus lezyonunda görülen görme alanı defekti hangisidir?",
  "Sol homonim hemianopsi",
  ["Sağ homonim hemianopsi", "Bitemporal hemianopsi", "Sağ gözde tam körlük", "Sol üst kadranopsi"],
  """Kiazmanın gerisindeki tüm lezyonlar karşı görme alanında homonim defekt yapar. Sağ optik trakt sağ
  gözün temporal ve sol gözün nazal retinasından, yani sol görme alanından lif taşır.""",
  e=["n-opticus"]),

Q("t", KS, "Temporal lobdan geçen optik radyasyon liflerinin (Meyer kulpu) hasarında hangi defekt beklenir?",
  "Karşı tarafta üst kadran homonim kadranopsi",
  ["Karşı tarafta alt kadran homonim kadranopsi", "Aynı tarafta üst kadranopsi", "Bitemporal hemianopsi", "Makula korunmalı tam hemianopsi"],
  """Optik radyasyonun alt lifleri (retinanın alt yarısından, üst görme alanını taşır) temporal lobda Meyer
  kulpunu yapar; hasarı karşı tarafta üst kadranopsiye ('gökyüzünde turta') yol açar. Parietal lob
  lezyonları ise alt kadranı etkiler.""",
  e=["n-opticus", "lobus-temporalis"]),

Q("tv", KS, """Ani başlayan şiddetli baş ağrısıyla gelen hastada sağ gözde pitozis, sabit dilate pupil ve gözün
aşağı-dışa kayması var. Bu tabloya en sık yol açan anevrizma hangi arterdedir?""",
  "A. communicans posterior",
  ["A. communicans anterior", "A. cerebri media", "A. basilaris'in ucu", "A. ophthalmica"],
  """N. oculomotorius PCom'un hemen yanından geçer. Parasempatik pupil lifleri sinirin yüzeyinde
  seyrettiğinden dıştan bası (anevrizma) erken dönemde pupillayı tutar. Diyabetik (iskemik) III felcinde
  ise sinirin içi etkilendiği için pupil genellikle korunur.""",
  e=["n-oculomotorius", "circulus-arteriosus"]),

Q("f", KS, "N. trigeminus'un üç dalı ve kafatasından çıktıkları açıklıklar hangisinde doğru eşleştirilmiştir?",
  "V1 – fissura orbitalis superior, V2 – foramen rotundum, V3 – foramen ovale",
  ["V1 – foramen rotundum, V2 – foramen ovale, V3 – foramen spinosum",
   "V1 – canalis opticus, V2 – fissura orbitalis inferior, V3 – foramen ovale",
   "V1 – fissura orbitalis superior, V2 – foramen ovale, V3 – foramen rotundum",
   "V1 – foramen ovale, V2 – foramen rotundum, V3 – fissura orbitalis superior"],
  """N. ophthalmicus fissura orbitalis superior'dan orbitaya, n. maxillaris foramen rotundum'dan fossa
  pterygopalatina'ya, n. mandibularis foramen ovale'den fossa infratemporalis'e geçer. Yalnızca V3 motor
  lif içerir.""",
  e=["n-trigeminus", "os-sphenoidale"]),

Q("t", KS, "Aşağıdaki kaslardan hangisi n. mandibularis (V3) tarafından innerve edilmez?",
  "M. stapedius",
  ["M. tensor tympani", "M. tensor veli palatini", "M. mylohyoideus", "M. digastricus venter anterior"],
  """V3 birinci faringeal ark kaslarını innerve eder: çiğneme kasları, tensor tympani, tensor veli palatini,
  mylohyoideus ve digastrik ön karın. M. stapedius ikinci ark kasıdır ve n. facialis ile innerve edilir;
  felcinde hiperakuzi olur.""",
  e=["n-trigeminus", "n-facialis", "auris-media"]),

Q("f", KS, "Kornea refleksinin afferent ve efferent kolları hangi sinirlerdir?",
  "Afferent: n. ophthalmicus (V1) – Efferent: n. facialis (VII)",
  ["Afferent: n. opticus (II) – Efferent: n. oculomotorius (III)", "Afferent: n. facialis – Efferent: n. trigeminus",
   "Afferent: n. maxillaris (V2) – Efferent: n. oculomotorius", "Afferent: n. ophthalmicus – Efferent: n. oculomotorius"],
  """Korneaya dokunulması n. nasociliaris (V1) ile algılanır; yanıt olarak her iki gözde m. orbicularis oculi
  (VII) kasılır. Işık refleksinde ise afferent II, efferent III'tür.""",
  e=["n-trigeminus", "n-facialis", "cornea"]),

Q("tv", KS, """Kulak arkasında ağrıyla başlayan yüz felci olan hastada aynı tarafta alın kırıştırılamıyor ve göz
kapanamıyor; ancak tat duyusu, gözyaşı salgısı ve işitme normal. Lezyon nerededir?""",
  "Foramen stylomastoideum düzeyinde veya distalinde",
  ["Meatus acusticus internus'ta", "Ganglion geniculi düzeyinde", "Pons'taki fasiyal çekirdekte",
   "Chorda tympani ayrıldıktan hemen önce"],
  """N. facialis fasiyal kanalda sırasıyla n. petrosus major'u (gözyaşı bezi), stapedius sinirini ve chorda
  tympani'yi (dilin ön 2/3'ü tadı) verir. Yalnızca mimik kaslar tutulmuşsa lezyon bu dalların tümü
  ayrıldıktan sonradır, yani stilomastoid delik veya parotis düzeyindedir.""",
  e=["n-facialis", "os-temporale"]),

Q("f", KS, "N. facialis'in parotis bezi içinde ayrıldığı uç dallar hangisinde doğru verilmiştir?",
  "Temporal, zigomatik, bukkal, marjinal mandibular ve servikal dallar",
  ["Oftalmik, maksiller, mandibular, bukkal ve servikal dallar", "Auriküler, temporal, lingual, bukkal ve mental dallar",
   "Temporal, infraorbital, bukkal, mental ve servikal dallar", "Frontal, zigomatik, lingual, mandibular ve servikal dallar"],
  """N. facialis stilomastoid delikten çıktıktan sonra parotisin içinde pes anserinus'u yapar ve beş uç
  dala ayrılır. Parotis cerrahisinde bu dalları korumak temel önceliktir; sinir bezi innerve etmez.""",
  e=["n-facialis", "glandula-parotidea"]),

Q("tv", KS, """Tek taraflı ilerleyici işitme kaybı ve kulak çınlaması olan hastada aynı tarafta korneal
refleks azalmış. MR'da serebellopontin açıda kitle var. En olası tanı hangisidir?""",
  "Vestibüler schwannom (akustik nörinom)",
  ["Menenjiyom (olfaktör oluk)", "Glomus jugulare tümörü", "Hipofiz adenomu", "Kraniyofarenjiyom"],
  """Vestibüler schwannom n. vestibulocochlearis'in vestibüler bölümünün Schwann hücrelerinden gelişir,
  meatus acusticus internus'ta büyüyüp serebellopontin açıya taşar. Büyüdükçe n. trigeminus (korneal refleks)
  ve n. facialis'e bası yapabilir.""",
  e=["n-vestibulocochlearis", "pons", "cerebellum"]),

Q("t", KS, "N. glossopharyngeus ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Dilin ön üçte ikisinin tat duyusunu alır.",
  ["Dilin arka üçte birinin hem tat hem genel duyusunu alır.", "Öğürme refleksinin afferent koludur.",
   "Sinus caroticus'tan baroreseptör bilgisi taşır.", "Otik ganglion aracılığıyla parotis salgısını uyarır."],
  """IX dilin arka 1/3'ünün tat ve genel duyusunu, farinks mukozasını ve karotis sinüs/cisminden gelen
  bilgiyi taşır; tek motor kası m. stylopharyngeus'tur. Dilin ön 2/3'ünün tadı chorda tympani (VII),
  genel duyusu n. lingualis (V3) ile taşınır.""",
  e=["n-glossopharyngeus", "gustus"]),

Q("tv", KS, "'Aaa' demesi istenen hastanın küçük dili (uvula) sağa sapıyor. Lezyon hangi sinirde ve taraftadır?",
  "Sol n. vagus",
  ["Sağ n. vagus", "Sol n. glossopharyngeus", "Sağ n. hypoglossus", "Sol n. facialis"],
  """Yumuşak damak kasları (levator veli palatini vb.) n. vagus ile innerve edilir. Bir tarafın felcinde
  sağlam taraf damağı kendine doğru çeker; uvula sağlam tarafa, yani lezyonun karşısına sapar. Dilde ise
  tersine, dil lezyon tarafına sapar.""",
  e=["n-vagus"]),

Q("t", KS, "Sol n. laryngeus recurrens hangi yapının altından dolanarak yukarı döner?",
  "Arcus aortae (lig. arteriosum'un hemen lateralinden)",
  ["A. subclavia sinistra", "Truncus brachiocephalicus", "Bronchus principalis sinister", "V. brachiocephalica sinistra"],
  """Sol rekürren sinir arcus aortae'nin altından, lig. arteriosum'un yanından dolanır; sağ rekürren sinir
  sağ a. subclavia'nın altından döner. Uzun seyri nedeniyle sol sinir aort anevrizması, sol atriyum
  genişlemesi veya akciğer tümörüyle sıkışabilir ve ses kısıklığı yapar.""",
  e=["n-vagus", "aorta", "larynx"]),

Q("f", KS, "Parasempatik lif taşıyan kranial sinirler hangileridir?",
  "III, VII, IX ve X",
  ["III, IV, V ve VI", "V, VII, IX ve XI", "II, III, VII ve XII", "VII, IX, X ve XII"],
  """Kraniyal parasempatik çıkış dört sinirle olur: III (siliyer ganglion – pupilla ve akomodasyon),
  VII (pterigopalatin ve submandibular ganglionlar), IX (otik ganglion – parotis) ve X (toraks ve karın
  organları).""",
  e=["systema-autonomicum", "n-vagus"]),

Q("f", KS, "Beyin sapının dorsal (arka) yüzünden çıkan tek kranial sinir hangisidir?",
  "N. trochlearis",
  ["N. abducens", "N. oculomotorius", "N. trigeminus", "N. accessorius"],
  """N. trochlearis lifleri orta beyinde çaprazlaşıp inferior kollikulusların altından, dorsal yüzden çıkar.
  En ince ve intrakraniyal seyri en uzun kranial sinirdir. Karşı taraftaki m. obliquus superior'u innerve eder.""",
  e=["n-trochlearis", "mesencephalon"]),

Q("t", KS, """Yüzündeki çıbanı sıktıktan sonra ateş, göz çevresinde ödem ve proptozis gelişen hastada sinus
cavernosus trombozu düşünülüyor. İlk etkilenmesi beklenen kranial sinir hangisidir ve neden?""",
  "N. abducens; sinüsün içinde a. carotis interna ile birlikte serbest seyrettiği için",
  ["N. oculomotorius; sinüsün dış duvarının en üstünde olduğu için", "N. opticus; sinüsün içinden geçtiği için",
   "N. maxillaris; sinüsün tabanında olduğu için", "N. trochlearis; sinüsün içinde serbest seyrettiği için"],
  """Sinus cavernosus'un dış duvarında yukarıdan aşağı III, IV, V1 ve V2; sinüsün içinde a. carotis interna
  ve n. abducens bulunur. Bu nedenle abducens felci (yana bakış kısıtlılığı) çoğunlukla ilk bulgudur.
  Yüzün 'tehlikeli üçgeni' v. ophthalmica aracılığıyla sinüsle bağlantılıdır.""",
  e=["n-abducens", "sinus-durae-matris", "a-carotis-interna"]),

# ------------------------------------------------------------------ Spinal sinirler ve pleksuslar
Q("f", SS, "Plexus brachialis'in fasikülleri (kordlar) neye göre adlandırılır?",
  "A. axillaris'in ikinci bölümüne göre konumlarına",
  ["Çıktıkları spinal segmentlere göre", "Klavikulaya göre konumlarına", "Innerve ettikleri kompartmana göre", "M. scalenus anterior'a göre konumlarına"],
  """Lateral, medial ve posterior kordlar pectoralis minor'un arkasında a. axillaris'in ikinci bölümünü
  çevreler ve adlarını bu artere göre konumlarından alır. Kökler (C5–T1) skalen aralıkta, gövdeler arka
  üçgende, bölümler klavikula arkasında yer alır.""",
  e=["plexus-brachialis", "a-axillaris"]),

Q("tv", SS, """Zor doğumda omuz takılması (distosi) yaşanan bebeğin kolu yanında addüksiyon ve iç rotasyonda,
dirseği ekstansiyonda, önkolu pronasyonda duruyor ('garson bahşişi' pozisyonu). Etkilenen yapı hangisidir?""",
  "Plexus brachialis'in üst gövdesi (C5–C6) – Erb–Duchenne felci",
  ["Plexus brachialis'in alt gövdesi (C8–T1) – Klumpke felci", "Fasciculus posterior", "N. axillaris", "N. musculocutaneus"],
  """Baş ile omuz arasının zorla açılması üst gövdeyi gerer. Deltoid, supraspinatus, infraspinatus (abdüksiyon
  ve dış rotasyon), biceps ve brachialis (dirsek fleksiyonu) ile supinatörler felç olur; kol tipik
  pozisyonu alır.""",
  e=["plexus-brachialis"]),

Q("tv", SS, """Düşerken bir dala tutunarak kolu zorla yukarı çekilen hastada elde pençeleşme, intrinsik kas
atrofisi, önkol iç yüzünde his kaybı ve aynı tarafta pitozis ile miyozis gelişiyor. Lezyon hangisidir?""",
  "Plexus brachialis'in alt gövdesi (C8–T1) – Klumpke felci",
  ["Plexus brachialis'in üst gövdesi (C5–C6)", "N. medianus'un bilek düzeyinde yaralanması", "N. radialis'in aksilla düzeyinde yaralanması",
   "Fasciculus lateralis"],
  """Kolun abdüksiyonda zorla çekilmesi alt gövdeyi (C8–T1) gerer: elin intrinsik kasları felç olur ve pençe
  el gelişir. T1 köküne yakın sempatik liflerin (stellat ganglion) etkilenmesi Horner sendromunu açıklar.""",
  e=["plexus-brachialis", "truncus-sympathicus"]),

Q("t", SS, "Aşağıdaki sinirlerden hangisi plexus brachialis'in fasciculus posterior'undan çıkmaz?",
  "N. musculocutaneus",
  ["N. axillaris", "N. radialis", "N. thoracodorsalis", "N. subscapularis superior"],
  """Arka kord omuz ve kolun arka yüzünü besleyen dalları verir: üst ve alt subskapular, torakodorsal,
  aksiller ve radial sinirler. N. musculocutaneus lateral korddan çıkar ve kolun ön kompartmanını innerve eder.""",
  e=["plexus-brachialis", "n-musculocutaneus"]),

Q("f", SS, "N. medianus plexus brachialis'in hangi kısımlarından oluşur?",
  "Fasciculus lateralis ve fasciculus medialis",
  ["Fasciculus posterior ve fasciculus medialis", "Yalnızca fasciculus lateralis", "Truncus superior ve truncus medius",
   "Fasciculus lateralis ve fasciculus posterior"],
  """N. medianus lateral ve medial kordlardan gelen iki kökün a. axillaris'in önünde birleşmesiyle oluşur
  (C6–T1, C5 lifleri de içerebilir). Kolda dal vermez; önkol fleksörlerinin çoğunu ve tenar kasları innerve eder.""",
  e=["n-medianus", "plexus-brachialis"]),

Q("t", SS, "Kolda (brachium) hiç dal vermeyen sinirler hangileridir?",
  "N. medianus ve n. ulnaris",
  ["N. radialis ve n. musculocutaneus", "N. axillaris ve n. radialis", "N. musculocutaneus ve n. medianus", "N. ulnaris ve n. radialis"],
  """N. medianus ve n. ulnaris kolda seyretse de motor ya da duyusal dal vermez; dalları önkol ve eldedir.
  Kolun ön kompartmanını n. musculocutaneus, arka kompartmanını n. radialis innerve eder.""",
  e=["n-medianus", "n-ulnaris"]),

Q("f", SS, "Aşağıdaki dermatom eşleştirmelerinden hangisi yanlıştır?",
  "C8 – başparmak",
  ["T4 – meme başı", "T10 – göbek", "L1 – kasık bölgesi", "S1 – ayağın dış kenarı ve topuk"],
  """Elde C6 başparmak, C7 orta parmak, C8 serçe parmak dermatomudur. Gövdede T4 meme başı, T10 göbek, L1 kasık;
  bacakta L4 medial malleol, L5 ayak sırtı ve başparmak, S1 ayak dış kenarı ve topuktur.""",
  e=["ganglion-spinale", "n-intercostales"]),

Q("tv", SS, """Obez, sıkı kemer takan hastada uyluğun ön-dış yüzünde yanma, uyuşma ve karıncalanma var; kas
gücü ve refleksler normal. Sıkışan sinir hangisidir?""",
  "N. cutaneus femoris lateralis",
  ["N. femoralis", "N. obturatorius", "N. genitofemoralis", "N. saphenus"],
  """Meralgia parestetika: L2–L3 kökenli, saf duyusal n. cutaneus femoris lateralis SIAS'ın hemen medialinde
  lig. inguinale'nin altından geçerken sıkışır. Motor lif içermediği için güçsüzlük olmaz.""",
  e=["plexus-lumbalis", "lig-inguinale"]),

Q("t", SS, "N. femoralis yaralanmasında aşağıdakilerden hangisi beklenmez?",
  "Uyluk addüksiyonunda belirgin güçsüzlük",
  ["Diz ekstansiyonunda güçsüzlük", "Patella refleksinin kaybı", "Uyluk ön yüzünde his kaybı", "Bacağın iç yüzünde his kaybı"],
  """N. femoralis (L2–L4) quadriceps, sartorius, iliacus ve pectineus'u innerve eder; uyluk ön yüzünün ve
  n. saphenus aracılığıyla bacak iç yüzünün duyusunu alır. Addüktörler n. obturatorius ile innerve edilir.""",
  e=["n-femoralis", "m-quadriceps-femoris"]),

Q("fv", SS, """Uzun süren pelvik cerrahi sonrası hasta bacaklarını birbirine yaklaştırmakta güçlük çekiyor ve
uyluğunun iç yüzünde küçük bir alanda uyuşma var. Yaralanan sinir hangisidir?""",
  "N. obturatorius",
  ["N. femoralis", "N. pudendus", "N. genitofemoralis", "N. gluteus superior"],
  """N. obturatorius (L2–L4) pelvisin yan duvarında, ovaryum çukurunun yakınından geçerek canalis
  obturatorius'a girer. Pelvik cerrahi, tümörler veya zor doğumda yaralanabilir; uyluk addüktörleri
  güçsüzleşir ve uyluk iç yüzünde his kaybı olur.""",
  e=["n-obturatorius", "mm-adductores"]),

Q("f", SS, "N. ischiadicus en sık hangi düzeyde iki uç dalına (n. tibialis ve n. fibularis communis) ayrılır?",
  "Fossa poplitea'nın üst köşesinde",
  ["Foramen ischiadicum majus'tan çıkarken", "Uyluğun en üst kısmında, gluteal kıvrımda", "Fibula boynunda", "Malleolus medialis'in arkasında"],
  """Vücudun en kalın siniri olan n. ischiadicus (L4–S3) genellikle popliteal çukurun tepesinde ikiye ayrılır.
  Bazen ayrılma daha yukarıda olur ve fibular bölüm piriformisi deler.""",
  e=["n-ischiadicus", "fossa-poplitea"]),

Q("t", SS, "N. tibialis'in popliteal çukurda yaralanması sonucunda aşağıdakilerden hangisi görülür?",
  "Ayak plantar fleksiyonunun ve parmak fleksiyonunun kaybı, ayak tabanında his kaybı",
  ["Düşük ayak ve ayak sırtında his kaybı", "Ayak eversiyonunun kaybı", "Diz ekstansiyonunun kaybı", "Bacağın iç yüzünde his kaybı"],
  """N. tibialis arka kompartman kaslarını (triceps surae, tibialis posterior, uzun fleksörler) ve plantar
  dallarıyla ayak tabanı kaslarını innerve eder. Hasarında ayak dorsifleksiyon ve eversiyonda kalır
  (kalkaneovalgus), parmak ucunda yürünemez ve taban duyusu kaybolur.""",
  e=["n-tibialis", "m-triceps-surae"]),

Q("f", SS, "M. sphincter ani externus'u innerve eden sinir hangisidir?",
  "N. pudendus (n. rectalis inferior)",
  ["Nn. splanchnici pelvici", "N. obturatorius", "N. genitofemoralis", "Plexus hypogastricus inferior"],
  """İstemli kontrol edilen dış anal sfinkter ve dış üretral sfinkter n. pudendus (S2–S4) ile innerve edilir.
  İç sfinkterler düz kastır ve otonom sinirlerle kontrol edilir.""",
  e=["n-pudendus", "rectum"]),

Q("f", SS, "Ganglion spinale (arka kök ganglionu) hangi hücrelerin gövdelerini içerir?",
  "Psödounipolar duyusal nöronlar",
  ["Alt motor nöronlar", "Preganglioner sempatik nöronlar", "Postganglioner parasempatik nöronlar", "Ara nöronlar (internöronlar)"],
  """Arka kök ganglionundaki psödounipolar nöronların periferik uzantısı reseptörlerden bilgi alır, santral
  uzantısı arka kökle omuriliğe girer. Bu ganglionda sinaps yoktur. Herpes zoster virüsü burada latent kalır.""",
  e=["ganglion-spinale"]),

Q("t", SS, "Koltuk değneğini yanlış kullanan hastada n. radialis aksillada sıkışırsa, sulcus nervi radialis düzeyindeki lezyondan farklı olarak hangisi de görülür?",
  "M. triceps brachii'de güçsüzlük ve triseps refleksinde azalma",
  ["Düşük el görülmez.", "Avuç içinde his kaybı", "Elin intrinsik kaslarında atrofi", "M. biceps brachii'de güçsüzlük"],
  """Tricepsin dalları n. radialis'ten aksilla ve kolun üst kısmında ayrılır. Aksiller (koltuk değneği) lezyonda
  dirsek ekstansiyonu da etkilenir; humerus cismi düzeyindeki lezyonda triceps çoğunlukla korunur,
  ikisinde de düşük el vardır.""",
  e=["n-radialis", "m-triceps-brachii"]),

Q("f", SS, "N. phrenicus hangi spinal segmentlerden köken alır?",
  "C3–C5",
  ["C1–C3", "C5–C7", "T1–T2", "C7–T1"],
  """'C3, C4, C5 diyaframı canlı tutar.' N. phrenicus plexus cervicalis'in en önemli dalıdır; C4 asıl
  katkıyı verir. C3 üstündeki omurilik yaralanmalarında kendiliğinden solunum durur.""",
  e=["n-phrenicus", "diaphragma"]),

# ------------------------------------------------------------------ Otonom
Q("f", OT, "Sempatik sistemin preganglioner nöron gövdeleri omuriliğin neresindedir?",
  "T1–L2 segmentlerinin lateral boynuzunda (nucleus intermediolateralis)",
  ["S2–S4 segmentlerinin ön boynuzunda", "Tüm segmentlerin arka boynuzunda", "C1–C8 segmentlerinin lateral boynuzunda",
   "Beyin sapındaki parasempatik çekirdeklerde"],
  """Sempatik sistem torakolomber çıkışlıdır: preganglioner nöronlar T1–L2'nin lateral boynuzundadır ve
  ak rami communicantes ile sempatik zincire ulaşır. Parasempatik sistem kraniosakraldir (III, VII, IX, X ve S2–S4).""",
  e=["truncus-sympathicus", "systema-autonomicum"]),

Q("t", OT, "Gözyaşı bezine giden parasempatik lifler hangi ganglionda sinaps yapar?",
  "Ganglion pterygopalatinum",
  ["Ganglion ciliare", "Ganglion oticum", "Ganglion submandibulare", "Ganglion cervicale superius"],
  """Lifler n. facialis'ten n. petrosus major ile çıkar, n. canalis pterygoidei ile ganglion pterygopalatinum'a
  ulaşır; postganglioner lifler n. zygomaticus ve n. lacrimalis ile bezi uyarır. Bu nedenle ganglion
  geniculi proksimalindeki VII lezyonlarında göz kuruluğu olur.""",
  e=["n-facialis", "apparatus-lacrimalis", "systema-autonomicum"]),

Q("t", OT, "Parotis bezinin salgısını uyaran parasempatik lifler hangi sinirle başlar ve hangi ganglionda sinaps yapar?",
  "N. glossopharyngeus – ganglion oticum",
  ["N. facialis – ganglion submandibulare", "N. facialis – ganglion pterygopalatinum", "N. vagus – ganglion oticum",
   "N. glossopharyngeus – ganglion ciliare"],
  """IX'un timpanik dalı n. petrosus minor'u oluşturur; lifler otik ganglionda sinaps yapar ve n. auriculotemporalis
  (V3) ile parotise ulaşır. Submandibular ve sublingual bezler ise VII'nin chorda tympani lifleriyle uyarılır.""",
  e=["n-glossopharyngeus", "glandula-parotidea"]),

Q("tv", OT, """Uzun süredir sigara içen hastada sağ omuz ve kolun iç yüzüne yayılan ağrı, sağ gözde hafif pitozis,
miyozis ve yüzünün sağ yarısında terleme kaybı var. En olası neden hangisidir?""",
  "Sağ akciğer apeksinde Pancoast tümörünün servikal sempatik zinciri tutması",
  ["Sağ n. oculomotorius felci", "Sol hemisfer inmesi", "Sağ n. facialis felci", "Myastenia gravis"],
  """Horner sendromu (pitozis – m. tarsalis superior, miyozis – m. dilatator pupillae, anhidroz) sempatik yolun
  herhangi bir yerdeki hasarıyla olur. Akciğer apeksi tümörü stellat ganglion ve alt gövdeyi (C8–T1) tutarak
  Horner ile kolda ağrıya yol açar.""",
  e=["truncus-sympathicus", "pulmones", "plexus-brachialis"]),

Q("t", OT, "Böbrek üstü bezi medullasının sempatik innervasyonu için hangisi doğrudur?",
  "Preganglioner lifler doğrudan medulla hücrelerinde sonlanır; medulla bir ganglion gibi davranır.",
  ["Postganglioner lifler çölyak ganglionundan gelir.", "Parasempatik lifler n. vagus ile gelir.",
   "Kromaffin hücreler postganglioner nöronlardan uyarı alır.", "Medulla otonom innervasyon almaz."],
  """Adrenal medullanın kromaffin hücreleri nöral krista kökenlidir ve modifiye postganglioner nöronlar
  sayılır. Splanknik sinirlerle gelen preganglioner lifler doğrudan bu hücrelerle sinaps yaparak adrenalin
  ve noradrenalin salınımını uyarır.""",
  e=["glandula-suprarenalis", "systema-autonomicum"]),

Q("t", OT, "Ter bezlerinin sempatik innervasyonunda postganglioner liflerin salgıladığı nörotransmiter hangisidir?",
  "Asetilkolin",
  ["Noradrenalin", "Adrenalin", "Dopamin", "Serotonin"],
  """Sempatik postganglioner liflerin çoğu noradrenerjiktir; ancak ekrin ter bezlerine gidenler kolinerjiktir
  (muskarinik reseptörler). Bu nedenle antikolinerjik ilaçlar terlemeyi azaltır.""",
  e=["glandulae-cutis", "systema-autonomicum"]),

Q("t", OT, "Nn. splanchnici pelvici ile ilgili aşağıdakilerden hangisi doğrudur?",
  "S2–S4'ten çıkan preganglioner parasempatik lifler taşırlar.",
  ["T5–T9'dan çıkan preganglioner sempatik lifler taşırlar.", "Postganglioner sempatik lifler taşırlar.",
   "Yalnızca duyusal liflerden oluşurlar.", "N. vagus'un pelvis dallarıdır."],
  """Pelvik splanknik sinirler mesane (detrusor kasılması), rektum, inen ve sigmoid kolon ile ereksiyonu
  (‘point’) sağlayan parasempatik lifleri taşır. Torakal splanknik sinirler (major T5–T9, minor T10–T11,
  imus T12) ise sempatiktir.""",
  e=["systema-autonomicum", "vesica-urinaria"]),

Q("fv", OT, """Apandisit başlangıcında hasta göbek çevresinde, sınırları belirsiz ağrı tarifliyor; saatler sonra
ağrı sağ alt kadrana yerleşiyor. İlk ağrının göbek çevresinde hissedilmesinin nedeni nedir?""",
  "Apendiksin viseral afferentleri T10 segmentine girer; ağrı bu dermatoma yansır.",
  ["Apendiks göbeğin hemen arkasında yer alır.", "N. phrenicus tahriş olur.",
   "Parietal periton erken dönemde tutulur.", "N. ilioinguinalis apendiksi innerve eder."],
  """Orta bağırsak kökenli organların viseral ağrısı sempatik liflerle T10 segmentine taşınır ve göbek
  çevresine yansır. İnflamasyon parietal peritona ulaştığında somatik innervasyon sayesinde ağrı McBurney
  noktasına lokalize olur.""",
  e=["appendix-vermiformis", "systema-autonomicum"]),

Q("t", OT, "N. vagus'un parasempatik innervasyonu bağırsak kanalında yaklaşık nereye kadar uzanır?",
  "Colon transversum'un sol üçte birine (flexura coli sinistra yakınına) kadar",
  ["Duodenumun sonuna kadar", "Ileumun sonuna kadar", "Rektumun sonuna kadar", "Sigmoid kolonun başına kadar"],
  """Vagus ön ve orta bağırsak türevlerini (transvers kolonun yaklaşık 2/3'üne kadar) innerve eder. Sol kolon
  bükümünden itibaren arka bağırsak türevleri parasempatik lifleri pelvik splanknik sinirlerden (S2–S4) alır.""",
  e=["n-vagus", "intestinum-crassum"]),

Q("f", OT, "Ganglion stellatum hangi ganglionların birleşmesiyle oluşur?",
  "Alt servikal ganglion ve birinci torakal ganglion",
  ["Üst ve orta servikal ganglionlar", "Çölyak ve aortikorenal ganglionlar", "Siliyer ve pterigopalatin ganglionlar",
   "Orta servikal ve ikinci torakal ganglionlar"],
  """Stellat (servikotorasik) ganglion çoğu kişide alt servikal ve T1 ganglionlarının kaynaşmasıyla oluşur;
  1. kaburga boynunun önünde, a. vertebralis'in başlangıcının arkasındadır. Blokajı üst ekstremitenin
  sempatik kaynaklı ağrılarında kullanılır ve Horner sendromuna yol açar.""",
  e=["truncus-sympathicus"]),

Q("t", OT, "Rami communicantes albi (ak bağlantı dalları) için aşağıdakilerden hangisi doğrudur?",
  "Yalnızca T1–L2 spinal sinirlerinde bulunur ve miyelinli preganglioner lifler taşır.",
  ["Tüm spinal sinirlerde bulunur.", "Miyelinsiz postganglioner lifler taşır.",
   "Parasempatik lifleri sempatik zincire taşır.", "Yalnızca servikal sinirlerde bulunur."],
  """Ak dallar preganglioner liflerin miyelinli olması nedeniyle beyaz görünür ve yalnızca sempatik çıkışın
  olduğu T1–L2 segmentlerinde vardır. Gri dallar (miyelinsiz postganglioner) zincirden tüm spinal sinirlere
  geri döner; böylece tüm vücut derisindeki damar, ter bezi ve kıl kasları sempatik lif alır.""",
  e=["truncus-sympathicus", "ganglion-spinale"]),
]

from q_nervous2 import questions as more  # noqa: E402

write("nervous", questions + more)
