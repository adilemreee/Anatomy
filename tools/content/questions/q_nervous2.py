"""Nervous system questions, second set: the basic level (lobes and cortical
areas, brainstem, spinal cord and meninges, the cranial and spinal nerves,
the autonomic system) and a few more faculty questions."""
from qcommon import Q

BE = "Beyin"
BS = "Beyin sapı ve beyincik"
OM = "Omurilik ve zarlar"
KS = "Kranial sinirler"
SS = "Spinal sinirler ve pleksuslar"
OT = "Otonom sinir sistemi"

questions = [
# ------------------------------------------------------------------ temel: beyin
Q("b", BE, "Beyin yarımkürelerini birbirine bağlayan en büyük komissural lif demeti hangisidir?",
  "Corpus callosum", ["Fornix", "Capsula interna", "Commissura anterior", "Corona radiata"],
  """Corpus callosum iki hemisferin korteksini birbirine bağlayan en büyük komissürdür. Capsula interna ve corona radiata
  korteksi alt merkezlere bağlayan projeksiyon lifleridir; fornix hipokampusun çıkış yoludur.""",
  e=["corpus-callosum"]),

Q("b", BE, "Birincil motor korteks hangi girusta bulunur?",
  "Gyrus precentralis", ["Gyrus postcentralis", "Gyrus temporalis superior", "Gyrus cinguli", "Gyrus angularis"],
  """Birincil motor korteks (Brodmann 4) sulcus centralis'in hemen önündeki gyrus precentralis'tedir. Vücudun karşı yarısının
  istemli hareketlerini başlatır; temsil haritası motor homunkulus olarak bilinir.""",
  e=["gyrus-precentralis"]),

Q("b", BE, "Birincil somatosensoriyel (duyu) korteks hangi girustadır?",
  "Gyrus postcentralis", ["Gyrus precentralis", "Gyrus frontalis superior", "Gyrus parahippocampalis", "Cuneus"],
  """Gyrus postcentralis (Brodmann 3, 1, 2) sulcus centralis'in hemen arkasındadır ve karşı vücut yarısından gelen dokunma,
  ağrı, ısı ve pozisyon duyusunu alır.""",
  e=["gyrus-postcentralis"]),

Q("b", BE, "Birincil görme korteksi hangi lobdadır?",
  "Lobus occipitalis (sulcus calcarinus çevresi)", ["Lobus temporalis", "Lobus parietalis", "Lobus frontalis", "Insula"],
  """Birincil görme korteksi (Brodmann 17) oksipital lobun iç yüzünde, sulcus calcarinus'un iki yanındadır. Buranın hasarı
  karşı görme alanında kayba yol açar.""",
  e=["lobus-occipitalis"]),

Q("b", BE, "Birincil işitme korteksi nerededir?",
  "Gyrus temporalis superior'daki transvers temporal girusler (Heschl)", ["Gyrus temporalis inferior", "Gyrus angularis",
   "Gyrus precentralis", "Cuneus"],
  """Birincil işitme korteksi (Brodmann 41–42) üst temporal girusun sulcus lateralis'e bakan yüzündeki transvers temporal
  (Heschl) giruslarındadır.""",
  e=["lobus-temporalis"]),

Q("b", BE, "Frontal lobu parietal loptan ayıran oluk hangisidir?",
  "Sulcus centralis (Rolando)", ["Sulcus lateralis (Sylvius)", "Sulcus parieto-occipitalis", "Sulcus calcarinus",
   "Sulcus cinguli"],
  """Sulcus centralis frontal ve parietal lobları ayırır; önünde motor, arkasında duyu korteksi bulunur. Sulcus lateralis
  temporal lobu frontal ve parietal loplardan ayırır.""",
  e=["lobus-frontalis", "lobus-parietalis"]),

Q("b", BE, "Yeni anıların oluşmasında (bellek) en önemli yapı hangisidir?",
  "Hippocampus", ["Corpus amygdaloideum", "Cerebellum", "Nucleus caudatus", "Thalamus"],
  """Hipokampus temporal lobun iç kısmındadır ve kısa süreli belleğin uzun süreli belleğe aktarılmasında temel rol oynar;
  iki taraflı hasarı yeni anı oluşturamamaya (anterograd amnezi) yol açar.""",
  e=["hippocampus"]),

Q("b", BE, "Korku ve duygusal tepkilerin işlenmesinde başlıca rol oynayan, temporal lobun derinindeki badem biçimli çekirdek hangisidir?",
  "Corpus amygdaloideum", ["Hippocampus", "Putamen", "Corpus mamillare", "Claustrum"],
  """Amigdala limbik sistemin parçasıdır; tehlikenin algılanması, korku ve duygusal belleğin oluşmasında görev alır.
  Hipokampusun hemen önünde yer alır.""",
  e=["corpus-amygdaloideum", "systema-limbicum"]),

Q("b", BE, "Koku dışındaki tüm duyuların kortekse ulaşmadan önce aktarıldığı (röle) çekirdek grubu hangisidir?",
  "Thalamus", ["Hypothalamus", "Nuclei basales", "Cerebellum", "Hippocampus"],
  """Talamus diensefalonun en büyük bölümüdür; görme, işitme, tat ve vücut duyuları buradaki çekirdeklerde aktarılarak
  ilgili kortikal alanlara gönderilir. Koku yolu talamusa uğramadan kortekse ulaşır.""",
  e=["thalamus"]),

Q("b", BE, "Vücut ısısını, açlık ve susuzluğu ve hipofiz salgılarını düzenleyen yapı hangisidir?",
  "Hypothalamus", ["Thalamus", "Corpus pineale", "Mesencephalon", "Pons"],
  """Hipotalamus üçüncü ventrikülün tabanını ve yan duvarlarının alt kısmını oluşturur. Otonom sistemi ve hipofizi
  yöneterek iç ortamın dengesini (homeostaz) sağlar.""",
  e=["hypothalamus"]),

Q("b", BE, "Beyin omurilik sıvısını (BOS) en çok üreten yapı hangisidir?",
  "Plexus choroideus", ["Granulationes arachnoideae", "Dura mater", "Sinus sagittalis superior", "Pia mater"],
  """BOS büyük ölçüde ventriküllerdeki koroid pleksuslarda üretilir (günde yaklaşık 500 ml). Araknoid granülasyonlar
  ise BOS'u venöz sinüslere geri emer.""",
  e=["ventriculi-cerebri"]),

Q("b", BE, "Lateral ventrikülleri üçüncü ventriküle bağlayan delik hangisidir?",
  "Foramen interventriculare (Monro)", ["Aqueductus mesencephali (Sylvius)", "Apertura mediana (Magendie)",
   "Apertura lateralis (Luschka)", "Canalis centralis"],
  """BOS lateral ventriküllerden Monro deliklerinden üçüncü ventriküle, oradan Sylvius kanalıyla dördüncü ventriküle geçer;
  Magendie ve Luschka açıklıklarından subaraknoid boşluğa çıkar.""",
  e=["ventriculi-cerebri"]),

# ------------------------------------------------------------------ temel: beyin sapı ve beyincik
Q("b", BS, "Beyin sapını oluşturan bölümler yukarıdan aşağıya hangi sıradadır?",
  "Mesencephalon – pons – medulla oblongata", ["Pons – mesencephalon – medulla oblongata",
   "Diencephalon – pons – medulla oblongata", "Mesencephalon – medulla oblongata – pons", "Thalamus – mesencephalon – pons"],
  """Beyin sapı yukarıdan aşağıya orta beyin (mesencephalon), pons ve medulla oblongata'dan oluşur; medulla foramen magnum
  düzeyinde omurilik ile devam eder.""",
  e=["mesencephalon", "pons", "medulla-oblongata"]),

Q("b", BS, "Solunum ve dolaşımın hayati merkezleri beyin sapının hangi bölümündedir?",
  "Medulla oblongata", ["Mesencephalon", "Cerebellum", "Thalamus", "Corpus callosum"],
  """Medulla oblongata'da solunum, kalp atımı ve damar tonusunu düzenleyen merkezler bulunur. Bu yüzden foramen magnum
  herniasyonu ile medullanın sıkışması öldürücü olabilir.""",
  e=["medulla-oblongata"]),

Q("b", BS, "Denge, kas tonusu ve hareketlerin koordinasyonunda görevli yapı hangisidir?",
  "Cerebellum", ["Pons", "Hypothalamus", "Corpus callosum", "Lobus occipitalis"],
  """Beyincik hareketin zamanlamasını ve uyumunu düzenler, dengeyi ve kas tonusunu korur. Hasarında ataksi, tremor ve
  denge bozukluğu görülür; bulgular lezyonla aynı taraftadır.""",
  e=["cerebellum"]),

Q("b", BS, "Cerebellum beyin sapına kaç çift pedinkül (sap) ile bağlanır?",
  "3 (üst, orta ve alt)", ["1", "2", "4", "5"],
  """Pedunculus cerebellaris superior mezensefalona, medius ponsa, inferior medulla oblongata'ya bağlanır. En büyüğü
  ponstan gelen lifleri taşıyan orta pedinküldür.""",
  e=["cerebellum"]),

# ------------------------------------------------------------------ temel: omurilik ve zarlar
Q("b", OM, "Yetişkinde omurilik (conus medullaris) genellikle hangi omur düzeyinde sona erer?",
  "L1–L2", ["T8", "L4–L5", "S2", "C7"],
  """Yetişkinde omurilik L1–L2 düzeyinde conus medullaris ile sona erer; yenidoğanda daha aşağıda, yaklaşık L3'tedir.
  Altında yalnızca sinir kökleri (cauda equina) bulunur.""",
  e=["medulla-spinalis"]),

Q("b", OM, "Beyin ve omuriliği saran zarlar dıştan içe hangi sıradadır?",
  "Dura mater – arachnoidea mater – pia mater", ["Pia mater – arachnoidea mater – dura mater",
   "Arachnoidea mater – dura mater – pia mater", "Dura mater – pia mater – arachnoidea mater",
   "Pia mater – dura mater – arachnoidea mater"],
  """En dışta kalın ve sert dura mater, ortada ağımsı arachnoidea, en içte beyin yüzeyine sıkıca yapışan ince pia mater
  bulunur.""",
  e=["meninges"]),

Q("b", OM, "Beyin omurilik sıvısı hangi aralıkta dolaşır?",
  "Arachnoidea ile pia mater arasında (spatium subarachnoideum)", ["Dura ile arachnoidea arasında (spatium subdurale)",
   "Dura ile kemik arasında (spatium epidurale)", "Pia mater ile beyin dokusu arasında", "Duranın iki yaprağı arasında"],
  """BOS subaraknoid aralıkta dolaşır; bu aralık sisternalarda genişler. Lomber ponksiyonda iğne bu aralığa girilerek
  BOS alınır.""",
  e=["meninges"]),

Q("b", OM, "Lomber ponksiyon yetişkinde genellikle hangi aralıktan yapılır?",
  "L3–L4 veya L4–L5 omurları arası", ["T12–L1 arası", "L1–L2 arası", "T10–T11 arası", "C7–T1 arası"],
  """Omurilik L1–L2'de sona erdiği için iğne daha aşağıdan, iliak kristaları birleştiren hattın (yaklaşık L4) çevresinden
  girilir; burada yalnızca cauda equina kökleri vardır ve iğneden kaçarlar.""",
  e=["cauda-equina", "medulla-spinalis"]),

Q("b", OM, "Conus medullaris'in altında, omurga kanalında aşağı inen sinir köklerinin oluşturduğu demete ne ad verilir?",
  "Cauda equina", ["Filum terminale", "Plexus sacralis", "Truncus sympathicus", "Intumescentia lumbosacralis"],
  """Omurilik omurgadan kısa olduğu için alt lomber ve sakral kökler kendi deliklerine ulaşmak üzere aşağı iner ve at kuyruğuna
  benzeyen cauda equina'yı oluşturur. Filum terminale conus'tan kuyruk sokumuna uzanan pial bir iplikçiktir.""",
  e=["cauda-equina"]),

# ------------------------------------------------------------------ temel: kranial sinirler
Q("b", KS, "Kaç çift kranial (kafa çifti) sinir vardır?",
  "12", ["10", "11", "31", "8"],
  """On iki çift kranial sinir beyinden ve beyin sapından çıkar: I olfactorius'tan XII hypoglossus'a kadar. Spinal sinirler
  ise 31 çifttir.""",
  e=["n-olfactorius", "n-hypoglossus"]),

Q("b", KS, "Göz kapağını kaldıran kasın ve göz kaslarının çoğunun siniri hangisidir?",
  "N. oculomotorius (III)", ["N. trochlearis (IV)", "N. abducens (VI)", "N. facialis (VII)", "N. trigeminus (V)"],
  """N. oculomotorius m. levator palpebrae superioris'i, m. rectus superior, inferior ve medialis'i ve m. obliquus inferior'u
  uyarır; ayrıca göz bebeğini daraltan parasempatik lifleri taşır.""",
  e=["n-oculomotorius"]),

Q("b", KS, "M. rectus lateralis'i (gözü dışa çeviren kas) hangi sinir uyarır?",
  "N. abducens (VI)", ["N. oculomotorius (III)", "N. trochlearis (IV)", "N. ophthalmicus", "N. facialis (VII)"],
  """N. abducens yalnızca m. rectus lateralis'i uyarır. Felcinde göz dışa döndürülemez ve yana bakışta çift görme olur
  (kısaca: LR6, SO4, geri kalanı III).""",
  e=["n-abducens"]),

Q("b", KS, "Yüz derisinin duyusunu taşıyan ve çiğneme kaslarını uyaran sinir hangisidir?",
  "N. trigeminus (V)", ["N. facialis (VII)", "N. glossopharyngeus (IX)", "N. hypoglossus (XII)", "N. accessorius (XI)"],
  """N. trigeminus'un üç dalı (oftalmik, maksiller, mandibular) yüz derisinin duyusunu alır; mandibular dalı ayrıca
  m. masseter, m. temporalis ve pterygoid kaslar gibi çiğneme kaslarını uyarır.""",
  e=["n-trigeminus"]),

Q("b", KS, "Mimik (yüz ifadesi) kaslarının siniri hangisidir?",
  "N. facialis (VII)", ["N. trigeminus (V)", "N. hypoglossus (XII)", "N. vagus (X)", "N. accessorius (XI)"],
  """Yüz ifadesini oluşturan kasların tümü n. facialis'ten innerve olur. Çiğneme kasları ise n. trigeminus'tan uyarılır;
  bu ayrım sık karıştırılır.""",
  e=["n-facialis"]),

Q("b", KS, "Dil kaslarının (m. palatoglossus hariç) motor siniri hangisidir?",
  "N. hypoglossus (XII)", ["N. glossopharyngeus (IX)", "N. lingualis", "N. vagus (X)", "N. facialis (VII)"],
  """N. hypoglossus dilin iç ve dış kaslarının hepsini uyarır, yalnızca m. palatoglossus n. vagus'tan gelir. Tek taraflı
  felcinde dil dışarı çıkarıldığında felçli tarafa sapar.""",
  e=["n-hypoglossus"]),

Q("b", KS, "M. sternocleidomastoideus ve m. trapezius'u uyaran kranial sinir hangisidir?",
  "N. accessorius (XI)", ["N. vagus (X)", "N. hypoglossus (XII)", "N. facialis (VII)", "Plexus brachialis"],
  """N. accessorius foramen jugulare'den çıkar, m. sternocleidomastoideus'u deler ve boynun arka üçgenini geçerek
  m. trapezius'a ulaşır. Boyun diseksiyonunda arka üçgende yaralanabilir.""",
  e=["n-accessorius"]),

Q("b", KS, "Göğüs ve karın organlarının çoğuna parasempatik lif veren kranial sinir hangisidir?",
  "N. vagus (X)", ["N. glossopharyngeus (IX)", "N. phrenicus", "N. accessorius (XI)", "N. oculomotorius (III)"],
  """N. vagus en uzun seyirli kranial sinirdir; kalbe, akciğerlere ve sindirim kanalına (yaklaşık transvers kolonun sol
  üçte birine kadar) parasempatik lif verir.""",
  e=["n-vagus", "systema-autonomicum"]),

Q("b", KS, "İşitme ve denge duyusunu taşıyan sinir hangisidir?",
  "N. vestibulocochlearis (VIII)", ["N. facialis (VII)", "N. glossopharyngeus (IX)", "N. trigeminus (V)", "N. abducens (VI)"],
  """N. vestibulocochlearis'in koklear bölümü işitmeyi, vestibüler bölümü dengeyi taşır. N. facialis ile birlikte meatus
  acusticus internus'tan geçer.""",
  e=["n-vestibulocochlearis"]),

# ------------------------------------------------------------------ temel: spinal sinirler ve pleksuslar
Q("b", SS, "Kaç çift spinal sinir vardır?",
  "31", ["12", "24", "33", "30"],
  """8 servikal, 12 torakal, 5 lomber, 5 sakral ve 1 koksigeal olmak üzere 31 çift spinal sinir vardır. Servikal omur 7
  olduğu hâlde 8 servikal sinir bulunur.""",
  e=["ganglion-spinale"]),

Q("b", SS, "Plexus brachialis hangi spinal sinirlerin ön dallarından oluşur?",
  "C5–T1", ["C1–C4", "C3–C7", "T1–T6", "L1–L4"],
  """Plexus brachialis C5–T1 ön dallarından oluşur ve kökler, trunkuslar, bölümler, kordlar ve dallar halinde düzenlenir;
  üst ekstremitenin tüm motor ve duyu innervasyonunu sağlar.""",
  e=["plexus-brachialis"]),

Q("b", SS, "Diyaframın motor siniri hangisidir?",
  "N. phrenicus (C3–C5)", ["N. vagus", "Nn. intercostales", "N. accessorius", "Truncus sympathicus"],
  """N. phrenicus boyunda m. scalenus anterior'un önünden iner ve diyaframı uyarır. Diyaframdan kaynaklanan ağrı aynı
  segmentlerin dermatomu olan omuza yansır.""",
  e=["n-phrenicus"]),

Q("b", SS, "Vücudun en kalın ve en uzun siniri hangisidir?",
  "N. ischiadicus", ["N. femoralis", "N. tibialis", "N. medianus", "N. obturatorius"],
  """N. ischiadicus L4–S3 köklerinden gelir, foramen ischiadicum majus'tan çıkar ve uyluğun arkasında iner; genellikle
  fossa poplitea'nın üstünde n. tibialis ve n. fibularis communis'e ayrılır.""",
  e=["n-ischiadicus"]),

Q("b", SS, "Uyluğun ön kaslarını (m. quadriceps femoris) uyaran sinir hangisidir?",
  "N. femoralis", ["N. obturatorius", "N. ischiadicus", "N. tibialis", "N. pudendus"],
  """N. femoralis (L2–L4) lacuna musculorum'dan uyluğa geçer ve m. quadriceps femoris, m. sartorius ve m. pectineus'u
  uyarır; hasarında diz ekstansiyonu ve patella refleksi kaybolur.""",
  e=["n-femoralis"]),

Q("b", SS, "Uyluğun iç (adduktor) kaslarının çoğunu uyaran sinir hangisidir?",
  "N. obturatorius", ["N. femoralis", "N. ischiadicus", "N. pudendus", "N. genitofemoralis"],
  """N. obturatorius (L2–L4) canalis obturatorius'tan geçerek uyluğun medial bölmesine girer ve adduktor kasların çoğunu
  uyarır; m. adductor magnus'un hamstring bölümü ise n. ischiadicus'tan innerve olur.""",
  e=["n-obturatorius"]),

Q("b", SS, "Karpal tünel sendromunda sıkışan sinir hangisidir?",
  "N. medianus", ["N. ulnaris", "N. radialis", "N. musculocutaneus", "N. axillaris"],
  """N. medianus el bileğinde retinaculum musculorum flexorum'un altından, fleksör tendonlarla birlikte karpal tünelden
  geçer. Sıkışmasında ilk üç buçuk parmakta uyuşma ve tenar kaslarda zayıflık olur.""",
  e=["n-medianus"]),

Q("b", SS, "Dirseğin iç yanı çarptığında elin küçük parmak tarafında karıncalanmaya yol açan sinir hangisidir?",
  "N. ulnaris", ["N. medianus", "N. radialis", "N. musculocutaneus", "N. cutaneus antebrachii lateralis"],
  """N. ulnaris dirsekte epicondylus medialis'in arkasında deri altında seyreder ('komik kemik'). Darbe ya da sıkışma
  4. ve 5. parmakta karıncalanma yapar.""",
  e=["n-ulnaris"]),

Q("b", SS, "Kolun arka kası m. triceps brachii'yi uyaran sinir hangisidir?",
  "N. radialis", ["N. ulnaris", "N. medianus", "N. axillaris", "N. musculocutaneus"],
  """N. radialis kolun ve önkolun arka (ekstansör) kaslarının tümünü uyarır. Humerus cisminin kırıklarında sulcus nervi
  radialis'te yaralanabilir ve el bileği düşüklüğü gelişir.""",
  e=["n-radialis"]),

Q("b", SS, "M. deltoideus'u uyaran sinir hangisidir?",
  "N. axillaris", ["N. radialis", "N. suprascapularis", "N. musculocutaneus", "N. thoracicus longus"],
  """N. axillaris (C5–C6) humerusun collum chirurgicum'u çevresinde dolanır ve m. deltoideus ile m. teres minor'u uyarır.
  Collum chirurgicum kırıkları ve omuz çıkıklarında yaralanabilir.""",
  e=["n-axillaris"]),

# ------------------------------------------------------------------ temel: otonom sinir sistemi
Q("b", OT, "Sempatik preganglioner nöronların hücre gövdeleri omuriliğin hangi segmentlerindedir?",
  "T1–L2 (lateral boynuz)", ["C1–C8", "S2–S4", "L3–S1", "Yalnız beyin sapı çekirdekleri"],
  """Sempatik sistem torakolomber çıkışlıdır: preganglioner nöronlar T1–L2 segmentlerinin lateral boynuzundadır. Lifleri
  ön kök ve ramus communicans albus ile sempatik gövdeye ulaşır.""",
  e=["systema-autonomicum", "truncus-sympathicus"]),

Q("b", OT, "Parasempatik sistemin lifleri hangi bölgelerden çıkar?",
  "Beyin sapı (III, VII, IX, X) ve S2–S4 (kraniyosakral)", ["T1–L2 (torakolomber)", "Yalnız beyin sapından",
   "Yalnız S2–S4 segmentlerinden", "C5–T1 segmentlerinden"],
  """Parasempatik sistem kraniyosakral çıkışlıdır: III, VII, IX ve X. kranial sinirlerle ve S2–S4 segmentlerinden çıkan
  pelvik splanknik sinirlerle dağılır.""",
  e=["systema-autonomicum"]),

Q("b", OT, "'Savaş ya da kaç' tepkisinde göz bebeği nasıl değişir ve bunu hangi sistem yapar?",
  "Genişler (midriyazis) – sempatik sistem", ["Daralır (miyozis) – sempatik sistem",
   "Genişler (midriyazis) – parasempatik sistem", "Daralır (miyozis) – parasempatik sistem", "Değişmez – somatik sistem"],
  """Sempatik uyarı m. dilatator pupillae'yi kasarak göz bebeğini genişletir. Parasempatik lifler (n. oculomotorius) ise
  m. sphincter pupillae ile göz bebeğini daraltır.""",
  e=["systema-autonomicum"]),

# ------------------------------------------------------------------ fakülte
Q("f", SS, "Spinal ganglionda (ganglion spinale) hangi nöronların hücre gövdeleri bulunur?",
  "Psödounipolar duyusal nöronlar", ["Multipolar motor nöronlar", "Sempatik preganglioner nöronlar",
   "Parasempatik postganglioner nöronlar", "Ara nöronlar (internöronlar)"],
  """Arka kök üzerindeki spinal ganglionda periferden gelen duyuyu omuriliğe taşıyan psödounipolar nöronlar bulunur;
  bu ganglionda sinaps yapılmaz.""",
  e=["ganglion-spinale"]),

Q("f", OT, "Sempatik gövde ganglionlarına giden preganglioner lifler spinal sinirden hangi dal ile ayrılır?",
  "Ramus communicans albus", ["Ramus communicans griseus", "Ramus meningeus", "Ramus dorsalis", "Radix posterior"],
  """Miyelinli preganglioner lifler ramus communicans albus ile sempatik gövdeye girer (yalnız T1–L2 düzeyinde bulunur).
  Miyelinsiz postganglioner lifler ramus communicans griseus ile spinal sinire geri döner.""",
  e=["truncus-sympathicus"]),

Q("f", SS, "N. pudendus pelvisten hangi delikten çıkar ve perineye hangi delikten girer?",
  "Foramen ischiadicum majus'tan çıkar, foramen ischiadicum minus'tan girer",
  ["Foramen ischiadicum minus'tan çıkar, foramen ischiadicum majus'tan girer",
   "Canalis obturatorius'tan çıkar, foramen ischiadicum minus'tan girer",
   "Foramen ischiadicum majus'tan çıkar, canalis inguinalis'ten girer",
   "Hiatus sacralis'ten çıkar, foramen ischiadicum minus'tan girer"],
  """N. pudendus (S2–S4) m. piriformis'in altından foramen ischiadicum majus ile pelvisten çıkar, lig. sacrospinale'nin
  arkasından dolanır ve foramen ischiadicum minus ile perineye girerek canalis pudendalis'te (Alcock) ilerler.""",
  e=["n-pudendus"]),

Q("f", SS, "N. fibularis communis en sık nerede yaralanır?",
  "Collum fibulae çevresinde", ["Malleolus medialis'in arkasında", "Canalis adductorius'ta",
   "Foramen ischiadicum majus'ta", "Tarsal tünelde"],
  """N. fibularis communis fibula başının hemen altında, collum fibulae'yi sararak yüzeyel seyreder. Kırık, alçı baskısı
  ya da bacak bacak üstüne atma burada sinire hasar verir ve düşük ayak gelişir.""",
  e=["n-fibularis-communis"]),
]
