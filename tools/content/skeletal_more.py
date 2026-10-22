"""More of the skeleton: overview topics (the skull as a whole, its base and
foramina, the orbit, the vertebral column, the pelvis), the individual
cuneiforms and more detail for the thinner bone entries.

`entries` are new entries; `EXTRA` adds facts, sections, clinical and exam
notes to existing entries (appended, see common.write).
"""
from common import E

GEN = "Genel yapılar"
K = "Kafatası (Cranium)"
O = "Omurga (Columna vertebralis)"
G = "Göğüs kafesi (Thorax)"
A = "Alt ekstremite kemikleri"
F = "Ayak kemikleri"

entries = [
# ---------------------------------------------------------------- genel
E("iskelet-genel", "İskeletin bölümleri", "Skeleton", "Human skeleton", GEN, "general",
  "Erişkin insan iskeleti yaklaşık 206 kemikten oluşur ve iki ana bölüme ayrılır: vücudun orta eksenini oluşturan eksen iskeleti (kafatası, omurga, göğüs kafesi) ile kolları ve bacakları taşıyan ekstremite iskeleti (kuşaklar ve serbest ekstremite kemikleri).",
  facts=[("Sayı", "Erişkinde yaklaşık 206 kemik; yenidoğanda kaynaşmamış parçalarla 270–300 civarında"),
         ("Eksen iskeleti (skeleton axiale)", "80 kemik: kafatası ve kulak kemikçikleri (29, hyoid dahil), omurga (26), göğüs kafesi (25: sternum ve 24 kaburga)"),
         ("Ekstremite iskeleti (skeleton appendiculare)", "126 kemik: omuz kuşağı (4), üst ekstremiteler (60), pelvis kuşağı (2), alt ekstremiteler (60)"),
         ("Kemik şekilleri", "Uzun (femur, humerus), kısa (karpal kemikler), yassı (sternum, kafatası tavanı), düzensiz (omurlar), pnömatik (maksilla, etmoid) ve sesamoid (patella) kemikler"),
         ("İşlevi", "Destek ve şekil, organların korunması, hareket için kaldıraç, kan yapımı (kırmızı kemik iliği), kalsiyum ve fosfor deposu")],
  sections=[("Kuşaklar", "Omuz kuşağı (cingulum pectorale) klavikula ve skapuladan oluşur; gövdeye yalnızca sternoklaviküler eklemle bağlanır ve geniş hareket sağlar. Pelvis kuşağı (cingulum pelvicum) iki kalça kemiğinden oluşur; arkada sakrumla, önde birbiriyle sağlam biçimde birleşerek ağırlığı bacaklara aktarır.")],
  clinical=["Kemik iliği biyopsisi ve aspirasyonu erişkinde genellikle krista iliakanın arka kısmından (spina iliaca posterior superior çevresi) yapılır.",
            "Kemik yaşı, sol el-el bileği grafisindeki kemikleşme merkezlerine bakılarak değerlendirilir."],
  tus=["Eksen iskeleti 80, ekstremite iskeleti 126 kemikten oluşur.",
       "Kırmızı kemik iliği erişkinde başlıca yassı kemiklerde (sternum, kaburgalar, kalça kemiği, omurlar) ve uzun kemiklerin proksimal uçlarında bulunur."],
  related=["os-structura", "cranium", "columna-vertebralis", "pelvis"],
  models=["Skeletal system"], aliases=["iskelet", "skeleton", "kemikler"]),

E("os-structura", "Kemiğin yapısı ve gelişimi", "Structura ossis", "Structure of bone", GEN, "general",
  "Kemik, kalsiyum fosfat kristalleri ve kollajenden oluşan sert bir bağ dokusudur. Dışta yoğun kompakt kemik, içte süngersi kemik bulunur; yüzeyini periost örter. Kemikler zar içi veya kıkırdak içi kemikleşmeyle gelişir.",
  facts=[("Doku", "Kompakt (kortikal) kemik – osteonlardan (Havers sistemleri) oluşur; süngersi (trabeküler) kemik – trabeküller arasında kemik iliği bulunur"),
         ("Hücreler", "Osteoblast (kemik yapar), osteosit (kemik içinde gömülü olgun hücre), osteoklast (kemiği yıkar; monosit kökenli çok çekirdekli hücre)"),
         ("Uzun kemiğin bölümleri", "Epifiz (uç), metafiz (büyümenin olduğu geçiş bölgesi), diafiz (gövde, içinde cavitas medullaris), epifiz plağı (büyüme kıkırdağı)"),
         ("Kemikleşme", "Zar içi (intramembranöz): kafatası tavanı, yüz kemikleri, klavikulanın büyük kısmı. Kıkırdak içi (endokondral): kafa tabanı, omurlar, ekstremite kemiklerinin çoğu"),
         ("Kanlanma", "Diafizi a. nutricia (foramen nutricium'dan girer), uçları metafizer ve epifizer arterler, dış korteksi periost arterleri besler")],
  sections=[("Periost ve endost", "Periost kemiğin dış yüzünü örten, sinir ve damardan zengin zardır; iç katmanındaki hücreler kemiğin kalınlaşmasını ve kırık iyileşmesini sağlar. Eklem yüzlerinde periost yoktur; burayı hiyalin kıkırdak örter. Endost kemik iliği boşluğunu döşer."),
            ("Büyüme", "Uzun kemikler boyca epifiz plağındaki kıkırdak hücrelerinin çoğalması ve kemikleşmesiyle uzar; plak ergenlik sonunda kapanır (epifizer çizgi kalır). Enine büyüme periosttan yeni kemik eklenmesiyle olur.")],
  clinical=["Çocuklarda epifiz plağını tutan kırıklar (Salter–Harris) büyüme bozukluğuna ve ekstremite boy farkına yol açabilir.",
            "Osteoporozda kemik kütlesi ve trabeküler yapı azalır; en sık omur cisimlerinde, femur boynunda ve distal radiusta kırık görülür.",
            "Kırık iyileşmesi hematom → yumuşak kallus (fibrokartilaj) → sert kallus (örgü kemik) → yeniden şekillenme (lameller kemik) aşamalarıyla olur."],
  tus=["Klavikula vücutta kemikleşmeye ilk başlayan kemiktir (5.–6. hafta) ve büyük kısmı zar içi kemikleşir.",
       "Volkmann kanalları Havers kanallarını birbirine ve periosta dik olarak bağlar."],
  related=["iskelet-genel", "femur", "humerus", "clavicula"],
  models=["Femur", "Humerus", "Tibia"], aliases=["kemik dokusu", "osteon", "periost", "kemikleşme"]),

E("ossa-sesamoidea", "Sesamoid kemikler", "Ossa sesamoidea", "Sesamoid bones", GEN, "general",
  "Bir tendonun içinde gelişen, tendonu kemik çıkıntısı üzerinden kaydırarak sürtünmeyi azaltan ve kasın kaldıraç kolunu artıran küçük kemiklerdir. En büyüğü patelladır.",
  facts=[("Örnekler", "Patella (m. quadriceps femoris tendonu), os pisiforme (m. flexor carpi ulnaris tendonu), başparmak ve ayak başparmağı MP eklemlerinin altındaki sesamoidler"),
         ("İşlevi", "Tendonu korur, yönünü değiştirir, kaldıraç kolunu uzatarak kas gücünü artırır"),
         ("Değişken olanlar", "Fabella (gastrocnemius lateral başında), os peroneum (m. fibularis longus tendonunda) bazı kişilerde bulunur")],
  clinical=["Ayak başparmağı sesamoidlerinin iltihabı (sesamoidit) dansçı ve koşucularda ön ayak ağrısına neden olur.",
            "Fabella ve os peroneum grafide kırık parçasıyla karıştırılabilir."],
  tus=["Patella vücudun en büyük sesamoid kemiğidir; pisiform da m. flexor carpi ulnaris tendonu içinde gelişmiş bir sesamoid sayılır."],
  related=["patella", "os-pisiforme", "phalanges-pedis"],
  models=["Patella", "Pisiform bone", "Sesamoid bones of foot"], aliases=["sesamoid"]),

# ---------------------------------------------------------------- kafatası
E("cranium", "Kafatası (bütün olarak)", "Cranium", "Skull", K, "head",
  "Beyni koruyan beyin kafası (neurocranium) ile yüzün iskeletini oluşturan yüz kafasından (viscerocranium) oluşan, alt çene dışındaki kemikleri dikişlerle sıkıca birleşmiş kemik yapıdır. Hyoid ve kulak kemikçikleriyle birlikte 29 kemik içerir.",
  facts=[("Beyin kafası (neurocranium)", "8 kemik: os frontale, iki os parietale, os occipitale, iki os temporale, os sphenoidale, os ethmoidale"),
         ("Yüz kafası (viscerocranium)", "14 kemik: iki maxilla, iki os zygomaticum, iki os nasale, iki os lacrimale, iki os palatinum, iki concha nasalis inferior, vomer, mandibula"),
         ("Bölümleri", "Kafatası tavanı (calvaria) ve kafa tabanı (basis cranii)"),
         ("Hareketli eklem", "Kafatasında tek sinovyal eklem çene eklemidir (art. temporomandibularis); diğer kemikler dikişlerle birleşir"),
         ("Önemli noktalar", "Bregma (sagittal ve koronal dikişlerin kesişimi), lambda (sagittal ve lambdoid), pterion (frontal, parietal, temporal, sfenoid), asterion (parietal, oksipital, temporal), nasion, inion")],
  sections=[("Görünüşler", "Önden (norma frontalis) orbitalar, burun açıklığı (apertura piriformis) ve çeneler görülür. Yandan (norma lateralis) fossa temporalis, arcus zygomaticus ve pterion; alttan (norma basalis) foramen magnum, kondiller ve kafa tabanı delikleri görülür. Kafa boşluğunun içinde ön, orta ve arka kafa çukurları basamak şeklinde dizilir.")],
  clinical=["Pterion kafatasının en ince bölgesidir; altından a. meningea media'nın ön dalı geçtiği için buradaki kırıklar epidural hematom yapabilir.",
            "Kafatası dikişlerinin erken kapanması (kraniyosinostoz) kafanın anormal şekillenmesine yol açar."],
  tus=["Neurocranium 8, viscerocranium 14 kemikten oluşur (hyoid ve kulak kemikçikleri sayılmaz).",
       "Pterion, asterion ve bregma cerrahi yaklaşımlarda önemli yüzey işaretleridir; pterion arcus zygomaticus'un orta noktasının yaklaşık 4 cm üstündedir."],
  related=["suturae-fonticuli", "basis-cranii", "orbita", "os-frontale", "os-sphenoidale", "mandibula"],
  models=["Cranium"], aliases=["kafatası", "kafa", "skull", "kranyum"]),

E("suturae-fonticuli", "Kafatası dikişleri ve bıngıldaklar", "Suturae et fonticuli cranii", "Sutures and fontanelles", K, "head",
  "Kafatası kemikleri dikiş (sutura) adı verilen fibröz eklemlerle birleşir. Yenidoğanda bu dikişlerin kesişme yerlerinde kemikleşmemiş zar alanları – bıngıldaklar (fonticuli) – bulunur; doğumda başın kalıplanmasına ve beynin büyümesine olanak tanır.",
  facts=[("Başlıca dikişler", "Sutura coronalis (frontal–parietal), sutura sagittalis (iki parietal arasında), sutura lambdoidea (parietal–oksipital), sutura squamosa (parietal–temporal), sutura metopica (iki frontal yarım arasında)"),
         ("Ön bıngıldak (fonticulus anterior)", "Elmas şeklinde, en büyüğü; frontal ve parietal kemikler arasında; 18–24. ayda kapanır"),
         ("Arka bıngıldak (fonticulus posterior)", "Üçgen şeklinde; parietal ve oksipital kemikler arasında; 2–3. ayda kapanır"),
         ("Yan bıngıldaklar", "Fonticulus sphenoidalis (anterolateral, pterion yerinde) ve fonticulus mastoideus (posterolateral, asterion yerinde); ilk yıl içinde kapanır"),
         ("Eklem tipi", "Sinartroz – fibröz eklem (suturae); yaşla kemikleşebilir (sinostoz)")],
  clinical=["Ön bıngıldağın çökük olması dehidratasyonu, gergin ve kabarık olması kafa içi basınç artışını (menenjit, hidrosefali) düşündürür.",
            "Sagittal dikişin erken kapanması uzun ve dar kafa (skafosefali), tek taraflı koronal dikişin erken kapanması asimetrik kafa (plagiosefali) yapar.",
            "Ön bıngıldağın geç kapanması rikets, hipotiroidi ve hidrosefalide görülebilir."],
  tus=["Ön fontanel 18–24. ayda, arka fontanel 2–3. ayda kapanır; ön fontanelden yenidoğanda sinus sagittalis superior'a ulaşılabilir.",
       "En sık görülen kraniyosinostoz sagittal sinostozdur (skafosefali)."],
  related=["cranium", "os-parietale", "os-frontale", "os-occipitale"],
  models=["Parietal bone", "Frontal bone", "Occipital bone", "Cranial fibrous joints"], aliases=["sutur", "fontanel", "bıngıldak", "dikiş"]),

E("basis-cranii", "Kafa tabanı ve delikleri", "Basis cranii interna", "Cranial base and foramina", K, "head",
  "Kafa boşluğunun tabanı önden arkaya basamak gibi dizilmiş üç çukura ayrılır: ön, orta ve arka kafa çukurları. Bu çukurlardaki delik ve kanallardan kranial sinirler ile beyne giren ve çıkan damarlar geçer.",
  facts=[("Ön kafa çukuru (fossa cranii anterior)", "Os frontale (pars orbitalis), lamina cribrosa (os ethmoidale) ve sfenoidin küçük kanatları; frontal lobları taşır. Delikler: lamina cribrosa delikleri (n. olfactorius lifleri), foramen caecum"),
         ("Orta kafa çukuru (fossa cranii media)", "Sfenoid gövdesi ve büyük kanatları, temporal kemik skuamöz ve petröz kısmı; temporal lobları ve hipofizi (sella turcica) taşır. Delikler: canalis opticus (II, a. ophthalmica), fissura orbitalis superior (III, IV, V1, VI, v. ophthalmica superior), foramen rotundum (V2), foramen ovale (V3, n. petrosus minor), foramen spinosum (a. meningea media), foramen lacerum (kıkırdakla dolu; üstünden ICA geçer)"),
         ("Arka kafa çukuru (fossa cranii posterior)", "Os occipitale ve temporal kemiğin petröz kısmının arka yüzü; beyincik, pons ve medulla oblongata'yı taşır. Delikler: meatus acusticus internus (VII, VIII, a. labyrinthi), foramen jugulare (IX, X, XI, v. jugularis interna, sinus petrosus inferior), canalis nervi hypoglossi (XII), foramen magnum (medulla oblongata, aa. vertebrales, XI spinal kökleri)"),
         ("Dış kafa tabanındaki delikler", "Canalis caroticus (a. carotis interna, sempatik pleksus), foramen stylomastoideum (VII), canalis condylaris (emissary ven), foramina palatina, fossa incisiva")],
  sections=[("Klinik önemi", "Kafa tabanı kırıkları en sık orta kafa çukurunda olur. Ön kafa tabanı kırığında göz çevresinde morarma (rakun gözleri), BOS rinoresi ve koku kaybı; orta kafa tabanı (petröz kısım) kırığında kulak arkasında morarma (Battle bulgusu), hemotimpanum, BOS otoresi ve fasiyal paralizi görülebilir.")],
  clinical=["Foramen jugulare'deki bir tümör veya kırık IX, X ve XI kranial sinirleri birlikte etkiler (Vernet sendromu): yutma güçlüğü, ses kısıklığı, trapez ve SCM güçsüzlüğü.",
            "Kafa içi basınç artışında beyincik tonsillerinin foramen magnum'a fıtıklaşması solunum durmasına yol açabilir."],
  tus=["Fissura orbitalis superior'dan III, IV, V1 ve VI geçer; canalis opticus'tan II ve a. ophthalmica geçer.",
       "Foramen rotundum V2'yi, foramen ovale V3'ü, foramen spinosum a. meningea media'yı geçirir (akılda tutma: 'Rotundum–Ovale–Spinosum' önden arkaya).",
       "Foramen jugulare'den IX, X, XI ve v. jugularis interna; canalis nervi hypoglossi'den XII geçer."],
  related=["cranium", "os-sphenoidale", "os-occipitale", "os-temporale", "os-ethmoidale"],
  models=["Occipital bone", "Sphenoid bone", "Temporal bone", "Ethmoid bone"], aliases=["kafa tabanı", "foramen", "kafa çukuru", "fossa cranii"]),

E("orbita", "Göz çukuru (Orbita)", "Orbita", "Orbit", K, "head",
  "Göz küresini, göz kaslarını, sinirleri ve damarları barındıran, tabanı önde, tepesi arkada olan dört yüzlü piramit şeklinde kemik boşluktur. Yedi kemiğin katılımıyla oluşur.",
  facts=[("Kemikleri", "Os frontale, os zygomaticum, maxilla, os sphenoidale, os ethmoidale, os lacrimale, os palatinum"),
         ("Duvarları", "Tavan: frontal kemiğin orbital kısmı ve sfenoidin küçük kanadı; taban: maxilla, os zygomaticum, os palatinum; iç duvar: etmoidin lamina orbitalis'i, lakrimal kemik, maxilla, sfenoid; dış duvar: os zygomaticum ve sfenoidin büyük kanadı (en kalın duvar)"),
         ("Açıklıkları", "Canalis opticus (II, a. ophthalmica), fissura orbitalis superior (III, IV, V1, VI, v. ophthalmica superior), fissura orbitalis inferior (n. infraorbitalis, v. ophthalmica inferior), canalis nasolacrimalis, foramina ethmoidalia"),
         ("İçerdiği yapılar", "Göz küresi, dış göz kasları, n. opticus, gözyaşı bezi, orbita yağ dokusu, a. ophthalmica ve dalları")],
  sections=[("En zayıf duvarlar", "İç duvardaki lamina orbitalis (papyracea) en ince duvardır; etmoid sinüs enfeksiyonları buradan orbitaya yayılabilir. Taban da incedir ve altında sinus maxillaris bulunur; göze gelen künt darbede taban kırılarak 'blow-out' kırığı oluşur.")],
  clinical=["Blow-out kırığında orbita tabanı kırılır; m. rectus inferior kırık hattına sıkışarak yukarı bakışta çift görmeye, n. infraorbitalis hasarı yanak ve üst dudakta uyuşukluğa yol açar.",
            "Orbital selülit genellikle etmoid sinüzitten yayılır; tedavi edilmezse sinus cavernosus trombozuna ilerleyebilir."],
  tus=["Orbitanın en ince duvarı iç duvar (lamina papyracea), en kalın duvarı dış duvardır; blow-out kırığı en sık tabanda olur.",
       "Anulus tendineus communis (Zinn halkası) dört rektus kasının başlangıcıdır; içinden II, III, VI ve n. nasociliaris geçer, IV ve n. frontalis ile n. lacrimalis halkanın dışından geçer."],
  related=["os-frontale", "os-zygomaticum", "maxilla", "os-sphenoidale", "os-ethmoidale", "os-lacrimale"],
  models=["Frontal bone", "Zygomatic bone", "Maxilla", "Sphenoid bone", "Ethmoid bone", "Lacrimal bone", "Palatine bone"], aliases=["göz çukuru", "orbit"]),

E("fossa-pterygopalatina", "Pterigopalatin çukur", "Fossa pterygopalatina", "Pterygopalatine fossa", K, "head",
  "Maksillanın arkasında, sfenoidin pterigoid çıkıntısının önünde yer alan küçük, ters piramit şeklindeki çukurdur. N. maxillaris, a. maxillaris'in son bölümü ve ganglion pterygopalatinum burada bulunur; burun, damak, orbita ve kafa boşluğu arasında önemli bir kavşaktır.",
  facts=[("Sınırları", "Önde maxilla (tuber maxillae), arkada processus pterygoideus ve sfenoidin büyük kanadı, içte os palatinum'un dikey levhası, dışta fissura pterygomaxillaris ile fossa infratemporalis"),
         ("İçerdiği yapılar", "N. maxillaris (V2), ganglion pterygopalatinum, a. maxillaris'in 3. (pterigopalatin) bölümü ve dalları"),
         ("Bağlantıları", "Foramen rotundum (orta kafa çukuru), canalis pterygoideus (foramen lacerum bölgesi), fissura orbitalis inferior (orbita), foramen sphenopalatinum (burun boşluğu), canalis palatinus major (damak), fissura pterygomaxillaris (fossa infratemporalis)")],
  sections=[("Ganglion pterygopalatinum", "Parasempatik bir gangliondur; preganglionik lifleri n. facialis'ten n. petrosus major ile gelir (n. canalis pterygoidei). Postganglionik lifler gözyaşı bezine, burun, damak ve yutak mukoza bezlerine gider. Bu nedenle bazen 'saman nezlesi gangliyonu' olarak anılır.")],
  clinical=["Arka burun kanamalarının kaynağı a. sphenopalatina'dır; tedavi edilemeyen kanamalarda bu arter pterigopalatin çukurda veya foramen sphenopalatinum'da bağlanabilir.",
            "Juvenil nazofaringeal anjiyofibrom bu çukura yayılma eğilimindedir."],
  tus=["N. petrosus major (VII, parasempatik) ve n. petrosus profundus (sempatik) birleşerek n. canalis pterygoidei'yi (Vidian siniri) oluşturur ve ganglion pterygopalatinum'a gelir.",
       "Gözyaşı bezinin parasempatik yolu: n. facialis → n. petrosus major → ganglion pterygopalatinum → n. zygomaticus → n. lacrimalis."],
  related=["os-sphenoidale", "os-palatinum", "maxilla", "orbita"],
  models=["Sphenoid bone", "Palatine bone", "Maxilla"], aliases=["pterigopalatin fossa", "sfenopalatin"]),

# ---------------------------------------------------------------- omurga
E("columna-vertebralis", "Omurga (genel yapı ve eğrilikler)", "Columna vertebralis", "Vertebral column", O, "back",
  "Kafatasından kuyruk sokumuna uzanan, 33 omurdan oluşan esnek eksendir. Gövdenin ağırlığını taşır, omuriliği korur ve hareket sağlar. Yandan bakıldığında dört fizyolojik eğriliği vardır.",
  facts=[("Sayı", "33 omur: 7 servikal, 12 torakal, 5 lomber, 5 sakral (kaynaşarak sakrum) ve 3–5 koksigeal (kaynaşarak koksiks)"),
         ("Tipik omurun bölümleri", "Corpus (gövde), arcus vertebrae (pediculus ve lamina), processus spinosus, iki processus transversus, dört processus articularis; gövde ile ark arasında foramen vertebrale"),
         ("Eğrilik", "Servikal ve lomber lordoz (öne dışbükey – ikincil eğrilikler), torakal ve sakral kifoz (arkaya dışbükey – birincil eğrilikler)"),
         ("Delikler", "Foramina vertebralia üst üste gelerek canalis vertebralis'i, komşu omurların incisura'ları foramen intervertebrale'yi oluşturur (spinal sinirler çıkar)"),
         ("Bölgesel ayırt edici özellikler", "Servikal: foramen transversarium, çatallı diken; torakal: kaburga eklem yüzleri, uzun aşağı eğik diken; lomber: büyük böbrek şeklinde gövde, kalın kısa diken")],
  sections=[("Eğriliklerin gelişimi", "Fetüste omurga tek bir C şeklinde öne içbükeydir (birincil kifoz). Bebek başını tutmaya başlayınca servikal lordoz, oturup yürümeye başlayınca lomber lordoz gelişir. Bu ikincil eğrilikler ağırlığı yaylanarak taşımayı sağlar.")],
  clinical=["Skolyoz omurganın yana eğriliği ve rotasyonudur; en sık adölesan idiyopatik tiptedir ve en iyi öne eğilme testinde fark edilir.",
            "Hiperkifoz (kambur) osteoporotik kompresyon kırıklarında ve Scheuermann hastalığında, hiperlordoz gebelik ve şişmanlıkta görülür.",
            "Spondilolistezis bir omurun alttakinin üzerinde öne kaymasıdır; en sık L5–S1'de görülür."],
  tus=["Birincil eğrilikler torakal ve sakral kifoz, ikincil eğrilikler servikal ve lomber lordozdur.",
       "Spinal sinirler servikal bölgede aynı numaralı omurun üstünden (C8 hariç), torakal ve lomber bölgede aynı numaralı omurun altından çıkar."],
  related=["vertebrae-cervicales", "vertebrae-thoracicae", "vertebrae-lumbales", "os-sacrum", "discus-intervertebralis", "ligg-columnae"],
  models=["Vertebral column"], aliases=["omurga", "omurilik kemiği", "spine", "belkemiği"]),

E("vertebra-prominens", "7. boyun omuru (Vertebra prominens)", "Vertebra prominens (C7)", "Seventh cervical vertebra", O, "neck",
  "Boyun omurlarının en altındakidir. Uzun ve çatallanmayan diken çıkıntısı ensenin alt kısmında deri altında kolayca ele gelir; omurları saymak için başlangıç noktası olarak kullanılır.",
  facts=[("Kemik tipi", "Düzensiz kemik – atipik boyun omuru"),
         ("Ayırt edici özellik", "Uzun, çatallanmamış, uç kısmı yumrulu processus spinosus; küçük foramen transversarium (genellikle yalnızca v. vertebralis geçer)"),
         ("Eklemleri", "C6 ve T1 omurları (diskler ve faset eklemler)"),
         ("Kas tutunmaları", "Lig. nuchae'nin alt ucu, m. trapezius, m. rhomboideus minor, m. serratus posterior superior, m. splenius capitis")],
  clinical=["Ense muayenesinde ele gelen en belirgin diken genellikle C7'dir; bazı kişilerde T1'in dikeni daha belirgin olabilir.",
            "C7'nin transvers çıkıntısının uzun olması veya ek servikal kaburga, plexus brachialis'in alt gövdesine bası yaparak torasik çıkış sendromuna yol açabilir."],
  tus=["A. vertebralis çoğunlukla C6'nın foramen transversarium'una girer; C7'nin deliğinden genellikle yalnızca vertebral ven geçer.",
       "Servikal kaburga en sık C7'den gelişir ve torasik çıkış sendromunun nedenlerindendir."],
  related=["vertebrae-cervicales", "vertebrae-thoracicae", "columna-vertebralis"],
  models=["Vertebra C7"], aliases=["C7", "vertebra prominens", "çıkıntılı omur"]),

# ---------------------------------------------------------------- göğüs kafesi
E("costae-atypicae", "Atipik kaburgalar", "Costae atypicae (I, II, X–XII)", "Atypical ribs", G, "thorax",
  "Tipik kaburgaların genel yapısından ayrılan kaburgalardır: 1. ve 2. kaburgalar kısa ve geniştir; 10., 11. ve 12. kaburgaların başında tek eklem yüzü bulunur, 11. ve 12. kaburgalar ön uçları serbest kalan yüzen kaburgalardır.",
  facts=[("1. kaburga", "En kısa, en geniş ve en eğri kaburga; üst yüzünde tuberculum m. scaleni anterioris, önünde v. subclavia oluğu, arkasında a. subclavia ve plexus brachialis alt gövdesi oluğu bulunur; başında tek eklem yüzü (T1)"),
         ("2. kaburga", "1.'den iki kat uzun ve daha ince; dış yüzünde m. serratus anterior'un tutunduğu tuberositas ossis costae secundae bulunur"),
         ("10. kaburga", "Başında tek eklem yüzü vardır (yalnızca T10 ile eklemleşir)"),
         ("11. ve 12. kaburgalar", "Yüzen kaburgalar: kısa, boyunsuz ve tüberkülsüz; ön uçları karın kaslarının arasında serbesttir; transvers çıkıntılarla eklem yapmazlar"),
         ("Kaburga sınıflaması", "Gerçek kaburgalar (1–7: kendi kıkırdağıyla sternuma), yalancı kaburgalar (8–10: üstteki kıkırdağa), yüzen kaburgalar (11–12)")],
  clinical=["1. kaburga kırığı ciddi enerjili travmayı gösterir ve altındaki a. subclavia ile plexus brachialis'in yaralanabileceğini düşündürmelidir.",
            "12. kaburga böbreğin arka yüzüne komşudur; böbrek cerrahisinde ve 12. kaburga kırıklarında plevra ve böbrek yaralanması akılda tutulmalıdır."],
  tus=["1. kaburganın üst yüzünde skalen tüberkülün önünden v. subclavia, arkasından a. subclavia ve plexus brachialis'in alt gövdesi geçer.",
       "Plevranın alt sınırı arkada 12. kaburganın altına kadar inebilir; bu bölgedeki böbrek girişimlerinde pnömotoraks riski vardır."],
  related=["costae", "cartilagines-costales", "vertebrae-thoracicae", "sternum"],
  models=["First rib", "Second rib", "Tenth rib", "Eleventh rib", "Twelfth rib"], aliases=["birinci kaburga", "yüzen kaburga", "atipik kaburga"]),

# ---------------------------------------------------------------- pelvis
E("pelvis", "Pelvis (leğen kemiği halkası)", "Pelvis ossea", "Bony pelvis", A, "pelvis",
  "İki kalça kemiği ile sakrum ve koksiksin oluşturduğu kemik halkadır. Gövdenin ağırlığını bacaklara aktarır, pelvis organlarını korur ve kadında doğum kanalını oluşturur. Linea terminalis büyük ve küçük pelvisi birbirinden ayırır.",
  facts=[("Kemikleri", "İki os coxae (ilium, ischium, pubis), os sacrum, os coccygis"),
         ("Bölümleri", "Büyük pelvis (pelvis major – linea terminalis'in üstü, karın boşluğunun parçası) ve küçük pelvis (pelvis minor – doğum kanalı)"),
         ("Eklemleri", "Artt. sacroiliacae, symphysis pubica, art. sacrococcygea, art. lumbosacralis"),
         ("Pelvis girişi (apertura pelvis superior)", "Promontorium, ala sacri, linea arcuata, pecten ossis pubis ve symphysis'in üst kenarı ile sınırlanır"),
         ("Pelvis çıkışı (apertura pelvis inferior)", "Koksiks, ligg. sacrotuberalia, tuber ischiadica, ramus ischiopubicus ve symphysis'in alt kenarı ile sınırlanır")],
  sections=[("Cinsiyet farkları", "Kadın pelvisi daha geniş ve sığdır; pelvis girişi oval (jinekoid), angulus subpubicus geniştir (90°'den büyük), foramen obturatum üçgene yakın, sakrum daha kısa ve geniştir, ischial dikenler daha az içe çıkıntılıdır. Erkek pelvisi daha dar ve derindir; giriş kalp şeklindedir (android), angulus subpubicus dardır (yaklaşık 60–70°)."),
            ("Obstetrik çaplar", "Gerçek konjugat (promontorium – symphysis üst kenarı) yaklaşık 11 cm; obstetrik konjugat (promontorium – symphysis'in arka yüzündeki en yakın nokta) doğum kanalının en dar ön-arka çapıdır; diagonal konjugat muayenede ölçülür ve obstetrik konjugattan yaklaşık 1,5–2 cm uzundur. Pelvis çıkışının en dar çapı interspinöz çaptır (yaklaşık 10 cm).")],
  clinical=["Pelvis halkası kırıkları genellikle iki yerden olur ve ciddi iç kanamaya (özellikle venöz pleksuslardan) yol açabilir.",
            "Sefalopelvik uyumsuzlukta bebeğin başı pelvisten geçemez; sezaryen gerekebilir."],
  tus=["Obstetrik konjugat doğum kanalının en dar ön-arka çapıdır; diagonal konjugattan 1,5–2 cm çıkarılarak tahmin edilir.",
       "Kadın pelvisinde angulus subpubicus 90°'den geniştir (yaklaşık 80–85° ile 90–100° arası), erkekte yaklaşık 60–70°'dir."],
  related=["os-coxae", "os-sacrum", "os-coccygis", "art-sacroiliaca", "symphysis-pubica", "ligg-pelvis"],
  models=["Hip bone", "Sacrum", "Coccyx"], aliases=["leğen", "pelvis", "leğen kemiği"]),

E("acetabulum", "Asetabulum (kalça çanağı)", "Acetabulum", "Acetabulum", A, "pelvis",
  "Kalça kemiğinin dış yüzündeki, femur başını kabul eden derin, yarım küre şeklindeki çukurdur. Ilium, ischium ve pubis bu çukurda Y şeklindeki bir kıkırdakla birleşir.",
  facts=[("Oluşum", "Ilium (yaklaşık 2/5), ischium (2/5) ve pubis (1/5); üç kemik ergenlikte Y (triradiat) kıkırdağın kemikleşmesiyle kaynaşır"),
         ("Önemli oluşumlar", "Facies lunata (at nalı şeklinde eklem yüzü), fossa acetabuli (eklem yüzü olmayan merkez, yağ yastığı içerir), incisura acetabuli (aşağıda çentik), limbus acetabuli"),
         ("Bağlantılar", "Labrum acetabuli kenarı derinleştirir; lig. transversum acetabuli çentiği köprüler; lig. capitis femoris çentikten femur başına uzanır"),
         ("Yönü", "Yana, öne ve aşağı bakar (anteversiyon)")],
  clinical=["Gelişimsel kalça displazisinde asetabulum sığdır ve femur başı tam yerleşmez; yenidoğanda Ortolani ve Barlow testleriyle taranır.",
            "Yüksek enerjili travmada femur başı asetabulumu kırabilir (asetabulum kırığı); diz panoya çarptığında arka duvar kırığı ve arka kalça çıkığı sıktır."],
  tus=["Triradiat kıkırdak 15–17 yaşlarında kemikleşerek üç kemiği kaynaştırır.",
       "Lig. capitis femoris içinden a. obturatoria'nın asetabular dalı (a. capitis femoris) geçer; erişkinde femur başına katkısı azdır."],
  related=["os-coxae", "femur", "art-coxae", "pelvis"],
  models=["Hip bone", "Triradiate cartilage", "Acetabular labrum"], aliases=["kalça çanağı", "asetabulum"]),

# ---------------------------------------------------------------- ayak
E("ossa-tarsi", "Ayak bileği kemikleri (Tarsal kemikler)", "Ossa tarsi", "Tarsal bones", F, "lowerLimb",
  "Ayağın arka yarısını oluşturan yedi kısa kemiktir: arka grupta talus ve kalkaneus, orta grupta naviküler, ön grupta kuboid ve üç kuneiform kemik. Vücut ağırlığını bacaktan ayağa aktarır ve ayak kemerlerini oluşturur.",
  facts=[("Sayı", "7: talus, calcaneus, os naviculare, os cuboideum, os cuneiforme mediale, intermedium ve laterale"),
         ("Kemik tipi", "Kısa kemikler"),
         ("Dizilimi", "Arka (proksimal) sıra: talus ve kalkaneus; orta: naviküler (iç tarafta); ön (distal) sıra: üç kuneiform (içte) ve kuboid (dışta)"),
         ("Eklemleri", "Art. talocruralis (talus ile tibia-fibula), art. subtalaris, art. tarsi transversa (Chopart), artt. tarsometatarsales (Lisfranc)"),
         ("Akılda tutma", "Talus bacağı ayağa bağlar; kalkaneus topuğu yapar; naviküler talusun önünde; kuboid kalkaneusun önünde; kuneiformlar navikülerin önünde 1.–3. metatarslara eklem yapar")],
  clinical=["Ayak bileği ve tarsal kırıkların en sık görüleni kalkaneus kırığıdır (yüksekten düşme); eşlik eden omur kırığı mutlaka aranmalıdır.",
            "Tarsal koalisyon (iki tarsal kemiğin doğuştan kaynaşması) adölesanlarda ağrılı rijid düztabana yol açar."],
  tus=["Talus üzerinde kas tutunmayan tek tarsal kemiktir; kanlanması retrograd olduğu için boyun kırıklarında avasküler nekroz riski yüksektir.",
       "Ayakta 7 tarsal, 5 metatarsal ve 14 falanks olmak üzere 26 kemik bulunur."],
  related=["talus", "calcaneus", "os-naviculare", "os-cuboideum", "ossa-cuneiformia", "artt-pedis"],
  models=["Tarsal bones"], aliases=["tarsal kemikler", "tarsus", "ayak bileği kemikleri"]),

E("os-cuneiforme-mediale", "İç kama kemiği", "Os cuneiforme mediale", "Medial cuneiform bone", F, "lowerLimb",
  "Üç kuneiform kemiğin en büyüğüdür; ayağın iç kenarında, naviküler ile 1. metatars arasında yer alır. Kama biçimi diğer ikisinin tersine tabanı aşağıda olacak şekildedir.",
  facts=[("Kemik tipi", "Kısa kemik"),
         ("Eklemleştiği kemikler", "Os naviculare, os cuneiforme intermedium, 1. ve 2. metatars"),
         ("Kas tutunmaları", "M. tibialis anterior ve m. fibularis longus (alt-iç yüz), m. tibialis posterior'un bir uzantısı"),
         ("Bağlar", "Lisfranc bağı: iç kuneiformdan 2. metatars tabanına uzanan güçlü interosseöz bağ")],
  clinical=["Lisfranc yaralanmasında bu bağın kopmasıyla 1. ve 2. metatars tabanları arasında açıklık oluşur; grafide gözden kaçabileceği için dikkatli değerlendirilmelidir."],
  tus=["M. tibialis anterior ve m. fibularis longus tendonları iç kuneiform ve 1. metatars tabanında bir 'üzengi' oluşturarak ayağın kemerlerini destekler."],
  related=["ossa-cuneiformia", "os-naviculare", "ossa-metatarsi", "ossa-tarsi"],
  models=["Medial cuneiform bone"], aliases=["medial kuneiform", "iç kuneiform"]),

E("os-cuneiforme-intermedium", "Orta kama kemiği", "Os cuneiforme intermedium", "Intermediate cuneiform bone", F, "lowerLimb",
  "Kuneiform kemiklerin en küçüğüdür; diğer ikisinin arasında yer alır. Daha kısa olduğu için önünde 2. metatars tabanının yerleştiği bir girinti (mortis) oluşur.",
  facts=[("Kemik tipi", "Kısa kemik"),
         ("Eklemleştiği kemikler", "Os naviculare, iç ve dış kuneiform kemikler, 2. metatars"),
         ("Ayırt edici özellik", "En kısa kuneiformdur; 2. metatars tabanı iç ve dış kuneiformlar arasına kilitlenir"),
         ("Kas tutunmaları", "M. tibialis posterior'un uzantıları")],
  clinical=["2. metatars tabanının bu girintiye kilitlenmesi tarsometatarsal eklemin anahtar taşıdır; Lisfranc kırık-çıkıklarında bu yapı bozulur."],
  tus=["2. metatars tabanı kuneiformlar arasına gömülü olduğu için Lisfranc ekleminin en stabil, kilit noktasıdır."],
  related=["ossa-cuneiformia", "os-cuneiforme-mediale", "os-cuneiforme-laterale", "ossa-metatarsi"],
  models=["Intermediate cuneiform bone"], aliases=["intermediate kuneiform", "orta kuneiform"]),

E("os-cuneiforme-laterale", "Dış kama kemiği", "Os cuneiforme laterale", "Lateral cuneiform bone", F, "lowerLimb",
  "Orta büyüklükteki kuneiformdur; ortadaki kuneiform ile kuboid arasında yer alır ve önde 3. metatarsla eklem yapar.",
  facts=[("Kemik tipi", "Kısa kemik"),
         ("Eklemleştiği kemikler", "Os naviculare, os cuneiforme intermedium, os cuboideum, 2., 3. ve 4. metatars"),
         ("Kas tutunmaları", "M. tibialis posterior uzantıları, m. flexor hallucis brevis'in bir kısmı")],
  clinical=["Ayak orta bölümünün stres kırıklarında kuneiformlar nadiren tutulur; ağrının yeri tarsometatarsal bağ yaralanmalarıyla karışabilir."],
  tus=["Dış kuneiform 2., 3. ve 4. metatarslarla temas eder; transvers kemerin tepesine yakındır."],
  related=["ossa-cuneiformia", "os-cuneiforme-intermedium", "os-cuboideum", "ossa-metatarsi"],
  models=["Lateral cuneiform bone"], aliases=["lateral kuneiform", "dış kuneiform"]),
]


EXTRA = {
"os-zygomaticum": dict(
    sections=[("Yapısı", "Yanak çıkıntısını oluşturan kemiktir. Processus temporalis'i temporal kemiğin processus zygomaticus'uyla birleşerek arcus zygomaticus'u yapar; processus frontalis'i orbitanın dış kenarını oluşturur. Orbital yüzündeki foramen zygomatico-orbitale'den giren n. zygomaticus dalları yanak ve şakak derisine çıkar.")],
    clinical=["Arcus zygomaticus kırığında altındaki m. temporalis ve processus coronoideus sıkışabildiği için ağız açma kısıtlanır."]),
"os-nasale": dict(
    facts=[("Eklemleştiği kemikler", "Karşı taraf os nasale, os frontale, maxilla (processus frontalis), os ethmoidale (lamina perpendicularis)"),
           ("Kemikleşme", "Zar içi kemikleşme")],
    tus=["Burun kemikleri kırığında septal hematom aranmalıdır; drene edilmezse septum kıkırdağı nekroza gider."]),
"os-lacrimale": dict(
    clinical=["Dakriyosistorinostomi (gözyaşı kesesini buruna açma ameliyatı) lakrimal kemik ve maksillanın frontal çıkıntısından yapılır."]),
"os-palatinum": dict(
    clinical=["Damak yarığında maksillanın damak çıkıntıları ve palatin kemiklerin yatay levhaları orta hatta birleşemez; beslenme ve konuşma bozukluğu yapar."]),
"vomer": dict(
    facts=[("Eklemleştiği kemikler", "Os sphenoidale, os ethmoidale (lamina perpendicularis), maxillae, ossa palatina; ön kenarı septum kıkırdağıyla birleşir")],
    clinical=["Septum deviasyonu çoğunlukla vomer ile septum kıkırdağı birleşim yerindeki eğrilikten kaynaklanır."]),
"concha-nasalis-inferior": dict(
    clinical=["Alt konka hipertrofisi burun tıkanıklığının sık nedenidir; ilaçla düzelmezse konka küçültme yapılır."]),
"atlas": dict(
    sections=[("Yapısı", "Atlas'ın gövdesi ve diken çıkıntısı yoktur; bir ön ve bir arka kemerle iki massa lateralis'ten oluşan bir halkadır. Ön kemerin arka yüzündeki fovea dentis'e aksis'in dens'i oturur ve lig. transversum atlantis onu arkadan tutar. Arka kemerin üst yüzündeki oluktan a. vertebralis ve n. suboccipitalis (C1) geçer.")]),
"axis": dict(
    facts=[("Bağlar", "Lig. transversum atlantis (dens'i arkadan tutar), ligg. alaria (dens'ten oksipital kondillere), lig. apicis dentis, membrana tectoria")],
    sections=[("Dens axis", "Embriyolojik olarak atlas'ın gövdesine karşılık gelir ve aksis'e kaynaşmıştır. Atlanto-aksiyal eklemde başın sağa sola dönme hareketinin yaklaşık yarısı bu çıkıntı etrafında gerçekleşir.")]),
"os-sacrum": dict(
    sections=[("Yapısı", "Beş sakral omurun kaynaşmasıyla oluşan üçgen kemiktir. Ön (pelvik) yüzü içbükeydir ve dört çift foramina sacralia anteriora'dan sakral spinal sinirlerin ön dalları çıkar. Arka yüzünde crista sacralis mediana (dikenlerin kalıntısı), alt ucunda hiatus sacralis ve cornua sacralia bulunur. Üst kenarın ön çıkıntısı promontorium'dur.")],
    clinical=["Kaudal epidural anestezi hiatus sacralis'ten yapılır; cornua sacralia iğne yeri için ele gelen işaretlerdir."]),
"os-coccygis": dict(
    facts=[("Kas tutunmaları", "M. gluteus maximus (arka yüz), m. coccygeus ve m. levator ani'nin iliococcygeus kısmı (lig. anococcygeum aracılığıyla)")]),
"cartilagines-costales": dict(
    sections=[("Yapısı ve işlevi", "Hiyalin kıkırdaktan oluşan bu uzantılar kaburgaları sternuma bağlar ve göğüs kafesine esneklik kazandırır. 1. kaburga kıkırdağı sternumla sinartroz (sinkondroz), 2.–7. kıkırdaklar sinovyal eklemle birleşir; 8.–10. kıkırdaklar üstteki kıkırdağa tutunarak arcus costalis'i oluşturur.")],
    clinical=["Tietze sendromunda üst kaburga kıkırdaklarında ağrılı şişlik olur; kostokondrit ise şişliksiz göğüs duvarı ağrısıdır ve kalp ağrısıyla karışabilir."]),
"clavicula": dict(
    sections=[("Yapısı", "S şeklinde, yatay duran uzun bir kemiktir: iç 2/3'ü öne dışbükey, dış 1/3'ü öne içbükeydir. Medial ucu sternumla, lateral ucu akromiyonla eklem yapar. Alt yüzde lig. coracoclaviculare'nin tutunduğu tuberculum conoideum ve linea trapezoidea, lig. costoclaviculare'nin tutunduğu yüzey ve m. subclavius oluğu bulunur. Kanal içi (medüller) boşluğu yoktur.")]),
"radius": dict(
    sections=[("Uçları", "Proksimalde disk şeklindeki caput radii capitulum humeri ve ulnanın incisura radialis'i ile eklem yapar ve lig. anulare ile sarılır; altında collum ve m. biceps brachii'nin tutunduğu tuberositas radii bulunur. Distal uç geniştir; dışta processus styloideus radii, içte ulnayla eklem yapan incisura ulnaris, arkada Lister tüberkülü (tuberculum dorsale) bulunur.")]),
"ulna": dict(
    sections=[("Uçları", "Proksimal uçta olecranon ve processus coronoideus, aralarında humerus troklear çentiği (incisura trochlearis) ve dışta radius başı için incisura radialis bulunur. Distal uçtaki küçük caput ulnae ve processus styloideus ulnae el bileği ekleminden üçgen fibrokartilaj diskle ayrılır.")]),
"os-lunatum": dict(
    facts=[("Eklemleştiği kemikler", "Radius, os scaphoideum, os triquetrum, os capitatum, os hamatum (bazen)"),
           ("Kanlanma", "Palmar ve dorsal yüzlerden giren damarlarla; bazı kişilerde tek kaynaktan beslenir")],
    sections=[("Konumu", "Proksimal karpal sıranın ortasında, radiusun lunat çukurunda bulunan yarım ay şeklindeki kemiktir. Karpal kemiklerin en sık çıkanıdır.")]),
"os-triquetrum": dict(
    facts=[("Eklemleştiği kemikler", "Os lunatum, os pisiforme, os hamatum; üçgen fibrokartilaj disk aracılığıyla ulnaya komşu")],
    clinical=["Triquetrum'un dorsal avülsiyon (kırık) parçası, scaphoid kırığından sonra en sık görülen karpal kırıktır; elin üstüne düşmede olur."]),
"os-trapezoideum": dict(
    facts=[("Eklemleştiği kemikler", "Os scaphoideum, os trapezium, os capitatum, 2. metakarp")],
    clinical=["Karpal kemiklerin en az kırılanıdır; 2. metakarp tabanıyla sıkı birleşmesi sayesinde korunur."]),
"os-capitatum": dict(
    clinical=["Kapitatum kırığı nadirdir ancak başına giden damarlar retrograd olduğundan avasküler nekroz gelişebilir.",
              "Lunatum çıkığında kapitatum radiusla aynı hizada kalırken lunatum öne doğru döner (perilunat çıkıkla ayırt edilir)."]),
"os-hamatum": dict(
    sections=[("Hamulus ossis hamati", "Avuç içine doğru uzanan kanca biçimli çıkıntıdır; retinaculum flexorum'un iç ucu ve Guyon kanalının dış duvarıdır. M. flexor digiti minimi brevis ve m. opponens digiti minimi buraya tutunur.")]),
"os-pisiforme": dict(
    clinical=["Pisiform kırığı genellikle hipotenar bölgeye doğrudan düşmeyle olur ve yakınındaki n. ulnaris'i etkileyebilir."]),
"ossa-metacarpi": dict(
    sections=[("Yapısı", "Her metakarpın proksimalde tabanı (basis), ortada gövdesi (corpus) ve distalde başı (caput) vardır. Başlar yumruk sıkıldığında 'boğumları' oluşturur. Birinci metakarp en kısa ve en kalın olanıdır; trapezium ile eyer eklemi yaparak başparmağın karşı koyma hareketini sağlar.")],
    tus=["Bennett kırığı 1. metakarp tabanının eklem içi kırık-çıkığıdır; m. abductor pollicis longus distal parçayı proksimale çeker."]),
"phalanges-manus": dict(
    sections=[("Yapısı", "Her falanksın tabanı, gövdesi ve başı vardır. Proksimal falanksların tabanı metakarp başıyla, diğerleri bir öncekinin başıyla eklem yapar. Distal falanksların ucunda tırnak yatağını taşıyan tuberositas phalangis distalis bulunur.")]),
"patella": dict(
    sections=[("Yapısı", "Üçgen şeklinde, tabanı yukarıda tepesi aşağıda olan sesamoid kemiktir. Ön yüzü m. quadriceps femoris tendonunun lifleriyle örtülüdür; arka yüzü kalın kıkırdakla kaplıdır ve dikey bir kabarıntıyla femurun kondilleri arasındaki oluğa (facies patellaris) oturan iç ve dış eklem yüzlerine ayrılır. Dış eklem yüzü daha geniştir.")]),
"tibia": dict(
    sections=[("Uçları", "Proksimal uç geniştir: iç ve dış kondiller, aralarında çapraz bağların ve menisküslerin tutunduğu area intercondylaris ile eminentia intercondylaris bulunur. Önde lig. patellae'nin tutunduğu tuberositas tibiae vardır. Distal uçta malleolus medialis ve fibula için incisura fibularis bulunur.")]),
"fibula": dict(
    sections=[("İşlevi", "Ağırlık taşımaya katkısı azdır (yaklaşık %10–15); esas görevi kaslara tutunma yeri sağlamak ve distalde malleolus lateralis ile ayak bileği ekleminin dış duvarını oluşturmaktır. Gövdesinin orta kısmı greft olarak alınabilir.")]),
"talus": dict(
    facts=[("Kanlanma", "Başlıca a. canalis tarsi (a. tibialis posterior'dan) ve a. sinus tarsi (a. dorsalis pedis'ten); kan boyundan gövdeye retrograd akar")],
    sections=[("Bölümleri", "Caput (naviküler ile eklem yapar), collum ve corpus'tan oluşur. Gövdenin üst yüzündeki trochlea tali önde arkadan daha geniştir; bu nedenle ayak bileği dorsifleksiyonda daha stabildir. Arka çıkıntının (processus posterior) iç ve dış tüberkülleri arasındaki oluktan m. flexor hallucis longus tendonu geçer.")]),
"calcaneus": dict(
    facts=[("Kas tutunmaları", "Tendo calcaneus (Aşil), m. plantaris, m. flexor digitorum brevis, m. abductor hallucis, m. abductor digiti minimi, m. quadratus plantae, m. extensor digitorum brevis")],
    sections=[("Önemli oluşumlar", "Arkada topuk yumrusu (tuber calcanei), içte talusu taşıyan sustentaculum tali (altından FHL tendonu geçer), dışta fibular kasların tendonlarını ayıran trochlea fibularis bulunur. Üst yüzde talusla üç eklem yüzü ve aralarında sulcus calcanei vardır; talus oluğuyla birlikte sinus tarsi'yi oluşturur.")]),
"os-naviculare": dict(
    facts=[("Eklemleştiği kemikler", "Talus (caput tali), üç kuneiform kemik, bazen kuboid"),
           ("Kas tutunmaları", "M. tibialis posterior (tuberositas ossis navicularis)")],
    sections=[("Klinik önemi", "Ayağın iç kemerinin tepesine yakın yer alır. Tuberositas'ı iç malleolün önünde ve altında ele gelir. Bazı kişilerde aksesuar naviküler kemik bulunur ve m. tibialis posterior tendonunun gerilmesiyle ağrıya yol açabilir.")]),
"os-cuboideum": dict(
    facts=[("Eklemleştiği kemikler", "Calcaneus, os cuneiforme laterale, os naviculare (bazen), 4. ve 5. metatars"),
           ("Önemli oluşumlar", "Alt yüzde m. fibularis longus tendonunun geçtiği sulcus tendinis m. fibularis longi ve önündeki tuberositas ossis cuboidei")],
    clinical=["Kuboid sendromu, kuboidin hafif yer değiştirmesiyle ayağın dış kenarında ağrı yapan, özellikle dansçılarda görülen bir durumdur."]),
"ossa-cuneiformia": dict(
    clinical=["Kuneiform kırıkları nadirdir; çoğunlukla Lisfranc yaralanmasına eşlik eder."],
    tus=["İç kuneiform en büyük, orta kuneiform en küçük kuneiformdur; orta kuneiformun kısa olması 2. metatars tabanının kilitlenmesini sağlar."]),
"phalanges-pedis": dict(
    sections=[("Yapısı", "Ayak falanksları el falankslarına göre çok daha kısadır; özellikle 2.–5. parmakların orta ve distal falanksları küçüktür ve 5. parmakta sıklıkla kaynaşmıştır. Başparmağın (hallux) falanksları kalın ve güçlüdür; yürümenin itme fazında ağırlığın son aktarıldığı yerdir.")]),
}


# Where each new entry goes in the reading order: after this entry id, or
# first in its group when None.
AFTER = {
    "iskelet-genel": None, "os-structura": "iskelet-genel", "ossa-sesamoidea": "os-structura",
    "cranium": None, "suturae-fonticuli": "cranium", "basis-cranii": "suturae-fonticuli",
    "orbita": "basis-cranii", "fossa-pterygopalatina": "orbita",
    "columna-vertebralis": None, "vertebra-prominens": "axis",
    "costae-atypicae": "costae",
    "pelvis": "os-coxae", "acetabulum": "pelvis",
    "ossa-tarsi": None, "os-cuneiforme-mediale": "ossa-cuneiformia",
    "os-cuneiforme-intermedium": "os-cuneiforme-mediale", "os-cuneiforme-laterale": "os-cuneiforme-intermedium",
}


def merge(base):
    """The base entries with the new ones in their places."""
    out = list(base)
    for e in entries:
        anchor = AFTER[e["id"]]
        if anchor is None:
            first = next((i for i, x in enumerate(out) if x["group"] == e["group"]), len(out))
            out.insert(first, e)
        else:
            out.insert(next(i for i, x in enumerate(out) if x["id"] == anchor) + 1, e)
    return out
