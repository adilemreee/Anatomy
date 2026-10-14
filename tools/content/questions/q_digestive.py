from qcommon import Q, write

AY = "Ağız ve yutak"
SK = "Sindirim kanalı"
KS = "Karaciğer, safra yolları ve pankreas"
PR = "Periton"

questions = [
# ------------------------------------------------------------------ Ağız ve yutak
Q("f", AY, "Parotis bezinin kanalı (ductus parotideus, Stensen) ağız boşluğunda nereye açılır?",
  "Üst 2. büyük azı dişinin karşısındaki yanak mukozasına",
  ["Dil altındaki caruncula sublingualis'e", "Alt 1. küçük azı dişinin karşısına", "Yumuşak damağın kenarına", "Dil kökündeki foramen caecum'a"],
  """Stensen kanalı masseter kasının ön kenarını dolanır, m. buccinator'u deler ve üst 2. büyük azı dişinin
  karşısındaki papilla parotidea'dan ağız vestibülüne açılır. Kabakulakta bu papilla kızarık ve ödemli olabilir.""",
  e=["glandula-parotidea", "m-buccinator"]),

Q("t", AY, "Aşağıdaki yapılardan hangisi parotis bezinin içinden geçmez?",
  "A. facialis",
  ["N. facialis", "V. retromandibularis", "A. carotis externa", "A. temporalis superficialis'in başlangıcı"],
  """Parotis içinde yüzeyelden derine n. facialis (ve dalları), v. retromandibularis ve a. carotis externa bulunur;
  ECA bez içinde a. temporalis superficialis ve a. maxillaris'e ayrılır. A. facialis ise submandibular bezle
  ilişkilidir ve parotise girmez.""",
  e=["glandula-parotidea", "n-facialis", "a-carotis-externa"]),

Q("fv", AY, """Kabakulak tanılı çocukta parotis bölgesinde şişlik ve çiğnerken artan şiddetli ağrı var. Ağrının
bu kadar şiddetli olmasının anatomik nedeni nedir?""",
  "Bezin sıkı ve esnemeyen parotis fasyasıyla sarılı olması",
  ["Bezin içinden n. trigeminus'un ana gövdesinin geçmesi", "Bezin kemik bir kanal içinde yer alması",
   "Kanalının ağız tabanına açılması", "Bezin perikondriyumla örtülü olması"],
  """Parotis, derin servikal fasyanın yüzeyel yaprağından gelen sıkı bir kapsülle sarılıdır. Şişen bez bu
  kapsülü gerer; ağrı n. auriculotemporalis ve n. auricularis magnus aracılığıyla hissedilir ve çiğnemeyle artar.""",
  e=["glandula-parotidea"]),

Q("t", AY, "Ductus submandibularis (Wharton) ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Ağız tabanında caruncula sublingualis'e açılır ve seyri sırasında n. lingualis tarafından alttan dolanılır.",
  ["Üst 2. büyük azı karşısına açılır.", "M. buccinator'u delerek ağız vestibülüne açılır.",
   "N. hypoglossus kanalın içinden geçer.", "Seröz salgı taşıdığı için taş oluşumu nadirdir."],
  """Submandibular kanal mylohyoideus'un üstünde, hyoglossus'un yanında öne ilerler ve frenulum linguae'nin
  iki yanındaki karunkullara açılır. N. lingualis kanalın altından dıştan içe doğru geçer; kanal cerrahisinde
  sinir yaralanabilir.""",
  e=["glandula-submandibularis", "n-trigeminus"]),

Q("fv", AY, """Yemek yerken çene altında ağrılı şişlik olan ve yemekten sonra şişliği azalan hastada tükürük taşı
düşünülüyor. Taşın en sık görüldüğü bez ve nedeni hangisidir?""",
  "Submandibular bez; salgısı daha viskoz ve alkalidir, kanalı yukarı doğru uzun bir yol izler.",
  ["Parotis bezi; salgısı tamamen müköz olduğu için.", "Sublingual bez; tek ve geniş bir kanalı olduğu için.",
   "Parotis bezi; kanalı aşağı doğru seyrettiği için.", "Küçük tükürük bezleri; sayıları çok olduğu için."],
  """Tükürük taşlarının yaklaşık %80'i submandibular bezde görülür. Salgının müsin ve kalsiyumdan zengin olması,
  kanalın uzun olması ve yerçekimine karşı yukarı doğru akım taş oluşumunu kolaylaştırır.""",
  e=["glandula-submandibularis"]),

Q("t", AY, "Dilin lenf drenajı ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Dil ucu submental, ön 2/3'ün yan kenarları submandibular, arka 1/3 her iki taraftaki derin servikal düğümlere drene olur.",
  ["Dilin tamamı yalnızca aynı taraftaki submandibular düğümlere drene olur.", "Dil lenfi doğrudan ductus thoracicus'a açılır.",
   "Dil ucu parotis düğümlerine drene olur.", "Dilin arka 1/3'ü lenfatik içermez."],
  """Dilin orta hattına yakın ve arka kısımlarının lenfi iki taraflı drene olur; bu nedenle dil kanserleri karşı
  taraf boyun düğümlerine de yayılabilir. Juguloomohyoid ve jugulodigastrik düğümler dilin önemli düğümleridir.""",
  e=["lingua", "nodi-cervicales", "nodus-jugulodigastricus"]),

Q("t", AY, "Dilin ön 2/3'ü ile arka 1/3'ünün farklı sinirlerle duyu almasının embriyolojik açıklaması nedir?",
  "Ön 2/3 birinci faringeal arktan, arka 1/3 üçüncü (ve dördüncü) arktan gelişir.",
  ["Ön 2/3 ektodermden, arka 1/3 nöral kristadan gelişir.", "Ön 2/3 ikinci arktan, arka 1/3 birinci arktan gelişir.",
   "Dilin tamamı oksipital miyotomlardan gelişir.", "Ön 2/3 endodermden, arka 1/3 mezodermden gelişir."],
  """Dilin ön kısmı 1. arkın lingual çıkıntılarından gelişir ve genel duyusu V3 (n. lingualis) ile taşınır; tat
  ise chorda tympani (VII) ile gelir. Arka kısım 3. arkın hipobrankiyal çıkıntısından gelişir ve IX ile innerve
  edilir. Dil kasları ise oksipital miyotomlardan gelir ve XII ile innerve edilir.""",
  e=["lingua", "n-glossopharyngeus", "n-hypoglossus"]),

Q("tv", AY, """Yaşlı hastada yutma güçlüğü, yemeklerin geri gelmesi, ağız kokusu ve boyunda gurultulu bir şişlik
var. Baryumlu grafide farinksin arka duvarından çıkan kese görülüyor. Kese hangi zayıf bölgeden çıkar?""",
  "M. constrictor pharyngis inferior'un tirofaringeal ve krikofaringeal bölümleri arasındaki Killian üçgeni",
  ["Üst ve orta konstriktörler arası", "Özofagusun diyaframdan geçtiği yer", "Recessus piriformis'in tabanı", "Tonsiller fossa"],
  """Zenker divertikülü bir pulsiyon divertikülüdür: krikofaringeal kas yeterince gevşemezse basınç Killian
  üçgenindeki mukozayı arkaya iter. Kese genellikle sol tarafta belirgin olur.""",
  e=["pharynx", "oesophagus"]),

Q("tv", AY, """Balık yerken boğazına kılçık kaçan hastada kılçık gırtlak girişinin yanındaki çukurda saptanıyor;
çıkarma sırasında aynı tarafta gırtlak mukozasında his kaybı gelişiyor. Kılçığın takıldığı yer ve
yaralanan sinir hangisidir?""",
  "Recessus piriformis – n. laryngeus internus",
  ["Vallecula epiglottica – n. hypoglossus", "Tonsiller fossa – n. glossopharyngeus",
   "Recessus piriformis – n. laryngeus recurrens", "Nazofarinks – n. maxillaris"],
  """Piriform girinti laringofarinksin gırtlak girişinin iki yanındaki cebidir; yabancı cisimler burada sıklıkla
  takılır. N. laryngeus internus bu girintinin mukozası altında seyreder ve yaralanmasında gırtlağın supraglottik
  duyusu kaybolur.""",
  e=["pharynx", "larynx", "n-vagus"]),

Q("f", AY, "Öğürme (gag) refleksinin afferent ve efferent kolları hangileridir?",
  "Afferent: n. glossopharyngeus – Efferent: n. vagus",
  ["Afferent: n. vagus – Efferent: n. glossopharyngeus", "Afferent: n. trigeminus – Efferent: n. facialis",
   "Afferent: n. hypoglossus – Efferent: n. vagus", "Afferent: n. facialis – Efferent: n. glossopharyngeus"],
  """Farinksin arka duvarına dokunulması IX ile algılanır; yanıt olarak X'un innerve ettiği farinks ve yumuşak damak
  kasları kasılır. Refleksin kaybı IX veya X lezyonunu düşündürür.""",
  e=["pharynx", "n-glossopharyngeus", "n-vagus"]),

Q("f", AY, "Yumuşak damak kaslarından hangisi n. mandibularis ile innerve edilir?",
  "M. tensor veli palatini",
  ["M. levator veli palatini", "M. uvulae", "M. palatoglossus", "M. palatopharyngeus"],
  """Tensor veli palatini birinci faringeal ark kökenlidir ve V3 ile innerve edilir; hamulus pterygoideus etrafından
  dönerek damağı gerer ve tuba auditiva'yı açar. Diğer yumuşak damak kasları plexus pharyngeus (X) ile innerve edilir.""",
  e=["palatum", "tuba-auditiva", "n-trigeminus"]),

# ------------------------------------------------------------------ Sindirim kanalı
Q("f", SK, "Özofagusun fizyolojik darlıkları kesici dişlerden itibaren yaklaşık hangi uzaklıklardadır?",
  "15 cm (krikofaringeal), 25 cm (aort kemeri–sol ana bronş), 40 cm (diyafram)",
  ["10 cm, 20 cm ve 30 cm", "15 cm, 30 cm ve 50 cm", "20 cm, 35 cm ve 45 cm", "5 cm, 15 cm ve 25 cm"],
  """Bu darlıklarda yutulan yabancı cisimler ve koroziv maddeler takılır; endoskopide referans noktalarıdır.
  Özofagus ~25 cm uzunluğundadır ve C6'da başlayıp T11 düzeyinde mideye açılır.""",
  e=["oesophagus"]),

Q("t", SK, "Özofagusun kas tabakası ile ilgili hangisi doğrudur?",
  "Üst 1/3'ü çizgili, orta 1/3'ü karışık, alt 1/3'ü düz kastır.",
  ["Tamamı çizgili kastır.", "Tamamı düz kastır.", "Üst 1/3'ü düz, alt 1/3'ü çizgili kastır.", "Yalnızca sirküler kas tabakası vardır."],
  """Özofagus geçiş kas yapısına sahiptir. Akalazyada alt özofagus sfinkteri gevşeyemez ve myenterik pleksustaki
  ganglion hücreleri azalmıştır. Özofagusun seroza tabakası yoktur; perforasyonları hızla mediastinite yol açar.""",
  e=["oesophagus"]),

Q("fv", SK, """Göğüs kemiği arkasında yanma ve yatınca artan ekşi su gelmesi şikâyeti olan obez hastada
endoskopide gastroözofageal bileşkenin diyafram üstüne yer değiştirdiği görülüyor. Bu durum hangisidir?""",
  "Kayan (sliding, tip I) hiatus hernisi",
  ["Paraözofageal (tip II) hiatus hernisi", "Bochdalek hernisi", "Morgagni hernisi", "Zenker divertikülü"],
  """Hiatus hernilerinin büyük çoğunluğu kayan tiptedir: gastroözofageal bileşke ve midenin üst kısmı özofagus
  hiatusundan yukarı kayar ve reflüye yatkınlık oluşur. Paraözofageal tipte bileşke yerindedir, fundus yanından
  yukarı çıkar ve strangülasyon riski taşır.""",
  e=["oesophagus", "gaster", "diaphragma"]),

Q("fv", SK, """6 haftalık erkek bebekte beslenmeden sonra fışkırır tarzda safrasız kusma var; epigastriumda zeytin
büyüklüğünde kitle ele geliyor. Sorunlu yapı hangisidir?""",
  "Pilor kası (m. sphincter pylori) hipertrofisi",
  ["Duodenumun ikinci bölümünün atrezisi", "Alt özofagus sfinkteri", "İleoçekal valv", "Halka pankreas"],
  """İnfantil hipertrofik pilor stenozu pilorun sirküler kas tabakasının kalınlaşmasıdır. Tıkanıklık papilla
  major'un proksimalinde olduğu için kusma safrasızdır; hipokloremik metabolik alkaloz gelişir. Tedavi
  piloromiyotomidir.""",
  e=["gaster"]),

Q("t", SK, "Midede HCl ve intrensek faktör salgılayan parietal hücreler en yoğun nerede bulunur?",
  "Fundus ve korpus",
  ["Antrum", "Pilor kanalı", "Kardiya", "Duodenal bulbus"],
  """Parietal (oksintik) ve esas (şef) hücreler fundus ve gövdedeki bezlerde bulunur. Gastrin salgılayan G hücreleri
  antrumdadır. Total gastrektomi sonrası intrensek faktör kaybı nedeniyle ömür boyu B12 desteği gerekir.""",
  e=["gaster"]),

Q("f", SK, "Papilla duodeni major duodenumun hangi bölümündedir?",
  "İkinci (inen) bölümün arka-iç duvarı",
  ["Birinci (üst) bölümün ön duvarı", "Üçüncü (yatay) bölümün alt duvarı", "Dördüncü (çıkan) bölüm", "Flexura duodenojejunalis"],
  """Koledok ve ana pankreas kanalı ampulla hepatopancreatica'yı oluşturarak inen duodenumun ortasında papilla
  major'a açılır. Bu nokta ön ve orta bağırsak arasındaki sınıra yakındır.""",
  e=["duodenum", "ductus-choledochus"]),

Q("t", SK, "Duodenum için aşağıdakilerden hangisi doğrudur?",
  "Yalnızca birinci bölümünün başlangıcı (bulbus) intraperitonealdir; geri kalanı retroperitonealdir.",
  ["Tamamen intraperitonealdir ve mezenteri vardır.", "Üçüncü bölümü SMA'nın önünden geçer.",
   "Treitz bağı duodenumun birinci bölümünü asar.", "Tamamı SMA tarafından beslenir."],
  """Duodenal bulbus omentum minus'a bağlıdır ve hareketlidir; bölümlerin geri kalanı arka karın duvarına
  yapışıktır. Yatay bölüm SMA ile aorta arasından geçer. Papilla major'a kadar çölyak, sonrası SMA dallarıyla
  beslenir.""",
  e=["duodenum", "peritoneum"]),

Q("t", SK, "Jejunumu ileumdan ayırt etmeye yarayan özellik hangisidir?",
  "Uzun vasa recta ve az sayıda büyük arter arkadı",
  ["Kısa vasa recta ve çok sayıda arkad", "Peyer plaklarının belirgin olması", "Mezenterinde bol yağ bulunması", "Plicae circulares'in az ve alçak olması"],
  """Jejunum: kalın duvar, geniş lümen, sık plicae circulares, uzun vasa recta, 1–2 sıra arkad ve az mezenter yağı.
  İleum: ince duvar, Peyer plakları, kısa vasa recta, çok sıra arkad ve bol mezenter yağı.""",
  e=["jejunum", "ileum", "a-mesenterica-superior"]),

Q("tv", SK, """2 yaşında çocuk ağrısız, koyu kırmızı renkli rektal kanamayla getiriliyor. Teknesyum-99m sintigrafisinde
sağ alt kadranda tutulum var. En olası tanı ve kanamanın nedeni hangisidir?""",
  "Meckel divertikülü – ektopik mide mukozasının asit salgısıyla oluşan ülser",
  ["Apendisit – apendiks perforasyonu", "İnvajinasyon – bağırsak iskemisi",
   "Juvenil polip – polip otoamputasyonu", "Hirschsprung hastalığı – enterokolit"],
  """Meckel divertikülü ductus vitellinus kalıntısıdır ve ileumun antimezenterik kenarında, ileoçekal valvin yaklaşık
  60 cm proksimalindedir. İçindeki ektopik mide mukozası asit salgılayarak komşu ileum mukozasında ülser yapar;
  sintigrafi bu mukozayı gösterir.""",
  e=["ileum"]),

Q("tv", SK, """Crohn hastalığı nedeniyle terminal ileum rezeksiyonu yapılan hastada aylar sonra makrositer anemi,
nöropati ve sulu ishal gelişiyor. Bu bulguların açıklaması nedir?""",
  "B12 vitamini ve konjuge safra asitleri terminal ileumda emildiği için emilim bozulmuştur.",
  ["Demir duodenumda emildiği için bozulmuştur.", "Folat yalnızca kolonda emilir.",
   "Terminal ileum intrensek faktör salgılar.", "Kalsiyum ve magnezyum yalnızca ileumda emilir."],
  """Terminal ileum B12–intrensek faktör kompleksinin ve safra asitlerinin emilim yeridir. Safra asitleri kolona
  ulaşınca sekretuvar ishal yapar; kronik kayıp yağ emilim bozukluğu ve safra taşına yatkınlık oluşturur.""",
  e=["ileum", "intestinum-tenue"]),

Q("f", SK, "Kalın bağırsağı ince bağırsaktan ayırt ettiren yapılar hangileridir?",
  "Taeniae coli, haustra ve appendices epiploicae",
  ["Plicae circulares, villuslar ve Peyer plakları", "Brunner bezleri ve plicae circulares", "Mezenter ve vasa recta", "Kerckring kıvrımları ve lakteal damarlar"],
  """Kalın bağırsağın dış uzunlamasına kası üç şerit (taenia) hâlindedir; bunlar kısa olduğundan duvar keseler
  (haustra) oluşturur. Appendices epiploicae seroza altındaki yağ püsküleridir. Rektum, anal kanal ve apendikste
  bu yapılar yoktur.""",
  e=["intestinum-crassum", "taeniae-coli"]),

Q("fv", SK, """Göbek çevresinde başlayıp sağ alt kadrana yerleşen ağrısı olan hastada en hassas nokta SIAS ile
göbeği birleştiren çizgide aranır. McBurney noktası nerededir?""",
  "Çizginin dış 1/3'ü ile iç 2/3'ünün birleştiği yer",
  ["Çizginin tam ortası", "Çizginin iç 1/3'ü ile dış 2/3'ünün birleştiği yer", "Göbeğin hemen altı", "SIAS'ın hemen üstü"],
  """McBurney noktası apendiks tabanının yüzeydeki izdüşümüdür. Apendiksin ucu ise çok değişken yerleşimlidir;
  en sık retroçekal, ikinci sıklıkla pelvik konumdadır.""",
  e=["appendix-vermiformis", "caecum"]),

Q("t", SK, "Apendektomide apendiksin tabanını bulmak için izlenen yapı hangisidir?",
  "Çekumun ön yüzündeki taenia libera",
  ["A. ileocolica'nın ana gövdesi", "İleumun antimezenterik kenarı", "Sağ üreter", "Lig. inguinale"],
  """Üç taenia coli çekumun tabanında apendiksin kökünde birleşir. Ön (serbest) taenia izlenerek apendiks kökü
  kolayca bulunur; apendiksin ucu nerede olursa olsun kökü bu noktadadır.""",
  e=["appendix-vermiformis", "taeniae-coli", "caecum"]),

Q("t", SK, "Distal kolon tıkanıklığında ileoçekal valv yeterliyse ilk perfore olan bölüm neden çekumdur?",
  "En geniş çaplı bölüm olduğundan duvar gerilimi en yüksektir (Laplace yasası).",
  ["Duvarı en kalın bölüm olduğu için.", "Kanlanması en zengin bölüm olduğu için.",
   "Retroperitoneal olduğu için.", "Taenia coli içermediği için."],
  """Laplace yasasına göre duvar gerilimi çapla doğru orantılıdır. Kapalı halka tıkanıklığında çekum çapı 12 cm'yi
  aştığında perforasyon riski belirgin artar.""",
  e=["caecum", "intestinum-crassum"]),

Q("fv", SK, """Kronik kabızlığı olan bakımevinde yaşayan yaşlı hastada ani karın şişliği ve gaz-gaita çıkaramama
var; düz grafide sol alt kadrandan yükselen büyük 'kahve çekirdeği' görünümü var. En olası tanı nedir?""",
  "Sigmoid volvulus",
  ["Çekum volvulusu", "İnce bağırsak tıkanıklığı", "Toksik megakolon", "Mide volvulusu"],
  """Sigmoid kolonun uzun ve dar köklü mezenteri onun kendi ekseni etrafında dönmesine izin verir. Kahve çekirdeği
  görünümü distandü kapalı halkayı gösterir; tedavide çoğunlukla endoskopik detorsiyon ilk adımdır.""",
  e=["colon-sigmoideum", "mesenterium"]),

Q("t", SK, "Orta bağırsak–arka bağırsak sınırı kalın bağırsağın neresine karşılık gelir?",
  "Colon transversum'un proksimal 2/3'ü ile distal 1/3'ünün birleşimine",
  ["İleoçekal valve", "Flexura coli dextra'ya", "Sigmoid kolonun başlangıcına", "Rektumun ortasına"],
  """Bu sınırın proksimalinde kanlanma SMA, parasempatik innervasyon n. vagus ve lenf drenajı süperior mezenterik
  düğümlerden; distalinde IMA, pelvik splanknik sinirler ve inferior mezenterik düğümlerden sağlanır.""",
  e=["colon-transversum", "a-mesenterica-superior", "a-mesenterica-inferior"]),

Q("t", SK, "Rektumun peritonla ilişkisi için aşağıdakilerden hangisi doğrudur?",
  "Üst 1/3'ü önde ve yanlarda, orta 1/3'ü yalnızca önde peritonla örtülüdür; alt 1/3'ünde periton yoktur.",
  ["Tamamı intraperitonealdir ve mezorektumu periton yapar.", "Tamamen peritonla sarılıdır.",
   "Yalnızca alt 1/3'ü peritonla örtülüdür.", "Rektum hiç peritonla ilişkili değildir."],
  """Rektumun alt kısmı periton yansımasının altında kalır; bu bölge erkekte rektovezikal, kadında rektouterin
  cebin tabanına karşılık gelir. Mezorektum rektumu saran yağ ve lenf dokusudur ve kanser cerrahisinde bütün
  olarak çıkarılır (total mezorektal eksizyon).""",
  e=["rectum", "peritoneum"]),

Q("fv", SK, """Dışkılama sırasında ağrısız, parlak kırmızı kanaması olan hastanın anoskopisinde pektinat çizginin
üstünde mor renkli şişlikler görülüyor. Bu şişliklerin ağrısız olmasının nedeni nedir?""",
  "Pektinat çizginin üstü otonom (visseral) liflerle innerve edilir.",
  ["Pektinat çizginin üstü n. pudendus ile innerve edilir.", "Bu bölgede hiç sinir yoktur.",
   "Bu venler sistemik dolaşıma açılır.", "Bölge çok katlı yassı epitelle örtülüdür."],
  """İç hemoroidler pektinat çizginin üstünde, a. rectalis superior dallarının girdiği yerlerdeki submukozal venöz
  yastıkçıklardır ve visseral innervasyon nedeniyle ağrısızdır. Dış hemoroidler çizginin altında, somatik
  innervasyonlu (n. rectalis inferior) bölgededir ve tromboze olunca çok ağrılıdır.""",
  e=["canalis-analis", "rectum"]),

Q("t", SK, "Anal kanalın pektinat çizginin altında kalan kısmından gelişen bir kanser ilk olarak hangi lenf düğümlerine yayılır?",
  "Yüzeyel inguinal lenf düğümleri",
  ["İnferior mezenterik lenf düğümleri", "İç iliak lenf düğümleri", "Paraaortik lenf düğümleri", "Çölyak lenf düğümleri"],
  """Pektinat çizginin altındaki deri kökenli bölüm yüzeyel inguinal düğümlere, üstündeki bölüm ise iç iliak ve
  inferior mezenterik düğümlere drene olur. Bu fark rektum ve anal kanal kanserlerinin evrelemesinde önemlidir.""",
  e=["canalis-analis", "nodi-inguinales"]),

Q("fv", SK, """Yenidoğan ilk 48 saatte mekonyum çıkaramıyor; rektal tuşe sonrası fışkırır tarzda gaita geliyor.
Rektal biyopside ganglion hücreleri yok. Bu hastalığın embriyolojik nedeni nedir?""",
  "Nöral krista hücrelerinin bağırsak duvarına göçünün distalde tamamlanamaması",
  ["Ductus vitellinus'un kapanmaması", "Orta bağırsağın rotasyon bozukluğu", "Ürorektal septumun gelişmemesi", "Ventral pankreas tomurcuğunun duodenumu sarması"],
  """Hirschsprung hastalığında nöral krista kökenli myenterik ve submukozal pleksus hücreleri rektumdan başlayarak
  proksimale doğru değişen uzunlukta bir segmentte yoktur. Aganglionik segment gevşeyemez ve proksimali genişler
  (megakolon).""",
  e=["rectum", "intestinum-crassum"]),

# ------------------------------------------------------------------ Karaciğer, safra yolları ve pankreas
Q("t", KS, "Karaciğerin peritonla örtülmeyen ve doğrudan diyaframa yapışan bölümü hangisidir?",
  "Area nuda (çıplak alan)",
  ["Porta hepatis", "Lobus quadratus", "Fossa vesicae biliaris", "Lig. teres hepatis"],
  """Koroner bağların iki yaprağı arasında kalan çıplak alan diyafram ile doğrudan temas eder. Karaciğer
  enfeksiyonları bu yolla diyafram ve plevraya yayılabilir; portokaval anastomozların küçük bir kısmı da buradadır.""",
  e=["hepar", "diaphragma"]),

Q("f", KS, "Porta hepatis'ten geçen yapılar hangileridir?",
  "V. portae, a. hepatica propria'nın dalları, hepatik kanallar, lenfatikler ve sinirler",
  ["Vv. hepaticae ve v. cava inferior", "Lig. venosum ve lig. teres hepatis", "A. cystica ve ductus cysticus", "A. gastrica sinistra ve v. gastrica sinistra"],
  """Porta hepatis karaciğerin alt yüzündeki H biçimli oluğun yatay koludur. Hepatik venler porta hepatis'ten
  geçmez; karaciğerin arka yüzünden doğrudan v. cava inferior'a açılır.""",
  e=["hepar", "v-portae-hepatis"]),

Q("f", KS, "Lig. teres hepatis ve lig. venosum hangi fetal yapıların kalıntılarıdır?",
  "Lig. teres hepatis: v. umbilicalis; lig. venosum: ductus venosus",
  ["Lig. teres hepatis: ductus venosus; lig. venosum: v. umbilicalis", "Lig. teres hepatis: a. umbilicalis; lig. venosum: ductus arteriosus",
   "Lig. teres hepatis: urachus; lig. venosum: v. umbilicalis", "Her ikisi de ductus arteriosus kalıntısıdır."],
  """Fetal oksijenli kan v. umbilicalis ile karaciğere gelir ve büyük kısmı ductus venosus aracılığıyla karaciğeri
  atlayıp VCI'ya geçer. Doğumdan sonra v. umbilicalis lig. teres hepatis'e (lig. falciforme'nin serbest kenarı),
  ductus venosus lig. venosum'a dönüşür.""",
  e=["hepar"]),

Q("t", KS, "Karaciğeri fonksiyonel olarak sağ ve sol yarıya ayıran çizgi (Cantlie çizgisi) hangi noktaları birleştirir?",
  "Safra kesesi yatağı ile v. cava inferior'u",
  ["Lig. falciforme ile lig. teres hepatis'i", "Porta hepatis ile lig. venosum'u",
   "Sağ hepatik ven ile safra kesesi fundusunu", "Kaudat lob ile kuadrat lobu"],
  """Fonksiyonel sağ ve sol lob portal ven, hepatik arter ve safra kanalının sağ ve sol dallarına göre ayrılır; bu
  sınır anatomik sınır olan lig. falciforme'nin daha sağındadır. Orta hepatik ven bu düzlemde seyreder.""",
  e=["segmenta-hepatis", "hepar"]),

Q("t", KS, "Budd–Chiari sendromunda (hepatik ven trombozu) hipertrofiye uğrayan karaciğer segmenti hangisidir ve nedeni nedir?",
  "Kaudat lob (segment I); venleri hepatik venlerden bağımsız olarak doğrudan VCI'ya açılır.",
  ["Segment IV; kuadrat lob ayrı bir arter alır.", "Segment VI; portal venin ilk dalını alır.",
   "Segment II; sol hepatik ven tıkanmaz.", "Segment VIII; diyaframdan ek kanlanma alır."],
  """Kaudat lob hem sağ hem sol portal dallardan beslenir ve kısa venleri doğrudan VCI'ya dökülür. Ana hepatik
  venler tıkandığında bu lobun çıkışı korunur ve kompansatuvar olarak büyür.""",
  e=["segmenta-hepatis", "v-cava-inferior"]),

Q("t", KS, "Calot (sistohepatik) üçgeninin sınırları ve önemli içeriği hangisidir?",
  "Ductus cysticus, ductus hepaticus communis ve karaciğerin alt yüzü; içinde a. cystica",
  ["Koledok, duodenum ve pankreas başı; içinde a. gastroduodenalis", "Lig. hepatoduodenale, VCI ve kaudat lob; içinde v. portae",
   "Ductus cysticus, koledok ve duodenum; içinde a. hepatica propria", "Safra kesesi fundusu, rektus kası ve kaburga kavsi; içinde a. epigastrica"],
  """Laparoskopik kolesistektomide 'kritik güvenlik görüntüsü' Calot üçgeninin temizlenip yalnızca iki yapının
  (ductus cysticus ve a. cystica) safra kesesine girdiğinin gösterilmesidir. Sağ hepatik arterin varyasyonları
  bu bölgede yaralanma riskini artırır.""",
  e=["vesica-biliaris", "ductus-choledochus"]),

Q("fv", KS, """Yağlı yemekten sonra sağ üst kadran ağrısı olan hastada, sağ kaburga kavsinin altına bastırılırken
derin nefes aldırıldığında hasta ağrıyla nefesini kesiyor. Safra kesesi fundusunun yüzeydeki izdüşümü
nerededir?""",
  "Sağ 9. kaburga kıkırdağının m. rectus abdominis'in dış kenarıyla kesiştiği yer",
  ["Göbeğin hemen sağı", "Sağ 12. kaburganın ucu", "Processus xiphoideus'un altı", "Sağ SIAS'ın iç tarafı"],
  """Murphy belirtisi akut kolesistitte inflame kesenin inspirasyonla inip muayene eden ele çarpmasıyla oluşur.
  Fundus sağ midklavikular hat (linea semilunaris) ile 9. kaburga kıkırdağının kesişimine izdüşer.""",
  e=["vesica-biliaris"]),

Q("t", KS, "Safra kesesi ağrısının sağ omza ve sağ skapula alt açısına yansımasının nedeni nedir?",
  "Diyafram altındaki peritonun tahrişi n. phrenicus (C3–C5), kesenin visseral afferentleri ise T6–T8 segmentlerine taşınır.",
  ["Safra kesesi n. accessorius ile innerve edilir.", "Safra kesesi doğrudan plexus brachialis'ten lif alır.",
   "Ağrı n. vagus ile omza taşınır.", "Safra kesesi omuz eklemiyle aynı arterden beslenir."],
  """Visseral ağrı başlangıçta epigastriumda hissedilir; sempatik afferentler T6–T8'e girdiği için sırtta skapula
  altına yansır. İnflamasyon diyafram peritonuna ulaşınca frenik sinir yoluyla omuz ucuna yansıyan ağrı ortaya çıkar.""",
  e=["vesica-biliaris", "n-phrenicus"]),

Q("tv", KS, """Safra taşı öyküsü olan hastada sırta yayılan şiddetli epigastrik ağrı ve serum lipazında belirgin
artış var. Ultrasonda koledok distalinde taş görülüyor. Taşın pankreatite yol açmasını en iyi açıklayan
anatomik yapı hangisidir?""",
  "Koledok ile ana pankreas kanalının ampulla hepatopancreatica'da (Vater) birleşerek ortak kanalla açılması",
  ["Yardımcı pankreas kanalının koledoğa açılması", "Koledoğun pankreas kuyruğundan geçmesi",
   "Pankreas kanalının doğrudan mideye açılması", "Ductus cysticus'un pankreasa açılması"],
  """Ampullada takılan taş hem safra hem pankreas salgısının akışını engeller; safranın pankreas kanalına geri
  akışı ve kanal içi basınç artışı enzimlerin bez içinde aktifleşmesine yol açar. Safra taşı akut pankreatitin
  en sık nedenidir.""",
  e=["ductus-choledochus", "ductus-pancreatici", "pancreas"]),

Q("tv", KS, """65 yaşında hastada kilo kaybı, ağrısız sarılık ve sağ üst kadranda ele gelen, ağrısız, gergin safra
kesesi var. En olası tanı ve tümörün yeri hangisidir?""",
  "Pankreas başı kanseri; koledoğun pankreas başı içindeki kısmına bası",
  ["Pankreas kuyruğu kanseri; dalak venine bası", "Akut kolesistit; ductus cysticus'ta taş",
   "Kolanjiokarsinom; sağ hepatik kanal düzeyinde", "Mide kanseri; pilor tıkanıklığı"],
  """Courvoisier yasası: ağrısız sarılıkla birlikte ele gelen safra kesesi taştan çok malign tıkanmayı düşündürür.
  Koledoğun distali pankreas başının arkasındaki oluk içinde veya bezin içinde seyrettiği için baş tümörleri
  erken sarılık yapar.""",
  e=["pancreas", "ductus-choledochus", "vesica-biliaris"]),

Q("t", KS, "Splenektomi sırasında pankreasın hangi bölümü yaralanabilir ve neden?",
  "Kuyruk; lig. splenorenale içinde dalak hilusuna kadar uzandığı için",
  ["Baş; duodenum kavsi içinde olduğu için", "Processus uncinatus; SMA'nın önünde olduğu için",
   "Boyun; v. portae'nin önünde olduğu için", "Gövde; mide ile kaynaşmış olduğu için"],
  """Pankreas kuyruğu splenik damarlarla birlikte lig. splenorenale içinde dalak hilusuna ulaşır ve pankreasın
  intraperitoneal tek bölümüdür. Hilusun bağlanması sırasında yaralanması pankreatik fistüle yol açabilir.""",
  e=["pancreas", "splen"]),

Q("t", KS, "Yenidoğanda safralı kusma ve duodenal tıkanıklık yapabilen halka (anüler) pankreas nasıl oluşur?",
  "Ventral pankreas tomurcuğunun iki lobunun duodenumun çevresini sarması",
  ["Dorsal tomurcuğun hiç gelişmemesi", "Pankreas kanallarının birleşmemesi", "Orta bağırsağın 270° dönmemesi", "Ductus vitellinus'un kapanmaması"],
  """Ventral tomurcuk normalde duodenumun arkasından dönerek dorsal tomurcukla birleşir. Anormal göçte duodenumu
  saran bir pankreas halkası oluşur ve tıkanmaya yol açabilir; Down sendromunda daha sıktır.""",
  e=["pancreas", "duodenum", "ductus-pancreatici"]),

Q("t", KS, "Pankreas divisum ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Dorsal ve ventral kanalların birleşmemesi sonucu salgının büyük kısmı papilla minor'dan boşalır.",
  ["Ventral tomurcuğun duodenumu sarmasıdır.", "Pankreasın iki ayrı organ hâlinde gelişmesidir ve tamamen belirtisizdir.",
   "Ana kanalın mideye açılmasıdır.", "Koledok ile pankreas kanalının hiç birleşmemesi anlamına gelir."],
  """En sık pankreas varyasyonudur. Dorsal kanal (Santorini) pankreasın büyük kısmını drene ettiği hâlde küçük
  papilladan açılır; göreceli darlık tekrarlayan pankreatite zemin hazırlayabilir.""",
  e=["ductus-pancreatici", "pancreas"]),

# ------------------------------------------------------------------ Periton
Q("t", PR, "Foramen omentale'nin (Winslow deliği) sınırları için aşağıdakilerden hangisi doğrudur?",
  "Önde lig. hepatoduodenale, arkada v. cava inferior, üstte kaudat lob, altta duodenumun 1. bölümü",
  ["Önde mide, arkada pankreas, üstte dalak, altta transvers kolon", "Önde aorta, arkada omurga, üstte diyafram, altta böbrek",
   "Önde lig. falciforme, arkada v. portae, üstte kuadrat lob, altta pilor", "Önde transvers kolon, arkada duodenum, üstte mide, altta jejunum"],
  """Winslow deliği büyük periton kesesini bursa omentalis'e bağlar. Ön sınırındaki lig. hepatoduodenale portal
  üçlüyü içerir; parmakla bu bağ sıkıştırılarak (Pringle) karaciğere gelen akım durdurulur.""",
  e=["bursa-omentalis", "omentum-minus", "v-cava-inferior"]),

Q("fv", PR, """Trafik kazası sonrası hipotansif hastada yatak başı ultrason (FAST) yapılıyor. Sırtüstü yatan hastada
karın içi serbest sıvının ilk biriktiği ve ilk bakılan yer neresidir?""",
  "Recessus hepatorenalis (Morison cebi)",
  ["Excavatio rectouterina (Douglas)", "Bursa omentalis", "Sol parakolik oluk", "Recessus subphrenicus sinister"],
  """Sırtüstü pozisyonda periton boşluğunun en alçak yeri karaciğer ile sağ böbrek arasındaki hepatorenal cebe
  karşılık gelir. Ayakta duran kişide ise en alçak yer pelvistir (kadında Douglas boşluğu).""",
  e=["peritoneum", "hepar", "ren"]),

Q("f", PR, "Aşağıdaki organlardan hangisi intraperitonealdir?",
  "Colon transversum",
  ["Colon ascendens", "Pankreas başı", "Böbrek", "Duodenumun 3. bölümü"],
  """Mezenteri olan organlar (mide, jejunum, ileum, transvers ve sigmoid kolon, apendiks, dalak, karaciğer, safra
  kesesi) intraperitonealdir. Çıkan ve inen kolon, duodenumun büyük kısmı ve pankreas (kuyruk hariç) sekonder
  retroperitoneal; böbrekler primer retroperitonealdir.""",
  e=["peritoneum", "colon-transversum"]),

Q("t", PR, "Omentum majus embriyolojik olarak hangi yapıdan gelişir?",
  "Dorsal mezogastrium",
  ["Ventral mezogastrium", "Septum transversum", "Dorsal mezenter (mezokolon)", "Allantois"],
  """Omentum majus ve lig. gastrosplenicum ile lig. splenorenale dorsal mezogastriumdan gelişir; dalak da bu
  mezenter içinde oluşur. Omentum minus ve lig. falciforme ventral mezogastriumdan gelişir.""",
  e=["omentum-majus", "omentum-minus"]),

Q("t", PR, "İnce bağırsak mezenterinin kökü aşağıdakilerden hangisini çaprazlamaz?",
  "Sol üreter",
  ["Duodenumun 3. bölümü", "Aorta", "V. cava inferior", "Sağ üreter"],
  """Mezenter kökü flexura duodenojejunalis'ten (L2, solda) sağ sakroiliak ekleme uzanırken duodenumun yatay
  bölümünü, aortu, VCI'yı, sağ üreteri, sağ psoas kasını ve sağ gonadal damarları çaprazlar. Sol üreter mezenter
  kökünün sol-alt tarafında kalır.""",
  e=["mesenterium", "ureter"]),

Q("f", PR, "Periton ağrısı ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Parietal periton somatik innervasyon aldığı için ağrı iyi lokalize edilir.",
  ["Visseral periton keskin ve iyi lokalize ağrıya yol açar.", "Parietal periton yalnızca n. vagus ile innerve edilir.",
   "Periton ağrıya tamamen duyarsızdır.", "Visseral periton n. pudendus ile innerve edilir."],
  """Parietal periton karın duvarını innerve eden spinal sinirlerden lif alır; tahrişi lokalize ağrı, defans ve
  rebound hassasiyeti yapar. Visseral periton yalnızca gerilme ve iskemiye duyarlıdır; ağrısı yaygın, orta hatta
  ve belirsizdir.""",
  e=["peritoneum"]),
]

write("digestive", questions)
