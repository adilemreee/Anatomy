from qcommon import Q, write

DK = "Deri katmanları"
DE = "Deri ekleri"
VB = "Vücut bölgeleri"

questions = [
Q("f", DK, "Epidermisin derinden yüzeye doğru katmanlarının doğru sıralaması hangisidir?",
  "Stratum basale, spinosum, granulosum, lucidum, corneum",
  ["Stratum corneum, lucidum, granulosum, spinosum, basale", "Stratum basale, granulosum, spinosum, corneum, lucidum",
   "Stratum spinosum, basale, granulosum, lucidum, corneum", "Stratum basale, lucidum, spinosum, granulosum, corneum"],
  """Keratinositler bazal tabakada bölünür ve yüzeye doğru olgunlaşarak keratinize olur. Stratum lucidum yalnızca avuç
  içi ve ayak tabanı gibi kalın deride belirgindir. Epidermiste kan damarı yoktur; beslenme dermisten difüzyonla olur.""",
  e=["epidermis"]),

Q("t", DK, "Deri rengini belirleyen melanositler ile ilgili hangisi doğrudur?",
  "Nöral krista kökenlidir ve stratum basale'de bulunur.",
  ["Endoderm kökenlidir ve stratum corneum'da bulunur.", "Kemik iliği kökenlidir ve dermiste bulunur.",
   "Irklar arasında melanosit sayısı çok farklıdır.", "Stratum spinosum'da antijen sunar."],
  """Melanosit sayısı insanlar arasında benzerdir; deri rengi farkı melanozomların sayısı, büyüklüğü ve dağılımından
  kaynaklanır. Albinizmde melanosit sayısı normaldir ancak tirozinaz eksikliği nedeniyle melanin yapılamaz.""",
  e=["epidermis", "cutis"]),

Q("t", DK, "Epidermiste antijen sunan Langerhans hücreleri hangi katmanda yoğundur ve kökeni nedir?",
  "Stratum spinosum; kemik iliği (monosit–dendritik hücre serisi)",
  ["Stratum basale; nöral krista", "Stratum corneum; ektoderm", "Dermis; mezoderm", "Stratum granulosum; endoderm"],
  """Langerhans hücreleri deriye giren antijenleri yakalayıp bölgesel lenf düğümlerine taşır; kontakt dermatitte rol
  oynar. Elektron mikroskopisinde tenis raketi biçimli Birbeck granülleri içerir.""",
  e=["epidermis"]),

Q("f", DK, "Hafif dokunma duyusundan sorumlu olup dermisin papiller tabakasında, özellikle parmak uçlarında bulunan reseptör hangisidir?",
  "Meissner cisimciği",
  ["Pacini cisimciği", "Ruffini cisimciği", "Serbest sinir uçları", "Kas iğciği"],
  """Meissner cisimcikleri kılsız derinin papiller dermisinde, ince ayrımlı dokunma için uzmanlaşmıştır. Pacini
  cisimcikleri derin dermis ve hipodermiste titreşim ve basınca, Ruffini cisimcikleri gerilmeye duyarlıdır.""",
  e=["dermis"]),

Q("fv", DK, """Mutfakta kızgın yağ ile yanan hastanın kolunda beyaz-deri görünümlü, kuru ve iğne batırıldığında
ağrısız bir alan var. Bu yanık hangi derinliktedir ve neden ağrısızdır?""",
  "Tam kat (üçüncü derece) yanık; dermisteki sinir uçları da yanmıştır.",
  ["Birinci derece yanık; yalnızca epidermis etkilenmiştir.", "Yüzeyel ikinci derece yanık; sinir uçları uyarılmıştır.",
   "Birinci derece yanık; dermis korunmuştur.", "Yüzeyel ikinci derece yanık; bül oluşmuştur."],
  """Birinci derece yanık kızarık ve ağrılıdır; ikinci derece yanıklar bül oluşturur ve yüzeyel olanlar çok ağrılıdır.
  Tam kat yanıkta epidermis ve dermisin tamamı, deri ekleri ve sinir uçları yok olduğu için yara kuru, sert ve
  ağrısızdır; kendiliğinden iyileşemez, greft gerekir.""",
  e=["dermis", "cutis"]),

Q("fv", DK, """Erişkin yanık hastasında tüm sağ kol ile gövdenin ön yüzü yanmış. Dokuzlar kuralına göre yanık yüzey
alanı yaklaşık ne kadardır?""",
  "%27",
  ["%18", "%36", "%45", "%9"],
  """Dokuzlar kuralı: baş-boyun %9, her kol %9, gövde ön yüzü %18, gövde arka yüzü %18, her bacak %18, perine %1.
  Bir kol (%9) + gövde ön yüzü (%18) = %27. Çocuklarda baş oranı daha büyüktür.""",
  e=["cutis"]),

Q("f", DK, "Cerrahi kesilerin Langer (gerilim) çizgilerine paralel yapılmasının nedeni nedir?",
  "Dermisteki kolajen liflerin dizilimine uyduğu için daha ince ve az belirgin skarla iyileşmesi",
  ["Daha az kanaması", "Sinirleri kesmemesi", "Epidermisin bu yönde daha kalın olması", "Lenfatiklerin bu yönde seyretmemesi"],
  """Langer çizgileri dermisteki kolajen liflerin baskın yönünü gösterir. Bu çizgilere dik kesiler yara ağzının açılmasına
  ve geniş skara yol açar.""",
  e=["cutis", "dermis"]),

Q("f", DK, "Hipodermis (tela subcutanea) ile ilgili hangisi doğrudur?",
  "Gevşek bağ dokusu ve yağdan oluşur; deri altı enjeksiyonlar bu tabakaya yapılır.",
  ["Epidermisin en derin katmanıdır.", "Damar içermez.", "Ter bezleri burada üretilmez ve bulunmaz.", "Yalnızca avuç içinde bulunur."],
  """Hipodermis deriyi alttaki fasyaya bağlar; ısı yalıtımı ve enerji deposu sağlar. İnsülin ve düşük molekül ağırlıklı
  heparin gibi ilaçlar buraya uygulanır. Pacini cisimcikleri ve ter bezlerinin sekretuvar kısmının bir bölümü de
  bu tabakaya uzanabilir.""",
  e=["tela-subcutanea"]),

# ------------------------------------------------------------------ Deri ekleri
Q("t", DE, "Apokrin ter bezleri için aşağıdakilerden hangisi doğrudur?",
  "Aksilla ve anogenital bölgede bulunur, kanalları kıl foliküllerine açılır ve ergenlikte aktifleşir.",
  ["Tüm vücutta yaygındır ve ısı düzenlemesinde asıl rolü oynar.", "Holokrin salgı yapar.",
   "Doğumdan itibaren aktiftir.", "Avuç içi ve ayak tabanında en yoğundur."],
  """Apokrin bezlerin salgısı kokusuzdur; bakterilerin parçalamasıyla vücut kokusu oluşur. Isı düzenlemesinde asıl
  görev, tüm vücuda yayılmış ve doğrudan deri yüzeyine açılan ekrin bezlerindir. Hidradenitis süpürativa apokrin bez
  taşıyan bölgelerde görülür.""",
  e=["glandulae-cutis"]),

Q("f", DE, "Yağ (sebase) bezleri için aşağıdakilerden hangisi yanlıştır?",
  "Avuç içi ve ayak tabanında en yoğun olarak bulunurlar.",
  ["Holokrin salgı yaparlar.", "Çoğunlukla kıl foliküllerine açılırlar.", "Androjenlerle uyarılırlar.", "Akne vulgariste rol oynarlar."],
  """Yağ bezleri kılsız bölgelerde (avuç içi, ayak tabanı) bulunmaz; yüz, saçlı deri ve göğüs ön yüzünde yoğundur.
  Salgı hücrelerin tümüyle parçalanmasıyla oluşur (holokrin).""",
  e=["glandulae-cutis", "pili"]),

Q("t", DE, "Kıl folikülünde epidermis ve kıl rejenerasyonunda görev yapan kök hücrelerin bulunduğu bölge hangisidir?",
  "Çıkıntı (bulge) bölgesi – m. arrector pili'nin tutunduğu yer",
  ["Kıl soğanının papillası", "Stratum corneum", "İnfundibulum'un ağzı", "Yağ bezinin kanalı"],
  """Bulge bölgesi dış kök kılıfında, arrector pili kasının tutunduğu yerdedir. Yanık ve yara iyileşmesinde kıl
  folikülleri korunmuşsa epitel bu kök hücrelerden yenilenir; bu nedenle kısmi kalınlıktaki yanıklar kendiliğinden
  iyileşebilir.""",
  e=["pili"]),

Q("f", DE, "Tırnak plağını üreten ve hasarı kalıcı tırnak deformitesine yol açan yapı hangisidir?",
  "Tırnak matriksi",
  ["Tırnak yatağı", "Eponişyum", "Hiponişyum", "Lunula'nın yüzeyi"],
  """Tırnak plağı proksimal tırnak kıvrımının altındaki matriksten üretilir; lunula matriksin görünen distal kısmıdır.
  Tırnak yatağı plağın üzerinde kaydığı yüzeydir. Matriks yaralanmaları dikkatle onarılmalıdır.""",
  e=["unguis"]),

Q("fv", DE, "Tırnakları ince, yassı ve kaşık biçiminde içe çökük olan kadında en olası altta yatan durum hangisidir?",
  "Demir eksikliği anemisi",
  ["Kronik akciğer hastalığı", "Psoriazis", "Böbrek yetmezliği", "Hipertiroidi"],
  """Koilonişi (kaşık tırnak) demir eksikliğinin klasik bulgusudur. Çomak parmak kronik hipoksiyle (akciğer kanseri,
  bronşektazi, siyanotik kalp hastalığı), tırnakta çukurlaşma (pitting) psoriazisle ilişkilidir.""",
  e=["unguis"]),

# ------------------------------------------------------------------ Vücut bölgeleri
Q("tv", VB, """Gebe kadında gece uyandıran, başparmak, işaret ve orta parmakta uyuşma var; bileğin ön yüzüne
vurulunca parmaklara elektriklenme yayılıyor. Bu tanıda aşağıdaki bulgulardan hangisi beklenmez?""",
  "Hipotenar kaslarda atrofi",
  ["Tenar kaslarda atrofi", "Phalen testinin pozitif olması", "Başparmak oppozisyonunda güçsüzlük", "Avuç içi derisinde duyunun korunması"],
  """Karpal tünel sendromunda n. medianus sıkışır: lateral 3,5 parmakta parestezi, tenar atrofi ve oppozisyon
  zayıflığı görülür; avuç içi duyusu korunur. Hipotenar kaslar n. ulnaris ile innerve edildiği için etkilenmez.""",
  e=["canalis-carpi", "n-medianus", "mm-thenares"]),

Q("t", VB, "Guyon kanalını (canalis ulnaris) sınırlayan kemik yapılar ve içeriği hangisidir?",
  "Os pisiforme ve hamulus ossis hamati arasında; n. ve a. ulnaris",
  ["Os scaphoideum ve os trapezium arasında; n. medianus", "Radius stiloidi ve os scaphoideum arasında; a. radialis",
   "Os lunatum ve os capitatum arasında; fleksör tendonlar", "Ulna başı ve os triquetrum arasında; n. radialis'in yüzeyel dalı"],
  """Guyon kanalı karpal tünelin yüzeyelinde ve ulnar tarafındadır. Buradaki sıkışma (bisikletçi felci) n. ulnaris'in
  elde motor ve duyusal dallarını etkiler; FCU ve FDP'nin ulnar yarısı korunur.""",
  e=["canalis-carpi", "n-ulnaris", "os-hamatum", "os-pisiforme"]),

Q("t", VB, "Femoral kanal ile ilgili aşağıdakilerden hangisi doğrudur?",
  "Femoral kılıfın en medial bölmesidir; lenfatikleri ve Cloquet lenf düğümünü içerir, femoral herniler buradan çıkar.",
  ["A. femoralis'i içerir.", "N. femoralis femoral kanalın içinden geçer.", "Lig. inguinale'nin üstünde yer alır.",
   "Femoral herniler erkeklerde kadınlardan daha sıktır."],
  """Femoral kılıfın lateral bölmesinde arter, orta bölmesinde ven, medial bölmesinde femoral kanal bulunur. Kanalın
  ağzı (anulus femoralis) dar ve sert sınırlı (lig. lacunare) olduğundan femoral herniler sıklıkla boğulur; kadınlarda
  daha sıktır.""",
  e=["trigonum-femorale", "lig-inguinale", "a-femoralis"]),

Q("f", VB, "Fossa poplitea'nın sınırları için hangisi doğrudur?",
  "Üstte biceps femoris ile semimembranosus–semitendinosus, altta gastrocnemius'un iki başı",
  ["Üstte sartorius ve gracilis, altta soleus", "Üstte quadriceps, altta tibialis anterior",
   "Üstte adductor magnus, altta fibularis longus", "Üstte gluteus maximus, altta popliteus"],
  """Elmas biçimli popliteal çukurun üst-dış sınırı biceps femoris, üst-iç sınırı semimembranosus ve semitendinosus,
  alt sınırları gastrocnemius'un lateral ve medial başlarıdır. Tabanını femurun popliteal yüzü, diz kapsülü ve
  popliteus kası yapar.""",
  e=["fossa-poplitea", "m-biceps-femoris", "m-triceps-surae"]),

Q("f", VB, "Fossa cubitalis'in sınırları hangisinde doğru verilmiştir?",
  "Üstte iki epikondili birleştiren çizgi, dışta m. brachioradialis, içte m. pronator teres",
  ["Üstte akromiyon, dışta deltoid, içte biceps", "Dışta m. pronator teres, içte m. brachioradialis",
   "Üstte olecranon, altta radius başı", "Dışta m. flexor carpi ulnaris, içte m. brachialis"],
  """Kübital çukurun tabanında brachialis ve supinator, tavanında fasya ve aponeurosis bicipitalis bulunur. İçinde
  dıştan içe biseps tendonu, a. brachialis ve n. medianus yer alır.""",
  e=["fossa-cubitalis", "m-brachioradialis", "m-pronator-teres"]),

Q("t", VB, "Boynun arka üçgeninde yüzeyel seyreden ve lenf nodu biyopsilerinde en sık yaralanan sinir hangisidir?",
  "N. accessorius",
  ["N. phrenicus", "N. vagus", "N. hypoglossus", "Truncus sympathicus"],
  """Arka üçgen SCM'nin arka kenarı, trapezius'un ön kenarı ve klavikula arasındadır. N. accessorius üçgeni SCM'nin
  ortasından trapezius'a doğru çapraz geçer ve yalnızca deri ile yüzeyel fasya altındadır. Frenik sinir daha derinde,
  prevertebral fasyanın altındadır.""",
  e=["trigona-colli", "n-accessorius"]),

Q("t", VB, "Transpilorik düzlem (Addison düzlemi, yaklaşık L1) aşağıdakilerden hangisinden geçmez?",
  "Göbek",
  ["Pilor", "Pankreas boynu", "Böbrek hilusları", "SMA'nın aortadan çıkış yeri"],
  """Transpilorik düzlem juguler çentik ile symphysis'in üst kenarı arasındaki çizginin orta noktasından geçer; pilor,
  pankreas boynu, duodenojejunal bükümün yakını, böbrek hilusları, SMA'nın çıkışı ve safra kesesi fundusu bu düzeye
  yakındır. Göbek genellikle L3–L4 düzeyindedir.""",
  e=["regiones-abdominis", "pancreas", "ren"]),

Q("t", VB, "Kasık (inguinal) kanalın duvarları ile ilgili hangisi doğrudur?",
  "Ön duvar dış oblik aponevrozu, arka duvar fascia transversalis, taban lig. inguinale",
  ["Ön duvar fascia transversalis, arka duvar dış oblik aponevrozu", "Tavan lig. inguinale, taban conjoint tendon",
   "Arka duvar m. rectus abdominis, ön duvar m. transversus abdominis", "Ön duvar periton, arka duvar m. psoas"],
  """Kanalın tavanını iç oblik ve transversus kaslarının kemer yapan lifleri, tabanını lig. inguinale ve lig. lacunare
  oluşturur. Arka duvarın medial kısmı conjoint tendonla güçlenir; direkt fıtıklar bu duvarın zayıflığından çıkar.""",
  e=["canalis-inguinalis", "lig-inguinale", "m-obliquus-externus"]),

Q("fv", VB, """Uzun süre koşan hastada ayak tabanı ve parmaklarda yanma ve uyuşma var; medial malleolün arkasına
vurulunca ayak tabanına elektriklenme yayılıyor. Sıkışan sinir ve yeri hangisidir?""",
  "N. tibialis – tarsal tünel (retinaculum musculorum flexorum altında)",
  ["N. fibularis profundus – ön tarsal tünel", "N. suralis – lateral malleol arkası",
   "N. saphenus – addüktör kanal", "N. plantaris lateralis – Guyon kanalı"],
  """Tarsal tünel sendromu karpal tünelin ayaktaki karşılığıdır. N. tibialis veya plantar dalları sıkışır; topuk derisi
  (rr. calcanei) çoğunlukla tünelden önce ayrıldığı için korunabilir.""",
  e=["canalis-tarsi", "n-tibialis"]),

Q("f", VB, "Deltopektoral üçgende fascia clavipectoralis'i delerek v. axillaris'e açılan yüzeyel ven hangisidir?",
  "V. cephalica",
  ["V. basilica", "V. mediana cubiti", "V. jugularis externa", "V. thoracoepigastrica"],
  """V. cephalica kolun dış yanında yükselir, deltoid ile pectoralis major arasındaki oluğu izler ve deltopektoral üçgende
  fasyayı delerek v. axillaris'e açılır. Bu bölgede kalp pili elektrotları için cutdown yapılabilir.""",
  e=["trigonum-deltopectorale", "vv-membri-superioris"]),
]

write("integumentary", questions)
