from qcommon import Q, write

KF = "Kafatası (Cranium)"
OM = "Omurga (Columna vertebralis)"
GK = "Göğüs kafesi (Thorax)"
UE = "Üst ekstremite kemikleri"
EL = "El kemikleri"
AE = "Alt ekstremite kemikleri"
AY = "Ayak kemikleri"

questions = [
# ------------------------------------------------------------------ Kafatası
Q("tv", KF, """Motosiklet kazası geçiren 24 yaşındaki hasta kısa süre bilinç kaybından sonra
uyanıyor, birkaç saat sonra bilinci yeniden bulanıyor. BT'de temporal bölgede bikonveks
epidural hematom görülüyor. Kanayan arter kafa boşluğuna hangi delikten girer?""",
  "Foramen spinosum",
  ["Foramen ovale", "Foramen rotundum", "Foramen lacerum", "Canalis caroticus"],
  """Lusid aralıklı epidural hematomun klasik kaynağı a. meningea media'dır. A. maxillaris'in
  dalı olan bu arter foramen spinosum'dan orta kafa çukuruna girer; ön dalı pterion'un iç
  yüzünde seyrettiği için bu bölgenin kırıkları arteri yırtar.""",
  ["N. mandibularis (V3) ve a. meningea accessoria geçer.", "N. maxillaris (V2) geçer.",
   "Canlıda kıkırdakla kapalıdır; üzerinden n. petrosus major geçer.", "A. carotis interna ve sempatik pleksus geçer."],
  e=["os-sphenoidale", "os-temporale", "os-parietale"]),

Q("f", KF, "Foramen rotundum'dan geçen yapı hangisidir?",
  "N. maxillaris",
  ["N. mandibularis", "N. ophthalmicus", "A. meningea media", "N. petrosus major"],
  """Os sphenoidale'nin ala major'unda bulunan foramen rotundum, n. trigeminus'un ikinci dalı
  n. maxillaris'i (V2) orta kafa çukurundan fossa pterygopalatina'ya iletir.""",
  ["Foramen ovale'den geçer.", "Fissura orbitalis superior'dan orbitaya girer.",
   "Foramen spinosum'dan girer.", "Foramen lacerum üzerinden canalis pterygoideus'a gider."],
  e=["os-sphenoidale", "n-trigeminus"]),

Q("tv", KF, """Kafa tabanı kırığı olan bir hastada yutma güçlüğü, ses kısıklığı, aynı tarafta omuz
silkmede ve başı karşı tarafa çevirmede güçsüzlük saptanıyor. Lezyon büyük olasılıkla hangi
açıklıktadır?""",
  "Foramen jugulare",
  ["Canalis nervi hypoglossi", "Foramen magnum", "Meatus acusticus internus", "Foramen stylomastoideum"],
  """Foramen jugulare'den n. glossopharyngeus (IX), n. vagus (X) ve n. accessorius (XI) ile
  v. jugularis interna'nın başlangıcı geçer. IX–X tutulumu yutma güçlüğü ve ses kısıklığı;
  XI tutulumu trapezius ve sternocleidomastoideus güçsüzlüğü yapar (Vernet sendromu).""",
  ["Yalnızca n. hypoglossus geçer; dil sapması olurdu.", "Medulla oblongata, aa. vertebrales ve XI'in spinal kökleri geçer; bu tablo tipik değildir.",
   "N. facialis ve n. vestibulocochlearis geçer.", "N. facialis kafatasından çıkar; yüz felci olurdu."],
  e=["os-occipitale", "os-temporale", "n-vagus", "n-accessorius", "n-glossopharyngeus"]),

Q("t", KF, "Aşağıdaki yapılardan hangisi fissura orbitalis superior'dan geçmez?",
  "N. opticus",
  ["N. oculomotorius", "N. trochlearis", "N. abducens", "V. ophthalmica superior"],
  """N. opticus a. ophthalmica ile birlikte canalis opticus'tan geçer. Fissura orbitalis
  superior'dan III, IV, VI, n. ophthalmicus'un dalları (n. lacrimalis, n. frontalis,
  n. nasociliaris) ve v. ophthalmica superior geçer.""",
  e=["os-sphenoidale", "n-opticus"]),

Q("f", KF, "Aşağıdaki kemiklerden hangisi pterion'un oluşumuna katılmaz?",
  "Os zygomaticum",
  ["Os frontale", "Os parietale", "Os temporale", "Os sphenoidale"],
  """Pterion; os frontale, os parietale, os temporale'nin squama'sı ve os sphenoidale'nin
  ala major'unun birleştiği H şeklindeki bölgedir. Kafatasının en ince yerlerinden biridir
  ve iç yüzünde a. meningea media'nın ön dalı seyreder.""",
  e=["os-frontale", "os-parietale", "os-temporale", "os-sphenoidale"]),

Q("fv", KF, """Ön kafa tabanı kırığı geçiren hastada burundan berrak sıvı gelmesi (rinore) ve koku
alamama gelişiyor. Kırık büyük olasılıkla hangi kemiğin hangi bölümündedir?""",
  "Os ethmoidale – lamina cribrosa",
  ["Os sphenoidale – corpus", "Os frontale – pars orbitalis", "Os nasale", "Vomer"],
  """Lamina cribrosa'nın deliklerinden fila olfactoria geçer. Kırığında koku lifleri kopar
  (anozmi) ve dura ile araknoid yırtılırsa beyin-omurilik sıvısı burun boşluğuna akar.""",
  e=["os-ethmoidale", "n-olfactorius"]),

Q("f", KF, "Hipofiz bezinin yerleştiği sella turcica hangi kemiğin üzerindedir?",
  "Os sphenoidale",
  ["Os ethmoidale", "Os occipitale", "Os temporale", "Os frontale"],
  """Sella turcica, os sphenoidale'nin corpus'unun üst yüzündeki eyer biçimli çukurdur; ortadaki
  fossa hypophysialis'e hipofiz oturur. Altında sinus sphenoidalis vardır; bu nedenle hipofiz
  cerrahisi transsfenoidal yolla yapılabilir.""",
  e=["os-sphenoidale", "hypophysis"]),

Q("tv", KF, """Diş hekimi alt çenedeki azı dişlerinde işlem yapmadan önce anestezi uyguluyor.
İğne hangi deliğin çevresine yapılırsa aynı taraftaki tüm alt dişler uyuşur?""",
  "Foramen mandibulae",
  ["Foramen mentale", "Foramen infraorbitale", "Foramen ovale", "Canalis incisivus"],
  """N. alveolaris inferior (V3) ramus mandibulae'nin iç yüzündeki foramen mandibulae'den
  canalis mandibulae'ye girer ve tüm alt dişleri innerve eder. Lingula'nın hemen üstüne
  yapılan blok aynı taraftaki dişleri, alt dudağı ve çene derisini uyuşturur.""",
  ["Buradan çıkan n. mentalis yalnızca alt dudak ve çene derisini innerve eder.", "Üst çene: n. infraorbitalis çıkar.",
   "Kafa tabanındadır; buraya ulaşmak pratik değildir.", "Üst ön dişlerin damak mukozası (n. nasopalatinus) içindir."],
  e=["mandibula", "n-trigeminus", "dentes"]),

Q("f", KF, "Foramen mentale'den çıkan sinir hangi sinirin dalıdır?",
  "N. alveolaris inferior",
  ["N. lingualis", "N. buccalis", "N. infraorbitalis", "N. facialis (ramus marginalis mandibulae)"],
  """Foramen mentale genellikle ikinci alt küçük azı dişinin altındadır. N. alveolaris inferior'un
  uç dalı olan n. mentalis buradan çıkarak alt dudak ve çene derisinin duyusunu alır.""",
  e=["mandibula", "n-trigeminus"]),

Q("tv", KF, """Çeneye yumruk yiyen hastada collum mandibulae kırığı saptanıyor. Kondil parçası öne ve
içe doğru yer değiştirmiştir. Bu yer değişikliğinden sorumlu kas hangisidir?""",
  "M. pterygoideus lateralis",
  ["M. masseter", "M. temporalis", "M. pterygoideus medialis", "M. digastricus"],
  """M. pterygoideus lateralis fovea pterygoidea (kondil boynu) ve eklem diskine tutunur, kondili
  öne ve içe çeker. Kırıkta proksimal parça bu kasın çekmesiyle anteromediale kayar.""",
  ["Ramus ve angulus'un dış yüzüne tutunur; distal parçayı yukarı çeker.", "Processus coronoideus'a tutunur.",
   "Angulus'un iç yüzüne tutunur; kondil parçasını etkilemez.", "Corpus mandibulae'ye yakın tutunur; çeneyi aşağı çeker."],
  e=["mandibula", "mm-pterygoidei", "art-temporomandibularis"]),

Q("f", KF, "Vücutta başka hiçbir kemikle eklem yapmayan kemik hangisidir?",
  "Os hyoideum",
  ["Vomer", "Os lacrimale", "Patella", "Os coccygis"],
  """Os hyoideum C3 düzeyinde, kaslar ve bağlarla (lig. stylohyoideum, membrana thyrohyoidea)
  asılı durur; hiçbir kemikle eklem yapmaz. Supra- ve infrahyoid kasların tutunma yeridir.""",
  e=["os-hyoideum", "mm-suprahyoidei", "mm-infrahyoidei"]),

Q("t", KF, "Aşağıdaki yapılardan hangisi processus styloideus'a tutunmaz?",
  "M. digastricus venter posterior",
  ["M. styloglossus", "M. stylohyoideus", "M. stylopharyngeus", "Lig. stylomandibulare"],
  """M. digastricus'un arka karnı os temporale'deki incisura mastoidea'dan başlar. Processus
  styloideus'tan stylo- ile başlayan üç kas (styloglossus – XII, stylohyoideus – VII,
  stylopharyngeus – IX) ve lig. stylohyoideum ile lig. stylomandibulare başlar.""",
  e=["os-temporale", "mm-suprahyoidei"]),

Q("f", KF, "İç kulak hangi kemiğin hangi bölümünde yer alır?",
  "Os temporale – pars petrosa",
  ["Os temporale – pars squamosa", "Os temporale – pars tympanica", "Os sphenoidale – ala major", "Os occipitale – pars basilaris"],
  """Pars petrosa (piramit) vücudun en sert kemik bölgesidir; içinde koklea, vestibül ve
  semisirküler kanallar bulunur. Orta kulak boşluğu da pars petrosa ile pars tympanica
  arasındadır.""",
  e=["os-temporale", "auris-interna"]),

Q("f", KF, "Bebeklerde en geç kapanan fontanel ve yaklaşık kapanma zamanı hangisidir?",
  "Fonticulus anterior – 18–24 ay",
  ["Fonticulus posterior – 18–24 ay", "Fonticulus anterior – 2–3 ay", "Fonticulus mastoideus – 3 yaş", "Fonticulus sphenoidalis – 5 yaş"],
  """Ön fontanel (bregma'daki eşkenar dörtgen açıklık) en büyük ve en geç (yaklaşık 18–24. ay)
  kapanandır. Arka fontanel 2–3. ayda, sfenoid fontanel yaklaşık 6. ayda, mastoid fontanel
  6–18. aylarda kapanır. Ön fontanelin çökük olması dehidratasyonu, kabarık olması kafa içi
  basınç artışını düşündürür.""",
  e=["os-frontale", "os-parietale"]),

Q("f", KF, "Bregma hangi suturaların kesiştiği noktadır?",
  "Sutura coronalis ve sutura sagittalis",
  ["Sutura sagittalis ve sutura lambdoidea", "Sutura coronalis ve sutura squamosa", "Sutura lambdoidea ve sutura occipitomastoidea", "Sutura frontalis ve sutura coronalis"],
  """Bregma, ön fontanelin yerinde koronal ve sagittal suturaların kesişimidir. Lambda ise
  sagittal ve lambdoid suturaların kesiştiği, arka fontanelin bulunduğu noktadır.""",
  e=["os-frontale", "os-parietale"]),

Q("tv", KF, """Yüzüne tenis topu çarpan hastada yukarı bakışta çift görme, göz küresinde çökme ve aynı
taraf yanak ile üst dudakta uyuşukluk var. En olası kırık hangisidir?""",
  "Orbita tabanı (maxilla) – blow-out kırığı",
  ["Orbita tavanı (os frontale)", "Orbita lateral duvarı (os zygomaticum)", "Canalis opticus", "Os nasale"],
  """Orbitaya künt travmada basınç en zayıf duvarlardan tabandan (maxilla) dışarı kırar. M. rectus
  inferior ve yağ dokusu sinus maxillaris'e sıkışır, yukarı bakış kısıtlanır. Tabandaki sulcus /
  canalis infraorbitalis'teki n. infraorbitalis yaralanınca yanak, alt kapak ve üst dudakta his
  kaybı olur. Medial duvar (lamina orbitalis ossis ethmoidalis) en ince duvardır ve o da sık kırılır.""",
  e=["maxilla", "os-ethmoidale", "mm-bulbi"]),

Q("f", KF, "Burun septumunun kemik bölümünü oluşturan yapılar hangileridir?",
  "Vomer ve os ethmoidale'nin lamina perpendicularis'i",
  ["Os nasale ve vomer", "Concha nasalis inferior ve os palatinum", "Os lacrimale ve os ethmoidale", "Maxilla'nın processus frontalis'i ve os nasale"],
  """Burun septumu arkada-aşağıda vomer, arkada-yukarıda lamina perpendicularis ossis ethmoidalis
  ve önde cartilago septi nasi'den oluşur. Septum deviasyonu çoğunlukla kıkırdak-kemik
  birleşim yerindedir.""",
  e=["vomer", "os-ethmoidale", "cavitas-nasi"]),

Q("f", KF, "Aşağıdakilerden hangisi ayrı bir kemiktir, os ethmoidale'nin bir parçası değildir?",
  "Concha nasalis inferior",
  ["Concha nasalis media", "Concha nasalis superior", "Lamina cribrosa", "Crista galli"],
  """Üst ve orta konkalar os ethmoidale'nin labirentinden uzanır. Alt konka ise kendi başına bir
  yüz kemiğidir ve maxilla, os lacrimale, os palatinum ve os ethmoidale ile eklemleşir.""",
  e=["concha-nasalis-inferior", "os-ethmoidale"]),

Q("f", KF, "Sert damağın (palatum durum) arka dörtte birlik bölümünü hangi kemik oluşturur?",
  "Os palatinum – lamina horizontalis",
  ["Maxilla – processus palatinus", "Vomer", "Os sphenoidale – processus pterygoideus", "Os palatinum – lamina perpendicularis"],
  """Sert damağın ön dörtte üçü maxilla'nın processus palatinus'u, arka dörtte biri os palatinum'un
  lamina horizontalis'i tarafından yapılır. İkisinin birleşimi sutura palatina transversa'dır.""",
  e=["os-palatinum", "maxilla"]),

Q("f", KF, "Fossa sacci lacrimalis'in oluşumuna katılan kemikler hangileridir?",
  "Os lacrimale ve maxilla'nın processus frontalis'i",
  ["Os nasale ve os frontale", "Os ethmoidale ve os sphenoidale", "Os zygomaticum ve maxilla", "Os palatinum ve os lacrimale"],
  """Gözyaşı kesesi orbitanın medial duvarının ön kısmındaki fossa sacci lacrimalis'te durur.
  Bu çukuru önde maxilla'nın processus frontalis'i (crista lacrimalis anterior), arkada os
  lacrimale (crista lacrimalis posterior) yapar. Kese aşağıda ductus nasolacrimalis ile alt
  meatusa açılır.""",
  e=["os-lacrimale", "maxilla", "apparatus-lacrimalis"]),

Q("f", KF, "Arcus zygomaticus hangi yapıların birleşmesiyle oluşur?",
  "Os zygomaticum'un processus temporalis'i ve os temporale'nin processus zygomaticus'u",
  ["Os zygomaticum'un processus frontalis'i ve os frontale",
   "Maxilla'nın processus zygomaticus'u ve os sphenoidale",
   "Os temporale'nin processus mastoideus'u ve os zygomaticum",
   "Os sphenoidale'nin ala major'u ve os temporale"],
  """Elmacık kemerini önde os zygomaticum'un processus temporalis'i, arkada os temporale'nin
  processus zygomaticus'u yapar. Alt kenarından m. masseter başlar; kemerin altından
  m. temporalis'in tendonu processus coronoideus'a uzanır.""",
  e=["os-zygomaticum", "os-temporale", "m-masseter"]),

Q("f", KF, "Condyli occipitales hangi kemikle eklem yapar?",
  "Atlas",
  ["Axis", "Os sphenoidale", "Os temporale", "Dens axis"],
  """Os occipitale'nin kondilleri atlasın massa lateralis'lerinin üst yüzleriyle articulatio
  atlantooccipitalis'i yapar. Bu eklemde 'evet' anlamında baş sallama (fleksiyon–ekstansiyon)
  gerçekleşir; 'hayır' hareketi ise atlantoaksiyel eklemdedir.""",
  e=["os-occipitale", "atlas"]),

Q("t", KF, "Foramen supraorbitale'den geçen sinir hangisidir ve hangi ana sinirden gelir?",
  "N. supraorbitalis – n. ophthalmicus (V1)",
  ["N. supratrochlearis – n. maxillaris (V2)", "N. infraorbitalis – n. maxillaris (V2)",
   "N. supraorbitalis – n. facialis", "N. zygomaticotemporalis – n. mandibularis (V3)"],
  """N. frontalis'in dalı olan n. supraorbitalis os frontale'deki foramen (incisura) supraorbitale'den
  çıkar ve alın ile saçlı derinin ön bölümünün duyusunu alır. Bu nokta trigeminal nevraljide
  V1 bası noktası olarak muayene edilir.""",
  e=["os-frontale", "n-trigeminus"]),

Q("f", KF, "Erişkinde kalıcı diş sayısı ve süt dişi sayısı sırasıyla hangisidir?",
  "32 ve 20",
  ["28 ve 20", "32 ve 24", "30 ve 20", "32 ve 16"],
  """Her yarım çenede kalıcı dişlenmede 2 kesici, 1 köpek, 2 küçük azı ve 3 büyük azı (toplam 32);
  süt dişlenmesinde 2 kesici, 1 köpek ve 2 azı (toplam 20) bulunur. Süt dişlerinde küçük azı yoktur.""",
  e=["dentes"]),

Q("f", KF, "Stapes'in tabanı (basis stapedis) nereye oturur?",
  "Fenestra vestibuli (oval pencere)",
  ["Fenestra cochleae (yuvarlak pencere)", "Membrana tympanica", "Promontorium", "Aditus ad antrum mastoideum"],
  """Stapes'in tabanı orta kulağın medial duvarındaki fenestra vestibuli'ye lig. anulare ile
  tutunur ve titreşimi perilenfe iletir. Otosklerozda bu bölgede kemik oluşumu stapesi sabitler
  ve iletim tipi işitme kaybı yapar. Fenestra cochleae ikincil timpan zarıyla kapalıdır.""",
  e=["ossicula-auditus", "auris-media"]),

# ------------------------------------------------------------------ Omurga
Q("f", OM, "Corpus vertebrae'si (omur gövdesi) olmayan omur hangisidir?",
  "Atlas (C1)",
  ["Axis (C2)", "Vertebra prominens (C7)", "Birinci torakal omur", "Beşinci lumbal omur"],
  """Atlas'ın gövdesi gelişim sırasında axis'e katılarak dens'i oluşturur. Atlas ön ve arka kemer
  ile iki massa lateralis'ten oluşan bir halkadır; dikensi çıkıntı yerine tuberculum posterius
  taşır.""",
  e=["atlas", "axis"]),

Q("t", OM, "A. vertebralis çoğunlukla hangi omurun foramen transversarium'una girerek yükselmeye başlar?",
  "C6",
  ["C7", "C5", "C4", "C1"],
  """A. subclavia'nın ilk dalı olan a. vertebralis tipik olarak C6'nın foramen transversarium'una
  girer, C6–C1 deliklerinden yükselir ve foramen magnum'dan kafa içine geçer. C7'nin
  foramen transversarium'undan genellikle yalnızca v. vertebralis geçer.""",
  e=["vertebrae-cervicales", "a-vertebralis"]),

Q("f", OM, "Ense bölgesinde en belirgin ele gelen dikensi çıkıntı hangi omura aittir?",
  "C7 (vertebra prominens)",
  ["C2 (axis)", "C5", "T4", "C1 (atlas)"],
  """C7'nin uzun, çatallanmamış processus spinosus'u boyun tabanında kolayca ele gelir ve omurları
  saymada başlangıç noktası olarak kullanılır. C2–C6'nın dikensi çıkıntıları kısa ve çatallıdır
  (bifid).""",
  e=["vertebrae-cervicales"]),

Q("f", OM, "Gövdesinde kaburga başı için eklem yüzü (fovea costalis) bulunan omurlar hangileridir?",
  "Torakal omurlar",
  ["Servikal omurlar", "Lumbal omurlar", "Sakral omurlar", "Koksigeal omurlar"],
  """Torakal omurların gövdelerinde kaburga başı, processus transversus'larında (T11–T12 hariç)
  kaburga tüberkülü için eklem yüzleri vardır. Gövdeleri kalp biçimli, dikensi çıkıntıları uzun
  ve aşağı eğiktir.""",
  e=["vertebrae-thoracicae", "costae"]),

Q("t", OM, "Processus mamillaris ve processus accessorius hangi omurlara özgüdür?",
  "Lumbal omurlar",
  ["Torakal omurlar", "Servikal omurlar", "Sakral omurlar", "Atlas ve axis"],
  """Lumbal omurlarda üst eklem çıkıntısının arka kenarında processus mamillaris, transvers
  çıkıntının kökünde processus accessorius bulunur; derin sırt kasları buralara tutunur. Gövdeleri
  böbrek biçimli ve iridir, foramen transversarium ve kaburga eklem yüzü yoktur.""",
  e=["vertebrae-lumbales", "mm-transversospinales"]),

Q("tv", OM, "Kaudal epidural anestezi uygulamasında iğne hangi açıklıktan girilir?",
  "Hiatus sacralis",
  ["Foramina sacralia anteriora", "Foramina sacralia posteriora", "Foramen ischiadicum majus", "Canalis obturatorius"],
  """S4–S5'in laminaları birleşmediğinden sakrumun arka yüzünde hiatus sacralis kalır. Her iki
  yanındaki cornua sacralia yol gösterir; iğne buradan canalis sacralis içindeki epidural aralığa
  ilerletilir.""",
  e=["os-sacrum"]),

Q("f", OM, "Pelvis girişinin (apertura pelvis superior) arka sınırını oluşturan yapı hangisidir?",
  "Promontorium ossis sacri",
  ["Os coccygis'in ucu", "Spina ischiadica", "Hiatus sacralis", "Crista iliaca"],
  """Pelvis girişi arkada promontorium, yanlarda linea arcuata ve pecten ossis pubis, önde symphysis
  pubica'nın üst kenarı ile çevrilidir. Obstetrik konjugat promontorium ile symphysis'in arka yüzü
  arasındaki en kısa uzaklıktır.""",
  e=["os-sacrum", "os-coxae"]),

Q("tv", OM, """45 yaşında erkek ağır kaldırma sonrası bele ve bacağın dış yüzüne, ayak sırtına ve
başparmağa yayılan ağrı ile başparmak dorsifleksiyonunda güçsüzlük tarifliyor. En olası tanı
hangisidir?""",
  "L4–L5 disk hernisi ile L5 kökü basısı",
  ["L3–L4 disk hernisi ile L4 kökü basısı", "L5–S1 disk hernisi ile S1 kökü basısı",
   "L1–L2 disk hernisi ile conus medullaris basısı", "S1–S2 disk hernisi ile S2 kökü basısı"],
  """Lomber disk hernileri çoğunlukla posterolateral olur ve bir alttaki kökü sıkıştırır: L4–L5
  hernisi L5 kökünü etkiler. L5: bacak dış yüzü, ayak sırtı, başparmak duyusu ve m. extensor
  hallucis longus gücü. S1: ayak dış kenarı, Aşil refleksi; L4: diz refleksi ve bacak iç yüzü.""",
  e=["vertebrae-lumbales", "discus-intervertebralis", "n-ischiadicus"]),

Q("f", OM, "Dens axis hangi bağ ile atlasın ön kemerine karşı tutulur?",
  "Lig. transversum atlantis",
  ["Lig. apicis dentis", "Ligg. alaria", "Lig. longitudinale anterius", "Lig. flavum"],
  """Lig. transversum atlantis (lig. cruciforme atlantis'in yatay kolu) dens'i arkadan sararak atlasın
  ön kemerine bastırır. Kopması (ör. romatoid artrit, Down sendromu) dens'in omuriliğe
  basmasına yol açabilir.""",
  e=["axis", "atlas", "ligg-columnae"]),

# ------------------------------------------------------------------ Göğüs kafesi
Q("fv", GK, "Göğüs muayenesinde kaburgaları saymak için referans alınan angulus sterni hangi kaburga kıkırdağının eklemleştiği düzeydedir?",
  "2. kaburga",
  ["1. kaburga", "3. kaburga", "4. kaburga", "7. kaburga"],
  """Angulus sterni (Louis açısı) manubrium ile corpus sterni'nin birleşim yeridir ve iki yanında
  2. kaburga kıkırdakları eklemleşir. Ön yüzde kolayca ele gelir; 2. kaburga bulunup aşağı
  doğru sayılır.""",
  e=["sternum", "costae", "cartilagines-costales"]),

Q("t", GK, "Angulus sterni'den geçen yatay düzlem (T4–T5) ile ilgili aşağıdakilerden hangisi yanlıştır?",
  "Özofagus bu düzeyde diyaframdan geçer.",
  ["Trakea bu düzeyde ikiye ayrılır.", "Arcus aortae bu düzlemde başlar ve biter.",
   "V. azygos bu düzeyde v. cava superior'a açılır.", "Üst ve alt mediastinumu ayırır."],
  """Angulus sterni düzlemi göğsün önemli bir işaretidir: üst/alt mediastinum sınırı, trakeanın
  bifurkasyonu, aort kemerinin başlangıç ve sonu, v. azygos'un VCS'ye açılması ve ductus
  thoracicus'un sola geçişi bu düzeydedir. Özofagus diyaframı T10 düzeyinde geçer.""",
  e=["sternum", "trachea", "aorta", "v-azygos"]),

Q("f", GK, "‘Costae fluctuantes’ (yüzen kaburgalar) hangileridir?",
  "11. ve 12. kaburgalar",
  ["1. ve 2. kaburgalar", "8., 9. ve 10. kaburgalar", "6. ve 7. kaburgalar", "10. ve 11. kaburgalar"],
  """1–7. kaburgalar sternuma doğrudan bağlanan gerçek kaburgalardır. 8–10. kaburgaların kıkırdakları
  bir üstteki kıkırdağa katılır (yalancı kaburgalar). 11–12. kaburgaların ön uçları serbesttir
  (yüzen kaburgalar).""",
  e=["costae", "cartilagines-costales"]),

Q("t", GK, "Birinci kaburgada tuberculum musculi scaleni anterioris'in arkasındaki olukta seyreden yapı hangisidir?",
  "A. subclavia",
  ["V. subclavia", "N. phrenicus", "Ductus thoracicus", "A. thoracica interna"],
  """M. scalenus anterior 1. kaburganın tüberkülüne tutunur. Tüberkülün önündeki olukta
  v. subclavia, arkasındaki olukta (sulcus arteriae subclaviae) a. subclavia ve plexus
  brachialis'in alt gövdesi bulunur. Arter ve pleksus skalen boşluktan, ven ise kasın önünden geçer.""",
  e=["costae", "a-subclavia", "mm-scaleni"]),

Q("tv", GK, "Torasentez yapılırken interkostal damar ve siniri korumak için iğne nereden ilerletilmelidir?",
  "Alttaki kaburganın üst kenarının hemen üzerinden",
  ["Üstteki kaburganın alt kenarının hemen altından", "İki kaburga arasının tam ortasından",
   "Angulus costae'nin medialinde sulcus costae içinden", "Kaburga kıkırdağının üzerinden"],
  """İnterkostal ven, arter ve sinir (yukarıdan aşağı VAN) kaburganın alt kenarındaki sulcus costae
  içinde seyreder. Bu nedenle iğne alttaki kaburganın üst kenarından geçirilir.""",
  e=["costae", "mm-intercostales", "n-intercostales"]),

Q("tv", GK, """Kolunu kaldırınca elinde uyuşma ve soğuma olan genç kadında boyun grafisinde servikal
kaburga görülüyor. Bu durumda en sık sıkışan yapı hangisidir?""",
  "Plexus brachialis'in alt gövdesi (C8–T1)",
  ["Plexus brachialis'in üst gövdesi (C5–C6)", "N. phrenicus", "V. jugularis interna", "N. accessorius"],
  """Servikal kaburga (C7'den) torasik çıkış sendromuna yol açar. Alt gövde (C8–T1) ve a. subclavia
  kaburga ya da fibröz bandı üzerinden geçerken sıkışır; elin ulnar kenarında parestezi,
  intrinsik kas güçsüzlüğü ve vasküler belirtiler olur.""",
  e=["costae", "vertebrae-cervicales", "plexus-brachialis", "a-subclavia"]),

Q("f", GK, "Processus xiphoideus en sık hangi omur düzeyine karşılık gelir?",
  "T9–T10",
  ["T4–T5", "T6–T7", "T12–L1", "L1–L2"],
  """Ksifosternal eklem yaklaşık T9 düzeyindedir. Xiphoid ileri yaşa kadar kıkırdak olarak kalabilir;
  linea alba ve diyaframın sternal parçası buraya tutunur.""",
  e=["sternum", "diaphragma"]),

# ------------------------------------------------------------------ Üst ekstremite
Q("f", UE, "Embriyonik dönemde kemikleşmeye ilk başlayan kemik hangisidir?",
  "Clavicula",
  ["Femur", "Humerus", "Mandibula", "Os parietale"],
  """Clavicula 5–6. haftada kemikleşmeye başlar; gövdesi membranöz (intramembranöz), uçları
  kıkırdak içi kemikleşir. Yetişkinde en sık kırılan kemiklerdendir.""",
  e=["clavicula"]),

Q("tv", UE, """Bisikletten düşen çocukta clavicula'nın orta ve dış üçte birlik bölümlerinin birleşiminden
kırık saptanıyor. Medial parçayı yukarı doğru çeken kas hangisidir?""",
  "M. sternocleidomastoideus",
  ["M. trapezius", "M. pectoralis major", "M. deltoideus", "M. subclavius"],
  """Kırıkta medial parça m. sternocleidomastoideus'un klavikular başıyla yukarı çekilir. Lateral
  parça kolun ağırlığıyla aşağı, m. pectoralis major ve m. latissimus dorsi ile içe çekilir; omuz
  düşük ve öne kaymış görünür.""",
  ["Lateral üçte bire tutunur; lateral parçayı yukarı tutmaya çalışır ama kolun ağırlığını yenemez.",
   "Lateral parçayı içe çeker.", "Lateral parçaya tutunur.", "Subklavyen damarları korur; parçayı yukarı çekmez."],
  e=["clavicula", "m-sternocleidomastoideus"]),

Q("t", UE, "Incisura scapulae'yi köprüleyen lig. transversum scapulae superius'un altından geçen yapı hangisidir?",
  "N. suprascapularis",
  ["A. suprascapularis", "N. axillaris", "N. dorsalis scapulae", "A. circumflexa scapulae"],
  """N. suprascapularis bağın altından, a. suprascapularis üstünden geçer. Bağın kalsifikasyonu veya
  çentikteki sıkışma m. supraspinatus ile m. infraspinatus'ta güçsüzlük ve atrofiye yol açar.""",
  e=["scapula", "m-supraspinatus", "m-infraspinatus"]),

Q("f", UE, "Aşağıdakilerden hangisi processus coracoideus'a tutunmaz?",
  "M. biceps brachii'nin uzun başı",
  ["M. pectoralis minor", "M. coracobrachialis", "M. biceps brachii'nin kısa başı", "Lig. coracoclaviculare"],
  """Biceps'in uzun başı tuberculum supraglenoidale'den başlar ve eklem kapsülü içinden geçer.
  Processus coracoideus'a m. pectoralis minor, m. coracobrachialis, biceps kısa başı ile
  coracoclavicular, coracoacromial ve coracohumeral bağlar tutunur.""",
  e=["scapula", "m-biceps-brachii", "m-pectoralis-minor", "m-coracobrachialis"]),

Q("tv", UE, """Omuz üzerine düşen yaşlı kadında collum chirurgicum humeri kırığı var. Deltoid bölgede
düzleşme ve omuz dış yüzünde küçük bir alanda his kaybı gelişiyor. Yaralanan sinir hangisidir?""",
  "N. axillaris",
  ["N. radialis", "N. suprascapularis", "N. musculocutaneus", "N. thoracicus longus"],
  """N. axillaris a. circumflexa humeri posterior ile birlikte boşluk kuadrangülerden geçip collum
  chirurgicum'u arkadan sarar. Kırıkta m. deltoideus ve m. teres minor güçsüzleşir; 'polis
  arması' bölgesinde (n. cutaneus brachii lateralis superior) his kaybı olur.""",
  e=["humerus", "n-axillaris", "m-deltoideus"]),

Q("tv", UE, """Humerus cisminin ortasından kırık sonrası hasta el bileğini ve parmaklarını kaldıramıyor
(düşük el). Kırık hattında yaralanan sinir ve ona eşlik eden arter hangisidir?""",
  "N. radialis – a. profunda brachii",
  ["N. ulnaris – a. collateralis ulnaris superior", "N. medianus – a. brachialis",
   "N. axillaris – a. circumflexa humeri posterior", "N. musculocutaneus – a. brachialis"],
  """N. radialis ve a. profunda brachii humerusun arka yüzündeki sulcus nervi radialis'te kemiğe
  sıkıca yaslanır. Cisim kırıklarında el bileği ve parmak ekstansörleri felç olur. Triceps'e
  giden dallar daha yukarıdan çıktığından triceps genellikle korunur.""",
  e=["humerus", "n-radialis"]),

Q("tv", UE, """7 yaşında çocuk düşme sonrası suprakondiler humerus kırığı ile getiriliyor. Saatler
sonra önkolda şiddetli ağrı, parmakların pasif ekstansiyonunda ağrı artışı ve radial nabız
alınamaması gelişiyor. Hasar gören damar hangisidir?""",
  "A. brachialis",
  ["A. profunda brachii", "A. radialis'in başlangıcı", "A. collateralis ulnaris inferior", "A. axillaris"],
  """Suprakondiler kırıkta proksimal parçanın keskin ucu a. brachialis'e ve n. medianus'a bası
  yapar. Önkol fleksör kompartmanı iskemiye girer; tedavi edilmezse Volkmann iskemik kontraktürü
  gelişir.""",
  e=["humerus", "a-brachialis", "n-medianus"]),

Q("f", UE, "Epicondylus medialis humeri'nin arkasındaki olukta seyreden sinir hangisidir?",
  "N. ulnaris",
  ["N. medianus", "N. radialis", "N. musculocutaneus", "N. cutaneus antebrachii medialis"],
  """N. ulnaris epicondylus medialis'in arkasındaki sulcus nervi ulnaris'te yüzeyeldir; dirseğin
  çarpmasıyla ele yayılan elektriklenme ('funny bone') buradan kaynaklanır. Bu bölgedeki
  sıkışmaya kübital tünel sendromu denir.""",
  e=["humerus", "n-ulnaris"]),

Q("t", UE, "Tuberculum minus humeri'ye tutunan kas hangisidir?",
  "M. subscapularis",
  ["M. supraspinatus", "M. infraspinatus", "M. teres minor", "M. teres major"],
  """Rotator manşet kaslarından supraspinatus, infraspinatus ve teres minor tuberculum majus'a;
  subscapularis ise tek başına tuberculum minus'a tutunur ve kolu içe döndürür.""",
  e=["humerus", "m-subscapularis"]),

Q("t", UE, "Sulcus intertubercularis'in tabanına tutunan kas hangisidir?",
  "M. latissimus dorsi",
  ["M. pectoralis major", "M. teres major", "M. deltoideus", "M. coracobrachialis"],
  """Sulcus intertubercularis'in dış dudağına m. pectoralis major, iç dudağına m. teres major,
  tabanına m. latissimus dorsi tutunur ('iki major arasında bir hanım'). Olukta biceps uzun
  başının tendonu ve sinovyal kılıfı bulunur.""",
  e=["humerus", "m-latissimus-dorsi", "m-pectoralis-major", "m-teres-major"]),

Q("fv", UE, """2 yaşında bir çocuk, annesi elinden tutup sertçe çektikten sonra kolunu kullanmıyor ve
önkolunu pronasyonda tutuyor. Radius başı hangi bağın içinden kaymıştır?""",
  "Lig. anulare radii",
  ["Lig. collaterale radiale", "Lig. collaterale ulnare", "Membrana interossea antebrachii", "Lig. quadratum"],
  """'Dadı dirseği' (radius başı subluksasyonu) küçük çocuklarda radius başı henüz küçük olduğundan
  görülür; baş, onu ulnanın incisura radialis'ine karşı tutan lig. anulare radii'den kayar.
  Supinasyon ve fleksiyonla kolayca yerine oturtulur.""",
  e=["radius", "artt-radioulnares", "art-cubiti"]),

Q("tv", UE, """Elinin üzerine düşen yaşlı kadında el bileğinde 'çatal sırtı' görünümü var. Grafide
radiusun distal ucunun kırık olduğu ve distal parçanın dorsale yer değiştirdiği görülüyor.
Bu kırığın adı nedir?""",
  "Colles kırığı",
  ["Smith kırığı", "Barton kırığı", "Monteggia kırığı", "Galeazzi kırığı"],
  """Colles kırığında distal radius parçası dorsale ve radiale yer değiştirir; yandan bakıldığında
  çatal sırtı görünümü oluşur. Smith kırığı bunun tersidir (distal parça volare). Monteggia ulna
  kırığı + radius başı çıkığı, Galeazzi radius kırığı + distal radioulnar çıkıktır.""",
  e=["radius", "art-radiocarpalis"]),

Q("f", UE, "Tuberositas ulnae'ye tutunan kas hangisidir?",
  "M. brachialis",
  ["M. biceps brachii", "M. triceps brachii", "M. anconeus", "M. supinator"],
  """M. brachialis humerusun ön yüzünün alt yarısından başlar, processus coronoideus ve tuberositas
  ulnae'ye tutunur; dirseğin asıl fleksörüdür. Biceps ise tuberositas radii'ye tutunur.""",
  e=["ulna", "m-brachialis"]),

# ------------------------------------------------------------------ El kemikleri
Q("tv", EL, """Elinin üzerine düşen 22 yaşındaki erkekte enfiyecinin çukurunda (tabakiyer) hassasiyet var;
ilk grafiler normal. İki hafta sonra kırık hattı belirginleşiyor. Bu kemiğin kırığında en çok
korkulan komplikasyon nedir?""",
  "Proksimal parçada avasküler nekroz",
  ["Distal parçada avasküler nekroz", "N. ulnaris felci", "Karpal tünel sendromu", "A. radialis yırtılması"],
  """En sık kırılan karpal kemik os scaphoideum'dur. Besleyici damarlar kemiğe çoğunlukla distalden
  girer; bel kırıklarında proksimal parçanın kanlanması bozulur ve avasküler nekroz, kaynamama
  gelişebilir. Tabakiyerin tabanında scaphoid ve trapezium vardır.""",
  e=["os-scaphoideum", "ossa-carpi", "a-radialis"]),

Q("t", EL, "En sık çıkığa uğrayan karpal kemik ve öne çıktığında bası yapabileceği sinir hangisidir?",
  "Os lunatum – n. medianus",
  ["Os scaphoideum – n. radialis", "Os pisiforme – n. ulnaris", "Os capitatum – n. medianus", "Os hamatum – n. ulnaris"],
  """Os lunatum volare çıkabilir ve karpal tünele girerek n. medianus'a bası yapar. Lunatumun
  avasküler nekrozu Kienböck hastalığı olarak bilinir.""",
  e=["os-lunatum", "n-medianus"]),

Q("f", EL, "Os pisiforme hangi kasın tendonu içinde gelişen sesamoid bir kemiktir?",
  "M. flexor carpi ulnaris",
  ["M. flexor carpi radialis", "M. palmaris longus", "M. abductor digiti minimi", "M. extensor carpi ulnaris"],
  """Os pisiforme m. flexor carpi ulnaris tendonu içinde yer alır ve os triquetrum ile eklem yapar.
  Lig. pisohamatum ve lig. pisometacarpale ile kasın kuvvetini hamatum ve 5. metakarpa iletir;
  m. abductor digiti minimi buradan başlar.""",
  e=["os-pisiforme", "m-flexor-carpi-ulnaris"]),

Q("tv", EL, """Golf oynarken sopası yere çarpan hastada hypothenar bölgede ağrı, 4–5. parmaklarda uyuşma
ve parmakları açıp kapamada güçsüzlük var. Kırılan kemik çıkıntısı hangisidir?""",
  "Hamulus ossis hamati",
  ["Tuberculum ossis trapezii", "Tuberculum ossis scaphoidei", "Processus styloideus ulnae", "Os pisiforme"],
  """Hamatumun çengeli Guyon kanalının (canalis ulnaris) dış duvarını oluşturur. Kırığında kanaldaki
  n. ulnaris ve a. ulnaris etkilenebilir; 4–5. parmak palmar yüzünde uyuşma ve interosseöz kas
  güçsüzlüğü olur.""",
  e=["os-hamatum", "n-ulnaris"]),

Q("f", EL, "Os trapezium hangi metakarp kemiği ile eyer tipi eklem yapar?",
  "1. metakarp (başparmak)",
  ["2. metakarp", "3. metakarp", "4. metakarp", "5. metakarp"],
  """Başparmağın karpometakarpal eklemi (trapezium–1. metakarp) eyer tipidir; oppozisyon dahil geniş
  hareket sağlar ve ileri yaşta artrozun sık görüldüğü yerdir.""",
  e=["os-trapezium", "ossa-metacarpi", "artt-manus"]),

Q("f", EL, "En büyük ve ilk kemikleşen karpal kemik hangisidir?",
  "Os capitatum",
  ["Os hamatum", "Os scaphoideum", "Os lunatum", "Os trapezium"],
  """Os capitatum karpal kemiklerin en büyüğüdür ve genellikle ilk yılda ilk kemikleşen karpaldir.
  3. metakarp ile eklem yapar; el bileğinin hareket ekseni çoğunlukla başından geçer.""",
  e=["os-capitatum", "ossa-carpi"]),

Q("fv", EL, "Duvara yumruk atan genç erkekte serçe parmağı eklem kabartısı düşmüş. En olası kırık hangisidir?",
  "5. metakarp boynu kırığı (boksör kırığı)",
  ["1. metakarp tabanı kırığı (Bennett kırığı)", "Os scaphoideum kırığı", "5. parmak distal falanks kırığı", "Hamulus ossis hamati kırığı"],
  """Kapalı yumrukla sert yüzeye vurmada en sık 5. metakarpın boynu kırılır; baş palmara açılanır ve
  eklem kabartısı kaybolur. Bennett kırığı 1. metakarp tabanının eklem içi kırığıdır.""",
  e=["ossa-metacarpi"]),

Q("f", EL, "El bileğinde proksimal sıra karpal kemiklerin dıştan (radial) içe (ulnar) doğru sırası hangisidir?",
  "Scaphoideum, lunatum, triquetrum, pisiforme",
  ["Lunatum, scaphoideum, triquetrum, pisiforme", "Trapezium, trapezoideum, capitatum, hamatum",
   "Scaphoideum, triquetrum, lunatum, pisiforme", "Pisiforme, triquetrum, lunatum, scaphoideum"],
  """Proksimal sıra: scaphoideum, lunatum, triquetrum, pisiforme. Distal sıra: trapezium, trapezoideum,
  capitatum, hamatum. Radiokarpal eklemi radius ve diskle scaphoideum, lunatum ve triquetrum yapar.""",
  e=["ossa-carpi"]),

# ------------------------------------------------------------------ Alt ekstremite
Q("f", AE, "Os coxae'yı oluşturan üç kemik nerede birleşir?",
  "Acetabulum'da",
  ["Symphysis pubica'da", "Foramen obturatum'da", "Incisura ischiadica major'da", "Crista iliaca'da"],
  """Os ilium, os ischii ve os pubis ergenlikte acetabulum'daki Y biçimli kıkırdakta kaynaşır.
  Acetabulum'un yaklaşık 2/5'ini ilium, 2/5'ini ischium, 1/5'ini pubis yapar.""",
  e=["os-coxae", "art-coxae"]),

Q("t", AE, "Canalis obturatorius'tan geçen yapılar hangileridir?",
  "N., a. ve v. obturatoria",
  ["N. femoralis ve a. femoralis", "N. pudendus ve a. pudenda interna", "N. ischiadicus ve a. glutea inferior", "N. cutaneus femoris lateralis"],
  """Foramen obturatum membrana obturatoria ile kapalıdır; yalnız üst kısmında canalis obturatorius
  kalır. Buradan n. obturatorius ile a. ve v. obturatoria uyluğun iç kompartmanına geçer.""",
  e=["os-coxae", "n-obturatorius"]),

Q("t", AE, "Foramen ischiadicum majus'tan pelvisten çıkıp foramen ischiadicum minus'tan perineye giren sinir hangisidir?",
  "N. pudendus",
  ["N. ischiadicus", "N. gluteus superior", "N. cutaneus femoris posterior", "N. obturatorius"],
  """N. pudendus, a. pudenda interna ve m. obturatorius internus'a giden sinir büyük siyatik delikten
  çıkar, spina ischiadica / lig. sacrospinale'yi dolanarak küçük siyatik delikten fossa
  ischioanalis'e ve Alcock kanalına girer. Pudendal blokta spina ischiadica yol göstericidir.""",
  e=["os-coxae", "n-pudendus", "ligg-pelvis"]),

Q("tv", AE, """Evde düşen 78 yaşındaki kadının sağ bacağı kısalmış ve dışa dönük. Grafide subkapital
femur boynu kırığı görülüyor. Bu kırıkta caput femoris'in avasküler nekrozundan en çok hangi
arterin hasarı sorumludur?""",
  "A. circumflexa femoris medialis",
  ["A. circumflexa femoris lateralis", "A. lig. capitis femoris", "A. glutea superior", "A. obturatoria"],
  """Femur başının asıl beslenmesi a. circumflexa femoris medialis'in boyun boyunca yükselen
  retinakular dallarından olur. Kırıkta bu damarlar yırtılır. Lig. capitis femoris içindeki
  arter (a. obturatoria'dan) erişkinde yetersizdir.""",
  e=["femur", "art-coxae", "a-femoralis"]),

Q("f", AE, "Trochanter minor'a tutunan kas hangisidir?",
  "M. iliopsoas",
  ["M. gluteus medius", "M. piriformis", "M. obturatorius externus", "M. quadratus femoris"],
  """M. psoas major ve m. iliacus ortak tendonla trochanter minor'a tutunur ve kalçanın en güçlü
  fleksörüdür. Gluteus medius/minimus ve piriformis trochanter major'a, obturatorius externus
  fossa trochanterica'ya tutunur.""",
  e=["femur", "m-iliopsoas"]),

Q("fv", AE, """Genç bir kadın voleybol oynarken dizinin dönmesi sonrası patellasının dışa çıktığını
söylüyor. Patellanın laterale çıkmasına karşı en önemli dinamik engel hangisidir?""",
  "M. vastus medialis'in alt (oblik) lifleri",
  ["M. vastus lateralis", "Tractus iliotibialis", "M. biceps femoris", "M. rectus femoris"],
  """Quadriceps'in çekme hattı ile lig. patellae arasındaki açı (Q açısı) patellayı dışa çekmeye
  eğilimlidir. Vastus medialis'in alt yatay lifleri patellayı içe çeker; femurun belirgin lateral
  kondili de kemik engeli oluşturur.""",
  e=["patella", "m-quadriceps-femoris", "art-genus"]),

Q("tv", AE, """Futbolda bacağının dış yanına darbe alan oyuncuda fibula boynu kırığı saptanıyor. Hastada
yürürken ayak ucunun yere sürtünmesi ve ayak sırtında his kaybı var. Yaralanan sinir hangisidir?""",
  "N. fibularis communis",
  ["N. tibialis", "N. saphenus", "N. suralis", "N. femoralis"],
  """N. fibularis communis fibula boynunu dıştan sararak yüzeyel seyreder. Yaralanmasında ön ve lateral
  kompartman kasları felç olur: düşük ayak, stepaj yürüyüşü ve ayak sırtı ile bacak dış yüzünde
  his kaybı görülür.""",
  e=["fibula", "n-fibularis-communis"]),

Q("fv", AE, "13 yaşında futbol oynayan erkek çocukta diz altında ağrılı, ele gelen bir şişlik var. Osgood–Schlatter hastalığı hangi yapıyı etkiler?",
  "Tuberositas tibiae",
  ["Tuberculum intercondylare", "Epicondylus lateralis femoris", "Caput fibulae", "Malleolus medialis"],
  """Osgood–Schlatter, hızlı büyüme döneminde lig. patellae'nin tuberositas tibiae apofizini tekrarlayan
  çekmesine bağlı apofizittir. Diz ekstansörlerinin kuvveti bu çıkıntı üzerinden tibiaya iletilir.""",
  e=["tibia", "m-quadriceps-femoris"]),

Q("t", AE, "Malleolus lateralis için aşağıdakilerden hangisi doğrudur?",
  "Malleolus medialis'ten daha aşağıda ve daha arkadadır.",
  ["Tibianın distal ucudur.", "Malleolus medialis'ten daha yukarıdadır.",
   "Arkasındaki oluktan m. tibialis posterior tendonu geçer.", "Talus ile eklem yapmaz."],
  """Malleolus lateralis fibulanın alt ucudur; medial malleolustan yaklaşık 1 cm daha aşağıda ve
  arkadadır. Arkasındaki oluktan m. fibularis longus ve brevis tendonları geçer. Talusun lateral
  yüzü ile eklem yaparak ayak bileği çatalının dış kolunu oluşturur.""",
  e=["fibula", "art-talocruralis"]),

# ------------------------------------------------------------------ Ayak kemikleri
Q("t", AY, "Hiçbir kasın tutunmadığı tarsal kemik hangisidir?",
  "Talus",
  ["Calcaneus", "Os naviculare", "Os cuboideum", "Os cuneiforme mediale"],
  """Talus'un yüzeyinin büyük kısmı eklem kıkırdağıyla kaplıdır ve hiçbir kas tutunmaz. Kanlanması
  sınırlı ve geriye doğru olduğundan boyun kırıklarında gövdenin avasküler nekrozu sıktır.""",
  e=["talus"]),

Q("f", AY, "Sustentaculum tali'nin alt yüzündeki oluktan geçen tendon hangisidir?",
  "M. flexor hallucis longus",
  ["M. flexor digitorum longus", "M. tibialis posterior", "M. fibularis longus", "M. tibialis anterior"],
  """Calcaneus'un iç yüzündeki raf benzeri çıkıntı (sustentaculum tali) talusu destekler. Alt
  yüzündeki sulcus tendinis musculi flexoris hallucis longi'den FHL tendonu geçer; FDL tendonu
  ise rafın iç kenarına yakın seyreder.""",
  e=["calcaneus", "m-flexor-hallucis-longus"]),

Q("t", AY, "Tuberositas ossis navicularis'e tutunan başlıca kas hangisidir?",
  "M. tibialis posterior",
  ["M. tibialis anterior", "M. fibularis longus", "M. flexor digitorum longus", "M. extensor hallucis longus"],
  """M. tibialis posterior'un ana tendonu naviküler tüberoziteye, ek uzantıları diğer tarsal ve
  metatarsal kemiklere tutunur. Ayağın en güçlü invertörüdür ve medial longitudinal kavsi destekler;
  disfonksiyonu edinsel düztabanın sık nedenidir.""",
  e=["os-naviculare", "m-tibialis-posterior"]),

Q("t", AY, "Os cuboideum'un plantar yüzündeki oluktan geçen tendon hangisidir?",
  "M. fibularis longus",
  ["M. fibularis brevis", "M. flexor hallucis longus", "M. tibialis posterior", "M. abductor digiti minimi"],
  """M. fibularis longus tendonu kuboidin plantar oluğundan ayak tabanını çaprazlayarak medial
  kuneiform ve 1. metatarsın tabanına tutunur; ayağın transvers kavsini destekler ve eversiyon yapar.""",
  e=["os-cuboideum", "m-fibularis-longus"]),

Q("fv", AY, """Basketbolda ayağı içe burkulan oyuncunun ayak dış kenarında ağrı var; grafide 5. metatarsın
tabanında avülsiyon kırığı görülüyor. Kemik parçasını koparan kas hangisidir?""",
  "M. fibularis brevis",
  ["M. fibularis longus", "M. fibularis tertius", "M. abductor digiti minimi", "M. tibialis anterior"],
  """M. fibularis brevis 5. metatarsın tuberositas'ına tutunur. Ani inversiyonda kasın kasılmasıyla
  tüberozite kopar (avülsiyon kırığı). Daha distaldeki metafiz-diyafiz bileşkesi kırığı (Jones
  kırığı) ise kaynama sorunlarıyla bilinir.""",
  e=["ossa-metatarsi", "m-fibularis-brevis"]),

Q("f", AY, "Ayağın medial longitudinal kavsinin en yüksek noktasında ve 'kilit taşı' konumunda bulunan kemik hangisidir?",
  "Talus başı",
  ["Os cuboideum", "Calcaneus'un tuber'i", "5. metatarsın tabanı", "Os cuneiforme laterale"],
  """Medial longitudinal kavsi calcaneus, talus, naviküler, üç kuneiform ve medial üç metatars oluşturur.
  Talus başı kavsin tepesinde kilit taşı gibidir ve altta lig. calcaneonaviculare plantare (yay bağı)
  tarafından desteklenir. Lateral kavisin kilit taşı ise kuboiddir.""",
  e=["talus", "artt-pedis"]),
]

write("skeletal", questions)
