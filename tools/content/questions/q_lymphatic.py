from qcommon import Q, write

LO = "Lenfoid organlar"
LD = "Lenf düğümleri ve damarları"

questions = [
Q("fv", LO, """Trafik kazasında sol alt kaburgaları kırılan hastada hipotansiyon ve sol omuz ağrısı gelişiyor.
Yaralanan organ ve yeri için hangisi doğrudur?""",
  "Dalak; sol 9–11. kaburgaların arkasında, uzun ekseni 10. kaburga boyunca",
  ["Karaciğer; sağ 7–9. kaburgaların arkasında", "Sol böbrek; T6–T8 düzeyinde", "Pankreas başı; sol 12. kaburganın altında",
   "Mide; sol 2–4. kaburgaların arkasında"],
  """Dalak karın içinde en sık yaralanan organdır. Kan diyafram altını tahriş ederek frenik sinir yoluyla sol omuza
  yansıyan ağrıya (Kehr belirtisi) yol açar. Normal dalak kaburga kavsinin altında ele gelmez.""",
  e=["splen", "costae"]),

Q("t", LO, "Dalağın bağlarıyla ilgili hangisi doğrudur?",
  "Lig. splenorenale splenik damarları ve pankreas kuyruğunu içerir.",
  ["Lig. gastrosplenicum a. splenica'nın ana gövdesini içerir.", "Lig. phrenicocolicum dalağı mideye bağlar.",
   "Dalağın hiç bağı yoktur, retroperitonealdir.", "Lig. splenorenale kısa gastrik arterleri içerir."],
  """Dalak intraperitonealdir. Lig. gastrosplenicum kısa gastrik damarları ve sol gastroomental damarları, lig.
  splenorenale splenik arter ve veni ile pankreas kuyruğunu içerir. Lig. phrenicocolicum dalağın alt kutbunu destekler.""",
  e=["splen", "pancreas"]),

Q("t", LO, "Splenektomi sonrası hastaların hangi enfeksiyonlara karşı aşılanması gerekir ve neden?",
  "Kapsüllü bakterilere (pnömokok, meningokok, H. influenzae); dalak opsonize olmamış kapsüllü bakterileri temizler.",
  ["Virüslere; dalak interferon üretir.", "Mantarlara; dalak kandida temizler.", "Parazitlere; dalak eozinofil üretir.", "Hiçbirine; karaciğer görevini tamamen üstlenir."],
  """Dalak kırmızı pulpası yaşlı eritrositleri ve kapsüllü bakterileri temizler, beyaz pulpası IgM yanıtını başlatır.
  Splenektomi sonrası ağır sepsis (OPSI) riski nedeniyle aşılama önerilir.""",
  e=["splen"]),

Q("f", LO, "T lenfositlerin olgunlaştığı primer lenfoid organ hangisidir ve nereden gelişir?",
  "Timus; 3. faringeal kese",
  ["Dalak; dorsal mezogastrium", "Tonsilla palatina; 2. faringeal kese", "Kemik iliği; sklerotom", "Lenf düğümleri; ara mezoderm"],
  """Timus ön-üst mediastende yer alır; çocuklukta büyüktür, ergenlikten sonra yağ dokusuna dönüşür. Epitel
  hücreleri 3. faringeal keseden, lenfositleri kemik iliğinden gelir. Primer lenfoid organlar kemik iliği ve
  timustur.""",
  e=["thymus"]),

Q("tv", LO, """Tonsillektomi sonrası hastada aynı tarafta dilin arka kısmında tat kaybı ve kulağa yayılan ağrı var.
Tonsil yatağında yaralanan sinir hangisidir?""",
  "N. glossopharyngeus",
  ["N. lingualis", "N. hypoglossus", "N. facialis", "N. vagus'un rekürren dalı"],
  """Tonsil yatağının tabanını m. constrictor pharyngis superior oluşturur ve bu kasın dışında n. glossopharyngeus
  seyreder. Hasarında dilin arka 1/3'ünde tat ve duyu kaybı olur; kulak ağrısı IX'un timpanik dalı yoluyla yansır.""",
  e=["tonsillae", "n-glossopharyngeus"]),

Q("f", LO, "Tonsilla palatina nerede bulunur?",
  "Arcus palatoglossus ile arcus palatopharyngeus arasındaki fossa tonsillaris'te",
  ["Nazofarinksin arka duvarında", "Dil kökünde", "Tuba auditiva'nın ağzında", "Piriform girintide"],
  """Damak bademciği orofarinksin yan duvarında iki damak kemeri arasında yer alır. Nazofarinksteki adenoid (tonsilla
  pharyngea), dil kökündeki tonsilla lingualis ve tuba ağzındaki tonsilla tubaria ile birlikte Waldeyer halkasını
  oluşturur.""",
  e=["tonsillae", "pharynx"]),

Q("fv", LO, """Çocukta horlama, ağızdan solunum, 'adenoid yüz' görünümü ve tekrarlayan orta kulak iltihabı var. Bu
belirtilerden sorumlu lenfoid doku hangisidir?""",
  "Tonsilla pharyngea (adenoid)",
  ["Tonsilla palatina", "Tonsilla lingualis", "Tonsilla tubaria", "Jugulodigastrik lenf düğümü"],
  """Nazofarinks tavanı ve arka duvarındaki adenoid çocuklukta büyür ve koanaları tıkayarak ağızdan solunuma yol
  açar. Tuba auditiva ağzına yakın olduğu için seröz otit ve tekrarlayan otitlere zemin hazırlar.""",
  e=["tonsillae", "tuba-auditiva"]),

Q("t", LO, "Kırmızı kemik iliği erişkinde en çok nerede bulunur?",
  "Aksiyal iskelette (vertebralar, sternum, kaburgalar, pelvis) ve uzun kemiklerin proksimal uçlarında",
  ["Yalnızca uzun kemiklerin diyafizlerinde", "El ve ayak kemiklerinde", "Kafatasının yalnızca yüz kemiklerinde", "Erişkinde kırmızı kemik iliği bulunmaz"],
  """Doğumda tüm kemiklerde kırmızı ilik bulunur; yaşla uzun kemiklerin diyafizleri sarı (yağlı) iliğe dönüşür.
  Kemik iliği aspirasyonu ve biyopsisi çoğunlukla arka iliak kristadan yapılır.""",
  e=["medulla-ossium"]),

# ------------------------------------------------------------------ Lenf düğümleri ve damarları
Q("f", LD, "Ductus thoracicus nereye açılır?",
  "Sol v. jugularis interna ile sol v. subclavia'nın birleşim yerine (sol venöz açı)",
  ["Sağ venöz açıya", "V. azygos'a", "V. cava inferior'a", "Sol atriyuma"],
  """Ductus thoracicus vücudun alt yarısının ve sol üst çeyreğinin lenfini toplar ve sol venöz açıya açılır. Sağ üst
  çeyreğin lenfi sağ lenf kanalıyla sağ venöz açıya boşalır.""",
  e=["ductus-thoracicus", "v-subclavia", "v-jugularis-interna"]),

Q("t", LD, "Ductus thoracicus'un seyri ile ilgili hangisi yanlıştır?",
  "Diyaframı özofagus hiatusundan geçer.",
  ["L1–L2 düzeyinde cisterna chyli'den başlar.", "Arka mediastende aorta ile v. azygos arasında yükselir.",
   "T4–T5 düzeyinde omurganın önünden sola geçer.", "Boyunda a. carotis communis'in arkasından dolanır."],
  """Ductus thoracicus diyaframı aort hiatusundan (T12) geçer. Toraksta önce sağda yükselir, angulus sterni düzeyinde
  sola geçer ve boyunda sol venöz açıya açılır. Sol taraf boyun cerrahisinde yaralanması şilöz kaçağa yol açar.""",
  e=["ductus-thoracicus", "mediastinum"]),

Q("t", LD, "Sağ lenf kanalı (ductus lymphaticus dexter) vücudun hangi bölümünün lenfini toplar?",
  "Baş-boynun sağ yarısı, sağ üst ekstremite ve göğsün sağ yarısı",
  ["Vücudun tüm sağ yarısı", "Yalnızca sağ akciğer", "Karın ve pelvis organları", "Sağ alt ekstremite"],
  """Sağ lenf kanalı sağ juguler, subklavyen ve bronkomediastinal gövdelerin birleşmesiyle oluşur ve sağ venöz açıya
  açılır. Vücudun geri kalan yaklaşık 3/4'ü ductus thoracicus ile drene olur.""",
  e=["ductus-lymphaticus-dexter", "ductus-thoracicus"]),

Q("fv", LD, """Kilo kaybı ve epigastrik ağrısı olan yaşlı hastada sol klavikula üstünde sert, ağrısız lenf düğümü
ele geliyor. Bu bulgu en çok hangi kanseri düşündürür ve neden solda olur?""",
  "Mide kanseri; karın lenfi ductus thoracicus ile sol venöz açıya taşınır.",
  ["Akciğer kanseri; sol akciğer daha büyüktür.", "Meme kanseri; meme lenfi sol tarafa toplanır.",
   "Tiroid kanseri; tiroidin sol lobu daha büyüktür.", "Lenfoma; yalnızca sol tarafta görülür."],
  """Virchow düğümü (Troisier belirtisi) sol supraklaviküler fossadaki düğümdür. Ductus thoracicus'un sonlanma
  yerine yakın olduğundan karın içi kanserlerin, özellikle mide kanserinin uzak metastazında büyür.""",
  e=["nodi-supraclaviculares", "gaster", "ductus-thoracicus"]),

Q("t", LD, "Tonsillerin ve dil kökünün asıl bölgesel lenf düğümü hangisidir?",
  "Nodus jugulodigastricus",
  ["Nodus juguloomohyoideus", "Nodi submentales", "Nodi occipitales", "Nodi supraclaviculares"],
  """Jugulodigastrik düğüm digastrik kasın arka karnının v. jugularis interna'yı çaprazladığı yerdedir. Tonsillitte en
  sık büyüyen düğümdür; erişkinde kalıcı büyümesi orofarinks kanserini düşündürmelidir.""",
  e=["nodus-jugulodigastricus", "tonsillae"]),

Q("f", LD, "Alt dudağın orta kısmı, ağız tabanının ön kısmı ve dil ucunun lenfi ilk olarak hangi düğümlere gider?",
  "Nodi submentales",
  ["Nodi parotidei", "Nodi occipitales", "Nodi mastoidei", "Nodi supraclaviculares"],
  """Submental düğümler hyoid üstünde, iki digastrik ön karın arasındaki üçgendedir. Alt dudak kanserlerinde ilk
  incelenen düğümlerdir; üst dudak ve yanaklar ise submandibular düğümlere drene olur.""",
  e=["nodi-cervicales"]),

Q("t", LD, "Aksiller lenf düğümleri cerrahide m. pectoralis minor'a göre üç düzeye ayrılır. Düzey III düğümler nerededir?",
  "Pectoralis minor'un medialinde-üstünde (apikal düğümler)",
  ["Pectoralis minor'un lateralinde-altında", "Pectoralis minor'un hemen arkasında", "Pectoralis major ile minor arasında", "Sternum kenarında"],
  """Düzey I: pectoralis minor'un lateralinde; düzey II: arkasında (santral düğümler ve interpektoral Rotter
  düğümleri); düzey III: medialinde (apikal/infraklaviküler). Meme kanseri genellikle düzeyler sırasıyla yayılır.""",
  e=["nodi-axillares", "m-pectoralis-minor", "glandula-mammaria"]),

Q("t", LD, "Aşağıdaki bölgelerden hangisi yüzeyel inguinal lenf düğümlerine drene olmaz?",
  "Testis",
  ["Skrotum derisi", "Anal kanalın pektinat çizgi altındaki kısmı", "Göbek altındaki karın ön duvarı derisi", "Ayak başparmağı derisi"],
  """Yüzeyel inguinal düğümler alt ekstremitenin yüzeyel dokularını, göbek altındaki gövde duvarını, perineyi ve dış
  genital organları drene eder. Testis, gelişimsel kökeni nedeniyle lomber (paraaortik) düğümlere drene olur.""",
  e=["nodi-inguinales", "testis", "nodi-lumbales"]),

Q("fv", LD, """Topuğunda enfekte yara olan hastada diz arkasında ağrılı, şiş lenf düğümü saptanıyor. Bu düğüm
grubunun drenaj alanı için hangisi doğrudur?""",
  "V. saphena parva boyunca gelen topuk, ayak dış kenarı ve baldırın yüzeyel lenfini alır.",
  ["Uyluğun ön yüzünün lenfini alır.", "Perinenin lenfini alır.", "Ayak iç kenarının ve v. saphena magna boyunca gelen lenfin tamamını alır.",
   "Diz ekleminin iç yapılarını drene etmez."],
  """Popliteal düğümler popliteal yağ dokusunda, küçük safen venin sonlanma yerinin yakınındadır. Ayak iç kenarı ve
  bacağın büyük kısmının yüzeyel lenfi ise büyük safen ven boyunca doğrudan yüzeyel inguinal düğümlere gider.""",
  e=["nodi-poplitei", "v-saphena-parva"]),

Q("t", LD, "Mezenterik lenf düğümlerine gelen bağırsak lenfinin süt beyazı görünümde (şilus) olmasının nedeni nedir?",
  "Emilen yağların kilomikronlar hâlinde laktealler aracılığıyla lenfe geçmesi",
  ["Lenfositlerin çok sayıda olması", "Safranın lenfe karışması", "Bağırsak bakterilerinin lenfe geçmesi", "Proteinlerin pıhtılaşması"],
  """İnce bağırsak villuslarındaki lakteal kapillerler uzun zincirli yağ asitlerinden oluşan kilomikronları alır. Lenf
  mezenterik düğümlerden geçerek cisterna chyli ve ductus thoracicus ile venöz dolaşıma ulaşır.""",
  e=["nodi-mesenterici", "intestinum-tenue", "ductus-thoracicus"]),

Q("t", LD, "Cisterna chyli nerede bulunur ve hangi gövdeler buraya açılır?",
  "L1–L2 düzeyinde aortanın sağ-arkasında; lomber gövdeler ve truncus intestinalis",
  ["T4 düzeyinde trakeanın önünde; bronkomediastinal gövdeler", "C7 düzeyinde sol venöz açıda; juguler gövde",
   "S1 düzeyinde rektumun arkasında; iliak gövdeler", "T10 düzeyinde özofagusun önünde; subklavyen gövdeler"],
  """Cisterna chyli ductus thoracicus'un başlangıcındaki keseciktir ve diyaframın sağ krusunun arkasında yer alır.
  Alt ekstremite, pelvis ve karın organlarının lenfi bu gövdelerle buraya ulaşır.""",
  e=["ductus-lymphaticus-dexter", "ductus-thoracicus", "nodi-lumbales"]),

Q("t", LD, "Mide kanseri cerrahisinde çıkarılan perigastrik ve çölyak lenf düğümleri ile ilgili hangisi doğrudur?",
  "Midenin küçük kurvaturu sol ve sağ gastrik, büyük kurvaturu gastroomental düğümlere drene olur; hepsi sonunda çölyak düğümlere ulaşır.",
  ["Mide lenfi doğrudan inguinal düğümlere gider.", "Mide lenfi yalnızca mezenterik düğümlere gider.",
   "Midenin lenfatiği yoktur.", "Büyük kurvatur lenfi doğrudan supraklaviküler düğümlere gider."],
  """Mide lenfi arterleri izleyerek perigastrik düğümlere, oradan çölyak düğümlere ve truncus intestinalis aracılığıyla
  cisterna chyli'ye gider. Cerrahide lenfadenektomi bu istasyonlara göre (D1, D2) tanımlanır.""",
  e=["nodi-coeliaci", "gaster"]),

Q("t", LD, "Serviks kanserinin ilk lenfatik metastaz istasyonu genellikle hangi düğümlerdir?",
  "Obturator ve iç-dış iliak (pelvik) lenf düğümleri",
  ["Paraaortik lenf düğümleri", "Yüzeyel inguinal lenf düğümleri", "Mezenterik lenf düğümleri", "Supraklaviküler lenf düğümleri"],
  """Serviks lenfatikleri parametrium boyunca lateral pelvis duvarına ilerler; obturator, iç ve dış iliak düğümler ilk
  istasyonlardır. Ardından ortak iliak ve paraaortik düğümler tutulur.""",
  e=["nodi-iliaci", "cervix-uteri"]),
]

write("lymphatic", questions)
