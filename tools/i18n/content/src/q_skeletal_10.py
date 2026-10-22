KIND = "questions"
SYSTEM = "skeletal"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("sk-f0c708e7",
  ("About how many bones are there in the adult human skeleton?", ["186", "256", "226", "206", "300"],
   "The adult skeleton has about 206 bones: 80 in the axial skeleton and 126 in the appendicular skeleton. In the newborn the number is around 270–300 because many parts have not yet fused."),
  ("Combien d'os compte environ le squelette humain adulte ?", ["186", "256", "226", "206", "300"],
   "Le squelette adulte compte environ 206 os : 80 dans le squelette axial et 126 dans le squelette appendiculaire. Chez le nouveau-né, on en compte 270 à 300 car de nombreuses pièces ne sont pas encore soudées."),
  ("Aus wie vielen Knochen besteht das Skelett des Erwachsenen ungefähr?", ["186", "256", "226", "206", "300"],
   "Das Skelett des Erwachsenen hat etwa 206 Knochen: 80 im Achsenskelett und 126 im Extremitätenskelett. Beim Neugeborenen sind es etwa 270–300, weil viele Teile noch nicht verschmolzen sind."),
  ("¿Aproximadamente cuántos huesos tiene el esqueleto humano adulto?", ["186", "256", "226", "206", "300"],
   "El esqueleto adulto tiene unos 206 huesos: 80 en el esqueleto axial y 126 en el apendicular. En el recién nacido hay unos 270–300 porque muchas piezas aún no se han fusionado."))

T("sk-93d7b509",
  ("Which is the longest and strongest bone of the body?", ["Humerus", "Fibula", "Tibia", "Femur", "Hip bone"],
   "The femur (thigh bone) is the longest, heaviest and strongest bone of the body; it is about a quarter of a person's height."),
  ("Quel est l'os le plus long et le plus solide du corps ?", ["Humérus", "Fibula", "Tibia", "Fémur", "Os coxal"],
   "Le fémur (os de la cuisse) est l'os le plus long, le plus lourd et le plus solide du corps ; il représente environ un quart de la taille."),
  ("Welcher ist der längste und stärkste Knochen des Körpers?", ["Humerus", "Fibula", "Tibia", "Femur", "Hüftbein"],
   "Der Femur (Oberschenkelknochen) ist der längste, schwerste und stärkste Knochen des Körpers; er macht etwa ein Viertel der Körpergröße aus."),
  ("¿Cuál es el hueso más largo y fuerte del cuerpo?", ["Húmero", "Peroné", "Tibia", "Fémur", "Coxal"],
   "El fémur (hueso del muslo) es el hueso más largo, pesado y fuerte del cuerpo; mide alrededor de un cuarto de la estatura."))

T("sk-a3b15dfd",
  ("Which is the smallest bone of the body?", ["Lacrimal bone", "Malleus (hammer)", "Pisiform", "Stapes (stirrup)", "Incus (anvil)"],
   "Of the three ossicles of the middle ear, the stapes is the smallest bone of the body; its footplate fits into the oval window."),
  ("Quel est le plus petit os du corps ?", ["Os lacrymal", "Malléus (marteau)", "Pisiforme", "Stapes (étrier)", "Incus (enclume)"],
   "Des trois osselets de l'oreille moyenne, l'étrier est le plus petit os du corps ; sa platine s'enchâsse dans la fenêtre ovale."),
  ("Welcher ist der kleinste Knochen des Körpers?", ["Tränenbein", "Malleus (Hammer)", "Erbsenbein", "Stapes (Steigbügel)", "Incus (Amboss)"],
   "Von den drei Gehörknöchelchen des Mittelohrs ist der Steigbügel der kleinste Knochen des Körpers; seine Fußplatte sitzt im ovalen Fenster."),
  ("¿Cuál es el hueso más pequeño del cuerpo?", ["Lagrimal", "Martillo", "Pisiforme", "Estribo", "Yunque"],
   "De los tres huesecillos del oído medio, el estribo es el hueso más pequeño del cuerpo; su platina encaja en la ventana oval."))

T("sk-59a23a69",
  ("Which membrane, rich in vessels and nerves, covers the outer surface of bone?", ["Perichondrium", "Fascia", "Endosteum", "Periosteum", "Synovial membrane"],
   "The periosteum covers the outer surface of bone; cells of its inner layer allow the bone to thicken and fractures to heal. Joint surfaces have no periosteum and are covered by hyaline cartilage. The endosteum lines the marrow cavity."),
  ("Quelle membrane, riche en vaisseaux et en nerfs, recouvre la face externe de l'os ?", ["Périchondre", "Fascia", "Endoste", "Périoste", "Membrane synoviale"],
   "Le périoste recouvre la face externe de l'os ; les cellules de sa couche profonde assurent la croissance en épaisseur et la consolidation des fractures. Les surfaces articulaires n'ont pas de périoste mais du cartilage hyalin. L'endoste tapisse la cavité médullaire."),
  ("Welche gefäß- und nervenreiche Haut überzieht die Außenfläche des Knochens?", ["Perichondrium", "Faszie", "Endost", "Periost", "Synovialmembran"],
   "Das Periost überzieht die Knochenoberfläche; die Zellen seiner inneren Schicht ermöglichen Dickenwachstum und Frakturheilung. Gelenkflächen haben kein Periost, sondern hyalinen Knorpel. Das Endost kleidet die Markhöhle aus."),
  ("¿Qué membrana, rica en vasos y nervios, cubre la superficie externa del hueso?", ["Pericondrio", "Fascia", "Endostio", "Periostio", "Membrana sinovial"],
   "El periostio cubre la superficie externa del hueso; las células de su capa interna permiten el crecimiento en grosor y la consolidación de las fracturas. Las superficies articulares no tienen periostio, sino cartílago hialino. El endostio tapiza la cavidad medular."))

T("sk-4df6a75a",
  ("What is the shaft of a long bone called?", ["Epiphyseal plate", "Diaphysis", "Epiphysis", "Apophysis", "Metaphysis"],
   "The shaft of a long bone is the diaphysis, its ends the epiphyses and the growth zone between them the metaphysis. Inside the diaphysis is the medullary cavity containing bone marrow."),
  ("Comment appelle-t-on le corps d'un os long ?", ["Cartilage de croissance", "Diaphyse", "Épiphyse", "Apophyse", "Métaphyse"],
   "Le corps d'un os long est la diaphyse, ses extrémités les épiphyses et la zone de croissance intermédiaire la métaphyse. La diaphyse contient la cavité médullaire avec la moelle osseuse."),
  ("Wie heißt der Schaft eines Röhrenknochens?", ["Epiphysenfuge", "Diaphyse", "Epiphyse", "Apophyse", "Metaphyse"],
   "Der Schaft eines Röhrenknochens ist die Diaphyse, die Enden sind die Epiphysen und die Wachstumszone dazwischen die Metaphyse. Im Schaft liegt die Markhöhle mit dem Knochenmark."),
  ("¿Cómo se llama el cuerpo de un hueso largo?", ["Placa epifisaria", "Diáfisis", "Epífisis", "Apófisis", "Metáfisis"],
   "El cuerpo de un hueso largo es la diáfisis, sus extremos las epífisis y la zona de crecimiento entre ambos la metáfisis. Dentro de la diáfisis está la cavidad medular con la médula ósea."))

T("sk-45e4abe2",
  ("Which cell breaks down (resorbs) bone?", ["Fibroblast", "Osteocyte", "Osteoclast", "Chondrocyte", "Osteoblast"],
   "Osteoclasts are multinucleated cells of monocyte origin that break down bone tissue. Osteoblasts build new bone, and osteocytes are mature cells embedded in bone."),
  ("Quelle cellule détruit (résorbe) l'os ?", ["Fibroblaste", "Ostéocyte", "Ostéoclaste", "Chondrocyte", "Ostéoblaste"],
   "Les ostéoclastes sont des cellules multinucléées d'origine monocytaire qui résorbent le tissu osseux. Les ostéoblastes fabriquent l'os et les ostéocytes sont des cellules matures emmurées dans l'os."),
  ("Welche Zelle baut Knochen ab (resorbiert ihn)?", ["Fibroblast", "Osteozyt", "Osteoklast", "Chondrozyt", "Osteoblast"],
   "Osteoklasten sind mehrkernige Zellen monozytären Ursprungs, die Knochengewebe abbauen. Osteoblasten bilden neuen Knochen, Osteozyten sind reife, eingemauerte Knochenzellen."),
  ("¿Qué célula destruye (reabsorbe) el hueso?", ["Fibroblasto", "Osteocito", "Osteoclasto", "Condrocito", "Osteoblasto"],
   "Los osteoclastos son células multinucleadas de origen monocítico que reabsorben el tejido óseo. Los osteoblastos forman hueso nuevo y los osteocitos son células maduras incluidas en el hueso."))

T("sk-900539f3",
  ("In which tissue are blood cells produced?", ["Periosteum", "Compact bone", "Articular cartilage", "Red bone marrow", "Yellow bone marrow"],
   "Blood cells are made in red bone marrow. In adults red marrow lies mainly in the flat bones (sternum, ribs, hip bone, vertebrae); the marrow in the shafts of long bones turns into fatty yellow marrow."),
  ("Dans quel tissu les cellules sanguines sont-elles produites ?", ["Périoste", "Os compact", "Cartilage articulaire", "Moelle osseuse rouge", "Moelle osseuse jaune"],
   "L'hématopoïèse a lieu dans la moelle rouge. Chez l'adulte, elle se trouve surtout dans les os plats (sternum, côtes, os coxal, vertèbres) ; la moelle des diaphyses devient une moelle jaune graisseuse."),
  ("In welchem Gewebe werden Blutzellen gebildet?", ["Periost", "Kompakta", "Gelenkknorpel", "Rotes Knochenmark", "Gelbes Knochenmark"],
   "Die Blutbildung erfolgt im roten Knochenmark. Beim Erwachsenen liegt es vor allem in den platten Knochen (Sternum, Rippen, Hüftbein, Wirbel); das Mark der Röhrenknochenschäfte wird zu fettreichem gelbem Mark."),
  ("¿En qué tejido se producen las células sanguíneas?", ["Periostio", "Hueso compacto", "Cartílago articular", "Médula ósea roja", "Médula ósea amarilla"],
   "La hematopoyesis ocurre en la médula ósea roja. En el adulto está sobre todo en los huesos planos (esternón, costillas, coxal, vértebras); la médula de las diáfisis se convierte en médula amarilla grasa."))

T("sk-6f3cbcfe",
  ("Where do long bones grow in length?", ["In the articular cartilage", "In the endosteum", "In the periosteum", "In the middle of the shaft", "In the epiphyseal plate (growth cartilage)"],
   "Growth in length takes place in the epiphyseal plate of the metaphysis as cartilage cells multiply and ossify; the plate closes at the end of puberty. Growth in width occurs by the periosteum adding new bone."),
  ("Où les os longs grandissent-ils en longueur ?", ["Dans le cartilage articulaire", "Dans l'endoste", "Dans le périoste", "Au milieu de la diaphyse", "Dans le cartilage de croissance (plaque épiphysaire)"],
   "La croissance en longueur se fait au niveau du cartilage de croissance de la métaphyse, par multiplication et ossification des chondrocytes ; il se ferme à la fin de la puberté. La croissance en largeur se fait par apposition périostée."),
  ("Wo wachsen Röhrenknochen in die Länge?", ["Im Gelenkknorpel", "Im Endost", "Im Periost", "In der Schaftmitte", "In der Epiphysenfuge (Wachstumsfuge)"],
   "Das Längenwachstum erfolgt in der Epiphysenfuge der Metaphyse durch Vermehrung und Verknöcherung der Knorpelzellen; die Fuge schließt sich am Ende der Pubertät. Das Dickenwachstum erfolgt durch Anlagerung vom Periost aus."),
  ("¿Dónde crecen en longitud los huesos largos?", ["En el cartílago articular", "En el endostio", "En el periostio", "En el centro de la diáfisis", "En la placa epifisaria (cartílago de crecimiento)"],
   "El crecimiento en longitud se produce en la placa epifisaria de la metáfisis, por multiplicación y osificación de los condrocitos; la placa se cierra al final de la pubertad. El crecimiento en anchura se produce por aposición desde el periostio."))

T("sk-1a21cd83",
  ("Which of the following bones belongs to the axial skeleton?", ["Scapula", "Humerus", "Clavicle", "Hip bone", "Sternum"],
   "The axial skeleton consists of the skull, vertebral column and thoracic cage (sternum and ribs). The clavicle and scapula belong to the shoulder girdle, the hip bone to the pelvic girdle and the humerus to the free upper limb."),
  ("Lequel de ces os appartient au squelette axial ?", ["Scapula", "Humérus", "Clavicule", "Os coxal", "Sternum"],
   "Le squelette axial comprend le crâne, la colonne vertébrale et la cage thoracique (sternum et côtes). Clavicule et scapula appartiennent à la ceinture scapulaire, l'os coxal à la ceinture pelvienne et l'humérus au membre supérieur libre."),
  ("Welcher der folgenden Knochen gehört zum Achsenskelett?", ["Scapula", "Humerus", "Klavikula", "Hüftbein", "Sternum"],
   "Das Achsenskelett besteht aus Schädel, Wirbelsäule und Brustkorb (Sternum und Rippen). Klavikula und Scapula gehören zum Schultergürtel, das Hüftbein zum Beckengürtel und der Humerus zur freien oberen Extremität."),
  ("¿Cuál de los siguientes huesos pertenece al esqueleto axial?", ["Escápula", "Húmero", "Clavícula", "Coxal", "Esternón"],
   "El esqueleto axial está formado por el cráneo, la columna vertebral y la caja torácica (esternón y costillas). Clavícula y escápula pertenecen a la cintura escapular, el coxal a la pélvica y el húmero al miembro superior libre."))

T("sk-2db88c9e",
  ("Which of the following is an example of a flat bone?", ["Vertebra", "Parietal bone", "Femur", "Capitate", "Metacarpal"],
   "Flat bones are thin and broad (skull vault, sternum, ribs, scapula). The femur and metacarpals are long bones, the capitate a short bone and the vertebrae irregular bones."),
  ("Lequel de ces os est un os plat ?", ["Vertèbre", "Os pariétal", "Fémur", "Capitatum", "Métacarpien"],
   "Les os plats sont minces et larges (voûte du crâne, sternum, côtes, scapula). Le fémur et les métacarpiens sont des os longs, le capitatum un os court et les vertèbres des os irréguliers."),
  ("Welcher der folgenden ist ein platter Knochen?", ["Wirbel", "Scheitelbein", "Femur", "Kopfbein", "Mittelhandknochen"],
   "Platte Knochen sind dünn und breit (Schädeldach, Sternum, Rippen, Scapula). Femur und Mittelhandknochen sind Röhrenknochen, das Kopfbein ein kurzer und die Wirbel unregelmäßige Knochen."),
  ("¿Cuál de los siguientes es un hueso plano?", ["Vértebra", "Parietal", "Fémur", "Grande", "Metacarpiano"],
   "Los huesos planos son delgados y anchos (bóveda craneal, esternón, costillas, escápula). El fémur y los metacarpianos son huesos largos, el grande un hueso corto y las vértebras huesos irregulares."))

T("sk-a98a93de",
  ("Which of the following is NOT a sesamoid bone?", ["Fabella", "Lunate", "Sesamoid of the big toe", "Patella", "Pisiform"],
   "Sesamoid bones develop within tendons: the patella, the pisiform, the sesamoids under the MP joints of the thumb and big toe and, in some people, the fabella. The lunate is a short bone of the proximal carpal row."),
  ("Lequel de ces os n'est PAS un sésamoïde ?", ["Fabella", "Lunatum", "Sésamoïde de l'hallux", "Patella", "Pisiforme"],
   "Les sésamoïdes se développent dans des tendons : patella, pisiforme, sésamoïdes sous les MP du pouce et de l'hallux et, chez certains, la fabella. Le lunatum est un os court de la rangée proximale du carpe."),
  ("Welcher der folgenden ist KEIN Sesambein?", ["Fabella", "Mondbein", "Sesambein der Großzehe", "Patella", "Erbsenbein"],
   "Sesambeine entstehen in Sehnen: Patella, Erbsenbein, die Sesambeine unter den Grundgelenken von Daumen und Großzehe und bei manchen Menschen die Fabella. Das Mondbein ist ein kurzer Knochen der proximalen Handwurzelreihe."),
  ("¿Cuál de los siguientes NO es un hueso sesamoideo?", ["Fabela", "Semilunar", "Sesamoideo del dedo gordo", "Rótula", "Pisiforme"],
   "Los sesamoideos se desarrollan dentro de tendones: rótula, pisiforme, sesamoideos bajo las MF del pulgar y del dedo gordo y, en algunas personas, la fabela. El semilunar es un hueso corto de la fila proximal del carpo."))

T("sk-66a08b42",
  ("Which bone forms the forehead and the roof of the orbits?", ["Frontal bone", "Sphenoid bone", "Zygomatic bone", "Ethmoid bone", "Parietal bone"],
   "The frontal bone forms the forehead with its vertical squamous part and the roofs of the orbits and floor of the anterior cranial fossa with its horizontal orbital part."),
  ("Quel os forme le front et le toit des orbites ?", ["Frontal", "Sphénoïde", "Zygomatique", "Ethmoïde", "Pariétal"],
   "L'os frontal forme le front par son écaille verticale et, par sa partie orbitaire horizontale, le toit des orbites et le plancher de la fosse crânienne antérieure."),
  ("Welcher Knochen bildet die Stirn und das Dach der Augenhöhlen?", ["Stirnbein", "Keilbein", "Jochbein", "Siebbein", "Scheitelbein"],
   "Das Stirnbein bildet mit seiner senkrechten Schuppe die Stirn und mit seiner waagerechten Pars orbitalis das Orbitadach und den Boden der vorderen Schädelgrube."),
  ("¿Qué hueso forma la frente y el techo de las órbitas?", ["Frontal", "Esfenoides", "Cigomático", "Etmoides", "Parietal"],
   "El frontal forma la frente con su escama vertical y, con su porción orbitaria horizontal, el techo de las órbitas y el suelo de la fosa craneal anterior."))

T("sk-cb93516d",
  ("Which is the only bone of the skull that moves at a synovial joint?", ["Nasal bone", "Vomer", "Mandible", "Maxilla", "Zygomatic bone"],
   "The bones of the skull are firmly joined by sutures; the only movable joint is the temporomandibular joint between the mandible and the temporal bone."),
  ("Quel est le seul os du crâne mobile grâce à une articulation synoviale ?", ["Os nasal", "Vomer", "Mandibule", "Maxillaire", "Os zygomatique"],
   "Les os du crâne sont solidement unis par des sutures ; la seule articulation mobile est l'articulation temporo-mandibulaire entre la mandibule et l'os temporal."),
  ("Welcher ist der einzige Schädelknochen, der sich in einem echten Gelenk bewegt?", ["Nasenbein", "Vomer", "Unterkiefer", "Oberkiefer", "Jochbein"],
   "Die Schädelknochen sind durch Nähte fest verbunden; das einzige bewegliche Gelenk ist das Kiefergelenk zwischen Unterkiefer und Schläfenbein."),
  ("¿Cuál es el único hueso del cráneo que se mueve en una articulación sinovial?", ["Nasal", "Vómer", "Mandíbula", "Maxilar", "Cigomático"],
   "Los huesos del cráneo se unen firmemente por suturas; la única articulación móvil es la temporomandibular, entre la mandíbula y el temporal."))

T("sk-4559542c",
  ("What are the unossified membranous areas between the skull bones of a newborn called?", ["Fontanelles", "Sutures", "Fissures", "Sinuses", "Foramina"],
   "Fontanelles are membranous areas where the sutures meet; they allow the head to mould during birth and the brain to grow. The largest is the anterior fontanelle."),
  ("Comment appelle-t-on les zones membraneuses non ossifiées entre les os du crâne du nouveau-né ?", ["Fontanelles", "Sutures", "Fissures", "Sinus", "Foramens"],
   "Les fontanelles sont des zones membraneuses situées à la rencontre des sutures ; elles permettent le modelage de la tête à l'accouchement et la croissance du cerveau. La plus grande est la fontanelle antérieure."),
  ("Wie nennt man die nicht verknöcherten, häutigen Bereiche zwischen den Schädelknochen des Neugeborenen?", ["Fontanellen", "Nähte", "Fissuren", "Sinus", "Foramina"],
   "Fontanellen sind häutige Bereiche an den Treffpunkten der Nähte; sie ermöglichen die Verformung des Kopfes bei der Geburt und das Wachstum des Gehirns. Die größte ist die große (vordere) Fontanelle."),
  ("¿Cómo se llaman las zonas membranosas no osificadas entre los huesos del cráneo del recién nacido?", ["Fontanelas", "Suturas", "Fisuras", "Senos", "Agujeros"],
   "Las fontanelas son zonas membranosas donde se encuentran las suturas; permiten el moldeamiento de la cabeza en el parto y el crecimiento del cerebro. La mayor es la fontanela anterior."))

T("sk-f341b2fb",
  ("Between which bones is the sagittal suture?", ["Parietal and temporal", "Between the two halves of the frontal bone", "Between the two parietal bones", "Frontal and parietal", "Parietal and occipital"],
   "The sagittal suture joins the two parietal bones in the midline. The coronal suture lies between frontal and parietal bones, the lambdoid between parietal and occipital, the squamous between parietal and temporal."),
  ("Entre quels os se trouve la suture sagittale ?", ["Pariétal et temporal", "Entre les deux moitiés du frontal", "Entre les deux pariétaux", "Frontal et pariétal", "Pariétal et occipital"],
   "La suture sagittale unit les deux pariétaux sur la ligne médiane. La suture coronale est entre frontal et pariétaux, la lambdoïde entre pariétaux et occipital, la squameuse entre pariétal et temporal."),
  ("Zwischen welchen Knochen liegt die Pfeilnaht (Sutura sagittalis)?", ["Scheitelbein und Schläfenbein", "Zwischen den beiden Stirnbeinhälften", "Zwischen den beiden Scheitelbeinen", "Stirnbein und Scheitelbein", "Scheitelbein und Hinterhauptsbein"],
   "Die Pfeilnaht verbindet die beiden Scheitelbeine in der Mittellinie. Die Kranznaht liegt zwischen Stirn- und Scheitelbeinen, die Lambdanaht zwischen Scheitel- und Hinterhauptsbein, die Schuppennaht zwischen Scheitel- und Schläfenbein."),
  ("¿Entre qué huesos está la sutura sagital?", ["Parietal y temporal", "Entre las dos mitades del frontal", "Entre los dos parietales", "Frontal y parietal", "Parietal y occipital"],
   "La sutura sagital une los dos parietales en la línea media. La coronal está entre frontal y parietales, la lambdoidea entre parietales y occipital, y la escamosa entre parietal y temporal."))

T("sk-bb6020cc",
  ("How many bones take part in forming the orbit?", ["5", "8", "6", "9", "7"],
   "The orbit is formed by seven bones: frontal, zygomatic, maxilla, sphenoid, ethmoid, lacrimal and palatine."),
  ("Combien d'os participent à la formation de l'orbite ?", ["5", "8", "6", "9", "7"],
   "L'orbite est formée par sept os : frontal, zygomatique, maxillaire, sphénoïde, ethmoïde, lacrymal et palatin."),
  ("Wie viele Knochen sind am Aufbau der Orbita beteiligt?", ["5", "8", "6", "9", "7"],
   "Die Orbita wird von sieben Knochen gebildet: Stirnbein, Jochbein, Oberkiefer, Keilbein, Siebbein, Tränenbein und Gaumenbein."),
  ("¿Cuántos huesos participan en la formación de la órbita?", ["5", "8", "6", "9", "7"],
   "La órbita está formada por siete huesos: frontal, cigomático, maxilar, esfenoides, etmoides, lagrimal y palatino."))

T("sk-13d66ee5",
  ("How many cervical vertebrae are there in the vertebral column?", ["6", "12", "7", "5", "8"],
   "The vertebral column has 7 cervical, 12 thoracic, 5 lumbar, 5 sacral and 3–5 coccygeal vertebrae."),
  ("Combien de vertèbres cervicales compte la colonne vertébrale ?", ["6", "12", "7", "5", "8"],
   "La colonne compte 7 vertèbres cervicales, 12 thoraciques, 5 lombales, 5 sacrales et 3 à 5 coccygiennes."),
  ("Wie viele Halswirbel hat die Wirbelsäule?", ["6", "12", "7", "5", "8"],
   "Die Wirbelsäule hat 7 Hals-, 12 Brust-, 5 Lenden-, 5 Kreuzbein- und 3–5 Steißwirbel."),
  ("¿Cuántas vértebras cervicales tiene la columna vertebral?", ["6", "12", "7", "5", "8"],
   "La columna tiene 7 vértebras cervicales, 12 torácicas, 5 lumbares, 5 sacras y 3–5 coccígeas."))

T("sk-894f664c",
  ("What is the special name of the first cervical vertebra (C1)?", ["Vertebra prominens", "Atlas", "Promontory", "Axis", "Dens"],
   "C1 is called the atlas, C2 the axis and C7 the vertebra prominens. The atlas has no body and no spinous process."),
  ("Quel est le nom particulier de la première vertèbre cervicale (C1) ?", ["Vertèbre proéminente", "Atlas", "Promontoire", "Axis", "Dent"],
   "C1 s'appelle l'atlas, C2 l'axis et C7 la vertèbre proéminente. L'atlas n'a ni corps ni processus épineux."),
  ("Welchen besonderen Namen trägt der erste Halswirbel (C1)?", ["Vertebra prominens", "Atlas", "Promontorium", "Axis", "Dens"],
   "C1 heißt Atlas, C2 Axis und C7 Vertebra prominens. Der Atlas hat weder Körper noch Dornfortsatz."),
  ("¿Qué nombre especial recibe la primera vértebra cervical (C1)?", ["Vértebra prominente", "Atlas", "Promontorio", "Axis", "Odontoides"],
   "C1 se llama atlas, C2 axis y C7 vértebra prominente. El atlas no tiene cuerpo ni apófisis espinosa."))

T("sk-a8bb291d",
  ("How many vertebrae fuse to form the sacrum?", ["7", "12", "5", "3", "4"],
   "Five sacral vertebrae fuse to form the triangular sacrum; the 3–5 coccygeal vertebrae below form the coccyx."),
  ("Combien de vertèbres se soudent pour former le sacrum ?", ["7", "12", "5", "3", "4"],
   "Cinq vertèbres sacrales se soudent pour former le sacrum triangulaire ; les 3 à 5 vertèbres coccygiennes sous-jacentes forment le coccyx."),
  ("Aus wie vielen verschmolzenen Wirbeln besteht das Kreuzbein?", ["7", "12", "5", "3", "4"],
   "Fünf Kreuzbeinwirbel verschmelzen zum dreieckigen Kreuzbein; die 3–5 Steißwirbel darunter bilden das Steißbein."),
  ("¿Cuántas vértebras se fusionan para formar el sacro?", ["7", "12", "5", "3", "4"],
   "Cinco vértebras sacras se fusionan para formar el sacro triangular; las 3–5 vértebras coccígeas inferiores forman el cóccix."))

T("sk-d1d02687",
  ("Which curvature of the spine develops when a baby begins to hold up its head?", ["Sacral kyphosis", "Thoracic kyphosis", "Cervical lordosis", "Scoliosis", "Lumbar lordosis"],
   "In the fetus the spine is a single C-shaped curve (primary kyphosis). When the baby holds up its head the cervical lordosis develops, and with sitting and walking the lumbar lordosis (secondary curvatures)."),
  ("Quelle courbure du rachis apparaît quand le nourrisson commence à tenir sa tête ?", ["Cyphose sacrale", "Cyphose thoracique", "Lordose cervicale", "Scoliose", "Lordose lombale"],
   "Chez le fœtus, le rachis forme une seule courbe en C (cyphose primaire). Quand le nourrisson tient sa tête apparaît la lordose cervicale, puis avec la station assise et la marche la lordose lombale (courbures secondaires)."),
  ("Welche Wirbelsäulenkrümmung entsteht, wenn der Säugling beginnt, den Kopf zu halten?", ["Sakralkyphose", "Brustkyphose", "Halslordose", "Skoliose", "Lendenlordose"],
   "Beim Fetus bildet die Wirbelsäule eine einzige C-Krümmung (primäre Kyphose). Mit dem Kopfhalten entsteht die Halslordose, mit Sitzen und Laufen die Lendenlordose (sekundäre Krümmungen)."),
  ("¿Qué curvatura de la columna aparece cuando el bebé empieza a sostener la cabeza?", ["Cifosis sacra", "Cifosis torácica", "Lordosis cervical", "Escoliosis", "Lordosis lumbar"],
   "En el feto la columna forma una sola curva en C (cifosis primaria). Al sostener la cabeza aparece la lordosis cervical, y al sentarse y caminar la lordosis lumbar (curvaturas secundarias)."))

T("sk-b2c190ac",
  ("How many pairs of ribs are there in the thoracic cage?", ["12 pairs", "11 pairs", "13 pairs", "24 pairs", "10 pairs"],
   "Humans have 12 pairs (24) of ribs: 7 pairs of true, 3 pairs of false and 2 pairs of floating ribs."),
  ("Combien de paires de côtes compte la cage thoracique ?", ["12 paires", "11 paires", "13 paires", "24 paires", "10 paires"],
   "L'être humain possède 12 paires (24) de côtes : 7 paires de vraies côtes, 3 de fausses côtes et 2 de côtes flottantes."),
  ("Wie viele Rippenpaare hat der Brustkorb?", ["12 Paare", "11 Paare", "13 Paare", "24 Paare", "10 Paare"],
   "Der Mensch hat 12 Rippenpaare (24 Rippen): 7 Paar echte, 3 Paar falsche und 2 Paar freie Rippen."),
  ("¿Cuántos pares de costillas tiene la caja torácica?", ["12 pares", "11 pares", "13 pares", "24 pares", "10 pares"],
   "El ser humano tiene 12 pares (24) de costillas: 7 pares verdaderas, 3 falsas y 2 flotantes."))

T("sk-e3425c63",
  ("Which are the 'true ribs', joined directly to the sternum by their own cartilage?", ["Ribs 8–10", "Ribs 11–12", "Ribs 1–10", "Ribs 1–12", "Ribs 1–7"],
   "The true ribs are ribs 1–7. Ribs 8–10 join the cartilage above (false ribs), and the front ends of ribs 11–12 are free (floating ribs)."),
  ("Quelles sont les « vraies côtes », reliées directement au sternum par leur propre cartilage ?", ["Côtes 8–10", "Côtes 11–12", "Côtes 1–10", "Côtes 1–12", "Côtes 1–7"],
   "Les vraies côtes sont les côtes 1 à 7. Les côtes 8 à 10 rejoignent le cartilage sus-jacent (fausses côtes) et les côtes 11 et 12 ont une extrémité antérieure libre (côtes flottantes)."),
  ("Welche sind die „echten Rippen“, die mit eigenem Knorpel direkt am Sternum ansetzen?", ["8.–10. Rippe", "11.–12. Rippe", "1.–10. Rippe", "1.–12. Rippe", "1.–7. Rippe"],
   "Echte Rippen sind die 1.–7. Rippe. Die 8.–10. Rippe setzen am darüberliegenden Knorpel an (falsche Rippen), die Vorderenden der 11.–12. Rippe sind frei (freie Rippen)."),
  ("¿Cuáles son las «costillas verdaderas», unidas directamente al esternón por su propio cartílago?", ["Costillas 8.ª–10.ª", "Costillas 11.ª–12.ª", "Costillas 1.ª–10.ª", "Costillas 1.ª–12.ª", "Costillas 1.ª–7.ª"],
   "Las costillas verdaderas son de la 1.ª a la 7.ª. Las 8.ª–10.ª se unen al cartílago superior (falsas) y las 11.ª–12.ª tienen el extremo anterior libre (flotantes)."))
