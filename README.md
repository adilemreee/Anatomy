# Anatomi Atlası

Etkileşimli, üç boyutlu ve Türkçe bir insan anatomisi atlası (iOS / iPadOS 27, SwiftUI + RealityKit).

## Özellikler

- **3D atlas**: 9 katman (iskelet, eklemler ve bağlar, kaslar, kas yapışma yerleri, kalp ve damarlar, lenfoid organlar, sinir sistemi ve duyu organları, iç organlar, deri ve bölgeler) ve toplam 3.858 seçilebilir parça.
  - Tek parmakla döndürme, iki parmakla kaydırma, çimdikleyerek yakınlaştırma
  - Dokunarak parça seçme; parçayı odaklama, izole etme ve gizleme
  - Katmanları saydam yapma, röntgen görünümü, hazır görünümler
  - Model üzerinde yapı etiketleri
  - Model hiyerarşisine göre parça tarayıcısı ve arama
  - Kendi Metal yüzey gölgelendiricisi: kas lifleri, kemik dokusu, organ yüzeyi, önceden hesaplanmış ortam örtmesi (AO), kenar ışığı ve zemin gölgesi
  - **Gerçekçi** (kadavra renkleri) ve **Öğretici** (kaslar hareketine, beyin lobları ayrı renklerde) renk modları, renk açıklamasıyla
  - Bir kasın bir başına dokununca kasın tüm başları birlikte seçilir
- **İnceleme modu** (seçim kartında *İncele*, madde sayfasında *3D İncele*): yapı tek başına, koyu bir sahnede açılır.
  - Kemik ve organlarda Z-Anatomy'nin 740 oluşum etiketi Latince ve İngilizce adlarla gösterilir (ör. *Caput ossis femoris*). Etiketler çakışmayacak şekilde yerleşir; dokununca açıklama kartı açılır.
  - Kaslar bağlandıkları kemiklerle birlikte açılır. Başlangıç yerleri kırmızı, tutunma yerleri mavi işaretlenir; kasın başları da etiketlenir.
  - Açılış görünümü, yapının en çok görünen yüzünü gösteren açıdan seçilir (ör. atlas omuru üstten, kalça kemiği yandan).
  - 187 kemik ve 7 organ, BodyParts3D'nin yüksek ayrıntılı (yaklaşık 4 kat) modelleriyle gösterilir; yüzeyler ayrıca PN üçgenleriyle pürüzsüzleştirilir.
- Aranan ya da sorulan bir yapı atlasta en iyi göründüğü yönden gösterilir; üstünü örten yapılar saydamlaşır (ör. diz arkası kası, supraspinatus).
- **İçerik**: 13 sistemde 358 Türkçe madde. Her madde Türkçe, Latince (TA) ve İngilizce adlarla birlikte gelir. Ayrıca şunları içerir:
  - Temel bilgiler: origo, insersiyo, innervasyon, kanlanma, fonksiyon, dallar, eklemler…
  - Ayrıntılı bölümler ve klinik notlar
  - İlişkili yapılar ve 3D modeldeki karşılığı
- **Sözlük**: Her 3D parça için Terminologia Anatomica 2'den Latince ad ve Z-Anatomy'nin İngilizce kaynak metni.
- **Çalış**:
  - Karma test, Latince terimler, ayrıntı soruları ve 3D tanıma testleri
  - Zayıf konular modu
  - Bilgi kartları
  - Günlük seri ve doğruluk takibi
- **Kitaplığım**: Sistem bazında ilerleme, favoriler, son bakılanlar, kaynaklar ve lisanslar.

## Proje yapısı

| Klasör | İçerik |
| --- | --- |
| `Anatomy/Model3D` | Mesh paketleri (`MeshPack`, `PackLibrary`), atlas sahnesi (`AnatomyScene`), inceleme sahnesi (`SpecimenScene`), Metal gölgelendirici (`AnatomyShaders.metal`), malzemeler ve renk kuralları (`MaterialStyle`) |
| `Anatomy/Models` | İçerik modeli, `AtlasStore`, `StudyStore`, `QuizEngine`, `AppModel` |
| `Anatomy/Views` | Atlas, sistemler, madde, arama, çalışma ve kitaplık ekranları |
| `Anatomy/Content` | `atlas-*.json` içerik dosyaları (`tools/content` ile üretilir) |
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
python3 tools/pack_hd.py <çıktı>/hd-skeletal.bin Anatomy/Resources/Models
python3 tools/pack_hd.py <çıktı>/hd-visceral.bin Anatomy/Resources/Models
```

`build_hd` parçaları adlarından eşleştirir. Önce tüm vücut için tek bir benzerlik dönüşümü, sonra her parça için rijit ICP uygular. Yalnızca iki yönde de yüzeyleri birkaç milimetre içinde örtüşen ve daha ayrıntılı olan modelleri tutar; Z-Anatomy'nin yeniden modellediği organlar (karaciğer, mide gibi) bu yüzden elenir. Malzeme bölgeleri (eklem kıkırdağı gibi) en yakın Z-Anatomy üçgeninden aktarılır. `pack_hd` her parçayı ayrı sıkıştırır ("ANH1"), böylece uygulama yalnızca açılan yapıyı çözer.

`export_labels` Z-Anatomy'deki etiketlerin işaret çizgilerini (`.i`/`.j` nesneleri) izler ve her etiketin yüzeydeki noktasını bulur.

Z-Anatomy'de bazı kasların başlangıç ve tutunma yerleri ters işaretlenmiştir (ör. trapezius, serratus anterior, suboksipital kaslar). Bunlar maddelerdeki origo/insersiyo bilgisiyle karşılaştırılmış ve `MaterialStyles.isOrigin` içinde düzeltilmiştir.

### İçeriği yeniden üretmek

```bash
tools/content/build_all.sh
```

Betik tüm `atlas-*.json` dosyalarını üretir. Ardından her maddenin `models` alanının gerçekten bir 3D parçaya karşılık geldiğini ve `related` bağlantılarının geçerli olduğunu doğrular.

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

## Lisanslar ve kaynaklar

- **3D modeller**: [Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy), CC BY-SA 4.0. Modeller sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır. Değiştirilmiş modeller (`Anatomy/Resources/Models`) de CC BY-SA 4.0 lisansıyla sunulur.
- **BodyParts3D**: Z-Anatomy modelleri bu veritabanından türetilmiştir. İnceleme modundaki yüksek ayrıntılı modeller (`hd-*.bin`) BodyParts3D 3.0 verisinden hazırlanmıştır. BodyParts3D, © The Database Center for Life Science (DBCLS), CC BY-SA 2.1 JP.
- **İngilizce kaynak metinler** (`glossary.json`): Z-Anatomy / Wikipedia, CC BY-SA.
- **Latince terimler**: Terminologia Anatomica 2 (FIPAT).
- **Türkçe içerik**: bu proje için hazırlanmıştır.

Uygulama eğitim amaçlıdır; tıbbi tanı ve tedavi için kullanılmamalıdır.
