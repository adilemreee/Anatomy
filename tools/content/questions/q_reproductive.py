from qcommon import Q, write

ER = "Erkek üreme organları"
KD = "Kadın üreme organları"
PE = "Perine"

questions = [
# ------------------------------------------------------------------ Erkek
Q("f", ER, "Testisin karın arka duvarından skrotuma inişinde ona yol gösteren yapı hangisidir?",
  "Gubernaculum testis",
  ["Processus vaginalis'in kapalı ucu", "Lig. teres hepatis", "Urachus", "Mesonephros"],
  """Gubernaculum testisin alt kutbundan labioskrotal kabarıklığa uzanan mezenkimal banttır ve testisin inguinal
  kanaldan geçerek skrotuma inmesine yol gösterir. Kadındaki karşılığı lig. ovarii proprium ve lig. teres uteri'dir.""",
  e=["testis", "canalis-inguinalis"]),

Q("fv", ER, """1 yaşındaki erkek çocukta sağ testis skrotumda ele gelmiyor; kasık bölgesinde palpe ediliyor.
İnmemiş testis için aşağıdakilerden hangisi doğrudur?""",
  "En sık inguinal kanal içinde bulunur ve tedavi edilmezse infertilite ile malignite riski artar.",
  ["En sık böbrek düzeyinde bulunur.", "Kendiliğinden inme olasılığı 5 yaşına kadar devam eder.",
   "Malignite riski cerrahiyle tamamen ortadan kalkar.", "Yalnızca sol tarafta görülür."],
  """Kriptorşidizm prematürelerde sıktır. İnmemiş testisler çoğunlukla inguinal kanaldadır; orşiopeksi genellikle
  6–18 ay arasında önerilir. Yüksek ısı spermatogenezi bozar; germ hücreli tümör riski cerrahi sonrası da normalden
  yüksek kalır.""",
  e=["testis", "canalis-inguinalis"]),

Q("tv", ER, """14 yaşında erkek çocuk uykudan ani başlayan şiddetli skrotal ağrıyla uyanıyor; testis yukarıda ve yatay
duruyor, kremaster refleksi alınamıyor. En olası tanı ve zemin hazırlayan anatomik durum hangisidir?""",
  "Testis torsiyonu – 'çan tokmağı' deformitesi (tunica vaginalis'in testisi çepeçevre sarması)",
  ["Epididimit – ductus deferens'in tıkanması", "Varikosel – sol testiküler venin dik açıyla açılması",
   "Hidrosel – processus vaginalis'in açık kalması", "İnguinal herni – derin halkanın geniş olması"],
  """Normalde testisin arka yüzü skrotuma yapışıktır. Tunica vaginalis testisi tamamen sardığında testis kord etrafında
  serbestçe dönebilir. Torsiyon ürolojik acildir; kremaster refleksinin kaybı tipiktir ve 6 saat içinde detorsiyon
  gerekir.""",
  e=["testis", "funiculus-spermaticus", "scrotum"]),

Q("t", ER, "Testis tümörünün ilk lenfatik metastazı hangi düzeyde beklenir?",
  "Renal damarlar düzeyindeki paraaortik (lomber) lenf düğümleri",
  ["Yüzeyel inguinal lenf düğümleri", "Dış iliak lenf düğümleri", "Derin inguinal lenf düğümleri", "Mezenterik lenf düğümleri"],
  """Testisin lenfatikleri spermatik kord içinde testiküler damarlara eşlik ederek doğrudan lomber düğümlere gider;
  bu, testisin arka karın duvarından inişinin bir sonucudur. Skrotum derisi ise yüzeyel inguinal düğümlere drene olur.""",
  e=["testis", "nodi-lumbales", "scrotum"]),

Q("fv", ER, """Skrotumunda ağrısız şişlik olan hastada şişliğin üstünden kord ayrı olarak ele geliyor ve ışık
tutulduğunda şişlik ışığı geçiriyor. Sıvı nerede birikmiştir?""",
  "Tunica vaginalis'in parietal ve visseral yaprakları arasında (hidrosel)",
  ["Pampiniform pleksus içinde", "Epididim kanalında", "Tunica albuginea'nın içinde", "İnguinal kanalın içinde"],
  """Hidrosel tunica vaginalis'in iki yaprağı arasında sıvı birikmesidir ve transillüminasyon pozitiftir. Çocuklarda
  processus vaginalis'in açık kalmasıyla (iletişimli hidrosel) ilişkilidir; varikosel ve herni ışık geçirmez.""",
  e=["scrotum", "testis"]),

Q("f", ER, "Spermlerin olgunlaştığı, hareket yeteneği kazandığı ve depolandığı yapı hangisidir?",
  "Epididim",
  ["Seminifer tübüller", "Seminal bez", "Prostat", "Ejakülatör kanal"],
  """Spermler testisteki seminifer tübüllerde üretilir, rete testis ve duktuli efferentesler ile epididime geçer.
  Epididimde 2–3 haftada olgunlaşır ve kuyruk bölümünde depolanır.""",
  e=["epididymis", "testis"]),

Q("f", ER, "Vazektomi en kolay ve güvenli olarak nerede yapılır?",
  "Skrotum kökünde, spermatik kordda ele gelen ductus deferens üzerinde",
  ["Derin inguinal halkada", "Pelvis içinde, üreteri çaprazladığı yerde", "Prostatın içinde", "Epididim başında"],
  """Ductus deferens skrotumun üst kısmında kordun arka kısmında sert bir kordon gibi kolayca ele gelir. Vazektomide
  burada bağlanıp kesilir; testis hormon üretimi ve semenin büyük kısmı etkilenmez.""",
  e=["ductus-deferens", "funiculus-spermaticus"]),

Q("f", ER, "Semen hacminin en büyük kısmını sağlayan ve fruktozdan zengin salgı yapan yapı hangisidir?",
  "Glandula vesiculosa (seminal bez)",
  ["Prostat", "Bulbouretral (Cowper) bezler", "Epididim", "Testis"],
  """Seminal bezler semenin yaklaşık %60–70'ini oluşturur; fruktoz spermlerin enerji kaynağıdır. Prostat %20–30
  katkı yapar (PSA, sitrat, çinko). Cowper bezleri ejakülasyon öncesi kayganlaştırıcı salgı yapar.""",
  e=["glandula-vesiculosa", "prostata"]),

Q("f", ER, "Ejakülatör kanallar nereye açılır?",
  "Prostatik üretrada colliculus seminalis üzerine",
  ["Mesanenin trigonum bölgesine", "Membranöz üretraya", "Spongiyöz üretranın bulbusuna", "Seminal bezin içine"],
  """Ductus deferens ampullası ve seminal bez kanalı birleşerek ejakülatör kanalı yapar; bu kanal prostattan geçerek
  colliculus seminalis'te, utriculus prostaticus'un iki yanında üretraya açılır.""",
  e=["ductus-ejaculatorius", "urethra-masculina"]),

Q("t", ER, "Prostat kanseri ve benign prostat hiperplazisinin (BPH) en sık geliştiği zonlar hangisinde doğru eşleştirilmiştir?",
  "Kanser – periferik zon; BPH – transizyonel zon",
  ["Kanser – transizyonel zon; BPH – periferik zon", "Kanser – santral zon; BPH – periferik zon",
   "Kanser – anterior fibromüsküler stroma; BPH – santral zon", "Her ikisi de santral zonda gelişir."],
  """Periferik zon prostat dokusunun en büyük kısmıdır ve rektuma bakar; kanser buradan geliştiği için rektal tuşede
  ele gelebilir. BPH üretrayı saran transizyonel zondan gelişir ve erken idrar yapma güçlüğü yapar.""",
  e=["prostata"]),

Q("t", ER, "Prostat kanserinin omurgaya hematojen yolla erken yayılmasında rol oynayan yapı hangisidir?",
  "Prostat venöz pleksusunun kapaksız iç vertebral venöz pleksusla (Batson) bağlantısı",
  ["Prostatın lenfatiklerinin ductus thoracicus'a açılması", "Prostat arterinin vertebral arterle anastomozu",
   "Prostatın doğrudan omurgaya komşu olması", "Seminal bezlerin vertebral kanala açılması"],
  """Pelvik venler ile vertebral venöz pleksus arasında kapaksız bağlantılar vardır; karın içi basınç arttığında kan
  vertebral pleksusa yönelir. Bu yol prostat kanserinin lomber omurga ve pelvis kemiklerine osteoblastik
  metastazını açıklar.""",
  e=["prostata", "vertebrae-lumbales"]),

Q("f", ER, "Ereksiyon ve ejakülasyonu sağlayan otonom lifler hangisinde doğru eşleştirilmiştir?",
  "Ereksiyon – parasempatik (S2–S4); ejakülasyon – sempatik (L1–L2)",
  ["Ereksiyon – sempatik; ejakülasyon – parasempatik", "Her ikisi de yalnızca n. pudendus ile",
   "Ereksiyon – sempatik (T10–T12); ejakülasyon – somatik", "Her ikisi de n. vagus ile"],
  """Pelvik splanknik sinirler (nn. erigentes) korpus kavernozum arterlerini genişleterek ereksiyon sağlar ('point').
  Sempatik lifler emisyonu (vas deferens, seminal bez ve prostat kasılması) ve mesane boynunun kapanmasını sağlar
  ('shoot'); bulbospongiosus'un ritmik kasılması n. pudendus ile olur.""",
  e=["penis", "systema-autonomicum", "n-pudendus"]),

Q("t", ER, "Penisin yapısı ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Üretra corpus spongiosum'un içinden geçer; corpus spongiosum distalde glans penisi oluşturur.",
  ["Üretra corpora cavernosa'nın içinden geçer.", "Corpus spongiosum ereksiyonda en sert yapıdır.",
   "Penisin dorsal arteri a. iliaca externa'dan çıkar.", "Corpora cavernosa'nın kökleri (crura) pubise tutunmaz."],
  """Penis iki corpus cavernosum ve bir corpus spongiosum'dan oluşur. Crura ramus ischiopubicus'a tutunur ve
  ischiocavernosus ile sarılıdır; bulbus spongiosum bulbospongiosus ile sarılıdır. Ereksiyonda corpus spongiosum
  daha az sertleşir, böylece üretra açık kalır. Damarları a. pudenda interna'dandır.""",
  e=["penis", "urethra-masculina"]),

Q("t", ER, "Spermatik kordun kılıfları ve karın duvarındaki kökenleri hangisinde doğru eşleştirilmiştir?",
  "Fascia spermatica interna – fascia transversalis",
  ["Fascia spermatica externa – m. transversus abdominis", "M. cremaster – m. obliquus externus",
   "Fascia spermatica interna – m. obliquus internus", "Tunica dartos – fascia transversalis"],
  """Testis inerken karın duvarı katmanlarını önüne katar: fascia spermatica externa dış oblik aponevrozundan,
  kremaster ve fasyası iç oblikten, fascia spermatica interna fascia transversalis'ten gelir. Transversus
  abdominis kemerini geçtiği için kılıfa katılmaz.""",
  e=["funiculus-spermaticus", "canalis-inguinalis"]),

Q("t", ER, "Utriculus prostaticus embriyolojik olarak hangi yapının kalıntısıdır?",
  "Paramezonefrik (Müller) kanalların birleşik alt uçları",
  ["Mezonefrik (Wolff) kanal", "Urachus", "Gubernaculum", "Ürorektal septum"],
  """Erkekte anti-Müller hormonu paramezonefrik kanalların gerilemesine yol açar; geride utriculus prostaticus ve
  appendix testis kalır. Utriculus uterus ve vajinanın üst kısmının erkekteki homoloğudur.""",
  e=["prostata", "ductus-ejaculatorius"]),

# ------------------------------------------------------------------ Kadın
Q("f", KD, "A. ovarica'nın kökeni ve overe ulaştığı bağ hangisidir?",
  "Abdominal aorta – lig. suspensorium ovarii (infundibulopelvik bağ)",
  ["A. iliaca interna – lig. ovarii proprium", "A. uterina – lig. latum", "A. iliaca externa – lig. teres uteri", "A. renalis – mesosalpinx"],
  """Over arteri gonadların iniş öyküsü nedeniyle L2 düzeyinde aortadan çıkar ve infundibulopelvik bağ içinde
  pelvise iner. Over ayrıca a. uterina'nın ovaryan dalıyla anastomoz yapan çift kanlanmaya sahiptir.""",
  e=["ovarium", "ligamenta-uteri", "aorta"]),

Q("t", KD, "Over patolojilerinde ağrının uyluğun iç yüzüne yansıması hangi sinirle ilişkilidir?",
  "N. obturatorius",
  ["N. femoralis", "N. genitofemoralis", "N. pudendus", "N. ilioinguinalis"],
  """Over pelvis yan duvarındaki fossa ovarica'da durur; bu çukurun tabanında n. obturatorius seyreder. Over
  iltihabı veya kitlesi siniri tahriş ederek uyluğun iç yüzünde ağrıya yol açabilir.""",
  e=["ovarium", "n-obturatorius"]),

Q("fv", KD, """Adet gecikmesi olan ve tek taraflı alt karın ağrısıyla başvuran kadında β-hCG pozitif, uterus boş.
Ektopik gebeliğin en sık yerleştiği yer neresidir?""",
  "Tuba uterina'nın ampullası",
  ["Tubanın isthmusu", "Over", "Serviks", "Karın boşluğu"],
  """Fertilizasyon genellikle ampullada olur ve ektopik gebeliklerin büyük kısmı da buraya yerleşir. Geçirilmiş pelvik
  enflamatuvar hastalık, tüp cerrahisi ve rahim içi araç risk faktörleridir. Rüptürde kan Douglas boşluğunda
  toplanır.""",
  e=["tuba-uterina", "excavatio-rectouterina"]),

Q("f", KD, "Uterusun normal pozisyonu hangisidir?",
  "Antevert ve antefleks",
  ["Retrovert ve retrofleks", "Antevert ve retrofleks", "Dikey ve fleksiyonsuz", "Retrovert ve antefleks"],
  """Anteversiyon serviksin vajinaya göre öne açılanmasını, antefleksiyon uterus gövdesinin servikse göre öne
  bükülmesini ifade eder. Bu pozisyonda uterus dolu olmayan mesanenin üzerine yaslanır.""",
  e=["uterus", "ligamenta-uteri"]),

Q("t", KD, "Uterusun en önemli pasif desteğini sağlayan ve a. uterina'yı taşıyan bağ hangisidir?",
  "Lig. cardinale (lig. transversum cervicis)",
  ["Lig. teres uteri", "Lig. latum uteri", "Lig. ovarii proprium", "Lig. suspensorium ovarii"],
  """Kardinal bağlar serviks ve vajen üst kısmından pelvis yan duvarına uzanır; uterosakral bağlar ve levator ani ile
  birlikte uterusun asıl desteğini oluşturur. Bu yapıların gevşemesi uterus prolapsusuna yol açar. Lig. latum ve
  lig. teres zayıf desteklerdir.""",
  e=["ligamenta-uteri", "cervix-uteri", "diaphragma-pelvis"]),

Q("f", KD, "Lig. teres uteri (round ligament) nereye uzanır?",
  "Uterus köşesinden inguinal kanal yoluyla labium majus'a",
  ["Uterustan sakruma", "Overden pelvis yan duvarına", "Serviksten pubise", "Uterustan mesane tabanına"],
  """Lig. teres uteri gubernakulumun kalıntısıdır; inguinal kanaldan geçerek labium majus'un bağ dokusunda sonlanır.
  Bu nedenle uterus kökenli bazı lenfatik akım yüzeyel inguinal düğümlere ulaşabilir.""",
  e=["ligamenta-uteri", "canalis-inguinalis", "vulva"]),

Q("tv", KD, """Histerektomi sonrası 3. günde hastada yan ağrısı, ateş ve vajinadan sulu akıntı gelişiyor. Ameliyat
sırasında a. uterina bağlanırken en olası yaralanan yapı hangisidir?""",
  "Üreter",
  ["N. obturatorius", "A. iliaca externa", "Ductus thoracicus", "N. femoralis"],
  """A. uterina servikse yaklaşık 2 cm uzaklıkta üreterin önünden ve üstünden geçer ('köprünün altından akan su').
  Arter bağlanırken üreter bağlanabilir veya kesilebilir; idrar kaçağı vajinal akıntı ve ürinoma yapabilir.""",
  e=["ureter", "cervix-uteri", "uterus"]),

Q("fv", KD, """Pelvik ağrı ve hipotansiyonu olan kadında karın içi kanama düşünülüyor. Vajinanın arka forniksinden
iğneyle girilerek hangi boşluktan örnek alınır?""",
  "Excavatio rectouterina (Douglas boşluğu)",
  ["Excavatio vesicouterina", "Fossa ischioanalis", "Spatium retropubicum (Retzius)", "Bursa omentalis"],
  """Douglas boşluğu ayakta duran kadında periton boşluğunun en alçak yeridir ve tabanı arka forniksle yalnızca vajen
  duvarı ve periton kadar ayrılır. Kuldosentezde kan, irin veya asit örneği alınabilir.""",
  e=["excavatio-rectouterina", "vagina"]),

Q("f", KD, "Serviks kanserinin büyük kısmının geliştiği bölge hangisidir?",
  "Endoserviks ile ektoserviks epitelinin buluştuğu transformasyon zonu",
  ["Uterus fundusu", "Ostium uteri internum'un üstündeki endometrium", "Vajinanın arka forniksi", "Tuba uterina'nın isthmusu"],
  """Kolumnar endoservikal epitelin skuamöz metaplaziye uğradığı transformasyon zonu HPV enfeksiyonuna en duyarlı
  bölgedir. Pap smear bu bölgeden örnek alınarak yapılır.""",
  e=["cervix-uteri"]),

Q("t", KD, "Vajinanın embriyolojik gelişimi ile ilgili hangisi doğrudur?",
  "Üst 1/3'ü paramezonefrik kanallardan, alt 2/3'ü ürogenital sinüsten gelişir.",
  ["Tamamı mezonefrik kanaldan gelişir.", "Tamamı ürogenital sinüsten gelişir.",
   "Üst 2/3'ü ektodermden, alt 1/3'ü mezodermden gelişir.", "Gubernakulumdan gelişir."],
  """Paramezonefrik kanalların birleşen alt uçları uterus ve vajinanın üst kısmını oluşturur; sinovajinal bulbuslar
  vajinanın alt kısmını yapar. Bu nedenle üst ve alt vajinanın lenf drenajı farklıdır (iliak ve inguinal düğümler).""",
  e=["vagina", "uterus"]),

Q("fv", KD, """Memesinde ele gelen kitle olan kadında kitlenin üzerindeki derinin portakal kabuğu görünümünde
olduğu ve meme başının içe çekildiği görülüyor. Deri çekintisinin anatomik nedeni nedir?""",
  "Tümörün asıcı bağları (Cooper ligamentleri) tutup kısaltması",
  ["M. pectoralis major'un kasılması", "Meme başının düz kaslarının hipertrofisi", "Retromammarya aralığın genişlemesi", "Aksiller lenf düğümlerinin şişmesi"],
  """Cooper ligamentleri meme dokusunu deriye ve pektoral fasyaya bağlar; tümör tarafından tutulduğunda deri çekilir.
  Portakal kabuğu görünümü (peau d'orange) dermal lenfatiklerin tümörle tıkanması sonucu ödeme bağlıdır.""",
  e=["glandula-mammaria"]),

Q("f", KD, "Meme kanserlerinin en sık yerleştiği kadran ve bunun nedeni hangisidir?",
  "Üst dış kadran; meme dokusunun en yoğun olduğu ve aksiller kuyruğa uzandığı bölge olduğu için",
  ["Alt iç kadran; lenfatiklerin en az olduğu bölge olduğu için", "Meme başı arkası; kanalların bulunmadığı bölge olduğu için",
   "Alt dış kadran; yağ dokusunun en az olduğu bölge olduğu için", "Üst iç kadran; parasternal düğümlere yakın olduğu için"],
  """Meme dokusunun en büyük kısmı üst dış kadrandadır ve aksillaya uzanan Spence kuyruğunu içerir. Lenf drenajının
  büyük kısmı aksiller düğümlere gider; iç kadranlardan bir kısmı parasternal düğümlere ulaşır.""",
  e=["glandula-mammaria", "nodi-axillares"]),

Q("f", KD, "Büyük vestibüler bezler (Bartholin bezleri) nerede bulunur?",
  "Vajen girişinin iki yanında, saat 4 ve 8 hizasında açılırlar.",
  ["Üretranın iki yanında, saat 11 ve 1 hizasında", "Klitorisin altında orta hatta", "Labium majus'un dış yüzünde",
   "Vajinanın arka forniksinde"],
  """Bartholin bezleri bulbus vestibuli'nin arka ucunda, yüzeyel perine boşluğundadır ve kanalları labium minus ile
  himen arasına açılır. Kanalın tıkanması kist ve apseye yol açar. Erkekteki karşılığı bulbouretral (Cowper) bezlerdir.""",
  e=["vulva", "perineum"]),

Q("t", KD, "Lig. latum uteri'nin tubayı saran bölümü hangisidir?",
  "Mesosalpinx",
  ["Mesovarium", "Mesometrium", "Lig. ovarii proprium", "Lig. suspensorium ovarii"],
  """Geniş bağ üç bölümden oluşur: tubayı saran mesosalpinx, overi asan mesovarium ve uterusun yanlarındaki
  mesometrium. Mesosalpinx içinde tubanın damarları ve embriyolojik kalıntılar (epoophoron) bulunur.""",
  e=["ligamenta-uteri", "tuba-uterina"]),

# ------------------------------------------------------------------ Perine
Q("fv", PE, """Zor vajinal doğum sırasında perine yırtığını önlemek için epizyotomi yapılıyor. Yırtıldığında pelvis
tabanı desteğini en çok bozan ve birçok perine kasının tutunduğu yapı hangisidir?""",
  "Corpus perineale (perine cismi)",
  ["Lig. sacrospinale", "Membrana obturatoria", "Arcus tendineus fasciae pelvis", "Lig. anococcygeum"],
  """Corpus perineale vajen ile anüs arasındaki fibromüsküler düğümdür; bulbospongiosus, yüzeyel ve derin transvers
  perine kasları, dış anal sfinkter ve levator ani lifleri buraya tutunur. Hasarı prolapsus ve inkontinansa zemin
  hazırlar; mediolateral epizyotomi anal sfinkteri korumayı amaçlar.""",
  e=["perineum", "diaphragma-pelvis"]),

Q("t", PE, "Aşağıdakilerden hangisi n. pudendus'un dalı değildir?",
  "N. genitofemoralis",
  ["N. rectalis inferior", "Nn. perineales", "N. dorsalis penis/clitoridis", "Nn. scrotales/labiales posteriores"],
  """N. pudendus (S2–S4) Alcock kanalında n. rectalis inferior'u verir, sonra perineal sinir (perine kasları ve arka
  skrotal/labial dallar) ve n. dorsalis penis/clitoridis'e ayrılır. N. genitofemoralis lomber pleksusun (L1–L2) dalıdır.""",
  e=["n-pudendus", "perineum"]),

Q("t", PE, "Canalis pudendalis (Alcock kanalı) nerede bulunur ve içinde neler seyreder?",
  "Fossa ischioanalis'in yan duvarında, m. obturatorius internus fasyası içinde; n. pudendus ve a./v. pudenda interna",
  ["İnguinal kanalın arka duvarında; spermatik kord", "Perine zarının üstünde; dış üretral sfinkter",
   "Sakrumun ön yüzünde; sakral pleksus", "Diyaframın krusları arasında; ductus thoracicus"],
  """Pudendal sinir ve damarlar küçük siyatik delikten fossa ischioanalis'e girer ve obturator internus fasyasının
  oluşturduğu kanalda öne ilerler. Bu bölgede sinir sıkışması perinede ağrı ve uyuşukluğa yol açabilir.""",
  e=["perineum", "n-pudendus"]),

Q("t", PE, "Yüzeyel perine boşluğunda (spatium superficiale perinei) aşağıdakilerden hangisi bulunmaz?",
  "M. sphincter urethrae externus",
  ["M. ischiocavernosus", "M. bulbospongiosus", "Penisin kökleri (crura)", "Büyük vestibüler bezler (kadında)"],
  """Yüzeyel perine boşluğu perine zarı ile Colles fasyası arasındadır ve erektil dokuların kökleri, onları saran kaslar
  ve kadında Bartholin bezlerini içerir. Dış üretral sfinkter, derin transvers perine kası, membranöz üretra ve
  erkekte bulbouretral bezler derin perine boşluğundadır.""",
  e=["perineum", "penis", "vulva"]),

Q("f", PE, "Perine bölgesini ürogenital ve anal üçgenlere ayıran çizgi hangisidir?",
  "İki tuber ischiadicum'u birleştiren çizgi",
  ["İki SIAS'ı birleştiren çizgi", "Symphysis pubica ile koksiksi birleştiren çizgi", "İki spina ischiadica'yı birleştiren çizgi", "İnguinal bağlar"],
  """Elmas biçimli perine, tuber ischiadica'ları birleştiren hatla önde ürogenital, arkada anal üçgene ayrılır.
  Corpus perineale bu çizginin orta noktasındadır.""",
  e=["perineum"]),
]

write("reproductive", questions)
