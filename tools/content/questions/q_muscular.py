from qcommon import Q, write

BAS = "Baş kasları"
BOY = "Boyun kasları"
SIR = "Sırt kasları"
GOG = "Göğüs kasları"
KAR = "Karın kasları"
OMZ = "Omuz kasları"
KOL = "Kol kasları"
ONK = "Önkol kasları"
EL = "El kasları"
KLC = "Kalça kasları"
UYL = "Uyluk kasları"
BCK = "Bacak kasları"
AYK = "Ayak kasları"

questions = [
# ------------------------------------------------------------------ Baş
Q("f", BAS, "M. buccinator'u innerve eden sinir hangisidir?",
  "N. facialis (ramus buccalis)",
  ["N. buccalis (V3)", "N. trigeminus'un motor kökü", "N. hypoglossus", "N. glossopharyngeus"],
  """Buccinator bir mimik kasıdır ve n. facialis'in bukkal dalıyla innerve edilir; yanağı dişlere
  bastırarak lokmanın vestibüle kaçmasını önler. N. buccalis (V3) yalnızca duyusaldır ve yanağın
  deri ile mukozasını innerve eder; isim benzerliği sık karıştırılır.""",
  ["Yanak deri ve mukozasının duyusunu alır; kası innerve etmez.", "Çiğneme kaslarını innerve eder.",
   "Dil kaslarını innerve eder.", "Yalnızca m. stylopharyngeus'u innerve eder."],
  e=["m-buccinator", "n-facialis"]),

Q("tv", BAS, """Sol hemisferde iskemik inme geçiren hastada sağ ağız köşesinde düşme ve sağ nazolabial
olukta silinme var; ancak hasta iki taraflı alnını kırıştırabiliyor ve gözlerini kapatabiliyor.
Bu bulgunun açıklaması nedir?""",
  "Yüzün üst kısmını innerve eden fasiyal çekirdek bölümü iki taraflı kortikal lif alır.",
  ["Lezyon fasiyal sinirin pons içindeki seyrindedir.", "Alın kaslarını n. trigeminus innerve eder.",
   "M. occipitofrontalis'in innervasyonu servikal sinirlerdendir.", "Lezyon n. facialis'in stilomastoid delikten çıktığı yerdedir."],
  """Santral (üst motor nöron) fasiyal felçte yalnızca karşı tarafın yüz alt yarısı etkilenir; çünkü
  fasiyal çekirdeğin alın ve orbicularis oculi'yi yöneten bölümü her iki hemisferden kortikobulber lif
  alır. Periferik (Bell) felçte ise aynı tarafın yüzünün tamamı tutulur.""",
  e=["n-facialis", "m-occipitofrontalis", "m-orbicularis-oculi"]),

Q("fv", BAS, """Bell paralizisi olan hasta sağ gözünü kapatamıyor ve gözünde kuruluk tarif ediyor. Göz
kapanmasını sağlayan kas ve siniri hangisidir?""",
  "M. orbicularis oculi – n. facialis",
  ["M. levator palpebrae superioris – n. oculomotorius", "M. tarsalis superior – sempatik lifler",
   "M. orbicularis oculi – n. trigeminus", "M. corrugator supercilii – n. oculomotorius"],
  """Göz kapağını kapatan m. orbicularis oculi n. facialis'in temporal ve zigomatik dallarıyla innerve
  edilir. Felcinde göz kapanamaz, kornea kurur ve korneal refleksin efferent kolu kaybolur. Kapağı
  kaldıran levator ise n. oculomotorius'tandır.""",
  e=["m-orbicularis-oculi", "n-facialis"]),

Q("t", BAS, "Çiğneme kaslarından ağzı açan (mandibulayı protrüzyon ve depresyona getiren) kas hangisidir?",
  "M. pterygoideus lateralis",
  ["M. masseter", "M. temporalis", "M. pterygoideus medialis", "M. mylohyoideus"],
  """Dört çiğneme kasından üçü (masseter, temporalis, medial pterygoid) çeneyi kapatır. Lateral
  pterygoid kondili ve diski öne çekerek ağzın açılmasını başlatır; yerçekimi ve suprahiyoid kaslar
  hareketi tamamlar. Tüm çiğneme kasları n. mandibularis (V3) ile innerve edilir.""",
  e=["mm-pterygoidei", "m-masseter", "m-temporalis"]),

Q("f", BAS, "Mandibulayı geriye çeken (retraksiyon) başlıca kas hangisidir?",
  "M. temporalis'in arka lifleri",
  ["M. masseter'in yüzeyel kısmı", "M. pterygoideus lateralis", "M. pterygoideus medialis", "M. buccinator"],
  """Temporalis'in yelpaze biçimli lifleri processus coronoideus'a uzanır. Ön ve orta lifler çeneyi
  kapatır; neredeyse yatay seyreden arka lifler mandibulayı geri çeker.""",
  e=["m-temporalis"]),

Q("tv", BAS, """Kafa travması sonrası hasta özellikle merdiven inerken ve kitap okurken çift görme
tarifliyor; başını sağlam tarafa eğerek tutuyor. Felçli kas hangisidir?""",
  "M. obliquus superior",
  ["M. rectus lateralis", "M. rectus inferior", "M. obliquus inferior", "M. rectus medialis"],
  """M. obliquus superior (n. trochlearis, IV) gözü özellikle addüksiyondayken aşağı çevirir ve
  intorsiyon yapar. Felcinde aşağı-içe bakışta (merdiven inme, okuma) dikey diplopi olur; hasta
  ekstorsiyonu dengelemek için başını karşı tarafa eğer. N. trochlearis kafa travmasında uzun
  intrakraniyal seyri nedeniyle sık yaralanır.""",
  e=["mm-bulbi", "n-trochlearis"]),

Q("f", BAS, "N. abducens felcinde etkilenen gözün dinlenme konumu nasıldır?",
  "İçe (addüksiyona) kaymıştır.",
  ["Dışa ve aşağı kaymıştır.", "Yukarı ve içe kaymıştır.", "Dışa (abdüksiyona) kaymıştır.", "Değişmez, yalnızca pupil genişler."],
  """N. abducens (VI) yalnızca m. rectus lateralis'i innerve eder. Felcinde rakipsiz kalan m. rectus
  medialis gözü içe çeker (esotropi) ve yana bakışta yatay diplopi olur. 'Dışa ve aşağı' konum
  okülomotor felcine özgüdür.""",
  e=["mm-bulbi", "n-abducens"]),

Q("f", BAS, "M. levator palpebrae superioris'i innerve eden sinir hangisidir?",
  "N. oculomotorius",
  ["N. facialis", "N. trochlearis", "N. ophthalmicus", "Servikal sempatik zincir"],
  """Levator palpebrae superioris n. oculomotorius'un üst dalıyla innerve edilir; III felcinde tam
  pitozis olur. Kasın düz kas bölümü olan m. tarsalis superior (Müller) sempatik liflerle innerve
  edilir; Horner sendromundaki hafif pitozis buna bağlıdır.""",
  e=["mm-bulbi", "n-oculomotorius"]),

Q("tv", BAS, "Dilini dışarı çıkaran hastanın dili sağa sapıyor. Lezyon hangi sinir ve taraftadır?",
  "Sağ n. hypoglossus",
  ["Sol n. hypoglossus", "Sağ n. glossopharyngeus", "Sol n. vagus", "Sağ n. lingualis"],
  """Dili dışarı çıkaran m. genioglossus her iki taraftan dili öne ve karşı tarafa iter. Tek taraflı
  XII felcinde sağlam taraf baskın kalır ve dil felçli tarafa (lezyon tarafına) sapar. Kronik
  lezyonda o tarafta atrofi ve fasikülasyon görülür.""",
  e=["mm-linguae", "n-hypoglossus"]),

Q("t", BAS, "Aşağıdaki dil kaslarından hangisi n. hypoglossus tarafından innerve edilmez?",
  "M. palatoglossus",
  ["M. genioglossus", "M. hyoglossus", "M. styloglossus", "M. longitudinalis superior"],
  """Tüm intrinsik ve ekstrinsik dil kasları n. hypoglossus ile innerve edilir; tek istisna yumuşak
  damak kası sayılan m. palatoglossus'tur ve n. vagus'un (plexus pharyngeus) dalını alır.""",
  e=["mm-linguae", "n-hypoglossus", "n-vagus"]),

Q("f", BAS, "Alnı kırıştıran ve kaşları kaldıran kas hangisidir?",
  "M. occipitofrontalis (venter frontalis)",
  ["M. corrugator supercilii", "M. procerus", "M. orbicularis oculi", "M. temporalis"],
  """Occipitofrontalis'in frontal karnı galea aponeurotica'yı öne çeker, kaşları kaldırır ve alında
  yatay çizgiler oluşturur. Frontal karın n. facialis'in temporal dalı, oksipital karın ise
  n. auricularis posterior ile innerve edilir.""",
  e=["m-occipitofrontalis", "n-facialis"]),

Q("f", BAS, "Gülümsemede ağız köşesini yukarı ve dışa çeken kas hangisidir?",
  "M. zygomaticus major",
  ["M. depressor anguli oris", "M. buccinator", "M. orbicularis oris", "M. levator labii superioris alaeque nasi"],
  """M. zygomaticus major os zygomaticum'dan başlayıp ağız köşesindeki modiolus'a tutunur ve gülme
  ifadesini sağlar. Depressor anguli oris ağız köşesini aşağı çekerek üzüntü ifadesi verir.""",
  e=["m-zygomaticus-major", "m-depressor-anguli-oris"]),

# ------------------------------------------------------------------ Boyun
Q("f", BOY, "Tek taraflı kasıldığında başı aynı omza eğip yüzü karşı tarafa ve yukarı çeviren kas hangisidir?",
  "M. sternocleidomastoideus",
  ["M. trapezius", "M. scalenus anterior", "M. levator scapulae", "M. splenius capitis"],
  """SCM sternum ve klavikuladan processus mastoideus'a uzanır. Tek taraflı kasılmada başı aynı tarafa
  eğer ve yüzü karşı tarafa döndürür; iki taraflı kasıldığında başı öne büker. Konjenital tortikolliste
  kas fibrozlaşır ve kısalır. Motor siniri n. accessorius'tur.""",
  e=["m-sternocleidomastoideus", "n-accessorius"]),

Q("t", BOY, "M. scalenus anterior'un ön yüzünde yukarıdan aşağı inen sinir hangisidir?",
  "N. phrenicus",
  ["N. vagus", "N. accessorius", "Truncus sympathicus", "N. laryngeus recurrens"],
  """N. phrenicus (C3–C5) prevertebral fasyanın altında, m. scalenus anterior'un ön yüzünde dıştan içe
  doğru aşağı iner ve göğüs girişinden toraksa geçer. Skalen kasın ön yüzü bu nedenle önemli bir
  cerrahi işarettir.""",
  e=["mm-scaleni", "n-phrenicus"]),

Q("t", BOY, "M. scalenus anterior ile m. scalenus medius arasındaki aralıktan geçen yapılar hangileridir?",
  "A. subclavia ve plexus brachialis'in kökleri/gövdeleri",
  ["V. subclavia ve n. phrenicus", "A. carotis communis ve n. vagus", "V. jugularis interna ve ductus thoracicus", "A. vertebralis ve truncus sympathicus"],
  """Skalen aralıktan a. subclavia ve plexus brachialis geçer; v. subclavia ise m. scalenus anterior'un
  önünden geçer. Skalen kasların hipertrofisi veya anomalisi bu aralıkta torasik çıkış sendromuna yol
  açabilir. İnterskalen blok bu bölgeye yapılır.""",
  e=["mm-scaleni", "a-subclavia", "plexus-brachialis"]),

Q("t", BOY, "Aşağıdaki suprahiyoid kas–sinir eşleştirmelerinden hangisi yanlıştır?",
  "M. geniohyoideus – n. mylohyoideus",
  ["M. digastricus venter anterior – n. mylohyoideus", "M. digastricus venter posterior – n. facialis",
   "M. stylohyoideus – n. facialis", "M. mylohyoideus – n. mylohyoideus"],
  """M. geniohyoideus C1 liflerince innerve edilir; bu lifler n. hypoglossus ile birlikte seyreder.
  Digastricus'un iki karnının farklı sinir alması (V3 ve VII) farklı faringeal arklardan gelişmesindendir.""",
  e=["mm-suprahyoidei", "n-trigeminus", "n-facialis"]),

Q("f", BOY, "İnfrahiyoid kasların çoğunu innerve eden yapı hangisidir?",
  "Ansa cervicalis (C1–C3)",
  ["N. hypoglossus'un kendi lifleri", "N. vagus", "N. accessorius", "N. phrenicus"],
  """Sternohyoideus, sternothyroideus ve omohyoideus ansa cervicalis ile innerve edilir. Thyrohyoideus
  ise n. hypoglossus ile seyreden C1 liflerini alır. Ansa cervicalis'in üst kökü (C1) XII ile birlikte,
  alt kökü C2–C3'ten gelir.""",
  e=["mm-infrahyoidei"]),

Q("f", BOY, "Platysma hangi sinir tarafından innerve edilir?",
  "N. facialis (ramus colli)",
  ["Ansa cervicalis", "N. transversus colli", "N. accessorius", "N. mandibularis"],
  """Platysma boyun yüzeyel fasyası içinde uzanan ince bir mimik kasıdır ve n. facialis'in servikal
  dalıyla innerve edilir. Boyun derisini gerer, ağız köşesini aşağı çeker.""",
  e=["m-platysma", "n-facialis"]),

# ------------------------------------------------------------------ Sırt
Q("tv", SIR, """Boynun arka üçgeninden lenf nodu biyopsisi yapılan hastada omuz düşük duruyor, kolunu
90°'nin üzerine kaldırmakta ve omuz silkmede güçlük çekiyor. Yaralanan sinir ve kas hangisidir?""",
  "N. accessorius – m. trapezius",
  ["N. dorsalis scapulae – m. rhomboideus major", "N. thoracicus longus – m. serratus anterior",
   "N. axillaris – m. deltoideus", "N. suprascapularis – m. supraspinatus"],
  """N. accessorius arka üçgende yüzeysel seyreder ve biyopsilerde kolayca yaralanır. Trapezius'un üst
  lifleri skapulayı yukarı kaldırır ve serratus anterior ile birlikte yukarı döndürür; felcinde omuz
  düşer ve 90°'nin üzerine abdüksiyon zorlaşır.""",
  e=["m-trapezius", "n-accessorius"]),

Q("f", SIR, "M. latissimus dorsi'yi innerve eden sinir hangisidir?",
  "N. thoracodorsalis",
  ["N. dorsalis scapulae", "N. subscapularis inferior", "N. thoracicus longus", "N. axillaris"],
  """N. thoracodorsalis (C6–C8) plexus brachialis'in arka kordundan çıkar. Latissimus dorsi kolu
  ekstansiyon, addüksiyon ve iç rotasyona getirir; tırmanma ve yüzme gibi hareketlerde güçlüdür.
  Rekonstrüktif cerrahide flep olarak kullanılır.""",
  e=["m-latissimus-dorsi", "plexus-brachialis"]),

Q("f", SIR, "Mm. rhomboidei'yi innerve eden sinir hangisidir?",
  "N. dorsalis scapulae (C5)",
  ["N. accessorius", "N. thoracodorsalis", "N. suprascapularis", "N. thoracicus longus"],
  """N. dorsalis scapulae doğrudan C5 kökünden çıkar, m. scalenus medius'u deler ve m. levator scapulae
  ile rhomboid kasları innerve eder. Rhomboidler skapulayı geri ve yukarı çekerek omurgaya yaklaştırır.""",
  e=["mm-rhomboidei", "m-levator-scapulae"]),

Q("f", SIR, "M. erector spinae gibi derin (asıl) sırt kaslarını innerve eden sinirler hangileridir?",
  "Spinal sinirlerin arka dalları (rami posteriores)",
  ["Spinal sinirlerin ön dalları (rami anteriores)", "N. accessorius", "N. thoracodorsalis", "Nn. intercostales"],
  """Gerçek sırt kasları (erector spinae, transversospinal kaslar, suboksipital kaslar) epaksiyel kökenlidir
  ve spinal sinirlerin arka dallarıyla segmenter olarak innerve edilir. Yüzeyel sırt kasları (trapezius,
  latissimus, rhomboidler) ise ekstremiteye ait kaslardır ve ön dal kökenli sinirler alır.""",
  e=["m-erector-spinae", "mm-transversospinales"]),

Q("t", SIR, "Suboksipital üçgenin tabanında, atlasın arka kemeri üzerinde seyreden arter hangisidir?",
  "A. vertebralis",
  ["A. occipitalis", "A. carotis interna", "A. cervicalis profunda", "A. auricularis posterior"],
  """Suboksipital üçgeni m. rectus capitis posterior major ile m. obliquus capitis superior ve inferior
  sınırlar. Tabanında atlasın arka kemeri üzerindeki olukta a. vertebralis ve n. suboccipitalis (C1 arka
  dalı) bulunur. Üçgenin üzerinden n. occipitalis major geçer.""",
  e=["mm-suboccipitales", "a-vertebralis", "atlas"]),

Q("t", SIR, "Trigonum lumbale inferius'u (Petit üçgeni) sınırlayan yapılar hangileridir?",
  "M. latissimus dorsi, m. obliquus externus abdominis ve crista iliaca",
  ["M. trapezius, m. latissimus dorsi ve skapulanın medial kenarı", "M. erector spinae, 12. kaburga ve m. obliquus internus",
   "Lig. inguinale, m. rectus abdominis ve a. epigastrica inferior", "M. quadratus lumborum, m. psoas major ve diyafram"],
  """Petit üçgeni latissimus dorsi (arka-iç), external oblik (ön-dış) ve crista iliaca (taban) arasındadır;
  tabanını internal oblik kası yapar. Nadir görülen lomber fıtıklar burada gelişebilir. Trapezius,
  latissimus ve skapula kenarı ise oskültasyon üçgenini sınırlar.""",
  e=["m-latissimus-dorsi", "m-obliquus-externus", "os-coxae"]),

# ------------------------------------------------------------------ Göğüs
Q("tv", GOG, """Mastektomi ve aksiller diseksiyon sonrası hasta kollarını öne uzatıp duvarı ittiğinde
skapulasının iç kenarı göğüs duvarından ayrılıyor (kanatlı skapula). Yaralanan sinir hangisidir?""",
  "N. thoracicus longus",
  ["N. thoracodorsalis", "N. dorsalis scapulae", "N. pectoralis medialis", "N. intercostobrachialis"],
  """N. thoracicus longus (C5–C7) m. serratus anterior'un dış yüzünde, aksillanın iç duvarında aşağı iner
  ve aksiller cerrahide kolayca yaralanır. Serratus anterior skapulayı göğüs duvarına bastırır ve öne
  çeker; felcinde skapula kanatlanır ve kol 90°'nin üzerine kaldırılamaz.""",
  e=["m-serratus-anterior", "plexus-brachialis"]),

Q("f", GOG, "M. pectoralis major'un innervasyonu hangisidir?",
  "Nn. pectorales medialis ve lateralis",
  ["N. thoracodorsalis", "N. thoracicus longus", "N. subclavius", "Nn. intercostales"],
  """M. pectoralis major lateral (C5–C7) ve medial (C8–T1) pektoral sinirlerle innerve edilir. Kolu
  addüksiyon ve iç rotasyona getirir; klavikular başı fleksiyon, sternokostal başı ekstansiyon yapar.""",
  e=["m-pectoralis-major", "plexus-brachialis"]),

Q("f", GOG, "A. axillaris'i üç bölüme ayıran kas hangisidir?",
  "M. pectoralis minor",
  ["M. pectoralis major", "M. subscapularis", "M. teres major", "M. coracobrachialis"],
  """A. axillaris 1. kaburganın dış kenarından teres major'un alt kenarına kadar uzanır; m. pectoralis
  minor'un üstündeki kısım 1., arkasındaki 2., altındaki 3. bölümdür. Pectoralis minor ayrıca aksiller
  lenf nodu düzeylerini ayırır.""",
  e=["m-pectoralis-minor", "a-axillaris"]),

Q("t", GOG, "İnterkostal ven, arter ve sinir hangi kas katmanları arasında seyreder?",
  "M. intercostalis internus ile m. intercostalis intimus arasında",
  ["M. intercostalis externus ile internus arasında", "Deri ile m. intercostalis externus arasında",
   "M. intercostalis intimus ile parietal plevra arasında", "M. serratus anterior ile m. intercostalis externus arasında"],
  """Damar-sinir paketi kaburganın alt kenarındaki sulcus costae'de iç ve en iç interkostal kaslar arasında
  yer alır; sıralama yukarıdan aşağı ven, arter, sinirdir (VAN).""",
  e=["mm-intercostales", "n-intercostales", "costae"]),

Q("f", GOG, "Hiatus aorticus'tan geçen yapılar hangileridir?",
  "Aorta, ductus thoracicus ve v. azygos",
  ["Özofagus ve truncus vagalis anterior ile posterior", "V. cava inferior ve n. phrenicus dexter",
   "Aorta, n. vagus ve truncus sympathicus", "Özofagus, aorta ve ductus thoracicus"],
  """Diyaframın üç büyük açıklığı: foramen venae cavae (T8) – VCI ve sağ n. phrenicus'un dalları;
  hiatus oesophageus (T10) – özofagus ve vagal gövdeler; hiatus aorticus (T12) – aorta, ductus
  thoracicus ve çoğunlukla v. azygos. Aort hiatusu aslında diyaframın arkasında, kruslar arasındadır.""",
  e=["diaphragma", "aorta", "ductus-thoracicus", "v-azygos"]),

Q("fv", GOG, """Trafik kazası sonrası dalak rüptürü olan hasta sol omuz ucunda ağrı tarifliyor (Kehr belirtisi).
Bu yansıyan ağrıyı ileten sinir hangisidir?""",
  "N. phrenicus (C3–C5)",
  ["N. vagus", "Nn. splanchnici majores", "N. intercostalis 10", "N. accessorius"],
  """Diyaframın merkezî kısmının ve altındaki peritonun duyusu n. phrenicus ile C3–C5 segmentlerine taşınır.
  Omuz derisi de C4 dermatomundandır; diyafram altındaki kan peritonu tahriş edince ağrı omuz ucuna
  yansır.""",
  e=["diaphragma", "n-phrenicus", "splen"]),

Q("t", GOG, "Diyafram ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Motor innervasyonunun önemli bir kısmı alt interkostal sinirlerdendir.",
  ["Kasılınca kubbeleri aşağı iner ve göğüs boşluğu genişler.", "Sağ kubbe karaciğer nedeniyle soldan daha yüksektir.",
   "Crus dextrum özofagus hiatusunu çevreler.", "Lig. arcuatum mediale m. psoas major'un üzerinden geçer."],
  """Diyaframın tek motor siniri n. phrenicus'tur (C3–C5). Alt interkostal sinirler yalnızca çevre
  kısmının duyusunu alır. Sağ crus daha büyüktür ve özofagus hiatusunu çevreleyen lifler çoğunlukla ondan
  gelir.""",
  e=["diaphragma", "n-phrenicus"]),

# ------------------------------------------------------------------ Karın
Q("t", KAR, "Linea arcuata'nın altında rectus kılıfı için aşağıdakilerden hangisi doğrudur?",
  "Üç yassı kasın aponevrozları kasın önünden geçer; arka duvarı yalnızca fascia transversalis yapar.",
  ["İnternal oblik aponevrozu ikiye ayrılarak kası sarar.", "Kılıfın ön duvarı bulunmaz.",
   "Transversus abdominis aponevrozu kasın arkasından geçer.", "Arka duvarı m. quadratus lumborum yapar."],
  """Göbekle symphysis arasındaki yaklaşık orta noktada (linea arcuata) arka kılıf sona erer. Bu düzeyin
  altında tüm aponevrozlar öne geçer; rectus kası arkada yalnızca fascia transversalis ve periton ile
  örtülüdür. A. epigastrica inferior kılıfa bu çizginin hemen altında girer.""",
  e=["m-rectus-abdominis", "m-transversus-abdominis", "m-obliquus-internus"]),

Q("tv", KAR, """Kasık fıtığı ameliyatında fıtık kesesinin a. ve v. epigastrica inferior'un lateralinden, derin
inguinal halkadan girerek spermatik kord içinde skrotuma indiği görülüyor. Bu fıtık hangisidir?""",
  "İndirekt inguinal herni",
  ["Direkt inguinal herni", "Femoral herni", "Spigel hernisi", "Obturator hernisi"],
  """İndirekt herni derin halkadan (epigastrik damarların lateralinden) girer, kanal boyunca ilerler ve
  skrotuma inebilir; genellikle açık kalmış processus vaginalis'e bağlıdır (konjenital). Direkt herni
  epigastrik damarların medialinden, Hesselbach üçgeninden kanalın arka duvarını iterek çıkar.""",
  e=["lig-inguinale", "m-obliquus-externus", "m-transversus-abdominis"]),

Q("t", KAR, "Hesselbach (inguinal) üçgeninin sınırları hangileridir?",
  "A. epigastrica inferior, m. rectus abdominis'in lateral kenarı ve lig. inguinale",
  ["Lig. inguinale, m. sartorius ve m. adductor longus", "A. epigastrica superior, linea alba ve lig. lacunare",
   "Funiculus spermaticus, lig. inguinale ve linea semilunaris", "M. latissimus dorsi, m. obliquus externus ve crista iliaca"],
  """Hesselbach üçgeni karın ön duvarının iç yüzünde, direkt inguinal hernilerin çıktığı zayıf bölgedir.
  Lateralinde a. epigastrica inferior, medialinde rectus kasının dış kenarı, altta lig. inguinale vardır.""",
  e=["lig-inguinale", "m-rectus-abdominis"]),

Q("t", KAR, "M. cremaster hangi kastan köken alır ve hangi sinirle innerve edilir?",
  "M. obliquus internus abdominis – n. genitofemoralis'in ramus genitalis'i",
  ["M. obliquus externus abdominis – n. ilioinguinalis", "M. transversus abdominis – n. iliohypogastricus",
   "M. rectus abdominis – n. subcostalis", "M. obliquus internus abdominis – n. pudendus"],
  """Kremaster lifleri iç oblik kasın alt kenarından ayrılarak spermatik kordu sarar. Uyluğun iç yüzüne
  dokunulunca testisin yükselmesi (kremaster refleksi) n. genitofemoralis (L1–L2) üzerinden olur.""",
  e=["m-obliquus-internus", "testis"]),

Q("f", KAR, "Falx inguinalis'i (conjoint tendon) oluşturan kaslar hangileridir?",
  "M. obliquus internus ve m. transversus abdominis",
  ["M. obliquus externus ve m. obliquus internus", "M. rectus abdominis ve m. pyramidalis",
   "M. transversus abdominis ve m. quadratus lumborum", "M. obliquus externus ve m. rectus abdominis"],
  """İç oblik ve transversus kaslarının alt aponevrotik lifleri birleşerek pecten ossis pubis'e tutunur ve
  inguinal kanalın medial arka duvarını güçlendirir. Direkt hernilerin önlenmesinde önemlidir.""",
  e=["m-obliquus-internus", "m-transversus-abdominis"]),

Q("f", KAR, "Lig. inguinale hangi yapının kıvrılmış alt kenarıdır?",
  "M. obliquus externus abdominis'in aponevrozu",
  ["M. transversus abdominis'in aponevrozu", "Fascia transversalis", "M. obliquus internus'un kas lifleri", "Fascia lata"],
  """Dış oblik kasın aponevrozu SIAS ile tuberculum pubicum arasında içe kıvrılarak lig. inguinale'yi yapar.
  Aynı aponevrozdaki üçgen açıklık yüzeyel inguinal halkadır.""",
  e=["lig-inguinale", "m-obliquus-externus"]),

Q("t", KAR, "Anorektal açıyı koruyarak fekal kontinansa önemli katkı sağlayan kas hangisidir?",
  "M. puborectalis",
  ["M. iliococcygeus", "M. coccygeus", "M. sphincter ani internus", "M. obturatorius internus"],
  """Levator ani'nin parçası olan puborectalis rektumun arkasında U biçimli bir askı yapar ve anorektal
  bileşkeyi öne çekerek yaklaşık 90°'lik açı oluşturur. Defekasyonda gevşeyerek açıyı düzleştirir.""",
  e=["diaphragma-pelvis", "rectum"]),

Q("f", KAR, "M. quadratus lumborum'un temel işlevlerinden biri hangisidir?",
  "Derin inspirasyonda 12. kaburgayı sabitlemek",
  ["Kalçayı fleksiyona getirmek", "Karın içi basıncı azaltmak", "Pelvisi öne eğmek", "Gövdeyi karşı tarafa döndürmek"],
  """Quadratus lumborum crista iliaca'dan 12. kaburga ve lomber transvers çıkıntılara uzanır. 12. kaburgayı
  aşağıda tutarak diyaframın etkili kasılmasına yardım eder; tek taraflı kasılınca gövdeyi yana eğer.""",
  e=["m-quadratus-lumborum", "costae"]),

# ------------------------------------------------------------------ Omuz
Q("f", OMZ, "Kol abdüksiyonunun ilk 15°'sini başlatan kas hangisidir?",
  "M. supraspinatus",
  ["M. deltoideus", "M. trapezius", "M. serratus anterior", "M. infraspinatus"],
  """Supraspinatus humerus başını cavitas glenoidalis'e bastırırken abdüksiyonu başlatır. 15°–90° arasında
  deltoid baskındır; 90°'nin üzeri skapulanın trapezius ve serratus anterior ile yukarı dönmesini gerektirir.""",
  e=["m-supraspinatus", "m-deltoideus"]),

Q("f", OMZ, "Kolu dış rotasyona getiren rotator manşet kasları hangileridir?",
  "M. infraspinatus ve m. teres minor",
  ["M. subscapularis ve m. teres major", "M. supraspinatus ve m. subscapularis",
   "M. latissimus dorsi ve m. teres major", "M. pectoralis major ve m. subscapularis"],
  """Infraspinatus (n. suprascapularis) ve teres minor (n. axillaris) tuberculum majus'un arka yüzlerine
  tutunur ve kolun başlıca dış rotatörleridir. Subscapularis, teres major, latissimus ve pectoralis major
  iç rotasyon yapar.""",
  e=["m-infraspinatus", "m-teres-minor"]),

Q("t", OMZ, "Boşluk kuadrangülerden (spatium quadrangulare) geçen yapılar hangileridir?",
  "N. axillaris ve a. circumflexa humeri posterior",
  ["N. radialis ve a. profunda brachii", "A. circumflexa scapulae", "N. suprascapularis ve a. suprascapularis",
   "N. thoracodorsalis ve a. thoracodorsalis"],
  """Kuadrangüler boşluğu teres minor (üst), teres major (alt), tricepsin uzun başı (iç) ve humerusun
  collum chirurgicum'u (dış) sınırlar. Üçgen boşluktan a. circumflexa scapulae, üçgen aralıktan
  n. radialis ve a. profunda brachii geçer.""",
  e=["m-teres-minor", "m-teres-major", "n-axillaris"]),

Q("t", OMZ, "Kolun 90°'nin üzerinde abdüksiyonu (elevasyon) için skapulayı yukarı döndüren kaslar hangileridir?",
  "M. trapezius (üst ve alt lifler) ve m. serratus anterior",
  ["M. rhomboideus major ve minor", "M. levator scapulae ve m. pectoralis minor",
   "M. deltoideus ve m. supraspinatus", "M. latissimus dorsi ve m. teres major"],
  """Skapulanın yukarı rotasyonu glenoid fossayı yukarı yöneltir. Trapezius'un üst ve alt lifleri ile
  serratus anterior'un alt lifleri bir kuvvet çifti oluşturur. Rhomboidler, levator scapulae ve
  pectoralis minor skapulayı aşağı döndürür.""",
  e=["m-trapezius", "m-serratus-anterior", "scapula"]),

Q("tv", OMZ, """Omuz ağrısı olan hastaya elinin sırtını beline koyması ve elini sırtından uzaklaştırması
söyleniyor; hasta bunu yapamıyor (lift-off testi pozitif). Hangi kasın yırtığı düşünülür?""",
  "M. subscapularis",
  ["M. supraspinatus", "M. infraspinatus", "M. teres minor", "M. teres major"],
  """Lift-off testinde kol iç rotasyondadır ve elin sırttan uzaklaştırılması ek iç rotasyon gerektirir;
  bu, subscapularis'in işlevidir. Supraspinatus 'boş kutu' (Jobe), infraspinatus ise dış rotasyona
  karşı direnç testleriyle değerlendirilir.""",
  e=["m-subscapularis"]),

Q("f", OMZ, "M. teres major'u innerve eden sinir hangisidir?",
  "N. subscapularis inferior",
  ["N. axillaris", "N. suprascapularis", "N. thoracodorsalis", "N. dorsalis scapulae"],
  """Teres major arka korddan çıkan alt subskapular sinirle innerve edilir; latissimus dorsi ile birlikte
  kolu addüksiyon, iç rotasyon ve ekstansiyona getirir. Rotator manşetin parçası değildir. Teres minor
  ise n. axillaris'ten innervasyon alır.""",
  e=["m-teres-major", "plexus-brachialis"]),

Q("f", OMZ, "M. deltoideus'un temel işlevi hangisidir?",
  "Kolu 15°–90° arasında abdüksiyona getirmek",
  ["Kolu iç rotasyona getirmek", "Abdüksiyonu başlatmak (0–15°)", "Skapulayı yukarı döndürmek", "Dirseği bükmek"],
  """Deltoidin orta lifleri güçlü bir abduktördür; ön lifler fleksiyon ve iç rotasyon, arka lifler
  ekstansiyon ve dış rotasyon yapar. Kas n. axillaris ile innerve edilir ve kas içi enjeksiyon için
  akromiyonun yaklaşık 3–5 cm altı kullanılır.""",
  e=["m-deltoideus", "n-axillaris"]),

# ------------------------------------------------------------------ Kol
Q("f", KOL, "Dirsek bükülü iken önkolun en güçlü supinatörü hangi kastır?",
  "M. biceps brachii",
  ["M. supinator", "M. brachioradialis", "M. brachialis", "M. pronator teres"],
  """Biceps tuberositas radii'ye tutunduğu için dirsek 90° bükülüyken çok güçlü supinasyon yapar (vida
  sıkma hareketi). Dirsek düzken supinasyonu daha çok m. supinator yapar.""",
  e=["m-biceps-brachii", "m-supinator"]),

Q("f", KOL, "M. coracobrachialis'i delip geçen sinir hangisidir?",
  "N. musculocutaneus",
  ["N. medianus", "N. ulnaris", "N. radialis", "N. axillaris"],
  """N. musculocutaneus lateral korddan çıkar, coracobrachialis'i deler, biceps ile brachialis arasında
  ilerler ve önkolda n. cutaneus antebrachii lateralis olarak sonlanır.""",
  e=["m-coracobrachialis", "n-musculocutaneus"]),

Q("f", KOL, "Dirsek ekleminin asıl (en güçlü) fleksörü hangisidir?",
  "M. brachialis",
  ["M. biceps brachii", "M. brachioradialis", "M. pronator teres", "M. coracobrachialis"],
  """Brachialis önkolun her pozisyonunda dirseği büken 'asıl fleksör'dür; ulnaya tutunduğu için önkolun
  rotasyonundan etkilenmez. Çoğunlukla n. musculocutaneus, küçük bir dış bölümü n. radialis ile
  innerve edilir.""",
  e=["m-brachialis", "n-musculocutaneus"]),

Q("t", KOL, "Triseps tendon refleksi hangi spinal segmenti en çok değerlendirir?",
  "C7",
  ["C5", "C6", "C8", "T1"],
  """Biseps refleksi C5–C6 (özellikle C5), brakioradialis refleksi C6, triseps refleksi C7 (C6–C8)
  segmentini değerlendirir. C6–C7 disk hernisinde (C7 kökü) triseps refleksi azalır.""",
  e=["m-triceps-brachii", "n-radialis"]),

Q("fv", KOL, """Ağır kaldıran 55 yaşında erkek omzunun önünde 'kopma' hissediyor; dirseği bükünce kolunun
alt ön kısmında belirgin bir kitle (Popeye belirtisi) oluşuyor. Yırtılan yapı hangisidir?""",
  "M. biceps brachii'nin uzun başının tendonu",
  ["M. biceps brachii'nin distal tendonu", "M. brachialis", "M. coracobrachialis", "M. triceps brachii'nin uzun başı"],
  """Biceps uzun baş tendonu sulcus intertubercularis'te sürtünme ve dejenerasyonla yırtılabilir; kas
  karnı aşağı kayarak kitle oluşturur. Kısa baş ve brachialis sağlam olduğundan dirsek fleksiyonu
  belirgin bozulmaz.""",
  e=["m-biceps-brachii"]),

Q("f", KOL, "Fossa cubitalis'te dıştan içe doğru yapıların sıralaması hangisidir?",
  "Biceps tendonu – a. brachialis – n. medianus",
  ["N. medianus – a. brachialis – biceps tendonu", "A. brachialis – biceps tendonu – n. medianus",
   "Biceps tendonu – n. medianus – a. brachialis", "N. radialis – n. medianus – a. brachialis"],
  """Kübital çukurda lateralden mediale biseps tendonu, a. brachialis ve n. medianus sıralanır.
  N. radialis ise brachioradialis'in altında daha derin ve dış tarafta yer alır. Tansiyon ölçümünde
  stetoskop biceps tendonunun iç yanına konur.""",
  e=["m-biceps-brachii", "a-brachialis", "n-medianus"]),

# ------------------------------------------------------------------ Önkol
Q("t", ONK, "N. medianus'un önkola girerken genellikle iki başı arasından geçtiği kas hangisidir?",
  "M. pronator teres",
  ["M. flexor carpi radialis", "M. supinator", "M. flexor carpi ulnaris", "M. brachioradialis"],
  """N. medianus pronator teres'in humeral ve ulnar başları arasından geçer; burada sıkışması pronator
  sendromuna yol açar. N. ulnaris ise FCU'nun iki başı arasından, n. radialis'in derin dalı
  supinator'dan geçer.""",
  e=["m-pronator-teres", "n-medianus"]),

Q("t", ONK, "M. flexor digitorum profundus'un 4. ve 5. parmaklara giden bölümünü innerve eden sinir hangisidir?",
  "N. ulnaris",
  ["N. interosseus anterior", "N. medianus'un ana gövdesi", "N. radialis", "N. musculocutaneus"],
  """FDP çift innervasyonludur: 2. ve 3. parmaklara giden lateral yarısı n. medianus'un n. interosseus
  anterior dalı, 4. ve 5. parmaklara giden medial yarısı n. ulnaris ile innerve edilir.""",
  e=["m-flexor-digitorum-profundus", "n-ulnaris"]),

Q("tv", ONK, """Önkol kırığı sonrası hasta başparmağı ile işaret parmağının ucunu birleştirip 'OK' işareti
yapamıyor; parmak uçlarını bükemediği için tırnak uçları yerine parmak pulpaları temas ediyor. Duyu
kaybı yok. Yaralanan sinir hangisidir?""",
  "N. interosseus anterior",
  ["N. ulnaris", "N. radialis'in yüzeyel dalı", "N. medianus'un ramus recurrens'i", "N. interosseus posterior"],
  """N. interosseus anterior n. medianus'un saf motor dalıdır: FPL, FDP'nin lateral yarısı ve pronator
  quadratus'u innerve eder. Felcinde başparmak ve işaret parmağının distal falankslarını bükme kaybolur;
  duyusal dalı olmadığından his kaybı olmaz.""",
  e=["m-flexor-pollicis-longus", "m-flexor-digitorum-profundus", "n-medianus"]),

Q("f", ONK, "Önkolda yer almasına karşın dirseği yarı pronasyon pozisyonunda büken ve n. radialis ile innerve edilen kas hangisidir?",
  "M. brachioradialis",
  ["M. pronator teres", "M. flexor carpi radialis", "M. anconeus", "M. extensor carpi ulnaris"],
  """Brachioradialis ekstansör (arka) kompartmanın kasıdır ve n. radialis'ten innervasyon alır; ancak
  dirsek ekleminin önünden geçtiği için özellikle önkol orta pozisyondayken dirseği büker.""",
  e=["m-brachioradialis", "n-radialis"]),

Q("t", ONK, "Aşağıdaki yapılardan hangisi karpal tünelden geçmez?",
  "M. palmaris longus tendonu",
  ["M. flexor digitorum superficialis tendonları", "M. flexor digitorum profundus tendonları",
   "M. flexor pollicis longus tendonu", "N. medianus"],
  """Karpal tünelden n. medianus ile birlikte dokuz tendon (4 FDS, 4 FDP, 1 FPL) geçer. Palmaris longus
  tendonu retinakulum flexorum'un önünden geçerek aponeurosis palmaris'e katılır; kişilerin yaklaşık
  %15'inde bulunmaz ve tendon grefti olarak kullanılır.""",
  e=["m-palmaris-longus", "n-medianus"]),

Q("tv", ONK, """Radius başı kırığı sonrası hasta parmaklarını MKF eklemlerden uzatamıyor. El bileğini
kaldırabiliyor ancak bilek radial tarafa sapıyor. Elde duyu kaybı yok. Yaralanan sinir hangisidir?""",
  "N. interosseus posterior (n. radialis'in derin dalı)",
  ["N. radialis'in ana gövdesi (sulcus nervi radialis'te)", "N. radialis'in yüzeyel dalı", "N. ulnaris", "N. interosseus anterior"],
  """Derin dal supinator'u (Frohse arkı) geçerek n. interosseus posterior adını alır ve parmak ekstansörleri
  ile ECU'yu innerve eder. ECRL ise dal ayrılmadan önce innerve edildiği için korunur; bilek ekstansiyonu
  radiale sapar. Duyusal yüzeyel dal etkilenmediğinden his kaybı olmaz.""",
  e=["m-supinator", "m-extensor-digitorum", "n-radialis"]),

Q("fv", ONK, """Tenis oynayan 40 yaşındaki hastada epicondylus lateralis üzerinde hassasiyet ve dirençli el bileği
ekstansiyonunda ağrı var. En sık etkilenen kasın başlangıç tendonu hangisidir?""",
  "M. extensor carpi radialis brevis",
  ["M. flexor carpi radialis", "M. brachioradialis", "M. anconeus", "M. pronator teres"],
  """Lateral epikondilit (tenis dirseği) ortak ekstansör orijinin, en çok ECRB tendonunun aşırı kullanıma
  bağlı dejenerasyonudur. Medial epikondilit (golfçü dirseği) ise ortak fleksör-pronator orijini tutar.""",
  e=["mm-extensores-carpi-radiales", "humerus"]),

Q("t", ONK, "Tabakiyer anatomiğin (enfiyecinin çukuru) ulnar (iç) sınırını yapan tendon hangisidir?",
  "M. extensor pollicis longus",
  ["M. abductor pollicis longus", "M. extensor pollicis brevis", "M. extensor carpi radialis longus", "M. extensor indicis"],
  """Tabakiyerin radial sınırını APL ve EPB, ulnar sınırını EPL tendonları yapar. Tabanında scaphoid ve
  trapezium, içinde a. radialis bulunur. EPL tendonu tuberculum dorsale radii (Lister) etrafından
  yön değiştirir.""",
  e=["mm-pollicis-longi", "os-scaphoideum", "a-radialis"]),

Q("fv", ONK, """Yeni doğum yapmış bir anne, bebeğini kucaklarken el bileğinin radial tarafında ağrı tarifliyor.
Başparmak avuca alınıp bilek ulnar deviasyona getirilince ağrı artıyor (Finkelstein testi). Etkilenen
tendonlar hangileridir?""",
  "M. abductor pollicis longus ve m. extensor pollicis brevis",
  ["M. extensor pollicis longus ve m. extensor indicis", "M. flexor pollicis longus ve m. flexor carpi radialis",
   "M. extensor carpi radialis longus ve brevis", "M. extensor digitorum ve m. extensor digiti minimi"],
  """De Quervain tenosinoviti, birinci dorsal kompartmanda (radius stiloid çıkıntısı üzerinde) birlikte
  geçen APL ve EPB tendonlarının kılıf inflamasyonudur.""",
  e=["mm-pollicis-longi", "radius"]),

Q("f", ONK, "M. flexor carpi ulnaris'in innervasyonu ve işlevi hangisidir?",
  "N. ulnaris – el bileğinin fleksiyonu ve addüksiyonu (ulnar deviasyon)",
  ["N. medianus – el bileğinin fleksiyonu ve abdüksiyonu", "N. ulnaris – el bileğinin ekstansiyonu",
   "N. radialis – el bileğinin addüksiyonu", "N. medianus – önkolun pronasyonu"],
  """FCU önkol fleksörleri arasında n. ulnaris ile innerve edilen tek yüzeyel kastır; os pisiforme
  üzerinden hamatum ve 5. metakarpa tutunur. FCR ise n. medianus ile innerve edilir ve bileği radiale
  saptırır.""",
  e=["m-flexor-carpi-ulnaris", "n-ulnaris"]),

# ------------------------------------------------------------------ El
Q("t", EL, "Başparmak kaslarından hangisi n. ulnaris ile innerve edilir?",
  "M. adductor pollicis",
  ["M. abductor pollicis brevis", "M. opponens pollicis", "M. flexor pollicis brevis'in yüzeyel başı", "M. flexor pollicis longus"],
  """Tenar kaslar (abductor pollicis brevis, opponens pollicis, FPB yüzeyel başı) n. medianus'un ramus
  recurrens'i ile innerve edilir. M. adductor pollicis ve FPB'nin derin başı n. ulnaris'in derin dalını
  alır.""",
  e=["mm-thenares", "n-ulnaris"]),

Q("f", EL, "Mm. lumbricales'in eldeki işlevi hangisidir?",
  "MKF eklemleri bükmek ve interfalangeal eklemleri uzatmak",
  ["MKF eklemleri uzatmak ve interfalangeal eklemleri bükmek", "Parmakları birbirinden uzaklaştırmak",
   "Parmakları birbirine yaklaştırmak", "Yalnızca distal falanksları bükmek"],
  """Lumbrikaller FDP tendonlarından başlar ve ekstansör kayışın radial kenarına tutunur. Bu sayede MKF
  eklemlerde fleksiyon, İF eklemlerde ekstansiyon yaparlar (yazı yazma pozisyonu). 1. ve 2. lumbrikal
  n. medianus, 3. ve 4. lumbrikal n. ulnaris ile innerve edilir.""",
  e=["mm-lumbricales-manus", "m-flexor-digitorum-profundus"]),

Q("tv", EL, """Hastadan başparmağı ile işaret parmağı arasında bir kâğıdı sıkıca tutması isteniyor; kâğıt
çekilince hasta başparmağının uç eklemini bükerek tutmaya çalışıyor (Froment belirtisi). Güçsüz kas
ve hasarlı sinir hangisidir?""",
  "M. adductor pollicis – n. ulnaris",
  ["M. flexor pollicis longus – n. interosseus anterior", "M. opponens pollicis – n. medianus",
   "M. abductor pollicis longus – n. radialis", "M. flexor pollicis brevis – n. medianus"],
  """Addüktör pollisis güçsüz olduğunda hasta kâğıdı tutmak için n. medianus'la innerve edilen FPL'yi
  kullanır ve başparmağın İF eklemi bükülür. Bu, n. ulnaris hasarının klasik bulgusudur.""",
  e=["mm-thenares", "n-ulnaris"]),

Q("t", EL, "Karpal tünel sendromunda avuç içinin dış yarısının duyusu neden genellikle korunur?",
  "N. medianus'un ramus palmaris'i karpal tünele girmeden ayrılır ve retinakulumun önünden geçer.",
  ["Avuç içi derisi yalnızca n. ulnaris ile innerve edilir.", "Avuç içinin duyusunu n. radialis'in yüzeyel dalı alır.",
   "Duyusal lifler sıkışmaya karşı dirençlidir.", "Avuç içi derisi n. musculocutaneus ile innerve edilir."],
  """Palmar kutanöz dal bileğin birkaç santimetre üstünde ayrılır ve tüneli kullanmaz. Bu nedenle karpal
  tünel sendromunda his kaybı parmaklarla (lateral 3,5 parmağın palmar yüzü) sınırlıdır; avuç içi
  tutulmuşsa lezyon daha proksimaldedir.""",
  e=["n-medianus", "ossa-carpi"]),

Q("t", EL, "Mm. interossei palmares ve dorsales için aşağıdakilerden hangisi doğrudur?",
  "Palmar interosseöz kaslar parmakları addüksiyona, dorsal interosseöz kaslar abdüksiyona getirir.",
  ["Tümü n. medianus ile innerve edilir.", "Dorsal interosseöz kaslar parmakları addüksiyona getirir.",
   "Orta parmağın ekseni olan 4. parmaktır.", "İnterfalangeal eklemleri bükerler."],
  """'PAD–DAB': Palmar ADdüksiyon, Dorsal ABdüksiyon. Hareketler orta parmak eksenine göre tanımlanır.
  Tüm interosseöz kaslar n. ulnaris'in derin dalıyla innerve edilir; lumbrikaller gibi MKF eklemi büker,
  İF eklemleri uzatırlar.""",
  e=["mm-interossei-manus", "n-ulnaris"]),

Q("t", EL, """N. ulnaris'in dirsek düzeyinde yaralandığı hastada pençe el deformitesi, bilek düzeyinde
yaralandığı hastaya göre neden daha hafiftir?""",
  "Dirsekte FDP'nin ulnar bölümü de felç olduğundan 4–5. parmakların İF fleksiyonu azalır.",
  ["Dirsekte lumbrikallerin tamamı korunur.", "Bilekte n. medianus da etkilenir.",
   "Dirsekte interosseöz kaslar korunur.", "Bilek düzeyinde ekstansörler felç olur."],
  """Pençe elde MKF eklemler hiperekstansiyon, İF eklemler fleksiyondadır; fleksiyonu FDP sağlar. Yüksek
  (dirsek) lezyonda FDP'nin ulnar yarısı da felçli olduğundan pençeleşme azdır. Bu durum 'ulnar paradoks'
  olarak bilinir.""",
  e=["m-flexor-digitorum-profundus", "mm-interossei-manus", "n-ulnaris"]),

# ------------------------------------------------------------------ Kalça
Q("fv", KLC, """Kalça cerrahisi sonrası hasta düz zeminde yürüyebiliyor; ancak oturduğu yerden kalkmakta
ve merdiven çıkmakta zorlanıyor. Hangi kas ve sinir etkilenmiştir?""",
  "M. gluteus maximus – n. gluteus inferior",
  ["M. gluteus medius – n. gluteus superior", "M. iliopsoas – n. femoralis",
   "M. quadriceps femoris – n. femoralis", "M. biceps femoris – n. ischiadicus"],
  """Gluteus maximus kalçanın güçlü ekstansörüdür ve özellikle fleksiyondan ekstansiyona geçerken (oturduğu
  yerden kalkma, merdiven çıkma, koşma) devreye girer. Normal yürümede katkısı azdır.""",
  e=["m-gluteus-maximus", "plexus-sacralis"]),

Q("tv", KLC, """Sağ bacağının üzerinde dururken hastanın pelvisinin sol tarafı aşağı düşüyor (pozitif
Trendelenburg belirtisi). Lezyon hangisidir?""",
  "Sağ n. gluteus superior",
  ["Sol n. gluteus superior", "Sağ n. gluteus inferior", "Sol n. femoralis", "Sağ n. obturatorius"],
  """Tek ayak üzerinde dururken, o taraftaki gluteus medius ve minimus pelvisi yatay tutar. Sağ n. gluteus
  superior felcinde sağ bacakta dururken desteklenmeyen sol pelvis düşer. Hasta yürürken gövdesini
  felçli tarafa eğerek bunu dengeler.""",
  e=["m-gluteus-medius", "m-gluteus-minimus"]),

Q("fv", KLC, "Gluteal bölgeye kas içi enjeksiyon için güvenli bölge hangisidir ve neden?",
  "Üst dış kadran; n. ischiadicus'tan uzak olduğu için",
  ["Alt iç kadran; kas kitlesi en kalın olduğu için", "Alt dış kadran; büyük damarlardan uzak olduğu için",
   "Üst iç kadran; n. gluteus superior'dan uzak olduğu için", "Tam orta nokta; kas tabakası en ince olduğu için"],
  """N. ischiadicus gluteal bölgenin alt iç kısmından, piriformisin altından çıkarak trochanter major ile
  tuber ischiadicum arasından aşağı iner. Üst dış kadran (veya ventrogluteal bölge) bu nedenle tercih edilir.""",
  e=["m-gluteus-maximus", "m-gluteus-medius", "n-ischiadicus"]),

Q("t", KLC, "Foramen ischiadicum majus'un m. piriformis'in üstünde kalan bölümünden (suprapiriform) geçen sinir hangisidir?",
  "N. gluteus superior",
  ["N. gluteus inferior", "N. ischiadicus", "N. pudendus", "N. cutaneus femoris posterior"],
  """Suprapiriform aralıktan yalnızca n. gluteus superior ve a./v. glutea superior geçer. İnfrapiriform
  aralıktan n. gluteus inferior, n. ischiadicus, n. cutaneus femoris posterior, n. pudendus, a. pudenda
  interna ve kısa rotatorların sinirleri geçer.""",
  e=["mm-rotatores-coxae", "plexus-sacralis"]),

Q("fv", KLC, """Sağ alt kadran ağrısı olan hastada, sol yanına yatırılıp sağ kalçası pasif ekstansiyona
getirilince ağrı artıyor. Bu bulgu inflame apendiksin hangi kas üzerinde olduğunu düşündürür?""",
  "M. iliopsoas (retroçekal apandisit)",
  ["M. obturatorius internus", "M. quadratus lumborum", "M. rectus abdominis", "M. gluteus medius"],
  """Psoas belirtisi: inflame retroçekal apendiks psoas kasının fasyasıyla temas eder; kalçanın
  ekstansiyonu kası gerer ve ağrıyı artırır. Obturator belirtisi ise pelvik apandisitte kalça
  fleksiyon ve iç rotasyonuyla ağrı oluşmasıdır.""",
  e=["m-iliopsoas", "appendix-vermiformis"]),

Q("f", KLC, "M. tensor fasciae latae'nin innervasyonu ve işlevi hangisidir?",
  "N. gluteus superior – tractus iliotibialis'i gererek kalçayı fleksiyon ve abdüksiyona getirir",
  ["N. femoralis – dizi ekstansiyona getirir", "N. gluteus inferior – kalçayı ekstansiyona getirir",
   "N. obturatorius – kalçayı addüksiyona getirir", "N. ischiadicus – dizi fleksiyona getirir"],
  """TFL, gluteus medius ve minimus ile aynı sinirden (n. gluteus superior) innervasyon alır. Tractus
  iliotibialis üzerinden dizin dış yanını da stabilize eder; aşırı gerginliği iliotibial bant
  sendromuna yol açar.""",
  e=["m-tensor-fasciae-latae", "tractus-iliotibialis"]),

# ------------------------------------------------------------------ Uyluk
Q("f", UYL, "Vücudun en uzun kası olan ve 'terzi kası' olarak da bilinen kas hangisidir?",
  "M. sartorius",
  ["M. gracilis", "M. rectus femoris", "M. semitendinosus", "M. adductor magnus"],
  """Sartorius SIAS'tan başlar, uyluğu çaprazlayarak tibianın iç yüzüne (pes anserinus) tutunur. Kalçayı
  fleksiyon, abdüksiyon ve dış rotasyona, dizi fleksiyona getirir (bağdaş kurma). N. femoralis ile
  innerve edilir ve femoral üçgenin dış sınırıdır.""",
  e=["m-sartorius", "n-femoralis"]),

Q("f", UYL, "Quadriceps femoris'in hem kalçayı büken hem de dizi uzatan başı hangisidir?",
  "M. rectus femoris",
  ["M. vastus lateralis", "M. vastus medialis", "M. vastus intermedius", "M. articularis genus"],
  """Rectus femoris SIAİ ve acetabulum'un üst kenarından başladığı için kalça eklemini de çaprazlar; diğer
  üç vastus yalnızca femurdan başlar ve sadece dizi uzatır. Tüm quadriceps n. femoralis ile innerve edilir.""",
  e=["m-quadriceps-femoris", "n-femoralis"]),

Q("t", UYL, "Çift innervasyon alan m. adductor magnus'un 'hamstring bölümü' hangi sinirle innerve edilir?",
  "N. ischiadicus'un tibial bölümü",
  ["N. obturatorius'un arka dalı", "N. femoralis", "N. ischiadicus'un fibular bölümü", "N. gluteus inferior"],
  """Adductor magnus'un addüktör bölümü n. obturatorius, tuber ischiadicum'dan başlayan hamstring bölümü
  n. ischiadicus'un tibial bölümü ile innerve edilir. İki bölüm arasındaki açıklık hiatus adductorius'tur.""",
  e=["mm-adductores", "n-obturatorius", "n-ischiadicus"]),

Q("t", UYL, "Hiatus adductorius'tan geçerek fossa poplitea'ya ulaşan yapılar hangileridir?",
  "A. ve v. femoralis",
  ["N. saphenus", "N. obturatorius'un ön dalı", "A. profunda femoris", "V. saphena magna"],
  """A. ve v. femoralis canalis adductorius'u izledikten sonra adductor magnus'taki açıklıktan geçer ve
  a./v. poplitea adını alır. N. saphenus ise kanaldan çıkıp hiatusa girmeden dizin iç yanına yönelir.""",
  e=["mm-adductores", "a-femoralis", "a-poplitea"]),

Q("t", UYL, "Aşağıdakilerden hangisi canalis adductorius (Hunter kanalı) içinde bulunmaz?",
  "V. saphena magna",
  ["A. femoralis", "V. femoralis", "N. saphenus", "M. vastus medialis'e giden sinir"],
  """Addüktör kanalı sartorius'un altında, vastus medialis ile addüktör kaslar arasındadır; içinden
  a. ve v. femoralis, n. saphenus ve vastus medialis'in siniri geçer. V. saphena magna yüzeyel fasyada
  seyreden yüzeyel bir vendir.""",
  e=["m-sartorius", "a-femoralis", "v-saphena-magna"]),

Q("t", UYL, "Hamstring grubunda n. fibularis communis ile innerve edilen kas hangisidir?",
  "M. biceps femoris'in kısa başı",
  ["M. biceps femoris'in uzun başı", "M. semitendinosus", "M. semimembranosus", "M. adductor magnus'un hamstring bölümü"],
  """Hamstring kaslarının çoğu n. ischiadicus'un tibial bölümünü alır. Biceps femoris'in kısa başı
  femurdan (linea aspera) başlar, gerçek bir hamstring değildir ve fibular bölümden innervasyon alır.""",
  e=["m-biceps-femoris", "mm-ischiocrurales", "n-fibularis-communis"]),

Q("f", UYL, "Pes anserinus'u oluşturan tendonlar hangi kaslara aittir?",
  "M. sartorius, m. gracilis ve m. semitendinosus",
  ["M. semimembranosus, m. gracilis ve m. sartorius", "M. biceps femoris, m. semitendinosus ve m. gracilis",
   "M. rectus femoris, m. sartorius ve m. gracilis", "M. adductor magnus, m. gracilis ve m. semitendinosus"],
  """Üç tendon tibianın üst iç yüzünde kaz ayağı biçiminde birleşir ve üç farklı sinirden innervasyon alır:
  sartorius (n. femoralis), gracilis (n. obturatorius), semitendinosus (n. ischiadicus–tibial).
  Altındaki bursanın iltihabı pes anserinus bursitidir.""",
  e=["m-sartorius", "m-gracilis", "mm-ischiocrurales"]),

Q("t", UYL, "Hem n. femoralis'ten hem de n. obturatorius'tan innervasyon alabilen uyluk kası hangisidir?",
  "M. pectineus",
  ["M. gracilis", "M. adductor longus", "M. sartorius", "M. vastus medialis"],
  """Pectineus çoğunlukla n. femoralis ile, sıklıkla ek olarak n. obturatorius (veya aksesuar obturator)
  ile innerve edilir; bu nedenle ön ve iç kompartman arasında geçiş kası sayılır.""",
  e=["m-pectineus", "n-femoralis", "n-obturatorius"]),

Q("f", UYL, "Femoral üçgenin lateral sınırını yapan kas hangisidir?",
  "M. sartorius",
  ["M. adductor longus", "M. iliopsoas", "M. rectus femoris", "M. pectineus"],
  """Femoral üçgen üstte lig. inguinale, dışta sartorius'un iç kenarı, içte adductor longus'un iç kenarı ile
  sınırlıdır. Tabanını iliopsoas, pectineus ve adductor longus yapar; içinde dıştan içe n. femoralis,
  a. femoralis, v. femoralis ve lenfatikler bulunur.""",
  e=["m-sartorius", "trigonum-femorale", "a-femoralis"]),

# ------------------------------------------------------------------ Bacak
Q("f", BCK, "M. tibialis anterior'un innervasyonu ve işlevi hangisidir?",
  "N. fibularis profundus – ayağı dorsifleksiyon ve inversiyona getirir",
  ["N. fibularis superficialis – ayağı eversiyona getirir", "N. tibialis – ayağı plantar fleksiyona getirir",
   "N. fibularis profundus – ayağı eversiyona getirir", "N. tibialis – ayağı inversiyona getirir"],
  """Tibialis anterior bacağın ön kompartmanındaki en güçlü dorsifleksördür ve ayağın iç kenarını kaldırır.
  Ön kompartman kasları n. fibularis profundus ile innerve edilir.""",
  e=["m-tibialis-anterior", "n-fibularis-communis"]),

Q("f", BCK, "M. fibularis longus ve brevis'i innerve eden sinir hangisidir?",
  "N. fibularis superficialis",
  ["N. fibularis profundus", "N. tibialis", "N. suralis", "N. saphenus"],
  """Lateral kompartman kasları (fibularis longus ve brevis) n. fibularis superficialis ile innerve edilir ve
  ayağın başlıca evertörleridir. Bu sinir daha sonra deriyi delerek ayak sırtının büyük kısmının duyusunu
  alır.""",
  e=["m-fibularis-longus", "m-fibularis-brevis", "n-fibularis-communis"]),

Q("tv", BCK, """Dar alçı sonrası bacak ön yüzünde şiddetli ağrı gelişen hastada ayak başparmağını pasif
olarak bükünce ağrı artıyor ve 1. ve 2. parmaklar arasındaki küçük alanda his kaybı var. Hangi
kompartman ve sinir etkilenmiştir?""",
  "Ön kompartman – n. fibularis profundus",
  ["Lateral kompartman – n. fibularis superficialis", "Derin arka kompartman – n. tibialis",
   "Yüzeyel arka kompartman – n. suralis", "Ön kompartman – n. saphenus"],
  """Ön kompartman sendromunda içerideki kaslar (tibialis anterior, EHL, EDL) pasif gerilmeyle ağrır. Bu
  kompartmanın siniri n. fibularis profundus'tur ve deride yalnızca 1. parmak aralığını innerve eder.
  Erken fasyotomi gerekir.""",
  e=["m-tibialis-anterior", "m-extensor-hallucis-longus", "n-fibularis-communis"]),

Q("t", BCK, "Aşil (topuk) refleksi esas olarak hangi spinal segmenti değerlendirir?",
  "S1",
  ["L3", "L4", "L5", "S3"],
  """Aşil refleksi triceps surae ve n. tibialis üzerinden S1 (S1–S2) segmentini test eder. Patella refleksi
  L4 (L3–L4) segmentini değerlendirir. L5'in güvenilir bir refleksi yoktur.""",
  e=["m-triceps-surae", "n-tibialis"]),

Q("f", BCK, "Venöz dönüşe katkısı nedeniyle 'periferik kalp' olarak adlandırılan kas hangisidir?",
  "M. soleus",
  ["M. tibialis anterior", "M. popliteus", "M. fibularis longus", "M. plantaris"],
  """Soleus içinde geniş venöz sinüsler bulunur; kasılınca derin venleri sıkıştırarak kanı yukarı pompalar
  (kas pompası). Uzun süre hareketsiz kalmak bu pompayı devre dışı bırakır ve derin ven trombozu riskini
  artırır.""",
  e=["m-triceps-surae"]),

Q("t", BCK, "Malleolus medialis'in arkasında önden arkaya doğru yapıların sıralaması hangisidir?",
  "M. tibialis posterior, m. flexor digitorum longus, a./v. tibialis posterior, n. tibialis, m. flexor hallucis longus",
  ["M. flexor hallucis longus, n. tibialis, a. tibialis posterior, m. flexor digitorum longus, m. tibialis posterior",
   "M. tibialis posterior, a. tibialis posterior, m. flexor digitorum longus, m. flexor hallucis longus, n. tibialis",
   "M. flexor digitorum longus, m. tibialis posterior, n. tibialis, a. tibialis posterior, m. flexor hallucis longus",
   "N. tibialis, a. tibialis posterior, m. tibialis posterior, m. flexor digitorum longus, m. flexor hallucis longus"],
  """Tarsal tünelde (retinaculum musculorum flexorum altında) önden arkaya sıralama: tibialis posterior,
  FDL, arter ve venler, n. tibialis, FHL. N. tibialis'in burada sıkışması tarsal tünel sendromudur.
  A. tibialis posterior nabzı medial malleol ile topuk arasında alınır.""",
  e=["m-tibialis-posterior", "m-flexor-digitorum-longus", "m-flexor-hallucis-longus", "n-tibialis"]),

Q("fv", BCK, """Basketbolda sıçrarken topuğunun arkasına tekme yemiş gibi hisseden hastada, yüzüstü yatarken
baldır sıkıldığında ayak plantar fleksiyona gelmiyor (Thompson testi pozitif). Yaralanan yapı hangisidir?""",
  "Tendo calcaneus (Aşil tendonu)",
  ["M. plantaris tendonu", "M. tibialis posterior tendonu", "Lig. deltoideum", "Aponeurosis plantaris"],
  """Aşil tendonu gastrocnemius ve soleus'un ortak tendonudur. Tam yırtıkta baldır sıkılınca ayak hareket
  etmez. Plantaris'in ince tendonu sağlam kalabilir ama tek başına hareket yaptıramaz.""",
  e=["m-triceps-surae", "calcaneus"]),

Q("f", BCK, "Tendonu tendon grefti olarak kullanılabilen ve bazı kişilerde bulunmayan bacak kası hangisidir?",
  "M. plantaris",
  ["M. soleus", "M. popliteus", "M. tibialis anterior", "M. fibularis brevis"],
  """Plantaris küçük bir kas karnına ve vücudun en uzun tendonlarından birine sahiptir; gastrocnemius ile
  soleus arasından inerek calcaneus'a tutunur. İşlevsel önemi az olduğundan greft olarak alınabilir.""",
  e=["m-plantaris"]),

# ------------------------------------------------------------------ Ayak
Q("f", AYK, "Ayak sırtındaki kaslar (m. extensor digitorum brevis ve m. extensor hallucis brevis) hangi sinirle innerve edilir?",
  "N. fibularis profundus",
  ["N. fibularis superficialis", "N. plantaris medialis", "N. suralis", "N. plantaris lateralis"],
  """Ayak sırtının tek kas grubu olan kısa ekstansörler n. fibularis profundus'un lateral dalıyla innerve
  edilir. Ayak tabanı kaslarının tamamı ise n. tibialis'in medial ve lateral plantar dallarındandır.""",
  e=["mm-dorsi-pedis", "n-fibularis-communis"]),

Q("t", AYK, "Aşağıdaki ayak tabanı kaslarından hangisi n. plantaris medialis ile innerve edilir?",
  "M. abductor hallucis",
  ["M. abductor digiti minimi", "M. quadratus plantae", "M. adductor hallucis", "Mm. interossei plantares"],
  """N. plantaris medialis eldeki n. medianus'a benzer: abductor hallucis, flexor digitorum brevis, flexor
  hallucis brevis ve 1. lumbrikali innerve eder. Geri kalan tüm plantar kaslar n. plantaris lateralis
  (eldeki n. ulnaris'in karşılığı) ile innerve edilir.""",
  e=["mm-plantares", "n-tibialis"]),
]

from q_muscular_trunk2 import questions as trunk2
from q_muscular_limbs2 import questions as limbs2
from q_muscular3 import questions as more3

write("muscular", questions + trunk2 + limbs2 + more3)
