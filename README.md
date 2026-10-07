# Anatomi Atlası

Etkileşimli, üç boyutlu ve Türkçe bir insan anatomisi atlası (iOS / iPadOS 27, SwiftUI + RealityKit).

## Özellikler

- **3D atlas**: 9 katman (iskelet, eklemler ve bağlar, kaslar, kas yapışma yerleri, kalp ve damarlar, lenfoid organlar, sinir sistemi ve duyu organları, iç organlar, deri ve bölgeler) ve toplam 3.858 seçilebilir parça.
  - Tek parmakla döndürme, iki parmakla kaydırma, çimdikleyerek yakınlaştırma
  - Dokunarak parça seçme; parçayı odaklama, izole etme ve gizleme
  - Katmanları saydam yapma, röntgen görünümü, hazır görünümler
  - Model üzerinde yapı etiketleri
  - Model hiyerarşisine göre parça tarayıcısı ve arama
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
| `Anatomy/Model3D` | Mesh paketlerini okuma (`MeshPack`), RealityKit sahnesi (`AnatomyScene`), görüntüleyici ve hareketler, renk paleti |
| `Anatomy/Models` | İçerik modeli, `AtlasStore`, `StudyStore`, `QuizEngine`, `AppModel` |
| `Anatomy/Views` | Atlas, sistemler, madde, arama, çalışma ve kitaplık ekranları |
| `Anatomy/Content` | `atlas-*.json` içerik dosyaları (`tools/content` ile üretilir) |
| `Anatomy/Resources` | 3D mesh paketleri (`Models/mesh-*.bin/json`) ve `glossary.json` |
| `tools` | Blender dışa aktarma, sözlük ve içerik üretim betikleri |

### 3D modelleri yeniden üretmek

Gerekenler: Blender 5.x ve Z-Anatomy `Startup.blend` dosyası ([Z-Anatomy/Models-of-human-anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy) reposundaki `Z-Anatomy.zip`).

```bash
Blender -b Startup.blend --python tools/export_zanatomy.py -- <çıktı-klasörü>
Blender -b Startup.blend --python tools/dump_zanatomy_texts.py -- texts.json
cp <çıktı-klasörü>/mesh-* Anatomy/Resources/Models/
python3 tools/build_glossary.py texts.json TA2.csv
```

Dışa aktarma betiği her sistem için şunları yapar:

- Belirlenen üçgen bütçesine göre modeli sadeleştirir
- Koordinatları Y-yukarı sisteme çevirir
- Konumları 16 bit, normalleri 8 bit olarak sıkıştırır
- `mesh-<sistem>.bin` (raw deflate) ve `mesh-<sistem>.json` (parça listesi) dosyalarını yazar

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
- `-atlas.labels YES`: etiketleri açar

## Lisanslar ve kaynaklar

- **3D modeller**: [Z-Anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy), CC BY-SA 4.0. Modeller sadeleştirilmiş, yeniden renklendirilmiş ve sistemlere ayrılmıştır. Değiştirilmiş modeller (`Anatomy/Resources/Models`) de CC BY-SA 4.0 lisansıyla sunulur.
- **BodyParts3D**: Z-Anatomy modelleri bu veritabanından türetilmiştir. BodyParts3D, © The Database Center for Life Science (DBCLS).
- **İngilizce kaynak metinler** (`glossary.json`): Z-Anatomy / Wikipedia, CC BY-SA.
- **Latince terimler**: Terminologia Anatomica 2 (FIPAT).
- **Türkçe içerik**: bu proje için hazırlanmıştır.

Uygulama eğitim amaçlıdır; tıbbi tanı ve tedavi için kullanılmamalıdır.
