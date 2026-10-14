"""Whole muscles whose attachment patches carry the parent muscle's name
(the other patches reuse the muscle terms from muscular.py)."""
from common import T

for en, tr, la, d in [
    ("Triceps surae muscle", "Triceps surae (baldır kası)", "Musculus triceps surae", "Gastroknemiusun iki başı ve soleustan oluşan kas grubu; Aşil tendonuyla kalkaneusa tutunarak ayağa plantar fleksiyon yaptırır. N. tibialis (S1–S2)."),
    ("Articularis genus muscle", "Diz eklem kası", "Musculus articularis genus", "Vastus intermedius'un derin lifleri; diz ekstansiyonunda suprapatellar bursayı yukarı çekerek sıkışmasını önler."),
    ("Iliopsoas muscle", "İliopsoas kas", "Musculus iliopsoas", "Psoas major ve iliak kasın trochanter minor'a ortak tutunan birleşimi; kalçanın en güçlü fleksörüdür."),
    ("Trochanteric insertion", "Trokanterik yapışma alanı", "Insertio trochanterica", "Derin kalça rotatorlarının trochanter major çevresindeki ortak tutunma alanı."),
    ("Biceps femoris muscle", "Biseps femoris kas", "Musculus biceps femoris", "Uzun ve kısa başı fibula başına tutunan lateral hamstring kası; dizi büker, bükülü dizde bacağı dışa döndürür."),
    ("Patellar ligament", "Patellar bağ", "Ligamentum patellae", "Quadriceps tendonunun patelladan tuberositas tibiae'ye uzanan devamı; patellar refleks (L3–L4) bu bağa vurularak alınır."),
    ("Quadriceps femoris muscle", "Kuadriseps femoris (dört başlı uyluk kası)", "Musculus quadriceps femoris", "Rectus femoris ve üç vastus kasından oluşan güçlü diz ekstansörü; patellaya ve patellar bağ aracılığıyla tibiaya tutunur. N. femoralis (L2–L4)."),
    ("Erector spinae", "Erector spinae (omurga dikleştirici kaslar)", "Musculus erector spinae", "İliokostal, longissimus ve spinalis sütunlarından oluşan derin sırt kası; omurgayı dikleştirir ve geriye büker. Spinal sinirlerin arka dalları."),
    ("Levator ani", "Levator ani", "Musculus levator ani", "Pubokoksigeal, puboanal ve iliokoksigeal kısımlardan oluşan pelvik taban kası; pelvik organları destekler ve kontinansa katılır. S4 ve n. pudendus dalları."),
    ("Adductor pollicis", "Başparmak adduktörü", "Musculus adductor pollicis", "Oblik ve transvers başlı derin el kası; başparmağı avuca yaklaştırır. N. ulnaris (derin dal)."),
    ("Common extensor tendon", "Ortak ekstansör tendon", "Tendo extensorius communis", "Önkol arka bölmesi yüzeyel kaslarının lateral epikondilden başlayan ortak tendonu; dejenerasyonu tenisçi dirseğidir."),
    ("Common flexor tendon", "Ortak fleksör tendon", "Tendo flexorius communis", "Önkol ön bölmesi yüzeyel kaslarının medial epikondilden başlayan ortak tendonu; dejenerasyonu golfçü dirseğidir."),
    ("Deltoid muscle", "Deltoid kas", "Musculus deltoideus", "Omzu örten üçgen kas; klaviküler, akromiyal ve spinal kısımları humerusun tuberositas deltoidea'sına tutunur. N. axillaris (C5–C6); humerus boyun kırığında felç olabilir."),
    ("Pronator teres", "Pronator teres", "Musculus pronator teres", "İki başlı önkol kası; radiusun gövdesinin ortasına tutunarak pronasyon yaptırır. N. medianus."),
    ("Flexor digitorum superficialis", "Yüzeyel parmak fleksörü", "Musculus flexor digitorum superficialis", "Dört tendonu orta falankslara tutunan kas; PIP eklemlerini büker. N. medianus."),
    ("Flexor carpi ulnaris", "Ulnar el bileği fleksörü", "Musculus flexor carpi ulnaris", "Pisiforma (ve pisohamat, pisometakarpal bağlar aracılığıyla hamat ile 5. metakarpa) tutunur; eli büker ve ulnara saptırır. N. ulnaris."),
    ("Biceps brachii muscle", "Biseps brakii (iki başlı kol kası)", "Musculus biceps brachii", "Tuberositas radii'ye ve lacertus fibrosus ile önkol fasyasına tutunan kas; güçlü supinatör ve dirsek fleksörüdür. N. musculocutaneus; biseps refleksi C5–C6."),
    ("Extensor carpi ulnaris", "Ulnar el bileği ekstansörü", "Musculus extensor carpi ulnaris", "5. metakarp tabanına tutunur; eli uzatır ve ulnara saptırır. N. interosseus posterior."),
    ("Triceps brachii muscle", "Triseps brakii (üç başlı kol kası)", "Musculus triceps brachii", "Uzun, lateral ve medial başı olekranona tutunan tek dirsek ekstansörü. N. radialis; triseps refleksi C7."),
    ("Pectoralis major muscle", "Büyük göğüs kası", "Musculus pectoralis major", "Klaviküler, sternokostal ve abdominal kısımları humerusun crista tuberculi majoris'ine tutunan yelpaze kas; kolu içe çeker ve içe döndürür. Nn. pectorales medialis et lateralis."),
    ("Lateral pterygoid muscle", "Lateral pterigoid kas", "Musculus pterygoideus lateralis", "Üst ve alt başıyla mandibula kondiline ve eklem diskine tutunur; ağzı açan ve çeneyi öne çeken çiğneme kasıdır."),
    ("Masseter", "Masseter (çiğneme kası)", "Musculus masseter", "Elmacık kemerinden mandibula açısına uzanan, vücudun ağırlığına göre en güçlü kaslarından biri; çeneyi kapatır. N. massetericus (V3)."),
]:
    T(en, tr, la, d)
