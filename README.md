# Anatomi Atlası

Etkileşimli, üç boyutlu ve Türkçe bir insan anatomisi atlası (iOS / iPadOS 27, SwiftUI + RealityKit).

Bu sürüm **kas-iskelet sistemine** odaklanır: iskelet, eklemler ve bağlar, kaslar ve kas yapışma yerleri; kalp ve damarlar da açıktır. Diğer sistemlerin
içeriği ve 3D katmanları kodda ve uygulama paketinde durur; `Anatomy/Models/AppScope.swift`'teki listelere eklendiklerinde
atlasa, Keşfet'e, soru bankasına ve bilgi kartlarına geri gelir.

## Özellikler

- **3D atlas**: 9 katman (iskelet, eklemler ve bağlar, kaslar, kas yapışma yerleri, kalp ve damarlar, lenfoid organlar, sinir sistemi ve duyu organları, iç organlar, deri ve bölgeler) ve yaklaşık 3.900 seçilebilir parça; bu sürümde iskelet, eklemler, kaslar, kas yapışma yerleri, kalp ve damarlar ile sinir sistemi açıktır.
  - Döndürme, kaydırma, yakınlaştırma; dokunarak seçme, odaklama, izole etme, gizleme ve saydamlaştırma
  - Uzaklığa göre detay seviyesi (LOD, meshoptimizer): tüm vücut 4,3 milyon yerine ~0,8 milyon üçgenle çizilir; ekranda görünmeyen parçalar en kaba seviyede tutulur
  - 32 baytlık sıkıştırılmış köşe biçimi, dokulu yüzey gölgelendiricisi (clearcoat), ekran yenilemesine bağlı kamera animasyonları, ana iş parçacığı dışında seçim ve etiket hesabı
  - İstek üzerine çizim (`RealityCanvas`, RealityRenderer): sahne yalnızca kamera hareket ettiğinde, bir şey değiştiğinde ya da seçim parlarken (birkaç saniye) çizilir; durağan atlas ekran kartını çalıştırmaz. Telefon ısındığında yalnızca kamera hareket ederken ayrıntı azaltılır
  - İç organlar BodyParts3D 3.0'dan (karaciğer segmentleri, mide, bağırsaklar, akciğer lobları ve segmental bronşlar, böbrekler…); kadın üreme organları, kadın mesanesi ve meme bezi Human Reference Atlas'tan; erkek/kadın görünümü değiştirilebilir, bir cinsiyete özgü bir yapı açıldığında atlas o görünüme geçer
  - **İki ayrı model (Erkek / Kadın)**: araç çubuğundaki seçiciyle değişir. Deri BodyParts3D'nin kendi derisidir (iskeletle aynı bedenden), bu yüzden kemik ve dokulara birebir uyar; sade bir yüzeydir (doku resmi ve kıl yok), gözler atlasın kendi göz küreleridir. Kadın modelinde deri ve bütün katmanlar kadın bedenine bir hacim dönüşüm alanıyla (`warp-female.bin`) taşınır; göğüs ve kasık biçimi MakeHuman (CC0) kadın bedeninden alınır, yumuşak dokular köşe başına düzeltmelerle (`female-fix.bin`) derinin altında tutulur. Deri katmanı beta olarak işaretlidir.
  - Kaynak modellerde olmayan yapılar çevre anatomiye göre modellendi: vajina, kadın üretrası, kadın dış genital bölge derisi, skrotum, perikard, ductus thoracicus, cisterna chyli, sağ lenf kanalı, faringeal (adenoid) ve lingual tonsil; çekum ve anal kanal kolon ve rektumdan ayrıldı
  - **Gerçekçi** ve **Öğretici** renk modları
  - **Diseksiyon** paneli (araç çubuğundaki makas): **kas katmanları** kaydırıcısı kasları yüzeyelden derine soyar (6 katman, `muscle-layers.json`; `tools/dissection_layers.py` Blender'da her kasın dışarıdan görünen yüzeyini ölçerek katmanları sırayla çıkarır), **kesit** yatay, sagital ya da koronal bir düzlemle modeli keser; kesilen yüzler koyu bir kesit rengiyle gösterilir ve kesilen taraf değiştirilebilir (`AnatomyScene+Section.swift`, gölgelendiricinin `anatomySurfaceSection` sürümü). Panelde röntgen görünümü de vardır
  - Seçilen yapıya kamera yumuşakça yaklaşır ve onu seçim kartının üstünde ortalar (Profil > Ayarlar'dan kapatılabilir)
  - **Sade görünüm**: sistem çubuğu ve arama tek düğmeye katlanır, araç çubuğu yalnızca simgelerle gösterilir; model ekranın tamamını kullanır
  - Her parçanın Türkçe adı, Latince adı ve kısa Türkçe açıklaması (2.993 terim)
  - **Yapı adları**: Türkçe ve Almancada Latince ad önde, dilin kendi adı altında (Profil > Ayarlar > "Latince adlar önde"; İngilizce, Fransızca ve İspanyolcada
    varsayılan kapalı). Etiketlerde uzun Latince biçimler kısaltılır ("musculi" → "m."). Ad sırası `AtlasStore.title`/`subtitle`'dadır
- **İnceleme modu**: yapı tek başına, koyu bir sahnede açılır; Z-Anatomy'nin 740 oluşum etiketi **Latince ad + Türkçe alt başlık** (ya da ayara göre tersi) ve kısa Türkçe açıklamayla gösterilir. Kaslar bağlandıkları kemiklerle, başlangıç (kırmızı) ve tutunma (mavi) yerleriyle açılır; her pin üzerinde durduğu kemik oluşumunun adını taşır ("Supraglenoid tüberkül · Kürek kemiği"). Kemiklerde atlas metinlerinde ve sorularda en çok geçen oluşumlar önce etiketlenir (`landmarks.json`'daki `rank`).
  - Bir etikete ya da modelin bir noktasına dokununca o oluşumun bölgesi model üzerinde **renkli olarak parlar** (parçalı yapılarda, örneğin karaciğer segmentlerinde tüm parça) ve kamera o bölgeye döner; kartta "Yakınlaş" vardır
  - "Oluşumlar" listesi: yapının tüm işaretli oluşumları aranabilir listede; seçilen oluşuma kamera gider ve bölgesi renklenir
- **İçerik**: açık sistemlerde 369 Türkçe madde (72 kemik ve iskelet yapısı, 45 eklem ve bağ, 206 kas, 46 kalp ve damar; kasların çoğu tek tek, gruplarına bağlı olarak), paket içinde 13 sistemde 564 madde. Her maddede Türkçe, Latince (TA2) ve İngilizce ad, temel bilgiler (origo, insersiyo, innervasyon, kanlanma, dallar…), bölümler, klinik bilgi, **TUS notları**, ilişkili yapılar ve 3D karşılığı bulunur.
- **Çalış**:
  - **Soru bankası**: açık sistemlerde 900 özgün soru (kemik 218, eklem 142, kas 260, kalp ve damar 140, sinir sistemi 140; paket içinde toplam 1.125), üç düzey (**Temel**, Fakülte, TUS), beş seçenek, ayrıntılı açıklama ve çoğunda seçenek notları; sistem, konu ve düzey bazında testler
  - Atlas maddelerinden üretilen sorular: Latince terimler, ayrıntı soruları (özelliklerden yapıyı bulma dahil), tanım, 3D tanıma, **kas ve sinirleri** ("hangisi n. femoralis tarafından innerve EDİLMEZ?"; sinir aileleri dalları kapsar), **kemik oluşumları** (488 oluşum: hangi kemikte, hangi kemikte bulunur), grup üyeliği ve TUS/klinik notlarından yapıyı bulma
  - **Deneme sınavları** (mini, temel tekrar, TUS, komite, maraton): süreli, soru haritası, işaretleme, TUS neti, sistemlere göre sonuç ve tüm soruların açıklamalı incelemesi
  - Yanlışlarım, işaretlediklerim, zayıf konular
  - **Aralıklı tekrar** bilgi kartları (Tekrar / Zor / İyi / Kolay): 6 deste ve 3.000'i aşkın kart (yapı, Latince ad, origo–insersiyo–sinir ve diğer ayrıntılar, kemik oluşumları, TUS bilgileri, klinik bilgiler); her kartın kendi takvimi vardır, sistem ve konu seçilebilir
  - **İstatistikler**: 30 günlük grafik, sistemlere göre başarı, en zayıf yapılar, deneme netleri; günlük hedef ve seri
  - **Günlük tekrar hatırlatması** (Profil): seçilen saatte, o gün çalışılmadıysa bekleyen kart sayısıyla bildirim; 7 gün ileriye planlanır ve uygulama arka plana geçtikçe yenilenir (`ReviewReminder.swift`). Bildirime dokununca Çalış sekmesi açılır
  - Her madde sayfasında "Bu konudan soru çöz"
- **Premium** (StoreKit 2; aylık, yıllık, ömür boyu): ücretsiz sürümde iskelet sistemi ve günde 10 soru açıktır; diğer sistemler, inceleme modu, kadın anatomisi, deneme sınavları ve istatistikler Premium'dadır. Aboneliği bitmiş kullanıcıya App Store Connect'te tanımlanan **kazandırma (win-back) teklifi** varsa satın alma ekranında o plan seçili gelir ve teklif "Sana özel" olarak gösterilir.
- **Tanılama**: MetricKit çökme ve performans raporları cihazda saklanır (en fazla 20); Profil'deki "Tanılama raporlarını gönder" ile kullanıcı isterse paylaşır (`Diagnostics.swift`). Atlas ve inceleme yükleme süreleri signpost olarak ölçülür.
- **Profil**: Premium durumu, sistem bazında ilerleme, ayarlar (renk modu, üreme organları, çalışma düzeyi, günlük hedef), favoriler, son bakılanlar, kaynaklar ve lisanslar.

## Proje yapısı

| Klasör | İçerik |
| --- | --- |
| `Anatomy/Model3D` | Mesh paketleri (`MeshPack`, `PackLibrary`), atlas sahnesi (`AnatomyScene`), inceleme sahnesi (`SpecimenScene`), Metal gölgelendirici (`AnatomyShaders.metal`), malzemeler ve renk kuralları (`MaterialStyle`) |
| `Anatomy/Models` | İçerik modeli, `AtlasStore`, `QuestionBank`, `QuizEngine`, `QuizSession`, `StudyStore`, `PurchaseStore`, `AppModel` |
| `Anatomy/Views` | Atlas, keşfet, madde, arama, çalış (soru, sınav, sonuç, kartlar, istatistik), profil, Premium ve tanıtım ekranları; `Theme.swift` tasarım dili |
| `Anatomy/Content` | `atlas-*.json` maddeler, `questions-*.json` soru bankası ve `terms.json` Türkçe parça sözlüğü (`tools/content` ile üretilir) |
| `Anatomy/Resources` | 3D mesh paketleri (`Models/mesh-*.bin/json`), oluşum etiketleri (`Models/labels.json`), Z-Anatomy malzeme renkleri ve `glossary.json` |
| `tools` | Blender dışa aktarma, sözlük ve içerik üretim betikleri |

### 3D modelleri yeniden üretmek

Gerekenler: Blender 5.x ve Z-Anatomy `Startup.blend` dosyası ([Z-Anatomy/Models-of-human-anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy) reposundaki `Z-Anatomy.zip`).

```bash
Blender -b Startup.blend --python tools/export_zanatomy.py -- <çıktı-klasörü>
Blender -b Startup.blend --python tools/export_labels.py -- Anatomy/Resources/Models/labels.json
Blender -b Startup.blend --python tools/dump_zanatomy_texts.py -- texts.json
swiftc -O tools/bake_ao.swift -o bake_ao && ./bake_ao <çıktı-klasörü>/mesh-*.bin
cp <çıktı-klasörü>/mesh-* Anatomy/Resources/Models/
python3 tools/build_glossary.py texts.json TA2.csv
```

Dışa aktarma betiği her sistem için şunları yapar:

- Belirlenen üçgen bütçesine göre modeli sadeleştirir
- Koordinatları Y-yukarı sisteme çevirir
- Konumları 16 bit, normalleri 8 bit olarak sıkıştırır
- Üçgenleri malzemeye göre sıralar; her parçanın malzeme dilimlerini (`seg`) kaydeder
- `mesh-<sistem>.bin` (raw deflate, "ANT1") ve `mesh-<sistem>.json` (parça ve malzeme listesi) dosyalarını yazar

`bake_ao` her köşe için ortam örtmesini hesaplar: BVH üzerinde 28 ışın gönderir ve örtü dokularını hesaba katmaz. Sonucu pakete ekleyip dosyayı "ANT2" olarak yeniden yazar.

### Yüksek ayrıntılı modeller (İnceleme modu)

Gerekenler: [BodyParts3D 3.0](https://dbarchive.biosciencedbc.jp/data/bodyparts3d/20110915/) `BodyParts3D_3.0_obj_95.zip` ve `parts_list_e.txt` (DBCLS, CC BY-SA 2.1 JP).

```bash
Blender -b --python tools/build_hd.py -- <obj-klasörü> parts_list_e.txt <çıktı> skeletal visceral
./bake_ao <çıktı>/hd-skeletal.bin <çıktı>/hd-visceral.bin
python3 tools/merge_hd.py Anatomy/Resources/Models/mesh-skeletal.{bin,json} <çıktı>/hd-skeletal.{bin,json} <birleşik>
./bake_ao <birleşik>/mesh-skeletal.bin && cp <birleşik>/mesh-skeletal.* Anatomy/Resources/Models/
python3 tools/pack_hd.py <çıktı>/hd-visceral.bin Anatomy/Resources/Models
```

İskeletin ayrıntılı kemikleri `merge_hd` ile doğrudan atlas paketine konur; atlasta da kullanılırlar (iskelet 702 bin yerine 1,95 milyon üçgen). Organlar ayrı tutulur ve yalnızca İnceleme modunda açılır.

`build_hd` parçaları adlarından eşleştirir. Önce tüm vücut için tek bir benzerlik dönüşümü, sonra her parça için rijit ICP uygular. Yalnızca iki yönde de yüzeyleri birkaç milimetre içinde örtüşen ve daha ayrıntılı olan modelleri tutar; Z-Anatomy'nin yeniden modellediği organlar (karaciğer, mide gibi) bu yüzden elenir. Malzeme bölgeleri (eklem kıkırdağı gibi) en yakın Z-Anatomy üçgeninden aktarılır. `pack_hd` her parçayı ayrı sıkıştırır ("ANH1"), böylece uygulama yalnızca açılan yapıyı çözer.

`export_labels` Z-Anatomy'deki etiketlerin işaret çizgilerini (`.i`/`.j` nesneleri) izler ve her etiketin yüzeydeki noktasını bulur.

Z-Anatomy'de bazı kasların başlangıç ve tutunma yerleri ters işaretlenmiştir (ör. trapezius, serratus anterior, suboksipital kaslar). Bunlar maddelerdeki origo/insersiyo bilgisiyle karşılaştırılmış ve `MaterialStyles.isOrigin` içinde düzeltilmiştir.

### Detay seviyeleri (LOD)

```bash
python3 tools/build_lods.py <meshoptimizer-klasörü> [--models Anatomy/Resources/Models] [sistem...]
```

`tools/lod/lodgen.cpp` meshoptimizer ile her parçanın %30 ve %8'lik iki sade sürümünü aynı köşeleri paylaşarak üretir; paketler "ANT3" olarak (her seviye için parça başına hata ve indeks listesi) yeniden yazılır. Uygulama her parçanın seviyesini ekrandaki hata miktarına göre seçer (`AnatomyScene+Camera.updateDetail`).

### İç organlar

```bash
tools/rebuild_organs.sh <orijinal-paketler> <bp3d-obj> <parts_list_e.txt> <hra-klasörü> <meshoptimizer> <çalışma-klasörü>
```

`build_organs.py` BodyParts3D organlarını önce genel benzerlik dönüşümü, sonra organ başına rijit ICP ile atlasa hizalar; akciğer segmentlerinin malzemelerini aktarır. `add_female.py` Human Reference Atlas'ın kadın üreme organlarını ve kadın mesanesini pelvise hizalar, üreterlerin kadın kopyalarını bu mesaneye bağlar ve parçaları cinsiyetle işaretler (`"sex": "m"/"f"`). `add_extras.py` çekumu ve anal kanalı keserek ayırır; meme bezini (HRA) göğüs duvarına oturtur; vajina, kadın üretrası, kadın dış genital deri bölgesi, skrotum, perikard, ductus thoracicus, cisterna chyli, sağ lenf kanalı ve faringeal/lingual tonsili çevre yapılardan modeller. Başka yapıları saran parçalar (perikard, skrotum, meme yağ dokusu) `"covering": true` alır: uygulamada varsayılan olarak gizlenir, `bake_ao` ise ışığı bunlardan geçirir. `bake_ao` öteki cinsiyetin organlarını gölge hesabında yok sayar; iki cinsiyette ortak parçalar iki sahnenin ortalamasını alır.

HRA klasöründe `uterus-female.glb`, `ovary-female-left/right.glb`, `fallopian-tube-female-left/right.glb`, `urinary-bladder-female.glb`, `pelvis-female.glb` ve `mammary-gland-female-left.glb` bulunmalıdır ([3D referans kütüphanesi](https://humanatlas.io/3d-reference-library)).

### Deri ve kadın modeli

`tools/skin/` deri ve kadın modeli araçlarını içerir. Deri: `bp3d_skin_prep.py` BodyParts3D derisini (FMA7163; deri ile deri altı yağın katı katmanı) kemik merkezlerinden bulunan tek bir benzerlik dönüşümüyle atlasa taşır ve dış yüzeyini ayırır; `bp3d_skin.py` dış yüzeyin altında kalması gereken her kemik, kas, damar, sinir ve organ noktası için deriyi yumuşak tümseklerle birkaç milimetre kaldırır, üçgenleri en yakın Z-Anatomy bölgesine göre bölgelere ayırır, göz açıklıklarına atlasın göz kürelerini koyar ve kadın derisini kurar (penis ve skrotum çevresi kesilip MakeHuman kadın kasığı dikilir, göğüs MakeHuman kadın bedeninden taşınır, uyluklar orta hatta buluşur). Kadın modeli: `write_warp.py` (dönüşüm alanını uygulamanın biçimine yazar), `warp_eval.py` (alanı Python'da değerlendirir), `female_fix.py` (kadın modeli için köşe düzeltmeleri; meme dokusunu ve burun kemiklerini de derinin altına alır), `fit_breast.py` (meme dokusunu kadın göğsüne yerleştirir), `replace_parts.py` (yeniden yerleştirilen meme parçalarını iç paketlere aktarır). Ayrıca `fit_inside.py`, `fit_bronchi.py`, `pushout.py`, `packedit.py` (paket okuma/yazma) ve önceki MakeHuman derisinin araçları (`genitals_male.py`, `vulva.py`).

`tools/regroup.py`, Z-Anatomy'nin hiyerarşide gruplamadığı el kemiklerini "El kemikleri" altında el bileği, tarak ve parmak kemikleri olarak gruplar (`export_zanatomy.py` bunu her dışa aktarımda uygular; tek başına çalıştırıldığında mevcut manifestleri düzeltir).

### İçeriği yeniden üretmek

```bash
tools/content/build_all.sh
python3 tools/content/terms/build.py
python3 tools/content/landmarks.py
```

- `tools/content/*.py`: maddeler (`viscera_extra.py`, `others_extra.py` ek maddeler; `tus_*.py` TUS notları, `common.write` sırasında eklenir)
- `tools/content/muscular_detail_axial.py`, `muscular_detail_limbs.py`: grup maddelerinin (ör. M. quadriceps femoris) altındaki tek tek kaslar; her biri `parent` alanıyla grubuna bağlanır, grup maddesi de onları ilişkili yapılarında listeler. Bir 3D parça onu listeleyen en özgül maddeye (en az modelli) aittir.
- `tools/content/landmarks.py`: inceleme etiketlerinden kemik oluşumu listesi (`landmarks.json`: Türkçe/Latince ad, açıklama, kemiğin maddesi, atlas ve sorulardaki geçme sayısı). Birden çok kemikte bulunan genel omur oluşumları dışarıda bırakılır. Kemik oluşumu soruları, kartları ve inceleme ekranındaki etiket önceliği bu dosyadan gelir.
- `tools/content/questions/q_*.py`: soru bankası. Her soru `Q(düzey, konu, kök, doğru, [4 çeldirici], açıklama, notlar, e=[madde id'leri])` biçimindedir; seçenekler kökten türetilen sabit bir tohumla karıştırılır, böylece sorunun kimliği ve sırası derlemeler arasında değişmez. `questions/validate.py` madde bağlantılarını ve doğru cevap dağılımını denetler.
- `tools/content/terms/*.py`: 3D parçaların ve inceleme etiketlerinin Türkçe sözlüğü (`features.py` adlar, `features_desc.py` açıklamalar, `fixes.py` son düzeltmeler ve eksik Latinceler)

Betik maddelerin `models` alanının gerçekten bir 3D parçaya karşılık geldiğini ve `related` bağlantılarının geçerli olduğunu da doğrular.

### Ekran görüntüsü için açılış argümanları

- `-AtlasLayers skeletal,visceral`: başlangıç katmanları
- `-AtlasGhost skeletal`: saydam başlayacak katmanlar
- `-AtlasCamera "x,y,z,mesafe,yaw"`: kamera konumu
- `-AtlasHideSide muscular:r`: bir katmanın tek tarafını gizler
- `-AtlasSection "horizontal,1.3[,above]"`: kesitle açar (`sagittal`, `horizontal` ya da `coronal`; düzlemin konumu metre cinsinden; üçüncü değer verilirse düzlemin üstü kalır)
- `-AtlasNoChrome YES`: kontrolleri gizler
- `-AtlasColors educational`: öğretici renklerle açar
- `-AtlasInspect "Femur"`: açılışta bir yapıyı inceleme modunda gösterir
- `-AtlasReveal "Popliteus muscle"`: açılışta bir yapıyı atlasta bulur
- `-atlas.labels YES`: etiketleri açar
- `-AppTab study`: başka bir sekmeyle açar (`atlas`, `systems`, `study`, `library`, `search`)
- `-AtlasSex female`: kadın anatomisiyle açar
- `-StartQuiz mixed|bank|clinical|terms|facts|model|weak|exam|cards`: açılışta bir test, deneme sınavı veya kart destesi başlatır
- `-PremiumUnlocked YES`: Premium'u açar (yalnızca geliştirme), `-SkipOnboarding YES`: tanıtımı atlar
- `-AtlasDebugLOD YES`: çizilen üçgen sayısını gösterir
- `-atlas.compact YES`: atlası sade görünümle açar
- `-OpenEntry hepar`: açılışta bir madde sayfası gösterir, `-ShowPaywall YES`: Premium ekranını açar
- `-StartQuiz key:cv-ac08c79d,g|model|m-deltoideus`: belirli soruları sırayla açar; `-QuizReveal YES` ilk soruyu doğru cevaplar
- `-SkipSplash YES`: açılış animasyonunu atlar, `-AtlasNoHint YES`: hareket ipucunu göstermez
- `-ForceLandscape YES` (yalnızca geliştirme): pencereyi yatay çevirir (alçak ekran düzeni denemeleri)
- `-WindowSize 669x951` (yalnızca geliştirme): pencereyi iPad'de bu boyuta küçültür (iPhone Duo ekranları)

### App Store ekran görüntüleri

`tools/screenshots/` görüntüleri iki adımda üretir:

1. `python3 tools/screenshots/capture.py <udid> <aygıt> [diller] [--only 01-atlas …]` uygulamayı simülatörde yukarıdaki argümanlarla
   açar ve ham ekranları `raw/<aygıt>/<dil>/` altına kaydeder (`iphone69`: iPhone 18 Pro Max, `ipad13`: iPad Pro 13 inç).
   iPhone Duo ekranları tam ekran bir iPad'de alınır: `--window 466x678` (dış ekran) veya `--window 669x951` (iç ekran) uygulamanın
   penceresini o boyuta küçültür ve boyut sınıfını ona göre ayarlar (`-WindowSize`, yalnızca geliştirme), görüntü pencereden kırpılır
   (`duo-outer`, `duo-inner`). Yavaş aygıtlarda `WAIT_SCALE=1.4` bekleme süresini uzatır.
2. `python3 tools/screenshots/compose.py [diller] [--device …] [--slide …]` her ekranı cihaz çerçevesi, başlık, ışık şeridi ve etiketlerle
   birleştirip headless Chrome ile App Store Connect ölçülerinde çizer: `out/<dil>/<aygıt>/` (iPhone 6,9 inç 1320×2868, 6,3 inç 1206×2622,
   iPad 13 inç 2064×2752, iPhone Duo dış ekran 1398×2034, iç ekran 2007×2853). Başlıklar `captions.py`'dedir.

`raw/` ve `out/` git'e eklenmez.

**Ürün sayfası başlığı ve arama sonucu** (App Store Connect > Header and Search Results, iOS 27): `render_figures.py` Blender ile
atlas paketlerinden dört figürü (deri, kaslar, iskelet, kalp ve damarlar) çizer (`still` tek kare, `turntable` 360 karelik dönüş);
`compose_creative.py header|video|search` bunlardan `out/creative/header.png` (3840×1646, metinsiz), `header.mp4` (12 sn döngü,
30 fps) ve her dil için `out/creative/<dil>/search.png` (3840×2560) üretir. Önemli öğeler Apple şablonlarındaki güvenli alanlarda kalır
(başlık ortadaki 1646×661, arama x 836–3004 / y 765–1795); deri figürü 4+ yaş sınırı için genital bölgesiz beyaz silüet olarak çizilir.

## Yerelleştirme

Uygulama Türkçe (kaynak), İngilizce, Fransızca, Almanca ve İspanyolca'dır; cihaz başka bir dildeyse İngilizce açılır.

- **Arayüz**: `Anatomy/Localizable.xcstrings`, `tools/i18n/ui/<dil>.py` sözlüklerinden `python3 tools/i18n/build_ui.py` ile doldurulur
  (önce `xcodebuild -exportLocalizations -project Anatomy.xcodeproj -localizationPath <klasör> -exportLanguage en` ile anahtarlar yenilenir).
  Aynı Türkçe kelimenin iki anlamı olduğunda kodda `defaultValue`'lu bir anahtar kullanılır (`flashcard.again`, `view.front`…);
  bunların Türkçesi `build_ui.py`'deki `TURKISH` tablosundadır.
- **İçerik**: kas-iskelet kapsamındaki maddeler, sorular, parça sözlüğü ve oluşumlar `Anatomy/Content/*.<dil>.json` dosyalarındadır.
  Çeviri kaynakları `tools/i18n/content/src/*.py`; `python3 tools/i18n/content.py build` birleştirir, `status` eksikleri listeler.
- **App Store metinleri**: `tools/i18n/appstore.md` (sınırlar: `python3 tools/i18n/check_appstore.py`).

## App Store notları

- Ürünler (`Anatomy/Products.storekit`, App Store Connect'te aynı kimliklerle oluşturulmalı): `com.adilemre.anatomi.premium.monthly`, `…premium.yearly` (otomatik yenilenen abonelik, aynı grup) ve `…premium.lifetime` (tüketilmeyen). Fiyatlar yer tutucudur.
- `Anatomy.xcscheme` StoreKit yapılandırmasını kullanır; gerçek satın alma testleri için TestFlight veya sandbox hesabı gerekir.
- `PrivacyInfo.xcprivacy`: izleme yok, veri toplama yok; yalnızca UserDefaults (CA92.1). `ITSAppUsesNonExemptEncryption = NO`.
- Uygulamanın sitesi `docs/` klasöründedir ve https://anatomi.adilemree.xyz adresinde yayındadır: ana sayfa, `/privacy` (gizlilik, Türkçe + İngilizce), `/terms` (kullanım ve abonelik koşulları, Apple'ın standart EULA'sına bağlantı içerir) ve `/destek`. `/gizlilik`, `/kosullar`, `/support` bu sayfalara yönlenir. Uygulamadaki bağlantılar `Legal` (PaywallView.swift) içindedir.
  Sunucuda dosyalar `/var/www/anatomi`, nginx sitesi `/etc/nginx/sites-available/anatomi` (127.0.0.1:8140), dışarıya Cloudflare tüneli (`/etc/cloudflared/config.yml`) açar. Güncellemek için: `rsync -az --delete docs/ root@SUNUCU:/var/www/anatomi/`.
- Uygulama verileri (ilerleme, favoriler, sınav geçmişi) yalnızca cihazda tutulur.

## Lisanslar ve kaynaklar

- **3D modeller**: [Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy), CC BY-SA 4.0. Modeller sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır. Değiştirilmiş modeller (`Anatomy/Resources/Models`) de CC BY-SA 4.0 lisansıyla sunulur.
- **BodyParts3D**: Z-Anatomy modelleri bu veritabanından türetilmiştir. İnceleme modundaki yüksek ayrıntılı modeller (`hd-*.bin`) BodyParts3D 3.0 verisinden hazırlanmıştır. BodyParts3D, © The Database Center for Life Science (DBCLS), CC BY-SA 2.1 JP.
- **Deri**: BodyParts3D derisi (FMA7163), CC BY-SA 2.1 JP. **Kadın bedeninin biçimi**: [MakeHuman](https://www.makehumancommunity.org) taban modeli, CC0 1.0.
- **Kadın üreme organları, kadın mesanesi ve meme bezi**: [Human Reference Atlas](https://humanatlas.io) (HuBMAP, Visible Human Female), CC BY 4.0.
- **meshoptimizer**: © Arseny Kapoulkine, MIT (yalnızca araç olarak, uygulamaya gömülü değildir).
- **İngilizce kaynak metinler** (`glossary.json`): Z-Anatomy / Wikipedia, CC BY-SA.
- **Latince terimler**: Terminologia Anatomica 2 (FIPAT).
- **Türkçe içerik, sözlük ve sorular**: bu proje için özgün olarak hazırlanmıştır; ÖSYM veya yayınevi soruları kullanılmamıştır.

Uygulama eğitim amaçlıdır; tıbbi tanı ve tedavi için kullanılmamalıdır.
