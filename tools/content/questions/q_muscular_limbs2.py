"""More muscular questions: shoulder, arm, forearm, hand, hip, thigh, leg and foot."""
from qcommon import Q

OMZ = "Omuz kasları"
KOL = "Kol kasları"
ONK = "Önkol kasları"
EL = "El kasları"
KLC = "Kalça kasları"
UYL = "Uyluk kasları"
BCK = "Bacak kasları"
AYK = "Ayak kasları"

questions = [
# ------------------------------------------------------------------ omuz
Q("f", OMZ, "Rotator manşet kaslarından n. suprascapularis ile innerve edilenler hangileridir?",
  "M. supraspinatus ve m. infraspinatus",
  ["M. supraspinatus ve m. teres minor", "M. infraspinatus ve m. teres minor", "M. subscapularis ve m. teres major",
   "M. supraspinatus ve m. subscapularis"],
  """N. suprascapularis incisura scapulae'den geçip supraspinatus'u, ardından spinoglenoid çentikten
  dolaşıp infraspinatus'u innerve eder. Teres minor n. axillaris, subscapularis nn. subscapulares ile
  innerve edilir; teres major rotator manşete dahil değildir.""",
  e=["m-supraspinatus", "m-infraspinatus"]),

Q("tv", OMZ, """Omuz ağrısı olan 62 yaşındaki hastanın kolu pasif olarak 90° abdüksiyona getirilip bırakılınca
hasta kolunu yavaşça indiremiyor ve kol aniden düşüyor. En olası yırtık hangisidir?""",
  "M. supraspinatus tendonu",
  ["M. subscapularis tendonu", "M. biceps brachii'nin uzun başı", "M. teres minor tendonu", "M. deltoideus'un akromiyal lifleri"],
  """Kol düşme testi supraspinatus yırtığını gösterir; tendon akromiyon altındaki dar aralıkta sıkışmaya
  ve dejenerasyona en açık rotator manşet tendonudur. Subscapularis yırtığında ‘lift-off’ ve ‘belly press’
  testleri, teres minor yırtığında dış rotasyon gücü bozulur.""",
  e=["m-supraspinatus"]),

Q("f", OMZ, "Üçgen boşluktan (spatium triangulare: teres minor, teres major ve triseps uzun başı arasında) geçen yapı hangisidir?",
  "A. circumflexa scapulae",
  ["N. axillaris ve a. circumflexa humeri posterior", "N. radialis ve a. profunda brachii", "N. suprascapularis",
   "A. thoracodorsalis"],
  """Üçgen boşluk yalnızca a. circumflexa scapulae'yi içerir; arter skapulanın arkasındaki anastomoz ağına
  katılır. Dört köşeli boşluktan n. axillaris ve a. circumflexa humeri posterior, triseps ile teres major
  arasındaki üçgen aralıktan ise n. radialis ve a. profunda brachii geçer.""",
  ["Dört köşeli boşluktan geçer.", "Teres major'un altındaki üçgen aralıktan geçer.", "İncisura scapulae'den geçer.",
   "Latissimus dorsi'ye eşlik eder; bu boşluktan geçmez."],
  e=["m-teres-minor", "m-teres-major", "m-triceps-brachii"]),

Q("t", OMZ, "Teres major'un alt kenarı ile triseps'in uzun ve lateral başları arasındaki üçgen aralıktan geçen yapılar hangileridir?",
  "N. radialis ve a. profunda brachii",
  ["N. axillaris ve a. circumflexa humeri posterior", "A. circumflexa scapulae", "N. ulnaris ve a. collateralis ulnaris superior",
   "N. musculocutaneus ve a. brachialis"],
  """N. radialis aksilladan kolun arkasına bu aralıktan geçer ve a. profunda brachii ile birlikte
  humerustaki sulcus nervi radialis'e ulaşır; humerus cisim kırıklarında burada yaralanır.""",
  e=["m-triceps-brachii", "m-teres-major"]),

Q("f", OMZ, "M. deltoideus nereye tutunur?",
  "Tuberositas deltoidea humeri",
  ["Tuberculum majus", "Sulcus intertubercularis'in dış dudağı", "Collum chirurgicum humeri", "Epicondylus lateralis humeri"],
  """Deltoid klavikulanın dış üçte biri, akromiyon ve spina scapulae'den başlayıp humerus cisminin dış
  yüzündeki tuberositas deltoidea'ya tutunur. Kolun 15–90° arası abdüksiyonunun asıl kasıdır; n. axillaris
  ile innerve edilir.""",
  e=["m-deltoideus"]),

# ------------------------------------------------------------------ kol
Q("f", KOL, "M. biceps brachii'nin kısa başı nereden başlar?",
  "Processus coracoideus'un ucundan",
  ["Tuberculum supraglenoidale'den", "Tuberculum infraglenoidale'den", "Akromiyondan", "Tuberculum minus'tan"],
  """Kısa baş coracobrachialis ile ortak tendonla processus coracoideus'tan, uzun baş tuberculum
  supraglenoidale ve labrum glenoidale'den başlar; uzun baş tendonu eklem kapsülünün içinden geçerek
  sulcus intertubercularis'e iner.""",
  ["Uzun başın origosudur.", "Triseps uzun başının origosudur.", "Deltoidin origosudur.",
   "Subscapularis'in insersiyosudur."],
  e=["m-biceps-brachii"]),

Q("t", KOL, "Aponeurosis bicipitalis (lacertus fibrosus) için hangisi doğrudur?",
  "Fossa cubitalis'te a. brachialis ve n. medianus'u örter",
  ["N. radialis'i örter", "Tuberositas radii'ye tutunur", "Fossa cubitalis'in tabanını oluşturur",
   "M. brachialis'in tendonudur"],
  """Biseps tendonundan içe doğru ayrılan aponevroz, önkolun derin fasyasına karışır; brakial arter ve
  median siniri örterken v. mediana cubiti'nin altında kalır. Bu nedenle venöz girişimlerde altındaki
  yapıları korur.""",
  ["N. radialis fossa cubitalis'in dış yanında, brachioradialis ile brachialis arasındadır.",
   "Tuberositas radii'ye biseps tendonu tutunur.", "Taban m. brachialis ve m. supinator'dur.",
   "M. biceps brachii'den ayrılır."],
  e=["m-biceps-brachii"]),

Q("f", KOL, "M. brachioradialis nereye tutunur?",
  "Processus styloideus radii'nin tabanına",
  ["Tuberositas radii'ye", "Radius cisminin dış yüzünün ortasına", "Processus styloideus ulnae'ye", "Os scaphoideum'a"],
  """Brachioradialis crista supracondylaris lateralis'ten başlar ve radiusun alt ucuna tutunur. Önkol yarı
  pronasyondayken dirseği büker; n. radialis ile innerve edilen bir dirsek fleksörüdür. Radius cisminin
  ortasına pronator teres tutunur.""",
  e=["m-brachioradialis"]),

# ------------------------------------------------------------------ önkol
Q("f", ONK, "Önkolun yüzeyel fleksör kasları ortak tendonla nereden başlar?",
  "Epicondylus medialis humeri",
  ["Epicondylus lateralis humeri", "Processus coronoideus ulnae", "Olecranon", "Crista supracondylaris lateralis"],
  """Pronator teres, flexor carpi radialis, palmaris longus, flexor digitorum superficialis ve flexor
  carpi ulnaris ortak fleksör tendonla medial epikondilden başlar. Bu tendonun aşırı yüklenmesi medial
  epikondilit (golfçü dirseği) yapar; ekstansörler ise lateral epikondilden başlar.""",
  e=["m-flexor-carpi-radialis", "m-palmaris-longus", "m-flexor-carpi-ulnaris"]),

Q("f", ONK, "Önkol ön bölmesinin en derin tabakasında, distalde bulunan dörtgen biçimli kas hangisidir?",
  "M. pronator quadratus",
  ["M. pronator teres", "M. supinator", "M. flexor pollicis longus", "M. brachioradialis"],
  """Pronator quadratus ulna ve radiusun distal dörtte birlik ön yüzleri arasında uzanır; pronasyonu
  başlatan asıl kastır ve distal radioulnar eklemi bir arada tutar. N. interosseus anterior ile innerve
  edilir.""",
  e=["m-pronator-quadratus"]),

Q("t", ONK, "Supinator kanalında (Frohse arkadı) sıkışan sinir ve tipik bulgusu hangisidir?",
  "N. interosseus posterior – parmak ekstansiyonu kaybı, duyu korunur",
  ["N. radialis'in yüzeyel dalı – yalnızca el sırtında duyu kaybı",
   "N. interosseus anterior – ‘OK’ işareti yapamama",
   "N. ulnaris – pençe el",
   "N. medianus – tenar atrofi ve maymun eli"],
  """N. radialis'in derin dalı m. supinator'un iki başı arasından geçerken (Frohse arkadı) sıkışabilir.
  Motor bir dal olduğu için parmaklar MKF eklemlerden uzatılamaz, ancak duyu kaybı olmaz. ECRL ve
  brachioradialis dalları daha yukarıda ayrıldığından el bileği ekstansiyonu korunur ve radiale sapar.""",
  e=["m-supinator", "m-extensor-digitorum"]),

Q("f", ONK, "M. palmaris longus tendonu el bileğinde nereden geçer?",
  "Retinaculum flexorum'un önünden (karpal tünelin dışından)",
  ["Karpal tünelin içinden", "Guyon kanalından", "Birinci ekstansör bölmeden", "Os pisiforme'nin arkasından"],
  """Palmaris longus tendonu retinakulumun önünden geçip aponeurosis palmaris'e devam eder; kişilerin
  %10–15'inde bulunmaz ve tendon greftlerinde sık kullanılır. Bileğin ortasında, n. medianus'un hemen
  önünde ele gelir.""",
  e=["m-palmaris-longus"]),

Q("t", ONK, "El bileğinin dorsal yüzündeki 1. ekstansör bölmede bulunan tendonlar hangileridir?",
  "M. abductor pollicis longus ve m. extensor pollicis brevis",
  ["M. extensor carpi radialis longus ve brevis", "M. extensor pollicis longus", "M. extensor digitorum ve m. extensor indicis",
   "M. extensor carpi ulnaris"],
  """Ekstansör retinakulum altındaki bölmeler radialden ulnara: 1) APL–EPB, 2) ECRL–ECRB, 3) EPL,
  4) ED–EI, 5) EDM, 6) ECU. Birinci bölmenin tenosinoviti de Quervain hastalığıdır.""",
  ["2. bölmededir.", "3. bölmededir.", "4. bölmededir.", "6. bölmededir."],
  e=["m-abductor-pollicis-longus", "m-extensor-pollicis-brevis"]),

Q("f", ONK, "Tuberculum dorsale radii (Lister tüberkülü) çevresinde yön değiştiren tendon hangisidir?",
  "M. extensor pollicis longus",
  ["M. extensor pollicis brevis", "M. abductor pollicis longus", "M. extensor carpi radialis brevis", "M. extensor digitorum"],
  """EPL tendonu 3. bölmede Lister tüberkülünü bir makara gibi kullanarak başparmağa yönelir. Distal radius
  kırıklarından sonra bu noktada sürtünme ve kanlanma bozukluğu nedeniyle geç rüptür görülebilir.""",
  e=["m-extensor-pollicis-longus"]),

# ------------------------------------------------------------------ el
Q("f", EL, "Mm. lumbricales manus nereden başlar?",
  "M. flexor digitorum profundus tendonlarından",
  ["M. flexor digitorum superficialis tendonlarından", "Metakarpların yan yüzlerinden", "Retinaculum flexorum'dan",
   "Aponeurosis palmaris'ten"],
  """Lumbrikaller derin fleksör tendonlarından başlar ve ekstansör aponevrozun radial kenarına tutunur;
  MKF eklemleri büküp IF eklemleri uzatırlar. 1.–2. lumbrikaller n. medianus, 3.–4. n. ulnaris ile
  innerve edilir. Metakarplardan interosseöz kaslar başlar.""",
  e=["mm-lumbricales-manus"]),

Q("t", EL, "Guyon kanalını (canalis ulnaris) sınırlayan kemik yapılar hangileridir?",
  "Os pisiforme ve hamulus ossis hamati",
  ["Os scaphoideum ve os trapezium", "Os lunatum ve os capitatum", "Os triquetrum ve os lunatum",
   "Processus styloideus ulnae ve os triquetrum"],
  """Guyon kanalı pisiform (iç) ile hamatın çengeli (dış) arasında, lig. carpi palmare ile retinaculum
  flexorum arasında kalır; içinden n. ulnaris ve a. ulnaris geçer. Bisiklet sürücülerinde bası sık görülür;
  dorsal kutanöz dal kanala girmediğinden el sırtı duyusu korunur.""",
  e=["os-pisiforme", "os-hamatum", "mm-hypothenares"]),

Q("f", EL, "Başparmağın opozisyonunu sağlayan asıl kas hangisidir?",
  "M. opponens pollicis",
  ["M. adductor pollicis", "M. abductor pollicis longus", "M. flexor pollicis longus", "M. extensor pollicis brevis"],
  """Opponens pollicis 1. metakarpı öne, içe çekip iç rotasyona getirerek başparmak pulpasını diğer
  parmaklarla karşılaştırır. N. medianus'un r. recurrens'i ile innerve edilir; bu dalın yaralanmasında
  opozisyon kaybolur.""",
  e=["m-opponens-pollicis", "mm-thenares"]),

Q("tv", EL, """Elinin iç kenarına cam batan hastada n. ulnaris'in yalnızca derin dalı kesilmiştir. Aşağıdaki
bulgulardan hangisi beklenmez?""",
  "Hipotenar bölgede ve serçe parmakta duyu kaybı",
  ["Parmaklar arasında kâğıt tutmada güçsüzlük", "Pozitif Froment işareti", "1. dorsal interosseöz kasta atrofi",
   "Başparmak addüksiyonunda güçsüzlük"],
  """N. ulnaris'in derin dalı yalnızca motordur: hipotenar kasları, interosseöz kasları, 3.–4. lumbrikalleri,
  adductor pollicis'i ve FPB'nin derin başını innerve eder. Hipotenar deri ve 5. parmak duyusu yüzeyel
  dal ile taşındığından korunur.""",
  e=["mm-interossei-manus", "m-adductor-pollicis", "mm-hypothenares"]),

# ------------------------------------------------------------------ kalça
Q("f", KLC, "M. gluteus maximus nereye tutunur?",
  "Tractus iliotibialis ve tuberositas glutea",
  ["Trochanter major'un dış yüzü", "Trochanter major'un ön yüzü", "Trochanter minor", "Linea aspera'nın iç dudağı"],
  """Gluteus maximus'un yüzeyel lifleri tractus iliotibialis'e, derin alt lifleri femurdaki tuberositas
  glutea'ya tutunur. Kalçanın güçlü ekstansörü ve dış rotatorudur; n. gluteus inferior ile innerve edilir.""",
  ["M. gluteus medius'un tutunma yeridir.", "M. gluteus minimus'un tutunma yeridir.", "M. iliopsoas'ın tutunma yeridir.",
   "Addüktörlerin tutunma yeridir."],
  e=["m-gluteus-maximus", "tractus-iliotibialis"]),

Q("t", KLC, "Trochanter major'un ön yüzüne tutunan kas hangisidir?",
  "M. gluteus minimus",
  ["M. gluteus medius", "M. piriformis", "M. obturatorius externus", "M. quadratus femoris"],
  """Gluteus minimus trochanter major'un ön yüzüne, medius dış yüzüne, piriformis üst kenarına tutunur.
  Obturator externus fossa trochanterica'ya, quadratus femoris crista intertrochanterica'daki tuberculum
  quadratum'a yapışır.""",
  e=["m-gluteus-minimus"]),

Q("t", KLC, "Tendonu foramen ischiadicum minus'tan geçen kalça dış rotatoru hangisidir?",
  "M. obturatorius internus",
  ["M. piriformis", "M. obturatorius externus", "M. quadratus femoris", "M. gemellus inferior"],
  """Obturator internus pelvisin içinden başlar; tendonu küçük siyatik delikten çıkarken incisura ischiadica
  minor üzerinde dik açıyla döner ve gemelli kaslar arasında trochanter major'a uzanır. Piriformis büyük
  siyatik delikten geçer; diğerleri pelvis dışındadır.""",
  e=["m-obturator-internus"]),

Q("tv", KLC, """Uzun süre sert zeminde oturan hastada kalçadan bacağın arkasına yayılan ağrı var; kalça
fleksiyon, addüksiyon ve iç rotasyondayken ağrı artıyor, bel MR'ı normal. En olası tanı hangisidir?""",
  "Piriformis sendromu",
  ["Lomber disk hernisi", "Trokanterik bursit", "Meraljia parestetika", "Tarsal tünel sendromu"],
  """N. ischiadicus çoğunlukla piriformis'in altından (bazen içinden) geçer; kasın gerilmesi veya
  hipertrofisi siniri sıkıştırarak bel kaynaklı olmayan siyatalji yapar. FAIR pozisyonu (fleksiyon,
  addüksiyon, iç rotasyon) kası gerdiği için ağrıyı artırır.""",
  e=["m-piriformis"]),

# ------------------------------------------------------------------ uyluk
Q("f", UYL, "Canalis adductorius'un tavanını (ön-iç duvarını) örten kas hangisidir?",
  "M. sartorius",
  ["M. adductor longus", "M. vastus medialis", "M. gracilis", "M. adductor magnus"],
  """Hunter kanalının dış duvarı vastus medialis, arka duvarı adductor longus ve magnus'tur; tavanı
  vastoaddüktör membran ve onun üzerindeki sartorius oluşturur. Kanaldan a. ve v. femoralis, n. saphenus
  ve vastus medialis'in siniri geçer.""",
  ["Kanalın arka duvarıdır.", "Kanalın dış duvarıdır.", "Kanalla ilişkisi yoktur.", "Kanalın arka duvarıdır."],
  e=["m-sartorius", "mm-adductores"]),

Q("f", UYL, "M. gracilis nereye tutunur?",
  "Tibianın üst iç yüzüne (pes anserinus)",
  ["Linea aspera'ya", "Tuberculum adductorium'a", "Condylus medialis femoris'e", "Caput fibulae'ye"],
  """Gracilis pubisin alt kolundan başlayan, uyluğun iç yüzündeki uzun ince kastır; sartorius ve
  semitendinosus ile birlikte pes anserinus'u oluşturur. Hem kalçayı addüksiyona hem dizi fleksiyona
  getirir; n. obturatorius ile innerve edilir.""",
  e=["m-gracilis"]),

Q("t", UYL, "Vastus medialis'in alt eğik liflerinin (VMO) temel işlevi hangisidir?",
  "Patellanın dışa kaymasını önlemek",
  ["Dizin fleksiyonunu başlatmak", "Kalçayı fleksiyona getirmek", "Tibiayı iç rotasyona getirmek",
   "Bursa suprapatellaris'i yukarı çekmek"],
  """VMO lifleri patellaya içten ve yataya yakın bir açıyla tutunur; kuadrisepsin dışa çeken bileşenini
  dengeleyerek patellayı trokleada tutar. Zayıflığı patellofemoral ağrı ve lateral patella çıkığına zemin
  hazırlar. Bursayı yukarı çeken kas m. articularis genus'tur.""",
  e=["m-vastus-medialis", "patella"]),

Q("f", UYL, "Fossa poplitea'nın üst-iç sınırını oluşturan kaslar hangileridir?",
  "M. semitendinosus ve m. semimembranosus",
  ["M. biceps femoris", "M. gastrocnemius'un iki başı", "M. plantaris ve gastrocnemius'un lateral başı",
   "M. sartorius ve m. gracilis"],
  """Popliteal çukurun üst-iç sınırı semimembranosus ve semitendinosus, üst-dış sınırı biceps femoris,
  alt sınırları gastrocnemius'un medial ve lateral başlarıdır (lateral başa plantaris eşlik eder).""",
  ["Üst-dış sınırdır.", "Alt sınırlardır.", "Alt-dış sınırdadır.", "Fossanın sınırına katılmazlar."],
  e=["m-semitendinosus", "m-semimembranosus"]),

Q("t", UYL, "Hamstring kaslarının ortak özelliği hangisidir?",
  "Tuber ischiadicum'dan başlarlar ve hem kalça hem diz eklemini geçerler",
  ["Hepsi n. femoralis ile innerve edilir", "Hepsi caput fibulae'ye tutunur", "Kalçayı fleksiyona getirirler",
   "Biceps femoris'in kısa başı da bu ölçütleri tam karşılar"],
  """Gerçek hamstringler (semitendinosus, semimembranosus, biceps femoris uzun başı ve adductor magnus'un
  hamstring bölümü) iskial tüberozden başlar, kalçayı ekstansiyona ve dizi fleksiyona getirir ve n.
  ischiadicus'un tibial bölümüyle innerve edilir. Biceps femoris kısa başı linea aspera'dan başlar,
  yalnızca dizi geçer ve fibular bölümle innerve edilir.""",
  e=["mm-ischiocrurales", "m-semitendinosus", "m-biceps-femoris"]),

Q("t", UYL, "Trigonum femorale içinde yapıların dıştan içe sıralaması hangisidir?",
  "N. femoralis, a. femoralis, v. femoralis, canalis femoralis",
  ["A. femoralis, n. femoralis, v. femoralis, canalis femoralis", "V. femoralis, a. femoralis, n. femoralis, canalis femoralis",
   "N. femoralis, v. femoralis, a. femoralis, canalis femoralis", "Canalis femoralis, v. femoralis, a. femoralis, n. femoralis"],
  """Dıştan içe ‘NAVEL’: sinir, arter, ven, boşluk (canalis femoralis) ve lenfatikler. Femoral kılıf
  arter, ven ve kanalı sarar; sinir kılıfın dışında kalır. Femoral fıtık, canalis femoralis'ten
  geçer ve venin iç yanında yer alır.""",
  e=["m-sartorius", "m-adductor-longus"]),

Q("tv", UYL, """Pelvik cerrahi sonrası hastanın uyluğunun iç yüzünün ortasında duyu kaybı var; bacak bacak
üstüne atmakta güçlük çekiyor ve yürürken bacağı dışa savruluyor. Hangi sinir hasar görmüştür?""",
  "N. obturatorius",
  ["N. femoralis", "N. gluteus superior", "N. ischiadicus", "N. cutaneus femoris lateralis"],
  """N. obturatorius pelvisin yan duvarında, ovaryum ve pelvik lenf düğümlerine komşu seyreder; canalis
  obturatorius'tan çıkıp addüktör kasları ve uyluğun iç yüzünün bir bölümünün derisini innerve eder.
  Hasarında addüksiyon zayıflar ve yürüyüşte bacak dışa savrulur.""",
  ["Kuadrisepsi ve uyluğun ön yüzünü innerve eder.", "Gluteus medius ve minimus'u innerve eder; Trendelenburg yapar.",
   "Hamstringleri ve diz altını innerve eder.", "Yalnızca uyluğun dış yüzünün duyusunu alır."],
  e=["mm-adductores", "m-adductor-longus", "m-gracilis"]),

Q("f", UYL, "Tractus iliotibialis'e tutunan kaslar hangileridir?",
  "M. tensor fasciae latae ve m. gluteus maximus",
  ["M. gluteus medius ve m. gluteus minimus", "M. sartorius ve m. rectus femoris", "M. piriformis ve m. obturatorius internus",
   "M. biceps femoris ve m. vastus lateralis"],
  """İliotibial bant fascia lata'nın dış yüzdeki kalınlaşmasıdır; üstte TFL ve gluteus maximus'un yüzeyel
  lifleri ona katılır, altta tibianın Gerdy tüberkülüne tutunur. Ayakta dururken dizin dış yanını ve
  kalçayı dengeler.""",
  e=["tractus-iliotibialis", "m-tensor-fasciae-latae", "m-gluteus-maximus"]),

Q("t", UYL, "İliotibial bant sürtünme sendromunda ağrı en sık nerede hissedilir?",
  "Femurun lateral epikondili üzerinde, dizin dış yanında",
  ["Tuberositas tibiae üzerinde", "Pes anserinus üzerinde", "Trochanter major üzerinde", "Patellanın alt ucunda"],
  """Koşucularda diz 20–30° fleksiyondayken bant lateral epikondilin üzerinden öne-arkaya kayar ve
  tekrarlayan sürtünme dizin dış yanında ağrıya yol açar. Pes anserinus bursiti iç yanda, Osgood–Schlatter
  tüberositas tibiae'de, jumper's knee patellanın alt ucunda ağrı yapar.""",
  e=["tractus-iliotibialis"]),

# ------------------------------------------------------------------ bacak
Q("t", BCK, "Fossa poplitea'da yüzeyelden derine yapıların sıralaması hangisidir?",
  "N. tibialis – v. poplitea – a. poplitea",
  ["A. poplitea – v. poplitea – n. tibialis", "V. poplitea – n. tibialis – a. poplitea",
   "N. tibialis – a. poplitea – v. poplitea", "A. poplitea – n. tibialis – v. poplitea"],
  """Popliteal çukurda en yüzeyelde n. tibialis, onun derininde v. poplitea, en derinde ve femura en
  yakın a. poplitea bulunur. Bu nedenle suprakondiler femur kırıklarında arter en çok risk altındadır.""",
  e=["m-gastrocnemius", "m-popliteus"]),

Q("f", BCK, "M. popliteus nereden başlar?",
  "Condylus lateralis femoris'in dış yüzünden (ve lateral menisküsten)",
  ["Condylus medialis femoris'ten", "Caput fibulae'den", "Tibiadaki linea musculi solei'den", "Patellanın alt ucundan"],
  """Popliteus tendonu eklem kapsülünün içinden geçerek femurun lateral kondiline tutunur; kas tibianın
  arka yüzüne, linea musculi solei'nin üstüne yapışır. Tam ekstansiyonda kilitlenen dizi, femuru dışa
  döndürerek açar; lateral menisküsü geriye çekerek sıkışmasını önler.""",
  e=["m-popliteus"]),

Q("t", BCK, "Ayağın en güçlü invertörü olan ve medial longitudinal kavsi dinamik olarak destekleyen kas hangisidir?",
  "M. tibialis posterior",
  ["M. tibialis anterior", "M. fibularis longus", "M. flexor hallucis longus", "M. extensor hallucis longus"],
  """Tibialis posterior tendonu iç malleolün arkasından geçip tuberositas ossis navicularis ve diğer
  tarsal kemiklerin plantar yüzüne yayılır. Tendon disfonksiyonu erişkinlerde edinsel düztabanlığın en
  sık nedenidir; hasta tek ayak üstünde parmak ucuna kalkamaz.""",
  e=["m-tibialis-posterior"]),

Q("f", BCK, "M. fibularis longus tendonu ayak tabanında nereye tutunur?",
  "Os cuneiforme mediale ve 1. metatarsın tabanına",
  ["5. metatarsın tuberositasına", "Tuberositas ossis navicularis'e", "Os cuboideum'un dış yüzüne", "2. metatarsın tabanına"],
  """Fibularis longus tendonu lateral malleolün arkasından, sonra kuboidin plantar oluğundan ayak tabanını
  çaprazlayarak iç tarafa ulaşır; ayağı plantar fleksiyon ve eversiyona getirir, transvers kavsi destekler.
  5. metatars tuberositasına fibularis brevis tutunur.""",
  ["M. fibularis brevis'in tutunma yeridir.", "M. tibialis posterior'un ana tutunma yeridir.",
   "Tendon kuboidin altındaki oluktan geçer; tutunmaz.", "Bu kasın tutunma yeri değildir."],
  e=["m-fibularis-longus"]),

Q("t", BCK, "Ayağı aşağıdan ‘üzengi’ gibi destekleyen tendon çifti hangisidir?",
  "M. tibialis anterior ve m. fibularis longus",
  ["M. tibialis posterior ve m. flexor hallucis longus", "M. fibularis brevis ve m. fibularis tertius",
   "M. extensor digitorum longus ve m. extensor hallucis longus", "M. gastrocnemius ve m. soleus"],
  """Tibialis anterior iç taraftan, fibularis longus dış taraftan os cuneiforme mediale ve 1. metatars
  tabanına tutunur; iki tendon birlikte ayağın altından bir üzengi oluşturarak transvers ve medial
  kavsi askıya alır, inversiyon ve eversiyonu dengeler.""",
  e=["m-tibialis-anterior", "m-fibularis-longus"]),

Q("f", BCK, "M. soleus için hangisi doğrudur?",
  "Diz bükülüyken ayak bileğinin başlıca plantar fleksörüdür",
  ["Diz ve ayak bileği eklemlerini birlikte geçer", "Femur kondillerinden başlar", "N. fibularis profundus ile innerve edilir",
   "Ayağı dorsifleksiyona getirir"],
  """Soleus tibia ve fibuladan başlar, yalnızca ayak bileğini geçer. Diz fleksiyondayken gastrocnemius
  gevşediğinden plantar fleksiyonu büyük ölçüde soleus sağlar; postüral bir kas olarak ayakta dururken
  sürekli çalışır ve n. tibialis ile innerve edilir.""",
  e=["m-soleus", "m-triceps-surae"]),

Q("tv", BCK, """Uzun koşulardan sonra topuğun iç yanında ve ayak tabanında yanma-uyuşma tarif eden hastada iç
malleolün arka-alt kısmına perküsyonla parestezi oluşuyor. Sıkışan sinir hangisidir?""",
  "N. tibialis",
  ["N. fibularis profundus", "N. suralis", "N. saphenus", "N. fibularis superficialis"],
  """Tarsal tünel sendromunda n. tibialis veya plantar dalları, iç malleol ile calcaneus arasında
  retinaculum musculorum flexorum altında sıkışır; ayak tabanında duyu bozukluğu ve intrinsik kas
  zayıflığı olur. Ön tarsal tünelde n. fibularis profundus sıkışır.""",
  e=["m-tibialis-posterior", "m-abductor-hallucis"]),

# ------------------------------------------------------------------ ayak
Q("t", AYK, "Ayak tabanı kaslarının ikinci tabakasında hangileri bulunur?",
  "M. quadratus plantae, mm. lumbricales ve FDL ile FHL tendonları",
  ["M. abductor hallucis, m. flexor digitorum brevis ve m. abductor digiti minimi",
   "M. flexor hallucis brevis, m. adductor hallucis ve m. flexor digiti minimi brevis",
   "Mm. interossei ile fibularis longus ve tibialis posterior tendonları",
   "M. quadratus plantae ve m. abductor hallucis"],
  """Ayak tabanının dört tabakası: 1) abductor hallucis, FDB, abductor digiti minimi; 2) quadratus
  plantae, lumbrikaller, FDL ve FHL tendonları; 3) FHB, adductor hallucis, FDMB; 4) interosseöz
  kaslar ile fibularis longus ve tibialis posterior tendonları.""",
  ["1. tabakadır.", "3. tabakadır.", "4. tabakadır.", "Farklı tabakalardan iki kastır."],
  e=["m-quadratus-plantae", "mm-lumbricales-pedis", "mm-plantares"]),

Q("f", AYK, "Ayakta parmakların abdüksiyon–addüksiyon ekseni hangi parmaktan geçer?",
  "2. parmaktan",
  ["1. parmaktan", "3. parmaktan", "4. parmaktan", "5. parmaktan"],
  """Ayakta dorsal interosseöz kaslar parmakları 2. parmak ekseninden uzaklaştırır, plantar interosseöz
  kaslar yaklaştırır. Elde bu eksen 3. parmaktır.""",
  e=["mm-interossei-dorsales-pedis", "mm-interossei-plantares"]),

Q("f", AYK, "Ayak sırtındaki kısa ekstansör kaslar nereden başlar?",
  "Calcaneus'un üst-dış yüzünden (sinus tarsi'nin önü)",
  ["Talusun boynundan", "Os naviculare'den", "Metatarsların tabanlarından", "Fibulanın alt ucundan"],
  """M. extensor digitorum brevis ve m. extensor hallucis brevis calcaneus'un üst-dış yüzünden başlar;
  ayak sırtının dış yanında yumuşak bir kitle olarak ele gelir ve ödem ya da kitle ile karışabilir.
  İkisi de n. fibularis profundus ile innerve edilir.""",
  e=["m-extensor-digitorum-brevis", "m-extensor-hallucis-brevis"]),
]
