from common import T, ORD_EN, ORD_TR, ROMAN, FINGER_TR, TOE_TR

# --- Phalanges, metacarpals, metatarsals --------------------------------------
for k in range(5):
    for row, (en_row, tr_row, la_row) in enumerate([("Proximal", "proksimal", "proximalis"), ("Middle", "orta", "media"), ("Distal", "distal", "distalis")]):
        if k == 0 and en_row == "Middle":
            continue  # the thumb and big toe have no middle phalanx
        T(f"{en_row} phalanx of {ORD_EN[k]} finger of hand", f"El {k + 1}. parmak {tr_row} falanksı ({FINGER_TR[k]})",
          f"Phalanx {la_row} digiti {ROMAN[k]} manus",
          f"Elin {FINGER_TR[k]} kemiklerinden {tr_row} olanı; " +
          ("tabanı metakarp başıyla, başı orta ya da distal falanksla eklem yapar." if en_row == "Proximal" else
           "proksimal ve distal falankslar arasında yer alır." if en_row == "Middle" else
           "ucunda tırnak yatağını taşıyan tuberositas phalangis distalis bulunur."))
        T(f"{en_row} phalanx of {ORD_EN[k]} finger of foot", f"Ayak {k + 1}. parmak {tr_row} falanksı ({TOE_TR[k]})",
          f"Phalanx {la_row} digiti {ROMAN[k]} pedis",
          f"Ayağın {TOE_TR[k]} kemiklerinden {tr_row} olanı; ayak falanksları elinkilerden daha kısadır.")
    T(f"{ORD_EN[k].capitalize()} metacarpal bone", f"{k + 1}. metakarp kemiği", f"Os metacarpi {ROMAN[k]}",
      ("Başparmağın tarak kemiği; en kısa ve en kalın metakarptır, os trapezium ile eyer tipi eklem yapar." if k == 0 else
       f"El tarağını oluşturan beş uzun kemikten {k + 1}.si; tabanı el bilek kemikleriyle, başı proksimal falanksla eklem yapar."))
    T(f"{ORD_EN[k].capitalize()} metatarsal bone", f"{k + 1}. metatars kemiği", f"Os metatarsi {ROMAN[k]}",
      ("Başparmağın kalın, kısa tarak kemiği; altındaki iki sesamoid kemikle yürürken ağırlığın büyük kısmını taşır." if k == 0 else
       "Lateral kenardaki metatars; tabanındaki tuberositas ossis metatarsi quinti'ye m. fibularis brevis tutunur, sık kırılır." if k == 4 else
       f"Ayak tarağını oluşturan beş uzun kemikten {k + 1}.si; tabanı tarsal kemiklerle, başı proksimal falanksla eklem yapar."))

# --- Ribs and costal cartilages -----------------------------------------------
RIB_LA = ["Costa prima (I)", "Costa secunda (II)", "Costa tertia (III)", "Costa quarta (IV)", "Costa quinta (V)", "Costa sexta (VI)",
          "Costa septima (VII)", "Costa octava (VIII)", "Costa nona (IX)", "Costa decima (X)", "Costa undecima (XI)", "Costa duodecima (XII)"]
for k in range(12):
    kind = "gerçek (vertebrosternal) kaburga; kıkırdağıyla doğrudan sternuma bağlanır" if k < 7 else \
        "yalancı (vertebrokondral) kaburga; kıkırdağı üstteki kaburga kıkırdağına katılır" if k < 10 else \
        "yüzen kaburga; ön ucu serbesttir, karın duvarı kasları arasında sonlanır"
    extra = {0: " En kısa, en geniş ve en eğik kaburgadır; üst yüzünde a. ve v. subclavia olukları ile m. scalenus anterior'un tutunduğu tuberculum bulunur.",
             1: " Üst yüzündeki tuberositas m. serrati anterioris'e m. serratus anterior tutunur."}.get(k, "")
    T(f"{ORD_EN[k].capitalize()} rib", f"{k + 1}. kaburga (kosta)", RIB_LA[k], f"{k + 1}. kaburga: {kind}.{extra}")
    if k < 10:
        T(f"Costal cartilage of {ORD_EN[k]} rib", f"{k + 1}. kaburga kıkırdağı", f"Cartilago costalis costae {ROMAN[k]}",
          "Kaburganın ön ucunu sternuma ya da üstteki kıkırdağa bağlayan hiyalin kıkırdak; göğüs kafesine esneklik kazandırır." if k < 7 else
          "Yalancı kaburga kıkırdağı; üstteki kıkırdağa katılarak arcus costalis'i (kaburga kemerini) oluşturur.")

# --- Vertebrae -------------------------------------------------------------------
for n in range(3, 8):
    extra = " Dikenli çıkıntısı (vertebra prominens) ense kökünde elle hissedilen ilk belirgin çıkıntıdır; foramen transversarium'undan genellikle a. vertebralis geçmez." if n == 7 else \
        " Ön tüberkülü (tuberculum caroticum) a. carotis communis'in bastırılabildiği noktadır." if n == 6 else ""
    T(f"Vertebra C{n}", f"C{n} omuru (boyun omuru)", f"Vertebra cervicalis {ROMAN[n - 1]}",
      f"Tipik boyun omuru: küçük gövdeli, üçgen omur delikli, transvers çıkıntılarında foramen transversarium bulunur, dikenli çıkıntısı çatallıdır.{extra}")
for n in range(1, 13):
    extra = {1: " Gövdesinde 1. kaburga için tam, 2. kaburga için yarım eklem yüzü bulunur.",
             10: " Genellikle yalnız 10. kaburga için tek eklem yüzü taşır.",
             11: " Tek kaburga eklem yüzü vardır; transvers çıkıntısında eklem yüzü yoktur.",
             12: " Gövdesi bel omurlarına benzer; torakolomber geçişte kırıkların en sık görüldüğü omurlardandır."}.get(n, "")
    T(f"Vertebra T{n}", f"T{n} omuru (göğüs omuru)", f"Vertebra thoracica {ROMAN[n - 1]}",
      f"Göğüs omuru: gövdesinde ve transvers çıkıntısında kaburgalarla eklem yapan yüzler bulunur, dikenli çıkıntısı uzun ve aşağı eğiktir.{extra}")
for n in range(1, 6):
    extra = {5: " En büyük omurdur; gövdesi önde daha yüksektir (kama şekilli), sacrum ile lumbosakral açıyı yapar. Spondilolistezis en sık L5–S1'de görülür.",
             4: " Krista iliaka'ların en üst noktalarını birleştiren çizgi (Tuffier) genellikle L4 dikenini keser; lomber ponksiyonun referansıdır.",
             1: " Omurilik konus medullaris ile çoğunlukla L1–L2 hizasında sonlanır."}.get(n, "")
    T(f"Vertebra L{n}", f"L{n} omuru (bel omuru)", f"Vertebra lumbalis {ROMAN[n - 1]}",
      f"Bel omuru: büyük böbrek biçimli gövde, kalın pediküller, kısa ve dörtgen dikenli çıkıntı; çıkıntıları processus mammillaris ve accessorius taşır.{extra}")

T("Atlas (C1)", "Atlas (C1 omuru)", "Atlas (vertebra cervicalis I)",
  "Kafatasını taşıyan halka şeklinde ilk boyun omuru; gövdesi ve dikenli çıkıntısı yoktur. Üst eklem yüzleri oksipital kondillerle 'evet' hareketini yapan art. atlantooccipitalis'i oluşturur.")
T("Axis (C2)", "Aksis (C2 omuru)", "Axis (vertebra cervicalis II)",
  "Gövdesinden yukarı uzanan dens (processus odontoideus) etrafında atlas döner; 'hayır' hareketinin yarısı art. atlantoaxialis'te gerçekleşir. Dens kırıkları ve hangman kırığı tipiktir.")
T("Sacrum", "Sakrum (kuyruk sokumu kemiği)", "Os sacrum",
  "Beş sakral omurun kaynaşmasıyla oluşan üçgen kemik; iki kalça kemiği arasında pelvisin arka duvarını yapar. Ön ve arka sakral deliklerden sakral sinirlerin dalları çıkar.")
T("Coccyx", "Koksiks (kuyruk kemiği)", "Os coccygis",
  "Genellikle dört rudimenter omurun kaynaşmasıyla oluşan küçük kemik; pelvik taban kaslarına ve lig. anococcygeum'a tutunma yeri verir.")

# --- Upper limb ------------------------------------------------------------------
T("Clavicle", "Köprücük kemiği", "Clavicula",
  "S şeklindeki, yatay uzanan tek uzun kemik; sternum ile skapula arasında payanda görevi görür. En sık kırılan kemiklerdendir, kırık genellikle orta ve dış üçte bir birleşiminde olur.")
T("Scapula", "Kürek kemiği", "Scapula",
  "Göğüs kafesinin arka-üst yüzündeki üçgen yassı kemik; spina, akromiyon, korakoid çıkıntı ve glenoid boşluk taşır. 17 kasa tutunma yeri verir.")
T("Humerus", "Kol kemiği", "Humerus",
  "Kolun tek uzun kemiği; başı skapulanın cavitas glenoidalis'iyle omuz eklemini yapar. Collum chirurgicum (n. axillaris), sulcus nervi radialis (n. radialis) ve epicondylus medialis (n. ulnaris) kırıklarda sinir hasarı açısından önemlidir.")
T("Radius", "Döner kemik (radius)", "Radius",
  "Önkolun başparmak (lateral) tarafındaki kemiği; ulna etrafında dönerek pronasyon ve supinasyonu sağlar. Distal ucunun kırığı (Colles) en sık görülen el bileği kırığıdır.")
T("Ulna", "Dirsek kemiği (ulna)", "Ulna",
  "Önkolun serçe parmak (medial) tarafındaki kemiği; olekranon ve processus coronoideus ile humerus trokleasını kavrayarak dirsek eklemini yapar.")
T("Scaphoid bone", "Skafoid kemik (kayık kemiği)", "Os scaphoideum",
  "Proksimal sıranın en lateral ve en büyük el bilek kemiği; anatomik enfiyedan çukurunda ele gelir. Kanlanması distalden geldiği için bel kırıklarında proksimal parçada avasküler nekroz gelişebilir.")
T("Lunate bone", "Lunat kemik (ay kemiği)", "Os lunatum",
  "Proksimal sıranın ortasındaki yarım ay biçimli kemik; en sık çıkığa uğrayan el bilek kemiğidir ve öne çıkığı karpal tünelde n. medianus'u sıkıştırabilir. Avasküler nekrozu Kienböck hastalığıdır.")
T("Triquetrum bone", "Triketrum kemiği (üçköşeli kemik)", "Os triquetrum",
  "Proksimal sıranın piramit biçimli medial kemiği; palmar yüzünde pisiform ile eklem yapar.")
T("Pisiform bone", "Pisiform kemik (bezelye kemiği)", "Os pisiforme",
  "M. flexor carpi ulnaris tendonu içinde gelişmiş sesamoid el bilek kemiği; Guyon kanalının medial duvarını oluşturur.")
T("Trapezium bone", "Trapez kemiği (büyük çokgen kemik)", "Os trapezium",
  "Distal sıranın lateral kemiği; 1. metakarpla başparmağın karşılaştırma (opozisyon) hareketini sağlayan eyer eklemi yapar.")
T("Trapezoid bone", "Trapezoid kemik (küçük çokgen kemik)", "Os trapezoideum",
  "Distal sıranın en küçük kemiği; 2. metakarpın tabanıyla eklem yapar.")
T("Capitate bone", "Kapitat kemik (başlı kemik)", "Os capitatum",
  "En büyük el bilek kemiği; distal sıranın ortasında yer alır ve 3. metakarpla eklem yapar. Elin hareket ekseni bu kemikten geçer.")
T("Hamate bone", "Hamat kemik (çengelli kemik)", "Os hamatum",
  "Distal sıranın medial kemiği; palmar yüzündeki çengel (hamulus ossis hamati) Guyon kanalının lateral duvarını ve karpal tünelin medial sınırını oluşturur.")

# --- Lower limb ------------------------------------------------------------------
T("Hip bone", "Kalça kemiği", "Os coxae",
  "Ilium, ischium ve pubisin asetabulumda kaynaşmasıyla oluşan büyük düzensiz kemik; sacrum ile pelvis halkasını yapar ve femur başıyla kalça eklemini oluşturur.")
T("Femur", "Uyluk kemiği", "Os femoris",
  "Vücudun en uzun ve en güçlü kemiği; başı asetabulumla kalça, kondilleri tibia ile diz eklemini yapar. Collum femoris kırıklarında a. circumflexa femoris medialis yaralanırsa baş nekrozu gelişebilir.")
T("Patella", "Diz kapağı kemiği", "Patella",
  "Vücudun en büyük sesamoid kemiği; m. quadriceps femoris tendonu içinde gelişir ve kasın kaldıraç kolunu uzatarak diz ekstansiyonunu güçlendirir.")
T("Tibia", "Kaval kemiği", "Tibia",
  "Bacağın medial, ağırlık taşıyan kemiği; ön kenarı ve medial yüzü deri altında ele gelir. Distal ucu malleolus medialis'i yapar; açık kırıkların en sık görüldüğü uzun kemiktir.")
T("Fibula", "Kamış kemiği (fibula)", "Fibula",
  "Bacağın lateral ince kemiği; ağırlık taşımaz ama kaslara tutunma yeri verir ve malleolus lateralis ile ayak bileği eklemini sabitler. Boynu etrafında n. fibularis communis dolanır.")
T("Talus", "Talus (aşık kemiği)", "Talus",
  "Bacak ile ayak arasında ağırlığı aktaran, hiçbir kasın tutunmadığı tarsal kemik; trochlea tali ile ayak bileği eklemini yapar. Boyun kırıklarında avasküler nekroz riski vardır.")
T("Calcaneus", "Topuk kemiği (kalkaneus)", "Calcaneus",
  "En büyük tarsal kemik; topuğu oluşturur, tuber calcanei'ye Aşil tendonu tutunur. Sustentaculum tali altında m. flexor hallucis longus tendonu geçer.")
T("Navicular bone", "Naviküler kemik (ayak kayık kemiği)", "Os naviculare",
  "Talus başı ile çivi kemikleri arasındaki kayık biçimli tarsal kemik; medial tüberkülüne m. tibialis posterior tutunur ve ayağın medial longitudinal kemerinin kilit taşıdır.")
T("Cuboid bone", "Küboid kemik (küp kemiği)", "Os cuboideum",
  "Lateral kolonun tarsal kemiği; alt yüzündeki olukta m. fibularis longus tendonu seyreder.")
T("Medial cuneiform bone", "Medial kuneiform kemik (iç çivi kemiği)", "Os cuneiforme mediale",
  "Üç çivi kemiğinin en büyüğü; 1. metatarsla eklem yapar, m. tibialis anterior ve m. fibularis longus'a tutunma yeri verir.")
T("Intermediate cuneiform bone", "İntermedier kuneiform kemik (orta çivi kemiği)", "Os cuneiforme intermedium",
  "En küçük çivi kemiği; 2. metatarsın tabanı bu kemiğe kenetlenir ve Lisfranc ekleminin stabilitesini sağlar.")
T("Lateral cuneiform bone", "Lateral kuneiform kemik (dış çivi kemiği)", "Os cuneiforme laterale",
  "Orta büyüklükteki çivi kemiği; küboid ile 3. metatars arasında yer alır.")
T("Sesamoid bones of foot", "Ayağın sesamoid kemikleri", "Ossa sesamoidea pedis",
  "Başparmak metatars başı altında m. flexor hallucis brevis tendonları içinde bulunan iki küçük kemik; ağırlık aktarımına katılır, sesamoidit ve kırıklara uğrayabilir.")

# --- Skull -----------------------------------------------------------------------
T("Frontal bone", "Alın kemiği (frontal kemik)", "Os frontale",
  "Alnı, orbita tavanını ve ön kafa çukurunun büyük kısmını oluşturan kemik; içinde sinus frontalis bulunur. Koronal sütürle paryetal kemiklere bağlanır.")
T("Parietal bone", "Yan kafa kemiği (paryetal kemik)", "Os parietale",
  "Kafatası tavanı ve yan duvarlarını yapan çift kemik; iç yüzündeki oluklarda a. meningea media'nın dalları seyreder.")
T("Occipital bone", "Art kafa kemiği (oksipital kemik)", "Os occipitale",
  "Kafatasının arka ve tabanını oluşturan kemik; foramen magnum'dan omurilik ve aa. vertebrales geçer, kondilleri atlasla eklem yapar.")
T("Temporal bone", "Şakak kemiği (temporal kemik)", "Os temporale",
  "Orta ve iç kulağı barındıran, pars petrosa, squamosa, tympanica ve processus mastoideus'tan oluşan karmaşık kemik; mandibula ile çene eklemini yapar.")
T("Sphenoid bone", "Kama kemiği (sfenoid kemik)", "Os sphenoideum",
  "Kafa tabanının ortasındaki kelebek biçimli kemik; sella turcica'da hipofiz bulunur. Büyük ve küçük kanatlarındaki deliklerden (optik kanal, fissura orbitalis superior, f. rotundum, ovale, spinosum) sinir ve damarlar geçer.")
T("Ethmoid bone", "Kalbur kemiği (etmoid kemik)", "Os ethmoideum",
  "Burun boşluğu tavanını ve orbitaların medial duvarını oluşturan hafif kemik; lamina cribrosa'nın deliklerinden koku sinirleri geçer, labirentinde etmoid hücreler bulunur.")
T("Anterior cells of ethmoid bone", "Ön etmoid hücreler", "Cellulae ethmoidales anteriores",
  "Etmoid labirentin ön hava hücreleri; meatus nasi medius'a açılır.")
T("Middle cells of ethmoid bone", "Orta etmoid hücreler", "Cellulae ethmoidales mediae",
  "Bulla ethmoidalis'i oluşturan hava hücreleri; meatus nasi medius'a açılır.")
T("Posterior cells of ethmoid bone", "Arka etmoid hücreler", "Cellulae ethmoidales posteriores",
  "Etmoid labirentin arka hava hücreleri; meatus nasi superior'a açılır ve n. opticus'a komşudur.")
T("Sinus of frontal bone", "Frontal sinüs", "Sinus frontalis",
  "Alın kemiği içindeki çift hava boşluğu; ductus frontonasalis aracılığıyla meatus nasi medius'a açılır.")
T("Sinus of sphenoid bone", "Sfenoid sinüs", "Sinus sphenoidalis",
  "Sfenoid gövdesindeki hava boşluğu; recessus sphenoethmoidalis'e açılır, hipofiz cerrahisinde transsfenoidal yol olarak kullanılır.")
T("Maxilla", "Üst çene kemiği (maksilla)", "Maxilla",
  "Üst çeneyi, sert damağın önünü, orbita tabanını ve burun boşluğunun yan duvarını yapan çift kemik; en büyük paranazal sinüs olan sinus maxillaris'i içerir.")
T("Palatine bone", "Damak kemiği", "Os palatinum",
  "Sert damağın arka kısmını ve burun boşluğu yan duvarının arkasını yapan L biçimli çift kemik; foramen palatinum majus'tan aynı adlı damar ve sinir geçer.")
T("Zygomatic bone", "Elmacık kemiği", "Os zygomaticum",
  "Yanak çıkıntısını ve orbitanın lateral duvarını oluşturan kemik; temporal kemikle arcus zygomaticus'u yapar.")
T("Nasal bone", "Burun kemiği", "Os nasale",
  "Burun sırtını oluşturan küçük dikdörtgen çift kemik; yüz kırıkları içinde en sık kırılanıdır.")
T("Lacrimal bone", "Gözyaşı kemiği", "Os lacrimale",
  "Orbitanın medial duvarındaki en küçük yüz kemiği; fossa sacci lacrimalis'te gözyaşı kesesi bulunur.")
T("Vomer", "Vomer (sapan kemiği)", "Vomer",
  "Burun septumunun arka-alt kısmını oluşturan ince tek kemik.")
T("Inferior nasal concha bone", "Alt burun konkası", "Concha nasalis inferior",
  "Burun boşluğunun yan duvarına tutunan bağımsız ince kemik; altındaki meatus nasi inferior'a ductus nasolacrimalis açılır.")
T("Mandible", "Alt çene kemiği (mandibula)", "Mandibula",
  "Yüzün tek hareketli kemiği; kondilleri temporal kemikle çene eklemini (art. temporomandibularis) yapar. Canalis mandibulae'de n. alveolaris inferior seyreder.")
T("Hyoid bone", "Dil kemiği (hiyoid)", "Os hyoideum",
  "Boyunda C3 hizasında, hiçbir kemikle eklem yapmayan U biçimli kemik; dil ve gırtlak kaslarına tutunma yeri verir. Kırığı boğulma (strangülasyon) açısından adli önem taşır.")
for en, tr, la, d in [("Incus", "Örs kemiği (inkus)", "Incus", "Orta kulaktaki üç kemikçiğin ortancası; malleus ile stapes arasında titreşimi iletir."),
                      ("Malleus", "Çekiç kemiği (malleus)", "Malleus", "Kulak zarına yapışık en dıştaki kemikçik; sapı (manubrium) zarın iç yüzüne gömülüdür, m. tensor tympani buraya tutunur."),
                      ("Stapes", "Üzengi kemiği (stapes)", "Stapes", "Vücudun en küçük kemiği; tabanı fenestra vestibuli'yi kapatarak titreşimi iç kulağa aktarır. M. stapedius tutunur; otosklerozda tabanı fikse olur.")]:
    T(en, tr, la, d)

# --- Cartilages of larynx and nose ----------------------------------------------------
T("Thyroid cartilage", "Tiroid kıkırdağı", "Cartilago thyroidea",
  "Gırtlağın en büyük kıkırdağı; iki laminanın önde birleşmesiyle prominentia laryngea'yı (Âdem elması) oluşturur.")
T("Cricoid cartilage", "Krikoid kıkırdak (yüzük kıkırdak)", "Cartilago cricoidea",
  "Hava yolunu tamamen saran tek kıkırdak halka (C6 hizası); önde dar, arkada geniştir. Trakeanın başlangıcıdır.")
T("Arytenoid cartilage", "Aritenoid kıkırdak", "Cartilago arytenoidea",
  "Krikoid laminası üzerindeki piramit biçimli çift kıkırdak; processus vocalis'ine ses teli bağı tutunur, dönme ve kaymasıyla glottisi açıp kapatır.")
T("Corniculate cartilage", "Kornikülat kıkırdak", "Cartilago corniculata",
  "Aritenoid kıkırdakların tepesinde oturan küçük elastik kıkırdaklar; plica aryepiglottica'yı destekler.")
T("Nasal septal cartilage", "Burun septum kıkırdağı", "Cartilago septi nasi",
  "Burun bölmesinin ön kısmını oluşturan dörtgen hiyalin kıkırdak; deviasyonu burun tıkanıklığına yol açar.")
T("Lateral process of nasal septal cartilage", "Septum kıkırdağının lateral çıkıntısı", "Processus lateralis cartilaginis septi nasi",
  "Burun sırtının orta kısmını destekleyen, septum kıkırdağından yanlara uzanan kıkırdak plaka (üst lateral kıkırdak).")
T("Major alar cartilage", "Büyük kanat kıkırdağı", "Cartilago alaris major",
  "Burun ucunu ve burun deliklerinin kenarını şekillendiren U biçimli kıkırdak; crus mediale ve laterale'den oluşur.")

# --- Sternum -------------------------------------------------------------------------
T("Manubrium of sternum", "Sternum sapı (manubrium)", "Manubrium sterni",
  "Sternumun üst parçası; klavikulalar ve 1. kaburga kıkırdaklarıyla eklem yapar, üst kenarında incisura jugularis bulunur.")
T("Body of sternum", "Sternum gövdesi", "Corpus sterni",
  "Sternumun en uzun parçası; 2.–7. kaburga kıkırdaklarıyla eklem yapar. Manubriumla birleşme yeri (angulus sterni) 2. kaburganın ve T4–T5 hizasının işaretidir.")
T("Xiphoid process", "Ksifoid çıkıntı", "Processus xiphoideus",
  "Sternumun en alttaki kıkırdaksı-kemiksi ucu; diyafram ve rectus kılıfına tutunma yeri verir, KPR sırasında bası alanının altında kalır.")

# --- Teeth -----------------------------------------------------------------------------
for jaw_en, jaw_tr, jaw_la in [("Upper", "Üst", "superior"), ("Lower", "Alt", "inferior")]:
    T(f"{jaw_en} medial incisor", f"{jaw_tr} orta kesici diş", f"Dens incisivus medialis {jaw_la}",
      "Ön dişlerin ortadaki keskin kenarlı, tek köklü dişi; besinleri ısırarak keser. Daimi dentisyonda 6–8 yaşlarında çıkar.")
    T(f"{jaw_en} lateral incisor", f"{jaw_tr} yan kesici diş", f"Dens incisivus lateralis {jaw_la}",
      "Orta kesicinin yanındaki tek köklü kesici diş.")
    T(f"{jaw_en} canine", f"{jaw_tr} köpek dişi", f"Dens caninus {jaw_la}",
      "Ağzın köşesindeki en uzun köklü diş; besinleri yırtar." + (" Üst köpek dişinin kökü göz köşesine kadar uzanabilir." if jaw_en == "Upper" else ""))
    T(f"{jaw_en} first premolar", f"{jaw_tr} 1. küçük azı dişi", f"Dens premolaris primus {jaw_la}",
      "İki tüberküllü (çift sivri uçlu) küçük azı; besinleri ezmeye başlar." + (" Üstte genellikle iki köklüdür." if jaw_en == "Upper" else ""))
    T(f"{jaw_en} second premolar", f"{jaw_tr} 2. küçük azı dişi", f"Dens premolaris secundus {jaw_la}",
      "İkinci küçük azı; genellikle tek köklüdür ve süt dişlerinde karşılığı yoktur (süt azılarının yerine çıkar).")
    T(f"{jaw_en} first molar tooth", f"{jaw_tr} 1. büyük azı dişi", f"Dens molaris primus {jaw_la}",
      "İlk çıkan daimi diş (6 yaş); geniş çiğneme yüzeyi ve " + ("üç kökü" if jaw_en == "Upper" else "iki kökü") + " vardır.")
    T(f"{jaw_en} second molar tooth", f"{jaw_tr} 2. büyük azı dişi", f"Dens molaris secundus {jaw_la}",
      "12 yaş civarında çıkan ikinci büyük azı; öğütme işlevi görür.")
