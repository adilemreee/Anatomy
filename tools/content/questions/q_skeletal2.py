"""More skeletal questions: foramina, landmarks, fractures and attachments."""
from qcommon import Q

KAF = "Kafatası (Cranium)"
OMR = "Omurga (Columna vertebralis)"
GKF = "Göğüs kafesi (Thorax)"
UST = "Üst ekstremite kemikleri"
ELK = "El kemikleri"
ALT = "Alt ekstremite kemikleri"
AYK = "Ayak kemikleri"

questions = [
# ------------------------------------------------------------------ kafatası delikleri
Q("f", KAF, "Foramen ovale'den geçen sinir hangisidir?",
  "N. mandibularis (V3)",
  ["N. maxillaris (V2)", "N. ophthalmicus (V1)", "N. facialis", "N. hypoglossus"],
  """Os sphenoidale'nin büyük kanadındaki foramen ovale'den n. mandibularis, a. meningea accessoria ve
  n. petrosus minor geçer. Akılda tutma: ‘Superior Rotundum Ovale’ – V1 fissura orbitalis superior'dan,
  V2 foramen rotundum'dan, V3 foramen ovale'den çıkar.""",
  ["Foramen rotundum'dan geçer.", "Fissura orbitalis superior'dan geçer.", "Meatus acusticus internus'tan girer.",
   "Canalis hypoglossi'den geçer."],
  e=["os-sphenoidale"]),

Q("t", KAF, "Foramen spinosum'dan geçen yapı hangisidir?",
  "A. meningea media",
  ["A. carotis interna", "V. jugularis interna", "N. petrosus major", "N. maxillaris"],
  """Foramen spinosum foramen ovale'nin arka-dışında, büyük kanattadır; a. meningea media ve n. mandibularis'in
  meningeal dalı (n. spinosus) geçer. Arterin ön dalı pterionun iç yüzünde seyreder ve kırıklarda epidural
  hematoma yol açar.""",
  e=["os-sphenoidale"]),

Q("f", KAF, "Aşağıdakilerden hangisi foramen jugulare'den geçmez?",
  "N. hypoglossus",
  ["N. glossopharyngeus", "N. vagus", "N. accessorius", "Sinus sigmoideus (v. jugularis interna)"],
  """Foramen jugulare'den IX, X ve XI. kafa sinirleri ile sinus sigmoideus ve sinus petrosus inferior geçer.
  N. hypoglossus kafatasını oksipital kondilin üstündeki canalis nervi hypoglossi'den terk eder.""",
  e=["os-occipitale", "os-temporale"]),

Q("t", KAF, "Canalis opticus'tan geçen yapılar hangileridir?",
  "N. opticus ve a. ophthalmica",
  ["N. opticus ve v. ophthalmica superior", "N. oculomotorius ve a. ophthalmica", "N. nasociliaris ve n. opticus",
   "A. centralis retinae ve n. trochlearis"],
  """Optik kanal sfenoidin küçük kanadının kökleri arasındadır; n. opticus ve altında a. ophthalmica geçer.
  V. ophthalmica superior, III, IV, V1 dalları ve VI ise fissura orbitalis superior'dan geçer.""",
  e=["os-sphenoidale"]),

Q("f", KAF, "Foramen stylomastoideum'dan çıkan sinir hangisidir?",
  "N. facialis",
  ["N. glossopharyngeus", "N. vestibulocochlearis", "N. accessorius", "Chorda tympani"],
  """N. facialis meatus acusticus internus'tan girip canalis facialis'te seyreder ve processus styloideus ile
  mastoideus arasındaki foramen stylomastoideum'dan çıkar; burada parotise girmeden önce yüz kaslarına
  dallanır. Bell paralizisinde bu dar kanaldaki ödem suçlanır.""",
  e=["os-temporale"]),

Q("t", KAF, "Lamina cribrosa hangi kemiğe aittir ve içinden ne geçer?",
  "Os ethmoidale – fila olfactoria (koku lifleri)",
  ["Os sphenoidale – n. opticus", "Os frontale – n. supraorbitalis", "Os ethmoidale – n. maxillaris",
   "Os nasale – n. ethmoidalis anterior"],
  """Etmoid kemiğin delikli yatay plağı burun boşluğunun tavanını yapar; koku epitelinden gelen n. olfactorius
  lifleri buradan bulbus olfactorius'a geçer. Ön kafa tabanı kırıklarında anosmi ve BOS rinoresi görülür.""",
  e=["os-ethmoidale"]),

Q("f", KAF, "Sinus maxillaris burun boşluğunda nereye açılır?",
  "Meatus nasi medius (hiatus semilunaris)",
  ["Meatus nasi inferior", "Meatus nasi superior", "Recessus sphenoethmoidalis", "Nazofarenks"],
  """Frontal, maksiller ve ön etmoid sinüsler orta meatusa (hiatus semilunaris) açılır. Ductus nasolacrimalis
  alt meatusa, arka etmoid hücreler üst meatusa, sfenoid sinüs recessus sphenoethmoidalis'e açılır.
  Maksiller sinüsün ağzı yüksekte olduğundan drenajı zordur.""",
  ["Ductus nasolacrimalis'in açıldığı yerdir.", "Arka etmoid hücrelerin açıldığı yerdir.",
   "Sfenoid sinüsün açıldığı yerdir.", "Tuba auditiva'nın açıldığı yerdir."],
  e=["maxilla", "os-ethmoidale"]),

Q("t", KAF, "Ductus nasolacrimalis burun boşluğunda nereye açılır?",
  "Meatus nasi inferior",
  ["Meatus nasi medius", "Meatus nasi superior", "Recessus sphenoethmoidalis", "Hiatus semilunaris"],
  """Gözyaşı kesesinden inen kanal maxilla, os lacrimale ve concha nasalis inferior'un oluşturduğu kemik
  kanaldan geçerek alt konkanın altındaki meatusa açılır; ağlarken burun akması bu yüzdendir.""",
  e=["concha-nasalis-inferior", "os-lacrimale"]),

Q("f", KAF, "Orbitanın iç duvarındaki ince lamina papyracea hangi kemiğe aittir?",
  "Os ethmoidale",
  ["Os lacrimale", "Maxilla", "Os sphenoidale", "Os zygomaticum"],
  """Etmoid labirentin dış yüzünü oluşturan kâğıt inceliğindeki lamina orbitalis, orbitanın iç duvarının
  büyük bölümünü yapar. Etmoid sinüzit bu ince duvardan orbitaya yayılarak orbital selülite yol açabilir.""",
  e=["os-ethmoidale"]),

Q("f", KAF, "Sutura lambdoidea hangi kemikler arasındadır?",
  "Os occipitale ile iki os parietale",
  ["Os frontale ile iki os parietale", "İki os parietale", "Os temporale ile os parietale", "Os sphenoidale ile os frontale"],
  """Lambdoid sutur oksipital kemik ile parietaller arasında Yunan λ harfi biçimindedir; sagittal sutur ile
  kesiştiği nokta lambda'dır ve arka fontanel burada kapanır. Diğer seçenekler koronal, sagittal ve
  skuamöz suturlardır.""",
  ["Sutura coronalis'tir.", "Sutura sagittalis'tir.", "Sutura squamosa'dır.", "Sutura sphenofrontalis'tir."],
  e=["os-occipitale", "os-parietale"]),

Q("t", KAF, "Foramen mandibulae'nin önünde bulunan ve lig. sphenomandibulare'nin tutunduğu çıkıntı hangisidir?",
  "Lingula mandibulae",
  ["Spina mentalis", "Processus coronoideus", "Fovea pterygoidea", "Linea mylohyoidea"],
  """Lingula, ramus mandibulae'nin iç yüzünde foramen mandibulae'yi önden örten dil biçimli kemik
  çıkıntısıdır. İnferior alveoler blokta iğne ucu lingulanın hemen üstüne yönlendirilir; n. alveolaris
  inferior buradan kanala girer.""",
  e=["mandibula"]),

Q("f", KAF, "Mandibuladaki spina mentalis'e tutunan kaslar hangileridir?",
  "M. genioglossus ve m. geniohyoideus",
  ["M. mylohyoideus ve m. digastricus'un ön karnı", "M. mentalis ve m. depressor labii inferioris",
   "M. hyoglossus ve m. genioglossus", "Platysma ve m. depressor anguli oris"],
  """Mandibulanın iç yüzünde orta hatta bulunan spina mentalis superior'a genioglossus, inferior'a
  geniohyoideus tutunur. Mylohyoideus linea mylohyoidea'ya, digastricus ön karnı fossa digastrica'ya yapışır.""",
  e=["mandibula", "m-genioglossus", "m-geniohyoideus"]),

Q("f", KAF, "Sella turcica'nın arka duvarını oluşturan yapı hangisidir?",
  "Dorsum sellae",
  ["Tuberculum sellae", "Processus clinoideus anterior", "Sulcus caroticus", "Sulcus prechiasmaticus"],
  """Sella turcica'nın önünde tuberculum sellae, arkasında dorsum sellae bulunur; dorsum sellae'nin üst
  köşeleri processus clinoidei posteriores'i oluşturur. Dorsumun arkasından aşağı inen eğim clivus'tur.""",
  e=["os-sphenoidale"]),

Q("t", KAF, "Clivus'u oluşturan kemikler hangileridir?",
  "Os sphenoidale'nin gövdesi ve os occipitale'nin pars basilaris'i",
  ["Os temporale'nin pars petrosa'sı ve os occipitale", "Os ethmoidale ve os sphenoidale", "Yalnızca os occipitale",
   "Os sphenoidale'nin büyük kanatları"],
  """Clivus dorsum sellae'den foramen magnum'a uzanan eğimli yüzeydir; üst kısmı sfenoid gövdesi, alt kısmı
  oksipital kemiğin baziler kısmıdır. Üzerinde pons ve a. basilaris yatar; ikisi arasındaki sfeno-oksipital
  sinkondroz ergenlikte kemikleşir.""",
  e=["os-occipitale", "os-sphenoidale"]),

Q("f", KAF, "Meatus acusticus internus'tan geçen sinirler hangileridir?",
  "N. facialis ve n. vestibulocochlearis",
  ["N. facialis ve n. glossopharyngeus", "N. vestibulocochlearis ve n. vagus", "N. trigeminus ve n. facialis",
   "N. abducens ve n. facialis"],
  """Temporal kemiğin petröz kısmındaki iç kulak yolundan n. facialis (ve n. intermedius), n. vestibulocochlearis
  ile a. labyrinthi geçer. Akustik nörinom burada hem işitme hem yüz siniri bulgularına yol açabilir.""",
  e=["os-temporale"]),

Q("t", KAF, "Fossa pterygopalatina'nın iç duvarını oluşturan kemik hangisidir?",
  "Os palatinum (lamina perpendicularis)",
  ["Maxilla", "Os sphenoidale'nin processus pterygoideus'u", "Os zygomaticum", "Vomer"],
  """Pterygopalatin çukurun önünde maxilla tuber'i, arkasında processus pterygoideus, içinde os palatinum'un
  dikey plağı bulunur. İç duvardaki foramen sphenopalatinum çukuru burun boşluğuna bağlar; çukurda
  ganglion pterygopalatinum ve a. maxillaris'in son bölümü yer alır.""",
  ["Ön duvarı oluşturur.", "Arka duvarı oluşturur.", "Fossaya komşu değildir.", "Burun septumunun parçasıdır."],
  e=["os-palatinum", "os-sphenoidale"]),

# ------------------------------------------------------------------ omurga
Q("f", OMR, "Foramen transversarium hangi omurlara özgüdür?",
  "Boyun omurları",
  ["Göğüs omurları", "Bel omurları", "Sakral omurlar", "Koksigeal omurlar"],
  """Boyun omurlarının transvers çıkıntılarındaki delikten a. ve v. vertebralis geçer; arter çoğunlukla
  C6'dan girer, C7'nin deliğinden yalnızca ven geçer. Bu delik boyun omurlarını diğerlerinden ayırmanın
  en güvenilir ölçütüdür.""",
  e=["vertebrae-cervicales"]),

Q("t", OMR, "Bel omurlarının ayırt edici özellikleri hangisidir?",
  "Büyük böbrek biçimli gövde, kalın dikdörtgen dikensi çıkıntı ve sagittal düzlemde eklem yüzleri",
  ["Kalp biçimli gövde ve kostal eklem yüzleri", "Çatallı dikensi çıkıntı ve foramen transversarium",
   "Gövdesi olmayan halka biçimi", "Yukarı uzanan diş biçimli çıkıntı"],
  """Lomber omurlar ağırlık taşıdıkları için en büyük gövdelere sahiptir; eklem yüzleri sagittal düzlemde
  olduğundan fleksiyon–ekstansiyona izin verir, rotasyonu kısıtlar. Diğer seçenekler göğüs omuru, boyun
  omuru, atlas ve axis'e aittir.""",
  ["Göğüs omurlarının özelliğidir.", "Boyun omurlarının özelliğidir.", "Atlasın özelliğidir.", "Axis'in özelliğidir."],
  e=["vertebrae-lumbales"]),

Q("f", OMR, "Erişkinde medulla spinalis genellikle hangi düzeyde sonlanır?",
  "L1–L2",
  ["T10", "L3–L4", "S2", "L5"],
  """Erişkinde conus medullaris L1–L2 düzeyinde sonlanır; yenidoğanda L3 düzeyindedir. Dural kese ve
  subaraknoid boşluk ise S2'ye kadar uzanır; bu nedenle lomber ponksiyon omuriliğin altında, cauda
  equina düzeyinde yapılır.""",
  ["Omurilik bu düzeyin altına uzanır.", "Yenidoğandaki düzeydir.", "Dural kesenin sonlandığı düzeydir.",
   "Omurilik bu düzeye uzanmaz."],
  e=["vertebrae-lumbales"]),

Q("t", OMR, "Lomber ponksiyon için güvenli düzey ve bu düzeyi bulmada kullanılan nokta hangisidir?",
  "L3–L4 veya L4–L5 aralığı; iki crista iliaca'nın en yüksek noktalarını birleştiren çizgi (L4)",
  ["T12–L1 aralığı; skapulaların alt açıları", "L1–L2 aralığı; 12. kaburgaların uçları",
   "S2–S3 aralığı; SIPS'leri birleştiren çizgi", "T10–T11 aralığı; göbek hizası"],
  """Supracristal (Tuffier) çizgi L4 dikensi çıkıntısından veya L4–L5 aralığından geçer. Bu düzey conus
  medullaris'in altında kaldığından iğne cauda equina köklerini iterek subaraknoid boşluğa ulaşır.""",
  e=["vertebrae-lumbales"]),

Q("t", OMR, "Spondilolizde kemik defekti omurun hangi bölümündedir?",
  "Pars interarticularis",
  ["Pedikül", "Laminaların orta hatta birleşme yeri", "Omur gövdesinin ön kenarı", "Processus transversus"],
  """Spondilolizis, üst ve alt eklem çıkıntıları arasındaki pars interarticularis'in stres kırığıdır; en sık
  L5'te görülür. Eğik grafide ‘İskoç köpeğinin boynundaki tasma’ görünümü verir; iki taraflı olursa omur
  öne kayabilir (spondilolistezis). Laminaların birleşmeme kusuru spina bifida'dır.""",
  e=["vertebrae-lumbales"]),

Q("f", OMR, "Atlasın ön ve arka kemerlerinin kırıldığı Jefferson kırığı genellikle hangi mekanizmayla oluşur?",
  "Başın tepesine dikey yüklenme (aksiyel kompresyon)",
  ["Hiperekstansiyonla axis pediküllerinin kırılması", "Ani fleksiyonla dens kırılması",
   "C7 dikensi çıkıntısının kas çekmesiyle kopması", "Rotasyonla faset eklem çıkığı"],
  """Sığ suya baş üstü dalma gibi aksiyel yüklenmede oksipital kondiller atlasın massa lateralis'lerini
  yana iter ve halka birkaç yerden kırılır. Spinal kanal genişlediği için nörolojik hasar çoğu zaman
  olmaz. Diğer seçenekler Hangman, dens ve clay-shoveler kırıklarını tanımlar.""",
  ["Hangman (cellat) kırığını tanımlar.", "Dens kırığını tanımlar.", "Clay-shoveler kırığını tanımlar.",
   "Faset çıkığını tanımlar."],
  e=["atlas"]),

Q("t", OMR, "Axis'in iki taraflı pars interarticularis (pedikül) kırığı hangi adla bilinir?",
  "Hangman (cellat) kırığı",
  ["Jefferson kırığı", "Clay-shoveler kırığı", "Chance kırığı", "Tip II dens kırığı"],
  """Hiperekstansiyon ve distraksiyonla C2'nin pedikülleri kırılır; asılma, emniyet kemeri olmadan çene
  ile ön panele çarpma tipik mekanizmadır. Chance kırığı emniyet kemeriyle ilişkili torakolomber
  fleksiyon-distraksiyon kırığıdır.""",
  e=["axis"]),

Q("f", OMR, "Foramina sacralia anteriora'dan çıkan yapılar hangileridir?",
  "Sakral spinal sinirlerin ön dalları",
  ["Sakral spinal sinirlerin arka dalları", "A. sacralis mediana", "Truncus sympathicus", "Filum terminale"],
  """Sakrumun ön (pelvik) yüzündeki dört çift delikten S1–S4 sinirlerinin ön dalları çıkarak plexus sacralis'e
  katılır; arka dallar foramina sacralia posteriora'dan çıkar. Filum terminale hiatus sacralis'ten çıkar.""",
  e=["os-sacrum"]),

Q("t", OMR, "Hiatus sacralis'i iki yandan sınırlayan çıkıntılar hangileridir?",
  "Cornua sacralia",
  ["Promontorium", "Crista sacralis lateralis", "Ala ossis sacri", "Cornua coccygea"],
  """S5'in laminaları birleşmediği için sakral kanal altta hiatus sacralis ile açılır; iki yanındaki
  cornua sacralia ele gelir ve kaudal epidural blokta iğnenin yerini bulmaya yarar.""",
  e=["os-sacrum"]),

# ------------------------------------------------------------------ göğüs kafesi
Q("f", GKF, "Atipik kaburgalar hangileridir?",
  "1., 2., 10., 11. ve 12. kaburgalar",
  ["Yalnızca 1., 2. ve 12. kaburgalar", "1., 11. ve 12. kaburgalar", "1.–7. kaburgalar", "8., 9. ve 10. kaburgalar"],
  """Tipik kaburgada baş (iki eklem yüzlü), boyun, tüberkül ve gövde bulunur. 1. kaburga en kısa, en geniş
  ve en kıvrık olanıdır; 2. kaburgada serratus anterior tüberozitesi vardır; 10.–12. kaburgaların başında
  tek eklem yüzü bulunur, 11. ve 12.'nin boynu ve tüberkülü yoktur.""",
  e=["costae"]),

Q("t", GKF, "Birinci kaburgada skalen tüberkülün önündeki olukta seyreden yapı hangisidir?",
  "V. subclavia",
  ["Plexus brachialis'in alt gövdesi", "A. subclavia", "N. phrenicus", "Ductus thoracicus"],
  """Skalen tüberküle tutunan m. scalenus anterior, v. subclavia'yı (önde) a. subclavia ve plexus
  brachialis'in alt gövdesinden (arkada) ayırır. Bu nedenle subklavyen ven kanülasyonunda iğne
  kasın önünde kalır.""",
  ["Arteriyle birlikte tüberkülün arkasından geçer.", "Tüberkülün arkasındaki oluktan geçer.",
   "M. scalenus anterior'un ön yüzünde iner; olukta seyretmez.", "Sol venöz açıya boşalır; kaburgada seyretmez."],
  e=["costae", "m-scalenus-anterior"]),

Q("t", GKF, "Solunumda ‘pompa kolu’ (pump handle) hareketi neyi ifade eder?",
  "Üst kaburgaların ve sternumun yükselerek göğsün ön-arka çapını artırması",
  ["Alt kaburgaların yana açılarak enine çapı artırması", "Diyaframın inerek dikey çapı artırması",
   "Sternumun aşağı inmesi", "Kaburgaların omurga etrafında içe dönmesi"],
  """Üst kaburgalar inspirasyonda sternumu öne-yukarı iterek ön-arka çapı artırır (pompa kolu); alt
  kaburgalar ise yana açılarak enine çapı artırır (kova sapı). Dikey çapı diyaframın kasılması artırır.""",
  ["Kova sapı (bucket handle) hareketidir.", "Diyafram kasılmasıdır.", "Ekspirasyonda olur.", "Böyle bir hareket yoktur."],
  e=["costae", "sternum"]),

# ------------------------------------------------------------------ üst ekstremite
Q("t", UST, "Lig. transversum scapulae superius'un üstünden geçen yapı hangisidir?",
  "A. suprascapularis",
  ["N. suprascapularis", "N. dorsalis scapulae", "A. transversa colli'nin derin dalı", "N. axillaris"],
  """Incisura scapulae'yi köprüleyen bağın altından n. suprascapularis, üstünden a. suprascapularis geçer
  (‘ordu köprünün üstünden, donanma altından geçer’). Sinir bu çentikte sıkışırsa supraspinatus ve
  infraspinatus zayıflar.""",
  e=["scapula", "m-supraspinatus"]),

Q("f", UST, "Humerusta collum anatomicum ile collum chirurgicum arasındaki fark hangisidir?",
  "Anatomik boyun eklem başının hemen altındaki daralma, cerrahi boyun tüberküllerin altındaki kırığa yatkın bölgedir",
  ["Cerrahi boyun eklem başının hemen altındadır, anatomik boyun tüberküllerin altındadır",
   "İkisi aynı yerdir, yalnızca adları farklıdır", "Anatomik boyun humerusun alt ucundadır",
   "Cerrahi boyun n. radialis'in oluğudur"],
  """Collum anatomicum eklem başı ile tüberküller arasındaki sığ oluktur ve eklem kapsülü buraya tutunur.
  Collum chirurgicum tüberküllerin altındaki daralmadır; yaşlılarda sık kırılır ve n. axillaris ile
  a. circumflexa humeri posterior burada risk altındadır.""",
  e=["humerus"]),

Q("t", UST, "Humerustaki sulcus nervi radialis'te seyreden yapılar hangileridir?",
  "N. radialis ve a. profunda brachii",
  ["N. ulnaris ve a. collateralis ulnaris superior", "N. axillaris ve a. circumflexa humeri posterior",
   "N. medianus ve a. brachialis", "N. musculocutaneus ve a. brachialis"],
  """Radial oluk humerus cisminin arka yüzünde, triseps'in lateral ve medial başlarının origoları arasında
  spiral seyreder. Cisim ortası kırıklarında n. radialis yaralanır ve düşük el gelişir; triseps dalları
  daha yukarıda ayrıldığı için dirsek ekstansiyonu çoğunlukla korunur.""",
  e=["humerus", "m-triceps-brachii"]),

Q("f", UST, "Olecranon'a tutunan kas hangisidir?",
  "M. triceps brachii",
  ["M. brachialis", "M. biceps brachii", "M. pronator quadratus", "M. flexor carpi radialis"],
  """Triseps'in üç başı ortak tendonla olecranon'un üst-arka yüzüne tutunur ve dirseği ekstansiyona getirir.
  Brachialis tuberositas ulnae'ye, biceps tuberositas radii'ye tutunur.""",
  e=["ulna", "m-triceps-brachii"]),

Q("t", UST, "Proksimalde radius başının eklem yaptığı ulnadaki eklem yüzü hangisidir?",
  "Incisura radialis ulnae",
  ["Incisura trochlearis", "Incisura ulnaris radii", "Capitulum humeri", "Fovea articularis capitis radii"],
  """Radius başının çevresi (circumferentia articularis) ulnanın incisura radialis'i ve lig. anulare radii
  ile proksimal radioulnar eklemi yapar. Incisura trochlearis trochlea humeri ile, incisura ulnaris radii
  distalde ulna başı ile eklemleşir.""",
  e=["ulna", "radius"]),

Q("f", UST, "Radiusun distal ucunda ulna başıyla eklem yapan çentik hangisidir?",
  "Incisura ulnaris radii",
  ["Incisura radialis ulnae", "Processus styloideus radii", "Tuberculum dorsale (Lister)", "Facies articularis carpalis"],
  """Distal radioulnar eklemde ulna başı radiusun incisura ulnaris'ine oturur; pronasyon-supinasyonda radius
  bu sabit ulna başı etrafında döner. Eklem, üçgen fibrokartilaj kompleksi (TFCC) ile desteklenir.""",
  e=["radius"]),

# ------------------------------------------------------------------ el
Q("t", ELK, "Distal sıra karpal kemiklerin radialden ulnara sırası hangisidir?",
  "Trapezium, trapezoideum, capitatum, hamatum",
  ["Trapezoideum, trapezium, capitatum, hamatum", "Trapezium, capitatum, trapezoideum, hamatum",
   "Hamatum, capitatum, trapezoideum, trapezium", "Scaphoideum, lunatum, triquetrum, pisiforme"],
  """Distal sıra dıştan içe trapezium (başparmak tarafı), trapezoideum, capitatum (en büyük) ve hamatum'dur.
  Proksimal sıra scaphoideum, lunatum, triquetrum ve pisiforme'dir.""",
  e=["ossa-carpi", "os-trapezium", "os-capitatum", "os-hamatum"]),

Q("t", ELK, "Kienböck hastalığı hangi kemiğin avasküler nekrozudur?",
  "Os lunatum",
  ["Os scaphoideum", "Os capitatum", "Caput femoris", "Os naviculare (ayak)"],
  """Kienböck hastalığı lunatumun avasküler nekrozudur; negatif ulnar varyans (kısa ulna) risk etkenidir.
  Skafoidin idiyopatik nekrozu Preiser, femur başınınki Legg–Calvé–Perthes, ayak naviküleri Köhler
  hastalığı olarak bilinir.""",
  ["Preiser hastalığının yeridir.", "Kendine özgü adlandırılmış bir nekrozu yoktur.",
   "Legg–Calvé–Perthes hastalığının yeridir.", "Köhler hastalığının yeridir."],
  e=["os-lunatum"]),

Q("f", ELK, "Hamulus ossis hamati'ye tutunan yapılar hangileridir?",
  "Retinaculum flexorum ile hipotenar kaslardan flexor ve opponens digiti minimi",
  ["Retinaculum extensorum ve m. extensor carpi ulnaris", "M. flexor carpi radialis tendonu",
   "M. abductor pollicis brevis ve m. opponens pollicis", "M. adductor pollicis'in oblik başı"],
  """Hamatın çengeli retinaculum flexorum'un iç-alt tutunma noktasıdır; flexor digiti minimi brevis ve
  opponens digiti minimi de buradan başlar. Çengel Guyon kanalının dış sınırıdır; golf ve beyzbolda
  kırılabilir ve n. ulnaris'in derin dalını etkileyebilir.""",
  e=["os-hamatum", "mm-hypothenares"]),

Q("f", ELK, "En kısa ve en hareketli metakarp kemiği hangisidir?",
  "1. metakarp",
  ["2. metakarp", "3. metakarp", "4. metakarp", "5. metakarp"],
  """Başparmağın metakarpı trapezium ile eyer eklem yaparak opozisyona izin verir. 2. ve 3. metakarplar en
  sabit olanlardır (el iskeletinin ‘sabit ünitesi’); 3. metakarpın tabanında stiloid çıkıntı bulunur.""",
  e=["ossa-metacarpi"]),

# ------------------------------------------------------------------ alt ekstremite
Q("t", ALT, "Spina iliaca anterior superior'a (SIAS) tutunan yapılar hangileridir?",
  "M. sartorius, m. tensor fasciae latae ve lig. inguinale",
  ["M. rectus femoris'in düz başı ve lig. iliofemorale", "M. iliacus ve m. psoas minor", "M. gracilis ve m. adductor longus",
   "M. obliquus internus ve lig. lacunare"],
  """SIAS'tan sartorius ve TFL başlar, lig. inguinale buradan tuberculum pubicum'a uzanır. SIAI'ye rectus
  femoris'in düz başı ve iliofemoral bağ tutunur. Ergen sporcularda sartorius SIAS'ı, rectus femoris SIAI'yi
  avülsiyonla koparabilir.""",
  ["SIAI'ye tutunan yapılardır.", "Fossa iliaca ve psoas'ın yapılarıdır.", "Pubisten başlarlar.",
   "Lig. lacunare pubise uzanır."],
  e=["os-coxae", "m-sartorius", "lig-inguinale"]),

Q("f", ALT, "Aşağıdakilerden hangisi tuber ischiadicum'dan başlamaz?",
  "M. biceps femoris'in kısa başı",
  ["M. biceps femoris'in uzun başı", "M. semitendinosus", "M. semimembranosus", "M. adductor magnus'un hamstring bölümü"],
  """Kısa baş linea aspera'nın dış dudağından başlar ve yalnızca diz eklemini geçer. İskial tüberoz oturma
  kemiğidir; hamstringler ve adductor magnus'un dikey lifleri buradan başlar, lig. sacrotuberale buraya
  tutunur.""",
  e=["os-coxae", "mm-ischiocrurales", "m-biceps-femoris"]),

Q("t", ALT, "Erişkinde femur başının ana kanlanmasını sağlayan arter hangisidir?",
  "A. circumflexa femoris medialis",
  ["Lig. capitis femoris içindeki arter", "A. circumflexa femoris lateralis", "A. profunda femoris'in perforan dalları",
   "A. glutea superior"],
  """Femur başını erişkinde büyük ölçüde a. circumflexa femoris medialis'in boyun boyunca yukarı çıkan
  retinaküler dalları besler. İntrakapsüler (subkapital) kırıklarda bu dallar yırtılır ve avasküler nekroz
  gelişebilir; lig. capitis femoris arteri erişkinde katkı sağlamaz.""",
  e=["femur", "art-coxae"]),

Q("f", ALT, "Erişkinde femurun boyun–cisim açısı yaklaşık kaç derecedir?",
  "125°",
  ["90°", "150°", "105°", "170°"],
  """Kolodiafizer açı doğumda yaklaşık 150° iken erişkinde 125° civarına iner. Açının belirgin artışı coxa
  valga, azalışı coxa vara olarak adlandırılır; kadınlarda geniş pelvis nedeniyle biraz daha küçüktür.""",
  e=["femur"]),

Q("t", ALT, "Aşağıdaki kaslardan hangisi linea aspera'dan başlamaz?",
  "M. vastus intermedius",
  ["M. vastus lateralis", "M. vastus medialis", "M. biceps femoris'in kısa başı", "M. adductor magnus"],
  """Vastus intermedius femur cisminin ön ve dış yüzlerinden başlar. Linea aspera'nın dış dudağından vastus
  lateralis ve biceps femoris kısa başı, iç dudağından vastus medialis başlar; addüktörler ise linea
  aspera'ya tutunur.""",
  e=["femur", "m-vastus-intermedius"]),

Q("f", ALT, "Gerdy tüberkülüne tutunan yapı hangisidir?",
  "Tractus iliotibialis",
  ["Lig. patellae", "Pes anserinus", "Lig. collaterale fibulare", "M. popliteus"],
  """Gerdy tüberkülü tibianın lateral kondilinin ön-dış yüzündedir; iliotibial bant buraya tutunur. Lig.
  patellae tuberositas tibiae'ye, pes anserinus tibianın üst iç yüzüne, lateral kollateral bağ fibula
  başına yapışır.""",
  e=["tibia", "tractus-iliotibialis"]),

Q("f", ALT, "Caput fibulae'ye tutunan yapılar hangileridir?",
  "M. biceps femoris tendonu ve lig. collaterale fibulare",
  ["Pes anserinus ve lig. collaterale tibiale", "Lig. patellae", "Tractus iliotibialis ve m. tensor fasciae latae",
   "M. popliteus ve lateral menisküs"],
  """Fibula başına biceps femoris tendonu ve dış yan bağ tutunur; n. fibularis communis hemen altında fibula
  boynunu sararak öne geçer. Bu nedenle fibula boynu kırıklarında düşük ayak gelişebilir.""",
  e=["fibula", "m-biceps-femoris", "ligg-collateralia-genus"]),

Q("t", ALT, "Patella için hangisi doğrudur?",
  "Vücudun en büyük sesamoid kemiğidir ve kuadriseps tendonu içinde gelişir",
  ["Arka yüzünde iç faset dış fasetten daha büyüktür", "Lig. patellae ile tibianın iç kondiline tutunur",
   "Diz eklem boşluğunun dışında kalır", "Doğumda tamamen kemikleşmiştir"],
  """Patella kuadrisepsin kaldıraç kolunu uzatarak ekstansiyon gücünü artırır. Arka yüzünde dış faset daha
  geniştir; lig. patellae ile tuberositas tibiae'ye bağlanır ve arka yüzü eklem boşluğuna bakar. Kemikleşmesi
  3–6 yaş arasında başlar.""",
  e=["patella"]),

Q("t", ALT, "Segond kırığı neyin göstergesidir?",
  "Tibia lateral platosu kenarında avülsiyon; ön çapraz bağ yırtığına eşlik eder",
  ["Arka çapraz bağ yırtığına eşlik eden fibula başı kırığı", "İç kollateral bağın femur tutunma yerindeki kalsifikasyon",
   "Patellanın lateral çıkığında oluşan osteokondral kırık", "Tuberositas tibiae'nin apofizit kaynaklı ayrılması"],
  """Segond kırığı, dizin iç rotasyon ve varus zorlanmasında anterolateral kapsül/bağın tibia lateral
  platosundan küçük bir kemik parçası koparmasıdır; grafide küçük görünse de yüksek oranda ön çapraz bağ
  yırtığına işaret eder. İç kollateral bağ kalsifikasyonu Pellegrini–Stieda, tüberozite apofiziti
  Osgood–Schlatter'dır.""",
  e=["tibia", "ligg-cruciata"]),

# ------------------------------------------------------------------ ayak
Q("f", AYK, "Talusun hangi bölümü ayak bileği (talokrural) eklemine katılır?",
  "Trochlea tali",
  ["Caput tali", "Facies articularis calcanea anterior", "Sulcus tali", "Processus posterior tali"],
  """Trochlea tali tibianın alt yüzü ve iki malleol arasındaki ‘zıvana’ya oturur. Trochlea önde daha
  geniş olduğundan dorsifleksiyonda eklem en kararlı hale gelir. Caput tali naviküler ile eklem yapar.""",
  e=["talus", "art-talocruralis"]),

Q("t", AYK, "Talusun arka çıkıntısının dış tüberkülünün ayrı kalmasıyla oluşan aksesuar kemik hangisidir?",
  "Os trigonum",
  ["Os naviculare accessorium", "Os peroneum", "Os vesalianum", "Os intermetatarseum"],
  """Os trigonum, processus posterior tali'nin dış tüberkülünün kaynamamasıyla oluşur; balerinler ve
  futbolcularda zorlu plantar fleksiyonda arka ayak bileğinde sıkışma (posterior impingement) yapabilir.""",
  e=["talus"]),

Q("f", AYK, "Sinus tarsi hangi iki kemik arasındaki boşluktur?",
  "Talus ve calcaneus",
  ["Talus ve os naviculare", "Calcaneus ve os cuboideum", "Os naviculare ve os cuneiforme", "Tibia ve fibula"],
  """Sinus tarsi, talus boynunun altındaki sulcus tali ile calcaneus'un üstündeki sulcus calcanei'nin
  oluşturduğu dış tarafa açılan kanaldır; içinde güçlü lig. talocalcaneum interosseum bulunur ve önünden
  extensor digitorum brevis başlar.""",
  e=["talus", "calcaneus"]),

Q("t", AYK, "Ayağın lateral longitudinal kavsine katılan kemikler hangileridir?",
  "Calcaneus, os cuboideum ve 4.–5. metatarslar",
  ["Calcaneus, talus, naviculare, cuneiformia ve 1.–3. metatarslar", "Cuneiformia ve metatars tabanları",
   "Talus, os cuboideum ve 5. metatars", "Calcaneus, os naviculare ve 1. metatars"],
  """Lateral kavis alçaktır ve yere yakındır; ağırlık taşımada önemlidir, kilit taşı kuboiddir. Medial kavis
  daha yüksektir ve calcaneus, talus, naviculare, üç cuneiforme ve 1.–3. metatarslardan oluşur.""",
  ["Medial longitudinal kavisi tanımlar.", "Transvers kavisi tanımlar.", "Talus lateral kavse katılmaz.",
   "Karışık bir dizidir."],
  e=["os-cuboideum", "calcaneus", "ossa-metatarsi"]),

Q("tv", AYK, """Askerlik eğitiminin ilk haftalarında uzun yürüyüşlerden sonra ayağının ön kısmında ağrı başlayan
gencin grafisinde 2. metatars cisminde stres kırığı saptanıyor. Bu kırığın yaygın adı hangisidir?""",
  "Marş (yürüyüş) kırığı",
  ["Jones kırığı", "Lisfranc yaralanması", "Pott kırığı", "Chopart çıkığı"],
  """Tekrarlayan yüklenme en ince ve en uzun metatars olan 2. metatarsta stres kırığına yol açar; ilk
  grafiler normal olabilir, kallus birkaç hafta sonra görünür. Jones kırığı 5. metatarsın metafiz–diafiz
  bileşkesindedir.""",
  e=["ossa-metatarsi"]),

Q("t", AYK, "Jones kırığı için hangisi doğrudur?",
  "5. metatarsın metafiz–diafiz bileşkesinde olur ve kaynamama riski yüksektir",
  ["5. metatars tuberositasının fibularis brevis ile avülsiyonudur", "Calcaneus'un stres kırığıdır",
   "1. metatars başında olur", "Talus boynu kırığıdır"],
  """Jones kırığı tuberositasın 1,5–3 cm distalindeki, kanlanmanın zayıf olduğu ‘su ayrımı’ bölgesindedir;
  kaynamama sık olduğundan cerrahi gerekebilir. Tuberositas avülsiyonu (psödo-Jones) ise inversiyonla
  fibularis brevis çekmesi sonucu olur ve genellikle iyi iyileşir.""",
  e=["ossa-metatarsi", "m-fibularis-brevis"]),

Q("f", AYK, "Tuber calcanei'ye tutunan tendon hangisidir?",
  "Tendo calcaneus (Aşil tendonu)",
  ["M. tibialis anterior tendonu", "M. fibularis brevis tendonu", "M. tibialis posterior tendonu",
   "M. flexor hallucis longus tendonu"],
  """Gastrocnemius ve soleus'un ortak tendonu olan Aşil tendonu topuk yumrusunun arka yüzünün orta kısmına
  tutunur; vücudun en kalın ve en güçlü tendonudur. Tutunma yerinin 2–6 cm yukarısı kanlanmanın en zayıf
  olduğu ve yırtığın en sık görüldüğü bölgedir.""",
  e=["calcaneus", "m-triceps-surae"]),
]
