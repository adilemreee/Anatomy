from qcommon import Q, write

EB = "Endokrin bezler"

questions = [
Q("fv", EB, """Baş ağrısı olan hastada görme alanı muayenesinde bitemporal hemianopsi saptanıyor; MR'da sella
turcica'dan yukarı uzanan kitle var. Kitle hangi yapıdan köken alır ve neye bası yapar?""",
  "Hipofiz bezi – chiasma opticum",
  ["Epifiz bezi – colliculus superior", "Tiroid bezi – trakea", "Hipotalamus – tractus opticus", "Sinus sphenoidalis – n. opticus"],
  """Hipofiz sella turcica'da, chiasma opticum'un hemen altındadır. Yukarı büyüyen makroadenomlar kiazmada
  çaprazlaşan nazal retina liflerine bası yapar. Yana büyüyen adenomlar sinus cavernosus'taki kranial sinirleri
  etkileyebilir.""",
  e=["hypophysis", "n-opticus", "os-sphenoidale"]),

Q("t", EB, "Adenohipofizin embriyolojik kökeni hangisidir?",
  "Ağız boşluğu tavanının ektoderminden gelişen Rathke kesesi",
  ["Diensefalonun aşağı uzantısı (infundibulum)", "Üçüncü faringeal kese", "Nöral krista", "Foramen caecum'dan inen endoderm"],
  """Ön hipofiz stomodeum tavanından yukarı büyüyen Rathke kesesinden, arka hipofiz ise diensefalonun tabanından
  aşağı inen infundibulumdan gelişir. Rathke kesesi kalıntılarından kraniyofarenjiyom gelişebilir.""",
  e=["adenohypophysis", "neurohypophysis"]),

Q("f", EB, "Aşağıdaki hormonlardan hangisi arka hipofizden (nörohipofiz) salınır?",
  "Oksitosin",
  ["Prolaktin", "Büyüme hormonu", "ACTH", "TSH"],
  """Arka hipofiz hormon üretmez; hipotalamusun supraoptik ve paraventriküler çekirdeklerinde yapılan ADH ve
  oksitosini aksonlarla taşıyıp depolar ve kana verir. Diğer seçenekler ön hipofiz hormonlarıdır.""",
  e=["neurohypophysis", "hypothalamus"]),

Q("tv", EB, """Doğum sırasında masif kanama geçiren kadın doğum sonrası emziremiyor, adetleri geri gelmiyor ve
yorgunluk, soğuk intoleransı gelişiyor. Bu tablonun anatomik açıklaması nedir?""",
  "Gebelikte büyüyen ön hipofizin portal sisteme bağımlı kanlanmasının hipotansiyonda bozulması (Sheehan sendromu)",
  ["Arka hipofizin doğrudan a. carotis interna'dan beslenmesi", "Hipofiz sapının doğum sırasında kopması",
   "Tiroid bezinin doğum travmasıyla hasar görmesi", "Böbreküstü bezinin doğum sırasında kanaması"],
  """Ön hipofiz kanının büyük kısmını hipofizer portal venlerden alır ve düşük basınçlı bir sistemdir. Gebelikte
  hipertrofiye uğrayan bez ağır hipotansiyonda iskemik nekroza gider; prolaktin, gonadotropin, TSH ve ACTH eksikliği
  gelişir.""",
  e=["adenohypophysis", "hypophysis"]),

Q("t", EB, "Hipofizin yanlarında sinus cavernosus bulunması klinik olarak neden önemlidir?",
  "Yana büyüyen adenomlar III, IV, V1, V2 ve VI ile a. carotis interna'yı etkileyebilir.",
  ["Hipofiz hormonları sinus cavernosus'a salınmaz.", "Sinus cavernosus hipofizin ana arteriyel kaynağıdır.",
   "Hipofiz cerrahisi sinus cavernosus'tan geçilerek yapılır.", "Sinus cavernosus hipofizi optik kiazmadan ayırır."],
  """Kavernöz sinüs içinde ICA ve n. abducens, dış duvarında III, IV, V1 ve V2 bulunur. Hipofiz tümörlerinin yana
  uzanması bu sinirlerin felcine yol açabilir; transsfenoidal cerrahide ICA'nın konumu önemlidir.""",
  e=["hypophysis", "sinus-durae-matris", "a-carotis-interna"]),

Q("f", EB, "Epifiz bezi (corpus pineale) hangi hormonu salgılar ve nerede yer alır?",
  "Melatonin; 3. ventrikülün arka duvarında, colliculus superior'ların üstünde",
  ["Melatonin; sella turcica'da", "Oksitosin; hipotalamusun tabanında", "Serotonin; 4. ventrikülün tabanında", "Kortizol; böbreğin üst kutbunda"],
  """Epifiz diensefalonun (epithalamus) parçasıdır. Retinadan suprakiazmatik çekirdeğe gelen ışık bilgisi sempatik
  yollarla epifize ulaşır; karanlıkta melatonin salınımı artar. Yaşla kalsifiye olan bez grafide orta hat
  göstergesidir.""",
  e=["glandula-pinealis", "mesencephalon"]),

Q("fv", EB, """Boynunun ön orta hattında, hyoidin hemen altında kitlesi olan çocukta kitle dilini dışarı çıkardığında
yukarı hareket ediyor. En olası tanı nedir?""",
  "Tiroglossal kanal kisti",
  ["Brankiyal yarık kisti", "Dermoid kist", "Tiroid adenomu", "Kistik higroma"],
  """Tiroid dilin kökündeki foramen caecum'dan başlayarak tiroglossal kanal boyunca aşağı iner. Kanal kalıntısı
  orta hatta kist oluşturur ve dil ile bağlantılı olduğu için dil çıkarılınca yükselir. Tedavide hyoidin orta
  kısmı da çıkarılır (Sistrunk).""",
  e=["glandula-thyroidea", "lingua", "os-hyoideum"]),

Q("t", EB, "Tiroid bezinin yutkunmayla yukarı hareket etmesinin nedeni nedir?",
  "Bezin pretrakeal fasya ile sarılı olması ve bu fasyanın larinks ile trakeaya bağlı olması",
  ["Bezin hyoide doğrudan tutunması", "Bezin m. sternocleidomastoideus'a yapışık olması",
   "Bezin özofagusun içinde yer alması", "Bezin lig. arteriosum ile bağlantılı olması"],
  """Tiroid, derin servikal fasyanın pretrakeal yaprağıyla sarılıdır ve bu fasya (Berry bağı) bezi krikoid kıkırdak ve
  trakeaya bağlar. Bu nedenle tiroid kökenli kitleler yutkunmayla larinksle birlikte yükselir.""",
  e=["glandula-thyroidea", "trachea"]),

Q("t", EB, "Tiroidektomide n. laryngeus recurrens'in yaralanma riski en fazla hangi damarın bağlanması sırasındadır?",
  "A. thyroidea inferior",
  ["A. thyroidea superior", "V. thyroidea superior", "A. carotis communis", "V. jugularis interna"],
  """Rekürren sinir trakeoözofageal olukta yükselirken bezin arka-alt kısmında a. thyroidea inferior'un dallarıyla
  çaprazlaşır; sinir arterin önünden, arkasından veya dalları arasından geçebilir. Arter bezden uzakta bağlanır,
  sinir görülerek korunur.""",
  e=["glandula-thyroidea", "n-vagus"]),

Q("f", EB, "A. thyroidea superior ve a. thyroidea inferior sırasıyla hangi arterlerden çıkar?",
  "A. carotis externa ve truncus thyrocervicalis",
  ["A. carotis interna ve a. vertebralis", "Truncus thyrocervicalis ve a. carotis externa", "A. subclavia ve a. carotis communis", "Arcus aortae ve a. thoracica interna"],
  """Üst tiroid arteri ECA'nın ilk dalıdır ve bezin üst kutbuna iner; alt tiroid arteri a. subclavia'nın tirocervikal
  gövdesinden çıkar ve bezin arka yüzüne ulaşır. Bazı kişilerde orta hatta a. thyroidea ima bulunur.""",
  e=["glandula-thyroidea", "a-carotis-externa", "a-subclavia"]),

Q("tv", EB, """Total tiroidektomiden 24 saat sonra hastada ağız çevresinde uyuşma, parmaklarda karıncalanma ve
tansiyon manşeti şişirildiğinde el bileğinde spazm (Trousseau belirtisi) gelişiyor. En olası neden nedir?""",
  "Paratiroid bezlerinin çıkarılması veya kanlanmasının bozulmasına bağlı hipokalsemi",
  ["N. laryngeus recurrens yaralanması", "Tiroid fırtınası", "Hipotiroidi", "Boyun hematomu"],
  """Paratiroidler tiroidin arka yüzündedir ve çoğunlukla a. thyroidea inferior'dan beslenir. Cerrahide çıkarılmaları
  veya devaskülarize olmaları PTH eksikliği ve hipokalsemi yapar; Chvostek ve Trousseau belirtileri görülür.""",
  e=["glandulae-parathyroideae", "glandula-thyroidea"]),

Q("t", EB, "Alt paratiroid bezlerinin yerinin üst paratiroidlerden daha değişken olmasının embriyolojik nedeni nedir?",
  "Alt paratiroidler 3. faringeal keseden timusla birlikte gelişir ve onunla birlikte aşağı göç eder.",
  ["Alt paratiroidler 4. faringeal keseden gelişir ve hiç göç etmez.", "Alt paratiroidler nöral kristadan gelişir.",
   "Üst paratiroidler timusla birlikte göç eder.", "Alt paratiroidler tiroid divertikülünden gelişir."],
  """3. kese hem alt paratiroidi hem timusu oluşturur; timus mediastene inerken alt paratiroidi de aşağı taşır ve
  bez bazen mediastende bulunabilir. Üst paratiroidler 4. keseden gelişir ve daha kısa bir göç yaptıkları için
  daha sabit konumdadır.""",
  e=["glandulae-parathyroideae", "thymus"]),

Q("f", EB, "Böbreküstü bezi korteksinin katmanları ve salgıladıkları hormonlar hangisinde doğru verilmiştir?",
  "Zona glomerulosa – aldosteron; zona fasciculata – kortizol; zona reticularis – androjenler",
  ["Zona glomerulosa – kortizol; zona fasciculata – aldosteron; zona reticularis – adrenalin",
   "Zona glomerulosa – androjenler; zona fasciculata – kortizol; zona reticularis – aldosteron",
   "Zona glomerulosa – adrenalin; zona fasciculata – noradrenalin; zona reticularis – kortizol",
   "Tüm katmanlar yalnızca kortizol salgılar."],
  """Dıştan içe 'tuz, şeker, seks' sırası: mineralokortikoid, glukokortikoid, androjen. Medulla nöral krista kökenli
  kromaffin hücrelerden oluşur ve katekolamin salgılar.""",
  e=["glandula-suprarenalis"]),

Q("t", EB, "Böbreküstü bezlerinin venöz drenajı ile ilgili hangisi doğrudur?",
  "Sağ suprarenal ven doğrudan VCI'ya, sol suprarenal ven sol renal vene açılır.",
  ["Her iki ven de doğrudan VCI'ya açılır.", "Her iki ven de portal vene açılır.",
   "Sol ven doğrudan VCI'ya, sağ ven sağ renal vene açılır.", "Böbreküstü bezlerinin veni yoktur, lenfatiklerle drene olur."],
  """Böbreküstü bezleri üç arterden beslenir (inferior frenik, aorta ve renal arter dalları) ancak tek bir ana venle
  drene olur. Sağ ven çok kısadır ve doğrudan VCI'ya açılır; sağ adrenalektomide kanama riski bu nedenle yüksektir.""",
  e=["glandula-suprarenalis", "v-cava-inferior"]),

Q("f", EB, "Böbreküstü bezinin arterleri hangilerinden çıkar?",
  "A. phrenica inferior, abdominal aorta ve a. renalis",
  ["Truncus coeliacus, a. splenica ve a. gastrica sinistra", "A. mesenterica superior ve inferior", "Aa. lumbales ve a. iliaca communis", "A. testicularis/ovarica ve a. renalis"],
  """Üst suprarenal arterler a. phrenica inferior'dan, orta suprarenal arter doğrudan aortadan, alt suprarenal arter
  a. renalis'ten çıkar. Bez organın büyüklüğüne göre çok zengin kanlanmaya sahiptir.""",
  e=["glandula-suprarenalis", "aorta", "aa-renales"]),

Q("tv", EB, """Atak tarzında baş ağrısı, terleme, çarpıntı ve yüksek tansiyonu olan genç hastada idrarda metanefrin
yüksek. Tümörün en sık köken aldığı hücreler ve bunların embriyolojik kökeni hangisidir?""",
  "Adrenal medulladaki kromaffin hücreler – nöral krista",
  ["Zona glomerulosa hücreleri – mezoderm", "Zona fasciculata hücreleri – endoderm", "Tiroidin C hücreleri – endoderm",
   "Pankreasın beta hücreleri – endoderm"],
  """Feokromositoma katekolamin salgılayan kromaffin hücre tümörüdür ve çoğunlukla adrenal medullada gelişir.
  Medulla nöral krista kökenlidir ve modifiye sempatik postganglioner nöronlardan oluşur.""",
  e=["glandula-suprarenalis", "systema-autonomicum"]),

Q("f", EB, "Langerhans adacıkları pankreasın en çok hangi bölümünde yoğunlaşır?",
  "Kuyruk",
  ["Baş", "Processus uncinatus", "Boyun", "Ana kanal çevresi"],
  """Adacıklar pankreasın tamamına dağılmış olsa da en yoğun olarak kuyrukta bulunur. Distal pankreatektomi sonrası
  diyabet riski bu nedenle önemlidir.""",
  e=["insulae-pancreaticae", "pancreas"]),

Q("t", EB, "Tiroidin kalsitonin salgılayan parafoliküler (C) hücreleri embriyolojik olarak nereden gelir?",
  "Ultimobrankiyal cisim (4.–5. faringeal kese) aracılığıyla nöral krista",
  ["Foramen caecum endodermi", "Rathke kesesi", "3. faringeal kese", "Mezonefroz"],
  """Tiroid foliküler hücreleri tiroglossal kanal endoderminden, C hücreleri ise ultimobrankiyal cisme göç eden nöral
  krista hücrelerinden gelişir. Medüller tiroid karsinomu C hücrelerinden köken alır ve kalsitonin salgılar.""",
  e=["glandula-thyroidea"]),

Q("t", EB, "Hipofiz sapının kesilmesi (örneğin travma) sonrasında hangi hormonun kan düzeyi artar?",
  "Prolaktin",
  ["Büyüme hormonu", "ACTH", "LH", "ADH"],
  """Prolaktin salınımı hipotalamik dopamin ile tonik olarak baskılanır. Sap kesildiğinde dopamin ön hipofize
  ulaşamaz ve prolaktin artar; diğer ön hipofiz hormonları ise uyarıcı hipotalamik hormonların yokluğunda azalır.
  ADH salınımı da bozulur (diabetes insipidus).""",
  e=["adenohypophysis", "hypothalamus"]),
]

write("endocrine", questions)
