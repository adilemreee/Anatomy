KIND = "questions"
SYSTEM = "skeletal"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("sk-cd7f4cd1",
  ("What are the three parts of the sternum?", ["Manubrium, angle and body", "Manubrium, body and costal cartilage", "Manubrium, body and xiphoid process", "Jugular notch, angle and xiphoid process", "Body, xiphoid process and jugular notch"],
   "From top to bottom the sternum consists of the manubrium, the body and the xiphoid process. The junction of manubrium and body is the sternal angle (level of the 2nd rib)."),
  ("Quelles sont les trois parties du sternum ?", ["Manubrium, angle et corps", "Manubrium, corps et cartilage costal", "Manubrium, corps et processus xiphoïde", "Incisure jugulaire, angle et processus xiphoïde", "Corps, processus xiphoïde et incisure jugulaire"],
   "De haut en bas, le sternum comprend le manubrium, le corps et le processus xiphoïde. La jonction manubrium–corps est l'angle sternal (niveau de la 2e côte)."),
  ("Welche drei Teile hat das Brustbein?", ["Manubrium, Angulus und Corpus", "Manubrium, Corpus und Rippenknorpel", "Manubrium, Corpus und Processus xiphoideus", "Incisura jugularis, Angulus und Processus xiphoideus", "Corpus, Processus xiphoideus und Incisura jugularis"],
   "Von oben nach unten besteht das Sternum aus Manubrium, Corpus und Processus xiphoideus. Die Verbindung von Manubrium und Corpus ist der Angulus sterni (Höhe der 2. Rippe)."),
  ("¿Cuáles son las tres partes del esternón?", ["Manubrio, ángulo y cuerpo", "Manubrio, cuerpo y cartílago costal", "Manubrio, cuerpo y apófisis xifoides", "Escotadura yugular, ángulo y apófisis xifoides", "Cuerpo, apófisis xifoides y escotadura yugular"],
   "De arriba abajo, el esternón consta de manubrio, cuerpo y apófisis xifoides. La unión de manubrio y cuerpo es el ángulo esternal (nivel de la 2.ª costilla)."))

T("sk-0a8d84f1",
  ("Which is the only bone of the arm?", ["Scapula", "Humerus", "Ulna", "Clavicle", "Radius"],
   "Only the humerus lies in the arm (brachium); the radius and ulna are in the forearm and the clavicle and scapula in the shoulder girdle."),
  ("Quel est le seul os du bras ?", ["Scapula", "Humérus", "Ulna", "Clavicule", "Radius"],
   "Seul l'humérus se trouve dans le bras ; le radius et l'ulna sont dans l'avant-bras, la clavicule et la scapula dans la ceinture scapulaire."),
  ("Welcher ist der einzige Knochen des Oberarms?", ["Scapula", "Humerus", "Ulna", "Klavikula", "Radius"],
   "Im Oberarm liegt nur der Humerus; Radius und Ulna liegen im Unterarm, Klavikula und Scapula im Schultergürtel."),
  ("¿Cuál es el único hueso del brazo?", ["Escápula", "Húmero", "Cúbito", "Clavícula", "Radio"],
   "En el brazo solo está el húmero; el radio y el cúbito están en el antebrazo, y la clavícula y la escápula en la cintura escapular."))

T("sk-b53d9bdb",
  ("Which bone lies on the thumb side of the forearm?", ["Scaphoid", "Humerus", "Ulna", "Fibula", "Radius"],
   "In the anatomical position the radius lies on the lateral (thumb) side of the forearm and the ulna on the medial (little finger) side."),
  ("Quel os se trouve du côté du pouce à l'avant-bras ?", ["Scaphoïde", "Humérus", "Ulna", "Fibula", "Radius"],
   "En position anatomique, le radius est du côté latéral (pouce) de l'avant-bras et l'ulna du côté médial (auriculaire)."),
  ("Welcher Knochen liegt an der Daumenseite des Unterarms?", ["Kahnbein", "Humerus", "Ulna", "Fibula", "Radius"],
   "In anatomischer Stellung liegt der Radius an der lateralen (Daumen-)Seite des Unterarms, die Ulna an der medialen (Kleinfinger-)Seite."),
  ("¿Qué hueso está en el lado del pulgar del antebrazo?", ["Escafoides", "Húmero", "Cúbito", "Peroné", "Radio"],
   "En posición anatómica el radio está en el lado lateral (del pulgar) del antebrazo y el cúbito en el medial (del meñique)."))

T("sk-02299d72",
  ("With which bone does the medial end of the clavicle articulate?", ["Sternum (manubrium)", "Body of the 1st rib", "C7 vertebra", "Humerus", "Scapula (acromion)"],
   "The medial end of the clavicle forms the sternoclavicular joint with the manubrium; the lateral end forms the acromioclavicular joint with the acromion."),
  ("Avec quel os s'articule l'extrémité médiale de la clavicule ?", ["Sternum (manubrium)", "Corps de la 1re côte", "Vertèbre C7", "Humérus", "Scapula (acromion)"],
   "L'extrémité médiale de la clavicule forme l'articulation sterno-claviculaire avec le manubrium ; l'extrémité latérale forme l'acromio-claviculaire avec l'acromion."),
  ("Mit welchem Knochen artikuliert das mediale Ende des Schlüsselbeins?", ["Sternum (Manubrium)", "Körper der 1. Rippe", "Wirbel C7", "Humerus", "Scapula (Akromion)"],
   "Das mediale Klavikulaende bildet mit dem Manubrium das Sternoklavikulargelenk, das laterale mit dem Akromion das Akromioklavikulargelenk."),
  ("¿Con qué hueso se articula el extremo medial de la clavícula?", ["Esternón (manubrio)", "Cuerpo de la 1.ª costilla", "Vértebra C7", "Húmero", "Escápula (acromion)"],
   "El extremo medial de la clavícula forma la articulación esternoclavicular con el manubrio; el lateral forma la acromioclavicular con el acromion."))

T("sk-dc65dbda",
  ("The acromion is part of which bone?", ["1st rib", "Scapula", "Sternum", "Humerus", "Clavicle"],
   "The acromion is the lateral end of the spine of the scapula; it forms the highest bony point of the shoulder and articulates with the clavicle."),
  ("L'acromion fait partie de quel os ?", ["1re côte", "Scapula", "Sternum", "Humérus", "Clavicule"],
   "L'acromion est l'extrémité latérale de l'épine de la scapula ; il forme le point osseux le plus haut de l'épaule et s'articule avec la clavicule."),
  ("Das Akromion ist Teil welches Knochens?", ["1. Rippe", "Scapula", "Sternum", "Humerus", "Klavikula"],
   "Das Akromion ist das laterale Ende der Spina scapulae; es bildet den höchsten Knochenpunkt der Schulter und artikuliert mit der Klavikula."),
  ("¿De qué hueso forma parte el acromion?", ["1.ª costilla", "Escápula", "Esternón", "Húmero", "Clavícula"],
   "El acromion es el extremo lateral de la espina de la escápula; forma el punto óseo más alto del hombro y se articula con la clavícula."))

T("sk-135626d7",
  ("In which hollow of the scapula does the head of the humerus sit at the shoulder joint?", ["Glenoid cavity", "Supraspinous fossa", "Subscapular fossa", "Olecranon fossa", "Acetabulum"],
   "The head of the humerus forms the shoulder (glenohumeral) joint with the glenoid cavity of the scapula; the socket is deepened by the glenoid labrum."),
  ("Dans quelle cavité de la scapula se loge la tête humérale dans l'articulation de l'épaule ?", ["Cavité glénoïdale", "Fosse supra-épineuse", "Fosse subscapulaire", "Fosse olécrânienne", "Acétabulum"],
   "La tête humérale forme l'articulation gléno-humérale avec la cavité glénoïdale de la scapula, approfondie par le labrum glénoïdal."),
  ("In welcher Vertiefung des Schulterblatts sitzt der Humeruskopf im Schultergelenk?", ["Cavitas glenoidalis", "Fossa supraspinata", "Fossa subscapularis", "Fossa olecrani", "Acetabulum"],
   "Der Humeruskopf bildet mit der Cavitas glenoidalis der Scapula das Schultergelenk; die Pfanne wird durch das Labrum glenoidale vertieft."),
  ("¿En qué cavidad de la escápula se aloja la cabeza del húmero en la articulación del hombro?", ["Cavidad glenoidea", "Fosa supraespinosa", "Fosa subescapular", "Fosa olecraniana", "Acetábulo"],
   "La cabeza del húmero forma la articulación glenohumeral con la cavidad glenoidea de la escápula, profundizada por el rodete glenoideo."))

T("sk-1a79acf4",
  ("The olecranon, felt at the back of the elbow, belongs to which bone?", ["Scapula", "Humerus", "Radius", "Pisiform", "Ulna"],
   "The olecranon is the projection at the proximal end of the ulna; with the elbow extended it enters the olecranon fossa of the humerus, and triceps brachii attaches to it."),
  ("L'olécrâne, palpable à l'arrière du coude, appartient à quel os ?", ["Scapula", "Humérus", "Radius", "Pisiforme", "Ulna"],
   "L'olécrâne est la saillie de l'extrémité proximale de l'ulna ; coude tendu, il pénètre dans la fosse olécrânienne de l'humérus, et le triceps brachial s'y insère."),
  ("Zu welchem Knochen gehört das am Ellenbogen hinten tastbare Olecranon?", ["Scapula", "Humerus", "Radius", "Erbsenbein", "Ulna"],
   "Das Olecranon ist der Vorsprung am proximalen Ende der Ulna; bei gestrecktem Ellenbogen greift es in die Fossa olecrani des Humerus, der M. triceps brachii setzt hier an."),
  ("¿A qué hueso pertenece el olécranon, palpable en la parte posterior del codo?", ["Escápula", "Húmero", "Radio", "Pisiforme", "Cúbito"],
   "El olécranon es la prominencia del extremo proximal del cúbito; con el codo extendido entra en la fosa olecraniana del húmero, y en él se inserta el tríceps braquial."))

T("sk-1924a576",
  ("How many carpal bones are there in the wrist?", ["7", "14", "5", "8", "10"],
   "The carpal bones are eight short bones in two rows: proximally scaphoid, lunate, triquetrum, pisiform; distally trapezium, trapezoid, capitate, hamate."),
  ("Combien d'os du carpe compte le poignet ?", ["7", "14", "5", "8", "10"],
   "Le carpe comprend huit os courts en deux rangées : en haut scaphoïde, lunatum, triquétrum, pisiforme ; en bas trapèze, trapézoïde, capitatum, hamatum."),
  ("Wie viele Handwurzelknochen gibt es?", ["7", "14", "5", "8", "10"],
   "Die Handwurzel besteht aus acht kurzen Knochen in zwei Reihen: proximal Kahnbein, Mondbein, Dreiecksbein, Erbsenbein; distal großes und kleines Vieleckbein, Kopfbein, Hakenbein."),
  ("¿Cuántos huesos del carpo hay en la muñeca?", ["7", "14", "5", "8", "10"],
   "El carpo tiene ocho huesos cortos en dos filas: proximal escafoides, semilunar, piramidal, pisiforme; distal trapecio, trapezoide, grande y ganchoso."))

T("sk-cc283b3f",
  ("How many phalanges does the thumb have?", ["1", "2", "3", "5", "4"],
   "The thumb has two phalanges (proximal and distal) and the other fingers three each; the hand has 14 phalanges in total."),
  ("Combien de phalanges possède le pouce ?", ["1", "2", "3", "5", "4"],
   "Le pouce a deux phalanges (proximale et distale), les autres doigts trois chacun ; la main compte 14 phalanges au total."),
  ("Wie viele Fingerglieder hat der Daumen?", ["1", "2", "3", "5", "4"],
   "Der Daumen hat zwei Glieder (Grund- und Endglied), die übrigen Finger je drei; die Hand hat insgesamt 14 Fingerglieder."),
  ("¿Cuántas falanges tiene el pulgar?", ["1", "2", "3", "5", "4"],
   "El pulgar tiene dos falanges (proximal y distal) y los demás dedos tres cada uno; la mano tiene 14 falanges en total."))

T("sk-766cdcb8",
  ("Which three bones form the hip bone?", ["Ischium, femur and pubis", "Ilium, sacrum and pubis", "Ilium, ischium and pubis", "Ilium, ischium and coccyx", "Sacrum, coccyx and pubis"],
   "The hip bone forms from the ilium, ischium and pubis fusing at the acetabulum; fusion is completed at puberty as the Y-shaped cartilage ossifies."),
  ("Quels sont les trois os qui forment l'os coxal ?", ["Ischium, fémur et pubis", "Ilium, sacrum et pubis", "Ilium, ischium et pubis", "Ilium, ischium et coccyx", "Sacrum, coccyx et pubis"],
   "L'os coxal résulte de la soudure de l'ilium, de l'ischium et du pubis dans l'acétabulum ; elle s'achève à la puberté avec l'ossification du cartilage en Y."),
  ("Welche drei Knochen bilden das Hüftbein?", ["Sitzbein, Femur und Schambein", "Darmbein, Kreuzbein und Schambein", "Darmbein, Sitzbein und Schambein", "Darmbein, Sitzbein und Steißbein", "Kreuzbein, Steißbein und Schambein"],
   "Das Hüftbein entsteht durch Verschmelzung von Darm-, Sitz- und Schambein in der Hüftpfanne; sie ist mit der Verknöcherung der Y-Fuge in der Pubertät abgeschlossen."),
  ("¿Qué tres huesos forman el coxal?", ["Isquion, fémur y pubis", "Ilion, sacro y pubis", "Ilion, isquion y pubis", "Ilion, isquion y cóccix", "Sacro, cóccix y pubis"],
   "El coxal se forma por la fusión del ilion, el isquion y el pubis en el acetábulo; la fusión termina en la pubertad al osificarse el cartílago en Y."))

T("sk-e8ec8422",
  ("Which bony prominence carries the body weight when sitting?", ["Anterior superior iliac spine", "Ischial tuberosity", "Greater trochanter", "Iliac crest", "Pubic tubercle"],
   "When sitting, weight rests on the ischial tuberosities. The hamstring muscles also arise from them."),
  ("Quelle saillie osseuse porte le poids du corps en position assise ?", ["Épine iliaque antéro-supérieure", "Tubérosité ischiatique", "Grand trochanter", "Crête iliaque", "Tubercule pubien"],
   "En position assise, le poids repose sur les tubérosités ischiatiques, d'où naissent aussi les ischio-jambiers."),
  ("Welcher Knochenvorsprung trägt im Sitzen das Körpergewicht?", ["Spina iliaca anterior superior", "Sitzbeinhöcker", "Trochanter major", "Beckenkamm", "Tuberculum pubicum"],
   "Im Sitzen ruht das Gewicht auf den Sitzbeinhöckern; dort entspringen auch die ischiokruralen Muskeln."),
  ("¿Qué prominencia ósea soporta el peso del cuerpo al sentarse?", ["Espina ilíaca anterosuperior", "Tuberosidad isquiática", "Trocánter mayor", "Cresta ilíaca", "Tubérculo del pubis"],
   "Al sentarse, el peso descansa sobre las tuberosidades isquiáticas, de donde también nacen los isquiotibiales."))

T("sk-fce811c8",
  ("Which thick, weight-bearing bone lies on the inner side of the leg?", ["Femur", "Fibula", "Talus", "Patella", "Tibia"],
   "The tibia (shinbone) is the thick bone on the inner side of the leg and carries most of the weight; the thin fibula on the outer side contributes little to weight-bearing."),
  ("Quel os épais, porteur du poids, se trouve du côté médial de la jambe ?", ["Fémur", "Fibula", "Talus", "Patella", "Tibia"],
   "Le tibia est l'os épais du côté médial de la jambe et porte l'essentiel du poids ; la fibula, mince et latérale, y contribue peu."),
  ("Welcher kräftige, gewichttragende Knochen liegt an der Innenseite des Unterschenkels?", ["Femur", "Fibula", "Talus", "Patella", "Tibia"],
   "Die Tibia (Schienbein) ist der kräftige Knochen an der Innenseite des Unterschenkels und trägt den größten Teil des Gewichts; die dünne Fibula außen trägt wenig."),
  ("¿Qué hueso grueso, que soporta el peso, está en el lado interno de la pierna?", ["Fémur", "Peroné", "Astrágalo", "Rótula", "Tibia"],
   "La tibia es el hueso grueso del lado interno de la pierna y soporta la mayor parte del peso; el peroné, delgado y lateral, contribuye poco."))

T("sk-3d64e2a3",
  ("Which is the kneecap bone?", ["Fabella", "Navicular", "Pisiform", "Talus", "Patella"],
   "The patella develops within the quadriceps femoris tendon and is the largest sesamoid bone of the body."),
  ("Quel est l'os de la rotule ?", ["Fabella", "Naviculaire", "Pisiforme", "Talus", "Patella"],
   "La patella se développe dans le tendon du quadriceps fémoral ; c'est le plus grand sésamoïde du corps."),
  ("Welcher Knochen ist die Kniescheibe?", ["Fabella", "Kahnbein", "Erbsenbein", "Talus", "Patella"],
   "Die Patella entsteht in der Sehne des M. quadriceps femoris und ist das größte Sesambein des Körpers."),
  ("¿Cuál es el hueso de la rodilla llamado rótula?", ["Fabela", "Navicular", "Pisiforme", "Astrágalo", "Rótula (patela)"],
   "La rótula se desarrolla dentro del tendón del cuádriceps femoral y es el mayor hueso sesamoideo del cuerpo."))

T("sk-51c47666",
  ("To which bone does the bony bump on the outer side of the ankle (lateral malleolus) belong?", ["Calcaneus", "Tibia (medial malleolus)", "Fibula (lateral malleolus)", "Cuboid", "Talus"],
   "The outer ankle bump is the lateral malleolus, the lower end of the fibula; the inner bump is the medial malleolus of the tibia. The lateral malleolus reaches lower than the medial."),
  ("À quel os appartient la saillie osseuse du bord externe de la cheville ?", ["Calcanéus", "Tibia (malléole médiale)", "Fibula (malléole latérale)", "Cuboïde", "Talus"],
   "La saillie externe est la malléole latérale, extrémité inférieure de la fibula ; la saillie interne est la malléole médiale du tibia. La malléole latérale descend plus bas."),
  ("Zu welchem Knochen gehört der Knochenvorsprung an der Außenseite des Sprunggelenks (Außenknöchel)?", ["Calcaneus", "Tibia (Innenknöchel)", "Fibula (Außenknöchel)", "Würfelbein", "Talus"],
   "Der Außenknöchel ist das untere Ende der Fibula, der Innenknöchel gehört zur Tibia. Der Außenknöchel reicht tiefer hinab als der Innenknöchel."),
  ("¿A qué hueso pertenece la prominencia ósea del lado externo del tobillo?", ["Calcáneo", "Tibia (maléolo medial)", "Peroné (maléolo lateral)", "Cuboides", "Astrágalo"],
   "La prominencia externa es el maléolo lateral, extremo inferior del peroné; la interna es el maléolo medial de la tibia. El maléolo lateral desciende más."))

T("sk-5b89ff5c",
  ("Which bone forms the heel?", ["Medial cuneiform", "Talus", "Calcaneus", "Cuboid", "Navicular"],
   "The calcaneus is the largest tarsal bone and forms the heel; the Achilles tendon attaches to its calcaneal tuberosity behind."),
  ("Quel os forme le talon ?", ["Cunéiforme médial", "Talus", "Calcanéus", "Cuboïde", "Naviculaire"],
   "Le calcanéus est le plus grand os du tarse et forme le talon ; le tendon d'Achille s'insère sur sa tubérosité postérieure."),
  ("Welcher Knochen bildet die Ferse?", ["Mediales Keilbein", "Talus", "Calcaneus", "Würfelbein", "Kahnbein"],
   "Der Calcaneus ist der größte Fußwurzelknochen und bildet die Ferse; die Achillessehne setzt hinten am Tuber calcanei an."),
  ("¿Qué hueso forma el talón?", ["Cuneiforme medial", "Astrágalo", "Calcáneo", "Cuboides", "Navicular"],
   "El calcáneo es el mayor hueso del tarso y forma el talón; el tendón de Aquiles se inserta en su tuberosidad posterior."))

T("sk-617628de",
  ("How many bones are there in each foot?", ["26", "28", "33", "24", "20"],
   "Each foot has 26 bones: 7 tarsals, 5 metatarsals and 14 phalanges (not counting sesamoids)."),
  ("Combien d'os compte chaque pied ?", ["26", "28", "33", "24", "20"],
   "Chaque pied compte 26 os : 7 os du tarse, 5 métatarsiens et 14 phalanges (sans les sésamoïdes)."),
  ("Wie viele Knochen hat ein Fuß?", ["26", "28", "33", "24", "20"],
   "Jeder Fuß hat 26 Knochen: 7 Fußwurzel-, 5 Mittelfußknochen und 14 Zehenglieder (ohne Sesambeine)."),
  ("¿Cuántos huesos tiene cada pie?", ["26", "28", "33", "24", "20"],
   "Cada pie tiene 26 huesos: 7 del tarso, 5 metatarsianos y 14 falanges (sin contar los sesamoideos)."))

T("sk-4ce46011",
  ("Which tarsal bone lies in front of the calcaneus on the outer border of the foot?", ["Lateral cuneiform", "Navicular", "5th metatarsal", "Cuboid", "Talus"],
   "The cuboid lies in front of the calcaneus on the outer border of the foot and articulates with the 4th–5th metatarsals; the navicular lies in front of the talus on the inner side."),
  ("Quel os du tarse se trouve en avant du calcanéus, au bord latéral du pied ?", ["Cunéiforme latéral", "Naviculaire", "5e métatarsien", "Cuboïde", "Talus"],
   "Le cuboïde est en avant du calcanéus au bord latéral du pied et s'articule avec les 4e et 5e métatarsiens ; le naviculaire est en avant du talus, du côté médial."),
  ("Welcher Fußwurzelknochen liegt vor dem Calcaneus am äußeren Fußrand?", ["Laterales Keilbein", "Kahnbein", "5. Mittelfußknochen", "Würfelbein", "Talus"],
   "Das Würfelbein liegt vor dem Calcaneus am äußeren Fußrand und artikuliert mit dem 4. und 5. Mittelfußknochen; das Kahnbein liegt vor dem Talus innen."),
  ("¿Qué hueso del tarso está delante del calcáneo, en el borde externo del pie?", ["Cuneiforme lateral", "Navicular", "5.º metatarsiano", "Cuboides", "Astrágalo"],
   "El cuboides está delante del calcáneo en el borde externo del pie y se articula con los metatarsianos 4.º y 5.º; el navicular está delante del astrágalo, en el lado interno."))

T("sk-62a44079",
  ("What is the basic structural unit of compact bone?", ["Periosteum", "Osteon (Haversian system)", "Lacuna", "Chondron", "Trabecula"],
   "Compact bone is built of osteons, lamellae arranged in rings around a central Haversian canal. Spongy bone is made of trabeculae."),
  ("Quelle est l'unité structurale de l'os compact ?", ["Périoste", "Ostéon (système de Havers)", "Lacune", "Chondrone", "Travée"],
   "L'os compact est formé d'ostéons, lamelles disposées en anneaux autour d'un canal de Havers central. L'os spongieux est formé de travées."),
  ("Was ist die Baueinheit der Kompakta?", ["Periost", "Osteon (Havers-System)", "Lakune", "Chondron", "Trabekel"],
   "Die Kompakta besteht aus Osteonen – ringförmig um einen zentralen Havers-Kanal angeordneten Lamellen. Die Spongiosa besteht aus Trabekeln."),
  ("¿Cuál es la unidad estructural del hueso compacto?", ["Periostio", "Osteona (sistema de Havers)", "Laguna", "Condrona", "Trabécula"],
   "El hueso compacto está formado por osteonas, láminas dispuestas en anillos alrededor de un conducto de Havers central. El hueso esponjoso está formado por trabéculas."))

T("sk-ef479b99",
  ("What are the collagen fibres that bind the periosteum firmly to bone and penetrate it called?", ["Elastic fibres", "Sharpey's fibres", "Volkmann's canals", "Haversian lamellae", "Reticular fibres"],
   "Sharpey's (perforating) fibres are thick collagen bundles passing from the periosteum into the bone matrix; they also anchor tendons and ligaments to bone."),
  ("Comment appelle-t-on les fibres de collagène qui fixent solidement le périoste à l'os en y pénétrant ?", ["Fibres élastiques", "Fibres de Sharpey", "Canaux de Volkmann", "Lamelles de Havers", "Fibres réticulées"],
   "Les fibres de Sharpey (perforantes) sont d'épais faisceaux de collagène qui passent du périoste dans la matrice osseuse ; elles ancrent aussi tendons et ligaments à l'os."),
  ("Wie heißen die Kollagenfasern, die das Periost fest im Knochen verankern?", ["Elastische Fasern", "Sharpey-Fasern", "Volkmann-Kanäle", "Havers-Lamellen", "Retikuläre Fasern"],
   "Sharpey-Fasern (perforierende Fasern) sind dicke Kollagenbündel, die vom Periost in die Knochenmatrix ziehen; sie verankern auch Sehnen und Bänder am Knochen."),
  ("¿Cómo se llaman las fibras de colágeno que fijan firmemente el periostio al hueso penetrando en él?", ["Fibras elásticas", "Fibras de Sharpey", "Conductos de Volkmann", "Laminillas de Havers", "Fibras reticulares"],
   "Las fibras de Sharpey (perforantes) son haces gruesos de colágeno que pasan del periostio a la matriz ósea; también anclan tendones y ligamentos al hueso."))

T("sk-545c3b65",
  ("By which process do the bones of the skull vault (calvaria) ossify?", ["Heterotopic ossification", "Endochondral ossification", "Intramembranous ossification", "Appositional cartilage growth", "Sesamoid ossification"],
   "The skull vault, the facial bones and most of the clavicle develop directly from mesenchyme by intramembranous ossification. The skull base, vertebrae and most limb bones ossify on a cartilage model (endochondral)."),
  ("Par quel mode s'ossifient les os de la voûte du crâne ?", ["Ossification hétérotopique", "Ossification enchondrale", "Ossification membranaire", "Croissance cartilagineuse appositionnelle", "Ossification sésamoïde"],
   "La voûte du crâne, les os de la face et la plus grande partie de la clavicule se forment directement à partir du mésenchyme par ossification membranaire. La base du crâne, les vertèbres et la plupart des os des membres s'ossifient sur un modèle cartilagineux (enchondrale)."),
  ("Wie verknöchern die Knochen des Schädeldachs (Calvaria)?", ["Heterotope Ossifikation", "Chondrale Ossifikation", "Desmale Ossifikation", "Appositionelles Knorpelwachstum", "Sesamoide Ossifikation"],
   "Schädeldach, Gesichtsknochen und der größte Teil der Klavikula entstehen direkt aus Mesenchym durch desmale Ossifikation. Schädelbasis, Wirbel und die meisten Extremitätenknochen verknöchern über ein Knorpelmodell (chondral)."),
  ("¿Cómo se osifican los huesos de la bóveda craneal (calvaria)?", ["Osificación heterotópica", "Osificación endocondral", "Osificación intramembranosa", "Crecimiento cartilaginoso por aposición", "Osificación sesamoidea"],
   "La bóveda craneal, los huesos de la cara y la mayor parte de la clavícula se forman directamente del mesénquima por osificación intramembranosa. La base del cráneo, las vértebras y la mayoría de los huesos de los miembros se osifican sobre un modelo cartilaginoso (endocondral)."))

T("sk-64644656",
  ("An X-ray of which region is most often used to assess bone age?", ["Left hand and wrist", "Knee", "Pelvis", "Skull", "Foot"],
   "Bone age is determined by comparing the appearance of the ossification centres and the state of the growth plates on an X-ray of the left hand and wrist with standard atlases (Greulich–Pyle)."),
  ("Quelle région radiographie-t-on le plus souvent pour déterminer l'âge osseux ?", ["Main et poignet gauches", "Genou", "Bassin", "Crâne", "Pied"],
   "L'âge osseux s'apprécie en comparant les noyaux d'ossification et l'état des cartilages de croissance d'une radiographie de la main et du poignet gauches à un atlas de référence (Greulich–Pyle)."),
  ("Eine Röntgenaufnahme welcher Region wird am häufigsten zur Bestimmung des Knochenalters verwendet?", ["Linke Hand und Handgelenk", "Knie", "Becken", "Schädel", "Fuß"],
   "Das Knochenalter wird bestimmt, indem man Ossifikationszentren und Wachstumsfugen auf einer Röntgenaufnahme der linken Hand mit Standardatlanten (Greulich–Pyle) vergleicht."),
  ("¿La radiografía de qué región se usa con más frecuencia para valorar la edad ósea?", ["Mano y muñeca izquierdas", "Rodilla", "Pelvis", "Cráneo", "Pie"],
   "La edad ósea se determina comparando los núcleos de osificación y el estado de las placas de crecimiento en una radiografía de la mano y la muñeca izquierdas con atlas de referencia (Greulich–Pyle)."))

T("sk-7f45caa6",
  ("In adults, where are bone marrow aspiration and biopsy most often performed?", ["Calcaneus", "Clavicle", "Femoral head", "Proximal tibia", "Posterior iliac crest (around the posterior superior iliac spine)"],
   "In adults the posterior iliac crest is preferred because it is both safe and rich in red marrow. The proximal tibia is used in small children."),
  ("Chez l'adulte, où réalise-t-on le plus souvent la ponction et la biopsie de moelle osseuse ?", ["Calcanéus", "Clavicule", "Tête fémorale", "Tibia proximal", "Crête iliaque postérieure (autour de l'épine iliaque postéro-supérieure)"],
   "Chez l'adulte, la crête iliaque postérieure est préférée car elle est sûre et riche en moelle rouge. Le tibia proximal est utilisé chez le petit enfant."),
  ("Wo werden Knochenmarkpunktion und -biopsie beim Erwachsenen am häufigsten durchgeführt?", ["Calcaneus", "Klavikula", "Femurkopf", "Proximale Tibia", "Hinterer Beckenkamm (um die Spina iliaca posterior superior)"],
   "Beim Erwachsenen wird der hintere Beckenkamm bevorzugt, da er sicher und reich an rotem Mark ist. Die proximale Tibia wird bei kleinen Kindern verwendet."),
  ("En el adulto, ¿dónde se realizan con más frecuencia el aspirado y la biopsia de médula ósea?", ["Calcáneo", "Clavícula", "Cabeza femoral", "Tibia proximal", "Cresta ilíaca posterior (alrededor de la espina ilíaca posterosuperior)"],
   "En el adulto se prefiere la cresta ilíaca posterior porque es segura y rica en médula roja. La tibia proximal se usa en niños pequeños."))
