from qcommon import Q, write

BK = "Böbrekler"
IY = "İdrar yolları"

questions = [
Q("f", BK, "Böbreklerin omurgaya göre konumu ile ilgili hangisi doğrudur?",
  "T12–L3 arasında yer alırlar; sağ böbrek karaciğer nedeniyle soldan biraz aşağıdadır.",
  ["T6–T10 arasında yer alırlar.", "Sol böbrek sağdan daha aşağıdadır.", "L4–S1 arasında, pelvis içindedir.", "Her iki böbrek de intraperitonealdir."],
  """Böbrekler retroperitoneal organlardır; sol böbrek yaklaşık T11–L2, sağ böbrek T12–L3 düzeyindedir. Derin
  inspirasyonda diyaframla birlikte 2–3 cm aşağı inerler.""",
  e=["ren"]),

Q("f", BK, "Böbrek hilusunda önden arkaya yapıların sıralaması hangisidir?",
  "V. renalis – a. renalis – pelvis renalis",
  ["A. renalis – v. renalis – pelvis renalis", "Pelvis renalis – a. renalis – v. renalis",
   "V. renalis – pelvis renalis – a. renalis", "A. renalis – pelvis renalis – v. renalis"],
  """Hilusta önde ven, ortada arter, arkada pelvis bulunur ('VAP'). Bu düzen nefrektomide damarların öne,
  toplayıcı sistemin arkaya yerleşimini hatırlatır.""",
  e=["ren", "pelvis-renalis", "aa-renales"]),

Q("t", BK, "Böbreğin arka yüzüyle komşu olmayan yapı hangisidir?",
  "Colon descendens",
  ["Diyafram", "M. quadratus lumborum", "M. psoas major", "N. subcostalis"],
  """Böbreklerin arka yüzü diyafram, 12. kaburga, psoas major, quadratus lumborum ve transversus abdominis ile;
  subkostal, iliohipogastrik ve ilioinguinal sinirlerle komşudur. Kolonlar böbreklerin ön-dış yüzüyle komşudur.
  Arka cerrahi girişimde 12. kaburga üstüne çıkılırsa plevra yaralanabilir.""",
  e=["ren", "diaphragma", "m-quadratus-lumborum"]),

Q("t", BK, "Renal fasya (Gerota) ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Böbrek ve böbreküstü bezini sarar; ancak böbreküstü bezi ayrı bir bölmededir.",
  ["Yalnızca böbreği sarar, böbreküstü bezi dışarıda kalır.", "Aşağı uçta tamamen kapalıdır.",
   "Böbreğe sıkıca yapışık olan iç kapsüldür.", "Periton ile aynı yapıdır."],
  """Böbreği içten dışa fibröz kapsül, perirenal yağ ve renal fasya sarar. Fasya aşağıda üreter boyunca açık kalır;
  bu nedenle nefroptozda böbrek aşağı kayabilir ama ayrı bölmedeki böbreküstü bezi yerinde kalır.""",
  e=["fascia-renalis", "glandula-suprarenalis"]),

Q("t", BK, "Bir segmental renal arterin tıkanması neden kama biçimli enfarkta yol açar?",
  "Segmental arterler aralarında anastomoz yapmayan uç arterlerdir.",
  ["Segmental arterlerin venleri olmadığı için.", "Renal korteks yalnızca venöz kanla beslendiği için.",
   "Segmental arterler birbirleriyle geniş anastomoz yaptığı için.", "Böbreğin lenfatik drenajı olmadığı için."],
  """A. renalis hilusta genellikle beş segmental artere (apikal, üst, orta, alt, posterior) ayrılır ve bunlar uç
  arterlerdir. Renal venler ise segmentler arasında serbestçe anastomoz yapar; bu nedenle segmental ven bağlanması
  enfarkt yapmaz.""",
  e=["nephronum", "aa-renales"]),

Q("tv", BK, """Turner sendromlu kız çocuğunda ultrasonda iki böbreğin alt kutuplarının orta hatta birleştiği
görülüyor. Bu böbreğin normal yerine yükselmesini engelleyen yapı hangisidir?""",
  "A. mesenterica inferior",
  ["A. mesenterica superior", "Truncus coeliacus", "A. iliaca communis", "Lig. inguinale"],
  """At nalı böbrekte birleşen alt kutuplar yükselirken IMA'nın çıkış yerine takılır ve böbrek normalden aşağıda
  kalır. Üreterler istmusun önünden geçtiği için drenaj sorunları ve taş oluşumu sıktır.""",
  e=["ren", "a-mesenterica-inferior"]),

Q("t", BK, "Böbreğin toplayıcı sistemi (üreter, pelvis, kaliksler, toplayıcı kanallar) embriyolojik olarak neyden gelişir?",
  "Üreter tomurcuğundan (mezonefrik kanal çıkıntısı)",
  ["Metanefrik blastemden", "Paramezonefrik kanaldan", "Ürogenital sinüsten", "Pronefrozdan"],
  """Metanefroz iki kaynaktan gelişir: üreter tomurcuğu toplayıcı sistemi, metanefrik blastem ise nefronu (Bowman
  kapsülünden distal tübüle kadar) oluşturur. İki dokunun karşılıklı indüksiyonu bozulursa renal agenezi veya
  multikistik displazi gelişebilir.""",
  e=["nephronum", "pelvis-renalis", "ureter"]),

Q("t", BK, "Jukstaglomerüler aparat ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Renin efferent arteriyoldeki macula densa hücrelerinden salgılanır.",
  ["Renin afferent arteriyolün duvarındaki jukstaglomerüler hücrelerden salgılanır.",
   "Macula densa distal tübülün glomerüle komşu duvarındadır.",
   "Ekstraglomerüler mezangiyal hücreler aparatın parçasıdır.",
   "Macula densa tübül içindeki NaCl yükünü algılar."],
  """Jukstaglomerüler hücreler afferent arteriyolün modifiye düz kas hücreleridir ve renin salgılar. Macula densa
  distal tübülün özelleşmiş epitelidir ve renin salınımını ile glomerüler filtrasyonu (tübüloglomerüler geri bildirim)
  düzenler.""",
  e=["nephronum"]),

Q("t", BK, "Canlı vericiden böbrek naklinde genellikle sol böbreğin tercih edilmesinin nedeni nedir?",
  "Sol renal venin daha uzun olması",
  ["Sol böbreğin daha büyük olması", "Sol renal arterin daha uzun olması", "Sol böbreğin intraperitoneal olması", "Sol üreterin daha kısa olması"],
  """Sol renal ven aortanın önünden geçerek VCI'ya ulaştığı için daha uzundur; bu da alıcıda damar
  anastomozunu kolaylaştırır. Sağ renal arter ise daha uzundur ve VCI'nın arkasından geçer.""",
  e=["ren", "aa-renales"]),

Q("fv", BK, """Antenatal ultrasonda tek taraflı hidronefroz saptanan bebekte üreter normal çapta, renal pelvis ve
kaliksler belirgin genişlemiş. Tıkanıklık en olası nerededir?""",
  "Üreteropelvik bileşke",
  ["Üreterovezikal bileşke", "Posterior üretral valv", "Pelvis girişinde iliak damarların çaprazladığı yer", "Mesane boynu"],
  """Üreter normal, pelvis genişse tıkanıklık pelvis ile üreterin birleşim yerindedir. Üreteropelvik bileşke darlığı
  çocuklarda hidronefrozun en sık nedenidir; posterior üretral valv ise erkeklerde iki taraflı hidronefroz ve
  mesane duvarı kalınlaşması yapar.""",
  e=["pelvis-renalis", "ureter"]),

Q("fv", IY, """Yan ağrısı kasığa ve skrotuma yayılan, kıvrandıran ağrısı olan hastada hematüri var. Taşın en sık
takıldığı ve üreterin en dar olduğu yer neresidir?""",
  "Üreterovezikal bileşke",
  ["Üreteropelvik bileşke", "Pelvis girişinde iliak damarların çaprazlandığı yer", "Böbrek kaliksleri", "Üretranın prostatik bölümü"],
  """Üreterin üç fizyolojik darlığı üreteropelvik bileşke, pelvis girişi ve üreterovezikal bileşkedir; en dar olanı
  mesane duvarını eğik olarak geçtiği üreterovezikal bileşkedir. Ağrının bele, kasığa ve skrotuma/labiuma yayılması
  T11–L2 segmentlerinin (genitofemoral ve ilioinguinal alanları) tutulmasıyla açıklanır.""",
  e=["ureter", "vesica-urinaria"]),

Q("f", IY, "Erkekte pelviste üreteri yukarıdan (önden) çaprazlayan yapı hangisidir?",
  "Ductus deferens",
  ["A. iliaca interna", "N. obturatorius", "A. uterina", "M. psoas major"],
  """Erkekte ductus deferens mesanenin arka-yan duvarına ilerlerken üreterin üstünden geçer. Kadında karşılık gelen
  ilişki a. uterina ile üreter arasındadır ('köprünün altından akan su').""",
  e=["ureter", "ductus-deferens"]),

Q("t", IY, "Üreterin kanlanması ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Karın kısmı damarlarını medialden (aortik dallar), pelvis kısmı lateralden (iliak dallar) alır.",
  ["Tüm uzunluğu boyunca yalnızca a. renalis'ten beslenir.", "Pelvis kısmı aortadan doğrudan dal alır.",
   "Üreterin kendine ait arteri yoktur.", "Kanlanma yalnızca a. mesenterica inferior'dandır."],
  """Üreter renal, gonadal, aortik, ortak iliak, iç iliak ve vezikal arterlerden segmental dallar alır; bunlar duvar
  içinde uzunlamasına anastomoz yapar. Cerrahide üreterin karın kısmı içten, pelvis kısmı dıştan
  diseke edilirse kanlanması korunur.""",
  e=["ureter"]),

Q("f", IY, "Mesanenin trigonum vesicae bölgesi ile ilgili aşağıdakilerden hangisi doğrudur?",
  "İki üreter ağzı ve iç üretra ağzı arasındaki düz mukozalı üçgendir.",
  ["Mesanenin tepesindeki (apex) kıvrımlı bölgedir.", "Kas tabakası içermez.",
   "Endodermal ürogenital sinüsten gelişir ve en kıvrımlı bölgedir.", "Prostatın içinde yer alır."],
  """Trigonun mukozası, mesanenin geri kalanının aksine mesane dolu veya boşken düz kalır; mezonefrik kanalların
  mesane duvarına katılmasıyla gelişir. Mesane tümörleri ve enfeksiyonları sıklıkla bu bölgeyi tutar.""",
  e=["vesica-urinaria"]),

Q("t", IY, "İşeme (miksiyon) sırasında detrusor kasını kasan lifler hangileridir?",
  "Pelvik splanknik sinirlerle gelen parasempatik lifler (S2–S4)",
  ["T11–L2 kökenli sempatik lifler", "N. pudendus'un somatik motor lifleri", "N. genitofemoralis lifleri", "N. obturatorius lifleri"],
  """Parasempatik uyarı detrusoru kasar ve iç sfinkteri gevşetir. Sempatik lifler (hipogastrik sinirler) dolum
  döneminde detrusoru gevşetir ve mesane boynunu kasar; n. pudendus istemli dış sfinkteri kontrol eder.""",
  e=["vesica-urinaria", "systema-autonomicum", "n-pudendus"]),

Q("tv", IY, """Trafik kazasında karnı dolu mesaneyle emniyet kemerine çarpan hastada karın ağrısı, hematüri ve
batında yaygın hassasiyet var; sistografide kontrast madde bağırsak halkalarının arasına yayılıyor.
Yırtılan bölge neresidir?""",
  "Mesane kubbesi (intraperitoneal rüptür)",
  ["Mesane boynu (ekstraperitoneal rüptür)", "Prostatik üretra", "Trigonum vesicae", "Membranöz üretra"],
  """Dolu mesane karın boşluğuna yükselir ve tepesi peritonla örtülüdür. Künt travmada kubbe yırtılır, idrar periton
  boşluğuna dolar (cerrahi onarım gerekir). Pelvis kırıklarına eşlik eden yırtıklar ise çoğunlukla ekstraperitoneal
  olup idrar prevezikal (Retzius) aralığa yayılır.""",
  e=["vesica-urinaria", "peritoneum"]),

Q("t", IY, "Göbekten idrar gelmesine yol açabilen ve mesanenin tepesini göbeğe bağlayan fetal yapının erişkindeki kalıntısı hangisidir?",
  "Lig. umbilicale medianum (urachus)",
  ["Lig. umbilicale mediale (a. umbilicalis)", "Lig. teres hepatis", "Lig. venosum", "Lig. arcuatum medianum"],
  """Urachus, allantois kanalının kalıntısıdır ve mesane tepesinden göbeğe uzanır. Tam açık kalırsa göbekten idrar
  gelir; kısmi açıklıklar urakal kist veya sinüs oluşturur. Lig. umbilicale mediale ise a. umbilicalis'in
  tıkanmış kısmıdır.""",
  e=["vesica-urinaria"]),

Q("f", IY, "Erkek üretrasının en dar ve en az genişleyebilen bölümü hangisidir?",
  "Pars membranacea",
  ["Pars prostatica", "Pars spongiosa", "Fossa navicularis", "Pars intramuralis"],
  """Membranöz üretra perine zarının içinden geçer ve dış üretral sfinkterle sarılıdır. Kateterizasyonda direnç ve
  yaralanma en sık burada olur. En geniş bölüm prostatik, en uzun bölüm spongiyöz üretradır.""",
  e=["urethra-masculina", "urethra"]),

Q("tv", IY, """Bisiklet sürerken ata biner şekilde demir çubuğun üzerine düşen erkekte perinede, skrotumda ve
penis çevresinde morluk ve şişlik gelişiyor; şişlik karın ön duvarına uzanıyor ancak uyluklara geçmiyor.
Yırtılan yapı ve yayılımı sınırlayan fasya hangisidir?""",
  "Spongiyöz (bulbar) üretra – Colles fasyasının fascia lata'ya yapışması",
  ["Membranöz üretra – fascia transversalis", "Prostatik üretra – Denonvilliers fasyası",
   "Mesane boynu – fascia endopelvina", "Spongiyöz üretra – Scarpa fasyasının inguinal bağa yapışmaması"],
  """Bulbar üretra perine zarının altında, yüzeyel perine boşluğundadır. Yırtıldığında idrar ve kan Colles fasyasının
  altında skrotum, penis ve Scarpa fasyası altından karın ön duvarına yayılır. Colles/Scarpa fasyası fascia lata'ya
  yapıştığı için uyluğa geçemez.""",
  e=["urethra-masculina", "perineum"]),

Q("f", IY, "Kadınlarda idrar yolu enfeksiyonlarının daha sık görülmesinin anatomik nedeni nedir?",
  "Üretranın kısa (yaklaşık 4 cm) olması ve dış ağzının vajen ve anüse yakın olması",
  ["Üreterlerin daha uzun olması", "Mesanenin daha büyük olması", "Üretranın prostatla çevrili olması", "Trigonun bulunmaması"],
  """Kadın üretrası kısa ve düzdür; dış ağzı vestibülde klitorisin altında, vajen girişinin önündedir. Perine
  florası bakterilerinin mesaneye ulaşması kolaylaşır.""",
  e=["urethra"]),
]

write("urinary", questions)
