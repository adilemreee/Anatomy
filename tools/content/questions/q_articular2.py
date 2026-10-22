"""More articular questions: ligaments, joint types and injuries."""
from qcommon import Q

KOE = "Kafa ve omurga eklemleri"
UEE = "Üst ekstremite eklemleri"
AEE = "Alt ekstremite eklemleri"
GEN = "Genel yapılar"

questions = [
# ------------------------------------------------------------------ genel
Q("f", GEN, "Aşağıdakilerden hangisi sinovyal eklemin özelliklerinden biri değildir?",
  "Kemik uçlarının fibröz dokuyla birbirine kaynaşmış olması",
  ["Eklem kapsülü", "Sinovyal sıvı", "Hiyalin eklem kıkırdağı", "Eklem boşluğu"],
  """Sinovyal eklemlerde kemik uçları hiyalin kıkırdakla örtülüdür ve bir eklem boşluğu ile birbirinden
  ayrılır; boşluğu sinovyal zar ve fibröz kapsül sarar, sinovyal sıvı besler ve kayganlaştırır. Fibröz
  dokuyla kaynaşma fibröz eklemlerin (sutur, sindesmoz) özelliğidir.""",
  e=["eklem-tipleri"]),

Q("t", GEN, "Hilton yasası neyi ifade eder?",
  "Bir eklemi hareket ettiren kasları innerve eden sinirler o eklemi ve üstündeki deriyi de innerve eder",
  ["Eklemin kanlanması yalnızca kapsülün arterlerinden gelir", "Bir eklemin bağları kasların tersine hareket eder",
   "Her eklem tek bir sinirle innerve edilir", "Eklem kıkırdağı sinirden zengindir"],
  """Hilton yasası, eklem ağrısının neden uzak bölgelere yansıyabildiğini açıklar: örneğin kalça eklemini
  n. obturatorius da innerve ettiği için kalça hastalığı diz iç yanında ağrı yapabilir. Eklem kıkırdağında
  sinir ve damar yoktur.""",
  e=["eklem-tipleri"]),

Q("f", GEN, "Dişlerin alveollere bağlandığı eklem tipi hangisidir?",
  "Gomphosis",
  ["Sutura", "Syndesmosis", "Synchondrosis", "Symphysis"],
  """Gomphosis bir fibröz eklem tipidir: diş kökü periodontal bağ ile alveol soketine çivi gibi tutturulur.
  Suturlar kafatası kemikleri, sindesmoz distal tibiofibular eklem, sinkondroz epifiz plağı, simfiz ise
  symphysis pubica ve intervertebral disk örnekleridir.""",
  e=["eklem-tipleri", "dentes"]),

Q("t", GEN, "Aşağıdakilerden hangisi synchondrosis değildir?",
  "Symphysis pubica",
  ["1. kaburga ile manubrium arasındaki eklem", "Sfeno-oksipital birleşme", "Epifiz plağı",
   "Os coxae'nin Y biçimli kıkırdağı"],
  """Sinkondrozlar hiyalin kıkırdakla oluşan primer kıkırdak eklemlerdir ve çoğu zamanla kemikleşir.
  Symphysis pubica ise fibrokartilaj disk içeren sekonder kıkırdak eklemdir (simfiz); intervertebral diskler
  ve manubriosternal eklem de bu gruptadır.""",
  e=["eklem-tipleri", "symphysis-pubica"]),

# ------------------------------------------------------------------ kafa ve omurga
Q("f", KOE, "Atlanto-oksipital eklemde başlıca hangi hareket olur?",
  "Başın öne-arkaya eğilmesi (‘evet’ hareketi)",
  ["Başın sağa-sola dönmesi (‘hayır’ hareketi)", "Yalnızca rotasyon", "Hiçbir hareket olmaz",
   "Yalnızca lateral fleksiyon"],
  """Oksipital kondiller atlasın üst eklem yüzlerine oturur; bu elipsoid eklem başlıca fleksiyon-ekstansiyona,
  biraz da yana eğilmeye izin verir. Rotasyonun büyük bölümü atlantoaksiyel eklemlerde olur.""",
  e=["ligg-columnae", "atlas"]),

Q("f", KOE, "Lig. nuchae hangi bağın boyundaki devamıdır?",
  "Lig. supraspinale",
  ["Lig. longitudinale anterius", "Lig. flavum", "Membrana tectoria", "Lig. apicis dentis"],
  """Dikensi çıkıntıların uçlarını birleştiren lig. supraspinale C7'nin üstünde genişleyerek protuberantia
  occipitalis externa'ya uzanan üçgen lig. nuchae'yı oluşturur; trapezius ve splenius'un tutunma yüzeyidir.""",
  e=["ligg-columnae"]),

Q("t", KOE, "Membrana tectoria hangi bağın yukarıdaki devamıdır?",
  "Lig. longitudinale posterius",
  ["Lig. longitudinale anterius", "Lig. flavum", "Lig. supraspinale", "Lig. transversum atlantis"],
  """Arka uzunlamasına bağ axis gövdesinden yukarı doğru genişleyerek membrana tectoria adını alır ve clivus'a
  tutunur; dens ile çapraz bağı arkadan örterek omuriliği korur.""",
  e=["ligg-columnae", "axis"]),

Q("f", KOE, "Lig. cruciforme atlantis'in bileşenleri hangileridir?",
  "Lig. transversum atlantis ve fasciculi longitudinales",
  ["Ligg. alaria ve lig. apicis dentis", "Membrana tectoria ve lig. flavum", "Lig. nuchae ve lig. supraspinale",
   "Lig. longitudinale anterius ve posterius"],
  """Çapraz bağın yatay kolu densi atlasın ön kemerine karşı tutan lig. transversum atlantis, dikey kolları
  axis gövdesinden foramen magnum'a uzanan uzunlamasına liflerdir. Alar bağlar densin yanlarından oksipital
  kondillere uzanır ve rotasyonu sınırlar.""",
  e=["ligg-columnae", "atlas", "axis"]),

Q("tv", KOE, """Uzun süredir romatoid artriti olan hastaya entübasyon öncesi boyun fleksiyon-ekstansiyon grafisi
çekiliyor; fleksiyonda atlas ile dens arasındaki mesafenin belirgin arttığı görülüyor. Bu instabiliteden
en çok hangi bağın zayıflaması sorumludur?""",
  "Lig. transversum atlantis",
  ["Lig. flavum", "Lig. nuchae", "Lig. longitudinale anterius", "Lig. interspinale"],
  """Romatoid sinovit densin çevresindeki bağları aşındırır; transvers bağ gevşeyince fleksiyonda atlas öne
  kayar ve dens omuriliğe bası yapabilir. Bu nedenle RA hastalarında entübasyonda boyun fleksiyonundan
  kaçınılır.""",
  e=["ligg-columnae", "atlas", "axis"]),

Q("f", KOE, "İntervertebral disk için hangisi doğrudur?",
  "Dış kısmı fibrokartilaj anulus fibrosus, iç kısmı jelatinöz nucleus pulposus'tur",
  ["Atlas ile axis arasında da disk bulunur", "Erişkinde diskin her yeri iyi damarlanır", "Sinovyal eklemdir",
   "Omurga uzunluğunun yarısını oluşturur"],
  """Diskler simfiz tipi kıkırdak eklemlerdir ve omurga uzunluğunun yaklaşık dörtte birini oluşturur.
  C1–C2 arasında disk yoktur. Erişkinde disk büyük ölçüde damarsızdır ve uç plaklardan difüzyonla beslenir.""",
  e=["discus-intervertebralis"]),

Q("t", KOE, "Omurlar arasındaki faset (zigapofizyal) eklemler hangi tiptedir?",
  "Düzlem tipi sinovyal eklem",
  ["Simfiz", "Sindesmoz", "Küresel sinovyal eklem", "Pivot sinovyal eklem"],
  """Üst ve alt eklem çıkıntıları arasındaki faset eklemler kayma hareketine izin veren düzlem eklemlerdir;
  yüzlerinin yönü bölgenin hareket yeteneğini belirler (boyunda oblik, göğüste koronal, belde sagittal).
  Dejenerasyonları bel ağrısının sık nedenlerindendir.""",
  e=["ligg-columnae", "vertebrae-lumbales"]),

Q("t", KOE, "Ağız açılırken temporomandibular eklemde hareketler hangi sırayla olur?",
  "Önce alt kompartmanda kondil menteşe gibi döner, sonra üst kompartmanda kondil ve disk birlikte öne kayar",
  ["Önce üst kompartmanda kayma, sonra alt kompartmanda dönme olur", "Yalnızca menteşe hareketi olur",
   "Disk kondilden bağımsız olarak geriye kayar", "Kondil tuberculum articulare'nin arkasında sabit kalır"],
  """Eklem diski TME'yi üst (disk–fossa/tuberculum) ve alt (disk–kondil) bölmelere ayırır. Ağız açılmasının
  başında alt bölmede rotasyon, geniş açılmada üst bölmede kondil-disk kompleksinin tuberculum articulare'ye
  doğru öne kayması (translasyon) olur; lateral pterygoid bu kaymayı sağlar.""",
  e=["art-temporomandibularis", "m-pterygoideus-lateralis"]),

Q("f", KOE, "Temporomandibular eklemin eklem yüzleri hangi dokuyla örtülüdür?",
  "Fibrokartilaj",
  ["Hiyalin kıkırdak", "Elastik kıkırdak", "Çıplak kemik", "Periost"],
  """TME, eklem yüzleri hiyalin değil fibrokartilajla örtülü olan atipik bir sinovyal eklemdir; bu özellik
  mandibulanın intramembranöz kökeniyle ilişkilidir. Klavikulanın iki ucundaki eklemler de benzer
  özellik gösterir.""",
  e=["art-temporomandibularis"]),

# ------------------------------------------------------------------ üst ekstremite
Q("t", UEE, "Glenohumeral eklemin en zayıf bölgesi neresidir ve neden?",
  "Alt kısmı; burada rotator manşet kası ve güçlü bağ desteği yoktur",
  ["Üst kısmı; akromiyon desteği yoktur", "Ön kısmı; subscapularis burada bulunmaz", "Arka kısmı; kapsül en ince buradadır",
   "Hiçbir bölgesi zayıf değildir"],
  """Rotator manşet kapsülü üstten, önden ve arkadan sarar; alt kısım yalnızca gevşek kapsül ve alt
  glenohumeral bağla korunur. Abdüksiyonda humerus başı bu bölgeden aşağı-öne çıkar ve n. axillaris
  risk altına girer.""",
  e=["art-humeri"]),

Q("f", UEE, "Lig. coracoclaviculare'nin iki bölümü hangileridir?",
  "Lig. conoideum ve lig. trapezoideum",
  ["Lig. coracoacromiale ve lig. coracohumerale", "Lig. acromioclaviculare superius ve inferius",
   "Lig. costoclaviculare ve lig. interclaviculare", "Lig. glenohumerale superius ve medium"],
  """Korakoklaviküler bağ klavikulayı skapulaya asan en güçlü bağdır: içte konoid (konoid tüberküle),
  dışta trapezoid (trapezoid çizgiye) bölümü vardır. AC çıkığında bu bağ da yırtılırsa klavikula belirgin
  biçimde yukarı kalkar.""",
  e=["art-acromioclavicularis", "clavicula"]),

Q("t", UEE, "Sternoklaviküler eklem için hangisi doğrudur?",
  "İçinde discus articularis bulunan eyer tipi sinovyal eklemdir",
  ["Disk içermeyen küresel eklemdir", "Fibröz bir eklemdir", "Tek eksenli menteşe eklemidir", "Kıkırdak bir eklemdir"],
  """Sternoklaviküler eklem, üst ekstremiteyi gövdeye bağlayan tek gerçek eklemdir; eklem diski eklemi
  ikiye ayırır ve klavikulanın içe doğru kaymasını önleyen güçlü bir yastık görevi görür. Lig.
  costoclaviculare eklemin asıl dengeleyicisidir.""",
  e=["art-sternoclavicularis"]),

Q("t", UEE, "Üçgen fibrokartilaj kompleksi (TFCC) nerede bulunur?",
  "Ulnanın distal ucu ile lunatum ve triquetrum arasında",
  ["Radius ile scaphoideum arasında", "Midkarpal eklemde", "Başparmağın karpometakarpal ekleminde",
   "Proksimal radioulnar eklemde"],
  """TFCC ulna başını karpal kemiklerden ayırır, distal radioulnar eklemin asıl dengeleyicisidir ve el
  bileğine gelen yükün bir kısmını taşır. Elin üzerine düşme ve ulnar deviasyonda zorlanma ile yırtılabilir;
  bileğin ulnar tarafında ağrı yapar.""",
  e=["artt-radioulnares", "art-radiocarpalis"]),

Q("t", UEE, "El bileğinde radial deviasyon (abdüksiyon) ulnar deviasyondan neden daha kısıtlıdır?",
  "Processus styloideus radii daha aşağıya uzanır",
  ["Ulna radiustan daha uzundur", "TFCC radial taraftadır", "Lig. collaterale carpi ulnare zayıftır",
   "Os pisiforme hareketi engeller"],
  """Radiusun stiloid çıkıntısı ulnanınkinden yaklaşık 1 cm aşağıda biter ve scaphoid'e çarparak radial
  deviasyonu sınırlar. Ulna ise karpal kemiklerle doğrudan eklem yapmadığı için ulnar deviasyon daha
  geniştir.""",
  e=["art-radiocarpalis", "radius"]),

Q("f", UEE, "Proksimal ve distal radioulnar eklemler hangi tiptedir?",
  "Pivot (trokoid) sinovyal eklem",
  ["Menteşe eklem", "Eyer eklem", "Düzlem eklem", "Sindesmoz"],
  """Proksimalde radius başı lig. anulare içinde, distalde radius ulna başı çevresinde döner; iki eklem
  birlikte pronasyon ve supinasyonu sağlar. Ortadaki membrana interossea ise bir sindesmozdur.""",
  e=["artt-radioulnares"]),

Q("t", UEE, "Önkol membrana interossea'sının liflerinin yönü hangi işlevi sağlar?",
  "Elden radiusa gelen yükü ulnaya aktarır",
  ["Ulnadan radiusa gelen yükü ele aktarır", "Pronasyonu tamamen engeller", "Yalnızca kaslara origo sağlar",
   "Dirseğin yan bağlarının yerini tutar"],
  """El bileğinde yükün büyük kısmı radiusa, dirsekte ise ulnaya (humeroulnar eklem) geçer. Membran lifleri
  radiustan aşağı-içe ulnaya uzandığı için radiustaki yükü ulnaya aktarır ve kaslara geniş bir origo
  yüzeyi sağlar.""",
  e=["artt-radioulnares"]),

# ------------------------------------------------------------------ alt ekstremite
Q("f", AEE, "Diz eklemi hangi tipe girer?",
  "Modifiye menteşe (bikondiler) sinovyal eklem",
  ["Pivot eklem", "Eyer eklem", "Küresel eklem", "Düzlem eklem"],
  """Diz, femurun iki kondili ile tibia platoları arasında menteşe hareketine ek olarak fleksiyonda bir
  miktar rotasyona izin veren bikondiler eklemdir; patellofemoral eklem de aynı kapsül içindedir.""",
  e=["art-genus"]),

Q("t", AEE, "Ön çapraz bağ (LCA) başlıca hangi hareketi engeller?",
  "Tibianın femura göre öne kaymasını",
  ["Tibianın femura göre arkaya kaymasını", "Dizin valgus zorlanmasını", "Dizin varus zorlanmasını",
   "Patellanın dışa kaymasını"],
  """LCA tibianın area intercondylaris anterior'undan femurun lateral kondilinin iç yüzüne uzanır; tibianın
  öne kaymasını ve aşırı iç rotasyonu sınırlar. Ön çekmece ve Lachman testleriyle değerlendirilir. Arkaya
  kaymayı LCP, valgusu iç, varusu dış yan bağ sınırlar.""",
  ["Arka çapraz bağın görevidir.", "İç kollateral bağın görevidir.", "Dış kollateral bağın görevidir.",
   "Medial patellofemoral bağ ve VMO'nun görevidir."],
  e=["ligg-cruciata"]),

Q("tv", AEE, """Motosiklet kazasında dizi bükülüyken tibianın üst ucuna önden darbe alan hastada, diz 90° fleksiyondayken
tibia femura göre arkaya doğru itilebiliyor. Hangi bağ yaralanmıştır?""",
  "Arka çapraz bağ",
  ["Ön çapraz bağ", "İç kollateral bağ", "Dış kollateral bağ", "Lig. patellae"],
  """Arka çapraz bağ tibianın arkaya kaymasını engeller; ‘ön panel yaralanması’ tipik mekanizmadır. Arka
  çekmece testi ve tibianın arkaya sarkması (sag işareti) pozitiftir. LCP, LCA'dan daha kalın ve güçlüdür.""",
  e=["ligg-cruciata"]),

Q("t", AEE, "Klasik ‘mutsuz üçlü’ (O'Donoghue) diz yaralanmasının bileşenleri hangileridir?",
  "Ön çapraz bağ, iç kollateral bağ ve medial menisküs",
  ["Arka çapraz bağ, dış kollateral bağ ve lateral menisküs", "Ön çapraz bağ, arka çapraz bağ ve lig. patellae",
   "İç kollateral bağ, pes anserinus ve medial menisküs", "Dış kollateral bağ, popliteus tendonu ve lateral menisküs"],
  """Ayak yere sabitken dizin dış yanına gelen darbe valgus ve dış rotasyonla iç yan bağı, ardından ona
  yapışık medial menisküsü ve ön çapraz bağı yırtar. Güncel çalışmalarda lateral menisküsün de sık
  tutulduğu gösterilmiştir.""",
  e=["ligg-cruciata", "ligg-collateralia-genus", "meniscus"]),

Q("t", AEE, "Ayak yere basarken dizin tam ekstansiyona kilitlenmesi (screw-home) sırasında ne olur?",
  "Femur tibia üzerinde iç rotasyon yapar",
  ["Femur tibia üzerinde dış rotasyon yapar", "Tibia femur üzerinde iç rotasyon yapar", "Patella yukarı kayarak kilitlenir",
   "Menisküsler arkaya kayar"],
  """Femurun medial kondili daha uzun olduğundan ekstansiyonun son derecelerinde kapalı zincirde femur iç
  rotasyon yaparak eklemi kilitler; açık zincirde aynı hareket tibianın dış rotasyonu olarak görülür.
  Kilidi m. popliteus femuru dışa döndürerek açar.""",
  e=["art-genus", "m-popliteus"]),

Q("f", AEE, "Bursa suprapatellaris için hangisi doğrudur?",
  "Çoğunlukla diz eklem boşluğuyla bağlantılıdır; eklem içi sıvıda şişer",
  ["Patella ile deri arasında bulunur", "Lig. patellae ile tibia arasındadır", "Pes anserinus'un altındadır",
   "Eklem boşluğundan her zaman ayrıdır"],
  """Suprapatellar bursa kuadriseps tendonunun altında, femurun önünde uzanır ve eklem boşluğunun yukarı
  doğru bir uzantısı gibidir; efüzyonda patellanın üstünde şişlik yapar. Prepatellar bursa patellanın
  önünde, derin infrapatellar bursa lig. patellae'nin arkasındadır.""",
  ["Prepatellar bursayı tanımlar.", "Derin infrapatellar bursayı tanımlar.", "Pes anserinus bursasını tanımlar.",
   "Yanlıştır; çoğunlukla bağlantılıdır."],
  e=["art-genus"]),

Q("f", AEE, "Menisküslerin hangi bölümü kanlanmadığı için yırtıkları zor iyileşir?",
  "Eklem içine bakan iç 2/3'lük bölüm (beyaz bölge)",
  ["Kapsüle yakın dış 1/3'lük bölüm (kırmızı bölge)", "Ön boynuzların tibiaya tutunan uçları",
   "Arka boynuzların tibiaya tutunan uçları", "Kapsüle yapışık kenarlar"],
  """Menisküsler perimenisküsal kapiller ağdan çevresel olarak beslenir; dış üçte bir (kırmızı bölge) iyi
  damarlanır ve onarılabilir, iç kısımlar sinovyal sıvıdan difüzyonla beslenir ve yırtıkları genellikle
  rezeke edilir.""",
  e=["meniscus"]),

Q("tv", AEE, """Futbolcu dizi bükülü ve ayağı yerde sabitken dönerken ani ağrı hissediyor. Ertesi gün eklem çizgisinin
iç tarafında hassasiyet ve dizde zaman zaman takılma-kilitlenme tarif ediyor; McMurray testi pozitif. En olası
yaralanma hangisidir?""",
  "Medial menisküs yırtığı",
  ["Ön çapraz bağ yırtığı", "Patella çıkığı", "Osgood–Schlatter hastalığı", "İliotibial bant sürtünme sendromu"],
  """Fleksiyon ve rotasyon altında yük binen diz menisküsü femur ile tibia arasında sıkıştırır; eklem
  çizgisi hassasiyeti, kilitlenme ve McMurray testi menisküs yırtığını düşündürür. Medial menisküs kapsüle ve
  iç yan bağa yapışık olduğundan daha az hareketlidir ve daha sık yırtılır.""",
  e=["meniscus", "art-genus"]),

Q("t", AEE, "Kalça ekleminin en kararlı (close-packed) pozisyonu hangisidir?",
  "Ekstansiyon, abdüksiyon ve iç rotasyon",
  ["Fleksiyon, addüksiyon ve iç rotasyon", "Fleksiyon, abdüksiyon ve dış rotasyon", "Hafif fleksiyon ve dış rotasyon",
   "Nötral pozisyon"],
  """Ekstansiyon ve iç rotasyonda iliofemoral, pubofemoral ve iskiofemoral bağlar spiral biçimde gerilir ve
  femur başını asetabuluma sıkıca bastırır. Fleksiyon-addüksiyon-iç rotasyon ise arka çıkığa en yatkın
  pozisyondur (ön panel yaralanması).""",
  e=["art-coxae"]),

Q("f", AEE, "Asetabulumun derinliğini artıran fibrokartilaj halka hangisidir?",
  "Labrum acetabuli",
  ["Labrum glenoidale", "Discus articularis", "Menisküs", "Lig. capitis femoris"],
  """Labrum acetabuli asetabulumun kenarına tutunur, alttaki çentiği lig. transversum acetabuli ile
  tamamlanır; femur başını bir vakum gibi tutarak eklemi derinleştirir. Femoroasetabüler sıkışmada
  yırtılabilir.""",
  e=["art-coxae"]),

Q("t", AEE, "Ayak bileğinin iç yan (deltoid) bağı için hangisi doğrudur?",
  "Malleolus medialis'ten talus, calcaneus ve naviculare'ye yelpaze gibi uzanır; eversiyonu sınırlar",
  ["Üç ayrı banttan oluşur ve en sık yırtılan bağdır", "Malleolus lateralis'ten başlar", "İnversiyonu sınırlar",
   "Tibia ile fibula arasında uzanır"],
  """Deltoid bağ çok güçlüdür; zorlu eversiyonda bağ yırtılmak yerine çoğu zaman iç malleolü koparır.
  Dış yan bağ kompleksi (ATFL, CFL, PTFL) ise inversiyon burkulmalarında en sık yaralanan yapıdır.""",
  e=["art-talocruralis"]),

Q("t", AEE, "Lisfranc eklemi hangisidir?",
  "Tarsometatarsal eklemler",
  ["Talonaviküler ve kalkaneokuboid eklemler", "Subtalar eklem", "Metatarsofalangeal eklemler", "İntermetatarsal eklemler"],
  """Lisfranc eklemi cuneiformia ve kuboid ile metatars tabanları arasındadır; 2. metatars tabanı orta
  cuneiforme'ye kilitlenerek eklemin kilit taşı olur. Talonaviküler ve kalkaneokuboid eklemler birlikte
  Chopart (transvers tarsal) eklemini oluşturur.""",
  e=["artt-pedis", "ossa-metatarsi"]),

Q("t", AEE, "Plantar fasyanın ‘ırgat’ (windlass) mekanizması nedir?",
  "Ayak başparmağının dorsifleksiyonu plantar fasyayı gererek medial kavsi yükseltir",
  ["Ayak bileği plantar fleksiyonu fasyayı gevşeterek kavsi düzleştirir",
   "Topuk vuruşunda fasya kopar ve yeniden bağlanır", "Fasya yalnızca ayakta dururken gevşer",
   "Başparmağın plantar fleksiyonu kavsi yükseltir"],
  """Plantar fasya calcaneus'tan parmak tabanlarına uzanır; itme fazında başparmak dorsifleksiyona gelince
  fasya MTF eklemin etrafında bir halat gibi sarılır, topuk ile metatars başlarını yaklaştırır ve kavsi
  yükseltir. Plantar fasiitte sabah ilk adımlardaki ağrı bu gerilimle ilişkilidir.""",
  e=["artt-pedis"]),

Q("f", AEE, "Lig. calcaneonaviculare plantare (‘yaylı bağ’) neyi destekler?",
  "Talus başını ve medial longitudinal kavsi",
  ["Tuber calcanei'yi", "Os cuboideum'u", "5. metatarsı", "Fibulanın alt ucunu"],
  """Yaylı bağ sustentaculum tali'den os naviculare'ye uzanır ve talus başının oturduğu yatağın tabanını
  oluşturur; altından geçen tibialis posterior tendonu ile birlikte medial kavsin anahtar destekçisidir.
  Gevşemesi talus başının aşağı kaymasına ve düztabanlığa yol açar.""",
  e=["artt-pedis", "talus"]),

Q("t", AEE, "Distal tibiofibular eklem hangi tiptedir?",
  "Syndesmosis",
  ["Düzlem tipi sinovyal eklem", "Pivot eklem", "Simfiz", "Gomphosis"],
  """Distal tibiofibular eklem güçlü bağlarla (ön ve arka tibiofibular bağlar, interosseöz bağ) tutturulan
  fibröz bir eklemdir ve ayak bileği zıvanasının bütünlüğünü sağlar. Proksimal tibiofibular eklem ise düzlem
  tipi sinovyal eklemdir.""",
  e=["artt-tibiofibulares"]),

Q("tv", AEE, """Ayak bileği burkulmasıyla gelen hastada iç malleol üzerinde hassasiyet ve şişlik var; ayak bileği
grafisinde kırık yok, ancak dizin hemen altında fibula üst ucunda da ağrı tarif ediyor. Grafide proksimal fibula
kırığı ve tibiofibular aralıkta genişleme saptanıyor. Bu tablonun adı hangisidir?""",
  "Maisonneuve kırığı",
  ["Jones kırığı", "Colles kırığı", "Segond kırığı", "Lisfranc yaralanması"],
  """Dış rotasyon kuvveti deltoid bağı (veya iç malleolü) yırtar, tibiofibular sindesmoz ve membrana
  interossea boyunca yukarı ilerleyerek proksimal fibulayı kırar. Ayak bileği yaralanmalarında fibula
  başının muayenesi bu yüzden atlanmamalıdır.""",
  e=["artt-tibiofibulares", "fibula", "art-talocruralis"]),

Q("f", AEE, "Sakroiliak eklemi en güçlü biçimde bir arada tutan bağ hangisidir?",
  "Ligg. sacroiliaca interossea",
  ["Lig. sacroiliacum anterius", "Lig. iliolumbale", "Lig. sacrotuberale", "Lig. sacrospinale"],
  """İnterosseöz sakroiliak bağlar eklemin arkasında, sakrum ile ilium tüberozitesi arasındaki boşluğu
  dolduran kısa ve çok güçlü liflerdir; vücut ağırlığını sakrumdan iliuma aktarır. Ön bağ incedir;
  sakrotuberal ve sakrospinal bağlar sakrumun öne dönmesini engelleyen yardımcı bağlardır.""",
  e=["art-sacroiliaca"]),

Q("t", AEE, "Aşağıdakilerden hangisi pelvis çıkımının (apertura pelvis inferior) sınırlarına katılmaz?",
  "Promontorium",
  ["Lig. sacrotuberale", "Arcus pubicus", "Tuber ischiadicum", "Os coccygis'in ucu"],
  """Pelvis çıkımı önde arcus pubicus ve simfizin alt kenarı, yanlarda tuber ischiadicum ve lig.
  sacrotuberale, arkada koksiksin ucu ile sınırlıdır. Promontorium pelvis girişinin (apertura superior)
  arka sınırıdır.""",
  e=["ligg-pelvis", "os-coxae"]),
]
