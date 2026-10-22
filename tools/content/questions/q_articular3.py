"""Articular questions, third set: basic terms and movements, the ligaments of
each joint, the foot joints and arches, and new TUS points."""
from qcommon import Q

KO = "Kafa ve omurga eklemleri"
UE = "Üst ekstremite eklemleri"
AE = "Alt ekstremite eklemleri"
GY = "Genel yapılar"

questions = [
# ------------------------------------------------------------------ temel
Q("b", GY, "Bağlar (ligamentler) genel olarak neyi neye bağlar?",
  "Kemiği kemiğe", ["Kası kemiğe", "Kası kasa", "Sinirleri kemiğe", "Deriyi kemiğe"],
  """Bağlar kemikleri birbirine bağlayan sıkı bağ dokusu şeritleridir ve eklemi pasif olarak destekler. Kası kemiğe
  bağlayan yapı tendondur.""",
  e=["eklem-tipleri", "art-synovialis"]),

Q("b", GY, "Kası kemiğe bağlayan yapıya ne ad verilir?",
  "Tendon (kiriş)", ["Bağ (ligament)", "Menisküs", "Bursa", "Labrum"],
  """Tendonlar kas kuvvetini kemiğe iletir. Bursalar tendonun kemik üzerinde kaymasını kolaylaştıran keselerdir; menisküs
  ve labrum eklem içi fibrokıkırdak yapılardır.""",
  e=["art-synovialis"]),

Q("b", GY, "Sinovyal eklemlerde eklem yüzlerini örten kıkırdak genellikle hangi tiptedir?",
  "Hiyalin kıkırdak", ["Elastik kıkırdak", "Fibrokıkırdak", "Kemik doku", "Yoğun bağ dokusu"],
  """Sinovyal eklemlerin çoğunda eklem yüzleri kaygan hiyalin kıkırdakla örtülüdür. Çene ve sternoklaviküler eklem gibi
  birkaç eklemde ise yüzeyleri fibrokıkırdak örter.""",
  e=["art-synovialis"]),

Q("b", GY, "Sinovyal sıvıyı üreten yapı hangisidir?",
  "Sinovyal zar (membrana synovialis)", ["Fibröz kapsül", "Eklem kıkırdağı", "Periost", "Eklem bağları"],
  """Eklem kapsülünün iç yüzünü döşeyen sinovyal zar, hiyalüronik asitten zengin kaygan sıvıyı üretir; bu sıvı kıkırdağı
  besler ve sürtünmeyi azaltır.""",
  e=["art-synovialis"]),

Q("b", GY, "Bir eklemde iki kemik arasındaki açıyı azaltan (bükme) harekete ne ad verilir?",
  "Fleksiyon", ["Ekstansiyon", "Abdüksiyon", "Addüksiyon", "Rotasyon"],
  """Fleksiyon bükme, ekstansiyon germe (açıyı artırma) hareketidir. Abdüksiyon orta hattan uzaklaştırma, addüksiyon orta
  hatta yaklaştırma, rotasyon ise kendi ekseni etrafında döndürmedir.""",
  e=["eklem-tipleri"]),

Q("b", GY, "Kolu gövdeden yana doğru uzaklaştırma hareketine ne ad verilir?",
  "Abdüksiyon", ["Addüksiyon", "Fleksiyon", "Ekstansiyon", "Sirkümdüksiyon"],
  """Abdüksiyon bir ekstremitenin vücudun orta hattından uzaklaştırılmasıdır; omuzda başlıca m. supraspinatus ve
  m. deltoideus tarafından yapılır.""",
  e=["eklem-tipleri", "art-humeri"]),

Q("b", GY, "Önkolda avuç içini yukarı (öne) çeviren harekete ne ad verilir?",
  "Supinasyon", ["Pronasyon", "İnversiyon", "Everziyon", "Opozisyon"],
  """Supinasyonda avuç içi yukarı/öne, pronasyonda aşağı/arkaya döner; bu hareketler radioulnar eklemlerde olur.
  İnversiyon ve everziyon ayağa ait hareketlerdir.""",
  e=["artt-radioulnares"]),

Q("b", GY, "Ayak tabanını içe doğru çeviren harekete ne ad verilir?",
  "İnversiyon", ["Everziyon", "Dorsifleksiyon", "Plantar fleksiyon", "Pronasyon"],
  """İnversiyonda ayak tabanı içe, everziyonda dışa döner. Bu hareketler başlıca subtalar ve transvers tarsal eklemlerde
  gerçekleşir; ayak bileği burkulmalarının çoğu inversiyonla olur.""",
  e=["art-subtalaris"]),

Q("b", GY, "Vücudun en hareketli eklemi hangisidir?",
  "Omuz (glenohumeral) eklemi", ["Kalça eklemi", "Diz eklemi", "Dirsek eklemi", "El bileği eklemi"],
  """Omuz eklemi geniş hareket açıklığı için stabiliteden fedakârlık eder: humerus başı sığ glenoid çukurla ancak kısmen
  temas eder. Bu nedenle en sık çıkan büyük eklemdir.""",
  e=["art-humeri"]),

Q("b", GY, "Vücudun en büyük eklemi hangisidir?",
  "Diz eklemi", ["Kalça eklemi", "Omuz eklemi", "Ayak bileği eklemi", "Sakroiliak eklem"],
  """Diz eklemi femur, tibia ve patellanın katıldığı, vücudun en büyük ve en karmaşık sinovyal eklemidir.""",
  e=["art-genus"]),

Q("b", AE, "Diz eklemine hangi kemikler katılır?",
  "Femur, tibia ve patella", ["Femur, tibia ve fibula", "Femur, fibula ve patella", "Tibia, fibula ve talus",
   "Femur, patella ve kalkaneus"],
  """Diz eklemi tibiofemoral ve patellofemoral eklemlerden oluşur. Fibula diz eklemine katılmaz; üst tibiofibular eklem
  ayrı bir eklemdir.""",
  e=["art-genus"]),

Q("b", UE, "Omuz eklemi hangi kemikler arasındadır?",
  "Humerus ve scapula", ["Humerus ve clavicula", "Clavicula ve scapula", "Humerus ve sternum", "Scapula ve sternum"],
  """Glenohumeral eklem humerus başı ile skapulanın cavitas glenoidalis'i arasındadır. Klavikula ile skapula
  akromiyoklaviküler eklemi yapar.""",
  e=["art-humeri"]),

Q("b", AE, "Kalça eklemi hangi eklem tipindedir?",
  "Küresel (top–çukur) eklem", ["Menteşe eklem", "Eyer eklem", "Silindir (pivot) eklem", "Düzlem eklem"],
  """Kalça eklemi femur başı ile asetabulum arasındaki küresel eklemdir (enartroz); üç eksende hareket eder ve derin
  çukuru nedeniyle omuzdan daha stabildir.""",
  e=["art-coxae"]),

Q("b", KO, "Çene eklemi hangi kemikler arasındadır?",
  "Mandibula ve os temporale", ["Mandibula ve maxilla", "Maxilla ve os temporale", "Mandibula ve os zygomaticum",
   "Mandibula ve os sphenoidale"],
  """Temporomandibular eklem mandibulanın kondili ile temporal kemiğin fossa mandibularis ve tuberculum articulare'si
  arasındadır; içinde bir fibrokıkırdak disk bulunur.""",
  e=["art-temporomandibularis"]),

Q("b", AE, "Pubik simfiz hangi kemikler arasında yer alır?",
  "Sağ ve sol pubis kemikleri", ["Sakrum ve ilium", "İskium ve pubis", "Sakrum ve koksiks", "Femur ve pubis"],
  """Pubik simfiz iki pubis kemiğini önde orta hatta birleştiren fibrokıkırdak eklemdir; arada discus interpubicus
  bulunur.""",
  e=["symphysis-pubica"]),

Q("b", AE, "Menisküsler hangi eklemde bulunur?",
  "Diz eklemi", ["Kalça eklemi", "Ayak bileği eklemi", "Omuz eklemi", "Dirsek eklemi"],
  """Diz ekleminde femur ve tibia kondilleri arasında medial ve lateral menisküs bulunur; eklem uyumunu artırır ve yükü
  dağıtırlar.""",
  e=["meniscus"]),

Q("b", GY, "Bursa nedir?",
  "Sürtünen yapılar arasında bulunan, sinovyal zarla döşeli küçük sıvı kesesi",
  ["Eklem kıkırdağının dış katmanı", "Kemiği örten zar", "Kası kemiğe bağlayan şerit", "Eklem içindeki fibrokıkırdak disk"],
  """Bursalar tendon–kemik veya deri–kemik gibi birbirine sürtünen yapılar arasında sürtünmeyi azaltır. Tekrarlayan bası
  veya sürtünmeyle iltihaplanmasına bursit denir.""",
  e=["art-synovialis"]),

# ------------------------------------------------------------------ fakülte: genel ve omurga
Q("f", GY, "Eklem kıkırdağı nasıl beslenir?",
  "Sinovyal sıvıdan difüzyonla", ["Kendi kan damarlarıyla", "Perikondriyum damarlarıyla", "Periost damarlarıyla",
   "Kemik iliğinden gelen kapillerlerle"],
  """Eklem kıkırdağında damar, sinir ve perikondriyum yoktur; besinler sinovyal sıvıdan difüzyonla gelir. Bu yüzden
  kıkırdak hasarları kendiliğinden iyileşmez.""",
  e=["art-synovialis"]),

Q("f", GY, "Romatoid artritte eklem kıkırdağını ve kemiği aşındıran iltihabi dokuya ne ad verilir?",
  "Pannus", ["Osteofit", "Tofüs", "Kallus", "Ganglion"],
  """Romatoid artrit sinovyal zarın kronik iltihabıdır; kalınlaşan sinovya pannus adını alır ve kıkırdak ile kemiği
  aşındırır. Osteofit osteoartritin, tofüs gutun bulgusudur.""",
  e=["art-synovialis"]),

Q("f", GY, "Sürekli diz çökerek çalışanlarda diz kapağının önünde şişlik yapan bursit hangi bursaya aittir?",
  "Bursa prepatellaris", ["Bursa suprapatellaris", "Bursa infrapatellaris profunda", "Bursa anserina",
   "Bursa semimembranosa"],
  """Prepatellar bursit ('hizmetçi dizi') patella ile deri arasındaki bursanın tekrarlayan basıyla iltihaplanmasıdır.
  Rahip dizi denen infrapatellar bursit ise tuberositas tibiae önündedir.""",
  e=["art-genus", "art-synovialis"]),

Q("f", KO, "Ligg. alaria'nın temel işlevi nedir?",
  "Başın aşırı rotasyonunu sınırlamak", ["Dens'i atlas'ın ön kemerine bastırmak", "Başın aşırı fleksiyonunu önlemek",
   "Atlas'ın arka kemerini oksipitale bağlamak", "Omurga kanalının ön duvarını oluşturmak"],
  """Alar bağlar dens'in yanlarından oksipital kondillere uzanır ve atlanto-aksiyal eklemde başın aşırı dönmesini
  engeller. Dens'i ön kemere bastıran lig. transversum atlantis'tir.""",
  e=["artt-craniovertebrales"]),

Q("f", KO, "Lomber bölgede omurga rotasyonunun kısıtlı olmasının nedeni nedir?",
  "Faset eklem yüzlerinin sagittal düzlemde yerleşmesi", ["Disklerin çok ince olması", "Dikenlerin kısa olması",
   "Kaburgaların varlığı", "Lig. flavum'un bulunmaması"],
  """Faset eklemlerin yönü bölgedeki hareket tipini belirler: lomber yüzler sagittaldir ve fleksiyon-ekstansiyona izin
  verip rotasyonu kısıtlar; torakal yüzler frontal düzlemdedir ve rotasyon serbesttir.""",
  e=["artt-zygapophysiales"]),

Q("f", KO, "Unkovertebral (Luschka) eklemler hangi omurlarda bulunur?",
  "C3–C7 boyun omurlarında", ["T1–T12 göğüs omurlarında", "L1–L5 bel omurlarında", "Atlas ile aksis arasında",
   "Sakral omurlar arasında"],
  """Unkovertebral eklemler C3–C7 omur gövdelerinin üst-yan kenarındaki processus uncinatus ile üstteki omur arasındaki
  yarık benzeri eklemlerdir; osteofitleri foramen intervertebrale'yi daraltabilir.""",
  e=["artt-zygapophysiales"]),

Q("f", KO, "Çene ekleminde kondilin arkaya doğru yer değiştirmesini önleyen bağ hangisidir?",
  "Lig. laterale (temporomandibulare)", ["Lig. sphenomandibulare", "Lig. stylomandibulare", "Lig. pterygospinale",
   "Lig. stylohyoideum"],
  """Lig. laterale kapsülün dış yanındaki kalınlaşmadır; arcus zygomaticus'tan mandibula boynuna uzanır ve kondilin arkaya
  ve aşağıya kaymasını önler. Sfeno- ve stilomandibular bağlar kapsülden uzaktaki yardımcı bağlardır.""",
  e=["ligg-art-temporomandibularis"]),

Q("f", KO, "Alt kaburgaların solunumda göğsün yan (transvers) çapını artıran hareketine ne ad verilir?",
  "Kova sapı (bucket handle) hareketi", ["Pompa kolu (pump handle) hareketi", "Kaliper hareketi", "Menteşe hareketi",
   "Kayma hareketi"],
  """Alt kaburgalar orta kısımları yukarı ve dışa kalkarak kova sapı gibi hareket eder ve yan çapı artırır. Üst
  kaburgaların pompa kolu hareketi ön-arka çapı artırır.""",
  e=["artt-costovertebrales"]),

Q("f", KO, "Aşağıdaki kaburgalardan hangisi transvers çıkıntıyla eklem (art. costotransversaria) yapmaz?",
  "12. kaburga", ["1. kaburga", "5. kaburga", "7. kaburga", "10. kaburga"],
  """Kostotransvers eklem kaburga tüberkülü ile transvers çıkıntı arasındadır. 11. ve 12. kaburgaların tüberkülü yoktur ve
  bu eklemi yapmazlar.""",
  e=["artt-costovertebrales"]),

Q("f", KO, "Doğum sırasında pelvis çıkışının ön-arka çapını artıran hareket hangisidir?",
  "Koksiksin geriye doğru hareketi", ["Pubik simfizin kaynaşması", "Sakrumun öne eğilmesi",
   "Asetabulumun genişlemesi", "İliumun içe dönmesi"],
  """Sakrokoksigeal eklem doğumda koksiksin geriye hareket etmesine izin verir ve pelvis çıkışının ön-arka çapı birkaç
  santimetre artar.""",
  e=["art-sacrococcygea"]),

# ------------------------------------------------------------------ fakülte: üst ekstremite
Q("f", UE, "Sternoklaviküler eklemin stabilitesini esas olarak sağlayan bağ hangisidir?",
  "Lig. costoclaviculare", ["Lig. interclaviculare", "Lig. sternoclaviculare anterius", "Lig. coracoclaviculare",
   "Lig. acromioclaviculare"],
  """Klavikulanın iç ucunu 1. kaburga kıkırdağına bağlayan kostoklaviküler bağ, eklemin en güçlü stabilizatörüdür ve
  klavikulanın yukarı kalkmasını sınırlar.""",
  e=["art-sternoclavicularis"]),

Q("f", UE, "Korakoakromiyal arkı oluşturan yapılar hangileridir?",
  "Akromiyon, lig. coraco-acromiale ve processus coracoideus", ["Akromiyon, klavikula ve spina scapulae",
   "Processus coracoideus, klavikula ve 1. kaburga", "Cavitas glenoidalis, labrum ve akromiyon",
   "Tuberculum majus, tuberculum minus ve lig. transversum humeri"],
  """Korakoakromiyal ark humerus başının üstünde koruyucu bir çatı oluşturur; altından supraspinatus tendonu ve bursa
  subacromialis geçer. Sıkışma sendromu bu arkın altında olur.""",
  e=["ligg-scapulae"]),

Q("f", UE, "Biceps uzun baş tendonunu sulcus intertubercularis içinde tutan bağ hangisidir?",
  "Lig. transversum humeri", ["Lig. coracohumerale", "Lig. glenohumerale superius", "Lig. coraco-acromiale",
   "Lig. transversum scapulae superius"],
  """Lig. transversum humeri tuberculum majus ile minus arasında uzanarak oluğu kanala çevirir. Yırtılırsa tendon oluktan
  çıkarak ağrılı bir klik yapabilir.""",
  e=["ligg-art-humeri"]),

Q("f", UE, "Tekrarlayan ön omuz çıkıklarının başlıca nedeni olan ön-alt labrum yırtığına ne ad verilir?",
  "Bankart lezyonu", ["Hill–Sachs lezyonu", "SLAP lezyonu", "Bennett lezyonu", "Stener lezyonu"],
  """Bankart lezyonu ön-alt labrum ve alt glenohumeral bağın glenoidden kopmasıdır. Hill–Sachs humerus başının
  arka-dış yüzündeki çökme kırığıdır; SLAP üst labrum yırtığıdır.""",
  e=["ligg-art-humeri", "art-humeri"]),

Q("f", UE, "SLAP lezyonu labrumun hangi bölümünü tutar?",
  "Üst labrumu (biceps uzun başının tutunduğu yer)", ["Ön-alt labrumu", "Arka-alt labrumu",
   "Labrumun tamamını", "Asetabular labrumu"],
  """SLAP (Superior Labrum Anterior to Posterior) lezyonu biceps uzun başının tutunduğu üst labrumun önden arkaya
  yırtılmasıdır; atma sporlarında sık görülür.""",
  e=["ligg-art-humeri"]),

Q("f", UE, "Dirsek ekleminin valgus stabilitesini sağlayan en önemli yapı hangisidir?",
  "Lig. collaterale ulnare'nin ön bandı", ["Lig. collaterale radiale", "Lig. anulare radii", "Lig. quadratum",
   "Chorda obliqua"],
  """Medial (ulnar) kollateral bağın ön bandı dirseği valgus kuvvetine karşı korur. Atıcı sporcularda bu bandın yırtığı
  tendon grefti ile onarılır ('Tommy John' ameliyatı).""",
  e=["ligg-cubiti"]),

Q("f", UE, "El bileği instabilitesinin en sık nedeni olan bağ yırtığı ve grafideki bulgusu hangisidir?",
  "Skafolunat bağ – skafoid ile lunatum arasında 3 mm'den geniş açıklık", ["Lunotrikuetral bağ – lunatumun dorsale dönmesi",
   "Radial kollateral bağ – processus styloideus radii kırığı", "Pisohamat bağ – hamulus kırığı",
   "Ulnar kollateral bağ – ulna başının çıkığı"],
  """Skafolunat bağ yırtığında ön-arka grafide iki kemik arasında açıklık (Terry Thomas bulgusu) ve skafoidin halka
  görünümü vardır; tedavi edilmezse DISI deformitesi ve SLAC artrozu gelişir.""",
  e=["ligg-carpi"]),

Q("f", UE, "Başparmak karpometakarpal ekleminin artrozuna ne ad verilir?",
  "Rizartroz", ["De Quervain tenosinoviti", "Dupuytren kontraktürü", "Kienböck hastalığı", "Heberden nodülü"],
  """Rizartroz trapezium ile 1. metakarp arasındaki eyer ekleminin artrozudur; özellikle menopoz sonrası kadınlarda
  kavrama ve anahtar çevirmede ağrı yapar.""",
  e=["art-carpometacarpalis-pollicis"]),

Q("f", UE, "El uzun süre atele alınacaksa MCP eklemlerinin fleksiyonda tutulmasının nedeni nedir?",
  "Kollateral bağlar fleksiyonda gergin olduğundan kısalıp sertliğe yol açmaz.", ["Fleksiyonda tendonlar daha iyi beslenir.",
   "Fleksiyonda volar plak gevşeyerek iyileşir.", "Ekstansiyonda kemikler kaynamaz.", "Fleksiyonda sinirler basıdan kurtulur."],
  """MCP kollateral bağları metakarp başının kam şekli nedeniyle fleksiyonda gerilir. Eklem ekstansiyonda uzun süre
  tutulursa gevşek bağlar kısalır ve kalıcı ekstansiyon kontraktürü gelişir.""",
  e=["artt-digitorum-manus"]),

Q("f", UE, "Kayakçı başparmağı (avcı başparmağı) hangi bağın yaralanmasıdır?",
  "Başparmak MCP ekleminin ulnar kollateral bağı", ["Başparmak IP ekleminin volar plağı",
   "Başparmak CMC ekleminin ön oblik bağı", "Başparmak MCP ekleminin radial kollateral bağı", "Skafolunat bağ"],
  """Batonla düşerken başparmağın zorla abdüksiyona itilmesi MCP ekleminin ulnar kollateral bağını yırtar; kavrama ve
  çimdikleme gücü azalır.""",
  e=["artt-digitorum-manus"]),

Q("f", UE, "Parmakların PIP ekleminde aşırı ekstansiyonu (hiperekstansiyon) önleyen yapı hangisidir?",
  "Volar plak", ["Kollateral bağlar", "Ekstansör aponevroz", "Derin transvers metakarpal bağ", "Lumbrikal kaslar"],
  """Volar plak eklemin avuç yüzündeki kalın fibrokıkırdak levhadır ve hiperekstansiyonu sınırlar. Hiperekstansiyon
  yaralanmasında avülsiyonu kuğu boynu deformitesine yol açabilir.""",
  e=["artt-digitorum-manus"]),

# ------------------------------------------------------------------ fakülte: alt ekstremite
Q("f", AE, "Kalça ekleminin aşırı abdüksiyonunu önleyen bağ hangisidir?",
  "Lig. pubofemorale", ["Lig. iliofemorale", "Lig. ischiofemorale", "Lig. capitis femoris", "Lig. transversum acetabuli"],
  """Pubofemoral bağ ramus superior ossis pubis'ten kapsülün alt-önüne uzanır ve aşırı abdüksiyonu sınırlar. İliofemoral
  bağ aşırı ekstansiyonu, iskiofemoral bağ aşırı iç rotasyonu önler.""",
  e=["ligg-art-coxae"]),

Q("f", AE, "Lig. popliteum obliquum hangi kasın tendonunun uzantısıdır?",
  "M. semimembranosus", ["M. semitendinosus", "M. biceps femoris", "M. popliteus", "M. gastrocnemius"],
  """Oblik popliteal bağ semimembranosus tendonundan yukarı-dışa uzanarak diz kapsülünün arka yüzünü güçlendirir;
  popliteal arterin hemen önünde yer alır.""",
  e=["ligg-genus-posteriora"]),

Q("f", AE, "Dizde dış (fibular) kollateral bağ ile dış menisküs arasından geçen tendon hangisidir?",
  "M. popliteus tendonu", ["M. biceps femoris tendonu", "Tractus iliotibialis", "M. plantaris tendonu",
   "M. gastrocnemius lateral başının tendonu"],
  """Dış kollateral bağ kapsülden ve dış menisküsten ayrıdır; aralarından popliteus tendonu geçer. Bu nedenle dış menisküs
  daha hareketlidir ve iç menisküse göre daha az yırtılır.""",
  e=["ligg-collateralia-genus", "meniscus", "m-popliteus"]),

Q("f", AE, "Ayak bileği dış bağlarından en güçlü olan ve en nadir yırtılan hangisidir?",
  "Lig. talofibulare posterius", ["Lig. talofibulare anterius", "Lig. calcaneofibulare", "Lig. tibiofibulare anterius",
   "Lig. bifurcatum"],
  """Dış bağlar sırayla önden arkaya yırtılır: önce talofibulare anterius, sonra calcaneofibulare. En güçlüsü
  talofibulare posterius'tur ve ancak ciddi yaralanmalarda yırtılır.""",
  e=["ligg-talocruralia-lateralia"]),

Q("f", AE, "Ayak bileği ön çekmece testi esas olarak hangi bağı değerlendirir?",
  "Lig. talofibulare anterius", ["Lig. calcaneofibulare", "Deltoid bağ", "Lig. talofibulare posterius",
   "Sindezmoz bağları"],
  """Ön çekmece testinde tibia sabitlenip topuk öne çekilir; talusun öne kayması ön talofibular bağ yırtığını gösterir.
  Kalkaneofibular bağ talar tilt (inversiyon stres) testiyle değerlendirilir.""",
  e=["ligg-talocruralia-lateralia"]),

Q("f", AE, "Yüksek ayak bileği burkulmasında yaralanan yapılar hangileridir?",
  "Distal tibiofibular sindezmoz bağları", ["Ayak bileği dış yan bağları", "Deltoid bağ", "Aşil tendonu",
   "Lisfranc bağı"],
  """Yüksek ayak bileği burkulması çoğunlukla dış rotasyonla olur ve tibia ile fibulayı bağlayan sindezmoz bağlarını
  yırtar; iyileşmesi lateral bağ burkulmasından çok daha uzundur.""",
  e=["ligg-tibiofibularia-distalia"]),

Q("f", AE, "Sinus tarsi içinde bulunan ve subtalar eklemin en güçlü bağı olan yapı hangisidir?",
  "Lig. talocalcaneum interosseum", ["Lig. talocalcaneum laterale", "Lig. calcaneofibulare", "Lig. bifurcatum",
   "Lig. plantare longum"],
  """İnterosseöz talokalkaneal bağ talus ile kalkaneus arasındaki sinus tarsi'de yer alır ve subtalar eklemin ana
  bağıdır.""",
  e=["art-subtalaris"]),

Q("f", AE, "Chopart (transvers tarsal) eklemini oluşturan eklemler hangileridir?",
  "Talonaviküler ve kalkaneokuboid eklemler", ["Talokrural ve subtalar eklemler",
   "Tarsometatarsal ve intermetatarsal eklemler", "Kuneonaviküler ve interkuneiform eklemler",
   "Kalkaneokuboid ve kuboideonaviküler eklemler"],
  """Chopart eklemi arka ayak ile orta ayak arasındaki S şeklindeki eklem çizgisidir; amputasyon seviyelerinden biridir.
  Lisfranc ise tarsometatarsal eklemlerdir.""",
  e=["art-tarsi-transversa"]),

Q("f", AE, "Lisfranc bağı nereden nereye uzanır?",
  "İç kuneiformdan 2. metatars tabanına", ["Orta kuneiformdan 1. metatars tabanına", "Kuboidden 5. metatars tabanına",
   "Navikülerden iç kuneiforma", "Kalkaneustan kuboide"],
  """Lisfranc bağı iç kuneiform ile 2. metatars tabanı arasındaki güçlü interosseöz bağdır; 1. ve 2. metatars tabanları
  arasında bağ bulunmadığından bu bağ tarsometatarsal eklemin anahtarıdır.""",
  e=["artt-tarsometatarsales"]),

Q("f", AE, "Ayağın dış boyuna kemerinin kilit taşı hangi kemiktir?",
  "Os cuboideum", ["Talus başı", "Os naviculare", "Os cuneiforme mediale", "5. metatars başı"],
  """İç boyuna kemerin kilit taşı talus başı, dış boyuna kemerinki kuboiddir. Dış kemer alçaktır ve yere yakındır.""",
  e=["arcus-pedis", "os-cuboideum"]),

Q("f", AE, "Erişkinde edinsel düztabanın en sık nedeni hangisidir?",
  "M. tibialis posterior tendon yetmezliği", ["M. tibialis anterior felci", "Aşil tendonu yırtığı",
   "M. fibularis longus yırtığı", "Plantar fasyanın kısalması"],
  """Tibialis posterior iç kemeri dinamik olarak destekleyen en önemli kastır; tendonunun dejenerasyonu ve yetmezliği
  iç kemerin çökmesine, topuğun valgusa dönmesine yol açar.""",
  e=["arcus-pedis", "m-tibialis-posterior"]),

Q("fv", AE, "Bükük ayağının üzerine düşen hastada orta ayakta şişlik ve ayak tabanında ekimoz var; grafide 1. ve 2. metatars tabanları arasında açıklık görülüyor. En olası tanı hangisidir?",
  "Lisfranc (tarsometatarsal) yaralanması", ["Jones kırığı", "Chopart çıkığı", "Ayak bileği dış bağ burkulması",
   "Kalkaneus kırığı"],
  """Ayak tabanında ekimoz ve 1.–2. metatars tabanları arasında açıklık Lisfranc bağı yaralanmasının tipik bulgularıdır;
  yaklaşık beşte biri ilk başvuruda gözden kaçtığı için dikkatli değerlendirilmelidir.""",
  e=["artt-tarsometatarsales"]),

# ------------------------------------------------------------------ TUS
Q("t", KO, "Kaynamama riski en yüksek olan dens kırığı tipi hangisidir?",
  "Tip II (dens tabanı)", ["Tip I (dens ucu)", "Tip III (aksis gövdesine uzanan)", "Hangman kırığı", "Jefferson kırığı"],
  """Anderson–D'Alonzo sınıflamasında tip II kırık dens tabanından geçer; kanlanmanın zayıf olduğu bu bölgede kaynamama
  oranı yüksektir. Tip III aksis gövdesine uzandığı için genellikle kaynar.""",
  e=["artt-craniovertebrales", "axis"]),

Q("t", KO, "Faset (zigapofizyal) eklemlerin duyu innervasyonu hangi yapıdan gelir?",
  "Spinal sinirlerin arka dalının medial dalları", ["Spinal sinirlerin ön dalları", "Sinuvertebral (rekürren meningeal) sinir",
   "Sempatik zincir", "Arka dalın lateral dalları"],
  """Her faset eklem iki komşu seviyenin arka dal medial dallarından innervasyon alır. Faset kaynaklı ağrıda bu dallara
  blok veya radyofrekans uygulanır.""",
  e=["artt-zygapophysiales"]),

Q("t", KO, "Lig. sphenomandibulare hangi faringeal ark yapısının kalıntısıdır?",
  "1. faringeal arkın kıkırdağı (Meckel kıkırdağı)", ["2. faringeal arkın kıkırdağı (Reichert)",
   "3. faringeal ark", "4. faringeal ark", "Notokord"],
  """Meckel kıkırdağından malleus, incus ve lig. sphenomandibulare gelişir. Reichert kıkırdağı (2. ark) stapes, processus
  styloideus ve lig. stylohyoideum'u oluşturur.""",
  e=["ligg-art-temporomandibularis"]),

Q("t", UE, "Önkolda lifleri membrana interossea'nın tersi yönde uzanan bağ hangisidir?",
  "Chorda obliqua", ["Lig. quadratum", "Lig. anulare radii", "Lig. collaterale radiale", "Lig. radioulnare dorsale"],
  """Membrana interossea lifleri radiustan ulnaya aşağı-içe uzanır; chorda obliqua ise tuberositas ulnae'den radiusa
  aşağı-dışa iner. Proksimal radioulnar eklemi destekler.""",
  e=["ligg-cubiti"]),

Q("t", UE, "Perilunat çıkıkların gerçekleştiği, kapitatumun palmar yüzündeki bağ bakımından zayıf alana ne ad verilir?",
  "Poirier aralığı", ["Guyon kanalı", "Anatomik enfiye çukuru", "Karpal tünel", "Parona aralığı"],
  """Poirier aralığı radioskafokapitat ile radiolunat bağlar arasındaki zayıf bölgedir; perilunat çıkıkta kapitatum
  buradan lunatumdan ayrılır.""",
  e=["ligg-carpi"]),

Q("t", UE, "TFCC'nin hangi bölümündeki yırtıklar avasküler olduğu için iyileşmez ve debridman gerektirir?",
  "Merkezi (diskin orta kısmı)", ["Periferik (ulnar kenar)", "Dorsal radioulnar bağ", "Palmar radioulnar bağ",
   "ECU tendon kılıfı"],
  """TFCC'nin yalnızca dış kenarı iyi kanlanır. Merkezi yırtıklar iyileşmediğinden artroskopik debridmanla, periferik
  yırtıklar ise onarımla tedavi edilir.""",
  e=["tfcc"]),

Q("t", UE, "Ulnanın radiustan uzun olduğu (ulna plus varyansı) kişilerde görülen ve TFCC ile lunatumun aşınmasına yol açan durum hangisidir?",
  "Ulnokarpal sıkışma (impaksiyon) sendromu", ["Kienböck hastalığı", "De Quervain tenosinoviti",
   "Karpal tünel sendromu", "Madelung deformitesi"],
  """Ulna plus varyansında ulna başı TFCC ve lunatuma baskı yapar; ulnar taraf ağrısı ve lunatumda kıkırdak hasarı
  gelişir. Kienböck ise daha çok ulna minus varyansıyla ilişkilidir.""",
  e=["tfcc"]),

Q("t", UE, "Başparmak karpometakarpal ekleminin en önemli stabilizatör bağı hangisidir?",
  "Ön oblik bağ ('gaga bağı')", ["Dorsoradial bağ", "İntermetakarpal bağ", "Radial kollateral bağ", "Volar plak"],
  """Ön oblik bağ trapezium tüberkülünden 1. metakarp tabanının iç-ön kısmına uzanır; Bennett kırığında küçük iç parçayı
  yerinde tutan da bu bağdır.""",
  e=["art-carpometacarpalis-pollicis"]),

Q("t", UE, "Stener lezyonunda kopan ulnar kollateral bağ ile tutunma yeri arasına giren yapı hangisidir?",
  "M. adductor pollicis aponevrozu", ["M. abductor pollicis brevis tendonu", "M. extensor pollicis longus tendonu",
   "Volar plak", "Sesamoid kemik"],
  """Başparmak MCP ulnar kollateral bağı koptuğunda bağ ucu adductor aponevrozunun üstüne kalabilir; araya giren
  aponevroz iyileşmeyi engellediği için cerrahi gerekir.""",
  e=["artt-digitorum-manus"]),

Q("t", UE, "Monteggia kırığında hangi yapı çıkar?",
  "Radius başı (proksimal radioulnar eklem)", ["Distal radioulnar eklem", "Ulna başı", "Lunatum", "Humerus başı"],
  """Monteggia kırığında ulna proksimal 1/3 kırığına radius başı çıkığı eşlik eder. Galeazzi kırığında ise radius gövde
  kırığına distal radioulnar eklem çıkığı eşlik eder.""",
  e=["artt-radioulnares"]),

Q("t", UE, "Sternoklaviküler eklemin arka çıkığı neden acil bir durumdur?",
  "Klavikulanın iç ucu arkadaki büyük damarlara ve trakeaya bası yapabilir.", ["Omuz ekleminin de çıkmasına yol açar.",
   "N. axillaris'i yaralar.", "Kostoklaviküler bağ asla yırtılmaz.", "Akromiyoklaviküler eklemi kilitler."],
  """Arka çıkıkta klavikulanın iç ucu brakiyosefalik damarlara, trakeaya ve özofagusa bası yapabilir; bu nedenle ön
  çıkıktan farklı olarak acil redüksiyon gerekebilir.""",
  e=["art-sternoclavicularis"]),

Q("t", AE, "Kalça ekleminin kapsülü femur boynunun arka yüzünde ne kadarını içine alır?",
  "İç 2/3'ünü", ["Tamamını", "İç 1/3'ünü", "Yalnızca femur başını", "Trochanter major'a kadar tamamını"],
  """Kapsül önde linea intertrochanterica'ya kadar uzanır ve boynun tamamını, arkada ise boynun yalnızca iç 2/3'ünü
  kapsar. Boyun kırıkları bu nedenle büyük ölçüde kapsül içidir.""",
  e=["art-coxae", "ligg-art-coxae"]),

Q("t", AE, "Kalça ekleminde aşırı iç rotasyonu sınırlayan bağ hangisidir?",
  "Lig. ischiofemorale", ["Lig. pubofemorale", "Lig. capitis femoris", "Lig. transversum acetabuli", "Zona orbicularis"],
  """İskiofemoral bağ iskiumdan kapsülün arka yüzüne spiral şekilde uzanır; iç rotasyon ve ekstansiyonda gerilir.""",
  e=["ligg-art-coxae"]),

Q("t", AE, "Dizin arka-dış köşesinin en önemli statik stabilizatörü hangisidir?",
  "Lig. popliteofibulare", ["Lig. popliteum obliquum", "Lig. collaterale tibiale", "Lig. meniscofemorale",
   "Tractus iliotibialis"],
  """Arka-dış köşe dış kollateral bağ, popliteus tendonu, popliteofibular bağ ve kapsülden oluşur; popliteofibular bağ
  dış rotasyon stabilitesinin başlıca statik yapısıdır.""",
  e=["ligg-genus-posteriora"]),

Q("t", AE, "Dial testinde hem 30° hem 90° diz fleksiyonunda artmış dış rotasyon neyi düşündürür?",
  "Arka-dış köşe ile arka çapraz bağın birlikte yaralanmasını", ["Yalnız ön çapraz bağ yırtığını",
   "Yalnız iç kollateral bağ yırtığını", "Medial menisküs yırtığını", "Patella çıkığını"],
  """Dış rotasyon artışı yalnız 30°'de ise izole arka-dış köşe yaralanması, hem 30° hem 90°'de ise arka-dış köşe ile
  AÇB'nin birlikte yaralanması düşünülür.""",
  e=["ligg-genus-posteriora", "ligg-cruciata"]),

Q("t", AE, "Hem talokrural hem subtalar ekleme katkı veren ayak bileği dış bağı hangisidir?",
  "Lig. calcaneofibulare", ["Lig. talofibulare anterius", "Lig. talofibulare posterius", "Lig. tibiofibulare anterius",
   "Lig. talocalcaneum interosseum"],
  """Kalkaneofibular bağ malleolus lateralis'ten kalkaneusa uzandığı için iki eklemi birden çaprazlar; talar tilt testiyle
  değerlendirilir.""",
  e=["ligg-talocruralia-lateralia", "art-subtalaris"]),

Q("t", AE, "Ayak bileğinde talusun mortis içinde dışa kaymasını önleyen en önemli yapı hangisidir?",
  "Deltoid bağın derin (tibiotalar) kısmı", ["Lig. talofibulare anterius", "Lig. calcaneofibulare",
   "Deltoid bağın tibionaviküler kısmı", "Lig. plantare longum"],
  """Deltoid bağın derin tibiotalar lifleri talusu iç malleole bağlar; bu lifler yırtıldığında talus dışa kayar ve eklem
  temas yüzeyi azalarak artroz gelişir.""",
  e=["lig-deltoideum"]),

Q("t", AE, "Lig. bifurcatum'un iki kolu kalkaneustan hangi kemiklere uzanır?",
  "Os naviculare ve os cuboideum", ["Talus ve os naviculare", "Os cuboideum ve 5. metatars",
   "Os naviculare ve iç kuneiform", "Talus ve os cuboideum"],
  """Y şeklindeki bifurkat bağın kalkaneonaviküler ve kalkaneokuboid kolları Chopart ekleminin dorsalinde yer alır;
  burkulması sinus tarsi'nin önünde ağrı yapar.""",
  e=["art-tarsi-transversa"]),

Q("t", AE, "Talokalkaneal koalisyonun yan ayak bileği grafisindeki tipik bulgusu hangisidir?",
  "C işareti", ["Karıncayiyen burnu işareti", "Halka işareti", "Terry Thomas işareti", "Çift kontur işareti"],
  """Talokalkaneal koalisyonda talus kubbesi ile sustentaculum tali arasında devamlı bir C şeklinde kontur oluşur.
  Kalkaneonaviküler koalisyonda ise oblik grafide 'karıncayiyen burnu' görülür.""",
  e=["art-subtalaris"]),

Q("tv", AE, "Kayak yaparken dizi dışa dönen sporcu ani ağrı ve instabilite tarif ediyor; ön çapraz bağ rekonstrüksiyonundan sonra dizde dış rotasyon instabilitesi sürüyor. Gözden kaçmış olabilecek yaralanma hangisidir?",
  "Dizin arka-dış köşe yaralanması", ["Medial menisküs yırtığı", "Patellar tendon yırtığı", "Prepatellar bursit",
   "Pes anserinus bursiti"],
  """Arka-dış köşe yaralanmaları sıklıkla çapraz bağ yaralanmalarına eşlik eder; tanınıp onarılmazsa çapraz bağ greftine
  aşırı yük biner ve rekonstrüksiyon başarısız olur.""",
  e=["ligg-genus-posteriora"]),
]
