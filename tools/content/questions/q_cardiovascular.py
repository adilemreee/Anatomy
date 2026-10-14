from qcommon import Q, write

KA = "Kalp"
AO = "Aorta ve dalları"
BB = "Baş ve boyun arterleri"
UE = "Üst ekstremite arterleri"
KP = "Karın ve pelvis arterleri"
AE = "Alt ekstremite arterleri"
VE = "Venler"

questions = [
# ------------------------------------------------------------------ Kalp
Q("f", KA, "Kalbin sternokostal (ön) yüzünün büyük kısmını oluşturan boşluk hangisidir?",
  "Sağ ventrikül",
  ["Sol ventrikül", "Sağ atriyum", "Sol atriyum", "Sol aurikula"],
  """Kalp sola dönmüş olduğundan ön yüzünü çoğunlukla sağ ventrikül yapar; sağ kenarı sağ atriyum, sol
  kenarı sol ventrikül (ve sol aurikula), apeksi sol ventrikül, tabanı (arka yüz) sol atriyum oluşturur.
  Sternuma yakın olan sağ ventrikül delici göğüs yaralanmalarında en sık yaralanan boşluktur.""",
  e=["ventriculus-dexter", "cor"]),

Q("tv", KA, """Mitral darlığı olan hastada yutma güçlüğü ve ses kısıklığı gelişiyor. Bu belirtiler en çok hangi
boşluğun genişlemesiyle açıklanır?""",
  "Sol atriyum",
  ["Sağ atriyum", "Sol ventrikül", "Sağ ventrikül", "Sinus coronarius"],
  """Sol atriyum kalbin tabanını yapar ve doğrudan özofagusun önündedir. Genişlediğinde özofagusa bası
  yapar (disfaji) ve sol n. laryngeus recurrens'i gerebilir (Ortner sendromu). Aynı komşuluk nedeniyle
  transözofageal ekokardiyografi sol atriyumu en iyi gösterir.""",
  e=["atrium-sinistrum", "oesophagus", "valvae-cordis"]),

Q("f", KA, "Sağ atriyumdaki fossa ovalis hangi fetal yapının kalıntısıdır?",
  "Foramen ovale",
  ["Ductus arteriosus", "Ductus venosus", "V. umbilicalis", "Sinus venosus"],
  """Fetal dönemde kan foramen ovale aracılığıyla sağ atriyumdan sol atriyuma geçer. Doğumda sol atriyum
  basıncı artınca septum primum septum secundum'a yapışarak deliği kapatır ve fossa ovalis kalır.
  Kişilerin yaklaşık dörtte birinde prob geçebilen açıklık (PFO) kalır.""",
  e=["atrium-dextrum"]),

Q("t", KA, "Atriyoventriküler (AV) düğümün yerini gösteren Koch üçgenini hangi yapılar sınırlar?",
  "Todaro tendonu, triküspit kapağın septal yaprağı ve sinus coronarius'un ağzı",
  ["Crista terminalis, v. cava superior ağzı ve aurikula", "Trabecula septomarginalis, ön papiller kas ve pulmoner kapak",
   "Fossa ovalis, limbus ve v. cava inferior ağzı", "Mitral kapağın ön yaprağı, aort kapağı ve septum membranaceum"],
  """Koch üçgeni sağ atriyumun septal duvarındadır. AV düğüm bu üçgenin tepesinde yer alır; kardiyak
  cerrahi ve ablasyonda iletim sistemini korumak için önemli bir işarettir.""",
  e=["atrium-dextrum"]),

Q("t", KA, "Sağ ventrikülde interventriküler septumdan ön papiller kasın tabanına uzanan ve sağ dal demetini taşıyan yapı hangisidir?",
  "Trabecula septomarginalis (moderatör bant)",
  ["Crista supraventricularis", "Chordae tendineae", "Musculi pectinati", "Crista terminalis"],
  """Moderatör bant sağ dal demetinin bir kısmını ön papiller kasa kısa yoldan ulaştırır; böylece papiller
  kas, triküspit kapak kapanmadan zamanında kasılır. Ayrıca ventrikülün aşırı genişlemesini sınırlar.""",
  e=["ventriculus-dexter"]),

Q("f", KA, "Kalp kapaklarının en iyi dinlendiği odaklarla ilgili hangisi doğrudur?",
  "Mitral kapak – sol 5. interkostal aralık, midklavikular hat (apeks)",
  ["Aort kapağı – sol 2. interkostal aralık, sternum kenarı", "Pulmoner kapak – sağ 2. interkostal aralık, sternum kenarı",
   "Triküspit kapak – sol 5. interkostal aralık, midklavikular hat", "Mitral kapak – sağ 4. interkostal aralık, sternum kenarı"],
  """Odaklar kapakların anatomik yerinden çok kanın aktığı yöne göredir: aort sağ 2. aralık, pulmoner sol
  2. aralık (sternum kenarı), triküspit sternumun sol alt kenarı (4–5. aralık), mitral ise apeks (sol 5.
  aralık, midklavikular hat).""",
  e=["valvae-cordis"]),

Q("tv", KA, """Göğüs ağrısıyla gelen hastanın EKG'sinde inferior derivasyonlarda (II, III, aVF) ST yükselmesi ve
ikinci derece AV blok var. Tıkanan arter büyük olasılıkla hangisidir?""",
  "A. coronaria dextra",
  ["R. interventricularis anterior", "R. circumflexus", "A. coronaria sinistra'nın ana gövdesi", "R. marginalis sinister"],
  """Kalbin diyafragmatik (inferior) yüzü çoğu kişide sağ koroner arterin r. interventricularis posterior
  dalıyla beslenir. AV düğüm arteri de olguların yaklaşık %80–90'ında RCA'dan çıktığı için inferior MI'ya
  sıklıkla bradikardi ve AV blok eşlik eder.""",
  e=["aa-coronariae"]),

Q("t", KA, "İnterventriküler septumun ön üçte ikisini besleyen arter hangisidir?",
  "R. interventricularis anterior (LAD)",
  ["R. interventricularis posterior", "R. circumflexus", "R. marginalis dexter", "A. nodi sinuatrialis"],
  """LAD'nin septal dalları septumun ön 2/3'ünü (sol dal demetinin büyük kısmı dahil), PDA ise arka
  1/3'ünü besler. LAD en sık tıkanan koroner arterdir ve geniş anterior enfarktlara yol açar.""",
  e=["aa-coronariae", "ventriculus-sinister"]),

Q("t", KA, "Koroner dolaşımda 'sağ dominansı' neye göre tanımlanır?",
  "R. interventricularis posterior'un sağ koroner arterden çıkmasına",
  ["Sinoatriyal düğüm arterinin sağ koronerden çıkmasına", "Sağ koroner arterin daha kalın olmasına",
   "Sağ ventrikülün daha büyük olmasına", "Konus arterinin sağ aort sinüsünden çıkmasına"],
  """Dominans, kalbin arka yüzünü ve septumun arka kısmını besleyen PDA'nın kaynağına göre belirlenir.
  İnsanların yaklaşık %70'i sağ dominanttır; sol dominansta PDA sirkumfleks arterden çıkar.""",
  e=["aa-coronariae"]),

Q("f", KA, "V. cordis magna hangi arterle birlikte seyreder?",
  "R. interventricularis anterior",
  ["R. interventricularis posterior", "A. coronaria dextra", "R. marginalis dexter", "A. nodi atrioventricularis"],
  """V. cordis magna ön interventriküler olukta LAD ile yükselir, sol AV oluğa dönerek sinus coronarius'a
  dökülür. V. cordis media PDA ile, v. cordis parva sağ marjinal arter ile seyreder. Sinus coronarius sağ
  atriyuma açılır.""",
  e=["venae-cordis", "aa-coronariae"]),

Q("f", KA, "Kalbin doğal uyarı merkezi (sinoatriyal düğüm) nerede bulunur?",
  "Sağ atriyumda, v. cava superior'un açıldığı yerin yakınında, crista terminalis'in üst ucunda",
  ["Sol atriyumda, pulmoner venlerin ağzında", "İnterventriküler septumun membranöz bölümünde",
   "Koch üçgeninin tepesinde", "Sağ ventrikülün çıkış yolunda"],
  """SA düğüm epikardın hemen altında, VCS–sağ atriyum bileşkesinde yer alır ve olguların yaklaşık %60'ında
  sağ koroner arterden beslenir. Uyarı atriyumlardan AV düğüme, His demeti ve dallar aracılığıyla
  ventriküllere iletilir.""",
  e=["atrium-dextrum", "aa-coronariae"]),

Q("t", KA, "Kalp cerrahisinde aort ve truncus pulmonalis'in arkasından parmak geçirilerek kelepçe konabilen boşluk hangisidir?",
  "Sinus transversus pericardii",
  ["Sinus obliquus pericardii", "Recessus costodiaphragmaticus", "Sinus coronarius", "Fossa ovalis"],
  """Sinus transversus önde aort ve truncus pulmonalis, arkada VCS ve pulmoner venler arasındadır. Bypass
  ameliyatlarında büyük arterleri birlikte kontrol etmek için kullanılır. Sinus obliquus sol atriyumun
  arkasındaki kör ceptir.""",
  e=["pericardium", "aorta", "truncus-pulmonalis"]),

Q("fv", KA, """Göğsünden bıçaklanan hastada hipotansiyon, boyun venlerinde dolgunluk ve derinden gelen kalp
sesleri var (Beck üçlemesi). Perikardiyosentez için en sık kullanılan giriş yeri hangisidir?""",
  "Processus xiphoideus ile sol kaburga kavsi arasındaki açı (subksifoid yol)",
  ["Sağ 2. interkostal aralık, sternum kenarı", "Sol 2. interkostal aralık, midklavikular hat",
   "Sağ 5. interkostal aralık, ön aksiller hat", "Sol 8. interkostal aralık, arka aksiller hat"],
  """Kardiyak tamponadda perikard boşluğundaki kan kalbin dolmasını engeller. İğne subksifoid bölgeden sol
  omuza doğru yönlendirilir; bu yol plevra ve koroner arterlerden uzaktır.""",
  e=["pericardium"]),

Q("t", KA, "Perikardit ağrısının omuz ucuna yansımasının nedeni nedir?",
  "Fibröz ve parietal seröz perikardın duyusunun n. phrenicus (C3–C5) ile taşınması",
  ["Viseral perikardın n. vagus ile innerve edilmesi", "Perikardın interkostal sinirlerle innerve edilmesi",
   "Kalbin sempatik afferentlerinin T1–T4'e girmesi", "Perikardın plexus brachialis'ten lif alması"],
  """Parietal perikard somatik duyu alır ve bu lifler n. phrenicus ile taşınır; ağrı C4 dermatomu olan omuz
  ucuna yansır. Miyokard iskemisinin ağrısı ise sempatik afferentlerle T1–T4'e taşınır ve kolun iç yüzüne
  yansır.""",
  e=["pericardium", "n-phrenicus"]),

Q("f", KA, "Lig. arteriosum hangi iki yapıyı birbirine bağlar?",
  "A. pulmonalis sinistra ile arcus aortae",
  ["Truncus pulmonalis ile v. cava superior", "Aort kökü ile sağ atriyum", "A. pulmonalis dextra ile v. azygos",
   "Arcus aortae ile a. subclavia sinistra"],
  """Lig. arteriosum fetal ductus arteriosus'un kalıntısıdır; sol pulmoner arterin başlangıcı ile aort
  kemerinin alt yüzünü bağlar. Sol n. laryngeus recurrens bu bağın lateralinden aort kemerinin altına dolanır.""",
  e=["truncus-pulmonalis", "aorta", "n-vagus"]),

Q("f", KA, "Sol ventrikül ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Çıkış yolunda conus arteriosus (infundibulum) bulunur.",
  ["Duvarı sağ ventrikülden yaklaşık üç kat kalındır.", "Mitral kapağın iki yaprağı vardır.",
   "Ön ve arka olmak üzere iki papiller kası vardır.", "Kalbin apeksini oluşturur."],
  """Conus arteriosus (infundibulum) sağ ventrikülün düz duvarlı çıkış yoludur. Sol ventrikülün çıkış yolu
  vestibulum aortae olarak adlandırılır. Sol ventrikül sistemik basınca karşı çalıştığı için duvarı en
  kalın boşluktur.""",
  e=["ventriculus-sinister", "ventriculus-dexter", "valvae-cordis"]),

# ------------------------------------------------------------------ Aorta
Q("f", AO, "Arcus aortae'den sağdan sola doğru çıkan dallar hangisinde doğru sıralanmıştır?",
  "Truncus brachiocephalicus, a. carotis communis sinistra, a. subclavia sinistra",
  ["A. subclavia dextra, a. carotis communis dextra, a. carotis communis sinistra",
   "Truncus brachiocephalicus, a. subclavia sinistra, a. carotis communis sinistra",
   "A. carotis communis sinistra, truncus brachiocephalicus, a. subclavia sinistra",
   "Aa. coronariae, truncus brachiocephalicus, a. subclavia sinistra"],
  """Arcus aortae genellikle üç dal verir. Truncus brachiocephalicus sağ sternoklavikular eklemin arkasında
  sağ a. subclavia ve sağ a. carotis communis'e ayrılır. Koroner arterler çıkan aortadan çıkar.""",
  e=["aorta", "truncus-brachiocephalicus"]),

Q("tv", AO, """16 yaşında hipertansif hastada kollarda kan basıncı yüksek, bacaklarda nabızlar zayıf ve gecikmeli.
Göğüs grafisinde kaburgaların alt kenarlarında çentiklenme görülüyor. Çentiklerin nedeni hangi damarların
genişlemesidir?""",
  "Aa. intercostales posteriores (kollateral dolaşım)",
  ["Aa. coronariae", "Vv. intercostales anteriores", "Aa. bronchiales", "A. thoracica lateralis"],
  """Aort koarktasyonunda (genellikle lig. arteriosum düzeyinde) kan; a. subclavia → a. thoracica interna →
  ön interkostal arterler → arka interkostal arterler yoluyla inen aortaya ulaşır. Genişleyen arka
  interkostal arterler kaburgaların alt kenarını aşındırır (3–8. kaburgalar).""",
  e=["aorta", "a-subclavia", "costae"]),

Q("f", AO, "Abdominal aorta hangi düzeyde iki a. iliaca communis'e ayrılır?",
  "L4 (yaklaşık göbek düzeyi)",
  ["T12", "L1", "L2", "S2"],
  """Abdominal aorta hiatus aorticus'tan (T12) sonra omurganın solunda iner ve L4 düzeyinde ikiye ayrılır;
  bu nokta yaklaşık göbeğin hemen altına ve krista iliaka çizgisine karşılık gelir.""",
  e=["aorta", "a-iliaca-communis"]),

Q("fv", AO, """70 yaşında sigara içen erkekte karında pulsatil kitle saptanıyor. Abdominal aort anevrizmalarının en
sık yerleştiği bölge hangisidir?""",
  "Renal arterlerin altında (infrarenal), bifurkasyonun üstünde",
  ["Truncus coeliacus'un üstünde", "Renal arterlerin çıkış düzeyinde", "A. iliaca externa'da", "Hiatus aorticus'ta"],
  """Abdominal aort anevrizmalarının büyük çoğunluğu infrarenal yerleşimlidir. Bu bölgede vasa vasorum
  azdır ve elastin içeriği düşüktür. Rüptür riski çap ile birlikte artar.""",
  e=["aorta", "aa-renales"]),

# ------------------------------------------------------------------ Baş ve boyun
Q("f", BB, "A. carotis communis genellikle hangi düzeyde a. carotis interna ve externa'ya ayrılır?",
  "Cartilago thyroidea'nın üst kenarı (C4)",
  ["Cartilago cricoidea düzeyi (C6)", "Angulus mandibulae'nin üstü (C2)", "Os hyoideum'un gövdesi (C3)", "Sternoklavikular eklem düzeyi"],
  """Karotis bifurkasyonu tiroid kıkırdağın üst kenarı hizasındadır. Bu bölgede ICA'nın başlangıcındaki
  genişleme (sinus caroticus) baroreseptör, bifurkasyondaki küçük cisim (glomus caroticum) kemoreseptördür;
  ikisi de n. glossopharyngeus ile innerve edilir.""",
  e=["a-carotis-communis", "a-carotis-interna", "a-carotis-externa"]),

Q("fv", BB, "Supraventriküler taşikardisi olan hastada boyunda karotis sinüs masajı yapılıyor. Kalp hızındaki azalmanın afferent ve efferent yolu hangisidir?",
  "Afferent: n. glossopharyngeus – Efferent: n. vagus",
  ["Afferent: n. vagus – Efferent: n. glossopharyngeus", "Afferent: n. accessorius – Efferent: n. vagus",
   "Afferent: sempatik zincir – Efferent: n. phrenicus", "Afferent: n. hypoglossus – Efferent: n. vagus"],
  """Sinus caroticus'taki baroreseptörler basınç artışını IX'un karotis sinüs dalıyla beyin sapına bildirir;
  yanıt olarak vagal çıkış artar ve kalp hızı yavaşlar. Yaşlılarda aşırı duyarlılık senkopa yol açabilir.""",
  e=["a-carotis-interna", "n-glossopharyngeus", "n-vagus"]),

Q("f", BB, "Boyunda hiç dal vermeyen arter hangisidir?",
  "A. carotis interna",
  ["A. carotis externa", "A. subclavia", "A. vertebralis", "Truncus thyrocervicalis"],
  """A. carotis interna boyunda dal vermeden canalis caroticus'a girer; ilk önemli dalı kafa içinde
  a. ophthalmica'dır. Bu özellik cerrahide ICA'yı ECA'dan ayırt etmeye yarar.""",
  e=["a-carotis-interna"]),

Q("t", BB, "Aşağıdakilerden hangisi a. carotis externa'nın dalı değildir?",
  "A. ophthalmica",
  ["A. thyroidea superior", "A. lingualis", "A. facialis", "A. maxillaris"],
  """ECA'nın dalları: a. thyroidea superior, a. pharyngea ascendens, a. lingualis, a. facialis, a. occipitalis,
  a. auricularis posterior ve uç dalları a. maxillaris ile a. temporalis superficialis. A. ophthalmica ICA'nın
  kafa içindeki ilk dalıdır.""",
  e=["a-carotis-externa", "a-carotis-interna"]),

Q("f", BB, "A. meningea media hangi arterin dalıdır?",
  "A. maxillaris",
  ["A. temporalis superficialis", "A. carotis interna", "A. occipitalis", "A. ophthalmica"],
  """A. maxillaris fossa infratemporalis'te a. meningea media'yı verir; bu arter foramen spinosum'dan kafa
  içine girerek duranın büyük kısmını ve kafatası kemiklerini besler.""",
  e=["a-carotis-externa", "meninges"]),

Q("f", BB, "Yüzde a. facialis'in nabzı en kolay nerede alınır?",
  "M. masseter'in ön kenarında, mandibula alt kenarı üzerinde",
  ["Tragusun önünde", "Foramen infraorbitale'nin üzerinde", "Angulus mandibulae'nin arkasında", "Göz iç köşesinde"],
  """A. facialis mandibula alt kenarını masseter'in ön kenarında çaprazlar ve burada kemiğe bastırılarak
  hissedilir. Kıvrımlı bir seyirle ağız köşesinden göz iç köşesine (a. angularis) uzanır.""",
  e=["a-carotis-externa", "m-masseter"]),

Q("fv", BB, """70 yaşında kadında yeni başlayan şakak ağrısı, çiğnerken çenede ağrı ve görme bulanıklığı var;
sedimentasyon yüksek. Tanı için biyopsi en sık hangi arterden alınır?""",
  "A. temporalis superficialis",
  ["A. facialis", "A. occipitalis", "A. carotis interna", "A. maxillaris"],
  """Dev hücreli (temporal) arterit orta ve büyük çaplı arterleri, özellikle ECA dallarını tutar. Tragusun
  önünde kolay ele gelen a. temporalis superficialis biyopsi için uygundur. Tedavi gecikirse
  a. ophthalmica tutulumu kalıcı körlüğe yol açabilir.""",
  e=["a-carotis-externa"]),

Q("t", BB, "A. cerebelli inferior posterior (PICA) hangi arterin dalıdır?",
  "A. vertebralis",
  ["A. basilaris", "A. cerebri posterior", "A. carotis interna", "A. spinalis anterior"],
  """PICA genellikle vertebral arterin kafa içindeki en büyük dalıdır. AICA ve SCA baziler arterden çıkar;
  baziler arter pons'un üst sınırında iki PCA'ya ayrılır. PICA tıkanması lateral medüller sendroma yol açar.""",
  e=["a-vertebralis", "circulus-arteriosus", "cerebellum"]),

Q("t", BB, "Aşağıdaki arterlerden hangisi Willis poligonunun (circulus arteriosus cerebri) bir parçası değildir?",
  "A. cerebri media",
  ["A. communicans anterior", "A. cerebri anterior (A1 bölümü)", "A. communicans posterior", "A. cerebri posterior (P1 bölümü)"],
  """Willis poligonunu ACom, iki ACA'nın A1 bölümleri, iki ICA'nın uçları, iki PCom ve iki PCA'nın P1 bölümleri
  oluşturur. MCA ICA'nın devamıdır ancak halkaya katılmaz.""",
  e=["circulus-arteriosus", "a-carotis-interna"]),

Q("tv", BB, """65 yaşında hastada tek gözde aniden başlayan ağrısız tam görme kaybı var. Fundusta retina soluk, makula
'kiraz kırmızısı' görünümde. Tıkanan arter hangisidir?""",
  "A. centralis retinae",
  ["A. cerebri posterior", "A. ciliaris posterior longa", "A. lacrimalis", "A. supraorbitalis"],
  """A. centralis retinae a. ophthalmica'nın dalıdır ve n. opticus içinden göze girer. Bir uç arter olduğundan
  tıkanmasında retinanın iç katmanları iskemiye girer; koroidden beslenen fovea kırmızı nokta olarak görünür.""",
  e=["retina", "a-carotis-interna"]),

Q("tv", BB, """Sol kolunu uzun süre kullandığında baş dönmesi ve görme bulanıklığı yaşayan hastada sol kol tansiyonu
sağdan belirgin düşük. Anjiyografide sol a. subclavia'nın başlangıcında darlık var. Belirtilerin
mekanizması nedir?""",
  "Sol a. vertebralis'te ters akım (subklavyen çalma sendromu)",
  ["Sol a. carotis interna'da ters akım", "Sağ a. vertebralis'in tıkanması", "A. basilaris'te anevrizma", "A. thoracica interna'nın tıkanması"],
  """Darlık vertebral arterin çıkışından önce olduğunda kol egzersizinde kan beyin sapından sol vertebral arter
  yoluyla kola doğru 'çalınır'; vertebrobaziler yetmezlik belirtileri ortaya çıkar.""",
  e=["a-subclavia", "a-vertebralis"]),

Q("t", BB, "Koroner bypass ameliyatlarında greft olarak en sık kullanılan ve uzun dönem açıklığı en iyi olan arter hangisinin dalıdır?",
  "A. subclavia (a. thoracica interna)",
  ["A. axillaris (a. thoracica lateralis)", "Aorta descendens (a. intercostalis)", "A. carotis communis", "Truncus thyrocervicalis"],
  """A. thoracica interna (mammaria interna) a. subclavia'nın ilk bölümünden çıkar ve sternum kenarına yakın
  iner. Sol internal torasik arterin LAD'ye bağlanması (LIMA–LAD) en iyi uzun dönem sonuçları verir.""",
  e=["a-subclavia", "aa-coronariae"]),

Q("t", BB, "Truncus thyrocervicalis'in dalı olmayan arter hangisidir?",
  "A. thyroidea superior",
  ["A. thyroidea inferior", "A. suprascapularis", "A. transversa colli (a. cervicalis transversa)", "A. cervicalis ascendens"],
  """Truncus thyrocervicalis a. subclavia'dan çıkar ve a. thyroidea inferior (dalı a. cervicalis ascendens),
  a. suprascapularis ve a. transversa colli'yi verir. A. thyroidea superior ECA'nın ilk dalıdır.""",
  e=["a-subclavia", "glandula-thyroidea"]),

# ------------------------------------------------------------------ Üst ekstremite
Q("t", UE, "Aşağıdakilerden hangisi a. axillaris'in üçüncü bölümünün dalıdır?",
  "A. subscapularis",
  ["A. thoracica superior", "A. thoracoacromialis", "A. thoracica lateralis", "A. thoracica interna"],
  """Birinci bölüm (pectoralis minor'un üstü): a. thoracica superior. İkinci bölüm (arkası): a. thoracoacromialis
  ve a. thoracica lateralis. Üçüncü bölüm (altı): a. subscapularis ile ön ve arka sirkumfleks humeral arterler.
  A. thoracica interna ise a. subclavia'dan çıkar.""",
  e=["a-axillaris", "m-pectoralis-minor"]),

Q("t", UE, "A. axillaris truncus thyrocervicalis ile a. subscapularis arasında bağlanırsa kolun kanlanmasını sürdüren kollateral ağ hangisidir?",
  "Skapula çevresi anastomozu (a. suprascapularis, a. dorsalis scapulae, a. circumflexa scapulae)",
  ["Dirsek çevresi anastomozu", "Arcus palmaris profundus", "Torakoakromiyal anastomoz", "Aa. intercostales anteriores"],
  """Skapula etrafında a. subclavia dalları (a. suprascapularis, a. dorsalis scapulae) ile a. axillaris'in
  dalı a. subscapularis (a. circumflexa scapulae) anastomoz yapar. Bu nedenle bağlama, iki dal arasında
  yapılırsa kol beslenmeye devam eder.""",
  e=["a-axillaris", "a-subclavia", "scapula"]),

Q("f", UE, "N. radialis ile birlikte sulcus nervi radialis'te seyreden arter hangisidir?",
  "A. profunda brachii",
  ["A. collateralis ulnaris superior", "A. circumflexa humeri posterior", "A. brachialis", "A. recurrens radialis"],
  """A. profunda brachii kolun en büyük dalıdır ve n. radialis ile humerusun arka yüzündeki olukta seyreder;
  kolun arka kompartmanını besler ve dirsek çevresi anastomozuna katılır.""",
  e=["a-brachialis", "n-radialis", "humerus"]),

Q("f", UE, "El bileğinde radial nabız hangi tendonun hemen lateralinde alınır?",
  "M. flexor carpi radialis",
  ["M. palmaris longus", "M. flexor carpi ulnaris", "M. abductor pollicis longus", "M. brachioradialis"],
  """A. radialis bilekte radiusun distal ucunun önünde, FCR tendonunun lateralinde yüzeyel seyreder ve kemiğe
  bastırılarak hissedilir. Daha sonra tabakiyerin tabanından el sırtına geçer.""",
  e=["a-radialis", "m-flexor-carpi-radialis"]),

Q("fv", UE, "Yoğun bakımda radial arter kanülasyonu öncesinde Allen testi yapılıyor. Bu testin amacı nedir?",
  "El kanlanmasının a. ulnaris ve palmar arkuslar yoluyla yeterli olup olmadığını değerlendirmek",
  ["A. radialis'in duvar kalınlığını ölçmek", "Venöz geri dönüşü değerlendirmek", "N. medianus'un işlevini test etmek",
   "A. brachialis'teki darlığı saptamak"],
  """Radial ve ulnar arterlere aynı anda bası yapılıp el soldurulur, sonra ulnar arter serbest bırakılır.
  Elin hızla pembeleşmesi ulnar arter ve yüzeyel palmar arkusun yeterli olduğunu, radial arter tıkansa
  bile elin beslenebileceğini gösterir.""",
  e=["a-ulnaris", "a-radialis", "arcus-palmares"]),

Q("f", UE, "Arcus palmaris superficialis'i esas olarak hangi arter oluşturur?",
  "A. ulnaris",
  ["A. radialis", "A. interossea anterior", "A. princeps pollicis", "A. mediana"],
  """Yüzeyel palmar arkus esas olarak a. ulnaris'in devamıdır ve radial arterin yüzeyel palmar dalıyla tamamlanır;
  derin palmar arkus ise esas olarak a. radialis'ten oluşur ve daha proksimalde yer alır.""",
  e=["arcus-palmares", "a-ulnaris"]),

Q("t", UE, "A. interossea communis hangi arterin dalıdır?",
  "A. ulnaris",
  ["A. radialis", "A. brachialis", "A. profunda brachii", "A. recurrens radialis"],
  """A. ulnaris kübital çukurun hemen altında a. interossea communis'i verir; bu arter membrana interossea'nın
  önünde ve arkasında seyreden ön ve arka interosseöz arterlere ayrılır.""",
  e=["a-ulnaris"]),

Q("f", UE, "Tansiyon ölçümünde stetoskobun yerleştirildiği arter hangisidir?",
  "A. brachialis",
  ["A. radialis", "A. axillaris", "A. ulnaris", "A. profunda brachii"],
  """Manşet kola sarılır; stetoskop kübital çukurda, biseps tendonunun hemen medialindeki a. brachialis
  üzerine konur. Korotkoff sesleri burada dinlenir.""",
  e=["a-brachialis"]),

# ------------------------------------------------------------------ Karın ve pelvis
Q("f", KP, "Truncus coeliacus'un üç dalı hangileridir?",
  "A. gastrica sinistra, a. splenica, a. hepatica communis",
  ["A. gastrica dextra, a. splenica, a. hepatica propria", "A. gastroduodenalis, a. splenica, a. mesenterica superior",
   "A. gastrica sinistra, a. gastroduodenalis, a. renalis", "A. phrenica inferior, a. splenica, a. hepatica communis"],
  """Truncus coeliacus T12 düzeyinde aortanın önünden çıkar ve ön bağırsak türevlerini (abdominal özofagus,
  mide, duodenumun üst kısmı, karaciğer, safra kesesi, pankreasın bir kısmı ve dalak) besler.""",
  e=["truncus-coeliacus"]),

Q("tv", KP, """Peptik ülser öyküsü olan hasta masif hematemez ile geliyor. Endoskopide duodenumun birinci
bölümünün arka duvarında kanayan ülser görülüyor. Kanayan arter büyük olasılıkla hangisidir?""",
  "A. gastroduodenalis",
  ["A. gastrica sinistra", "A. splenica", "A. pancreaticoduodenalis inferior", "A. mesenterica superior"],
  """A. gastroduodenalis a. hepatica communis'ten çıkar ve duodenumun ilk bölümünün hemen arkasından iner. Arka
  duvar ülserleri bu arteri aşındırarak ciddi kanamaya yol açar. Ön duvar ülserleri ise daha çok perforasyon
  yapar.""",
  e=["truncus-coeliacus", "duodenum"]),

Q("t", KP, "A. splenica için aşağıdakilerden hangisi yanlıştır?",
  "A. gastroepiploica dextra'yı verir.",
  ["Pankreasın üst kenarı boyunca kıvrımlı seyreder.", "Aa. gastricae breves ile mide fundusunu besler.",
   "Lig. splenorenale içinde dalağa ulaşır.", "Truncus coeliacus'un en büyük dalıdır."],
  """A. splenica a. gastroepiploica sinistra'yı ve kısa gastrik arterleri verir. A. gastroepiploica dextra ise
  a. gastroduodenalis'in dalıdır; iki gastroepiploik arter midenin büyük kurvaturunda anastomoz yapar.""",
  e=["truncus-coeliacus", "splen", "gaster"]),

Q("f", KP, "A. mesenterica superior'un beslediği alan hangisidir?",
  "Duodenumun inen kısmının ortasından colon transversum'un yaklaşık sol üçte birine kadar olan bağırsak",
  ["Özofagustan duodenumun ortasına kadar", "Colon transversum'un sol 1/3'ünden rektumun üst kısmına kadar",
   "Yalnızca jejunum ve ileum", "Mide ve dalak"],
  """SMA (L1) orta bağırsak türevlerini besler: duodenumun papilla major'dan sonraki kısmı, jejunum, ileum,
  çekum, apendiks, çıkan kolon ve transvers kolonun proksimal 2/3'ü. Dalları: a. pancreaticoduodenalis
  inferior, jejunal ve ileal arterler, a. ileocolica, a. colica dextra ve media.""",
  e=["a-mesenterica-superior", "intestinum-tenue"]),

Q("tv", KP, """Hızlı kilo kaybı sonrası yemekten sonra şiddetli kusma ve şişkinlik yaşayan genç kadında, duodenumun
aorta ile bir damar arasında sıkıştığı saptanıyor. Bu damar hangisidir ve duodenumun hangi bölümü
etkilenmiştir?""",
  "A. mesenterica superior – duodenumun üçüncü (yatay) bölümü",
  ["Truncus coeliacus – duodenumun birinci bölümü", "A. mesenterica inferior – duodenumun dördüncü bölümü",
   "A. renalis sinistra – duodenumun ikinci bölümü", "V. portae hepatis – duodenumun birinci bölümü"],
  """Duodenumun yatay bölümü L3 düzeyinde aorta ile SMA arasından geçer. Retroperitoneal yağ dokusu azalınca
  aradaki açı daralır ve duodenum sıkışır (SMA sendromu, Wilkie sendromu).""",
  e=["a-mesenterica-superior", "duodenum", "aorta"]),

Q("t", KP, "Kolonun kanlanmasında 'su ayrım bölgesi' olarak bilinen ve iskemiye en duyarlı bölge hangisidir?",
  "Flexura coli sinistra (SMA ile IMA sulama alanlarının birleşimi)",
  ["Çekum", "Flexura coli dextra", "Rektumun alt kısmı", "Colon ascendens'in ortası"],
  """Sol kolon bükümü (Griffiths noktası) SMA'nın a. colica media'sı ile IMA'nın a. colica sinistra'sının
  uç bölgelerinin buluştuğu, marjinal arterin (Drummond) zayıf olabildiği bölgedir. Rektosigmoid bileşke
  (Sudeck noktası) diğer kritik bölgedir.""",
  e=["a-mesenterica-inferior", "a-mesenterica-superior", "intestinum-crassum"]),

Q("f", KP, "A. mesenterica inferior'un uç dalı olarak rektumun üst kısmını besleyen arter hangisidir?",
  "A. rectalis superior",
  ["A. rectalis media", "A. rectalis inferior", "A. sigmoidea", "A. sacralis mediana"],
  """IMA (L3) a. colica sinistra, aa. sigmoideae ve a. rectalis superior'u verir. A. rectalis media
  a. iliaca interna'dan, a. rectalis inferior a. pudenda interna'dan çıkar.""",
  e=["a-mesenterica-inferior", "rectum"]),

Q("f", KP, "Renal arterler için aşağıdakilerden hangisi doğrudur?",
  "Sağ renal arter v. cava inferior'un arkasından geçer.",
  ["Sol renal arter sağdan daha uzundur.", "Segmental arterler arasında geniş anastomozlar vardır.",
   "T10 düzeyinde aortadan çıkarlar.", "Renal venlerin önünde seyrederler."],
  """Renal arterler L1–L2 düzeyinde çıkar; aorta sola yakın olduğu için sağ renal arter daha uzundur ve VCI'nın
  arkasından geçer. Hilumda önden arkaya ven, arter, pelvis sıralanır. Segmental arterler uç arterdir.""",
  e=["aa-renales", "ren", "v-cava-inferior"]),

Q("t", KP, "A. iliaca interna'nın posterior trunkusundan çıkan arter hangisidir?",
  "A. glutea superior",
  ["A. glutea inferior", "A. pudenda interna", "A. obturatoria", "A. uterina"],
  """Arka trunkus a. iliolumbalis, aa. sacrales laterales ve a. glutea superior'u verir. Ön trunkus visseral
  dalları (a. umbilicalis, a. vesicalis inferior/a. vaginalis, a. uterina, a. rectalis media) ve parietal
  dalları (a. obturatoria, a. pudenda interna, a. glutea inferior) verir.""",
  e=["a-iliaca-communis"]),

Q("f", KP, "A. epigastrica inferior hangi arterin dalıdır?",
  "A. iliaca externa",
  ["A. iliaca interna", "A. femoralis", "A. thoracica interna", "A. obturatoria"],
  """A. epigastrica inferior lig. inguinale'nin hemen üstünde a. iliaca externa'dan çıkar, derin inguinal
  halkanın medialinden yükselir ve rectus kılıfında a. epigastrica superior (a. thoracica interna'nın dalı)
  ile anastomoz yapar.""",
  e=["a-iliaca-communis", "m-rectus-abdominis"]),

Q("t", KP, "A. iliaca communis bifurkasyonu ile ilgili hangisi doğrudur?",
  "Sakroiliak eklemin önünde olur ve üreter genellikle bu bölgede iliak damarları çaprazlar.",
  ["L1 düzeyinde, böbreklerin hilumunda olur.", "V. cava inferior bu noktanın önünden geçer.",
   "A. iliaca interna bu noktadan sonra uyluğa iner.", "Ductus deferens bifurkasyonun arkasından geçer."],
  """Ortak iliak arterler sakroiliak eklemin önünde iç ve dış iliak arterlere ayrılır. Üreter pelvis girişinde bu
  bifurkasyonun önünden geçer; bu nokta üreterin fizyolojik darlıklarından biridir ve taşların takıldığı yerdir.""",
  e=["a-iliaca-communis", "ureter"]),

# ------------------------------------------------------------------ Alt ekstremite
Q("f", AE, "A. femoralis'in nabzı en iyi nerede alınır?",
  "Lig. inguinale'nin altında, SIAS ile symphysis pubica arasının orta noktasında (mid-inguinal nokta)",
  ["Tuberculum pubicum'un hemen üstünde", "Uyluğun ortasında, sartorius'un dış kenarında",
   "Adductor hiatus düzeyinde", "Trochanter major'un arkasında"],
  """A. femoralis lig. inguinale'nin altından femoral üçgene girer ve mid-inguinal noktada kemiğe (caput femoris,
  pubis) bastırılarak hissedilir. Kateterizasyon için en sık kullanılan arterdir; ven arterin hemen
  medialindedir.""",
  e=["a-femoralis", "trigonum-femorale"]),

Q("f", AE, "A. profunda femoris'in dalları hangileridir?",
  "A. circumflexa femoris medialis, a. circumflexa femoris lateralis ve perforan arterler",
  ["A. epigastrica superficialis ve a. circumflexa ilium superficialis", "A. obturatoria ve a. glutea inferior",
   "A. genus descendens ve a. poplitea", "A. pudenda externa ve a. epigastrica inferior"],
  """Derin femoral arter uyluğun ana besleyicisidir; iki sirkumfleks arter kalça çevresini, perforan arterler
  uyluğun arka kompartmanını besler. Medial sirkumfleks arter femur başının ana kaynağıdır.""",
  e=["a-femoralis", "femur"]),

Q("t", AE, "Fossa poplitea'da yüzeyelden derine doğru yapıların sıralaması hangisidir?",
  "N. tibialis – v. poplitea – a. poplitea",
  ["A. poplitea – v. poplitea – n. tibialis", "V. poplitea – n. tibialis – a. poplitea",
   "N. tibialis – a. poplitea – v. poplitea", "A. poplitea – n. tibialis – v. poplitea"],
  """Popliteal çukurda sinir en yüzeyde, ven ortada, arter en derindedir (femur ve diz kapsülüne yaslanır).
  Bu nedenle popliteal nabız diz hafif bükülüyken derine bastırılarak alınır ve suprakondiler femur
  kırıklarında arter yaralanabilir.""",
  e=["a-poplitea", "fossa-poplitea", "n-tibialis"]),

Q("f", AE, "A. dorsalis pedis nabzı en iyi nerede alınır?",
  "Ayak sırtında, m. extensor hallucis longus tendonunun lateralinde",
  ["Malleolus medialis'in arkasında", "Malleolus lateralis'in önünde", "Topuğun iç yanında", "5. metatarsın tabanında"],
  """A. dorsalis pedis a. tibialis anterior'un devamıdır; ayak sırtında EHL tendonunun hemen lateralinde,
  1. ve 2. metatarslar arasında hissedilir. Periferik arter hastalığında ilk kaybolan nabızlardandır.""",
  e=["a-dorsalis-pedis", "a-tibialis-anterior", "m-extensor-hallucis-longus"]),

Q("t", AE, "A. fibularis (peronea) hangi arterin dalıdır?",
  "A. tibialis posterior",
  ["A. tibialis anterior", "A. poplitea'nın doğrudan dalı", "A. dorsalis pedis", "A. femoralis"],
  """A. tibialis posterior bacağın üst kısmında a. fibularis'i verir; bu arter fibulaya yakın seyreder ve
  lateral kompartman kaslarını perforan dallarla besler. Fibula serbest flebi bu arter üzerinde kaldırılır.""",
  e=["a-tibialis-posterior", "fibula"]),

Q("t", AE, "Kalça bölgesindeki çapraz (krusiat) anastomoza katılan arterler hangileridir?",
  "A. glutea inferior, medial ve lateral sirkumfleks femoral arterler ve 1. perforan arter",
  ["A. glutea superior, a. obturatoria ve a. pudenda interna", "A. epigastrica inferior ve a. obturatoria",
   "A. poplitea'nın genikular dalları", "A. iliolumbalis ve aa. sacrales laterales"],
  """Krusiat anastomoz trochanter minor düzeyinde, femurun arkasında kurulur ve a. iliaca interna ile
  a. femoralis sistemleri arasında kollateral yol sağlar. Femoral arterin proksimal tıkanmasında önemlidir.""",
  e=["a-femoralis", "femur"]),

# ------------------------------------------------------------------ Venler
Q("fv", VE, """Şokta olan ve periferik ven bulunamayan hastada acil 'venöz cutdown' için en güvenilir yer olarak
kullanılan ven hangisidir?""",
  "V. saphena magna – malleolus medialis'in önünde",
  ["V. saphena parva – malleolus lateralis'in arkasında", "V. cephalica – sulcus deltopectoralis'te",
   "V. basilica – dirseğin iç yanında", "V. jugularis externa – boyunda"],
  """V. saphena magna medial malleolün hemen önünde sabit ve yüzeyeldir; bu nedenle cutdown için klasik yerdir.
  Bu bölgede n. saphenus ven ile birlikte seyreder ve işlem sırasında korunmalıdır.""",
  e=["v-saphena-magna"]),

Q("f", VE, "V. saphena magna hangi vene dökülür?",
  "V. femoralis (hiatus saphenus'ta)",
  ["V. poplitea", "V. iliaca interna", "V. profunda femoris", "V. iliaca externa"],
  """V. saphena magna uyluğun iç yüzünden yükselir ve tuberculum pubicum'un yaklaşık 3–4 cm alt-yanındaki
  hiatus saphenus'tan fascia lata'yı geçerek v. femoralis'e dökülür. Koroner bypassta greft olarak
  kullanılır.""",
  e=["v-saphena-magna", "v-femoralis"]),

Q("f", VE, "V. saphena parva için aşağıdakilerden hangisi doğrudur?",
  "Malleolus lateralis'in arkasından geçer ve genellikle v. poplitea'ya dökülür.",
  ["Malleolus medialis'in önünden geçer.", "V. femoralis'e dökülür.", "N. saphenus ile birlikte seyreder.", "Derin fasyanın altında, kas içinde seyreder."],
  """Küçük safen ven ayak dış kenarından başlar, lateral malleolün arkasından baldırın orta hattına yükselir ve
  popliteal çukurda v. poplitea'ya açılır. Baldırda n. suralis ile birlikte seyreder.""",
  e=["v-saphena-parva", "fossa-poplitea"]),

Q("f", VE, "V. cava inferior hangi düzeyde oluşur ve diyaframı hangi düzeyde geçer?",
  "L5'te oluşur, T8'de diyaframı geçer.",
  ["L1'de oluşur, T10'da diyaframı geçer.", "L4'te oluşur, T12'de diyaframı geçer.",
   "S1'de oluşur, T10'da diyaframı geçer.", "L3'te oluşur, T8'de diyaframı geçer."],
  """İki v. iliaca communis L5 düzeyinde, aort bifurkasyonunun sağında ve biraz altında birleşerek VCI'yı
  oluşturur. VCI diyaframın tendinöz merkezindeki foramen venae cavae'den (T8) geçer.""",
  e=["v-cava-inferior", "diaphragma"]),

Q("f", VE, "V. cava superior'a sağ arka yüzden açılan ven hangisidir?",
  "V. azygos",
  ["V. hemiazygos", "V. thoracica interna", "V. jugularis externa", "V. subclavia dextra"],
  """V. azygos T4 düzeyinde sağ akciğer kökünün üzerinden kemer yaparak VCS'ye açılır. Arka interkostal venleri,
  özofagus ve bronş venlerini toplar; VCI tıkanmasında önemli bir kollateral yoldur.""",
  e=["v-azygos", "v-cava-superior"]),

Q("f", VE, "V. portae hepatis nerede ve hangi venlerin birleşmesiyle oluşur?",
  "Pankreas boynunun arkasında, v. mesenterica superior ile v. splenica'nın birleşmesiyle",
  ["Karaciğer hilusunda, v. hepatica dextra ile sinistra'nın birleşmesiyle", "Duodenumun önünde, v. gastrica sinistra ile v. splenica'nın birleşmesiyle",
   "Pankreas kuyruğunun arkasında, v. renalis ile v. splenica'nın birleşmesiyle", "Mide küçük kurvaturunda, v. gastrica dextra ile sinistra'nın birleşmesiyle"],
  """V. portae L1–L2 düzeyinde pankreas boynunun arkasında oluşur; v. mesenterica inferior çoğunlukla v. splenica'ya
  açılır. Ven lig. hepatoduodenale içinde, safra kanalı ve hepatik arterin arkasında yükselir.""",
  e=["v-portae-hepatis", "pancreas"]),

Q("tv", VE, """Alkolik siroz tanılı hasta masif kan kusmayla getiriliyor; muayenede karın duvarında göbek çevresinde
genişlemiş venler (caput medusae) ve hemoroidler var. Kusmanın kaynağı olan portokaval anastomoz hangisidir?""",
  "V. gastrica sinistra ile vv. oesophageae (v. azygos sistemi) arasındaki anastomoz",
  ["V. rectalis superior ile v. rectalis media arasındaki anastomoz", "Vv. paraumbilicales ile v. epigastrica superficialis arasındaki anastomoz",
   "V. colica sinistra ile v. renalis arasındaki anastomoz", "V. splenica ile v. renalis sinistra arasındaki anastomoz"],
  """Portal hipertansiyonda kan sistemik venlere kollaterallerle geçer: özofagusun alt ucunda özofagus varisleri
  (kanaması ölümcül olabilir), anorektal bölgede rektal varisler, göbek çevresinde caput medusae ve
  retroperitoneal anastomozlar.""",
  e=["v-portae-hepatis", "oesophagus", "v-azygos"]),

Q("f", VE, "Boyunda v. jugularis interna'nın a. carotis communis'e göre konumu nedir?",
  "Vagina carotica içinde arterin lateralinde",
  ["Arterin medialinde, trakeaya yakın", "Arterin arkasında, prevertebral fasyanın altında",
   "Karotis kılıfının dışında, SCM'nin yüzeyinde", "Arterin önünde, tiroid bezinin içinde"],
  """Karotis kılıfında a. carotis communis medialde, v. jugularis interna lateralde, n. vagus ikisinin arkasında
  yer alır. Santral kateter takılırken ven SCM'nin iki başı arasındaki üçgenden, arterin lateralinden aranır.""",
  e=["v-jugularis-interna", "a-carotis-communis", "n-vagus"]),

Q("f", VE, "Juguler venöz basınç (JVP) gözlemlenirken boyunda görülen ve SCM'yi yüzeysel olarak çaprazlayan ven hangisidir?",
  "V. jugularis externa",
  ["V. jugularis interna", "V. vertebralis", "V. thyroidea media", "V. facialis"],
  """V. jugularis externa SCM'nin yüzeyinden çapraz olarak iner ve klavikulanın üstünde v. subclavia'ya açılır.
  Sağ kalp yetmezliğinde dolgunlaşır. JVP'nin asıl değerlendirildiği ven ise iç juguler vendir.""",
  e=["v-jugularis-externa", "m-sternocleidomastoideus"]),

Q("t", VE, "Subklavyen ven kateterizasyonunda en sık görülen ciddi komplikasyon hangisidir ve nedeni nedir?",
  "Pnömotoraks; plevra kubbesi (cupula pleurae) venin hemen arkasında ve altında olduğu için",
  ["Hemoperikard; ven doğrudan perikarda açıldığı için", "N. phrenicus felci; sinir venin içinden geçtiği için",
   "Şilotoraks; sağ tarafta ductus thoracicus bulunduğu için", "Hava embolisi olmaz, çünkü ven kapaklıdır."],
  """V. subclavia klavikula ile 1. kaburga arasında, m. scalenus anterior'un önünde seyreder. Plevra ve akciğer
  apeksi hemen arkasında olduğundan iğne derine ilerlerse pnömotoraks gelişir. Ductus thoracicus sol venöz
  açıya döküldüğü için sol taraf girişimlerinde şilotoraks riski vardır.""",
  e=["v-subclavia", "pleura"]),

Q("f", VE, "Kan almak için en sık kullanılan, dirsek önündeki yüzeyel ven hangisidir?",
  "V. mediana cubiti",
  ["V. basilica", "V. cephalica", "V. brachialis", "V. axillaris"],
  """V. mediana cubiti v. cephalica'yı v. basilica'ya bağlar ve aponeurosis bicipitalis'in üzerinde yer alır;
  bu aponevroz alttaki a. brachialis ve n. medianus'u korur.""",
  e=["vv-membri-superioris"]),

Q("f", VE, "V. cephalica nerede derin vene açılır?",
  "Sulcus deltopectoralis'ten geçerek v. axillaris'e",
  ["Dirsekte v. brachialis'e", "Koltuk altında v. basilica'ya", "Boyunda v. jugularis externa'ya", "Kolun ortasında v. brachialis'e"],
  """V. cephalica önkol ve kolun dış yanında yükselir, deltoid ile pectoralis major arasındaki oluktan
  klavipektoral fasyayı delerek v. axillaris'e açılır. V. basilica ise kolun ortasında derin fasyayı delip
  brakiyal venlerle birleşerek v. axillaris'i oluşturur.""",
  e=["vv-membri-superioris"]),

Q("f", VE, "Kafatası içindeki venöz kanın akış yolu hangisinde doğru verilmiştir?",
  "Sinus sagittalis superior → confluens sinuum → sinus transversus → sinus sigmoideus → v. jugularis interna",
  ["Sinus sagittalis inferior → sinus cavernosus → v. jugularis externa", "Sinus transversus → sinus sagittalis superior → v. vertebralis",
   "Sinus cavernosus → sinus rectus → v. jugularis externa", "Sinus sigmoideus → sinus transversus → confluens sinuum → v. jugularis interna"],
  """Dural sinüsler beyin, meninksler ve kafatasından gelen kanı toplar. Sinus sagittalis superior BOS'un emildiği
  granülasyonları da içerir. Sigmoid sinüs foramen jugulare'de v. jugularis interna'ya devam eder.""",
  e=["sinus-durae-matris", "v-jugularis-interna"]),

Q("t", VE, "Sol testiküler venin döküldüğü yer ve bunun klinik önemi hangisidir?",
  "V. renalis sinistra'ya döküldüğü için varikosel daha sık solda görülür.",
  ["V. cava inferior'a döküldüğü için varikosel solda görülmez.", "V. iliaca interna'ya döküldüğü için hemoroide yol açar.",
   "V. portae'ye döküldüğü için portal hipertansiyonda genişler.", "V. azygos'a döküldüğü için göğüs ağrısı yapar."],
  """Sağ testiküler ven doğrudan VCI'ya eğik açıyla, sol testiküler ven sol renal vene dik açıyla açılır. Sol
  renal ven ayrıca aorta ile SMA arasında sıkışabilir (nutcracker). Bu nedenle pampiniform pleksusun
  genişlemesi (varikosel) çoğunlukla soldadır.""",
  e=["testis", "v-cava-inferior"]),

Q("t", VE, "Sol v. renalis için aşağıdakilerden hangisi yanlıştır?",
  "Aortanın arkasından geçerek v. cava inferior'a açılır.",
  ["Sağ renal venden daha uzundur.", "Sol gonadal ve sol suprarenal venleri alır.",
   "A. mesenterica superior ile aorta arasından geçer.", "Aorta ile SMA arasında sıkışması 'nutcracker' sendromuna yol açar."],
  """Sol renal ven normalde aortanın önünden, SMA'nın hemen altından geçer. Retroaortik sol renal ven nadir bir
  varyasyondur. Sol renal venin uzun olması nedeniyle sol böbrek nakil için çoğunlukla tercih edilir.""",
  e=["ren", "aorta", "a-mesenterica-superior"]),

Q("t", VE, "Yüzün 'tehlikeli üçgeni'ndeki enfeksiyonların sinus cavernosus'a yayılmasında başlıca rol oynayan yol hangisidir?",
  "V. facialis → v. angularis → v. ophthalmica superior",
  ["V. retromandibularis → v. jugularis externa", "V. facialis → v. jugularis interna → sinus sigmoideus",
   "V. temporalis superficialis → sinus sagittalis superior", "Plexus pterygoideus → v. maxillaris → v. jugularis externa"],
  """Göz iç köşesinde v. facialis'in başlangıcı olan v. angularis, kapaksız v. ophthalmica superior ile bağlantılıdır.
  Burun ve üst dudak çevresindeki enfeksiyonlar bu yolla sinus cavernosus'a ulaşarak tromboflebite neden olabilir.""",
  e=["sinus-durae-matris", "v-jugularis-interna"]),

Q("f", VE, "V. brachiocephalica sinistra için hangisi doğrudur?",
  "Sağdan daha uzundur ve arcus aortae dallarının önünden eğik olarak geçer.",
  ["Sağdan daha kısadır ve dikey iner.", "Doğrudan sağ atriyuma açılır.", "Aortanın arkasından geçer.", "V. azygos'u alır."],
  """Her iki tarafta v. jugularis interna ile v. subclavia sternoklavikular eklemin arkasında birleşerek
  brakiyosefalik venleri yapar. Sol brakiyosefalik ven manubriumun arkasından sağa geçer ve sağ ile birleşerek
  VCS'yi oluşturur. Ductus thoracicus sol venöz açıya açılır.""",
  e=["v-cava-superior", "v-subclavia", "v-jugularis-interna"]),
]

write("cardiovascular", questions)
