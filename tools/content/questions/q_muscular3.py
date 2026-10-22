"""Muscular questions, third set: basic level (names, actions, groups), more
faculty questions on origins, actions and reflexes, and new TUS points."""
from qcommon import Q

BAS = "Baş kasları"
BOY = "Boyun kasları"
SIR = "Sırt kasları"
GOG = "Göğüs kasları"
KAR = "Karın kasları"
OMU = "Omuz kasları"
KOL = "Kol kasları"
ONK = "Önkol kasları"
EL = "El kasları"
KAL = "Kalça kasları"
UYL = "Uyluk kasları"
BAC = "Bacak kasları"
AYA = "Ayak kasları"

questions = [
# ------------------------------------------------------------------ temel
Q("b", BAS, "Mimik (yüz ifadesi) kaslarını innerve eden sinir hangisidir?",
  "N. facialis (VII)", ["N. trigeminus (V)", "N. hypoglossus (XII)", "N. oculomotorius (III)", "N. accessorius (XI)"],
  """Bütün mimik kasları 2. faringeal arktan gelişir ve n. facialis ile innerve edilir. Çiğneme kasları ise 1. ark kökenlidir
  ve n. mandibularis (V3) ile innerve edilir.""",
  e=["m-orbicularis-oculi", "m-zygomaticus-major"]),

Q("b", BAS, "Çiğneme kaslarını innerve eden sinir hangisidir?",
  "N. mandibularis (V3)", ["N. facialis", "N. maxillaris (V2)", "N. glossopharyngeus", "N. hypoglossus"],
  """Masseter, temporalis, pterygoideus medialis ve lateralis 1. faringeal arktan gelişir ve trigeminus'un mandibular dalıyla
  innerve edilir.""",
  e=["m-masseter", "m-temporalis", "mm-pterygoidei"]),

Q("b", BAS, "Dişleri sıkınca yanakta sertleşerek ele gelen çiğneme kası hangisidir?",
  "M. masseter", ["M. temporalis", "M. buccinator", "M. pterygoideus medialis", "M. zygomaticus major"],
  """Masseter zigomatik arktan mandibula ramusunun dış yüzüne uzanır; çeneyi kapatan en güçlü kaslardandır ve dişler
  sıkıldığında yanakta kolayca hissedilir.""",
  e=["m-masseter"]),

Q("b", BAS, "Şakak bölgesinde yelpaze şeklinde yer alan çiğneme kası hangisidir?",
  "M. temporalis", ["M. masseter", "M. occipitofrontalis", "M. pterygoideus lateralis", "M. auricularis superior"],
  """Temporalis fossa temporalis'i dolduran yelpaze şeklindeki kastır; lifleri processus coronoideus'a toplanır ve çeneyi
  kapatır, arka lifleri geri çeker.""",
  e=["m-temporalis"]),

Q("b", BAS, "Dudakları büzen (ıslık çalma, öpücük verme) kas hangisidir?",
  "M. orbicularis oris", ["M. buccinator", "M. zygomaticus major", "M. depressor anguli oris", "M. mentalis"],
  """Orbicularis oris ağzı halka şeklinde çevreleyen sfinkter kastır; dudakları kapatır ve büzer. Buccinator yanağı dişlere
  bastırır.""",
  e=["m-orbicularis-oris"]),

Q("b", BAS, "Göz küresini hareket ettiren dış göz kası sayısı kaçtır?",
  "6 (4 rektus, 2 oblik)", ["4", "5", "7", "8"],
  """Göz küresini dört rektus (superior, inferior, medialis, lateralis) ve iki oblik (superior, inferior) kas hareket ettirir.
  M. levator palpebrae superioris göz kapağını kaldırır, göz küresini hareket ettirmez.""",
  e=["mm-bulbi"]),

Q("b", BOY, "Boynun yanında kulak arkasından sternum ve klavikulaya uzanan belirgin kas hangisidir?",
  "M. sternocleidomastoideus", ["M. trapezius", "Platysma", "M. scalenus anterior", "M. omohyoideus"],
  """SCM processus mastoideus'tan manubrium ve klavikulanın iç kısmına uzanır; boynu ön ve arka üçgenlere ayıran önemli bir
  yüzey işaretidir.""",
  e=["m-sternocleidomastoideus"]),

Q("b", BOY, "Boynun ön yüzünü deri altında örten ince, geniş mimik kası hangisidir?",
  "Platysma", ["M. sternohyoideus", "M. omohyoideus", "M. sternocleidomastoideus", "M. mylohyoideus"],
  """Platysma göğsün üst kısmından mandibula ve ağız köşesine uzanan yüzeyel bir mimik kasıdır; n. facialis'in servikal dalıyla
  innerve edilir.""",
  e=["m-platysma"]),

Q("b", SIR, "Omuzları silken (yukarı kaldıran) sırtın üst kısmındaki yüzeyel kas hangisidir?",
  "M. trapezius", ["M. latissimus dorsi", "M. rhomboideus major", "M. serratus anterior", "M. erector spinae"],
  """Trapeziusun üst lifleri skapulayı kaldırır (omuz silkme); orta lifler geri çeker, alt lifler aşağı çeker. Levator scapulae
  da elevasyona yardım eder.""",
  e=["m-trapezius"]),

Q("b", SIR, "Sırtın en geniş kası hangisidir?",
  "M. latissimus dorsi", ["M. trapezius", "M. erector spinae", "M. serratus posterior inferior", "M. quadratus lumborum"],
  """Latissimus dorsi bel ve sırtın alt kısmını örten geniş, üçgen bir kastır; kolu ekstansiyon, addüksiyon ve iç rotasyona
  getirir (tırmanma ve yüzme kası).""",
  e=["m-latissimus-dorsi"]),

Q("b", SIR, "Omurganın iki yanında uzanan ve gövdeyi dik tutan kas grubu hangisidir?",
  "M. erector spinae", ["M. latissimus dorsi", "Mm. rhomboidei", "M. trapezius", "M. serratus anterior"],
  """Erector spinae dıştan içe iliocostalis, longissimus ve spinalis kolonlarından oluşur; omurganın ekstansiyonunu ve dik
  duruşu sağlar.""",
  e=["m-erector-spinae"]),

Q("b", GOG, "Solunumun en önemli (ana) kası hangisidir?",
  "Diyafram", ["Mm. intercostales externi", "M. sternocleidomastoideus", "M. rectus abdominis", "M. pectoralis major"],
  """Sakin solunumda inspirasyonun büyük kısmını diyafram yapar; kasılınca kubbesi aşağı iner ve göğüs boşluğunun dikey çapı
  artar.""",
  e=["diaphragma"]),

Q("b", GOG, "Göğsün ön yüzündeki en büyük kas hangisidir?",
  "M. pectoralis major", ["M. pectoralis minor", "M. serratus anterior", "M. subclavius", "M. deltoideus"],
  """Pectoralis major göğsün ön yüzünü örten yelpaze şeklindeki kastır; kolu addüksiyon, iç rotasyon ve fleksiyona getirir.""",
  e=["m-pectoralis-major"]),

Q("b", KAR, "Karın ön duvarında 'altılı kas' görünümünü veren kas hangisidir?",
  "M. rectus abdominis", ["M. obliquus externus abdominis", "M. transversus abdominis", "M. pyramidalis",
   "M. quadratus lumborum"],
  """Rectus abdominis'in üzerindeki tendinöz kesişimler (intersectiones tendineae) kası bölmelere ayırarak karakteristik
  görünümü oluşturur.""",
  e=["m-rectus-abdominis"]),

Q("b", KAR, "Karın ön-yan duvarındaki üç yassı kastan en yüzeyel olanı hangisidir?",
  "M. obliquus externus abdominis", ["M. obliquus internus abdominis", "M. transversus abdominis", "M. rectus abdominis",
   "M. latissimus dorsi"],
  """Yüzeyelden derine sıralama: obliquus externus, obliquus internus, transversus abdominis. Dış oblik liflerin yönü 'eller
  cepte' şeklindedir (aşağı ve öne).""",
  e=["m-obliquus-externus"]),

Q("b", KAR, "Kasık bağı (lig. inguinale) hangi iki nokta arasında uzanır?",
  "Spina iliaca anterior superior ile tuberculum pubicum", ["Crista iliaca ile symphysis pubica",
   "Spina iliaca anterior inferior ile tuber ischiadicum", "Processus xiphoideus ile tuberculum pubicum",
   "Trochanter major ile tuberculum pubicum"],
  """Lig. inguinale dış oblik kasın aponevrozunun kıvrılmış alt kenarıdır; SIAS'tan tuberculum pubicum'a uzanır ve kasık
  bölgesinin önemli işaretidir.""",
  e=["lig-inguinale"]),

Q("b", KAR, "Linea alba nerede uzanır?",
  "Processus xiphoideus ile symphysis pubica arasında", ["Kaburga kavsi boyunca", "SIAS ile tuberculum pubicum arasında",
   "Rectus kasının dış kenarı boyunca", "Göbekten kaburga kavsine"],
  """Linea alba iki rectus kasının arasında, karın kaslarının aponevrozlarının orta hatta birleşmesiyle oluşan fibröz
  şerittir; göbek bu hattın üzerindedir.""",
  e=["linea-alba"]),

Q("b", OMU, "Omzun yuvarlak görünümünü veren üçgen şeklindeki kas hangisidir?",
  "M. deltoideus", ["M. supraspinatus", "M. trapezius", "M. teres major", "M. pectoralis major"],
  """Deltoid klavikula, akromiyon ve spina scapulae'den başlayıp tuberositas deltoidea'ya tutunur; omzun yuvarlak konturunu
  verir ve kolu abdüksiyona getirir.""",
  e=["m-deltoideus"]),

Q("b", OMU, "Rotator manşeti oluşturan kaslar hangileridir?",
  "Supraspinatus, infraspinatus, teres minor ve subscapularis", ["Supraspinatus, infraspinatus, teres major ve subscapularis",
   "Deltoideus, supraspinatus, infraspinatus ve teres minor", "Supraspinatus, teres major, teres minor ve latissimus dorsi",
   "Subscapularis, pectoralis minor, teres minor ve deltoideus"],
  """Rotator manşet (SITS) humerus başını glenoid çukurda tutan dinamik stabilizatördür. Teres major rotator manşete
  dahil değildir.""",
  e=["m-supraspinatus", "m-infraspinatus", "m-teres-minor", "m-subscapularis"]),

Q("b", KOL, "Kolun önündeki 'pazı' kası hangisidir?",
  "M. biceps brachii", ["M. triceps brachii", "M. brachialis", "M. coracobrachialis", "M. brachioradialis"],
  """Biceps brachii kolun önündeki iki başlı kastır; dirseği büker ve önkolu güçlü biçimde supinasyona getirir.""",
  e=["m-biceps-brachii"]),

Q("b", KOL, "Dirseği uzatan (ekstansiyon) ana kas hangisidir?",
  "M. triceps brachii", ["M. biceps brachii", "M. brachialis", "M. brachioradialis", "M. pronator teres"],
  """Triceps brachii kolun arkasındaki üç başlı kastır ve olecranon'a tutunarak dirseği uzatır; anconeus ona yardım eder.""",
  e=["m-triceps-brachii"]),

Q("b", ONK, "Önkolun ön (fleksör) bölmesindeki kaslar genel olarak hangi hareketi yapar?",
  "El bileğini ve parmakları büker", ["El bileğini ve parmakları uzatır", "Önkolu yalnızca supinasyona getirir",
   "Dirseği uzatır", "Parmakları yalnızca açar"],
  """Önkol ön bölmesi el bileği ve parmak fleksörlerinden ve pronatörlerden oluşur; çoğu epicondylus medialis'ten başlar ve
  n. medianus ile innerve edilir. Arka bölme ekstansörleri içerir.""",
  e=["m-flexor-digitorum-superficialis", "m-flexor-carpi-radialis"]),

Q("b", EL, "Başparmak tabanındaki kas kabartısına ne ad verilir?",
  "Tenar kabartı (eminentia thenaris)", ["Hipotenar kabartı", "Tabakiyer anatomik", "Avuç içi çukuru",
   "İnterosseöz aralık"],
  """Tenar kabartıyı abductor pollicis brevis, flexor pollicis brevis ve opponens pollicis oluşturur; serçe parmak tabanındaki
  kabartı hipotenar kabartıdır.""",
  e=["mm-thenares"]),

Q("b", EL, "Elin küçük (intrinsik) kaslarının çoğunu innerve eden sinir hangisidir?",
  "N. ulnaris", ["N. medianus", "N. radialis", "N. musculocutaneus", "N. axillaris"],
  """N. ulnaris hipotenar kasları, interosseöz kasları, 3.–4. lumbrikalleri, adductor pollicis'i ve FPB'nin derin başını innerve
  eder. N. medianus ise tenar kaslar ile 1.–2. lumbrikalleri innerve eder.""",
  e=["mm-interossei-manus", "mm-hypothenares"]),

Q("b", KAL, "Kalça bölgesinin en büyük ve en yüzeyel kası hangisidir?",
  "M. gluteus maximus", ["M. gluteus medius", "M. gluteus minimus", "M. piriformis", "M. tensor fasciae latae"],
  """Gluteus maximus kalçanın en yüzeyel ve en büyük kasıdır; kalçanın en güçlü ekstansörüdür ve oturur pozisyondan kalkma,
  merdiven çıkma gibi hareketlerde kullanılır.""",
  e=["m-gluteus-maximus"]),

Q("b", KAL, "Kalçayı büken (fleksiyon) en güçlü kas hangisidir?",
  "M. iliopsoas", ["M. gluteus maximus", "M. sartorius", "M. pectineus", "M. gracilis"],
  """İliopsoas (psoas major ve iliacus) trochanter minor'a tutunur ve kalçanın en güçlü fleksörüdür.""",
  e=["m-iliopsoas"]),

Q("b", KAL, "Yürürken tek ayak üzerinde dururken pelvisi dengede tutan kalça abdüktörü hangisidir?",
  "M. gluteus medius", ["M. gluteus maximus", "M. piriformis", "M. adductor longus", "M. iliopsoas"],
  """Gluteus medius (ve minimus) basılan taraftaki kalçayı abdüksiyona getirerek karşı taraf pelvisin düşmesini önler.
  Felcinde Trendelenburg bulgusu ortaya çıkar.""",
  e=["m-gluteus-medius"]),

Q("b", UYL, "Uyluğun önünde dizi uzatan dört başlı kas hangisidir?",
  "M. quadriceps femoris", ["M. biceps femoris", "M. sartorius", "M. gracilis", "M. adductor magnus"],
  """Quadriceps femoris rectus femoris ve üç vastus kasından oluşur; ortak tendonu patellayı sarar ve lig. patellae ile
  tuberositas tibiae'ye tutunarak dizi uzatır.""",
  e=["m-quadriceps-femoris"]),

Q("b", UYL, "Uyluğun arkasındaki hamstring kasları dizde hangi hareketi yapar?",
  "Fleksiyon (bükme)", ["Ekstansiyon (uzatma)", "Abdüksiyon", "Addüksiyon", "Hiçbir hareket yapmaz"],
  """Hamstringler (biceps femoris, semitendinosus, semimembranosus) kalçayı uzatır ve dizi büker.""",
  e=["mm-ischiocrurales"]),

Q("b", UYL, "Uyluğun iç (medial) bölmesindeki kasların ortak işlevi nedir?",
  "Uyluğu orta hatta yaklaştırmak (addüksiyon)", ["Uyluğu uzaklaştırmak (abdüksiyon)", "Dizi uzatmak",
   "Ayağı dorsifleksiyona getirmek", "Kalçayı dış rotasyona getirmek"],
  """Medial bölmedeki adductor longus, brevis, magnus, gracilis ve pectineus uyluğu addüksiyona getirir; çoğu n. obturatorius
  ile innerve edilir.""",
  e=["mm-adductores"]),

Q("b", BAC, "Baldırı oluşturan ve Aşil tendonuyla topuğa tutunan kas grubu hangisidir?",
  "M. triceps surae (gastrocnemius ve soleus)", ["M. tibialis posterior ve FDL", "M. fibularis longus ve brevis",
   "M. tibialis anterior ve EHL", "M. popliteus ve plantaris"],
  """Gastrocnemius'un iki başı ve soleus ortak Aşil tendonuyla tuber calcanei'ye tutunur; ayak bileğinin en güçlü plantar
  fleksörüdür (parmak ucunda yükselme).""",
  e=["m-triceps-surae"]),

Q("b", BAC, "Bacağın dış (lateral) bölmesinde hangi kaslar bulunur?",
  "M. fibularis longus ve m. fibularis brevis", ["M. tibialis anterior ve m. extensor hallucis longus",
   "M. gastrocnemius ve m. soleus", "M. tibialis posterior ve m. flexor digitorum longus", "M. popliteus ve m. plantaris"],
  """Lateral bölme fibularis longus ve brevis'i içerir; ayağı everziyona getirirler ve n. fibularis superficialis ile innerve
  edilirler.""",
  e=["m-fibularis-longus", "m-fibularis-brevis"]),

Q("b", GOG, "İskelet kasları hangi tür kas dokusundan oluşur?",
  "Çizgili, istemli kas", ["Düz, istemsiz kas", "Kalp kası", "Düz, istemli kas", "Çizgisiz kalp kası"],
  """İskelet kasları enine çizgili ve istem dışı değil, istemli kaslardır; somatik motor sinirlerle innerve edilir. Düz kaslar
  iç organ duvarlarında, kalp kası kalpte bulunur."""),

Q("b", BAS, "Vücudun en küçük iskelet kası hangisidir?",
  "M. stapedius", ["M. tensor tympani", "M. levator palpebrae superioris", "M. procerus", "M. arytenoideus"],
  """Stapedius orta kulakta stapese tutunan, yaklaşık 1 mm'lik kastır; yüksek seste stapesin hareketini azaltarak iç kulağı
  korur ve n. facialis ile innerve edilir."""),

Q("b", OMU, "Kasın hareket sırasında sabit kalan kemik tutunma yerine ne ad verilir?",
  "Origo (başlangıç)", ["İnsersiyo (sonlanma)", "Aponevroz", "Kas karnı (venter)", "Tendon kılıfı"],
  """Origo genellikle proksimaldeki sabit tutunma yeridir; insersiyo ise hareket eden kemiğe tutunma yeridir. Kas kasıldığında
  insersiyo origoya yaklaşır."""),

# ------------------------------------------------------------------ fakülte: baş-boyun-gövde
Q("f", BAS, "M. temporalis nereden başlar?",
  "Fossa temporalis ve fascia temporalis'ten", ["Arcus zygomaticus'tan", "Processus pterygoideus'tan",
   "Processus mastoideus'tan", "Linea nuchae superior'dan"],
  """Temporalis fossa temporalis'in tabanından ve onu örten fasyadan başlar; arcus zygomaticus'un altından geçerek processus
  coronoideus'a tutunur.""",
  e=["m-temporalis"]),

Q("f", BAS, "M. buccinator'un başlıca işlevi nedir?",
  "Yanağı dişlere bastırarak çiğnemede besini dişler arasında tutmak ve üflemek", ["Çeneyi kapatmak",
   "Ağız köşesini yukarı kaldırmak", "Dili dışarı çıkarmak", "Ağzı açmak"],
  """Buccinator yanağın kas tabakasıdır; besinin yanakla dişler arasına kaçmasını önler ve üflemede (trompet çalma) yanağı
  sıkar. N. facialis ile innerve edilir; içinden ductus parotideus geçer.""",
  e=["m-buccinator"]),

Q("f", BAS, "Ağız köşesini aşağı çeken (üzgün ifade veren) kas hangisidir?",
  "M. depressor anguli oris", ["M. zygomaticus major", "M. levator labii superioris", "M. risorius", "M. levator anguli oris"],
  """Depressor anguli oris mandibulanın alt kenarından ağız köşesine uzanır ve köşeyi aşağı çeker. Zygomaticus major köşeyi
  yukarı-dışa çeker (gülümseme).""",
  e=["m-depressor-anguli-oris"]),

Q("f", BOY, "Boynu ön ve arka üçgenlere ayıran kas hangisidir?",
  "M. sternocleidomastoideus", ["M. trapezius", "M. omohyoideus", "M. digastricus", "M. scalenus anterior"],
  """SCM'nin önünde ön üçgen, SCM ile trapezius arasında arka üçgen bulunur. Omohyoideus ve digastricus bu üçgenleri daha
  küçük üçgenlere böler.""",
  e=["m-sternocleidomastoideus"]),

Q("f", BOY, "M. scalenus anterior nereden başlar?",
  "C3–C6 transvers çıkıntılarının ön tüberküllerinden", ["C1–C4 transvers çıkıntılarının arka tüberküllerinden",
   "T1–T4 dikenlerinden", "Os occipitale'den", "1. kaburgadan"],
  """Scalenus anterior C3–C6 transvers çıkıntılarının ön tüberküllerinden başlar ve 1. kaburganın skalen tüberkülüne tutunur;
  önünden n. phrenicus iner.""",
  e=["m-scalenus-anterior"]),

Q("f", SIR, "M. trapezius'un hangi lifleri skapulayı geriye (omurgaya doğru) çeker?",
  "Orta (transvers) lifleri", ["Üst (inen) lifleri", "Alt (çıkan) lifleri", "Yalnızca klaviküler lifleri",
   "Hiçbiri; trapezius skapulayı geri çekmez"],
  """Trapeziusun orta lifleri skapulayı retraksiyona getirir. Üst lifler skapulayı kaldırır, alt lifler aşağı çeker; üst ve alt
  lifler birlikte skapulayı yukarı döndürür.""",
  e=["m-trapezius"]),

Q("f", GOG, "Diyafram kasıldığında göğüs boşluğunda ne olur?",
  "Kubbe aşağı iner ve göğsün dikey çapı artar.", ["Kubbe yukarı kalkar ve göğüs hacmi azalır.",
   "Kaburgalar aşağı çekilir ve ekspirasyon olur.", "Göğsün ön-arka çapı azalır.", "Karın içi basınç düşer."],
  """Diyaframın kasılmasıyla kubbesi düzleşir ve aşağı iner; göğüs boşluğunun dikey çapı artarak hava içeri girer.
  Bu sırada karın içi basınç artar.""",
  e=["diaphragma"]),

Q("f", GOG, "M. serratus anterior'un başlıca hareketi hangisidir?",
  "Skapulayı öne çekmek (protraksiyon) ve yukarı döndürmek", ["Skapulayı geri çekmek", "Kolu iç rotasyona getirmek",
   "Kaburgaları aşağı çekmek", "Skapulayı aşağı çekmek ve geri itmek"],
  """Serratus anterior skapulayı göğüs duvarına bastırır, öne çeker (yumruk atma kası) ve trapeziusla birlikte yukarı döndürerek
  kolun 90°'nin üzerine kalkmasını sağlar.""",
  e=["m-serratus-anterior"]),

Q("f", GOG, "M. subclavius'u innerve eden sinir hangisidir?",
  "N. subclavius (C5–C6)", ["N. pectoralis lateralis", "N. thoracicus longus", "N. phrenicus", "N. dorsalis scapulae"],
  """N. subclavius plexus brachialis'in üst gövdesinden çıkan küçük bir daldır; bazen n. phrenicus'a katılan aksesuar frenik
  sinir verir.""",
  e=["m-subclavius"]),

Q("f", KAR, "M. transversus abdominis'in başlıca işlevi nedir?",
  "Karın duvarını sıkıştırarak karın içi basıncı artırmak", ["Gövdeyi öne bükmek", "Gövdeyi yana döndürmek",
   "Pelvisi öne eğmek", "Kaburgaları yukarı kaldırmak"],
  """Transversus abdominis yatay lifleriyle bir kemer gibi karın duvarını sıkar; öksürme, ıkınma, doğum ve zorlu ekspirasyonda
  karın içi basıncı artırır ve gövdeyi stabilize eder.""",
  e=["m-transversus-abdominis"]),

Q("f", KAR, "Canalis inguinalis'in ön duvarını oluşturan başlıca yapı hangisidir?",
  "M. obliquus externus abdominis aponevrozu", ["Fascia transversalis", "Lig. inguinale", "Falx inguinalis (conjoint tendon)",
   "M. rectus abdominis"],
  """İnguinal kanalın ön duvarını dış oblik aponevrozu (dışta iç oblik lifleri destekler), arka duvarını fascia transversalis
  (içte conjoint tendon), tabanını lig. inguinale oluşturur.""",
  e=["m-obliquus-externus", "lig-inguinale"]),

Q("f", KAR, "Aşağıdakilerden hangisi m. levator ani'nin bölümlerinden biri değildir?",
  "M. coccygeus", ["M. puborectalis", "M. pubococcygeus", "M. iliococcygeus", "M. puboprostaticus/pubovaginalis"],
  """Levator ani puborectalis, pubococcygeus (pubovaginalis/puboprostaticus lifleriyle) ve iliococcygeus'tan oluşur.
  Coccygeus pelvis diyafragmasının ayrı bir kasıdır.""",
  e=["m-levator-ani", "diaphragma-pelvis"]),

# ------------------------------------------------------------------ fakülte: üst ekstremite
Q("f", OMU, "M. teres minor'u innerve eden sinir hangisidir?",
  "N. axillaris", ["N. suprascapularis", "N. subscapularis inferior", "N. radialis", "N. thoracodorsalis"],
  """N. axillaris deltoid ve teres minor'u innerve eder. Supraspinatus ve infraspinatus n. suprascapularis, subscapularis ve
  teres major subskapular sinirler ile innerve edilir.""",
  e=["m-teres-minor"]),

Q("f", KOL, "M. brachialis'in innervasyonu hangisidir?",
  "Esas olarak n. musculocutaneus (dış kısmı n. radialis'ten de lif alır)", ["Yalnızca n. radialis", "N. medianus",
   "N. ulnaris", "N. axillaris"],
  """Kolun ön bölmesindeki üç kas (biceps, brachialis, coracobrachialis) n. musculocutaneus ile innerve edilir;
  brachialis'in dış kısmı ek olarak n. radialis'ten lif alır.""",
  e=["m-brachialis"]),

Q("f", KOL, "M. anconeus'un işlevi ve innervasyonu hangisidir?",
  "Dirsek ekstansiyonuna yardım eder – n. radialis", ["Dirseği büker – n. musculocutaneus",
   "Önkolu supinasyona getirir – n. medianus", "El bileğini uzatır – n. ulnaris", "Dirseği büker – n. radialis"],
  """Anconeus lateral epikondilden olecranon'un dış yüzüne uzanan küçük kastır; triceps'e yardım eder ve dirsek eklem kapsülünü
  germe görevi görür.""",
  e=["m-anconeus"]),

Q("f", ONK, "Önkol yüzeyel fleksörlerinin dıştan (radial) içe (ulnar) doğru sırası hangisidir?",
  "Pronator teres, flexor carpi radialis, palmaris longus, flexor carpi ulnaris",
  ["Flexor carpi radialis, pronator teres, flexor carpi ulnaris, palmaris longus",
   "Palmaris longus, flexor carpi radialis, pronator teres, flexor carpi ulnaris",
   "Flexor carpi ulnaris, palmaris longus, flexor carpi radialis, pronator teres",
   "Pronator teres, palmaris longus, flexor carpi radialis, flexor carpi ulnaris"],
  """Sağ eli göğse koyup başparmağı dışta tutarak dört kası sayabilirsiniz: PT, FCR, PL, FCU. Hepsi medial epikondildeki ortak
  fleksör başlangıçtan çıkar; FDS bunların derininde yer alır.""",
  e=["m-pronator-teres", "m-flexor-carpi-radialis", "m-palmaris-longus", "m-flexor-carpi-ulnaris"]),

Q("f", ONK, "FDS ve FDP tendonları parmaklarda nereye tutunur?",
  "FDS orta falanksa, FDP distal falanksa", ["FDS distal falanksa, FDP orta falanksa", "İkisi de proksimal falanksa",
   "FDS metakarp başına, FDP orta falanksa", "İkisi de distal falanksa"],
  """FDS tendonu proksimal falanks düzeyinde ikiye ayrılır (kamper kiazması), FDP tendonu bu ayrıktan geçerek distal falanksa
  ulaşır. Bu nedenle DIP fleksiyonu yalnızca FDP ile yapılır.""",
  e=["m-flexor-digitorum-superficialis", "m-flexor-digitorum-profundus"]),

Q("f", ONK, "Diğer parmaklardan bağımsız olarak işaret parmağını uzatmayı sağlayan kas hangisidir?",
  "M. extensor indicis", ["M. extensor digitorum", "M. extensor digiti minimi", "M. extensor pollicis longus",
   "M. abductor pollicis longus"],
  """Extensor indicis önkolun derin ekstansörlerindendir ve işaret parmağının bağımsız ekstansiyonunu sağlar (işaret etme).
  Tendonu tendon transferlerinde sık kullanılır.""",
  e=["m-extensor-indicis"]),

Q("f", ONK, "Mallet (çekiç) parmak hangi yapının yaralanmasıdır?",
  "Ekstansör tendonun distal falanksa tutunan terminal bölümü", ["FDP tendonunun distal falanksa tutunması",
   "PIP ekleminin volar plağı", "MCP ekleminin kollateral bağı", "Ekstansör tendonun merkezi şeridi"],
  """Parmak ucuna gelen darbeyle ekstansör tendonun distal falanksa tutunan ucu kopar ve hasta DIP eklemini aktif olarak
  uzatamaz. Merkezi şerit yaralanması ise butonyer deformitesi yapar.""",
  e=["m-extensor-digitorum"]),

# ------------------------------------------------------------------ fakülte: alt ekstremite
Q("f", KAL, "M. piriformis'in başlıca hareketi hangisidir?",
  "Kalçanın dış rotasyonu", ["Kalçanın fleksiyonu", "Kalçanın addüksiyonu", "Dizin fleksiyonu", "Kalçanın iç rotasyonu"],
  """Piriformis sakrumun ön yüzünden başlayıp foramen ischiadicum majus'tan geçerek trochanter major'a tutunur; kalçayı dış
  rotasyona, fleksiyondayken abdüksiyona getirir.""",
  e=["m-piriformis"]),

Q("f", KAL, "Kalçanın derin dış rotatörlerinin yukarıdan aşağı sırası hangisidir?",
  "Piriformis, gemellus superior, obturatorius internus, gemellus inferior, quadratus femoris",
  ["Gemellus superior, piriformis, gemellus inferior, obturatorius internus, quadratus femoris",
   "Quadratus femoris, gemellus inferior, obturatorius internus, gemellus superior, piriformis",
   "Piriformis, obturatorius internus, gemellus superior, gemellus inferior, quadratus femoris",
   "Obturatorius internus, piriformis, quadratus femoris, gemellus superior, gemellus inferior"],
  """Gluteus maximus kaldırıldığında yukarıdan aşağı piriformis, gemellus superior, obturatorius internus tendonu, gemellus
  inferior ve quadratus femoris görülür; obturatorius externus daha derindedir.""",
  e=["mm-rotatores-coxae"]),

Q("f", UYL, "M. sartorius'un hareketleri hangileridir?",
  "Kalçayı büker, abdüksiyon ve dış rotasyona getirir; dizi büker", ["Kalçayı uzatır ve dizi uzatır",
   "Yalnızca dizi uzatır", "Kalçayı addüksiyon ve iç rotasyona getirir", "Yalnızca kalçayı büker"],
  """Sartorius bağdaş kurma pozisyonunu sağlayan hareketlerin hepsini yapar: kalça fleksiyonu, abdüksiyonu, dış rotasyonu ve
  diz fleksiyonu. N. femoralis ile innerve edilir.""",
  e=["m-sartorius"]),

Q("f", UYL, "Femoral üçgenin iç (medial) sınırını oluşturan kas hangisidir?",
  "M. adductor longus", ["M. sartorius", "M. pectineus", "M. gracilis", "M. iliopsoas"],
  """Femoral üçgen yukarıda lig. inguinale, dışta sartorius, içte adductor longus'un iç kenarıyla sınırlanır. Tabanını
  iliopsoas, pectineus ve adductor longus yapar.""",
  e=["m-adductor-longus"]),

Q("f", UYL, "Patellar (diz) refleksi hangi spinal segmenti en çok değerlendirir?",
  "L4", ["L2", "L5", "S1", "S2"],
  """Patellar refleks n. femoralis ile L2–L4 segmentlerinden, özellikle L4'ten geçer. Aşil refleksi S1, biseps refleksi C5,
  triseps refleksi C7 segmentini değerlendirir.""",
  e=["m-quadriceps-femoris"]),

Q("f", KOL, "Biseps tendon refleksi hangi spinal segmenti en çok değerlendirir?",
  "C5", ["C7", "C8", "T1", "C3"],
  """Biseps refleksi n. musculocutaneus ile C5–C6, özellikle C5 segmentini değerlendirir. Brakiyoradyal refleks C6, triseps
  refleksi C7 içindir.""",
  e=["m-biceps-brachii"]),

Q("f", BAC, "Aşağıdaki kaslardan hangisi bacağın ön bölmesinde yer almaz?",
  "M. fibularis brevis", ["M. tibialis anterior", "M. extensor hallucis longus", "M. extensor digitorum longus",
   "M. fibularis tertius"],
  """Ön bölmede tibialis anterior, EHL, EDL ve fibularis tertius bulunur ve n. fibularis profundus ile innerve edilir.
  Fibularis brevis lateral bölmededir (n. fibularis superficialis).""",
  e=["m-tibialis-anterior", "m-fibularis-brevis"]),

Q("f", BAC, "M. gastrocnemius'un iki başı nereden başlar?",
  "Femurun medial ve lateral kondillerinin arka yüzünden", ["Tibia ve fibulanın arka yüzünden", "Linea musculi solei'den",
   "Tuber ischiadicum'dan", "Patella ve lig. patellae'den"],
  """Gastrocnemius femur kondillerinden başladığı için diz eklemini de geçer ve dizi bükmeye yardım eder. Soleus tibia ve
  fibuladan başlar ve dizi geçmez.""",
  e=["m-gastrocnemius"]),

Q("f", BAC, "M. popliteus'u innerve eden sinir hangisidir?",
  "N. tibialis", ["N. fibularis communis", "N. femoralis", "N. obturatorius", "N. saphenus"],
  """Popliteus diz çukurunun tabanındaki kastır; tam ekstansiyonda kilitlenen dizi açar ve n. tibialis ile innerve edilir.""",
  e=["m-popliteus"]),

Q("f", AYA, "Ayak tabanı kaslarının birinci (en yüzeyel) tabakasında hangileri bulunur?",
  "M. abductor hallucis, m. flexor digitorum brevis ve m. abductor digiti minimi",
  ["M. quadratus plantae ve mm. lumbricales", "M. flexor hallucis brevis ve m. adductor hallucis",
   "Mm. interossei plantares ve dorsales", "M. extensor digitorum brevis ve m. extensor hallucis brevis"],
  """Ayak tabanı kasları dört tabakadır: 1. abductor hallucis, FDB, abductor digiti minimi; 2. quadratus plantae, lumbrikaller;
  3. FHB, adductor hallucis, FDMB; 4. interosseöz kaslar.""",
  e=["mm-plantares"]),

Q("fv", UYL, "Basketbolda sıçradıktan sonra yere inen oyuncu diz önünde ağrı tarifliyor ve dizini aktif olarak uzatamıyor; patella normalden yukarıda görülüyor. En olası tanı hangisidir?",
  "Patellar tendon (lig. patellae) yırtığı", ["Quadriceps tendon yırtığı", "Ön çapraz bağ yırtığı", "Medial menisküs yırtığı",
   "Patella çıkığı"],
  """Lig. patellae yırtıldığında quadriceps patellayı yukarı çeker (patella alta) ve ekstansör mekanizma bozulduğu için diz
  aktif olarak uzatılamaz. Quadriceps tendon yırtığında ise patella aşağıda kalır (patella baja).""",
  e=["m-quadriceps-femoris"]),

# ------------------------------------------------------------------ TUS
Q("t", BAS, "Damak kaslarından n. mandibularis (V3) ile innerve edilen tek kas hangisidir?",
  "M. tensor veli palatini", ["M. levator veli palatini", "M. palatoglossus", "M. palatopharyngeus", "M. uvulae"],
  """Damak kaslarının hepsi plexus pharyngeus aracılığıyla n. vagus ile innerve edilir; tek istisna 1. ark kökenli tensor veli
  palatini'dir (V3). Tensor tympani de aynı şekilde V3 ile innerve edilir."""),

Q("t", BAS, "Orta kulak kaslarının innervasyonu hangisinde doğru verilmiştir?",
  "M. tensor tympani – n. mandibularis (V3); m. stapedius – n. facialis (VII)",
  ["M. tensor tympani – n. facialis; m. stapedius – n. mandibularis",
   "İkisi de n. facialis", "İkisi de n. glossopharyngeus", "M. tensor tympani – n. vagus; m. stapedius – n. facialis"],
  """Tensor tympani 1. ark kökenlidir (V3), stapedius 2. ark kökenlidir (VII). Fasiyal sinirin stapedius dalından önceki
  lezyonlarında hiperakuzi görülür."""),

Q("t", GOG, "Diyaframın sağ krusu hangi omurlardan başlar?",
  "L1–L3 omur gövdeleri", ["L1–L2 omur gövdeleri", "T10–T12 omur gövdeleri", "L3–L5 omur gövdeleri", "T12–L1 omur gövdeleri"],
  """Sağ krus L1–L3, daha kısa sol krus L1–L2 omur gövdelerinden başlar. Sağ krusun lifleri özofagusu halka gibi çevreleyerek
  hiatus oesophageus'u oluşturur.""",
  e=["diaphragma"]),

Q("t", GOG, "Konjenital diyafram hernisinin en sık tipi ve yeri hangisidir?",
  "Bochdalek hernisi – posterolateral, çoğunlukla solda", ["Morgagni hernisi – anteromedial, çoğunlukla sağda",
   "Hiatal herni – özofageal açıklık", "Bochdalek hernisi – anteromedial, çoğunlukla sağda", "Morgagni hernisi – posterolateral, solda"],
  """Bochdalek hernisi plöroperitoneal zarın kapanmamasıyla posterolateral bölgede (en sık solda) oluşur ve yenidoğanda
  akciğer hipoplazisine yol açar. Morgagni hernisi daha nadir ve anteromedialdir.""",
  e=["diaphragma"]),

Q("t", OMU, "Erb–Duchenne paralizisinde (üst gövde, C5–C6) kolun tipik pozisyonu hangisidir?",
  "Kol addüksiyon ve iç rotasyonda, önkol ekstansiyon ve pronasyonda ('garson bahşiş eli')",
  ["Kol abdüksiyon ve dış rotasyonda, önkol fleksiyonda", "El parmakları pençe şeklinde, kol normal",
   "Düşük el (el bileği fleksiyonda)", "Kol normal, yalnızca başparmak opozisyonu kayıp"],
  """C5–C6 hasarında deltoid, supraspinatus, infraspinatus, biceps ve brachialis felç olur; kol yanda addüksiyon ve iç
  rotasyonda, önkol ekstansiyon ve pronasyonda kalır. Doğum travması ve omuz-boyun açılmasıyla olur.""",
  e=["m-deltoideus", "m-biceps-brachii"]),

Q("t", EL, "Klumpke paralizisinde (alt gövde, C8–T1) en çok etkilenen kaslar hangileridir?",
  "Elin intrinsik kasları", ["Rotator manşet kasları", "Deltoid ve biceps", "Önkol supinatörleri", "Triceps ve anconeus"],
  """C8–T1 köklerinin zedelenmesi (kolun aşırı abdüksiyonla çekilmesi) elin tüm intrinsik kaslarını etkiler ve pençe el
  oluşur; T1 sempatik lifleri tutulursa Horner sendromu eşlik edebilir.""",
  e=["mm-interossei-manus"]),

Q("t", KOL, "Humerus orta 1/3 kırığında n. radialis yaralandığında m. triceps brachii neden genellikle korunur?",
  "Triseps dalları sinir spiral oluğa girmeden önce ayrılır.", ["Triceps n. ulnaris ile innerve edilir.",
   "Triceps n. axillaris ile innerve edilir.", "Sinir spiral olukta tricepsin içinden geçmez.", "Triceps çift innervasyon alır."],
  """N. radialis kolun üst kısmında, sulcus nervi radialis'e girmeden önce tricepsin uzun ve medial başlarına dallarını verir.
  Bu nedenle orta 1/3 kırığında dirsek ekstansiyonu çoğunlukla korunur, düşük el gelişir.""",
  e=["m-triceps-brachii"]),

Q("t", ONK, "Rugby'de rakibin formasını tutarken parmağı zorla uzatılan oyuncuda DIP eklemi aktif olarak bükülemiyor (jersey parmak). Hangi tendon kopmuştur?",
  "M. flexor digitorum profundus", ["M. flexor digitorum superficialis", "Ekstansör tendonun terminal bölümü",
   "M. lumbricalis", "M. interosseus palmaris"],
  """Jersey parmakta FDP tendonu distal falanks tabanından avülse olur; en sık yüzük parmağı etkilenir. DIP fleksiyonunu yalnızca
  FDP yaptığı için bu hareket kaybolur.""",
  e=["m-flexor-digitorum-profundus"]),

Q("t", KAL, "M. quadratus femoris'i innerve eden sinir hangisidir?",
  "N. musculi quadrati femoris (L4–S1)", ["N. gluteus inferior", "N. musculi obturatorii interni", "N. obturatorius",
   "N. ischiadicus'un tibial bölümü"],
  """Quadratus femoris ve gemellus inferior'u sakral pleksustan gelen n. quadratus femoris innerve eder. Obturatorius internus ve
  gemellus superior ise n. obturatorius internus ile innerve edilir.""",
  e=["m-quadratus-femoris"]),

Q("t", UYL, "Femoral üçgenin tabanını (zeminini) oluşturan kaslar hangileridir?",
  "İliopsoas, pectineus ve adductor longus", ["Sartorius ve gracilis", "Vastus medialis ve vastus intermedius",
   "Gluteus medius ve minimus", "Adductor magnus ve semimembranosus"],
  """Femoral üçgenin tabanı dıştan içe iliopsoas, pectineus ve adductor longus tarafından oluşturulur; tavanını fascia lata ve
  fascia cribrosa örter.""",
  e=["m-iliopsoas", "m-pectineus", "m-adductor-longus"]),

Q("t", UYL, "Sprint koşucularında en sık yırtılan hamstring kası hangisidir?",
  "M. biceps femoris'in uzun başı", ["M. semitendinosus", "M. semimembranosus", "M. biceps femoris'in kısa başı",
   "M. adductor magnus'un hamstring bölümü"],
  """Biceps femoris uzun başı, koşunun salınım fazının sonunda eksantrik olarak aşırı gerildiğinden en sık yaralanan hamstring
  kasıdır.""",
  e=["m-biceps-femoris"]),

Q("t", AYA, "M. quadratus plantae'nin işlevi nedir?",
  "FDL tendonunun eğik çekişini düzelterek parmak fleksiyonunu doğrultmak", ["Ayak başparmağını abdüksiyona getirmek",
   "Ayak parmaklarını uzatmak", "İç kemeri yükseltmek", "Ayağı everziyona getirmek"],
  """Quadratus plantae kalkaneustan FDL tendonunun dış kenarına tutunur; FDL'nin malleolus medialis arkasından gelen eğik
  çekişini düzelterek parmakların düz bükülmesini sağlar. N. plantaris lateralis ile innerve edilir.""",
  e=["m-quadratus-plantae"]),

Q("tv", KAL, "Total kalça protezi ameliyatından sonra hastada ayak bileğini kaldıramama (düşük ayak) ve bacağın dış yanında uyuşukluk gelişiyor. En olası hasar hangisidir?",
  "N. ischiadicus'un fibular bölümünün zedelenmesi", ["N. femoralis zedelenmesi", "N. obturatorius zedelenmesi",
   "N. gluteus superior zedelenmesi", "N. tibialis zedelenmesi"],
  """Kalça cerrahisinde siyatik sinirin yüzeyel ve daha az bağ dokusuyla korunan fibular bölümü daha sık zedelenir;
  dorsifleksiyon ve everziyon kaybı ile bacak dış yüzünde duyu kaybı gelişir.""",
  e=["mm-rotatores-coxae"]),
]
