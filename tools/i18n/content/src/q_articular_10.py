KIND = "questions"
SYSTEM = "articular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("ar-158c435d",
  ("In general, what do ligaments connect?", ["Nerves to bone", "Skin to bone", "Muscle to bone", "Bone to bone", "Muscle to muscle"],
   "Ligaments are bands of dense connective tissue joining bones together; they support the joint passively. The structure joining muscle to bone is a tendon."),
  ("De façon générale, que relient les ligaments ?", ["Les nerfs à l'os", "La peau à l'os", "Le muscle à l'os", "L'os à l'os", "Le muscle au muscle"],
   "Les ligaments sont des bandes de tissu conjonctif dense qui unissent les os et stabilisent passivement l'articulation. La structure qui relie le muscle à l'os est le tendon."),
  ("Was verbinden Bänder (Ligamente) im Allgemeinen?", ["Nerven mit Knochen", "Haut mit Knochen", "Muskel mit Knochen", "Knochen mit Knochen", "Muskel mit Muskel"],
   "Bänder sind straffe Bindegewebszüge, die Knochen miteinander verbinden und das Gelenk passiv sichern. Die Verbindung von Muskel und Knochen ist die Sehne."),
  ("En general, ¿qué unen los ligamentos?", ["Nervios con hueso", "Piel con hueso", "Músculo con hueso", "Hueso con hueso", "Músculo con músculo"],
   "Los ligamentos son bandas de tejido conjuntivo denso que unen los huesos entre sí y estabilizan pasivamente la articulación. La estructura que une el músculo al hueso es el tendón."))

T("ar-3d9b7532",
  ("What is the structure joining muscle to bone called?", ["Tendon", "Labrum", "Ligament", "Bursa", "Meniscus"],
   "Tendons transmit muscle force to bone. Bursae are sacs that help tendons glide over bone; menisci and labra are intra-articular fibrocartilaginous structures."),
  ("Comment appelle-t-on la structure qui relie le muscle à l'os ?", ["Tendon", "Labrum", "Ligament", "Bourse", "Ménisque"],
   "Les tendons transmettent la force du muscle à l'os. Les bourses facilitent le glissement des tendons sur l'os ; ménisques et labrums sont des structures fibrocartilagineuses intra-articulaires."),
  ("Wie heißt die Struktur, die Muskel und Knochen verbindet?", ["Sehne", "Labrum", "Band (Ligament)", "Schleimbeutel", "Meniskus"],
   "Sehnen übertragen die Muskelkraft auf den Knochen. Schleimbeutel erleichtern das Gleiten der Sehnen über den Knochen; Menisken und Labra sind faserknorpelige Strukturen im Gelenk."),
  ("¿Cómo se llama la estructura que une el músculo al hueso?", ["Tendón", "Rodete", "Ligamento", "Bolsa", "Menisco"],
   "Los tendones transmiten la fuerza del músculo al hueso. Las bolsas facilitan el deslizamiento de los tendones sobre el hueso; meniscos y rodetes son estructuras fibrocartilaginosas intraarticulares."))

T("ar-3fe924fa",
  ("What type of cartilage usually covers the articular surfaces of synovial joints?", ["Bone tissue", "Hyaline cartilage", "Elastic cartilage", "Fibrocartilage", "Dense connective tissue"],
   "In most synovial joints the articular surfaces are covered by smooth hyaline cartilage. In a few joints, such as the temporomandibular and sternoclavicular joints, they are covered by fibrocartilage."),
  ("Quel type de cartilage recouvre habituellement les surfaces des articulations synoviales ?", ["Tissu osseux", "Cartilage hyalin", "Cartilage élastique", "Fibrocartilage", "Tissu conjonctif dense"],
   "Dans la plupart des articulations synoviales, les surfaces sont recouvertes de cartilage hyalin lisse. Dans quelques-unes, comme la temporo-mandibulaire et la sterno-claviculaire, c'est du fibrocartilage."),
  ("Welche Knorpelart überzieht gewöhnlich die Gelenkflächen echter Gelenke?", ["Knochengewebe", "Hyaliner Knorpel", "Elastischer Knorpel", "Faserknorpel", "Straffes Bindegewebe"],
   "In den meisten echten Gelenken sind die Gelenkflächen von glattem hyalinem Knorpel überzogen. In wenigen, etwa Kiefer- und Sternoklavikulargelenk, ist es Faserknorpel."),
  ("¿Qué tipo de cartílago cubre habitualmente las superficies de las articulaciones sinoviales?", ["Tejido óseo", "Cartílago hialino", "Cartílago elástico", "Fibrocartílago", "Tejido conjuntivo denso"],
   "En la mayoría de las articulaciones sinoviales las superficies están cubiertas de cartílago hialino liso. En unas pocas, como la temporomandibular y la esternoclavicular, es fibrocartílago."))

T("ar-5deb5335",
  ("Which structure produces synovial fluid?", ["Joint ligaments", "Periosteum", "Synovial membrane", "Fibrous capsule", "Articular cartilage"],
   "The synovial membrane lining the inside of the joint capsule produces a slippery fluid rich in hyaluronic acid, which nourishes the cartilage and reduces friction."),
  ("Quelle structure produit le liquide synovial ?", ["Ligaments articulaires", "Périoste", "Membrane synoviale", "Capsule fibreuse", "Cartilage articulaire"],
   "La membrane synoviale qui tapisse l'intérieur de la capsule produit un liquide glissant riche en acide hyaluronique, qui nourrit le cartilage et réduit les frottements."),
  ("Welche Struktur bildet die Gelenkflüssigkeit?", ["Gelenkbänder", "Periost", "Synovialmembran", "Fibröse Kapsel", "Gelenkknorpel"],
   "Die Synovialmembran an der Innenseite der Kapsel bildet eine hyaluronsäurereiche Gleitflüssigkeit, die den Knorpel ernährt und die Reibung vermindert."),
  ("¿Qué estructura produce el líquido sinovial?", ["Ligamentos articulares", "Periostio", "Membrana sinovial", "Cápsula fibrosa", "Cartílago articular"],
   "La membrana sinovial que tapiza el interior de la cápsula produce un líquido resbaladizo rico en ácido hialurónico que nutre el cartílago y reduce el rozamiento."))

T("ar-968e75e8",
  ("What is the movement that decreases the angle between two bones (bending) called?", ["Abduction", "Extension", "Flexion", "Rotation", "Adduction"],
   "Flexion is bending and extension straightening (increasing the angle). Abduction moves away from the midline, adduction towards it, and rotation turns a part about its own axis."),
  ("Comment appelle-t-on le mouvement qui diminue l'angle entre deux os (plier) ?", ["Abduction", "Extension", "Flexion", "Rotation", "Adduction"],
   "La flexion plie, l'extension déplie (augmente l'angle). L'abduction éloigne de la ligne médiane, l'adduction en rapproche et la rotation fait tourner un segment autour de son axe."),
  ("Wie heißt die Bewegung, die den Winkel zwischen zwei Knochen verkleinert (Beugen)?", ["Abduktion", "Extension", "Flexion", "Rotation", "Adduktion"],
   "Flexion ist Beugen, Extension Strecken (Winkel wird größer). Abduktion entfernt von der Mittellinie, Adduktion führt zu ihr hin, Rotation dreht um die eigene Achse."),
  ("¿Cómo se llama el movimiento que reduce el ángulo entre dos huesos (doblar)?", ["Abducción", "Extensión", "Flexión", "Rotación", "Aducción"],
   "La flexión dobla y la extensión endereza (aumenta el ángulo). La abducción aleja de la línea media, la aducción acerca a ella y la rotación gira un segmento sobre su eje."))

T("ar-59af87db",
  ("What is the movement of raising the arm sideways away from the body called?", ["Flexion", "Circumduction", "Adduction", "Extension", "Abduction"],
   "Abduction is moving a limb away from the midline of the body; at the shoulder it is produced mainly by supraspinatus and deltoid."),
  ("Comment appelle-t-on le mouvement qui écarte le bras du tronc sur le côté ?", ["Flexion", "Circumduction", "Adduction", "Extension", "Abduction"],
   "L'abduction écarte un membre de la ligne médiane ; à l'épaule elle est réalisée surtout par le supra-épineux et le deltoïde."),
  ("Wie heißt das seitliche Abspreizen des Arms vom Rumpf?", ["Flexion", "Zirkumduktion", "Adduktion", "Extension", "Abduktion"],
   "Abduktion ist das Wegführen einer Gliedmaße von der Körpermittellinie; an der Schulter erfolgt sie vor allem durch M. supraspinatus und M. deltoideus."),
  ("¿Cómo se llama el movimiento de separar el brazo del tronco hacia un lado?", ["Flexión", "Circunducción", "Aducción", "Extensión", "Abducción"],
   "La abducción aleja un miembro de la línea media del cuerpo; en el hombro la realizan sobre todo el supraespinoso y el deltoides."))

T("ar-4d1f8034",
  ("What is the forearm movement that turns the palm upwards (forwards) called?", ["Eversion", "Pronation", "Supination", "Opposition", "Inversion"],
   "In supination the palm faces up/forwards, in pronation down/backwards; these movements take place at the radio-ulnar joints. Inversion and eversion are movements of the foot."),
  ("Comment appelle-t-on le mouvement de l'avant-bras qui tourne la paume vers le haut (vers l'avant) ?", ["Éversion", "Pronation", "Supination", "Opposition", "Inversion"],
   "En supination la paume regarde en haut/en avant, en pronation en bas/en arrière ; ces mouvements se font dans les articulations radio-ulnaires. Inversion et éversion concernent le pied."),
  ("Wie heißt die Unterarmbewegung, die die Handfläche nach oben (vorn) dreht?", ["Eversion", "Pronation", "Supination", "Opposition", "Inversion"],
   "Bei der Supination zeigt die Handfläche nach oben/vorn, bei der Pronation nach unten/hinten; diese Bewegungen erfolgen in den Radioulnargelenken. Inversion und Eversion sind Fußbewegungen."),
  ("¿Cómo se llama el movimiento del antebrazo que gira la palma hacia arriba (hacia delante)?", ["Eversión", "Pronación", "Supinación", "Oposición", "Inversión"],
   "En la supinación la palma mira arriba/adelante y en la pronación abajo/atrás; estos movimientos ocurren en las articulaciones radiocubitales. La inversión y la eversión son movimientos del pie."))

T("ar-d52f46c3",
  ("What is the movement that turns the sole of the foot inwards called?", ["Eversion", "Inversion", "Pronation", "Dorsiflexion", "Plantar flexion"],
   "In inversion the sole turns inwards, in eversion outwards. These movements take place mainly at the subtalar and transverse tarsal joints; most ankle sprains occur in inversion."),
  ("Comment appelle-t-on le mouvement qui tourne la plante du pied vers l'intérieur ?", ["Éversion", "Inversion", "Pronation", "Flexion dorsale", "Flexion plantaire"],
   "En inversion la plante regarde en dedans, en éversion en dehors. Ces mouvements se font surtout dans la sous-talienne et la transverse du tarse ; la plupart des entorses de cheville surviennent en inversion."),
  ("Wie heißt die Bewegung, bei der die Fußsohle nach innen gedreht wird?", ["Eversion", "Inversion", "Pronation", "Dorsalextension", "Plantarflexion"],
   "Bei der Inversion dreht die Sohle nach innen, bei der Eversion nach außen. Diese Bewegungen erfolgen vor allem im unteren Sprunggelenk und in der Chopart-Linie; die meisten Distorsionen geschehen in Inversion."),
  ("¿Cómo se llama el movimiento que gira la planta del pie hacia dentro?", ["Eversión", "Inversión", "Pronación", "Flexión dorsal", "Flexión plantar"],
   "En la inversión la planta mira hacia dentro y en la eversión hacia fuera. Estos movimientos ocurren sobre todo en la subastragalina y la transversa del tarso; la mayoría de los esguinces se producen en inversión."))

T("ar-3eb5fefe",
  ("Which is the most mobile joint of the body?", ["Hip joint", "Shoulder (glenohumeral) joint", "Knee joint", "Elbow joint", "Wrist joint"],
   "The shoulder trades stability for a wide range of movement: the humeral head contacts the shallow glenoid only partly. It is therefore the large joint that dislocates most often."),
  ("Quelle est l'articulation la plus mobile du corps ?", ["Hanche", "Épaule (gléno-humérale)", "Genou", "Coude", "Poignet"],
   "L'épaule sacrifie la stabilité à l'amplitude : la tête humérale n'est en contact que partiel avec la glène peu profonde. C'est donc la grosse articulation qui se luxe le plus souvent."),
  ("Welches ist das beweglichste Gelenk des Körpers?", ["Hüftgelenk", "Schultergelenk", "Kniegelenk", "Ellenbogengelenk", "Handgelenk"],
   "Die Schulter opfert Stabilität zugunsten der Beweglichkeit: der Humeruskopf berührt die flache Pfanne nur teilweise. Daher ist sie das am häufigsten luxierende große Gelenk."),
  ("¿Cuál es la articulación más móvil del cuerpo?", ["Cadera", "Hombro (glenohumeral)", "Rodilla", "Codo", "Muñeca"],
   "El hombro sacrifica estabilidad a cambio de amplitud: la cabeza humeral solo contacta parcialmente con la glena poco profunda. Por eso es la gran articulación que más se luxa."))

T("ar-f3f16261",
  ("Which is the largest joint of the body?", ["Knee joint", "Hip joint", "Sacroiliac joint", "Shoulder joint", "Ankle joint"],
   "The knee, formed by the femur, tibia and patella, is the largest and most complex synovial joint of the body."),
  ("Quelle est la plus grande articulation du corps ?", ["Genou", "Hanche", "Sacro-iliaque", "Épaule", "Cheville"],
   "Le genou, formé par le fémur, le tibia et la patella, est l'articulation synoviale la plus grande et la plus complexe du corps."),
  ("Welches ist das größte Gelenk des Körpers?", ["Kniegelenk", "Hüftgelenk", "Iliosakralgelenk", "Schultergelenk", "Sprunggelenk"],
   "Das Kniegelenk aus Femur, Tibia und Patella ist das größte und komplizierteste echte Gelenk des Körpers."),
  ("¿Cuál es la articulación más grande del cuerpo?", ["Rodilla", "Cadera", "Sacroilíaca", "Hombro", "Tobillo"],
   "La rodilla, formada por el fémur, la tibia y la rótula, es la articulación sinovial más grande y compleja del cuerpo."))

T("ar-809c1821",
  ("Which bones take part in the knee joint?", ["Femur, patella and calcaneus", "Femur, fibula and patella", "Tibia, fibula and talus", "Femur, tibia and fibula", "Femur, tibia and patella"],
   "The knee consists of the tibiofemoral and patellofemoral joints. The fibula does not take part in the knee joint; the superior tibiofibular joint is a separate joint."),
  ("Quels os participent à l'articulation du genou ?", ["Fémur, patella et calcanéus", "Fémur, fibula et patella", "Tibia, fibula et talus", "Fémur, tibia et fibula", "Fémur, tibia et patella"],
   "Le genou comprend les articulations fémoro-tibiale et fémoro-patellaire. La fibula ne participe pas au genou ; la tibio-fibulaire supérieure est une articulation distincte."),
  ("Welche Knochen bilden das Kniegelenk?", ["Femur, Patella und Calcaneus", "Femur, Fibula und Patella", "Tibia, Fibula und Talus", "Femur, Tibia und Fibula", "Femur, Tibia und Patella"],
   "Das Knie besteht aus Femorotibial- und Femoropatellargelenk. Die Fibula ist nicht am Kniegelenk beteiligt; das obere Tibiofibulargelenk ist ein eigenes Gelenk."),
  ("¿Qué huesos participan en la articulación de la rodilla?", ["Fémur, rótula y calcáneo", "Fémur, peroné y rótula", "Tibia, peroné y astrágalo", "Fémur, tibia y peroné", "Fémur, tibia y rótula"],
   "La rodilla consta de las articulaciones femorotibial y femoropatelar. El peroné no participa en la rodilla; la tibioperonea superior es una articulación aparte."))

T("ar-e4a2fa9a",
  ("Between which bones is the shoulder joint?", ["Clavicle and scapula", "Scapula and sternum", "Humerus and sternum", "Humerus and clavicle", "Humerus and scapula"],
   "The glenohumeral joint lies between the head of the humerus and the glenoid cavity of the scapula. The clavicle and scapula form the acromioclavicular joint."),
  ("Entre quels os se trouve l'articulation de l'épaule ?", ["Clavicule et scapula", "Scapula et sternum", "Humérus et sternum", "Humérus et clavicule", "Humérus et scapula"],
   "L'articulation gléno-humérale unit la tête humérale à la cavité glénoïdale de la scapula. La clavicule et la scapula forment l'acromio-claviculaire."),
  ("Zwischen welchen Knochen liegt das Schultergelenk?", ["Klavikula und Scapula", "Scapula und Sternum", "Humerus und Sternum", "Humerus und Klavikula", "Humerus und Scapula"],
   "Das Glenohumeralgelenk liegt zwischen Humeruskopf und Cavitas glenoidalis der Scapula. Klavikula und Scapula bilden das Akromioklavikulargelenk."),
  ("¿Entre qué huesos está la articulación del hombro?", ["Clavícula y escápula", "Escápula y esternón", "Húmero y esternón", "Húmero y clavícula", "Húmero y escápula"],
   "La articulación glenohumeral está entre la cabeza del húmero y la cavidad glenoidea de la escápula. La clavícula y la escápula forman la acromioclavicular."))

T("ar-aec5db37",
  ("What type of joint is the hip joint?", ["Saddle joint", "Hinge joint", "Ball-and-socket joint", "Pivot joint", "Plane joint"],
   "The hip joint is a ball-and-socket joint between the femoral head and the acetabulum; it moves in three axes and, thanks to its deep socket, is more stable than the shoulder."),
  ("De quel type est l'articulation de la hanche ?", ["En selle", "Charnière", "Sphéroïde (énarthrose)", "Trochoïde (pivot)", "Plane"],
   "La hanche est une articulation sphéroïde entre la tête fémorale et l'acétabulum ; elle se meut selon trois axes et, grâce à sa cavité profonde, est plus stable que l'épaule."),
  ("Welcher Gelenktyp ist das Hüftgelenk?", ["Sattelgelenk", "Scharniergelenk", "Kugelgelenk", "Zapfengelenk", "Planes Gelenk"],
   "Das Hüftgelenk ist ein Kugelgelenk zwischen Femurkopf und Hüftpfanne; es bewegt sich um drei Achsen und ist dank der tiefen Pfanne stabiler als die Schulter."),
  ("¿De qué tipo es la articulación de la cadera?", ["En silla de montar", "En bisagra", "Esferoidea (enartrosis)", "Trocoide (pivote)", "Plana"],
   "La cadera es una articulación esferoidea entre la cabeza femoral y el acetábulo; se mueve en tres ejes y, gracias a su cavidad profunda, es más estable que el hombro."))

T("ar-55d60eb1",
  ("Between which bones is the jaw (temporomandibular) joint?", ["Mandible and sphenoid", "Mandible and zygomatic bone", "Mandible and maxilla", "Mandible and temporal bone", "Maxilla and temporal bone"],
   "The temporomandibular joint lies between the condyle of the mandible and the mandibular fossa and articular tubercle of the temporal bone; it contains a fibrocartilaginous disc."),
  ("Entre quels os se trouve l'articulation de la mâchoire (temporo-mandibulaire) ?", ["Mandibule et sphénoïde", "Mandibule et os zygomatique", "Mandibule et maxillaire", "Mandibule et os temporal", "Maxillaire et os temporal"],
   "L'ATM unit le condyle de la mandibule à la fosse mandibulaire et au tubercule articulaire du temporal ; elle contient un disque fibrocartilagineux."),
  ("Zwischen welchen Knochen liegt das Kiefergelenk?", ["Unterkiefer und Keilbein", "Unterkiefer und Jochbein", "Unterkiefer und Oberkiefer", "Unterkiefer und Schläfenbein", "Oberkiefer und Schläfenbein"],
   "Das Kiefergelenk liegt zwischen dem Kondylus des Unterkiefers und Fossa mandibularis sowie Tuberculum articulare des Schläfenbeins; es enthält einen faserknorpeligen Diskus."),
  ("¿Entre qué huesos está la articulación de la mandíbula (temporomandibular)?", ["Mandíbula y esfenoides", "Mandíbula y cigomático", "Mandíbula y maxilar", "Mandíbula y temporal", "Maxilar y temporal"],
   "La ATM está entre el cóndilo mandibular y la fosa mandibular y el tubérculo articular del temporal; contiene un disco fibrocartilaginoso."))

T("ar-1c1cd56a",
  ("Between which bones is the pubic symphysis?", ["Sacrum and coccyx", "Sacrum and ilium", "Femur and pubis", "Right and left pubic bones", "Ischium and pubis"],
   "The pubic symphysis is the fibrocartilaginous joint joining the two pubic bones in the midline in front; the interpubic disc lies between them."),
  ("Entre quels os se trouve la symphyse pubienne ?", ["Sacrum et coccyx", "Sacrum et ilium", "Fémur et pubis", "Pubis droit et gauche", "Ischium et pubis"],
   "La symphyse pubienne est l'articulation fibrocartilagineuse qui unit en avant, sur la ligne médiane, les deux pubis ; le disque interpubien les sépare."),
  ("Zwischen welchen Knochen liegt die Schambeinfuge?", ["Kreuzbein und Steißbein", "Kreuzbein und Darmbein", "Femur und Schambein", "Rechtes und linkes Schambein", "Sitzbein und Schambein"],
   "Die Schambeinfuge ist die faserknorpelige Verbindung der beiden Schambeine vorn in der Mittellinie; dazwischen liegt der Discus interpubicus."),
  ("¿Entre qué huesos está la sínfisis del pubis?", ["Sacro y cóccix", "Sacro e ilion", "Fémur y pubis", "Pubis derecho e izquierdo", "Isquion y pubis"],
   "La sínfisis del pubis es la articulación fibrocartilaginosa que une por delante, en la línea media, los dos pubis; entre ellos está el disco interpúbico."))

T("ar-c9695c99",
  ("In which joint are the menisci found?", ["Shoulder joint", "Knee joint", "Ankle joint", "Hip joint", "Elbow joint"],
   "The medial and lateral menisci lie between the femoral and tibial condyles in the knee; they improve congruence and distribute load."),
  ("Dans quelle articulation trouve-t-on les ménisques ?", ["Épaule", "Genou", "Cheville", "Hanche", "Coude"],
   "Les ménisques médial et latéral se trouvent entre les condyles fémoraux et tibiaux ; ils améliorent la congruence et répartissent les charges."),
  ("In welchem Gelenk liegen die Menisken?", ["Schultergelenk", "Kniegelenk", "Sprunggelenk", "Hüftgelenk", "Ellenbogengelenk"],
   "Innen- und Außenmeniskus liegen im Knie zwischen Femur- und Tibiakondylen; sie verbessern die Kongruenz und verteilen die Last."),
  ("¿En qué articulación se encuentran los meniscos?", ["Hombro", "Rodilla", "Tobillo", "Cadera", "Codo"],
   "Los meniscos medial y lateral están entre los cóndilos femorales y tibiales de la rodilla; aumentan la congruencia y reparten la carga."))

T("ar-df324558",
  ("What is a bursa?", ["A small fluid-filled sac lined by synovial membrane between structures that rub together", "A fibrocartilaginous disc inside a joint", "The outer layer of articular cartilage", "The membrane covering bone", "A band joining muscle to bone"],
   "Bursae reduce friction between structures that rub against each other, such as tendon and bone or skin and bone. Their inflammation from repeated pressure or friction is called bursitis."),
  ("Qu'est-ce qu'une bourse séreuse ?", ["Un petit sac rempli de liquide, tapissé de synoviale, entre des structures qui frottent", "Un disque fibrocartilagineux intra-articulaire", "La couche externe du cartilage articulaire", "La membrane qui recouvre l'os", "Une bande reliant le muscle à l'os"],
   "Les bourses réduisent les frottements entre structures qui glissent l'une sur l'autre, comme tendon et os ou peau et os. Leur inflammation par pression ou frottement répétés est une bursite."),
  ("Was ist ein Schleimbeutel (Bursa)?", ["Ein kleiner, mit Synovialis ausgekleideter Flüssigkeitssack zwischen aneinander reibenden Strukturen", "Ein faserknorpeliger Diskus im Gelenk", "Die äußere Schicht des Gelenkknorpels", "Die Haut, die den Knochen überzieht", "Ein Strang, der Muskel und Knochen verbindet"],
   "Schleimbeutel verringern die Reibung zwischen aneinander gleitenden Strukturen, etwa Sehne und Knochen oder Haut und Knochen. Ihre Entzündung durch wiederholten Druck oder Reibung heißt Bursitis."),
  ("¿Qué es una bolsa sinovial?", ["Un pequeño saco lleno de líquido, tapizado de sinovial, entre estructuras que rozan", "Un disco fibrocartilaginoso intraarticular", "La capa externa del cartílago articular", "La membrana que cubre el hueso", "Una banda que une el músculo al hueso"],
   "Las bolsas reducen el rozamiento entre estructuras que se deslizan entre sí, como tendón y hueso o piel y hueso. Su inflamación por presión o roce repetidos se llama bursitis."))

T("ar-0716071b",
  ("How is articular cartilage nourished?", ["By perichondrial vessels", "By its own blood vessels", "By periosteal vessels", "By capillaries from the bone marrow", "By diffusion from the synovial fluid"],
   "Articular cartilage has no vessels, nerves or perichondrium; nutrients come by diffusion from the synovial fluid. That is why cartilage damage does not heal on its own."),
  ("Comment le cartilage articulaire est-il nourri ?", ["Par les vaisseaux du périchondre", "Par ses propres vaisseaux", "Par les vaisseaux du périoste", "Par des capillaires venus de la moelle", "Par diffusion à partir du liquide synovial"],
   "Le cartilage articulaire n'a ni vaisseaux, ni nerfs, ni périchondre ; il est nourri par diffusion à partir du liquide synovial. C'est pourquoi ses lésions ne cicatrisent pas spontanément."),
  ("Wie wird der Gelenkknorpel ernährt?", ["Über Gefäße des Perichondriums", "Über eigene Blutgefäße", "Über Periostgefäße", "Über Kapillaren aus dem Knochenmark", "Durch Diffusion aus der Gelenkflüssigkeit"],
   "Gelenkknorpel hat weder Gefäße, Nerven noch Perichondrium; er wird durch Diffusion aus der Gelenkflüssigkeit ernährt. Deshalb heilen Knorpelschäden nicht von selbst."),
  ("¿Cómo se nutre el cartílago articular?", ["Por los vasos del pericondrio", "Por sus propios vasos", "Por los vasos del periostio", "Por capilares de la médula ósea", "Por difusión desde el líquido sinovial"],
   "El cartílago articular no tiene vasos, nervios ni pericondrio; se nutre por difusión desde el líquido sinovial. Por eso sus lesiones no cicatrizan por sí solas."))

T("ar-7804f95c",
  ("In rheumatoid arthritis, what is the inflammatory tissue that erodes articular cartilage and bone called?", ["Callus", "Tophus", "Ganglion", "Osteophyte", "Pannus"],
   "Rheumatoid arthritis is chronic inflammation of the synovial membrane; the thickened synovium, called pannus, erodes cartilage and bone. Osteophytes are a sign of osteoarthritis, tophi of gout."),
  ("Dans la polyarthrite rhumatoïde, comment appelle-t-on le tissu inflammatoire qui érode le cartilage et l'os ?", ["Cal", "Tophus", "Kyste synovial", "Ostéophyte", "Pannus"],
   "La polyarthrite rhumatoïde est une inflammation chronique de la synoviale ; la synoviale épaissie, appelée pannus, érode cartilage et os. Les ostéophytes signent l'arthrose, les tophus la goutte."),
  ("Wie heißt bei rheumatoider Arthritis das entzündliche Gewebe, das Knorpel und Knochen zerstört?", ["Kallus", "Tophus", "Ganglion", "Osteophyt", "Pannus"],
   "Die rheumatoide Arthritis ist eine chronische Synovialitis; die verdickte Synovialis, der Pannus, zerstört Knorpel und Knochen. Osteophyten sind ein Zeichen der Arthrose, Tophi der Gicht."),
  ("En la artritis reumatoide, ¿cómo se llama el tejido inflamatorio que erosiona el cartílago y el hueso?", ["Callo", "Tofo", "Ganglión", "Osteofito", "Pannus"],
   "La artritis reumatoide es una inflamación crónica de la sinovial; la sinovial engrosada, llamada pannus, erosiona el cartílago y el hueso. Los osteofitos son signo de artrosis y los tofos de gota."))

T("ar-a742a27f",
  ("In people who work kneeling, swelling in front of the kneecap is a bursitis of which bursa?", ["Semimembranosus bursa", "Deep infrapatellar bursa", "Suprapatellar bursa", "Prepatellar bursa", "Anserine bursa"],
   "Prepatellar bursitis ('housemaid's knee') is inflammation of the bursa between the patella and the skin from repeated pressure. Infrapatellar bursitis ('clergyman's knee') lies in front of the tibial tuberosity."),
  ("Chez les personnes qui travaillent à genoux, le gonflement devant la rotule est une bursite de quelle bourse ?", ["Bourse du semi-membraneux", "Bourse infrapatellaire profonde", "Bourse suprapatellaire", "Bourse prépatellaire", "Bourse ansérine"],
   "L'hygroma prérotulien est l'inflammation de la bourse située entre la patella et la peau, due à des pressions répétées. La bursite infrapatellaire se situe en avant de la tubérosité tibiale."),
  ("Bei Menschen, die kniend arbeiten, ist eine Schwellung vor der Kniescheibe eine Bursitis welches Schleimbeutels?", ["Bursa m. semimembranosi", "Bursa infrapatellaris profunda", "Bursa suprapatellaris", "Bursa praepatellaris", "Bursa anserina"],
   "Die Bursitis praepatellaris („Fliesenlegerknie“) ist eine Entzündung des Schleimbeutels zwischen Patella und Haut durch wiederholten Druck. Die Bursitis infrapatellaris liegt vor der Tuberositas tibiae."),
  ("En personas que trabajan de rodillas, la hinchazón delante de la rótula es una bursitis de ¿qué bolsa?", ["Bolsa del semimembranoso", "Bolsa infrarrotuliana profunda", "Bolsa suprarrotuliana", "Bolsa prerrotuliana", "Bolsa anserina"],
   "La bursitis prerrotuliana («rodilla de beata») es la inflamación de la bolsa entre la rótula y la piel por presión repetida. La infrarrotuliana está delante de la tuberosidad tibial."))

T("ar-4202eeca",
  ("What is the main function of the alar ligaments?", ["To prevent excessive flexion of the head", "To press the dens against the anterior arch of the atlas", "To limit excessive rotation of the head", "To join the posterior arch of the atlas to the occiput", "To form the anterior wall of the vertebral canal"],
   "The alar ligaments run from the sides of the dens to the occipital condyles and prevent excessive turning of the head at the atlanto-axial joint. The ligament pressing the dens against the anterior arch is the transverse ligament of the atlas."),
  ("Quelle est la fonction principale des ligaments alaires ?", ["Empêcher la flexion excessive de la tête", "Plaquer la dent contre l'arc antérieur de l'atlas", "Limiter la rotation excessive de la tête", "Unir l'arc postérieur de l'atlas à l'occipital", "Former la paroi antérieure du canal vertébral"],
   "Les ligaments alaires vont des côtés de la dent aux condyles occipitaux et empêchent la rotation excessive de la tête dans l'atlanto-axiale. Le ligament qui plaque la dent contre l'arc antérieur est le ligament transverse de l'atlas."),
  ("Was ist die Hauptfunktion der Ligg. alaria?", ["Übermäßige Kopfbeugung verhindern", "Den Dens an den vorderen Atlasbogen drücken", "Übermäßige Kopfdrehung begrenzen", "Den hinteren Atlasbogen mit dem Hinterhaupt verbinden", "Die Vorderwand des Wirbelkanals bilden"],
   "Die Ligg. alaria ziehen von den Seiten des Dens zu den Hinterhauptskondylen und verhindern eine übermäßige Kopfdrehung im Atlantoaxialgelenk. Den Dens drückt das Lig. transversum atlantis an den vorderen Bogen."),
  ("¿Cuál es la función principal de los ligamentos alares?", ["Impedir la flexión excesiva de la cabeza", "Apretar la odontoides contra el arco anterior del atlas", "Limitar la rotación excesiva de la cabeza", "Unir el arco posterior del atlas al occipital", "Formar la pared anterior del conducto vertebral"],
   "Los ligamentos alares van de los lados de la odontoides a los cóndilos occipitales e impiden la rotación excesiva de la cabeza en la atlantoaxial. El que aprieta la odontoides contra el arco anterior es el ligamento transverso del atlas."))

T("ar-4ecc76c5",
  ("Why is rotation of the spine limited in the lumbar region?", ["Because of the ribs", "Because the facet joint surfaces lie in the sagittal plane", "Because the discs are very thin", "Because the spines are short", "Because there is no ligamentum flavum"],
   "The orientation of the facet joints determines the type of movement in each region: lumbar facets are sagittal and allow flexion-extension but restrict rotation; thoracic facets lie in the frontal plane and rotation is free."),
  ("Pourquoi la rotation du rachis est-elle limitée à l'étage lombal ?", ["À cause des côtes", "Parce que les surfaces des articulations zygapophysaires sont sagittales", "Parce que les disques sont très minces", "Parce que les épineuses sont courtes", "Parce qu'il n'y a pas de ligament jaune"],
   "L'orientation des articulations zygapophysaires détermine le mouvement de chaque étage : les facettes lombales sont sagittales et permettent la flexion-extension mais limitent la rotation ; les thoraciques sont frontales et la rotation y est libre."),
  ("Warum ist die Rotation der Wirbelsäule im Lendenbereich eingeschränkt?", ["Wegen der Rippen", "Weil die Facettengelenkflächen sagittal stehen", "Weil die Bandscheiben sehr dünn sind", "Weil die Dornfortsätze kurz sind", "Weil das Lig. flavum fehlt"],
   "Die Ausrichtung der Facettengelenke bestimmt die Bewegungsart: lumbale Facetten stehen sagittal und erlauben Beugung-Streckung, schränken aber die Rotation ein; thorakale stehen frontal, dort ist Rotation frei."),
  ("¿Por qué está limitada la rotación de la columna en la región lumbar?", ["Por las costillas", "Porque las carillas facetarias están en el plano sagital", "Porque los discos son muy delgados", "Porque las espinosas son cortas", "Porque no hay ligamento amarillo"],
   "La orientación de las facetas determina el tipo de movimiento: las lumbares son sagitales y permiten la flexoextensión pero limitan la rotación; las torácicas están en el plano frontal y la rotación es libre."))

T("ar-0ab30723",
  ("In which vertebrae are the uncovertebral (Luschka) joints found?", ["Cervical vertebrae C3–C7", "Thoracic vertebrae T1–T12", "Between atlas and axis", "Lumbar vertebrae L1–L5", "Between the sacral vertebrae"],
   "Uncovertebral joints are cleft-like joints between the uncinate processes on the upper lateral margins of the C3–C7 bodies and the vertebra above; their osteophytes can narrow the intervertebral foramen."),
  ("Dans quelles vertèbres trouve-t-on les articulations unco-vertébrales (de Luschka) ?", ["Vertèbres cervicales C3–C7", "Vertèbres thoraciques T1–T12", "Entre atlas et axis", "Vertèbres lombales L1–L5", "Entre les vertèbres sacrales"],
   "Les unco-vertébrales sont des fentes articulaires entre les processus unciformes du bord latéral supérieur des corps de C3 à C7 et la vertèbre sus-jacente ; leurs ostéophytes peuvent rétrécir le foramen intervertébral."),
  ("An welchen Wirbeln finden sich die Unkovertebralgelenke (Luschka)?", ["Halswirbel C3–C7", "Brustwirbel T1–T12", "Zwischen Atlas und Axis", "Lendenwirbel L1–L5", "Zwischen den Kreuzbeinwirbeln"],
   "Unkovertebralgelenke sind spaltförmige Gelenke zwischen den Processus uncinati am oberen Seitenrand der Wirbelkörper C3–C7 und dem darüberliegenden Wirbel; ihre Osteophyten können das Foramen intervertebrale einengen."),
  ("¿En qué vértebras se encuentran las articulaciones uncovertebrales (de Luschka)?", ["Vértebras cervicales C3–C7", "Vértebras torácicas T1–T12", "Entre atlas y axis", "Vértebras lumbares L1–L5", "Entre las vértebras sacras"],
   "Las uncovertebrales son hendiduras articulares entre las apófisis unciformes del borde lateral superior de los cuerpos de C3–C7 y la vértebra superior; sus osteofitos pueden estrechar el agujero intervertebral."))

T("ar-ff6c7a3d",
  ("Which ligament prevents backward displacement of the condyle at the jaw joint?", ["Lateral (temporomandibular) ligament", "Pterygospinous ligament", "Stylomandibular ligament", "Sphenomandibular ligament", "Stylohyoid ligament"],
   "The lateral ligament is a thickening of the outer side of the capsule; it runs from the zygomatic arch to the neck of the mandible and prevents the condyle from moving backwards and downwards. The spheno- and stylomandibular ligaments are accessory ligaments away from the capsule."),
  ("Quel ligament empêche le recul du condyle dans l'articulation temporo-mandibulaire ?", ["Ligament latéral (temporo-mandibulaire)", "Ligament ptérygo-épineux", "Ligament stylo-mandibulaire", "Ligament sphéno-mandibulaire", "Ligament stylo-hyoïdien"],
   "Le ligament latéral est un épaississement de la face externe de la capsule ; il va de l'arcade zygomatique au col de la mandibule et empêche le condyle de reculer et de descendre. Les ligaments sphéno- et stylo-mandibulaires sont des ligaments accessoires à distance."),
  ("Welches Band verhindert das Zurückweichen des Kondylus im Kiefergelenk?", ["Lig. laterale (temporomandibulare)", "Lig. pterygospinale", "Lig. stylomandibulare", "Lig. sphenomandibulare", "Lig. stylohyoideum"],
   "Das Lig. laterale ist eine Verstärkung der Kapselaußenseite vom Jochbogen zum Unterkieferhals und verhindert, dass der Kondylus nach hinten unten weicht. Lig. sphenomandibulare und stylomandibulare sind kapselferne Hilfsbänder."),
  ("¿Qué ligamento impide el desplazamiento posterior del cóndilo en la ATM?", ["Ligamento lateral (temporomandibular)", "Ligamento pterigoespinoso", "Ligamento estilomandibular", "Ligamento esfenomandibular", "Ligamento estilohioideo"],
   "El ligamento lateral es un engrosamiento de la cara externa de la cápsula; va del arco cigomático al cuello de la mandíbula e impide que el cóndilo se desplace atrás y abajo. Los esfeno- y estilomandibulares son ligamentos accesorios alejados de la cápsula."))
