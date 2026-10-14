from qcommon import Q, write

GO = "Görme organı"
KU = "İşitme ve denge organı"
KT = "Koku ve tat"

questions = [
# ------------------------------------------------------------------ Görme
Q("f", GO, "Gözün toplam kırma gücünün yaklaşık üçte ikisini sağlayan yapı hangisidir?",
  "Kornea",
  ["Lens", "Aköz hümör", "Vitreus", "Retina"],
  """Işığın en büyük kırılması hava–kornea yüzeyinde olur (yaklaşık 40–43 diyoptri). Lens daha az kırma gücüne sahiptir
  ancak akomodasyonla gücünü değiştirebilir. Refraktif cerrahi bu nedenle korneayı hedefler.""",
  e=["cornea", "lens"]),

Q("f", GO, "Göz küresinin tabakaları dıştan içe doğru hangisinde doğru verilmiştir?",
  "Fibröz tabaka (sklera, kornea) – vasküler tabaka (uvea) – sinirsel tabaka (retina)",
  ["Retina – uvea – sklera", "Uvea – sklera – retina", "Kornea – retina – koroid", "Sklera – retina – koroid"],
  """Dış fibröz tabaka göze şeklini verir; orta vasküler tabaka (koroid, siliyer cisim, iris) beslenme ve akomodasyonu,
  iç tabaka (retina) görme duyusunu sağlar.""",
  e=["bulbus-oculi", "sclera", "tunica-vasculosa", "retina"]),

Q("t", GO, "Aköz hümörün dolaşım yolu hangisinde doğru verilmiştir?",
  "Siliyer çıkıntılar → arka kamara → pupilla → ön kamara → trabeküler ağ → Schlemm kanalı",
  ["Lens → vitreus → retina → koroid", "Ön kamara → arka kamara → siliyer cisim → vortex venleri",
   "Gözyaşı bezi → kornea → ön kamara → Schlemm kanalı", "Siliyer çıkıntılar → vitreus → optik disk → n. opticus"],
  """Aköz hümör siliyer epitel tarafından üretilir ve iridokorneal açıdan drene olur. Akımın engellenmesi göz içi basıncını
  artırarak glokoma ve optik sinir hasarına yol açar.""",
  e=["tunica-vasculosa", "sclera", "cornea"]),

Q("tv", GO, """Karanlık sinema salonunda aniden şiddetli göz ağrısı, kızarıklık, bulantı ve ışıkların etrafında
haleler gören yaşlı kadında pupil orta derecede genişlemiş ve ışığa yanıtsız, göz sert. En olası tanı ve
mekanizma nedir?""",
  "Akut açı kapanması glokomu; pupil genişleyince iris iridokorneal açıyı kapatır.",
  ["Akut üveit; siliyer cisim iltihabı aköz üretimini artırır.", "Retina dekolmanı; vitreus retinayı çeker.",
   "Santral retinal arter tıkanması; retina iskemiye girer.", "Bakteriyel keratit; kornea ödemi oluşur."],
  """Dar açılı gözlerde midriyazis (karanlık, antikolinerjik ilaçlar) irisin periferini açıya yığar ve trabeküler ağa
  aköz akışını engeller. Göz içi basıncı hızla yükselir; midriyatik damlalardan kaçınılmalı, acil tedavi gerekir.""",
  e=["tunica-vasculosa", "iris", "cornea"]),

Q("t", GO, "Yakına bakarken (akomodasyon) gerçekleşen değişiklik hangisinde doğru verilmiştir?",
  "M. ciliaris kasılır, zonül lifleri gevşer, lens kalınlaşır ve kırma gücü artar.",
  ["M. ciliaris gevşer, zonül lifleri gerilir, lens incelir.", "M. dilatator pupillae kasılır, lens incelir.",
   "Zonül lifleri kasılarak lensi çeker ve kalınlaştırır.", "Kornea eğriliği artar, lens değişmez."],
  """Akomodasyonda parasempatik lifler (III, ganglion ciliare) siliyer kası kasar; siliyer halka daralır, zonüller gevşer
  ve elastik lens küreselleşir. Yakın refleksi akomodasyon, konverjans ve miyozisten oluşur.""",
  e=["lens", "tunica-vasculosa", "n-oculomotorius"]),

Q("t", GO, "Pupil ışık refleksinde her iki gözde de pupilin daralmasını (konsensüel yanıt) sağlayan yapı hangisidir?",
  "Pretektal çekirdeklerin her iki Edinger–Westphal çekirdeğine lif göndermesi",
  ["Optik kiazmada tüm liflerin çaprazlaşması", "Corpus geniculatum laterale'nin iki taraflı bağlantısı",
   "N. oculomotorius'un iki gözü birden innerve etmesi", "Görme korteksinin iki taraflı temsil edilmesi"],
  """Işık refleksi: retina → n. opticus → tractus opticus → pretektal çekirdek → her iki Edinger–Westphal çekirdeği →
  n. oculomotorius → ganglion ciliare → kısa siliyer sinirler → m. sphincter pupillae. Yol LGN ve görme korteksine
  uğramaz.""",
  e=["iris", "n-opticus", "n-oculomotorius"]),

Q("tv", GO, """Optik nörit geçiren hastada sağ göze ışık tutulduğunda her iki pupil daralıyor; ışık hızla sol gözden
sağ göze getirildiğinde ise her iki pupil genişliyor. Bu bulgu neyi gösterir?""",
  "Sağ n. opticus'ta afferent defekt (relatif afferent pupil defekti – Marcus Gunn)",
  ["Sağ n. oculomotorius felci", "Sol n. opticus'ta afferent defekt", "Sağ Horner sendromu", "Argyll Robertson pupili"],
  """Sallanan ışık testinde hasarlı optik sinire ışık tutulduğunda sağlam taraftan daha az afferent uyarı gelir; bu
  nedenle ışık sağlamdan hasarlıya geçerken iki pupil birden genişler. Efferent yol sağlam olduğundan konsensüel yanıt
  korunur.""",
  e=["n-opticus", "iris"]),

Q("f", GO, "Görme keskinliğinin en yüksek olduğu ve yalnızca konilerden oluşan retina bölgesi hangisidir?",
  "Fovea centralis",
  ["Discus nervi optici", "Ora serrata", "Retinanın periferi", "Corpus ciliare"],
  """Fovea makulanın ortasındaki çukurcuktur; burada iç retina katmanları kenara itilmiştir ve yoğun koni dizilimi
  bulunur. Optik diskte fotoreseptör yoktur ve görme alanında kör noktaya karşılık gelir.""",
  e=["retina"]),

Q("fv", GO, """Miyop hasta sağ gözünde ani başlayan ışık çakmaları, çok sayıda uçuşan cisim ve görme alanının bir
kısmına 'perde inmesi' tarifliyor. En olası tanı nedir?""",
  "Retina dekolmanı",
  ["Akut açı kapanması glokomu", "Katarakt", "Konjonktivit", "Presbiyopi"],
  """Yırtıklı (regmatojen) retina dekolmanında nöral retina pigment epitelinden ayrılır; vitreusun retinayı çekmesi
  ışık çakmalarına, yırtıktan dökülen pigment ve kan uçuşan cisimlere yol açar. Yüksek miyopi risk faktörüdür ve
  durum acildir.""",
  e=["retina", "corpus-vitreum"]),

Q("f", GO, "Gözyaşının boşalma yolu hangisinde doğru sıralanmıştır?",
  "Puncta lacrimalia → canaliculi lacrimales → saccus lacrimalis → ductus nasolacrimalis → meatus nasi inferior",
  ["Saccus lacrimalis → puncta → canaliculi → meatus nasi medius", "Glandula lacrimalis → ductus nasolacrimalis → saccus → meatus superior",
   "Canaliculi → puncta → ductus nasolacrimalis → sinus maxillaris", "Puncta → saccus → canaliculi → recessus sphenoethmoidalis"],
  """Gözyaşı bezi orbitanın üst-dış köşesindedir; gözyaşı göz yüzeyini iç köşeye doğru geçer ve kapak kenarındaki
  puncta'lardan drene olur. Kanal tıkanıklığında sulanma (epifora) ve dakriyosistit gelişebilir.""",
  e=["apparatus-lacrimalis", "cavitas-nasi"]),

Q("f", GO, "Göz kapağında Meibom bezlerinin kronik granülomatöz iltihabı sonucu oluşan ağrısız şişlik hangisidir?",
  "Şalazyon",
  ["Hordeolum (arpacık)", "Blefarit", "Dakriyosistit", "Pterjiyum"],
  """Meibom (tarsal) bezleri tarsal plak içinde yer alır ve gözyaşı filminin yağ tabakasını salgılar. Şalazyon tıkanmaya
  bağlı kronik iltihaptır ve ağrısızdır; hordeolum ise kirpik dibi bezlerinin (Zeis, Moll) veya Meibom bezinin akut,
  ağrılı enfeksiyonudur.""",
  e=["palpebrae"]),

Q("t", GO, "Retinanın beslenmesi ile ilgili aşağıdakilerden hangisi doğrudur?",
  "İç katmanlar a. centralis retinae'den, dış katmanlar (fotoreseptörler) koroid kapillerlerinden beslenir.",
  ["Retinanın tamamı yalnızca a. centralis retinae'den beslenir.", "Retinanın tamamı yalnızca koroidden beslenir.",
   "Fovea a. centralis retinae'nin dallarıyla yoğun şekilde beslenir.", "Retina vitreus içindeki damarlarla beslenir."],
  """Bu çift kanlanma nedeniyle santral retinal arter tıkanmasında iç retina iskemiye girer ve soluklaşır; damarsız fovea
  koroidden beslendiği için kırmızı görünür (kiraz kırmızısı leke). Retina dekolmanında fotoreseptörler koroidden
  ayrıldığı için beslenemez.""",
  e=["retina", "tunica-vasculosa"]),

# ------------------------------------------------------------------ İşitme ve denge
Q("t", KU, "Dış kulak yolu temizlenirken bazı kişilerde öksürük refleksi oluşmasından sorumlu sinir hangisidir?",
  "N. vagus'un ramus auricularis'i (Arnold siniri)",
  ["N. auriculotemporalis", "N. auricularis magnus", "N. facialis'in motor dalı", "N. glossopharyngeus'un timpanik dalı"],
  """Dış kulak yolunun arka ve alt duvarı ile kulak zarının dış yüzünün bir kısmı vagusun aurikular dalından duyu alır.
  Bu bölgenin uyarılması vagal refleksle öksürük, nadiren senkop yapabilir.""",
  e=["auris-externa", "n-vagus", "membrana-tympanica"]),

Q("t", KU, "Miringotomi (kulak zarına insizyon) genellikle hangi kadrandan yapılır ve neden?",
  "Ön-alt veya arka-alt kadrandan; üst-arka kadrandaki kemikçikler ve chorda tympani korunur.",
  ["Arka-üst kadrandan; zar en kalın olduğu için", "Pars flaccida'dan; damar içermediği için",
   "Umbonun tam ortasından; malleusa kolay ulaşıldığı için", "Ön-üst kadrandan; tuba auditiva'ya yakın olduğu için"],
  """Kulak zarının arka-üst kadranının arkasında incus, stapes ve chorda tympani bulunur. Alt kadranlardan yapılan
  insizyon bu yapıları korur. Otoskopide ışık refleksi ön-alt kadranda görülür.""",
  e=["membrana-tympanica", "auris-media"]),

Q("t", KU, "Orta kulak boşluğunun tavanını oluşturan ince kemik lamina ve klinik önemi hangisidir?",
  "Tegmen tympani; orta kulak enfeksiyonları orta kafa çukuruna (menenjit, temporal lob apsesi) yayılabilir.",
  ["Promontorium; koklear hasara yol açar.", "Fenestra cochleae; vertigo yapar.",
   "Bulbus v. jugularis; sigmoid sinüs trombozu yapar.", "Canalis caroticus; ICA anevrizması yapar."],
  """Orta kulağın tavanı tegmen tympani, tabanı bulbus v. jugularis, ön duvarı ICA ve tuba auditiva, medial duvarı
  promontorium (kokleanın bazal turu) ile oval ve yuvarlak pencereler, arka duvarı aditus ad antrum mastoideum'dur.""",
  e=["auris-media", "os-temporale"]),

Q("fv", KU, """35 yaşında kadında yıllar içinde ilerleyen iki taraflı işitme kaybı var; gebelikte kötüleşmiş. Kulak
zarları normal görünüyor, odyometride iletim tipi kayıp saptanıyor. En olası patoloji nedir?""",
  "Otoskleroz – stapes tabanının fenestra vestibuli'de sabitlenmesi",
  ["Ménière hastalığı – endolenf artışı", "Presbiakuzi – tüylü hücre kaybı", "Akustik nörinom – VIII basısı", "Kolesteatom – pars flaccida retraksiyonu"],
  """Otosklerozda oval pencere çevresinde anormal kemik yapımı stapesi kilitler ve sesin iç kulağa iletimini bozar.
  Genç kadınlarda sıktır, gebelikle artabilir; stapedektomi ve protezle tedavi edilir.""",
  e=["ossicula-auditus", "auris-media"]),

Q("f", KU, "Bell paralizisi olan hastada seslerin rahatsız edici derecede yüksek duyulması (hiperakuzi) hangi kasın felcine bağlıdır?",
  "M. stapedius",
  ["M. tensor tympani", "M. tensor veli palatini", "M. levator veli palatini", "M. auricularis posterior"],
  """M. stapedius vücudun en küçük iskelet kasıdır; yüksek seslerde stapesin hareketini sınırlayarak iç kulağı korur
  (akustik refleks). N. facialis'in fasiyal kanaldaki dalıyla innerve edilir. Tensor tympani ise V3 ile innerve edilir.""",
  e=["auris-media", "ossicula-auditus", "n-facialis"]),

Q("fv", KU, """3 yaşında çocukta üst solunum yolu enfeksiyonundan sonra ateş, kulak ağrısı ve kulak zarında bombeleşme
gelişiyor. Çocuklarda orta kulak enfeksiyonlarının sık görülmesinin anatomik nedeni nedir?""",
  "Tuba auditiva'nın çocuklarda daha kısa, geniş ve yatay olması",
  ["Dış kulak yolunun çocuklarda daha uzun olması", "Kulak zarının çocuklarda olmaması",
   "Mastoid hücrelerin çocuklarda tamamen gelişmiş olması", "Tuba auditiva'nın çocuklarda tamamen kapalı olması"],
  """Çocukta tuba daha yatay ve kısa olduğundan nazofarinks sekresyonları ve mikroorganizmalar orta kulağa kolayca ulaşır;
  ayrıca adenoid dokusu tuba ağzını tıkayabilir. Tubanın kıkırdak kısmının açılması m. tensor veli palatini'ye bağlıdır.""",
  e=["tuba-auditiva", "auris-media", "tonsillae"]),

Q("t", KU, "Kokleada yüksek frekanslı seslerin algılandığı bölge ve bunun nedeni hangisidir?",
  "Kokleanın tabanı; baziler membran burada dar ve serttir.",
  ["Kokleanın tepesi (helikotrema); baziler membran burada en dardır.", "Kokleanın tepesi; baziler membran burada en serttir.",
   "Vestibül; otolitler yüksek frekansa duyarlıdır.", "Yarım daire kanalları; endolenf akımı hızlıdır."],
  """Baziler membran tabandan tepeye genişler ve esnekleşir; bu nedenle taban yüksek, tepe düşük frekanslara yanıt verir
  (tonotopi). Yaşa bağlı ve ototoksik işitme kayıpları önce bazal turdaki yüksek frekans bölgesini etkiler.""",
  e=["cochlea", "auris-interna"]),

Q("tv", KU, """Sağ kulağında işitme azlığı olan hastada Weber testinde ses sağ kulağa lateralize oluyor; sağda Rinne testi
negatif (kemik yolu hava yolundan daha iyi). Hangi tip işitme kaybı vardır?""",
  "Sağda iletim tipi işitme kaybı",
  ["Sağda sensörinöral işitme kaybı", "Solda iletim tipi işitme kaybı", "Solda sensörinöral işitme kaybı", "İki taraflı sensörinöral işitme kaybı"],
  """İletim tipi kayıpta çevre gürültüsünün maskeleyici etkisi azaldığı için Weber'de ses hasta kulağa lateralize olur ve
  Rinne negatiftir. Sensörinöral kayıpta Weber sağlam kulağa lateralize olur ve Rinne pozitif kalır.""",
  e=["auris-media", "cochlea", "n-vestibulocochlearis"]),

Q("tv", KU, """Yatakta dönerken veya başını geriye attığında saniyeler süren şiddetli baş dönmesi yaşayan hastada
Dix–Hallpike manevrasıyla rotatuvar nistagmus ortaya çıkıyor. Sorun en sık hangi yapıdadır?""",
  "Arka yarım daire kanalı (yerinden oynamış otolitler – BPPV)",
  ["Lateral yarım daire kanalı – vestibüler nörit", "Koklea – Ménière hastalığı", "Sacculus – otoskleroz", "N. vestibularis – akustik nörinom"],
  """Benign paroksismal pozisyonel vertigoda utrikülden kopan otokonyalar en sık arka kanala düşer; başın belirli
  pozisyonlarında kupulayı uyararak kısa süreli vertigo yapar. Epley manevrasıyla otokonyalar utriküle geri taşınır.""",
  e=["organum-vestibulare"]),

Q("fv", KU, """Atak tarzında saatler süren vertigo, kulakta dolgunluk hissi, çınlama ve dalgalı seyirli düşük frekanslı
işitme kaybı olan hastada en olası patoloji nedir?""",
  "Zar labirentte endolenf artışı (endolenfatik hidrops – Ménière hastalığı)",
  ["Perilenf fistülü", "Stapesin fiksasyonu", "Kulak zarı perforasyonu", "N. facialis felci"],
  """Ménière hastalığında endolenfin üretim-emilim dengesi bozulur ve zar labirent genişler. Klasik dörtlü: atak
  tarzında vertigo, dalgalı işitme kaybı, tinnitus ve kulak dolgunluğu.""",
  e=["auris-interna", "organum-vestibulare", "cochlea"]),

Q("t", KU, "Soğuk su ile kalorik test yapıldığında bilinçli sağlıklı kişide nistagmusun hızlı fazı hangi yöne olur?",
  "Karşı tarafa",
  ["Aynı tarafa", "Yukarı", "Aşağı", "Nistagmus oluşmaz"],
  """'COWS': Cold – Opposite, Warm – Same. Soğuk su lateral kanalda endolenfi ampulladan uzaklaştırarak o taraftaki
  vestibüler girdiyi azaltır; gözler yavaşça aynı tarafa kayar, hızlı faz karşı tarafa olur. Komadaki hastada hızlı faz
  kaybolur ve gözler soğuk su verilen tarafa tonik deviasyon gösterir.""",
  e=["organum-vestibulare", "n-vestibulocochlearis"]),

Q("t", KU, "Mastoidit komplikasyonlarından hangisi mastoid hücrelerin sigmoid sinüse komşuluğuyla açıklanır?",
  "Lateral (sigmoid) sinüs trombozu",
  ["Bezold apsesi", "Yüz felci", "Labirentit", "Subperiosteal apse"],
  """Mastoid antrum ve hücreleri arkada ince bir kemikle sigmoid sinüsten ayrılır; enfeksiyon bu yoldan sinüse geçerek
  trombofilebite yol açabilir. Bezold apsesi mastoid ucundan SCM altına, yüz felci ise fasiyal kanala yayılımla olur.""",
  e=["auris-media", "sinus-durae-matris", "os-temporale"]),

# ------------------------------------------------------------------ Koku ve tat
Q("f", KT, "Koku epiteli (regio olfactoria) burun boşluğunda nerede bulunur?",
  "Burun boşluğunun tavanında; üst konka ve septumun üst kısmında",
  ["Alt konkanın üzerinde", "Burun deliklerinin girişinde (vestibulum)", "Maksiller sinüsün tabanında", "Nazofarinkste"],
  """Koku epiteli lamina cribrosa'nın hemen altında, küçük bir alanda yer alır; bipolar koku nöronlarının aksonları
  lamina cribrosa'dan geçerek bulbus olfactorius'ta sinaps yapar. Burun tıkanıklığında koku alma azalır.""",
  e=["organum-olfactus", "n-olfactorius", "cavitas-nasi"]),

Q("t", KT, "Chorda tympani'nin seyri ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Orta kulakta malleus ile incus arasından geçer, fissura petrotympanica'dan çıkıp n. lingualis'e katılır.",
  ["Doğrudan foramen ovale'den çıkar.", "N. glossopharyngeus'un dalıdır.", "Parotis bezine salgı lifleri taşır.", "Dilin arka 1/3'ünün tadını alır."],
  """Chorda tympani n. facialis'in fasiyal kanaldaki dalıdır; dilin ön 2/3'ünün tat liflerini ve submandibular ile
  sublingual bezlere giden preganglioner parasempatik lifleri taşır. Orta kulak cerrahisinde yaralanması tat
  bozukluğuna yol açar.""",
  e=["gustus", "n-facialis", "auris-media"]),

Q("f", KT, "Tat tomurcuğu içermeyen dil papillası hangisidir?",
  "Papilla filiformis",
  ["Papilla vallata", "Papilla fungiformis", "Papilla foliata", "Hepsi tat tomurcuğu içerir"],
  """Filiform papillalar en sayılı papillalardır ve mekanik işlev görür (keratinize, sürtünme sağlar). Vallat papillalar
  sulcus terminalis önünde sıralanır ve en çok tat tomurcuğunu taşır; fungiform papillalar dil ucu ve kenarlarında,
  foliate papillalar arka-yan kenarlardadır.""",
  e=["gustus", "lingua"]),

Q("t", KT, "Tat liflerinin beyin sapında sonlandığı çekirdek hangisidir?",
  "Nucleus tractus solitarii (üst/gustatuvar bölümü)",
  ["Nucleus ambiguus", "Nucleus spinalis nervi trigemini", "Nucleus dorsalis nervi vagi", "Nucleus salivatorius superior"],
  """VII, IX ve X ile gelen tat lifleri soliter traktusa katılarak çekirdeğin rostral kısmında sonlanır; buradan talamusun
  VPM çekirdeğine ve insula/frontal operkulumdaki tat korteksine ulaşılır. Nucleus ambiguus motor, salivatuvar
  çekirdekler parasempatik çekirdeklerdir.""",
  e=["gustus", "medulla-oblongata", "thalamus"]),
]

write("senses", questions)
