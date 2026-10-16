# Anatomi Atlası

Etkileşimli, üç boyutlu ve Türkçe bir insan anatomisi atlası (iOS / iPadOS 27, SwiftUI + RealityKit).

## Özellikler

- **3D atlas**: 9 katman (iskelet, eklemler ve bağlar, kaslar, kas yapışma yerleri, kalp ve damarlar, lenfoid organlar, sinir sistemi ve duyu organları, iç organlar, deri ve bölgeler) ve yaklaşık 3.900 seçilebilir parça.
  - Döndürme, kaydırma, yakınlaştırma; dokunarak seçme, odaklama, izole etme, gizleme ve saydamlaştırma
  - Uzaklığa göre detay seviyesi (LOD, meshoptimizer): tüm vücut 4,3 milyon yerine ~0,8 milyon üçgenle çizilir; ekranda görünmeyen parçalar en kaba seviyede tutulur
  - 32 baytlık sıkıştırılmış köşe biçimi, dokulu yüzey gölgelendiricisi (clearcoat), ekran yenilemesine bağlı kamera animasyonları, ana iş parçacığı dışında seçim ve etiket hesabı
  - İç organlar BodyParts3D 3.0'dan (karaciğer segmentleri, mide, bağırsaklar, akciğer lobları ve segmental bronşlar, böbrekler…); kadın üreme organları, kadın mesanesi ve meme bezi Human Reference Atlas'tan; erkek/kadın görünümü değiştirilebilir, bir cinsiyete özgü bir yapı açıldığında atlas o görünüme geçer
  - **İki ayrı model (Erkek / Kadın)**: araç çubuğundaki seçiciyle değişir. Deri, yüz ve dokular MakeHuman'dan (CC0); deri atlas derisine oturtuldu (katı olmayan ICP), yüz göz ve ağız noktalarından kafatasına hizalandı. Kadın modelinde iskelet, kaslar, damarlar, sinirler ve organlar kadın derisine göre bir hacim dönüşüm alanıyla (`warp-female.bin`) ve köşe başına düzeltmelerle (`female-fix.bin`) biçimlendirilir; meme ve vulva doğrudan kadın bedeninde modellenmiştir. Deri katmanında kıl yoktur (kaş ve kirpik hariç).
  - Kaynak modellerde olmayan yapılar çevre anatomiye göre modellendi: vajina, kadın üretrası, kadın dış genital bölge derisi, skrotum, perikard, ductus thoracicus, cisterna chyli, sağ lenf kanalı, faringeal (adenoid) ve lingual tonsil; çekum ve anal kanal kolon ve rektumdan ayrıldı
  - **Gerçekçi** ve **Öğretici** renk modları
  - Seçilen yapıya kamera yumuşakça yaklaşır ve onu seçim kartının üstünde ortalar (Profil > Ayarlar'dan kapatılabilir)
  - **Sade görünüm**: sistem çubuğu ve arama tek düğmeye katlanır, araç çubuğu yalnızca simgelerle gösterilir; model ekranın tamamını kullanır
  - Her parçanın Türkçe adı, Latince adı ve kısa Türkçe açıklaması (2.993 terim)
- **İnceleme modu**: yapı tek başına, koyu bir sahnede açılır; Z-Anatomy'nin 740 oluşum etiketi **Türkçe ad + Latince alt başlık** ve kısa Türkçe açıklamayla gösterilir. Kaslar bağlandıkları kemiklerle, başlangıç (kırmızı) ve tutunma (mavi) yerleriyle açılır.
  - Bir etikete ya da modelin bir noktasına dokununca o oluşumun bölgesi model üzerinde **renkli olarak parlar** (parçalı yapılarda, örneğin karaciğer segmentlerinde tüm parça) ve kamera o bölgeye döner; kartta "Yakınlaş" vardır
  - "Oluşumlar" listesi: yapının tüm işaretli oluşumları aranabilir listede; seçilen oluşuma kamera gider ve bölgesi renklenir
- **İçerik**: 13 sistemde 416 Türkçe madde. Her maddede Türkçe, Latince (TA2) ve İngilizce ad, temel bilgiler (origo, insersiyo, innervasyon, kanlanma, dallar…), bölümler, klinik bilgi, **TUS notları**, ilişkili yapılar ve 3D karşılığı bulunur.
- **Çalış**:
  - **Soru bankası**: 597 özgün soru (311 TUS, 286 fakülte düzeyi; 159 klinik vaka), beş seçenek, ayrıntılı açıklama ve seçenek notları; sistem ve konu bazında testler
  - Atlas maddelerinden üretilen sorular: Latince terimler, ayrıntı soruları (özelliklerden yapıyı bulma dahil), tanım ve 3D tanıma
  - **Deneme sınavları**: süreli, soru haritası, işaretleme, TUS neti, sistemlere göre sonuç ve tüm soruların açıklamalı incelemesi
  - Yanlışlarım, işaretlediklerim, zayıf konular
  - **Aralıklı tekrar** bilgi kartları (Tekrar / Zor / İyi / Kolay)
  - **İstatistikler**: 30 günlük grafik, sistemlere göre başarı, en zayıf yapılar, deneme netleri; günlük hedef ve seri
  - Her madde sayfasında "Bu konudan soru çöz"
- **Premium** (StoreKit 2; aylık, yıllık, ömür boyu): ücretsiz sürümde iskelet sistemi ve günde 10 soru açıktır; diğer sistemler, inceleme modu, kadın anatomisi, deneme sınavları ve istatistikler Premium'dadır.
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

`tools/skin/` deri ve kadın modeli araçlarını içerir: `write_warp.py` (dönüşüm alanını uygulamanın biçimine yazar), `warp_eval.py` (alanı Python'da değerlendirir), `fit_inside.py` (yumuşak dokuları erkek derisinin altına alır), `fit_breast.py` (meme dokusunu kadın göğsüne yerleştirir), `fit_bronchi.py` (segment bronşlarını akciğer içinde tutar), `female_fix.py` (kadın modeli için köşe düzeltmeleri; kadın biçiminde modellenen meme dokusunu ve kadının küçük burnundan taşan burun kemiklerini de derinin altına alır), `pushout.py` (deriyi kemiklerin üzerinde kaldırır; erkek burun kökünde geniş ve öne doğru yumuşak bir kabartma), `genitals_male.py` (penis ve skrotum derisi; kesenin üst yarısı kasık derisine kavuşarak asılı durur, penis kökü gövdeye yumuşak girer), `replace_parts.py` (yeniden yerleştirilen meme parçalarını iç paketlere aktarır), `vulva.py` (kadın dış genitali: kasık orta hattı boyunca yükseklik alanı olarak kurulan, deriye dikilen yama; açıklıklar iç organlara hizalı), `packedit.py` (paket okuma/yazma). MakeHuman gövdesinin pozlanması, oturtulması, ayak parmaklarının Z-Anatomy ayağına parmak parmak oturtulması, yüz hizalaması, kadın kasığının açılması ve doku boyama adımları çalışma klasöründeki betiklerle (`mh/`) yapılır.

`tools/regroup.py`, Z-Anatomy'nin hiyerarşide gruplamadığı el kemiklerini "El kemikleri" altında el bileği, tarak ve parmak kemikleri olarak gruplar (`export_zanatomy.py` bunu her dışa aktarımda uygular; tek başına çalıştırıldığında mevcut manifestleri düzeltir).

### İçeriği yeniden üretmek

```bash
tools/content/build_all.sh
python3 tools/content/terms/build.py
```

- `tools/content/*.py`: maddeler (`viscera_extra.py`, `others_extra.py` ek maddeler; `tus_*.py` TUS notları, `common.write` sırasında eklenir)
- `tools/content/questions/q_*.py`: soru bankası. Her soru `Q(düzey, konu, kök, doğru, [4 çeldirici], açıklama, notlar, e=[madde id'leri])` biçimindedir; seçenekler kökten türetilen sabit bir tohumla karıştırılır, böylece sorunun kimliği ve sırası derlemeler arasında değişmez. `questions/validate.py` madde bağlantılarını ve doğru cevap dağılımını denetler.
- `tools/content/terms/*.py`: 3D parçaların ve inceleme etiketlerinin Türkçe sözlüğü (`features.py` adlar, `features_desc.py` açıklamalar, `fixes.py` son düzeltmeler ve eksik Latinceler)

Betik maddelerin `models` alanının gerçekten bir 3D parçaya karşılık geldiğini ve `related` bağlantılarının geçerli olduğunu da doğrular.

### Ekran görüntüsü için açılış argümanları

- `-AtlasLayers skeletal,visceral`: başlangıç katmanları
- `-AtlasGhost skeletal`: saydam başlayacak katmanlar
- `-AtlasCamera "x,y,z,mesafe,yaw"`: kamera konumu
- `-AtlasHideSide muscular:r`: bir katmanın tek tarafını gizler
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
- **Deri, yüz ve deri dokuları**: [MakeHuman](https://www.makehumancommunity.org) taban modeli ve dokuları, CC0 1.0.
- **Kadın üreme organları, kadın mesanesi ve meme bezi**: [Human Reference Atlas](https://humanatlas.io) (HuBMAP, Visible Human Female), CC BY 4.0.
- **meshoptimizer**: © Arseny Kapoulkine, MIT (yalnızca araç olarak, uygulamaya gömülü değildir).
- **İngilizce kaynak metinler** (`glossary.json`): Z-Anatomy / Wikipedia, CC BY-SA.
- **Latince terimler**: Terminologia Anatomica 2 (FIPAT).
- **Türkçe içerik, sözlük ve sorular**: bu proje için özgün olarak hazırlanmıştır; ÖSYM veya yayınevi soruları kullanılmamıştır.

Uygulama eğitim amaçlıdır; tıbbi tanı ve tedavi için kullanılmamalıdır.
