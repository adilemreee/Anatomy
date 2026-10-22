"""More muscular questions: head, neck, back, thorax, abdomen and pelvis."""
from qcommon import Q

BAS = "Baş kasları"
BOY = "Boyun kasları"
SIR = "Sırt kasları"
GOG = "Göğüs kasları"
KAR = "Karın kasları"

questions = [
# ------------------------------------------------------------------ göz ve çiğneme
Q("f", BAS, "Göz küresini aşağı ve dışa çeviren ve n. trochlearis ile innerve edilen kas hangisidir?",
  "M. obliquus superior",
  ["M. obliquus inferior", "M. rectus inferior", "M. rectus lateralis", "M. rectus superior"],
  """M. obliquus superior tendonu trochlea'dan geçip yön değiştirir ve göz küresinin arka-üst-dış
  kadranına tutunur; gözü içe döndürür (intorsiyon), aşağı ve dışa çevirir. N. trochlearis (IV)
  yalnızca bu kası innerve eder. Klinik testte göz addüksiyondayken aşağı bakış bu kası değerlendirir.""",
  ["Gözü yukarı-dışa çevirir; n. oculomotorius ile innerve edilir.", "Gözü aşağı-içe çevirir; n. oculomotorius ile innerve edilir.",
   "Yalnızca abdüksiyon yaptırır; n. abducens ile innerve edilir.", "Gözü yukarı-içe çevirir; n. oculomotorius ile innerve edilir."],
  e=["m-obliquus-superior", "mm-bulbi"]),

Q("t", BAS, "Göz içe (addüksiyon) bakarken yukarı bakışı sağlayan kas hangisidir?",
  "M. obliquus inferior",
  ["M. rectus superior", "M. obliquus superior", "M. levator palpebrae superioris", "M. rectus medialis"],
  """Klinik muayenede oblik kaslar göz addüksiyondayken, rektuslar abdüksiyondayken test edilir:
  içe bakarken yukarı bakış m. obliquus inferior'u, dışa bakarken yukarı bakış m. rectus superior'u
  gösterir. Obliquus inferior, n. oculomotorius'un alt dalıyla innerve edilir.""",
  ["Dışa bakarken yukarı bakışın kasıdır.", "İçe bakarken aşağı bakışın kasıdır.",
   "Göz kapağını kaldırır; göz küresini hareket ettirmez.", "Yalnızca addüksiyon yaptırır."],
  e=["m-obliquus-inferior", "mm-bulbi"]),

Q("tv", BAS, """Anevrizma nedeniyle başvuran hastada sağ göz kapağı tamamen düşük; kapak kaldırılınca
sağ gözün aşağı ve dışa baktığı, pupilin geniş ve ışığa yanıtsız olduğu görülüyor. Etkilenen sinir hangisidir?""",
  "N. oculomotorius (III)",
  ["N. trochlearis (IV)", "N. abducens (VI)", "Servikal sempatik zincir", "N. facialis (VII)"],
  """N. oculomotorius felcinde m. levator palpebrae (tam pitoz), rectus superior, inferior, medialis ve
  obliquus inferior felç olur; göz, sağlam kalan rectus lateralis (VI) ve obliquus superior (IV)
  etkisiyle aşağı-dışa döner. Sinirin yüzeyindeki parasempatik lifler bası altında erken etkilenir;
  pupil genişler. A. communicans posterior anevrizması klasik nedendir.""",
  ["Felcinde göz addüksiyonda aşağı bakamaz; pitoz olmaz.", "Felcinde göz içe kayar; pitoz olmaz.",
   "Horner sendromunda pitoz hafiftir ve pupil küçülür.", "Göz kapanmasını sağlar; kapak kaldırmaz."],
  e=["mm-bulbi", "m-levator-palpebrae"]),

Q("f", BAS, "Aşağıdaki göz dışı kaslarından hangisi anulus tendineus communis'ten başlamaz?",
  "M. obliquus inferior",
  ["M. rectus lateralis", "M. rectus medialis", "M. rectus superior", "M. rectus inferior"],
  """Dört rektus kası optik kanalı ve fissura orbitalis superior'un iç kısmını çevreleyen ortak tendon
  halkasından başlar. M. obliquus inferior ise orbita tabanının ön-iç kısmından (maxilla'nın orbital
  yüzü) başlayan, orbitanın arkasından köken almayan tek göz dışı kastır.""",
  e=["m-obliquus-inferior", "mm-bulbi"]),

Q("f", BAS, "Üst göz kapağını kaldıran ve sempatik liflerle innerve edilen düz kas hangisidir?",
  "M. tarsalis superior (Müller kası)",
  ["M. levator palpebrae superioris", "M. orbicularis oculi'nin palpebral bölümü", "M. occipitofrontalis",
   "M. corrugator supercilii"],
  """M. levator palpebrae superioris'in alt yüzünden ayrılan düz kas lifleri tarsal plağa tutunur ve
  sempatik sistemle innerve edilir. Horner sendromunda bu kasın felci nedeniyle 1–2 mm'lik hafif pitoz
  görülür; tam pitoz ise n. oculomotorius felcini düşündürür.""",
  ["Çizgili kastır; n. oculomotorius ile innerve edilir.", "Göz kapağını kapatır; n. facialis ile innerve edilir.",
   "Alnı kırıştırır; n. facialis ile innerve edilir.", "Kaşları içe çeker; n. facialis ile innerve edilir."],
  e=["m-levator-palpebrae"]),

Q("t", BAS, "M. pterygoideus lateralis'in üst başı nereye tutunur?",
  "Temporomandibular eklemin discus articularis'i ve kapsülüne",
  ["Processus coronoideus mandibulae'ye", "Angulus mandibulae'nin iç yüzündeki tuberositas pterygoidea'ya",
   "Ramus mandibulae'nin dış yüzüne", "Linea mylohyoidea'ya"],
  """Lateral pterygoid kasın üst başı eklem diski ve kapsülüne, alt başı collum mandibulae'deki fovea
  pterygoidea'ya tutunur. Ağız açılırken kondili ve diski birlikte tuberculum articulare'ye doğru öne
  çeker. Processus coronoideus'a temporalis, angulusun iç yüzüne medial pterygoid, dış yüzüne masseter
  tutunur.""",
  ["M. temporalis'in insersiyosudur.", "M. pterygoideus medialis'in insersiyosudur.",
   "M. masseter'in insersiyosudur.", "M. mylohyoideus'un origosudur."],
  e=["m-pterygoideus-lateralis", "art-temporomandibularis"]),

Q("f", BAS, "Mandibula angulusunun iç yüzüne tutunan çiğneme kası hangisidir?",
  "M. pterygoideus medialis",
  ["M. masseter", "M. pterygoideus lateralis", "M. temporalis", "M. buccinator"],
  """M. pterygoideus medialis, lamina lateralis processus pterygoidei'nin iç yüzünden başlar ve angulus
  mandibulae'nin iç yüzüne (tuberositas pterygoidea) tutunur. Masseter ile birlikte mandibulayı içten ve
  dıştan saran bir 'askı' oluşturarak çeneyi kapatır.""",
  e=["m-pterygoideus-medialis"]),

Q("f", BAS, "M. temporalis'in insersiyosu hangisidir?",
  "Processus coronoideus mandibulae ve ramusun ön kenarı",
  ["Fovea pterygoidea", "Tuberositas masseterica", "Tuberculum articulare", "Spina mentalis"],
  """Fossa temporalis'in tamamından yelpaze gibi başlayan temporalis, arcus zygomaticus'un altından geçip
  processus coronoideus'a tutunur. Ön lifleri çeneyi kapatır, arka yatay lifleri mandibulayı geriye
  çeker; n. mandibularis'in nn. temporales profundi dallarıyla innerve edilir.""",
  e=["m-temporalis"]),

Q("t", BAS, "Dili dışarı çıkaran (protrüzyon) başlıca kas hangisidir?",
  "M. genioglossus",
  ["M. hyoglossus", "M. styloglossus", "M. palatoglossus", "M. mylohyoideus"],
  """M. genioglossus spina mentalis superior'dan başlar; arka lifleri dil kökünü öne çekerek dili dışarı
  çıkarır. Tek taraflı n. hypoglossus felcinde sağlam taraftaki genioglossus dili karşıya iter ve dil
  lezyon tarafına sapar. Hyoglossus dili aşağı, styloglossus geri ve yukarı çeker.""",
  ["Dili aşağı ve geri çeker.", "Dili yukarı ve geri çeker.",
   "Dil kökünü yükseltir; n. vagus ile innerve edilir.", "Ağız tabanını oluşturur, dil kası değildir."],
  e=["m-genioglossus", "mm-linguae"]),

Q("t", BAS, "Aşağıdaki yapılardan hangisi m. hyoglossus'un yüzeyinden (dışından) geçmez?",
  "A. lingualis",
  ["N. hypoglossus", "N. lingualis", "Ductus submandibularis", "V. comitans nervi hypoglossi"],
  """M. hyoglossus submandibular bölgenin önemli bir dönüm noktasıdır: n. hypoglossus, ona eşlik eden ven,
  n. lingualis ve ductus submandibularis kasın yüzeyinden ilerler; a. lingualis ise kasın derininden
  (medialinden) geçer. Bu nedenle cerrahide a. lingualis kasın arka kenarında aranır.""",
  e=["m-hyoglossus", "mm-linguae"]),

# ------------------------------------------------------------------ boyun
Q("f", BOY, "M. digastricus'un iki karnını bağlayan ara tendon nereye tutunur?",
  "Fibröz bir halka ile os hyoideum'un gövdesi ve büyük boynuzuna",
  ["Mandibulanın fossa digastrica'sına", "Processus mastoideus'un incisura mastoidea'sına",
   "Tiroid kıkırdağın linea obliqua'sına", "Processus styloideus'a"],
  """Ön karın fossa digastrica'dan, arka karın incisura mastoidea'dan başlar; ara tendon fibröz bir
  askıyla hyoid kemiğe bağlanır ve m. stylohyoideus'un ikiye ayrılan tendonunun arasından geçer.
  Ön karın n. mylohyoideus (V3), arka karın n. facialis ile innerve edilir.""",
  ["Ön karnın origosudur.", "Arka karnın origosudur.", "M. sternothyroideus ve thyrohyoideus'un tutunma yeridir.",
   "M. stylohyoideus ve styloglossus'un origosudur."],
  e=["m-digastricus", "mm-suprahyoidei"]),

Q("f", BOY, "Ağız tabanını (diaphragma oris) oluşturan kas hangisidir?",
  "M. mylohyoideus",
  ["M. geniohyoideus", "M. digastricus'un ön karnı", "M. genioglossus", "M. hyoglossus"],
  """İki taraftaki m. mylohyoideus mandibulanın linea mylohyoidea'sından başlayıp orta hattaki rafede ve
  hyoid gövdesinde birleşerek ağız tabanını oluşturur. Submandibular bezin yüzeyel ve derin bölümleri
  bu kasın arka kenarı etrafında kıvrılır.""",
  e=["m-mylohyoideus", "mm-suprahyoidei"]),

Q("f", BOY, "M. omohyoideus'un ara tendonunu yerinde tutan yapı hangisidir?",
  "Klavikula ve 1. kaburgaya bağlanan fasyal bir askı",
  ["Os hyoideum'un büyük boynuzu", "Tiroid kıkırdağın linea obliqua'sı", "Manubrium sterni'nin arka yüzü",
   "Processus coracoideus"],
  """M. omohyoideus'un alt karnı skapulanın üst kenarından (incisura scapulae yakınından), üst karnı hyoid
  gövdesinden başlar. İki karın v. jugularis interna'nın önünde ara tendonla birleşir; bu tendon derin
  servikal fasyanın oluşturduğu askıyla klavikula ve 1. kaburgaya tutturulur.""",
  e=["m-omohyoideus", "mm-infrahyoidei"]),

Q("t", BOY, "M. omohyoideus'un alt karnı boynun arka üçgenini hangi iki alt üçgene ayırır?",
  "Trigonum occipitale ve trigonum omoclaviculare",
  ["Trigonum caroticum ve trigonum musculare", "Trigonum submandibulare ve trigonum submentale",
   "Trigonum caroticum ve trigonum occipitale", "Trigonum musculare ve trigonum omoclaviculare"],
  """Arka üçgen (SCM, trapezius ve klavikula arasında) omohyoid alt karnı ile üstte oksipital, altta
  omoklaviküler (supraklaviküler) üçgene ayrılır. N. accessorius oksipital üçgeni çaprazlar; a. subclavia'nın
  üçüncü bölümü ve plexus brachialis gövdeleri omoklaviküler üçgendedir.""",
  e=["m-omohyoideus", "m-sternocleidomastoideus", "m-trapezius"]),

Q("f", BOY, "Trigonum caroticum'u sınırlayan kaslar hangileridir?",
  "M. sternocleidomastoideus, m. omohyoideus'un üst karnı ve m. digastricus'un arka karnı",
  ["M. sternocleidomastoideus, m. trapezius ve klavikula",
   "M. digastricus'un iki karnı ve mandibula",
   "M. sternocleidomastoideus, m. omohyoideus'un üst karnı ve boynun orta hattı",
   "M. digastricus'un ön karnı, os hyoideum ve boynun orta hattı"],
  """Karotis üçgeninde a. carotis communis'in çatallanması, v. jugularis interna, n. vagus ve n. hypoglossus
  bulunur. Diğer seçenekler sırasıyla arka üçgen, submandibular üçgen, kas (muskuler) üçgen ve submental
  üçgenin sınırlarıdır.""",
  e=["m-sternocleidomastoideus", "m-omohyoideus", "m-digastricus"]),

Q("f", BOY, "M. sternocleidomastoideus'un iki başı nereden başlar?",
  "Manubrium sterni'nin ön yüzü ve klavikulanın iç 1/3'ü",
  ["Manubrium sterni ve 1. kaburga kıkırdağı", "Klavikulanın dış 1/3'ü ve akromiyon",
   "Processus mastoideus ve linea nuchalis superior", "Corpus sterni ve processus xiphoideus"],
  """Sternal baş manubriumun ön yüzünden, klaviküler baş klavikulanın iç üçte birinden başlar; kas
  processus mastoideus ve linea nuchalis superior'un dış yarısına tutunur. İki başın arasındaki küçük
  üçgen çukurluk (fossa supraclavicularis minor) v. jugularis interna'nın üzerindedir.""",
  e=["m-sternocleidomastoideus"]),

Q("f", BOY, "M. scalenus anterior'un insersiyosu hangisidir?",
  "1. kaburganın tuberculum musculi scaleni anterioris'i",
  ["2. kaburganın dış yüzü", "1. kaburgada a. subclavia oluğunun arkası", "C7'nin processus transversus'u",
   "Klavikulanın alt yüzü"],
  """M. scalenus anterior C3–C6 transvers çıkıntıların ön tüberküllerinden başlayıp 1. kaburgadaki
  skalen tüberküle tutunur. Bu tüberkülün önünden v. subclavia, arkasındaki oluktan a. subclavia geçer.
  Scalenus medius 1. kaburgada oluğun arkasına, scalenus posterior 2. kaburgaya tutunur.""",
  ["M. scalenus posterior'un insersiyosudur.", "M. scalenus medius'un insersiyosudur.",
   "M. scalenus anterior hiçbir zaman C7'ye tutunmaz.", "M. subclavius'un insersiyosudur."],
  e=["m-scalenus-anterior", "mm-scaleni"]),

Q("f", BOY, "Ses tellerini geren ve n. laryngeus superior'un dış dalıyla innerve edilen larinks kası hangisidir?",
  "M. cricothyroideus",
  ["M. cricoarytenoideus posterior", "M. thyroarytenoideus", "M. arytenoideus", "M. cricoarytenoideus lateralis"],
  """M. cricothyroideus tiroid kıkırdağı öne-aşağı eğerek ses tellerini uzatır ve gerer; tiz seslerde önemlidir.
  Larinksin dış yüzündeki tek iç kas olup n. laryngeus superior'un ramus externus'uyla innerve edilir;
  diğer tüm iç larinks kasları n. laryngeus recurrens iledir.""",
  e=["m-cricothyroideus"]),

Q("t", BOY, "Rima glottidis'i açan (ses tellerini uzaklaştıran) tek larinks kası hangisidir?",
  "M. cricoarytenoideus posterior",
  ["M. cricoarytenoideus lateralis", "M. arytenoideus", "M. thyroarytenoideus", "M. cricothyroideus"],
  """M. cricoarytenoideus posterior aritenoidlerin kas çıkıntısını geriye çekip ses çıkıntılarını yana
  döndürür ve glottisi açar. İki taraflı n. laryngeus recurrens hasarında bu kasların felci ses tellerini
  orta hatta bırakır; stridor ve solunum sıkıntısı gelişir.""",
  ["Ses tellerini yaklaştırır.", "Aritenoidleri birbirine yaklaştırarak glottisin arka kısmını kapatır.",
   "Ses tellerini gevşetir.", "Ses tellerini gerer; açmaz."],
  e=["m-cricoarytenoideus-posterior"]),

Q("tv", BOY, """Total tiroidektomiden sonra hastada ses kısıklığı gelişiyor. Laringoskopide sol ses telinin
paramedyan konumda hareketsiz olduğu görülüyor. Hangi sinir hasar görmüştür?""",
  "Sol n. laryngeus recurrens",
  ["Sol n. laryngeus superior'un iç dalı", "Sol n. laryngeus superior'un dış dalı", "Sol n. hypoglossus",
   "Ansa cervicalis'in üst kökü"],
  """N. laryngeus recurrens, m. cricothyroideus dışındaki tüm iç larinks kaslarını innerve eder ve
  a. thyroidea inferior ile yakın komşuluk gösterir. Tek taraflı hasarda ses teli paramedyan konumda
  kalır, ses kısılır. Dış dal hasarında ses yorgunluğu ve tiz seslerde güçlük olur; iç dal ise
  duyusaldır.""",
  ["Glottis üstü mukozanın duyusunu taşır; motor değildir.", "Yalnızca m. cricothyroideus'u innerve eder.",
   "Dil kaslarını innerve eder.", "İnfrahiyoid kasları innerve eder."],
  e=["m-cricoarytenoideus-posterior", "m-thyroarytenoideus"]),

Q("t", BOY, "Farinks kaslarından n. glossopharyngeus ile innerve edilen tek kas hangisidir?",
  "M. stylopharyngeus",
  ["M. palatopharyngeus", "M. constrictor pharyngis superior", "M. salpingopharyngeus",
   "M. constrictor pharyngis inferior"],
  """Farinks kaslarının hepsi n. vagus'un plexus pharyngeus aracılığıyla innerve edilir; tek istisna
  processus styloideus'tan başlayan m. stylopharyngeus'tur (n. glossopharyngeus). Kas, üst ve orta
  konstriktörler arasından farinkse girer ve yutkunmada farinksi yükseltir.""",
  e=["m-stylopharyngeus"]),

Q("t", BOY, "Zenker divertikülünün çıktığı Killian üçgeni nerede bulunur?",
  "M. constrictor pharyngis inferior'un tirofaringeal ve krikofaringeal lifleri arasında",
  ["Üst ve orta konstriktör kaslar arasında", "Orta ve alt konstriktör kaslar arasında",
   "Krikofaringeal lifler ile özofagusun boyuna kas tabakası arasında",
   "M. stylopharyngeus ile üst konstriktör arasında"],
  """Alt konstriktörün eğik tirofaringeal lifleri ile yatay krikofaringeal lifleri (üst özofagus sfinkteri)
  arasındaki arka zayıf alan Killian üçgenidir. Krikofaringeal lifler gevşemediğinde mukoza buradan
  arkaya fıtıklaşır. Krikofaringeus ile özofagus kasları arasındaki alan ise Laimer üçgenidir.""",
  e=["m-constrictor-pharyngis-inferior"]),

Q("f", BOY, "Başı aynı tarafa döndüren ve ense bölgesinde trapeziusun derininde bulunan kas hangisidir?",
  "M. splenius capitis",
  ["M. sternocleidomastoideus", "M. trapezius'un üst lifleri", "M. scalenus anterior", "M. levator scapulae"],
  """M. splenius capitis lig. nuchae ve üst torakal dikensi çıkıntılardan başlayıp processus mastoideus
  ve linea nuchalis superior'a tutunur; tek taraflı kasılmada başı aynı tarafa döndürür. SCM ise yüzü
  karşı tarafa çevirir; iki kas başın dönmesinde birlikte çalışır.""",
  ["Yüzü karşı tarafa çevirir.", "Başı aynı tarafa eğer ve yüzü karşı tarafa çevirir.",
   "Boynu aynı tarafa eğer; başı döndürmez.", "Skapulayı yükseltir."],
  e=["m-splenius"]),

# ------------------------------------------------------------------ sırt
Q("f", SIR, "Suboksipital üçgeni sınırlayan kaslar hangileridir?",
  "M. rectus capitis posterior major, m. obliquus capitis superior ve m. obliquus capitis inferior",
  ["M. rectus capitis posterior minor, major ve m. obliquus capitis inferior",
   "M. semispinalis capitis, m. splenius capitis ve m. obliquus capitis superior",
   "M. longissimus capitis, m. rectus capitis posterior major ve m. obliquus capitis inferior",
   "M. rectus capitis posterior minor, m. obliquus capitis superior ve inferior"],
  """Üçgenin iç-üst sınırı rectus capitis posterior major, dış-üst sınırı obliquus capitis superior, alt
  sınırı obliquus capitis inferior'dur. Tabanında atlasın arka kemeri ve membrana atlantooccipitalis
  posterior, içinde a. vertebralis ve n. suboccipitalis bulunur; tavanını semispinalis capitis örter.""",
  e=["mm-suboccipitales", "m-rectus-capitis-posterior-major", "m-obliquus-capitis-superior",
     "m-obliquus-capitis-inferior"]),

Q("f", SIR, "Suboksipital kasları innerve eden sinir hangisidir?",
  "N. suboccipitalis (C1'in arka dalı)",
  ["N. occipitalis major (C2'nin arka dalı)", "N. occipitalis minor (C2'nin ön dalı)",
   "N. occipitalis tertius (C3'ün arka dalı)", "N. accessorius"],
  """N. suboccipitalis, C1'in arka dalıdır ve a. vertebralis ile atlasın arka kemeri arasından çıkarak
  suboksipital üçgendeki kasların hepsini innerve eder; genellikle deri dalı yoktur. N. occipitalis
  major obliquus capitis inferior'un altından çıkıp ense ve kafa derisini innerve eder.""",
  ["Ense ve kafa derisinin duyusunu alır; suboksipital kasları innerve etmez.",
   "Kulak arkası derinin duyusunu alır.", "Ensenin alt kısmının derisini innerve eder.",
   "Trapezius ve SCM'yi innerve eder."],
  e=["mm-suboccipitales", "m-rectus-capitis-posterior-major"]),

Q("t", SIR, "Başı aynı tarafa döndüren ve suboksipital üçgenin alt sınırını yapan kas hangisidir?",
  "M. obliquus capitis inferior",
  ["M. obliquus capitis superior", "M. rectus capitis posterior minor", "M. rectus capitis lateralis",
   "M. longus capitis"],
  """Axis'in dikensi çıkıntısından atlasın transvers çıkıntısına uzanan obliquus capitis inferior, kafaya
  tutunmayan tek suboksipital kastır; atlası ve başı axis üzerinde aynı tarafa döndürür.""",
  e=["m-obliquus-capitis-inferior", "mm-suboccipitales"]),

Q("t", SIR, "Auskültasyon üçgenini (trigonum auscultationis) sınırlayan yapılar hangileridir?",
  "M. trapezius, m. latissimus dorsi ve skapulanın iç kenarı",
  ["M. latissimus dorsi, m. obliquus externus abdominis ve crista iliaca",
   "M. quadratus lumborum, 12. kaburga ve m. obliquus internus abdominis",
   "M. trapezius, m. sternocleidomastoideus ve klavikula",
   "M. teres major, m. teres minor ve m. triceps brachii'nin uzun başı"],
  """Auskültasyon üçgeninde kas tabakası incedir; hasta öne eğilip kollarını kavuşturunca skapula yana
  kayar ve üçgen genişler, akciğer sesleri daha iyi duyulur. Diğer seçenekler alt lomber (Petit), üst
  lomber (Grynfeltt), arka boyun üçgeni ve skapular aralıklardır.""",
  e=["m-trapezius", "m-latissimus-dorsi", "m-rhomboideus-major"]),

Q("f", SIR, "M. erector spinae'nin en dışta (lateralde) yer alan kolonu hangisidir?",
  "M. iliocostalis",
  ["M. longissimus", "M. spinalis", "M. multifidus", "M. semispinalis"],
  """Erector spinae dıştan içe iliocostalis, longissimus ve spinalis kolonlarından oluşur (‘I Love
  Spaghetti’). Multifidus ve semispinalis daha derindeki transversospinal gruba aittir. Hepsi spinal
  sinirlerin arka dallarıyla innerve edilir.""",
  e=["m-iliocostalis", "m-erector-spinae"]),

Q("t", SIR, "Lomber bölgede en kalın transversospinal kas olup segmental stabilizasyonda önemli rol oynayan kas hangisidir?",
  "M. multifidus",
  ["M. semispinalis", "Mm. rotatores", "M. spinalis", "M. iliocostalis"],
  """M. multifidus sakrumdan C2'ye kadar uzanır ve en kalın olduğu yer lomber bölgedir; her omuru alttaki
  2–4 omura bağlayarak segmentleri sabitler. Kronik bel ağrısında atrofisi ve yağlanması sık görülür.
  Semispinalis torakal-servikal bölgede, rotatores torakal bölgede belirgindir.""",
  e=["m-multifidus", "mm-transversospinales"]),

Q("f", SIR, "M. rhomboideus major nereye tutunur?",
  "Skapulanın iç kenarına, spina scapulae'nin kökünden angulus inferior'a kadar",
  ["Skapulanın iç kenarının spina hizasındaki küçük bölümüne", "Angulus superior scapulae'ye",
   "Processus coracoideus'a", "Skapulanın ön yüzünün iç kenarı boyunca"],
  """Rhomboideus major T2–T5 dikensi çıkıntılarından başlar ve skapulanın iç kenarının spina altındaki
  bölümüne tutunur; minor C7–T1'den spina kökü hizasına uzanır. İkisi n. dorsalis scapulae ile innerve
  edilir ve skapulayı geriye-yukarı çeker.""",
  ["M. rhomboideus minor'un insersiyosudur.", "M. levator scapulae'nin insersiyosudur.",
   "M. pectoralis minor'un insersiyosudur.", "M. serratus anterior'un insersiyosudur."],
  e=["m-rhomboideus-major", "mm-rhomboidei"]),

Q("f", SIR, "M. levator scapulae nereden başlar?",
  "C1–C4 omurlarının transvers çıkıntılarının arka tüberküllerinden",
  ["C7–T5 dikensi çıkıntılarından", "Linea nuchalis superior ve lig. nuchae'dan",
   "C3–C6 transvers çıkıntılarının ön tüberküllerinden", "1. kaburganın üst yüzünden"],
  """Levator scapulae üst servikal omurlardan başlayıp skapulanın angulus superior'una ve iç kenarın üst
  kısmına tutunur. Skapulayı yükseltir ve aşağı döndürür; n. dorsalis scapulae ve C3–C4 dallarıyla
  innerve edilir.""",
  e=["m-levator-scapulae"]),

Q("t", SIR, "Aşağıdakilerden hangisi m. latissimus dorsi'nin hareketlerinden biri değildir?",
  "Kolun dış rotasyonu",
  ["Kolun ekstansiyonu", "Kolun addüksiyonu", "Kolun iç rotasyonu", "Kollar sabitken gövdeyi yukarı çekme"],
  """Latissimus dorsi sulcus intertubercularis'in tabanına tutunur; kolu ekstansiyon, addüksiyon ve iç
  rotasyona getirir (‘yüzücü kası’). Kollar sabitken (barfiks) gövdeyi yukarı çeker. Dış rotasyon
  infraspinatus ve teres minor'un işidir.""",
  e=["m-latissimus-dorsi"]),

# ------------------------------------------------------------------ göğüs
Q("f", GOG, "M. serratus anterior nereye tutunur?",
  "Skapulanın iç kenarının ön (kostal) yüzüne",
  ["Skapulanın iç kenarının arka yüzüne", "Processus coracoideus'a", "Skapulanın dış kenarına",
   "Spina scapulae'nin üst kenarına"],
  """Serratus anterior üst 8–9 kaburgadan dişler halinde başlar ve skapulanın iç kenarının ön yüzüne,
  en kalın lifleriyle angulus inferior'a tutunur. Skapulayı göğüs duvarına bastırır ve öne çeker; alt
  lifleri skapulayı yukarı döndürerek kolun 90°'nin üzerine kalkmasına yardım eder.""",
  e=["m-serratus-anterior"]),

Q("t", GOG, "M. pectoralis minor nereden başlar ve nereye tutunur?",
  "3.–5. kaburgalardan başlar, processus coracoideus'a tutunur",
  ["1. kaburga ve kıkırdağından başlar, klavikulanın alt yüzüne tutunur",
   "1.–8. kaburgalardan başlar, skapulanın iç kenarına tutunur",
   "Klavikula ve sternumdan başlar, crista tuberculi majoris'e tutunur",
   "2.–5. kaburgalardan başlar, akromiyona tutunur"],
  """Pectoralis minor, a. axillaris'i üç bölüme ayıran dönüm noktasıdır. Diğer seçenekler sırasıyla
  m. subclavius, m. serratus anterior ve m. pectoralis major'u tanımlar; akromiyona göğüs kası tutunmaz.""",
  ["M. subclavius'u tanımlar.", "M. serratus anterior'u tanımlar.", "M. pectoralis major'u tanımlar.",
   "Akromiyona göğüs kası tutunmaz."],
  e=["m-pectoralis-minor"]),

Q("f", GOG, "Aşağıdakilerden hangisi zorlu inspirasyonda yardımcı solunum kası olarak görev yapmaz?",
  "M. rectus abdominis",
  ["M. sternocleidomastoideus", "Mm. scaleni", "M. pectoralis minor", "M. serratus posterior superior"],
  """Zorlu inspirasyonda göğüs kafesini yükselten kaslar yardıma gelir: SCM, skalenler, pectoralis minor
  (kol sabitken) ve serratus posterior superior. Karın ön duvarı kasları ise karın içi basıncı artırarak
  zorlu ekspirasyonda ve öksürmede çalışır.""",
  e=["m-rectus-abdominis", "mm-scaleni", "m-sternocleidomastoideus"]),

Q("f", GOG, "Diyaframdaki kaval, özofageal ve aortik açıklıkların omur düzeyleri sırasıyla hangisidir?",
  "T8, T10, T12",
  ["T10, T8, T12", "T8, T12, T10", "T6, T8, T10", "T12, T10, T8"],
  """V. cava inferior T8'de centrum tendineum'dan, özofagus ve trunci vagales T10'da sağ krusun kas
  liflerinden, aorta ise T12'de diyaframın arkasından (lig. arcuatum medianum altından) geçer.
  Akılda tutma: ‘I ate ten eggs at twelve’ (IVC 8, esophagus 10, aorta 12).""",
  e=["diaphragma"]),

Q("t", GOG, "Hiatus oesophageus'tan geçen yapılar hangileridir?",
  "Özofagus, trunci vagales ve a./v. gastrica sinistra'nın özofageal dalları",
  ["Aorta, ductus thoracicus ve v. azygos", "V. cava inferior ve n. phrenicus dexter'in dalları",
   "Truncus sympathicus ve nn. splanchnici", "A. epigastrica superior"],
  """Özofageal açıklık T10 düzeyinde sağ krusun kas lifleri arasındadır; özofagus ile birlikte ön ve arka
  vagal gövdeler ve sol gastrik damarların özofageal dalları geçer. Kas liflerinin oluşturduğu bu halka
  fizyolojik bir sfinkter gibi davranır ve hiatal herni burada gelişir.""",
  ["Hiatus aorticus'tan geçer.", "Foramen venae cavae'dan geçer.", "Krusların arkasından veya içinden geçer.",
   "Sternokostal üçgenden (Larrey) geçer."],
  e=["diaphragma"]),

Q("t", GOG, "Mm. intercostales externi için hangisi doğrudur?",
  "Lifleri aşağı ve öne uzanır; inspirasyonda kaburgaları yükseltir",
  ["Lifleri aşağı ve arkaya uzanır; ekspirasyonda kaburgaları alçaltır",
   "Lifleri dikey uzanır; yalnızca öksürmede çalışır",
   "Önde sternuma kadar kas olarak uzanır",
   "İnterkostal damar-sinir paketi bu kasın hemen derininde seyreder"],
  """Dış interkostal kaslar ‘ellerini cebe sokan’ yönde aşağı-öne uzanır ve inspirasyonda kaburgaları
  kaldırır; önde kıkırdaklar arasında membrana intercostalis externa'ya dönüşür. İç interkostaller aşağı-
  arkaya uzanır. Damar-sinir paketi iç ve en iç interkostal kaslar arasındadır.""",
  ["İç interkostal kasları tanımlar.", "Böyle bir kas yoktur.",
   "Önde membrana intercostalis externa'ya dönüşür.", "Paket iç ve en iç interkostaller arasındadır."],
  e=["mm-intercostales-externi", "mm-intercostales"]),

Q("f", GOG, "M. transversus thoracis nerede bulunur?",
  "Sternumun arka yüzünden 2.–6. kaburga kıkırdaklarının iç yüzüne uzanır",
  ["Kaburga açılarına yakın, bir-iki interkostal aralığı atlayarak uzanır",
   "Omurların transvers çıkıntılarından alttaki kaburgalara uzanır",
   "Boyun tabanında 1. kaburganın üstünde yer alır",
   "Karın ön duvarının en derin kas tabakasını oluşturur"],
  """Transversus thoracis göğüs ön duvarının iç yüzünde, a. ve v. thoracica interna'nın arkasında yer
  alan ince kastır; karın duvarındaki transversus abdominis'in göğüsteki devamı sayılır. İkinci seçenek
  mm. subcostales'i, üçüncüsü levatores costarum'u tanımlar.""",
  e=["m-transversus-thoracis"]),

# ------------------------------------------------------------------ karın
Q("f", KAR, "Linea semilunaris neyi gösterir?",
  "M. rectus abdominis kılıfının dış kenarını",
  ["Rectus kılıfı arka yaprağının alt sınırını", "İki rectus kasını ayıran orta hattı",
   "Rectus kasının tendinöz kesişimlerini", "Lig. inguinale'nin iç ucunu"],
  """Linea semilunaris, rectus kılıfının dış kenarı boyunca yassı kas aponevrozlarının birleştiği kavisli
  çizgidir; dokuzuncu kaburga kıkırdağının ucunda safra kesesi bu çizgi üzerine izdüşer. Arka yaprağın
  alt sınırı linea arcuata, orta hat ise linea alba'dır.""",
  e=["m-rectus-abdominis", "linea-alba"]),

Q("t", KAR, "Spiegel fıtığı en sık nerede görülür?",
  "Linea semilunaris boyunca, linea arcuata hizasında",
  ["Göbek halkasında", "Hesselbach üçgeninde", "Petit (alt lomber) üçgeninde", "Göbeğin üstünde linea alba'da"],
  """Spiegel fıtığı, transversus abdominis aponevrozunun rectus kenarındaki (Spiegel fasyası) zayıf
  noktasından, çoğunlukla arka rectus kılıfının bittiği linea arcuata düzeyinde gelişir. Obliquus externus
  aponevrozunun altında kaldığı için ele gelmesi zor olabilir.""",
  ["Umbilikal fıtığın yeridir.", "Direkt kasık fıtığının yeridir.", "Lomber fıtığın yeridir.",
   "Epigastrik fıtığın yeridir."],
  e=["m-transversus-abdominis", "m-rectus-abdominis"]),

Q("f", KAR, "Karın ön-yan duvarındaki üç yassı kasın en derinde olanı hangisidir?",
  "M. transversus abdominis",
  ["M. obliquus internus abdominis", "M. obliquus externus abdominis", "M. rectus abdominis",
   "M. quadratus lumborum"],
  """Yüzeyelden derine: obliquus externus (aşağı-öne), obliquus internus (yukarı-öne) ve transversus
  abdominis (yatay). Transversus abdominis'in altında fascia transversalis ve periton bulunur; kasın
  derin lifleri karın içi basıncını artıran ‘korse’ işlevini görür.""",
  e=["m-transversus-abdominis"]),

Q("t", KAR, "Linea arcuata'nın üstünde rectus kılıfının arka yaprağını oluşturan yapılar hangileridir?",
  "Obliquus internus aponevrozunun arka yaprağı ve transversus abdominis aponevrozu",
  ["Yalnızca fascia transversalis", "Obliquus externus ve internus aponevrozları",
   "Üç yassı kasın aponevrozlarının tamamı", "Yalnızca transversus abdominis aponevrozu"],
  """Linea arcuata'nın üstünde obliquus internus aponevrozu ikiye ayrılır: ön yaprak externus ile ön
  kılıfa, arka yaprak transversus ile arka kılıfa katılır. Linea arcuata'nın altında ise üç aponevroz da
  öne geçer; rectus'un arkasında yalnızca fascia transversalis kalır.""",
  e=["m-rectus-abdominis", "m-obliquus-internus", "m-transversus-abdominis"]),

Q("f", KAR, "M. pyramidalis'in işlevi hangisidir?",
  "Linea alba'yı gerer",
  ["Pelvisi öne eğer", "Gövdeyi fleksiyona getiren asıl kastır", "Kremaster refleksini sağlar",
   "Mesane boynunu kapatır"],
  """M. pyramidalis, pubisten başlayıp linea alba'ya tutunan küçük üçgen kastır; rectus kılıfının içinde,
  rectus abdominis'in önünde yer alır ve kişilerin bir kısmında bulunmaz. N. subcostalis (T12) ile
  innerve edilir.""",
  e=["m-pyramidalis", "linea-alba"]),

Q("f", KAR, "M. quadratus lumborum nereye tutunur?",
  "12. kaburganın alt kenarı ve L1–L4 transvers çıkıntılarına",
  ["Crista iliaca'nın arka kısmına", "T12–L4 omur cisimlerine", "Trochanter minor'a",
   "L5 transvers çıkıntısı ve lig. iliolumbale'ye"],
  """Quadratus lumborum crista iliaca'nın arka kısmı ve lig. iliolumbale'den başlar; 12. kaburgaya ve
  üst lomber transvers çıkıntılara tutunur. İnspirasyonda 12. kaburgayı sabitler, tek taraflı kasılmada
  gövdeyi yana büker. Omur cisimlerinden psoas major başlar ve trochanter minor'a tutunur.""",
  ["Kasın origosudur.", "M. psoas major'un origosudur.", "M. iliopsoas'ın insersiyosudur.",
   "Kasın origosunun bir parçasıdır."],
  e=["m-quadratus-lumborum"]),

Q("f", KAR, "Diaphragma pelvis'i oluşturan kaslar hangileridir?",
  "M. levator ani ve m. coccygeus",
  ["M. levator ani ve m. obturatorius internus", "M. sphincter ani externus ve m. transversus perinei profundus",
   "M. coccygeus ve m. piriformis", "M. bulbospongiosus ve m. ischiocavernosus"],
  """Pelvis tabanı (diaphragma pelvis) huni biçimli levator ani (puborectalis, pubococcygeus, iliococcygeus)
  ve arkadaki coccygeus'tan oluşur. Obturatorius internus ve piriformis pelvisin yan ve arka duvarındadır;
  bulbospongiosus ve ischiocavernosus perinenin yüzeyel kaslarıdır.""",
  e=["diaphragma-pelvis", "m-levator-ani", "m-coccygeus"]),

Q("t", KAR, "M. levator ani'nin başladığı arcus tendineus hangi kasın fasyasının kalınlaşmasıdır?",
  "M. obturatorius internus",
  ["M. piriformis", "M. coccygeus", "M. iliacus", "M. psoas major"],
  """Levator ani önde pubisin arka yüzünden, arkada spina ischiadica'dan, aradaki bölümde ise obturator
  internus fasyasının kalınlaşmasıyla oluşan arcus tendineus musculi levatoris ani'den başlar. Bu nedenle
  obturator internus'un üst kısmı pelvis içinde, alt kısmı perinede (fossa ischioanalis'in yan duvarı) kalır.""",
  e=["m-levator-ani", "m-obturator-internus"]),

Q("tv", KAR, """Zor vajinal doğumdan sonra gaz ve gaita kaçırma şikâyeti olan hastada anal sfinkter kompleksinde
yırtık saptanıyor. İstemli kontrol edilen dış anal sfinkteri innerve eden sinir hangisidir?""",
  "N. rectalis inferior (n. pudendus)",
  ["Nn. splanchnici pelvici (S2–S4)", "N. hypogastricus", "N. obturatorius", "N. genitofemoralis"],
  """Dış anal sfinkter çizgili kastır ve n. pudendus'un n. rectalis inferior dalıyla innerve edilir; zor
  doğum hem kas yırtığına hem de pudendal sinir gerilme hasarına yol açabilir. İç sfinkter düz kastır ve
  otonom sinirlerle (sempatik: kasılma) kontrol edilir.""",
  ["Parasempatiktir; iç sfinkteri gevşetir.", "Sempatiktir; iç sfinkteri kasar.",
   "Uyluğun addüktör kaslarını innerve eder.", "Kremaster kasını ve uyluk ön-üst derisini innerve eder."],
  e=["m-sphincter-ani-externus", "diaphragma-pelvis"]),
]
