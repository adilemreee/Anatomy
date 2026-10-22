from qcommon import Q, write

KO = "Kafa ve omurga eklemleri"
UE = "Üst ekstremite eklemleri"
AE = "Alt ekstremite eklemleri"
GY = "Genel yapılar"

questions = [
# ------------------------------------------------------------------ Genel
Q("f", GY, "Aşağıdaki eklemlerden hangisi syndesmosis tipindedir?",
  "Distal tibiofibular eklem",
  ["Symphysis pubica", "Birinci sternokostal eklem", "Dişlerin alveollere bağlantısı", "Sutura sagittalis"],
  """Syndesmosis, kemiklerin bir bağ veya zarla bağlandığı fibröz eklemdir: distal tibiofibular eklem ve
  önkol/bacaktaki membrana interossea örnektir. Symphysis pubica fibrokartilajinöz, 1. sternokostal
  eklem sinkondroz, diş–alveol bağlantısı gomphosis, sutura ise kafatasına özgü fibröz eklemdir.""",
  ["Fibrokıkırdak (symphysis).", "Hiyalin kıkırdak (synchondrosis).", "Gomphosis.", "Sutura."],
  e=["eklem-tipleri", "artt-tibiofibulares"]),

Q("f", GY, "Aşağıdaki eklemlerden hangisi eyer (sellar) tipi sinovyal eklemdir?",
  "Başparmağın karpometakarpal eklemi",
  ["Art. radiocarpalis", "Art. humeroulnaris", "Proksimal radioulnar eklem", "Art. acromioclavicularis"],
  """Eyer eklemlerde iki yüz de bir yönde içbükey, diğer yönde dışbükeydir; iki eksende hareket ve
  oppozisyon sağlar. Örnekler: 1. karpometakarpal eklem ve art. sternoclavicularis. Radiokarpal
  eklem elipsoid, humeroulnar menteşe, proksimal radioulnar pivot, akromioklavikular düz eklemdir.""",
  e=["eklem-tipleri", "artt-manus"]),

Q("t", GY, "Aşağıdaki eşleştirmelerden hangisi yanlıştır?",
  "Art. atlantooccipitalis – trokoid (pivot) eklem",
  ["Art. atlantoaxialis mediana – trokoid eklem", "Art. coxae – küresel (sferoid) eklem",
   "Art. genus – bikondiler eklem", "Art. zygapophysialis – düz (plana) eklem"],
  """Atlantooksipital eklem elipsoid (kondiler) tiptedir ve 'evet' hareketini sağlar. Pivot tipi
  eklemler atlantoaksiyel medyan eklem ('hayır' hareketi) ve proksimal/distal radioulnar eklemlerdir.""",
  e=["eklem-tipleri", "atlas", "axis"]),

Q("f", GY, "Büyüme kıkırdağı (epifiz plağı) hangi eklem tipine örnektir?",
  "Synchondrosis (primer kıkırdak eklem)",
  ["Symphysis (sekonder kıkırdak eklem)", "Syndesmosis", "Gomphosis", "Diartroz"],
  """Primer kıkırdak eklemlerde (synchondrosis) kemikler hiyalin kıkırdakla bağlanır ve çoğu zamanla
  kemikleşir: epifiz plağı, 1. kaburga–manubrium eklemi, sfenooksipital sinkondroz. Sekonder kıkırdak
  eklemler (symphysis) fibrokıkırdak içerir ve orta hatta bulunur.""",
  e=["eklem-tipleri"]),

# ------------------------------------------------------------------ Kafa ve omurga
Q("t", KO, "Art. temporomandibularis ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Eklem yüzleri hiyalin kıkırdakla örtülüdür.",
  ["Eklem diski eklemi üst ve alt iki boşluğa ayırır.", "M. pterygoideus lateralis'in bir kısmı diske tutunur.",
   "Ağız açılırken kondil ve disk tuberculum articulare'ye doğru öne kayar.", "Alt eklem boşluğunda menteşe (rotasyon) hareketi olur."],
  """TME'nin eklem yüzleri hiyalin değil fibrokıkırdakla örtülüdür (kemiğin intramembranöz kökenli
  olmasıyla ilişkili). Disk eklemi ikiye böler: alt boşlukta rotasyon, üst boşlukta öne kayma
  (translasyon) olur. Lateral pterygoid kondili ve diski öne çeker.""",
  e=["art-temporomandibularis", "mm-pterygoidei"]),

Q("tv", KO, """Esnerken ağzı açık kalan hasta ağzını kapatamıyor. Mandibula kondili tuberculum
articulare'nin önüne çıkmıştır. Redüksiyonda çene hangi yöne itilir?""",
  "Önce aşağı, sonra arkaya",
  ["Önce yukarı, sonra öne", "Doğrudan arkaya", "Önce yana, sonra yukarı", "Doğrudan yukarı"],
  """TME çıkığı hemen her zaman öne olur; kondil eminensin önünde takılır ve kasların (masseter,
  temporalis, medial pterygoid) spazmı onu orada tutar. Başparmaklar alt azı dişlerine konarak
  çene önce aşağı (eminensin altından geçmek için), sonra arkaya itilir.""",
  e=["art-temporomandibularis", "mandibula"]),

Q("f", KO, "İntervertebral diskin merkezindeki jelatinöz kısım (nucleus pulposus) embriyolojik olarak neyin kalıntısıdır?",
  "Notokord",
  ["Sklerotom", "Nöral krista", "Dermomiyotom", "Ara mezoderm"],
  """Nucleus pulposus notokordun kalıntısıdır; çevresindeki anulus fibrosus ise sklerotom kökenli
  fibrokıkırdak halkalardır. Yaşla su içeriği azalır ve disk yüksekliği düşer.""",
  e=["discus-intervertebralis"]),

Q("t", KO, "Lomber disk hernileri neden en sık posterolateral yönde olur?",
  "Lig. longitudinale posterius orta hatta kalın, yanlarda incedir.",
  ["Anulus fibrosus arkada daha kalındır.", "Lig. flavum diski yanlardan iter.",
   "Nucleus pulposus diskin ön kısmına yakındır.", "Lig. longitudinale anterius arkayı destekler."],
  """Arka uzun bağ omur gövdelerinin arkasında dar bir şerit hâlindedir ve diski yalnızca orta hatta
  destekler. Ayrıca anulus fibrosus arkada daha incedir. Bu nedenle nucleus pulposus en sık
  posterolateralden fıtıklaşır ve sinir kökünü sıkıştırır.""",
  e=["discus-intervertebralis", "ligg-columnae"]),

Q("f", KO, "Omur arkuslarının laminaları arasında uzanan, elastik lif bakımından zengin sarı renkli bağ hangisidir?",
  "Lig. flavum",
  ["Lig. supraspinale", "Lig. interspinale", "Lig. longitudinale posterius", "Lig. nuchae"],
  """Ligg. flava komşu laminaları bağlar; elastik lifler sayesinde fleksiyondan sonra omurganın
  dikleşmesine yardım eder. Lomber ponksiyonda iğne deri, supraspinal ve interspinal bağlardan sonra
  lig. flavum'u geçer ('pop' hissi) ve epidural aralığa ulaşır.""",
  e=["ligg-columnae"]),

Q("t", KO, "Başın 'hayır' hareketi (rotasyon) büyük oranda hangi eklemde gerçekleşir?",
  "Art. atlantoaxialis",
  ["Art. atlantooccipitalis", "C2–C3 faset eklemleri", "Art. temporomandibularis", "C7–T1 diski"],
  """Atlantoaksiyel eklemlerde (bir medyan pivot, iki lateral düz eklem) atlas dens etrafında döner;
  boyun rotasyonunun yaklaşık yarısı burada olur. 'Evet' hareketi atlantooksipital eklemdedir.
  Ligg. alaria aşırı rotasyonu sınırlar.""",
  e=["atlas", "axis", "ligg-columnae"]),

Q("f", KO, "Kaburga başının iki komşu torakal omur gövdesiyle yaptığı eklem hangisidir?",
  "Art. capitis costae",
  ["Art. costotransversaria", "Art. sternocostalis", "Art. costochondralis", "Art. interchondralis"],
  """Tipik kaburganın başı iki komşu omurun gövdesindeki yarım eklem yüzleri ve aradaki diskle art.
  capitis costae'yi; tüberkülü ise alttaki omurun processus transversus'u ile art. costotransversaria'yı
  yapar. Bu iki eklem solunumda kaburganın 'kova sapı' ve 'pompa kolu' hareketlerini sağlar.""",
  e=["artt-thoracis", "costae", "vertebrae-thoracicae"]),

# ------------------------------------------------------------------ Üst ekstremite
Q("f", UE, "Üst ekstremiteyi gövde iskeletine bağlayan tek gerçek (sinovyal) eklem hangisidir?",
  "Art. sternoclavicularis",
  ["Art. acromioclavicularis", "Art. humeri", "Skapulotorasik bağlantı", "Art. costoclavicularis"],
  """Üst ekstremitenin aksiyal iskeletle tek eklemsel bağlantısı sternoklavikular eklemdir. Eyer tipindedir,
  bir eklem diski içerir ve lig. costoclaviculare ile çok güçlü desteklenir; bu nedenle çıkığı nadir,
  klavikula kırığı daha sıktır. Skapulotorasik 'eklem' gerçek bir eklem değildir.""",
  e=["art-sternoclavicularis", "clavicula"]),

Q("fv", UE, """Omzu üzerine düşen rugby oyuncusunda akromiyon ile klavikula arasında basamak var ve
klavikulanın dış ucu yukarıda belirgin. Bu ayrışmanın (tip III) oluşması için hangi bağın da kopmuş
olması gerekir?""",
  "Lig. coracoclaviculare",
  ["Lig. coracoacromiale", "Lig. coracohumerale", "Lig. glenohumerale inferius", "Lig. transversum scapulae superius"],
  """Akromioklavikular ayrılmada yalnız AC bağ koparsa basamak hafiftir. Lig. coracoclaviculare
  (conoid ve trapezoid bölümler) da koparsa skapula ve kol aşağı düşer, klavikula ucu belirgin
  şekilde yukarıda kalır.""",
  e=["art-acromioclavicularis", "clavicula", "scapula"]),

Q("tv", UE, """Voleybolcu, kolu abdüksiyon ve dış rotasyondayken düşüyor. Omuz çıkığı saptanıyor ve
redüksiyon sonrası omuz dış yüzünde his kaybı var. Çıkığın yönü ve yaralanan sinir hangisidir?""",
  "Ön-alt çıkık – n. axillaris",
  ["Arka çıkık – n. suprascapularis", "Üst çıkık – n. musculocutaneus", "Ön-alt çıkık – n. radialis", "Arka çıkık – n. axillaris"],
  """Glenohumeral eklem vücudun en sık çıkan büyük eklemidir; %95'ten fazlası öne-aşağı olur çünkü
  kapsülün alt kısmı en zayıftır. Humerus başı aşağı inerken collum chirurgicum'un hemen altındaki
  n. axillaris gerilir.""",
  e=["art-humeri", "n-axillaris"]),

Q("f", UE, "Glenohumeral eklemin derinliğini artıran fibrokartilajinöz halka hangisidir?",
  "Labrum glenoidale",
  ["Discus articularis", "Meniscus", "Lig. coracohumerale", "Bursa subacromialis"],
  """Cavitas glenoidalis sığdır; çevresindeki labrum glenoidale çukuru derinleştirir. Üst kısmına biceps
  uzun başı tutunur; burada yırtık SLAP lezyonu, ön-alt kısımda yırtık Bankart lezyonu adını alır.""",
  e=["art-humeri", "scapula"]),

Q("tv", UE, """Elli yaşında boyacıda kolunu yana kaldırırken 60–120° arasında ağrı (ağrılı ark) var.
Akromiyon altında sıkışan ve en sık yırtılan rotator manşet tendonu hangisidir?""",
  "M. supraspinatus",
  ["M. infraspinatus", "M. teres minor", "M. subscapularis", "M. teres major"],
  """Supraspinatus tendonu akromiyon, lig. coracoacromiale ve humerus başı arasındaki dar aralıktan
  geçer. Abdüksiyonun orta açılarında sıkışır (subakromiyal sıkışma); kanlanmanın zayıf olduğu bölgede
  dejenerasyon ve yırtık en sık bu tendonda görülür.""",
  e=["art-humeri", "m-supraspinatus"]),

Q("f", UE, "Dirsek ekleminde 'taşıma açısı' (carrying angle) neden oluşur?",
  "Trochlea humeri'nin medial kenarının lateralden daha aşağıda olması",
  ["Radius başının ulnadan uzun olması", "Olecranon'un laterale eğik olması",
   "Lig. collaterale radiale'nin kısa olması", "Capitulum humeri'nin büyük olması"],
  """Ekstansiyonda önkol kola göre dışa açılanır (erkekte ~10°, kadında ~15°). Bunun nedeni trochlea'nın
  medial dudağının daha aşağıya uzanmasıdır. Kubitus valgus/varus bu açının artması/azalmasıdır.""",
  e=["art-cubiti", "humerus"]),

Q("t", UE, "Dirsek eklemi ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Proksimal radioulnar eklem ayrı bir eklem kapsülüne sahiptir.",
  ["Humeroulnar eklem menteşe tipindedir.", "Humeroradial eklemde hem fleksiyon hem rotasyon olur.",
   "Lig. anulare radii radius başını sarar.", "Lig. collaterale ulnare valgus zorlanmasına karşı korur."],
  """Dirsek eklemi humeroulnar, humeroradial ve proksimal radioulnar eklemlerden oluşan bileşik bir
  eklemdir ve üçü tek bir kapsül içindedir. Medial (ulnar) kollateral bağ valgus, lateral (radial)
  kollateral bağ varus zorlanmasına karşı korur.""",
  e=["art-cubiti", "artt-radioulnares"]),

Q("f", UE, "Pronasyon ve supinasyon hareketleri hangi eklemlerde olur?",
  "Proksimal ve distal radioulnar eklemler",
  ["Humeroulnar ve radiokarpal eklemler", "Yalnızca radiokarpal eklem", "Midkarpal eklem", "Humeroradial ve karpometakarpal eklemler"],
  """Pronasyon-supinasyonda radius, proksimalde ulnanın incisura radialis'i içinde, distalde ulna başı
  etrafında döner. İki pivot eklem membrana interossea ile birlikte çalışır.""",
  e=["artt-radioulnares", "radius", "ulna"]),

Q("t", UE, "Art. radiocarpalis'in oluşumuna aşağıdakilerden hangisi doğrudan katılmaz?",
  "Ulna'nın distal ucu",
  ["Radius'un distal eklem yüzü", "Os scaphoideum", "Os lunatum", "Discus articularis (TFCC)"],
  """Radiokarpal eklemi proksimalde radius ve üçgen fibrokıkırdak disk (TFCC), distalde scaphoideum,
  lunatum ve triquetrum yapar. Ulna, disk tarafından karpal kemiklerden ayrıldığı için eklem içine
  doğrudan katılmaz.""",
  e=["art-radiocarpalis", "ulna", "ossa-carpi"]),

Q("f", UE, "Metakarpofalangeal eklemler hangi eklem tipindedir?",
  "Elipsoid (kondiler)",
  ["Menteşe (ginglymus)", "Eyer", "Pivot", "Düz (plana)"],
  """MKF eklemler elipsoid tiptedir: fleksiyon-ekstansiyon ve abdüksiyon-addüksiyon yapılır; aktif
  rotasyon yoktur. İnterfalangeal eklemler ise saf menteşe eklemlerdir.""",
  e=["artt-manus", "phalanges-manus"]),

# ------------------------------------------------------------------ Alt ekstremite
Q("f", AE, "Vücudun en güçlü bağı olarak bilinen ve kalça ekleminin aşırı ekstansiyonunu engelleyen bağ hangisidir?",
  "Lig. iliofemorale",
  ["Lig. pubofemorale", "Lig. ischiofemorale", "Lig. capitis femoris", "Lig. inguinale"],
  """Ters Y biçimli lig. iliofemorale (Bigelow bağı) SIAİ ile linea intertrochanterica arasında uzanır.
  Ayakta dururken gövdenin arkaya düşmesini pasif olarak engeller ve kas enerjisi harcamadan dik
  durmayı sağlar.""",
  e=["art-coxae", "os-coxae", "femur"]),

Q("tv", AE, """Trafik kazasında dizi ön panele çarpan sürücünün bacağı kısalmış, fleksiyon, addüksiyon ve iç
rotasyonda. Kalça çıkığı saptanıyor. Bu çıkıkta en sık yaralanan sinir hangisidir?""",
  "N. ischiadicus",
  ["N. femoralis", "N. obturatorius", "N. gluteus inferior", "N. cutaneus femoris lateralis"],
  """Dizin bükülü olduğu 'dashboard' yaralanmasında femur başı arkaya çıkar (kalça çıkıklarının
  çoğu). Baş arkada n. ischiadicus'a bası yapar veya onu gerer; en sık fibular bölüm etkilenir.""",
  e=["art-coxae", "n-ischiadicus"]),

Q("t", AE, "Lig. capitis femoris içinde seyreden arter genellikle hangi arterin dalıdır?",
  "A. obturatoria",
  ["A. circumflexa femoris medialis", "A. circumflexa femoris lateralis", "A. glutea superior", "A. profunda femoris"],
  """Lig. capitis femoris'in arteri (a. acetabularis) a. obturatoria'nın dalıdır; çocuklukta femur başına
  önemli katkı sağlar, erişkinde katkısı küçüktür. Erişkinde başın asıl beslenmesi a. circumflexa
  femoris medialis'tendir.""",
  e=["art-coxae", "femur"]),

Q("tv", AE, """Futbolcu ani yön değiştirirken dizinden 'pop' sesi geliyor ve diz hızla şişiyor. Muayenede
diz 90° fleksiyondayken tibia öne doğru aşırı kayıyor. Yaralanan yapı hangisidir?""",
  "Lig. cruciatum anterius",
  ["Lig. cruciatum posterius", "Lig. collaterale tibiale", "Meniscus lateralis", "Lig. patellae"],
  """Ön çapraz bağ tibianın femura göre öne kaymasını engeller; ön çekmece ve Lachman testleri pozitif
  olur. Arka çapraz bağ tibianın arkaya kaymasını önler (arka çekmece testi).""",
  e=["ligg-cruciata", "art-genus"]),

Q("t", AE, "Medial menisküsün lateral menisküse göre daha sık yırtılmasının temel nedeni nedir?",
  "Lig. collaterale tibiale'ye sıkıca yapışık olduğu için hareketliliğinin az olması",
  ["Daha küçük ve dairesel olması", "M. popliteus tendonuna yapışması",
   "Kanlanmasının tamamen olmaması", "Lig. cruciatum posterius ile kaynaşmış olması"],
  """Medial menisküs C biçimlidir ve dış kenarı medial kollateral bağa yapışıktır; hareket sırasında
  yer değiştiremediği için yırtılır. Lateral menisküs daha dairesel ve hareketlidir; popliteus tendonu
  onu kollateral bağdan ayırır. 'Mutsuz üçlü': MKB + ÖÇB + medial menisküs.""",
  e=["meniscus", "ligg-collateralia-genus", "art-genus"]),

Q("t", AE, "Tam ekstansiyonda kilitlenmiş dizin fleksiyona başlayabilmesi için kilidi açan kas hangisidir?",
  "M. popliteus",
  ["M. biceps femoris", "M. gastrocnemius", "M. semimembranosus", "M. sartorius"],
  """Tam ekstansiyonun son derecelerinde femur tibia üzerinde içe döner ve diz kilitlenir. Fleksiyonun
  başında m. popliteus femuru dışa (ya da yük taşımıyorsa tibiayı içe) döndürerek kilidi açar.""",
  e=["m-popliteus", "art-genus"]),

Q("f", AE, "Dizin dış yanına gelen darbe ile oluşan valgus zorlanmasında öncelikle hangi bağ zarar görür?",
  "Lig. collaterale tibiale (medial)",
  ["Lig. collaterale fibulare (lateral)", "Lig. cruciatum posterius", "Lig. patellae", "Lig. popliteum obliquum"],
  """Dize dıştan gelen kuvvet medial tarafı gerer (valgus): medial kollateral bağ yırtılır, ağır
  yaralanmada ÖÇB ve medial menisküs de eşlik eder. Lateral kollateral bağ ise varus zorlanmasında
  yaralanır.""",
  e=["ligg-collateralia-genus", "art-genus"]),

Q("tv", AE, """Engebeli yolda ayağı içe burkulan genç kadında lateral malleolün önünde şişlik ve hassasiyet
var. En sık yaralanan bağ hangisidir?""",
  "Lig. talofibulare anterius",
  ["Lig. calcaneofibulare", "Lig. talofibulare posterius", "Lig. deltoideum", "Lig. tibiofibulare anterius"],
  """Ayak bileği burkulmalarının çoğu plantar fleksiyon ve inversiyonda olur; lateral bağların en zayıfı
  olan anterior talofibular bağ ilk yırtılır, ardından kalkaneofibular bağ. Medial deltoid bağ çok
  güçlüdür ve genellikle malleol kırığı ile birlikte yaralanır.""",
  e=["art-talocruralis", "fibula"]),

Q("t", AE, "Ayağın inversiyon ve eversiyon hareketleri başlıca hangi eklemlerde gerçekleşir?",
  "Subtalar ve talokalkaneonaviküler eklemler",
  ["Talokrural eklem", "Tarsometatarsal eklemler", "Metatarsofalangeal eklemler", "Distal tibiofibular eklem"],
  """Talokrural eklem menteşe eklemdir ve dorsifleksiyon-plantar fleksiyon yapar. İnversiyon-eversiyon
  talusun altında, subtalar (talokalkaneal) ve talokalkaneonaviküler eklemlerde; az bir kısmı da
  transvers tarsal (Chopart) eklemde olur.""",
  e=["artt-pedis", "art-talocruralis", "talus"]),

Q("t", AE, "Ayak bileği (talokrural) eklemi hangi pozisyonda en kararlıdır ve neden?",
  "Dorsifleksiyonda; trochlea tali önde daha geniş olduğu için malleoller arasında sıkıca kilitlenir.",
  ["Plantar fleksiyonda; malleoller talusu tam kavradığı için.",
   "Plantar fleksiyonda; deltoid bağ en gergin olduğu için.",
   "İnversiyonda; lateral bağlar gergin olduğu için.",
   "Nötralde; kapsül en gevşek olduğu için."],
  """Trochlea tali önde geniş, arkada dardır. Dorsifleksiyonda geniş ön kısım malleoller arasına girer ve
  eklem kararlıdır. Plantar fleksiyonda dar kısım çatalın içinde kalır, eklem gevşer; bu nedenle burkulmalar
  çoğunlukla plantar fleksiyonda olur.""",
  e=["art-talocruralis", "talus"]),

Q("f", AE, "Art. sacroiliaca için aşağıdakilerden hangisi doğrudur?",
  "Ön bölümü sinovyal, arka bölümü güçlü interosseöz bağlarla bağlı karma bir eklemdir.",
  ["Tamamen fibröz bir eklemdir.", "Küresel bir eklemdir ve geniş hareket sağlar.",
   "Os coccygis ile ilium arasındadır.", "Ankilozan spondilitte etkilenmez."],
  """Sakroiliak eklemin auriküler yüzler arasındaki kısmı sinovyaldir; arkasında vücudun en güçlü
  bağlarından olan ligg. sacroiliaca interossea vardır. Hareketi çok azdır ve ağırlığı gövdeden
  pelvise aktarır. Ankilozan spondilit genellikle bu eklemden başlar (sakroileit).""",
  e=["art-sacroiliaca", "os-sacrum", "os-coxae"]),

Q("f", AE, "Symphysis pubica hangi eklem tipindedir?",
  "Sekonder kıkırdak eklem (fibrokartilajinöz symphysis)",
  ["Sinovyal düz eklem", "Primer kıkırdak eklem (synchondrosis)", "Syndesmosis", "Sutura"],
  """İki pubis kemiği hiyalin kıkırdakla örtülü yüzlerle, aradaki fibrokartilajinöz disk (discus
  interpubicus) aracılığıyla birleşir. Gebelikte hormonların etkisiyle bağlar gevşer ve eklem biraz
  genişler.""",
  e=["symphysis-pubica", "os-coxae"]),

Q("t", AE, "Lig. sacrospinale ve lig. sacrotuberale'nin oluşturduğu açıklıklar için hangisi doğrudur?",
  "Incisura ischiadica major ve minor'u foramen ischiadicum majus ve minus'a çevirirler.",
  ["Foramen obturatum'u kapatırlar.", "Canalis inguinalis'in tabanını yaparlar.",
   "Lacuna musculorum ile lacuna vasorum'u ayırırlar.", "Canalis pudendalis'in duvarını yaparlar."],
  """Bu iki bağ sakrumu ischiuma bağlayarak sakrumun öne dönmesini engeller. Büyük siyatik çentiği
  büyük siyatik deliğe, küçük çentiği küçük siyatik deliğe çevirirler. M. piriformis büyük siyatik
  deliği suprapiriform ve infrapiriform bölümlere ayırır.""",
  e=["ligg-pelvis", "os-coxae", "os-sacrum"]),
]

from q_articular2 import questions as more
from q_articular3 import questions as more3

write("articular", questions + more + more3)
