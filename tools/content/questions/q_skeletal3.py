"""Skeletal questions, third set: basic level (names, counts, parts), more
faculty questions on landmarks and bone structure and new TUS points."""
from qcommon import Q

KAF = "Kafatası (Cranium)"
OMR = "Omurga (Columna vertebralis)"
GKF = "Göğüs kafesi (Thorax)"
UST = "Üst ekstremite kemikleri"
ELK = "El kemikleri"
ALT = "Alt ekstremite kemikleri"
AYK = "Ayak kemikleri"
GEN = "Genel yapılar"

questions = [
# ------------------------------------------------------------------ temel: genel
Q("b", GEN, "Erişkin insan iskeletinde yaklaşık kaç kemik bulunur?",
  "206", ["186", "226", "256", "300"],
  """Erişkin iskeleti yaklaşık 206 kemikten oluşur: 80'i eksen iskeletinde, 126'sı ekstremite iskeletindedir.
  Yenidoğanda henüz kaynaşmamış parçalar nedeniyle sayı 270–300 civarındadır.""",
  e=["iskelet-genel"]),

Q("b", GEN, "Vücudun en uzun ve en güçlü kemiği hangisidir?",
  "Femur", ["Tibia", "Humerus", "Fibula", "Os coxae"],
  """Femur (uyluk kemiği) vücudun en uzun, en ağır ve en güçlü kemiğidir; boyun yaklaşık dörtte biri kadardır.""",
  e=["femur"]),

Q("b", GEN, "Vücudun en küçük kemiği hangisidir?",
  "Stapes (üzengi kemiği)", ["Incus (örs)", "Malleus (çekiç)", "Os pisiforme", "Os lacrimale"],
  """Orta kulaktaki üç kemikçikten stapes vücudun en küçük kemiğidir; tabanı oval pencereye oturur.""",
  e=["ossicula-auditus"]),

Q("b", GEN, "Kemiğin dış yüzünü örten, damar ve sinirden zengin zar hangisidir?",
  "Periost", ["Endost", "Perikondriyum", "Sinovyal zar", "Fasya"],
  """Periost kemiğin dış yüzünü örter; iç katmanındaki hücreler kemiğin kalınlaşmasını ve kırık iyileşmesini sağlar.
  Eklem yüzlerinde periost yoktur, buraları hiyalin kıkırdak örter. Endost kemik iliği boşluğunu döşer.""",
  e=["os-structura"]),

Q("b", GEN, "Uzun bir kemiğin gövde kısmına ne ad verilir?",
  "Diafiz", ["Epifiz", "Metafiz", "Apofiz", "Epifiz plağı"],
  """Uzun kemiğin gövdesi diafiz, uçları epifiz, ikisi arasındaki büyüme bölgesi metafizdir.
  Diafizin içinde kemik iliğini barındıran cavitas medullaris bulunur.""",
  e=["os-structura"]),

Q("b", GEN, "Kemiği yıkan (rezorbe eden) hücre hangisidir?",
  "Osteoklast", ["Osteoblast", "Osteosit", "Kondrosit", "Fibroblast"],
  """Osteoklastlar monosit kökenli, çok çekirdekli hücrelerdir ve kemik dokusunu yıkar. Osteoblastlar yeni kemik yapar,
  osteositler ise kemik içine gömülmüş olgun hücrelerdir.""",
  e=["os-structura"]),

Q("b", GEN, "Kan hücrelerinin yapıldığı doku hangisidir?",
  "Kırmızı kemik iliği", ["Sarı kemik iliği", "Periost", "Kompakt kemik", "Eklem kıkırdağı"],
  """Kan yapımı kırmızı kemik iliğinde olur. Erişkinde kırmızı ilik başlıca yassı kemiklerde (sternum, kaburgalar,
  kalça kemiği, omurlar) bulunur; uzun kemiklerin gövdesindeki ilik yağdan zengin sarı iliğe dönüşür.""",
  e=["iskelet-genel"]),

Q("b", GEN, "Uzun kemikler boyca nerede uzar?",
  "Epifiz plağında (büyüme kıkırdağı)", ["Periostta", "Diafizin ortasında", "Eklem kıkırdağında", "Endostta"],
  """Boyca uzama metafizdeki epifiz plağında kıkırdak hücrelerinin çoğalıp kemikleşmesiyle olur; plak ergenlik
  sonunda kapanır. Enine büyüme ise periosttan yeni kemik eklenmesiyle gerçekleşir.""",
  e=["os-structura"]),

Q("b", GEN, "Aşağıdakilerden hangisi eksen iskeletine (skeleton axiale) ait bir kemiktir?",
  "Sternum", ["Clavicula", "Scapula", "Os coxae", "Humerus"],
  """Eksen iskeleti kafatası, omurga ve göğüs kafesinden (sternum ve kaburgalar) oluşur. Klavikula ve skapula omuz
  kuşağının, os coxae pelvis kuşağının, humerus serbest üst ekstremitenin kemiğidir.""",
  e=["iskelet-genel"]),

Q("b", GEN, "Aşağıdakilerden hangisi yassı kemik örneğidir?",
  "Os parietale", ["Femur", "Os capitatum", "Vertebra", "Os metacarpale"],
  """Yassı kemikler ince ve geniştir (kafatası tavanı, sternum, kaburgalar, skapula). Femur ve metakarplar uzun,
  kapitatum kısa, omurlar düzensiz kemiklerdir.""",
  e=["iskelet-genel", "os-parietale"]),

Q("b", GEN, "Aşağıdakilerden hangisi sesamoid bir kemik değildir?",
  "Os lunatum", ["Patella", "Os pisiforme", "Fabella", "Ayak başparmağı sesamoidi"],
  """Sesamoid kemikler tendon içinde gelişir: patella, pisiform, başparmak ve ayak başparmağı MP eklemlerinin altındaki
  sesamoidler ile bazı kişilerde fabella. Lunatum ise proksimal karpal sıradaki kısa kemiktir.""",
  e=["ossa-sesamoidea"]),

# ------------------------------------------------------------------ temel: kafatası
Q("b", KAF, "Alnı ve göz çukurlarının tavanını oluşturan kemik hangisidir?",
  "Os frontale", ["Os parietale", "Os sphenoidale", "Os ethmoidale", "Os zygomaticum"],
  """Os frontale dikey pars squamosa ile alnı, yatay pars orbitalis ile orbitaların tavanını ve ön kafa çukurunun
  tabanını oluşturur.""",
  e=["os-frontale"]),

Q("b", KAF, "Kafatası kemiklerinden sinovyal eklemle hareket eden tek kemik hangisidir?",
  "Mandibula", ["Maxilla", "Os zygomaticum", "Os nasale", "Vomer"],
  """Kafatası kemikleri dikişlerle sıkıca birleşir; tek hareketli eklem mandibula ile temporal kemik arasındaki çene
  eklemidir (art. temporomandibularis).""",
  e=["mandibula", "cranium"]),

Q("b", KAF, "Yenidoğanda kafatası kemikleri arasında kalan, kemikleşmemiş zar alanlarına ne ad verilir?",
  "Fontanel (bıngıldak)", ["Sutura (dikiş)", "Sinüs", "Foramen", "Fissür"],
  """Fontaneller dikişlerin kesiştiği yerlerdeki zarlı alanlardır; doğumda başın kalıplanmasını ve beynin büyümesini
  sağlar. En büyüğü ön fontaneldir.""",
  e=["suturae-fonticuli"]),

Q("b", KAF, "Sutura sagittalis hangi kemikler arasındadır?",
  "İki os parietale arasında", ["Os frontale ile os parietale", "Os parietale ile os occipitale",
   "Os parietale ile os temporale", "İki os frontale yarımı arasında"],
  """Sutura sagittalis iki parietal kemiği orta hatta birleştirir. Koronal dikiş frontal–parietal, lambdoid dikiş
  parietal–oksipital, skuamöz dikiş parietal–temporal kemikler arasındadır.""",
  e=["suturae-fonticuli", "os-parietale"]),

Q("b", KAF, "Göz çukurunun (orbita) oluşumuna kaç kemik katılır?",
  "7", ["5", "6", "8", "9"],
  """Orbitayı frontal, zygomatik, maksilla, sfenoid, etmoid, lakrimal ve palatin kemikler olmak üzere yedi kemik
  oluşturur.""",
  e=["orbita"]),

# ------------------------------------------------------------------ temel: omurga ve göğüs
Q("b", OMR, "Omurgada kaç boyun (servikal) omuru bulunur?",
  "7", ["5", "6", "8", "12"],
  """Omurga 7 servikal, 12 torakal, 5 lomber, 5 sakral ve 3–5 koksigeal omurdan oluşur.""",
  e=["columna-vertebralis", "vertebrae-cervicales"]),

Q("b", OMR, "Birinci boyun omurunun (C1) özel adı nedir?",
  "Atlas", ["Axis", "Vertebra prominens", "Dens", "Promontorium"],
  """C1 atlas, C2 axis, C7 vertebra prominens olarak adlandırılır. Atlas'ın gövdesi ve diken çıkıntısı yoktur.""",
  e=["atlas"]),

Q("b", OMR, "Sakrum kaç omurun kaynaşmasıyla oluşur?",
  "5", ["3", "4", "7", "12"],
  """Beş sakral omur kaynaşarak üçgen biçimli sakrumu oluşturur; altındaki 3–5 koksigeal omur da koksiksi yapar.""",
  e=["os-sacrum"]),

Q("b", OMR, "Bebek başını dik tutmaya başladığında omurgada hangi eğrilik gelişir?",
  "Servikal lordoz", ["Torakal kifoz", "Lomber lordoz", "Sakral kifoz", "Skolyoz"],
  """Fetüste omurga tek bir C şeklindedir (birincil kifoz). Baş tutulmaya başlayınca servikal lordoz, oturma ve
  yürümeyle lomber lordoz (ikincil eğrilikler) gelişir.""",
  e=["columna-vertebralis"]),

Q("b", GKF, "Göğüs kafesinde kaç çift kaburga bulunur?",
  "12 çift", ["10 çift", "11 çift", "13 çift", "24 çift"],
  """İnsanda 12 çift (24) kaburga vardır: 7 çift gerçek, 3 çift yalancı ve 2 çift yüzen kaburga.""",
  e=["costae"]),

Q("b", GKF, "Kendi kıkırdağıyla doğrudan sternuma bağlanan 'gerçek kaburgalar' hangileridir?",
  "1.–7. kaburgalar", ["1.–10. kaburgalar", "8.–10. kaburgalar", "11.–12. kaburgalar", "1.–12. kaburgalar"],
  """Gerçek kaburgalar (costae verae) 1.–7. kaburgalardır. 8.–10. kaburgalar kıkırdaklarıyla üstteki kıkırdağa
  bağlanır (yalancı kaburgalar), 11.–12. kaburgaların ön ucu serbesttir (yüzen kaburgalar).""",
  e=["costae", "costae-atypicae"]),

Q("b", GKF, "Sternumun üç bölümü hangileridir?",
  "Manubrium, corpus ve processus xiphoideus",
  ["Manubrium, angulus ve corpus", "Corpus, processus xiphoideus ve incisura jugularis",
   "Manubrium, corpus ve cartilago costalis", "Incisura jugularis, angulus ve processus xiphoideus"],
  """Sternum yukarıdan aşağıya manubrium, corpus ve processus xiphoideus'tan oluşur. Manubrium ile corpus arasındaki
  birleşme yeri angulus sterni'dir (2. kaburga hizası).""",
  e=["sternum"]),

# ------------------------------------------------------------------ temel: üst ekstremite
Q("b", UST, "Kolun (arm) tek kemiği hangisidir?",
  "Humerus", ["Radius", "Ulna", "Clavicula", "Scapula"],
  """Kol (brachium) bölgesinde yalnızca humerus bulunur; önkolda radius ve ulna, omuz kuşağında klavikula ve skapula
  yer alır.""",
  e=["humerus"]),

Q("b", UST, "Önkolda başparmak tarafında bulunan kemik hangisidir?",
  "Radius", ["Ulna", "Humerus", "Os scaphoideum", "Fibula"],
  """Anatomik pozisyonda radius önkolun dış (başparmak), ulna iç (serçe parmak) tarafındadır.""",
  e=["radius"]),

Q("b", UST, "Klavikulanın iç (medial) ucu hangi kemikle eklem yapar?",
  "Sternum (manubrium)", ["Scapula (akromiyon)", "1. kaburga gövdesi", "Humerus", "C7 omuru"],
  """Klavikulanın iç ucu manubrium sterni ile sternoklaviküler eklemi, dış ucu akromiyon ile akromiyoklaviküler eklemi
  yapar.""",
  e=["clavicula", "art-sternoclavicularis"]),

Q("b", UST, "Akromiyon (acromion) hangi kemiğin parçasıdır?",
  "Scapula", ["Clavicula", "Humerus", "Sternum", "1. kaburga"],
  """Akromiyon skapula dikeninin (spina scapulae) dış ucudur; omzun en yüksek kemik noktasını oluşturur ve
  klavikulayla eklem yapar.""",
  e=["scapula"]),

Q("b", UST, "Omuz ekleminde humerus başının oturduğu skapuladaki çukur hangisidir?",
  "Cavitas glenoidalis", ["Fossa supraspinata", "Fossa subscapularis", "Acetabulum", "Fossa olecrani"],
  """Humerus başı skapulanın cavitas glenoidalis'iyle omuz (glenohumeral) eklemini yapar; çukur labrum glenoidale ile
  derinleşir.""",
  e=["scapula", "art-humeri"]),

Q("b", UST, "Dirseğin arkasında ele gelen olecranon hangi kemiğe aittir?",
  "Ulna", ["Radius", "Humerus", "Scapula", "Os pisiforme"],
  """Olecranon ulnanın proksimal ucundaki çıkıntıdır; dirsek ekstansiyonda iken humerusun fossa olecrani'sine girer ve
  m. triceps brachii buraya tutunur.""",
  e=["ulna"]),

Q("b", ELK, "El bileğinde kaç karpal kemik bulunur?",
  "8", ["5", "7", "10", "14"],
  """Karpal kemikler iki sıra hâlinde dizilmiş sekiz kısa kemiktir: proksimalde scaphoideum, lunatum, triquetrum,
  pisiforme; distalde trapezium, trapezoideum, capitatum, hamatum.""",
  e=["ossa-carpi"]),

Q("b", ELK, "Elin başparmağında kaç falanks bulunur?",
  "2", ["1", "3", "4", "5"],
  """Başparmakta proksimal ve distal olmak üzere iki falanks, diğer parmaklarda üçer falanks bulunur; elde toplam 14
  falanks vardır.""",
  e=["phalanges-manus"]),

# ------------------------------------------------------------------ temel: alt ekstremite ve ayak
Q("b", ALT, "Kalça kemiğini (os coxae) oluşturan üç kemik hangileridir?",
  "Ilium, ischium ve pubis", ["Ilium, sacrum ve pubis", "Ischium, femur ve pubis", "Ilium, ischium ve coccyx",
   "Sacrum, coccyx ve pubis"],
  """Os coxae ilium, ischium ve pubisin asetabulumda kaynaşmasıyla oluşur; kaynaşma ergenlikte Y şeklindeki kıkırdağın
  kemikleşmesiyle tamamlanır.""",
  e=["os-coxae", "acetabulum"]),

Q("b", ALT, "Otururken vücut ağırlığını taşıyan kemik çıkıntısı hangisidir?",
  "Tuber ischiadicum", ["Crista iliaca", "Spina iliaca anterior superior", "Trochanter major", "Tuberculum pubicum"],
  """Otururken ağırlık iskium yumruları (tuber ischiadicum) üzerine biner. Hamstring kasları da buradan başlar.""",
  e=["os-coxae"]),

Q("b", ALT, "Bacağın iç tarafında bulunan, ağırlığı taşıyan kalın kemik hangisidir?",
  "Tibia", ["Fibula", "Femur", "Patella", "Talus"],
  """Tibia (kaval kemiği) bacağın iç tarafındaki kalın kemiktir ve ağırlığın büyük kısmını taşır; dış taraftaki ince
  fibulanın ağırlık taşımaya katkısı azdır.""",
  e=["tibia"]),

Q("b", ALT, "Diz kapağı kemiği hangisidir?",
  "Patella", ["Fabella", "Os pisiforme", "Talus", "Os naviculare"],
  """Patella m. quadriceps femoris tendonu içinde gelişen, vücudun en büyük sesamoid kemiğidir.""",
  e=["patella"]),

Q("b", ALT, "Ayak bileğinin dış yanındaki kemik çıkıntı (dış topuk) hangi kemiğe aittir?",
  "Fibula (malleolus lateralis)", ["Tibia (malleolus medialis)", "Talus", "Calcaneus", "Os cuboideum"],
  """Dış topuk fibulanın alt ucu olan malleolus lateralis'tir; iç topuk ise tibianın malleolus medialis'idir.
  Dış malleol iç malleolden daha aşağıya iner.""",
  e=["fibula"]),

Q("b", AYK, "Topuğu oluşturan kemik hangisidir?",
  "Calcaneus", ["Talus", "Os cuboideum", "Os naviculare", "Os cuneiforme mediale"],
  """Kalkaneus en büyük tarsal kemiktir ve topuğu oluşturur; arkasındaki tuber calcanei'ye Aşil tendonu tutunur.""",
  e=["calcaneus"]),

Q("b", AYK, "Ayakta toplam kaç kemik bulunur?",
  "26", ["20", "24", "28", "33"],
  """Her ayakta 7 tarsal, 5 metatarsal ve 14 falanks olmak üzere 26 kemik bulunur (sesamoidler sayılmaz).""",
  e=["ossa-tarsi"]),

Q("b", AYK, "Kalkaneusun önünde, ayağın dış kenarında bulunan tarsal kemik hangisidir?",
  "Os cuboideum", ["Os naviculare", "Talus", "Os cuneiforme laterale", "5. metatars"],
  """Kuboid kemik kalkaneusun önünde ayağın dış kenarındadır ve 4.–5. metatarslarla eklem yapar; naviküler ise talusun
  önünde iç taraftadır.""",
  e=["os-cuboideum", "ossa-tarsi"]),

# ------------------------------------------------------------------ fakülte
Q("f", GEN, "Kompakt kemiğin temel yapısal birimi hangisidir?",
  "Osteon (Havers sistemi)", ["Trabekül", "Lakün", "Kondron", "Periost"],
  """Kompakt kemik, merkezindeki Havers kanalı etrafında halkalar hâlinde dizilmiş lamellerden oluşan osteonlardan
  yapılmıştır. Süngersi kemik ise trabeküllerden oluşur.""",
  e=["os-structura"]),

Q("f", GEN, "Periostu kemiğe sıkıca bağlayan ve kemik içine giren kollajen liflere ne ad verilir?",
  "Sharpey lifleri", ["Volkmann kanalları", "Havers lamelleri", "Elastik lifler", "Retiküler lifler"],
  """Sharpey (perforan) lifleri periosttan kemik matriksine giren kalın kollajen demetleridir; tendon ve bağların kemiğe
  tutunmasını da sağlar.""",
  e=["os-structura"]),

Q("f", GEN, "Kafatası tavanı (calvaria) kemikleri hangi yolla kemikleşir?",
  "Zar içi (intramembranöz) kemikleşme", ["Kıkırdak içi (endokondral) kemikleşme", "Sesamoid kemikleşme",
   "Heterotopik kemikleşme", "Apozisyonel kıkırdak büyümesi"],
  """Kafatası tavanı, yüz kemikleri ve klavikulanın büyük kısmı doğrudan mezenkimden zar içi kemikleşmeyle gelişir.
  Kafa tabanı, omurlar ve ekstremite kemiklerinin çoğu ise kıkırdak taslak üzerinden (endokondral) kemikleşir.""",
  e=["os-structura", "cranium"]),

Q("f", GEN, "Kemik yaşı tayininde en sık hangi bölgenin grafisi kullanılır?",
  "Sol el ve el bileği", ["Diz", "Kafatası", "Pelvis", "Ayak"],
  """Kemik yaşı, sol el ve el bileği grafisindeki kemikleşme merkezlerinin görünümü ve epifiz plaklarının durumu
  standart atlaslarla (Greulich–Pyle) karşılaştırılarak belirlenir.""",
  e=["os-structura"]),

Q("f", GEN, "Erişkinde kemik iliği aspirasyonu ve biyopsisi en sık nereden yapılır?",
  "Arka krista iliaka (spina iliaca posterior superior çevresi)", ["Proksimal tibia", "Femur başı", "Kalkaneus", "Klavikula"],
  """Erişkinde arka iliak krista hem güvenli hem de kırmızı ilikten zengin olduğu için tercih edilir. Proksimal tibia
  küçük çocuklarda kullanılır.""",
  e=["iskelet-genel", "os-coxae"]),

Q("f", KAF, "Processus mastoideus'a tutunan kas hangisidir?",
  "M. sternocleidomastoideus", ["M. trapezius", "M. masseter", "M. temporalis", "Platysma"],
  """SCM sternum ve klavikuladan başlayıp processus mastoideus ile linea nuchae superior'un dış kısmına tutunur.
  Mastoid çıkıntı doğumda yoktur; kasın çekişiyle çocuklukta gelişir.""",
  e=["os-temporale", "m-sternocleidomastoideus"]),

Q("f", KAF, "Foramen magnum'dan geçmeyen yapı hangisidir?",
  "V. jugularis interna", ["Medulla oblongata", "Aa. vertebrales", "N. accessorius'un spinal kökü", "A. spinalis anterior"],
  """Foramen magnum'dan medulla oblongata ve zarları, vertebral arterler, spinal arterler ve n. accessorius'un spinal
  kökleri geçer. V. jugularis interna foramen jugulare'den başlar.""",
  e=["os-occipitale", "basis-cranii"]),

Q("f", KAF, "Sinus sphenoidalis burun boşluğunda nereye açılır?",
  "Recessus sphenoethmoidalis", ["Meatus nasi superior", "Meatus nasi medius", "Meatus nasi inferior", "Nazofarinks"],
  """Sfenoid sinüs üst konkanın arka-üstündeki recessus sphenoethmoidalis'e açılır. Arka etmoid hücreler üst meatusa,
  frontal, maksiller ve ön etmoid sinüsler orta meatusa, ductus nasolacrimalis alt meatusa açılır.""",
  e=["os-sphenoidale"]),

Q("f", KAF, "Os sphenoidale'nin processus pterygoideus'unun dış levhasına (lamina lateralis) tutunan kaslar hangileridir?",
  "M. pterygoideus lateralis ve m. pterygoideus medialis", ["M. masseter ve m. temporalis",
   "M. tensor veli palatini ve m. levator veli palatini", "M. buccinator ve m. constrictor pharyngis superior",
   "M. digastricus ve m. stylohyoideus"],
  """Lamina lateralis'in dış yüzünden m. pterygoideus lateralis'in alt başı, iç yüzünden m. pterygoideus medialis'in
  derin başı başlar. İç levhanın ucundaki hamulus etrafında m. tensor veli palatini tendonu döner.""",
  e=["os-sphenoidale", "mm-pterygoidei"]),

Q("f", KAF, "Orbitanın en kalın duvarı hangisidir?",
  "Dış (lateral) duvar", ["Tavan", "Taban", "İç (medial) duvar", "Orbita tepesi"],
  """Dış duvarı os zygomaticum ve sfenoidin büyük kanadı oluşturur ve en kalın duvardır. En ince duvar etmoidin lamina
  papyracea'sıyla iç duvardır; blow-out kırıkları en sık tabanda olur.""",
  e=["orbita"]),

Q("f", KAF, "Fissura orbitalis inferior'dan geçen sinir hangisidir?",
  "N. infraorbitalis", ["N. frontalis", "N. lacrimalis", "N. trochlearis", "N. abducens"],
  """N. maxillaris pterigopalatin çukurdan fissura orbitalis inferior aracılığıyla orbitaya girerek n. infraorbitalis
  adını alır. N. frontalis, n. lacrimalis, n. trochlearis ve n. abducens fissura orbitalis superior'dan geçer.""",
  e=["orbita", "basis-cranii"]),

Q("f", KAF, "Fossa pterygopalatina'yı orta kafa çukuruna bağlayan açıklık hangisidir?",
  "Foramen rotundum", ["Foramen ovale", "Foramen spinosum", "Canalis opticus", "Fissura orbitalis superior"],
  """N. maxillaris (V2) orta kafa çukurundan foramen rotundum ile pterigopalatin çukura geçer. Foramen ovale ve
  spinosum fossa infratemporalis'e açılır.""",
  e=["fossa-pterygopalatina"]),

Q("f", KAF, "Sutura metopica hangi kemiğin iki yarısı arasında bulunur?",
  "Os frontale", ["Os parietale", "Os occipitale", "Os sphenoidale", "Mandibula"],
  """Os frontale doğumda iki yarım hâlindedir; aralarındaki sutura metopica genellikle 1–2 yaşta kapanır. Bazı
  erişkinlerde açık kalabilir ve grafide kırık hattıyla karıştırılabilir.""",
  e=["os-frontale", "suturae-fonticuli"]),

Q("f", KAF, "Arka fontanel (fonticulus posterior) hangi kemikler arasında yer alır?",
  "İki os parietale ve os occipitale", ["İki os frontale ve iki os parietale", "Os parietale, os temporale ve os occipitale",
   "Os frontale, os parietale, os temporale ve os sphenoidale", "Os sphenoidale ve os temporale"],
  """Üçgen biçimli arka fontanel lambda noktasında, iki parietal ile oksipital kemik arasındadır ve 2–3. ayda kapanır.
  Ön fontanel bregmada, frontal ve parietal kemikler arasındadır.""",
  e=["suturae-fonticuli"]),

Q("f", KAF, "Os hyoideum genellikle hangi omur düzeyinde bulunur?",
  "C3", ["C1", "C5", "C6", "T1"],
  """Hyoid kemiği boyunda C3 düzeyindedir. Tiroid kıkırdağın üst kenarı C4, krikoid kıkırdak C6 düzeyine karşılık gelir.""",
  e=["os-hyoideum"]),

Q("f", KAF, "Süt dişlerinde aşağıdaki diş gruplarından hangisi bulunmaz?",
  "Küçük azı dişleri (premolarlar)", ["Orta kesici dişler", "Yan kesici dişler", "Köpek dişleri", "Büyük azı dişleri (molarlar)"],
  """Süt dişleri her yarım çenede 2 kesici, 1 köpek ve 2 büyük azı olmak üzere toplam 20 dişten oluşur; premolar süt
  dişi yoktur. Kalıcı premolarlar süt molarlarının yerine çıkar.""",
  e=["dentes"]),

Q("f", KAF, "Kalıcı dişlerden ilk süren diş hangisidir?",
  "1. büyük azı dişi (yaklaşık 6 yaş)", ["Orta kesici diş", "Köpek dişi", "1. küçük azı dişi", "3. büyük azı dişi"],
  """Kalıcı dişlerden ilk çıkan, süt dişlerinin arkasından süren 1. büyük azıdır (6 yaş dişi); son çıkan 3. büyük azıdır
  (yirmi yaş dişi).""",
  e=["dentes"]),

Q("f", OMR, "Kalp şeklinde gövde ve küçük yuvarlak foramen vertebrale hangi omurlara özgüdür?",
  "Torakal omurlar", ["Servikal omurlar", "Lomber omurlar", "Sakral omurlar", "Koksigeal omurlar"],
  """Torakal omurların gövdesi kalp şeklindedir, foramen vertebrale küçük ve yuvarlaktır; gövde ve transvers
  çıkıntılarda kaburga eklem yüzleri bulunur. Servikal omurlarda foramen üçgen ve geniştir.""",
  e=["vertebrae-thoracicae", "columna-vertebralis"]),

Q("f", OMR, "Omurganın birincil (primer) eğrilikleri hangileridir?",
  "Torakal ve sakral kifoz", ["Servikal ve lomber lordoz", "Servikal lordoz ve torakal kifoz",
   "Lomber lordoz ve sakral kifoz", "Torakal kifoz ve lomber lordoz"],
  """Fetüsteki C şeklindeki eğriliğin kalıntısı olan torakal ve sakral kifoz birincil eğriliklerdir; servikal ve lomber
  lordoz doğumdan sonra gelişen ikincil eğriliklerdir.""",
  e=["columna-vertebralis"]),

Q("f", OMR, "L4 spinal siniri hangi omurlar arasındaki foramen intervertebrale'den çıkar?",
  "L4 ile L5 arasından", ["L3 ile L4 arasından", "L5 ile S1 arasından", "L2 ile L3 arasından", "T12 ile L1 arasından"],
  """Torakal ve lomber bölgede spinal sinirler aynı numaralı omurun altındaki foramenden çıkar; L4 siniri L4–L5
  foramenindedir. Posterolateral L4–L5 disk hernisi ise genellikle bir alt kök olan L5'e bası yapar.""",
  e=["columna-vertebralis", "vertebrae-lumbales"]),

Q("f", GKF, "2. kaburganın dış yüzündeki pürüzlü alana (tuberositas) tutunan kas hangisidir?",
  "M. serratus anterior", ["M. pectoralis minor", "M. scalenus anterior", "M. subclavius", "M. pectoralis major"],
  """2. kaburga atipiktir: 1. kaburgadan iki kat uzundur ve dış yüzünde m. serratus anterior'un ilk dişinin tutunduğu
  tuberositas bulunur. Pectoralis minor 3.–5., scalenus anterior ve subclavius 1. kaburgaya tutunur.""",
  e=["costae-atypicae", "m-serratus-anterior"]),

Q("f", UST, "Kollar yanda serbestken skapulanın alt açısı (angulus inferior) hangi omur düzeyine karşılık gelir?",
  "T7", ["T2", "T4", "T10", "L1"],
  """Skapulanın üst açısı T2, spina scapulae'nin iç ucu T3, alt açısı T7 düzeyindedir. Alt açı göğüs muayenesinde ve
  torasentezde yüzey işareti olarak kullanılır.""",
  e=["scapula"]),

Q("f", UST, "Trochlea humeri ulnanın hangi bölümüyle eklem yapar?",
  "Incisura trochlearis", ["Incisura radialis", "Caput ulnae", "Processus styloideus ulnae", "Tuberositas ulnae"],
  """Humerusun makara biçimli trochlea'sı ulnanın olecranon ile processus coronoideus arasındaki incisura trochlearis'e
  oturarak humeroulnar menteşe eklemini yapar. Capitulum humeri ise radius başıyla eklemleşir.""",
  e=["humerus", "ulna", "art-cubiti"]),

Q("f", UST, "Tuberositas radii'ye tutunan kas hangisidir?",
  "M. biceps brachii", ["M. brachialis", "M. triceps brachii", "M. supinator", "M. pronator teres"],
  """Biceps brachii tendonu radius boynunun altındaki tuberositas radii'ye tutunur; bu nedenle güçlü bir supinatördür.
  Brachialis tuberositas ulnae'ye, pronator teres radiusun dış yüzünün ortasına tutunur.""",
  e=["radius", "m-biceps-brachii"]),

Q("f", ELK, "Retinaculum flexorum'un dış (radial) tutunma noktaları hangileridir?",
  "Tuberculum ossis scaphoidei ve tuberculum ossis trapezii", ["Os pisiforme ve hamulus ossis hamati",
   "Processus styloideus radii ve os lunatum", "Os capitatum ve os trapezoideum", "1. metakarp tabanı ve os lunatum"],
  """Retinaculum flexorum dışta skafoid ve trapezium tüberküllerine, içte pisiform ve hamulus ossis hamati'ye tutunarak
  karpal tünelin tavanını oluşturur.""",
  e=["ossa-carpi", "os-scaphoideum", "os-trapezium"]),

Q("f", ALT, "Sırtın alt kısmındaki deri çukurcukları (Venüs gamzeleri) hangi kemik çıkıntısını gösterir ve hangi omur düzeyindedir?",
  "Spina iliaca posterior superior – S2", ["Spina iliaca anterior superior – L4", "Tuber ischiadicum – S4",
   "Crista iliaca'nın en yüksek noktası – L4", "Spina ischiadica – S3"],
  """Sakroiliak bölgedeki gamzeler SIPS'in yerini gösterir ve S2 düzeyine karşılık gelir; bu düzey aynı zamanda dural
  kesenin ve subaraknoid aralığın sonlandığı yerdir.""",
  e=["os-coxae", "pelvis"]),

Q("f", ALT, "Femurdaki linea pectinea'ya tutunan kas hangisidir?",
  "M. pectineus", ["M. adductor longus", "M. iliopsoas", "M. gluteus maximus", "M. vastus medialis"],
  """M. pectineus pecten ossis pubis'ten başlayıp trochanter minor'un altındaki linea pectinea'ya tutunur.
  İliopsoas trochanter minor'a, gluteus maximus tuberositas glutea'ya tutunur.""",
  e=["femur", "m-pectineus"]),

Q("f", ALT, "Femurdaki tuberculum adductorium'a tutunan kas hangisidir?",
  "M. adductor magnus (hamstring bölümü)", ["M. adductor longus", "M. gracilis", "M. vastus medialis", "M. semimembranosus"],
  """Adductor magnus'un tuber ischiadicum'dan gelen dikey (hamstring) bölümü medial epikondilin üstündeki tuberculum
  adductorium'a tutunur; bu bölüm n. ischiadicus'un tibial kısmıyla innerve edilir.""",
  e=["femur", "m-adductor-magnus"]),

Q("f", ALT, "Lig. capitis femoris femur başında hangi çukura tutunur?",
  "Fovea capitis femoris", ["Fossa trochanterica", "Fossa acetabuli", "Fossa intercondylaris", "Linea intertrochanterica"],
  """Lig. capitis femoris asetabular çentikten femur başının ortasındaki fovea capitis'e uzanır; içinden a. obturatoria'nın
  asetabular dalı geçer.""",
  e=["femur", "acetabulum"]),

Q("f", ALT, "Kadın pelvisini erkek pelvisinden ayıran özellik hangisidir?",
  "Angulus subpubicus daha geniştir.", ["Pelvis girişi kalp şeklindedir.", "Sakrum daha uzun ve dardır.",
   "Spina ischiadica daha içe çıkıntılıdır.", "Pelvis daha derin ve dardır."],
  """Kadın pelvisi daha geniş ve sığdır; giriş oval, angulus subpubicus 90°'den geniş, sakrum kısa ve geniştir, ischial
  dikenler daha az çıkıntılıdır. Diğer seçenekler erkek pelvisinin özellikleridir.""",
  e=["pelvis"]),

Q("f", AYK, "Talus aşağıdaki kemiklerden hangisiyle eklem yapmaz?",
  "Os cuboideum", ["Tibia", "Fibula", "Calcaneus", "Os naviculare"],
  """Talus üstte tibia ve fibula (talokrural eklem), altta kalkaneus (subtalar eklem), önde naviküler
  (talonaviküler eklem) ile eklem yapar. Kuboid kalkaneusun önündedir.""",
  e=["talus"]),

Q("f", AYK, "Üç kuneiform kemikten en büyüğü hangisidir?",
  "İç (medial) kuneiform", ["Orta (intermediate) kuneiform", "Dış (lateral) kuneiform", "Üçü eşit büyüklüktedir",
   "Os cuboideum"],
  """İç kuneiform en büyük, orta kuneiform en küçüktür. Orta kuneiformun kısa olması 2. metatars tabanının iç ve dış
  kuneiformlar arasına kilitlenmesini sağlar.""",
  e=["ossa-cuneiformia", "os-cuneiforme-mediale"]),

# ------------------------------------------------------------------ fakülte: vaka
Q("fv", ALT, "Yüksekten düşen inşaat işçisinde topuk kırığı saptanıyor. Bu hastada mutlaka araştırılması gereken eşlik eden yaralanma hangisidir?",
  "Torakolomber omur kırığı", ["Kafatası kırığı", "Klavikula kırığı", "Distal radius kırığı", "Patella kırığı"],
  """Ayakları üzerine düşmede yük aksiyel olarak omurgaya iletilir; kalkaneus kırıklarının yaklaşık %10'unda
  torakolomber (özellikle L1) kompresyon kırığı eşlik eder ve gözden kaçmamalıdır.""",
  e=["calcaneus", "ossa-tarsi"]),

Q("fv", GKF, "Trafik kazası geçiren hastada 1. kaburga kırığı saptanıyor. Bu bulgu öncelikle neyi düşündürmelidir?",
  "Yüksek enerjili travma ve altındaki a. subclavia ile plexus brachialis yaralanması", ["Basit ve önemsiz bir kırık",
   "Osteoporoz", "Patolojik kırık (metastaz)", "Kostokondrit"],
  """1. kaburga kısa, kalın ve iyi korunmuş olduğundan ancak ciddi enerjili travmayla kırılır. Üzerinden a. subclavia,
  v. subclavia ve plexus brachialis'in alt gövdesi geçtiği için damar-sinir yaralanması araştırılmalıdır.""",
  e=["costae-atypicae"]),

# ------------------------------------------------------------------ TUS
Q("t", GEN, "Havers kanallarını birbirine ve periosta dik olarak bağlayan kanallar hangileridir?",
  "Volkmann kanalları", ["Sharpey lifleri", "Canaliculi", "Lakünler", "Canalis nutricius"],
  """Volkmann kanalları kemiğin uzun eksenine dik seyreder ve Havers kanallarındaki damarları birbirine, periost ve endost
  damarlarına bağlar. Canaliculi osteositlerin uzantılarını barındıran ince kanalcıklardır.""",
  e=["os-structura"]),

Q("t", GEN, "Çocuklarda en sık görülen epifiz plağı kırığı tipi (Salter–Harris) hangisidir?",
  "Tip II", ["Tip I", "Tip III", "Tip IV", "Tip V"],
  """Salter–Harris tip II kırıkta hat büyüme plağından geçip metafizden çıkar (Thurston–Holland parçası); en sık
  görülen tiptir ve prognozu iyidir. Tip V (ezilme) en kötü prognozludur ve sıklıkla geç fark edilir.""",
  e=["os-structura"]),

Q("t", KAF, "Anulus tendineus communis'in (Zinn halkası) içinden geçmeyen sinir hangisidir?",
  "N. trochlearis", ["N. oculomotorius", "N. abducens", "N. nasociliaris", "N. opticus"],
  """Zinn halkasının içinden n. opticus ve a. ophthalmica (canalis opticus), n. oculomotorius'un iki dalı, n. nasociliaris
  ve n. abducens geçer. N. trochlearis, n. frontalis ve n. lacrimalis halkanın üstünden, dışından geçer.""",
  e=["orbita"]),

Q("t", KAF, "Fossa pterygopalatina'yı burun boşluğuna bağlayan açıklık hangisidir?",
  "Foramen sphenopalatinum", ["Fissura pterygomaxillaris", "Canalis pterygoideus", "Canalis palatinus major",
   "Fissura orbitalis inferior"],
  """Foramen sphenopalatinum pterigopalatin çukuru burun boşluğunun arka-üst kısmına bağlar; a. sphenopalatina ve
  nazal sinirler buradan geçer. Fissura pterygomaxillaris fossa infratemporalis'e açılır.""",
  e=["fossa-pterygopalatina"]),

Q("t", KAF, "N. canalis pterygoidei (Vidian siniri) hangi sinirlerin birleşmesiyle oluşur?",
  "N. petrosus major ve n. petrosus profundus", ["N. petrosus minor ve chorda tympani",
   "N. petrosus major ve n. petrosus minor", "Chorda tympani ve n. lingualis", "N. petrosus profundus ve n. caroticus internus"],
  """N. petrosus major (VII'nin parasempatik lifleri) ile n. petrosus profundus (karotis pleksusundan sempatik lifler)
  birleşerek Vidian sinirini yapar ve ganglion pterygopalatinum'a ulaşır.""",
  e=["fossa-pterygopalatina"]),

Q("t", KAF, "Sagittal dikişin erken kapanması (kraniyosinostoz) hangi kafa şekline yol açar?",
  "Skafosefali (uzun ve dar kafa)", ["Brakisefali (kısa ve geniş kafa)", "Trigonosefali (üçgen alın)",
   "Plagiosefali (asimetrik kafa)", "Oksisefali (kule kafa)"],
  """Kapanan dikişe dik yönde büyüme durur, paralel yönde artar. Sagittal sinostozda kafa enine büyüyemez ve öne-arkaya
  uzar (skafosefali); en sık kraniyosinostoz tipidir. Metopik sinostoz trigonosefali yapar.""",
  e=["suturae-fonticuli"]),

Q("t", KAF, "Le Fort I kırığında kırık hattı nereden geçer?",
  "Maksillayı burun tabanının hemen üstünden yatay olarak keser.", ["Burun kökü ve orbita tabanından piramidal olarak geçer.",
   "Orbitaların içinden geçerek yüzü kafatasından tamamen ayırır.", "Yalnızca arcus zygomaticus'u tutar.",
   "Mandibula boynundan geçer."],
  """Le Fort I diş yuvalarını taşıyan alt maksillayı ayırır (yüzen damak). Le Fort II piramidal kırıktır (burun kökü,
  orbita tabanı), Le Fort III kraniyofasiyal ayrılmadır (orbitalar ve zigomatik ark boyunca).""",
  e=["maxilla"]),

Q("t", OMR, "C5 spinal siniri hangi omurlar arasından çıkar?",
  "C4 ile C5 arasından", ["C5 ile C6 arasından", "C3 ile C4 arasından", "C6 ile C7 arasından", "C7 ile T1 arasından"],
  """Servikal bölgede 8 sinir, 7 omur vardır; C1–C7 sinirleri aynı numaralı omurun üstünden çıkar, C8 ise C7 ile T1
  arasından çıkar. Bu nedenle C5–C6 disk hernisi C6 köküne bası yapar.""",
  e=["vertebrae-cervicales", "columna-vertebralis"]),

Q("t", ALT, "Asetabulumu oluşturan üç kemiği birleştiren Y (triradiat) kıkırdak yaklaşık hangi yaşlarda kemikleşir?",
  "15–17 yaş", ["1–2 yaş", "5–7 yaş", "25–30 yaş", "40 yaş sonrası"],
  """İlium, iskium ve pubis asetabulumda Y şeklindeki kıkırdakla ayrılır; bu kıkırdak ergenlik sonunda (15–17 yaş)
  kemikleşerek os coxae'yı tek kemik hâline getirir.""",
  e=["acetabulum", "os-coxae"]),

Q("t", ALT, "Doğum kanalının en dar ön-arka çapı hangisidir?",
  "Obstetrik konjugat", ["Diagonal konjugat", "Anatomik (gerçek) konjugat", "Transvers çap", "İnterspinöz çap"],
  """Obstetrik konjugat promontorium ile symphysis'in arka yüzündeki en yakın nokta arasındaki mesafedir ve pelvis
  girişinin en dar ön-arka çapıdır. Muayenede diagonal konjugat ölçülür ve 1,5–2 cm çıkarılarak tahmin edilir.""",
  e=["pelvis"]),

Q("t", ALT, "Femurdaki fossa trochanterica'ya tutunan kas hangisidir?",
  "M. obturatorius externus", ["M. piriformis", "M. gluteus medius", "M. quadratus femoris", "M. iliopsoas"],
  """Fossa trochanterica trochanter major'un iç yüzündeki çukurdur ve m. obturatorius externus'un tutunma yeridir.
  Piriformis trochanter major'un üst kenarına, quadratus femoris tuberculum quadratum'a tutunur.""",
  e=["femur", "m-obturator-externus"]),

Q("t", AYK, "Talus boyun kırıklarında avasküler nekroz riskinin yüksek olmasının temel nedeni nedir?",
  "Talus gövdesinin kanının boyundan geriye doğru (retrograd) gelmesi", ["Talusun kas tutunmalarının çok olması",
   "Talusun yalnızca a. fibularis'ten beslenmesi", "Talusun epifiz plağının erişkinde açık kalması",
   "Talusun periostunun kalın olması"],
  """Talusun büyük kısmı eklem kıkırdağıyla örtülüdür ve kas tutunması yoktur; gövdenin kanı başlıca a. canalis tarsi
  dallarıyla boyundan gövdeye retrograd akar. Boyun kırığı bu damarları keserek gövdede nekroza yol açar (Hawkins).""",
  e=["talus"]),

Q("t", ELK, "Bennett kırığında asıl (distal) parçayı proksimale ve dışa çeken kas hangisidir?",
  "M. abductor pollicis longus", ["M. adductor pollicis", "M. flexor pollicis longus", "M. extensor pollicis longus",
   "M. opponens pollicis"],
  """Bennett kırığı 1. metakarp tabanının eklem içi kırık-çıkığıdır. Ön oblik bağa bağlı küçük iç parça yerinde kalır;
  1. metakarp tabanına tutunan APL asıl parçayı proksimale ve dışa çeker.""",
  e=["ossa-metacarpi", "m-abductor-pollicis-longus"]),

Q("tv", ALT, "Motosiklet kazası geçiren hastada pelvis halkası kırığı ve hemodinamik instabilite var. Pelvis kırıklarında kanamanın en sık kaynağı hangisidir?",
  "Presakral ve pelvik venöz pleksuslar ile kırık kemik yüzeyleri", ["A. iliaca communis", "Aorta abdominalis",
   "A. femoralis", "V. cava inferior"],
  """Pelvis kırığı kanamalarının yaklaşık %80–90'ı venöz pleksuslar ve kırık süngersi kemikten kaynaklanır; bu nedenle
  pelvis kuşağı (binder) ile halkanın kapatılması ilk müdahaledir. Arteriyel kanamada anjiyoembolizasyon yapılır.""",
  e=["pelvis"]),
]
