"""Cardiovascular questions, second set: basic level (chambers, valves, main
vessels, pulses), more faculty questions and new TUS points."""
from qcommon import Q

KLP = "Kalp"
AOR = "Aorta ve dalları"
BBA = "Baş ve boyun arterleri"
UEA = "Üst ekstremite arterleri"
KPA = "Karın ve pelvis arterleri"
AEA = "Alt ekstremite arterleri"
VEN = "Venler"

questions = [
# ------------------------------------------------------------------ temel: kalp
Q("b", KLP, "Kalpte kaç boşluk (oda) bulunur?",
  "4 (iki atriyum, iki ventrikül)", ["2", "3", "5", "6"],
  """Kalp iki atriyum (kulakçık) ve iki ventrikülden (karıncık) oluşur. Sağ taraf oksijensiz kanı akciğerlere, sol taraf
  oksijenli kanı vücuda pompalar.""",
  e=["cor"]),

Q("b", KLP, "Kalbi saran çift katlı zara ne ad verilir?",
  "Perikard", ["Endokard", "Miyokard", "Plevra", "Periton"],
  """Perikard dışta fibröz, içte seröz (paryetal ve viseral) yapraklardan oluşan bir kesedir. Endokard kalbin iç yüzünü
  döşer, miyokard kalp kasıdır.""",
  e=["pericardium"]),

Q("b", KLP, "Sağ atriyum ile sağ ventrikül arasındaki kapak hangisidir?",
  "Triküspit kapak", ["Mitral kapak", "Aort kapağı", "Pulmoner kapak", "Eustachi kapağı"],
  """Sağ atrioventriküler kapak üç yaprakçıklıdır (triküspit). Sol atriyum ile sol ventrikül arasında iki yaprakçıklı mitral
  kapak bulunur.""",
  e=["valvae-cordis", "atrium-dextrum"]),

Q("b", KLP, "Sol atriyum ile sol ventrikül arasındaki kapak hangisidir?",
  "Mitral (biküspit) kapak", ["Triküspit kapak", "Aort kapağı", "Pulmoner kapak", "Thebesius kapağı"],
  """Mitral kapağın ön ve arka olmak üzere iki yaprakçığı vardır; korda tendinealar ile sol ventrikülün papiller kaslarına
  bağlıdır.""",
  e=["valvae-cordis", "ventriculus-sinister"]),

Q("b", KLP, "Duvarı en kalın olan kalp boşluğu hangisidir?",
  "Sol ventrikül", ["Sağ ventrikül", "Sol atriyum", "Sağ atriyum", "Dört boşluğun duvarı eşittir"],
  """Sol ventrikül kanı yüksek basınçla tüm vücuda pompaladığı için duvarı en kalındır; sağ ventrikülden yaklaşık üç kat
  kalındır.""",
  e=["ventriculus-sinister"]),

Q("b", KLP, "Kalbin ucunu (apeks) oluşturan boşluk hangisidir?",
  "Sol ventrikül", ["Sağ ventrikül", "Sol atriyum", "Sağ atriyum", "Sol aurikula"],
  """Kalbin apeksi sol ventrikül tarafından oluşturulur ve sol 5. interkostal aralıkta, midklavikular hattın hemen içinde
  hissedilir (apeks vurusu).""",
  e=["ventriculus-sinister", "cor"]),

Q("b", KLP, "Kalp kasını besleyen arterlere ne ad verilir?",
  "Koroner arterler", ["Pulmoner arterler", "Bronşiyal arterler", "İnterkostal arterler", "Perikardiyofrenik arterler"],
  """Sağ ve sol koroner arterler çıkan aortanın kökündeki aort sinüslerinden çıkar ve kalp duvarını besler; tıkanmaları miyokard
  enfarktüsüne yol açar.""",
  e=["aa-coronariae"]),

Q("b", KLP, "Kalbin doğal uyarı merkezine (pacemaker) ne ad verilir?",
  "Sinoatriyal (SA) düğüm", ["Atrioventriküler (AV) düğüm", "His demeti", "Purkinje lifleri", "Moderatör bant"],
  """SA düğüm sağ atriyumda v. cava superior ağzının yanındadır ve kalp atımını başlatır. Uyarı sonra AV düğüm, His demeti,
  dallar ve Purkinje liflerine iletilir.""",
  e=["cor", "atrium-dextrum"]),

Q("b", KLP, "Akciğer (pulmoner) dolaşımı kalbin hangi boşluğundan başlar?",
  "Sağ ventrikül", ["Sol ventrikül", "Sağ atriyum", "Sol atriyum", "Sinus coronarius"],
  """Pulmoner dolaşım sağ ventrikülden truncus pulmonalis ile başlar ve pulmoner venlerle sol atriyumda biter. Sistemik dolaşım
  sol ventrikülden aort ile başlar.""",
  e=["ventriculus-dexter", "truncus-pulmonalis"]),

# ------------------------------------------------------------------ temel: damarlar
Q("b", AOR, "Oksijenli kanı tüm vücuda dağıtan en büyük arter hangisidir?",
  "Aorta", ["Truncus pulmonalis", "A. carotis communis", "A. subclavia", "V. cava inferior"],
  """Aorta sol ventrikülden çıkar; çıkan aorta, aort kemeri, torakal ve abdominal aorta bölümleriyle tüm sistemik dolaşıma
  kan taşır.""",
  e=["aorta"]),

Q("b", KLP, "Oksijensiz kanı kalpten akciğerlere taşıyan damar hangisidir?",
  "Truncus pulmonalis (pulmoner arter)", ["Pulmoner venler", "Aorta", "V. cava superior", "Bronşiyal arterler"],
  """Pulmoner arterler oksijensiz kan taşıyan tek arterlerdir; sağ ventrikülden çıkıp akciğerlere gider.""",
  e=["truncus-pulmonalis"]),

Q("b", VEN, "Oksijenli kan taşıyan venler hangileridir?",
  "Pulmoner venler", ["V. cava superior ve inferior", "Portal ven", "Koroner venler", "Juguler venler"],
  """Pulmoner venler akciğerlerden oksijenlenmiş kanı sol atriyuma getirir; oksijenli kan taşıyan tek venlerdir.""",
  e=["vv-pulmonales"]),

Q("b", AOR, "Aortun kalpten çıktıktan sonra sola ve arkaya kıvrıldığı bölüme ne ad verilir?",
  "Arcus aortae (aort kemeri)", ["Aorta ascendens", "Aorta descendens", "Bifurcatio aortae", "Bulbus aortae"],
  """Çıkan aorta yukarı çıktıktan sonra T4 düzeyinde sol ana bronşun üstünden arkaya kıvrılarak aort kemerini yapar; kemerden
  baş, boyun ve kollara giden üç büyük dal çıkar.""",
  e=["aorta"]),

Q("b", BBA, "Boyunda nabzın alındığı arter hangisidir?",
  "A. carotis communis", ["A. vertebralis", "V. jugularis interna", "A. subclavia", "A. thyroidea superior"],
  """Karotis nabzı tiroid kıkırdağı hizasında, sternokleidomastoid kasın ön kenarında alınır; acil durumlarda en güvenilir
  santral nabızdır.""",
  e=["a-carotis-communis"]),

Q("b", BBA, "Beynin ön ve orta bölümlerini ve gözü besleyen boyun arteri hangisidir?",
  "A. carotis interna", ["A. carotis externa", "A. vertebralis", "A. facialis", "A. subclavia"],
  """İç karotis arter boyunda dal vermeden kafa içine girer; a. ophthalmica ile gözü, a. cerebri anterior ve media ile
  hemisferlerin büyük kısmını besler.""",
  e=["a-carotis-interna"]),

Q("b", BBA, "Beynin tabanında karotis ve vertebrobaziler sistemleri birbirine bağlayan arter halkasına ne ad verilir?",
  "Willis poligonu (circulus arteriosus cerebri)", ["Arcus palmaris", "Arcus aortae", "Sinus cavernosus", "Arcus venosus"],
  """Willis poligonu ön ve arka dolaşımı birbirine bağlayarak bir arter tıkandığında kollateral akım sağlayabilir; beyin
  anevrizmalarının çoğu bu halkada gelişir.""",
  e=["circulus-arteriosus"]),

Q("b", BBA, "A. basilaris hangi arterlerin birleşmesiyle oluşur?",
  "İki a. vertebralis", ["İki a. carotis interna", "A. carotis interna ve a. vertebralis", "İki a. cerebri posterior",
   "İki a. subclavia"],
  """Sağ ve sol vertebral arterler pons ile medulla sınırında birleşerek baziler arteri yapar; baziler arter beyin sapı,
  beyincik ve oksipital lobu besler.""",
  e=["a-vertebralis", "circulus-arteriosus"]),

Q("b", UEA, "A. brachialis dirsek önünde hangi iki dala ayrılır?",
  "A. radialis ve a. ulnaris", ["A. axillaris ve a. subclavia", "A. profunda brachii ve a. radialis",
   "A. interossea anterior ve posterior", "Yüzeyel ve derin palmar arkus"],
  """Brakiyal arter kübital fossada, radius boynu hizasında radial ve ulnar arterlere ayrılır.""",
  e=["a-brachialis"]),

Q("b", UEA, "El bileğinde nabzın en sık alındığı arter hangisidir?",
  "A. radialis", ["A. ulnaris", "A. brachialis", "A. interossea anterior", "Arcus palmaris superficialis"],
  """Radial nabız el bileğinin başparmak tarafında, radiusun alt ucu üzerinde kolayca hissedilir.""",
  e=["a-radialis"]),

Q("b", KPA, "Abdominal aorta alt ucunda hangi arterlere ayrılır?",
  "Aa. iliacae communes", ["Aa. renales", "Aa. femorales", "A. mesenterica inferior ve superior", "Aa. iliacae internae"],
  """Abdominal aorta L4 düzeyinde sağ ve sol ortak iliak arterlere ayrılır; bunlar da iç ve dış iliak arterlere bölünür.""",
  e=["aorta", "a-iliaca-communis"]),

Q("b", KPA, "Böbrekleri besleyen arterler hangileridir?",
  "Aa. renales", ["Aa. suprarenales", "Aa. lumbales", "Aa. testiculares", "A. mesenterica superior"],
  """Renal arterler L1–L2 düzeyinde abdominal aortanın iki yanından çıkar; kalp debisinin yaklaşık beşte biri böbreklere
  gider.""",
  e=["aa-renales"]),

Q("b", AEA, "Uyluğun ana arteri hangisidir?",
  "A. femoralis", ["A. poplitea", "A. iliaca interna", "A. tibialis anterior", "A. obturatoria"],
  """Dış iliak arter kasık bağının altından geçince femoral arter adını alır; uyluğu boydan boya geçerek diz arkasında popliteal
  arter olur.""",
  e=["a-femoralis"]),

Q("b", AEA, "A. poplitea'nın uç dalları hangileridir?",
  "A. tibialis anterior ve a. tibialis posterior", ["A. femoralis ve a. profunda femoris", "A. dorsalis pedis ve a. fibularis",
   "Medial ve lateral plantar arterler", "Aa. genus superiores"],
  """Popliteal arter popliteus kasının alt kenarında ön ve arka tibial arterlere ayrılır; fibular arter arka tibial arterden
  çıkar.""",
  e=["a-poplitea"]),

Q("b", AEA, "Arka tibial nabız nerede alınır?",
  "İç malleolün arkasında", ["Dış malleolün önünde", "Ayak sırtında", "Diz arkasında", "Kasıkta"],
  """A. tibialis posterior iç malleol ile Aşil tendonu arasında yüzeyeldir ve burada nabzı alınır.""",
  e=["a-tibialis-posterior"]),

Q("b", VEN, "Vücudun en büyük veni hangisidir?",
  "V. cava inferior", ["V. cava superior", "V. portae hepatis", "V. femoralis", "V. jugularis interna"],
  """Alt ana toplardamar diyaframın altındaki tüm vücut bölümlerinin kanını sağ atriyuma taşır ve vücudun en büyük
  venidir.""",
  e=["v-cava-inferior"]),

Q("b", VEN, "Baş, boyun ve kolların kanını kalbe getiren ana ven hangisidir?",
  "V. cava superior", ["V. cava inferior", "V. azygos", "V. portae hepatis", "Sinus coronarius"],
  """Üst ana toplardamar iki brakiyosefalik venin birleşmesiyle oluşur ve diyaframın üstündeki bölgelerin kanını sağ atriyuma
  getirir.""",
  e=["v-cava-superior"]),

Q("b", VEN, "Vücudun en uzun veni hangisidir?",
  "V. saphena magna", ["V. femoralis", "V. cava inferior", "V. saphena parva", "V. cephalica"],
  """Büyük safen ven ayak sırtından kasığa kadar bacağın iç yüzünde uzanan yüzeyel vendir; vücudun en uzun venidir.""",
  e=["v-saphena-magna"]),

Q("b", VEN, "Sindirim kanalından gelen besinden zengin kanı karaciğere taşıyan ven hangisidir?",
  "V. portae hepatis", ["V. cava inferior", "Vv. hepaticae", "V. azygos", "V. renalis"],
  """Portal ven mide, bağırsaklar, dalak ve pankreasın kanını karaciğere taşır; karaciğerden süzülen kan hepatik venlerle
  VCI'ya döner.""",
  e=["v-portae-hepatis"]),

Q("b", VEN, "Venlerde kanın geriye akmasını önleyen yapı hangisidir?",
  "Ven kapakçıkları", ["Tunica media'daki kalın kas tabakası", "Elastik membran", "Papiller kaslar", "Prekapiller sfinkterler"],
  """Özellikle bacak venlerindeki kapakçıklar kanın kalbe doğru tek yönde akmasını sağlar. Kapak yetmezliği varislere yol açar.""",
  e=["v-saphena-magna", "v-femoralis"]),

# ------------------------------------------------------------------ fakülte
Q("f", KLP, "Koroner arterler en çok kalp döngüsünün hangi evresinde kanla dolar?",
  "Diyastol", ["Sistol", "İzovolümik kasılma", "Ejeksiyon", "Atriyal sistol"],
  """Sistolde kasılan miyokard koroner damarları sıkıştırır; özellikle sol ventrikülün koroner akımı diyastolde olur. Bu nedenle
  taşikardide diyastol kısalınca koroner perfüzyon azalır.""",
  e=["aa-coronariae"]),

Q("f", KLP, "Sol ana koroner arter hangi iki dala ayrılır?",
  "R. interventricularis anterior (LAD) ve r. circumflexus", ["R. interventricularis anterior ve posterior",
   "R. marginalis dexter ve r. circumflexus", "A. nodi sinuatrialis ve a. nodi atrioventricularis",
   "R. circumflexus ve r. interventricularis posterior"],
  """Sol ana koroner kısa bir gövdedir; ön interventriküler olukta inen LAD'ye ve sol AV olukta kalbin arkasına dolanan
  sirkumfleks dala ayrılır.""",
  e=["aa-coronariae"]),

Q("f", KLP, "Sinus coronarius nereye açılır?",
  "Sağ atriyuma", ["Sol atriyuma", "V. cava superior'a", "Sağ ventriküle", "V. azygos'a"],
  """Koroner sinüs kalbin arka yüzündeki AV olukta yer alır, kalp venlerinin çoğunu toplar ve sağ atriyuma, VCI ağzı ile
  triküspit kapak arasında açılır.""",
  e=["venae-cordis", "atrium-dextrum"]),

Q("f", KLP, "Semilunar (aort ve pulmoner) kapakların AV kapaklardan farkı nedir?",
  "Korda tendinea ve papiller kasları yoktur.", ["Dört yaprakçıkları vardır.", "Ventrikül içinde yer alırlar.",
   "Fibröz iskelete tutunmazlar.", "Sistolde kapanırlar."],
  """Semilunar kapaklar üç yarım ay biçimli yaprakçıktan oluşur ve kan geri akmaya başlayınca cepler dolarak kapanır; korda
  tendinea veya papiller kas desteği yoktur.""",
  e=["valvae-cordis"]),

Q("f", KLP, "Birinci kalp sesi (S1) neyin kapanmasıyla oluşur?",
  "Mitral ve triküspit (AV) kapakların", ["Aort ve pulmoner kapakların", "Yalnızca aort kapağının", "Foramen ovale'nin",
   "Ductus arteriosus'un"],
  """S1 ventrikül sistolünün başında AV kapakların, S2 ise sistolün sonunda semilunar kapakların kapanmasıyla oluşur.""",
  e=["valvae-cordis"]),

Q("f", KLP, "Sağ koroner arter hangi aort sinüsünden çıkar ve hangi olukta seyreder?",
  "Sağ aort sinüsü – sağ atrioventriküler (koroner) oluk", ["Sol aort sinüsü – ön interventriküler oluk",
   "Koroner olmayan sinüs – arka interventriküler oluk", "Sağ aort sinüsü – ön interventriküler oluk",
   "Sol aort sinüsü – sol AV oluk"],
  """Sağ koroner arter sağ aort sinüsünden çıkar, sağ aurikula ile truncus pulmonalis arasından sağ AV oluğa girer ve kalbin
  arka yüzüne dolanır.""",
  e=["aa-coronariae"]),

Q("f", AOR, "Arcus aortae hangi düzeyde başlar ve biter?",
  "Angulus sterni (T4–T5) düzeyinde", ["T12 düzeyinde", "C7 düzeyinde", "Processus xiphoideus (T9) düzeyinde",
   "L1 düzeyinde"],
  """Aort kemeri angulus sterni'den geçen düzlemde başlar ve aynı düzeyde biter; bu düzlem trakea bifurkasyonu ve azigos venin
  VCS'ye açıldığı düzeye de karşılık gelir.""",
  e=["aorta"]),

Q("f", KPA, "Truncus coeliacus, a. mesenterica superior ve a. mesenterica inferior sırasıyla hangi omur düzeylerinde çıkar?",
  "T12, L1, L3", ["T10, L1, L4", "L1, L2, L3", "T12, L2, L4", "T11, L1, L2"],
  """Çölyak trunkus T12'de, SMA L1'de, IMA L3'te aortanın ön yüzünden çıkar; renal arterler L1–L2'de, bifurkasyon L4'tedir.""",
  e=["truncus-coeliacus", "a-mesenterica-superior", "a-mesenterica-inferior"]),

Q("f", KPA, "Gonadal (testiküler/ovaryen) arterler nereden çıkar?",
  "Abdominal aortadan, renal arterlerin altından (L2)", ["A. iliaca interna'dan", "A. iliaca externa'dan",
   "A. renalis'ten", "A. mesenterica inferior'dan"],
  """Gonadlar böbreklerin yakınında geliştiği için arterleri yüksekten, abdominal aortadan çıkar ve inişleri sırasında
  uzar. Sol gonadal ven ise sol renal vene dökülür.""",
  e=["aorta"]),

Q("f", BBA, "A. vertebralis kafa içine nereden girer?",
  "Foramen magnum'dan", ["Canalis caroticus'tan", "Foramen jugulare'den", "Foramen lacerum'dan", "Foramen ovale'den"],
  """Vertebral arter C6–C1 transvers deliklerinden yükselir, atlas'ın arka kemeri üzerinden dolanır ve foramen magnum'dan
  kafa içine girer.""",
  e=["a-vertebralis"]),

Q("f", BBA, "A. cerebri media'nın beslediği başlıca alan hangisidir?",
  "Hemisferin dış yüzü (yüz ve kol motor-duyu alanları, dil merkezleri)", ["Hemisferin iç yüzü (bacak alanı)",
   "Oksipital lob ve görme korteksi", "Beyin sapı ve beyincik", "Talamus ve hipokampus"],
  """MCA tıkanmasında karşı yüz ve kolda belirgin güçsüzlük ve duyu kaybı, dominant hemisferde afazi görülür; bacak daha az
  etkilenir.""",
  e=["circulus-arteriosus"]),

Q("f", BBA, "A. cerebri anterior tıkanmasında en belirgin felç nerede görülür?",
  "Karşı taraf bacakta", ["Karşı taraf yüz ve kolda", "Aynı taraf bacakta", "Her iki gözde", "Aynı taraf yüzde"],
  """ACA hemisferin iç yüzünü, motor korteksin bacak alanını besler; tıkanmasında karşı bacakta belirgin güçsüzlük ve duyu kaybı
  olur.""",
  e=["circulus-arteriosus"]),

Q("f", UEA, "A. axillaris hangi kasın alt kenarında a. brachialis adını alır?",
  "M. teres major", ["M. pectoralis minor", "M. latissimus dorsi'nin üst kenarı", "M. deltoideus", "M. coracobrachialis"],
  """Aksiller arter 1. kaburganın dış kenarından teres major'un alt kenarına kadar uzanır; burada brakiyal arter olur.""",
  e=["a-axillaris", "a-brachialis"]),

Q("f", UEA, "Derin palmar arkı esas olarak hangi arter oluşturur?",
  "A. radialis", ["A. ulnaris", "A. interossea anterior", "A. mediana", "A. brachialis"],
  """Radial arter 1. interosseöz aralıktan avuca girerek derin arkusu oluşturur ve ulnar arterin derin dalıyla tamamlanır.
  Yüzeyel arkus ise esas olarak ulnar arterdir.""",
  e=["arcus-palmares", "a-radialis"]),

Q("f", AEA, "A. femoralis'in uyluktaki en büyük dalı hangisidir?",
  "A. profunda femoris", ["A. epigastrica superficialis", "A. genus descendens", "A. circumflexa ilium superficialis",
   "A. pudenda externa"],
  """Derin femoral arter kasık bağının yaklaşık 4 cm altından çıkar ve uyluk kaslarının ana arteridir; sirkumfleks ve perforan
  dallar verir.""",
  e=["a-femoralis"]),

Q("f", VEN, "Hepatik venler nereye açılır?",
  "Doğrudan v. cava inferior'a", ["V. portae'ye", "V. azygos'a", "Sağ renal vene", "V. cava superior'a"],
  """Karaciğerin üç büyük hepatik veni, karaciğerin arka yüzünde VCI'ya doğrudan açılır. Portal ven ise karaciğere kan getirir.""",
  e=["v-cava-inferior"]),

Q("f", VEN, "Beyin omurilik sıvısını (BOS) sinus sagittalis superior'a boşaltan yapılar hangileridir?",
  "Araknoid granülasyonlar (Pacchioni cisimcikleri)", ["Koroid pleksus", "Emissary venler", "Köprü venler",
   "Ependim hücreleri"],
  """BOS koroid pleksusta üretilir ve araknoid granülasyonlar aracılığıyla dural venöz sinüslere, özellikle sinus sagittalis
  superior'a emilir.""",
  e=["sinus-durae-matris"]),

Q("f", VEN, "Ductus thoracicus nereye dökülür?",
  "Sol venöz açıya (sol v. jugularis interna ile v. subclavia'nın birleşim yeri)", ["V. cava inferior'a",
   "Sağ venöz açıya", "V. azygos'a", "Sol atriyuma"],
  """Vücudun lenfinin büyük kısmını toplayan ductus thoracicus sol iç juguler ve subklavyen venlerin birleştiği yere açılır;
  sağ üst vücudun lenfi sağ lenf kanalıyla sağ venöz açıya gelir.""",
  e=["v-subclavia", "v-jugularis-interna"]),

Q("f", VEN, "Fetal dolaşımda plasentadan oksijenli kanı fetüse getiren damar hangisidir?",
  "V. umbilicalis", ["Aa. umbilicales", "Ductus arteriosus", "V. cava inferior", "A. iliaca interna"],
  """Tek göbek veni plasentadan oksijenli kanı getirir; iki göbek arteri ise oksijensiz kanı plasentaya taşır. Kanın bir
  kısmı ductus venosus ile karaciğeri atlayarak VCI'ya geçer.""",
  e=["v-cava-inferior"]),

Q("f", VEN, "Sinus cavernosus'un içinden (duvarından değil) geçen sinir hangisidir?",
  "N. abducens (VI)", ["N. oculomotorius (III)", "N. trochlearis (IV)", "N. ophthalmicus (V1)", "N. maxillaris (V2)"],
  """A. carotis interna ve n. abducens sinüsün içinden geçer; III, IV, V1 ve V2 dış duvarında seyreder. Bu nedenle kavernöz
  sinüs trombozunda ve ICA anevrizmasında ilk etkilenen sinir genellikle abdusenstir.""",
  e=["sinus-durae-matris"]),

Q("fv", AOR, "Ani başlayan, yırtılır tarzda, sırta yayılan şiddetli göğüs ağrısı olan hipertansif hastada iki kol arasında belirgin tansiyon farkı var. En olası tanı hangisidir?",
  "Aort diseksiyonu", ["Akut miyokard enfarktüsü", "Pulmoner emboli", "Perikardit", "Pnömotoraks"],
  """Aort diseksiyonunda damarın iç tabakası yırtılır ve kan duvar katmanları arasına girer; dalların ağzı tutulabildiği için
  kollar arasında nabız ve tansiyon farkı oluşur. Çıkan aorta tutulumu (Stanford A) cerrahi acildir.""",
  e=["aorta"]),

Q("fv", KPA, "Atriyal fibrilasyonu olan yaşlı hastada ani başlayan, muayene bulgularıyla orantısız şiddette karın ağrısı var. En olası neden hangisidir?",
  "A. mesenterica superior embolisi", ["Truncus coeliacus darlığı", "A. mesenterica inferior trombozu",
   "Renal arter embolisi", "Abdominal aort anevrizması rüptürü"],
  """SMA aortadan dar bir açıyla çıktığı için kalpten kopan emboliler sıklıkla buraya gider; akut mezenterik iskemi erken
  dönemde ağrının şiddetine göre çok az muayene bulgusu verir.""",
  e=["a-mesenterica-superior"]),

Q("fv", VEN, "Uzun uçak yolculuğundan sonra bacağında şişlik ve ağrı gelişen hastada derin ven trombozu saptanıyor. Bu durumun en ciddi komplikasyonu hangisidir?",
  "Pulmoner emboli", ["Varis", "Selülit", "Kompartman sendromu", "Lenfödem"],
  """Bacak derin venlerindeki pıhtı koparak VCI, sağ kalp ve pulmoner artere ulaşabilir; masif pulmoner emboli ani ölüme yol
  açabilir.""",
  e=["v-femoralis"]),

# ------------------------------------------------------------------ TUS
Q("t", KLP, "Aşağıdakilerden hangisi Fallot tetralojisinin bileşenlerinden biri değildir?",
  "Atriyal septal defekt", ["Ventriküler septal defekt", "Pulmoner darlık (sağ ventrikül çıkış yolu darlığı)",
   "Aortanın septum üzerine ata binmesi", "Sağ ventrikül hipertrofisi"],
  """Fallot tetralojisi VSD, pulmoner darlık, ata binen aorta ve sağ ventrikül hipertrofisinden oluşur; konus septumun öne
  kaymasından kaynaklanır ve en sık siyanotik konjenital kalp hastalığıdır.""",
  e=["ventriculus-dexter", "cor"]),

Q("t", KLP, "Sinus coronarius'un ağzını koruyan kapakçığa ne ad verilir?",
  "Thebesius kapağı (valvula sinus coronarii)", ["Eustachi kapağı", "Chiari ağı", "Crista terminalis", "Todaro tendonu"],
  """Koroner sinüsün sağ atriyuma açıldığı yerde Thebesius kapağı, VCI ağzında ise Eustachi kapağı bulunur. Todaro tendonu
  Eustachi kapağının devamı olup Koch üçgeninin sınırıdır.""",
  e=["atrium-dextrum", "venae-cordis"]),

Q("t", AOR, "Disfaji lusoria'ya (yutma güçlüğü) yol açan damar anomalisi hangisidir?",
  "Aort kemerinin son dalı olarak çıkıp özofagusun arkasından geçen sağ a. subclavia", ["Çift aort kemeri",
   "Patent ductus arteriosus", "Sol v. cava superior", "Aort koarktasyonu"],
  """Aberran sağ subklavyen arter (a. lusoria) aort kemerinin son dalıdır ve özofagusun arkasından sağa geçerek ona bası
  yapabilir; en sık görülen aort kemeri anomalisidir. Bu durumda sağ n. laryngeus recurrens kemersiz (non-rekürren) seyreder.""",
  e=["a-subclavia", "aorta"]),

Q("t", BBA, "Hipertansif intraserebral kanamaların en sık kaynağı hangi arterlerdir?",
  "Lentikülostriat arterler (a. cerebri media'nın delici dalları)", ["A. communicans anterior", "A. basilaris",
   "A. cerebri anterior'un kortikal dalları", "A. meningea media"],
  """Lentikülostriat arterler MCA'dan dik açıyla çıkan ince uç arterlerdir; kronik hipertansiyonda Charcot–Bouchard
  mikroanevrizmaları gelişir ve bazal gangliyon (putamen) kanamalarına yol açar.""",
  e=["circulus-arteriosus"]),

Q("t", BBA, "Burun kanamalarının çoğunun kaynaklandığı Kiesselbach alanına katılmayan arter hangisidir?",
  "A. pharyngea ascendens", ["A. sphenopalatina", "A. ethmoidalis anterior", "A. palatina major", "A. labialis superior"],
  """Kiesselbach (Little) alanı septumun ön-alt kısmında a. sphenopalatina, a. ethmoidalis anterior, a. palatina major ve
  a. labialis superior'un (a. facialis) dallarının anastomozuyla oluşur.""",
  e=["a-carotis-externa"]),

Q("t", KPA, "Fıtık cerrahisinde tehlikeli olan 'corona mortis' nedir?",
  "A. epigastrica inferior (dış iliak sistem) ile a. obturatoria arasındaki, pubis üstünden geçen anastomoz",
  ["A. iliaca interna'nın arka trunkusu", "A. femoralis'in derin dalı", "Sağ ve sol a. iliaca communis arasındaki bağlantı",
   "A. rectalis superior ile media arasındaki anastomoz"],
  """Bazı kişilerde obturator arter (veya ven) dış iliak/alt epigastrik sistemden çıkar ya da onunla geniş anastomoz yapar ve
  ramus superior ossis pubis üzerinden geçer. Femoral fıtık veya pelvis cerrahisinde yaralanırsa ciddi kanama olur.""",
  e=["a-iliaca-communis"]),

Q("t", VEN, "Ductus venosus'un erişkindeki kalıntısı hangisidir?",
  "Lig. venosum", ["Lig. teres hepatis", "Lig. arteriosum", "Lig. umbilicale mediale", "Fossa ovalis"],
  """Ductus venosus fetüste göbek veninden gelen kanı karaciğeri atlatarak VCI'ya iletir; doğumdan sonra kapanarak lig. venosum
  olur. Göbek veni lig. teres hepatis'e dönüşür.""",
  e=["v-cava-inferior", "v-portae-hepatis"]),

Q("t", VEN, "V. umbilicalis'in erişkindeki kalıntısı hangisidir?",
  "Lig. teres hepatis (lig. falciforme'nin serbest kenarında)", ["Lig. venosum", "Lig. umbilicale mediale",
   "Lig. umbilicale medianum", "Lig. arteriosum"],
  """Göbek veni doğumdan sonra lig. teres hepatis olur. Portal hipertansiyonda bu bağın çevresindeki paraumbilikal venler
  açılarak caput medusae'ye katılır.""",
  e=["v-portae-hepatis"]),

Q("t", KPA, "A. umbilicalis'in distal bölümünün erişkindeki kalıntısı hangisidir?",
  "Lig. umbilicale mediale", ["Lig. umbilicale medianum", "Lig. teres hepatis", "Lig. venosum", "Lig. arteriosum"],
  """Göbek arterlerinin proksimal kısmı a. vesicalis superior olarak açık kalır, distal kısmı lig. umbilicale mediale'ye
  dönüşür. Lig. umbilicale medianum ise urakus kalıntısıdır.""",
  e=["a-iliaca-communis"]),

Q("t", VEN, "Subdural hematomun kaynağı genellikle hangi damarlardır?",
  "Korteksten dural sinüslere giden köprü venler", ["A. meningea media", "Lentikülostriat arterler",
   "A. communicans anterior", "Sinus cavernosus"],
  """Subdural hematom dura ile araknoid arasında, yaşlılarda ve alkoliklerde beyin atrofisiyle gerilen köprü venlerin
  yırtılmasıyla oluşur; yavaş gelişir ve hilal şeklindedir. Epidural hematom ise genellikle a. meningea media kaynaklıdır.""",
  e=["sinus-durae-matris"]),

Q("t", VEN, "Prostat kanserinin omurgaya metastaz yapmasında rol oynayan kapakçıksız ven ağı hangisidir?",
  "Vertebral venöz pleksus (Batson pleksusu)", ["Pampiniform pleksus", "Pterigoid pleksus", "Rektal venöz pleksus",
   "Portal sistem"],
  """Batson pleksusu omurga çevresinde kapakçıksız bir ven ağıdır ve pelvis venleriyle bağlantılıdır; karın içi basınç
  arttığında kan omurgaya doğru akabilir ve prostat, meme gibi tümörlerin omurgaya yayılmasını açıklar.""",
  e=["v-azygos"]),

Q("t", VEN, "May–Thurner sendromunda sol bacakta derin ven trombozuna yatkınlık yapan bası hangisidir?",
  "Sol v. iliaca communis'in sağ a. iliaca communis tarafından omurgaya karşı sıkıştırılması",
  ["Sol renal venin aorta ile SMA arasında sıkışması", "V. cava inferior'un karaciğer tarafından sıkıştırılması",
   "Sol v. femoralis'in kasık bağı altında sıkışması", "Sağ v. iliaca externa'nın sigmoid kolonla sıkışması"],
  """Sağ ortak iliak arter sol ortak iliak venin önünden çaprazlar ve onu L5 omuruna doğru bastırır; zamanla ven duvarında
  fibröz bant oluşur ve sol bacak DVT'si gelişir.""",
  e=["v-cava-inferior", "a-iliaca-communis"]),

Q("tv", VEN, "Burun kenarındaki bir çıbanı sıkan hastada ateş, göz kapağında şişlik, ekzoftalmi ve yana bakışta çift görme gelişiyor. İlk etkilenen sinir hangisidir ve neden?",
  "N. abducens – sinus cavernosus'un içinden serbestçe geçtiği için", ["N. oculomotorius – sinüsün içinden geçtiği için",
   "N. opticus – sinüsün duvarında olduğu için", "N. trochlearis – sinüsün tabanında olduğu için",
   "N. facialis – v. facialis ile birlikte seyrettiği için"],
  """Yüzün tehlikeli üçgenindeki enfeksiyon v. angularis–v. ophthalmica superior yoluyla kavernöz sinüse yayılır. Sinüsün içinde,
  ICA'nın yanında serbest seyreden n. abducens genellikle ilk tutulan sinirdir; lateral bakış kısıtlanır.""",
  e=["sinus-durae-matris"]),
]
