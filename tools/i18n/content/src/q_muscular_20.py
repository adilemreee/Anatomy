KIND = "questions"
SYSTEM = "muscular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("mu-dc79ab25",
  ("Which nerve supplies the muscles of facial expression?", ["Trigeminal nerve (V)", "Oculomotor nerve (III)", "Accessory nerve (XI)", "Hypoglossal nerve (XII)", "Facial nerve (VII)"],
   "All muscles of facial expression develop from the 2nd pharyngeal arch and are supplied by the facial nerve. The muscles of mastication come from the 1st arch and are supplied by the mandibular nerve (V3)."),
  ("Quel nerf innerve les muscles de la mimique (peauciers) ?", ["Nerf trijumeau (V)", "Nerf oculomoteur (III)", "Nerf accessoire (XI)", "Nerf hypoglosse (XII)", "Nerf facial (VII)"],
   "Tous les muscles de la mimique dérivent du 2e arc pharyngien et sont innervés par le nerf facial. Les muscles masticateurs viennent du 1er arc et sont innervés par le nerf mandibulaire (V3)."),
  ("Welcher Nerv innerviert die mimische Muskulatur?", ["N. trigeminus (V)", "N. oculomotorius (III)", "N. accessorius (XI)", "N. hypoglossus (XII)", "N. facialis (VII)"],
   "Alle mimischen Muskeln entstehen aus dem 2. Schlundbogen und werden vom N. facialis innerviert. Die Kaumuskeln stammen aus dem 1. Bogen und werden vom N. mandibularis (V3) versorgt."),
  ("¿Qué nervio inerva los músculos de la expresión facial?", ["Nervio trigémino (V)", "Nervio oculomotor (III)", "Nervio accesorio (XI)", "Nervio hipogloso (XII)", "Nervio facial (VII)"],
   "Todos los músculos de la expresión facial derivan del 2.º arco faríngeo y los inerva el facial. Los masticadores proceden del 1.er arco y los inerva el nervio mandibular (V3)."))

T("mu-bfc1e2e0",
  ("Which nerve supplies the muscles of mastication?", ["Glossopharyngeal nerve", "Facial nerve", "Maxillary nerve (V2)", "Hypoglossal nerve", "Mandibular nerve (V3)"],
   "Masseter, temporalis, medial and lateral pterygoid develop from the 1st pharyngeal arch and are supplied by the mandibular division of the trigeminal nerve."),
  ("Quel nerf innerve les muscles masticateurs ?", ["Nerf glosso-pharyngien", "Nerf facial", "Nerf maxillaire (V2)", "Nerf hypoglosse", "Nerf mandibulaire (V3)"],
   "Le masséter, le temporal et les ptérygoïdiens médial et latéral dérivent du 1er arc pharyngien et sont innervés par la branche mandibulaire du trijumeau."),
  ("Welcher Nerv innerviert die Kaumuskeln?", ["N. glossopharyngeus", "N. facialis", "N. maxillaris (V2)", "N. hypoglossus", "N. mandibularis (V3)"],
   "M. masseter, M. temporalis, M. pterygoideus medialis und lateralis entstehen aus dem 1. Schlundbogen und werden vom mandibulären Ast des N. trigeminus innerviert."),
  ("¿Qué nervio inerva los músculos masticadores?", ["Nervio glosofaríngeo", "Nervio facial", "Nervio maxilar (V2)", "Nervio hipogloso", "Nervio mandibular (V3)"],
   "El masetero, el temporal y los pterigoideos medial y lateral derivan del 1.er arco faríngeo y los inerva la rama mandibular del trigémino."))

T("mu-5756c484",
  ("Which muscle of mastication can be felt hardening in the cheek when the teeth are clenched?", ["Medial pterygoid", "Masseter", "Zygomaticus major", "Buccinator", "Temporalis"],
   "Masseter runs from the zygomatic arch to the outer surface of the mandibular ramus; it is one of the strongest jaw-closing muscles and is easily felt in the cheek when the teeth are clenched."),
  ("Quel muscle masticateur se durcit sous les doigts dans la joue quand on serre les dents ?", ["Muscle ptérygoïdien médial", "Muscle masséter", "Muscle grand zygomatique", "Muscle buccinateur", "Muscle temporal"],
   "Le masséter va de l'arcade zygomatique à la face externe de la branche mandibulaire ; c'est l'un des plus puissants élévateurs de la mandibule et on le sent facilement dans la joue en serrant les dents."),
  ("Welcher Kaumuskel wird beim Zusammenbeißen der Zähne in der Wange tastbar hart?", ["M. pterygoideus medialis", "M. masseter", "M. zygomaticus major", "M. buccinator", "M. temporalis"],
   "Der M. masseter zieht vom Jochbogen zur Außenfläche des Unterkieferasts; er gehört zu den stärksten Kieferschließern und ist beim Zusammenbeißen in der Wange gut tastbar."),
  ("¿Qué músculo masticador se endurece en la mejilla al apretar los dientes?", ["Músculo pterigoideo medial", "Músculo masetero", "Músculo cigomático mayor", "Músculo buccinador", "Músculo temporal"],
   "El masetero va del arco cigomático a la cara externa de la rama mandibular; es uno de los más potentes cerradores de la mandíbula y se palpa fácilmente en la mejilla al apretar los dientes."))

T("mu-77190f39",
  ("Which fan-shaped muscle of mastication lies in the temple region?", ["Superior auricular muscle", "Occipitofrontalis", "Temporalis", "Lateral pterygoid", "Masseter"],
   "Temporalis is the fan-shaped muscle filling the temporal fossa; its fibres converge on the coronoid process; it closes the jaw and its posterior fibres retract it."),
  ("Quel muscle masticateur en éventail occupe la région de la tempe ?", ["Muscle auriculaire supérieur", "Muscle occipito-frontal", "Muscle temporal", "Muscle ptérygoïdien latéral", "Muscle masséter"],
   "Le temporal est le muscle en éventail qui remplit la fosse temporale ; ses fibres convergent vers le processus coronoïde ; il élève la mandibule et ses fibres postérieures la rétropulsent."),
  ("Welcher fächerförmige Kaumuskel liegt in der Schläfenregion?", ["M. auricularis superior", "M. occipitofrontalis", "M. temporalis", "M. pterygoideus lateralis", "M. masseter"],
   "Der M. temporalis füllt fächerförmig die Fossa temporalis; seine Fasern konvergieren zum Processus coronoideus; er schließt den Kiefer, seine hinteren Fasern ziehen ihn zurück."),
  ("¿Qué músculo masticador en abanico ocupa la región de la sien?", ["Músculo auricular superior", "Músculo occipitofrontal", "Músculo temporal", "Músculo pterigoideo lateral", "Músculo masetero"],
   "El temporal es el músculo en abanico que llena la fosa temporal; sus fibras convergen en la apófisis coronoides; cierra la mandíbula y sus fibras posteriores la retraen."))

T("mu-9fd66965",
  ("Which muscle purses the lips (whistling, kissing)?", ["Zygomaticus major", "Mentalis", "Orbicularis oris", "Buccinator", "Depressor anguli oris"],
   "Orbicularis oris is the sphincter muscle encircling the mouth; it closes and purses the lips. Buccinator presses the cheek against the teeth."),
  ("Quel muscle fait la moue (siffler, embrasser) ?", ["Muscle grand zygomatique", "Muscle mentonnier", "Muscle orbiculaire de la bouche", "Muscle buccinateur", "Muscle abaisseur de l'angle de la bouche"],
   "L'orbiculaire de la bouche est le sphincter qui entoure l'orifice buccal ; il ferme et projette les lèvres. Le buccinateur plaque la joue contre les dents."),
  ("Welcher Muskel spitzt die Lippen (Pfeifen, Küssen)?", ["M. zygomaticus major", "M. mentalis", "M. orbicularis oris", "M. buccinator", "M. depressor anguli oris"],
   "Der M. orbicularis oris ist der ringförmige Schließmuskel des Mundes; er schließt und spitzt die Lippen. Der M. buccinator drückt die Wange an die Zähne."),
  ("¿Qué músculo frunce los labios (silbar, besar)?", ["Músculo cigomático mayor", "Músculo mentoniano", "Músculo orbicular de la boca", "Músculo buccinador", "Músculo depresor del ángulo de la boca"],
   "El orbicular de la boca es el esfínter que rodea la boca; cierra y frunce los labios. El buccinador aprieta la mejilla contra los dientes."))

T("mu-a136b758",
  ("How many extraocular muscles move the eyeball?", ["6 (4 recti, 2 obliques)", "4", "7", "8", "5"],
   "The eyeball is moved by four recti (superior, inferior, medial, lateral) and two obliques (superior, inferior). Levator palpebrae superioris raises the eyelid and does not move the eyeball."),
  ("Combien de muscles oculomoteurs (extrinsèques) meuvent le globe oculaire ?", ["6 (4 droits, 2 obliques)", "4", "7", "8", "5"],
   "Le globe est mû par quatre muscles droits (supérieur, inférieur, médial, latéral) et deux obliques (supérieur, inférieur). Le releveur de la paupière supérieure élève la paupière et ne meut pas le globe."),
  ("Wie viele äußere Augenmuskeln bewegen den Augapfel?", ["6 (4 gerade, 2 schräge)", "4", "7", "8", "5"],
   "Der Augapfel wird von vier geraden (superior, inferior, medialis, lateralis) und zwei schrägen Muskeln (superior, inferior) bewegt. Der M. levator palpebrae superioris hebt das Lid und bewegt den Augapfel nicht."),
  ("¿Cuántos músculos extraoculares mueven el globo ocular?", ["6 (4 rectos, 2 oblicuos)", "4", "7", "8", "5"],
   "El globo lo mueven cuatro rectos (superior, inferior, medial, lateral) y dos oblicuos (superior, inferior). El elevador del párpado superior eleva el párpado y no mueve el globo."))

T("mu-93236a42",
  ("Which prominent muscle on the side of the neck runs from behind the ear to the sternum and clavicle?", ["Trapezius", "Scalenus anterior", "Omohyoid", "Sternocleidomastoid", "Platysma"],
   "Sternocleidomastoid runs from the mastoid process to the manubrium and medial clavicle; it is an important surface landmark dividing the neck into anterior and posterior triangles."),
  ("Quel muscle saillant du côté du cou va de l'arrière de l'oreille au sternum et à la clavicule ?", ["Muscle trapèze", "Muscle scalène antérieur", "Muscle omo-hyoïdien", "Muscle sterno-cléido-mastoïdien", "Platysma"],
   "Le SCM va du processus mastoïde au manubrium et à la partie médiale de la clavicule ; c'est un repère de surface important qui divise le cou en triangles antérieur et postérieur."),
  ("Welcher markante Muskel an der Halsseite zieht von hinter dem Ohr zu Brustbein und Schlüsselbein?", ["M. trapezius", "M. scalenus anterior", "M. omohyoideus", "M. sternocleidomastoideus", "Platysma"],
   "Der M. sternocleidomastoideus zieht vom Warzenfortsatz zum Manubrium und medialen Klavikulaanteil; er ist eine wichtige Landmarke, die den Hals in vorderes und seitliches Halsdreieck teilt."),
  ("¿Qué músculo prominente del lado del cuello va de detrás de la oreja al esternón y la clavícula?", ["Músculo trapecio", "Músculo escaleno anterior", "Músculo omohioideo", "Músculo esternocleidomastoideo", "Platisma"],
   "El ECM va de la apófisis mastoides al manubrio y a la parte medial de la clavícula; es un importante punto de referencia que divide el cuello en triángulos anterior y posterior."))

T("mu-17cc2434",
  ("Which thin, broad muscle of facial expression covers the front of the neck under the skin?", ["Platysma", "Mylohyoid", "Sternohyoid", "Sternocleidomastoid", "Omohyoid"],
   "Platysma is a superficial muscle of facial expression running from the upper chest to the mandible and corner of the mouth; it is supplied by the cervical branch of the facial nerve."),
  ("Quel muscle peaucier mince et large recouvre la face antérieure du cou sous la peau ?", ["Platysma", "Muscle mylo-hyoïdien", "Muscle sterno-hyoïdien", "Muscle sterno-cléido-mastoïdien", "Muscle omo-hyoïdien"],
   "Le platysma est un muscle peaucier superficiel qui va du haut du thorax à la mandibule et à l'angle de la bouche ; il est innervé par le rameau cervical du nerf facial."),
  ("Welcher dünne, breite mimische Muskel bedeckt die Vorderseite des Halses unter der Haut?", ["Platysma", "M. mylohyoideus", "M. sternohyoideus", "M. sternocleidomastoideus", "M. omohyoideus"],
   "Das Platysma ist ein oberflächlicher mimischer Muskel von der oberen Brust zum Unterkiefer und Mundwinkel; es wird vom R. colli des N. facialis innerviert."),
  ("¿Qué músculo de la expresión, delgado y ancho, cubre bajo la piel la cara anterior del cuello?", ["Platisma", "Músculo milohioideo", "Músculo esternohioideo", "Músculo esternocleidomastoideo", "Músculo omohioideo"],
   "El platisma es un músculo superficial de la expresión facial que va de la parte alta del tórax a la mandíbula y la comisura bucal; lo inerva la rama cervical del facial."))

T("mu-2e1f0cc1",
  ("Which superficial muscle of the upper back shrugs (elevates) the shoulders?", ["Serratus anterior", "Latissimus dorsi", "Erector spinae", "Trapezius", "Rhomboid major"],
   "The upper fibres of trapezius elevate the scapula (shrugging); the middle fibres retract it and the lower fibres depress it. Levator scapulae also helps elevation."),
  ("Quel muscle superficiel du haut du dos hausse les épaules ?", ["Muscle dentelé antérieur", "Muscle grand dorsal", "Muscle érecteur du rachis", "Muscle trapèze", "Muscle grand rhomboïde"],
   "Les fibres supérieures du trapèze élèvent la scapula (haussement d'épaules) ; les moyennes la rapprochent du rachis et les inférieures l'abaissent. L'élévateur de la scapula participe à l'élévation."),
  ("Welcher oberflächliche Muskel des oberen Rückens zieht die Schultern hoch?", ["M. serratus anterior", "M. latissimus dorsi", "M. erector spinae", "M. trapezius", "M. rhomboideus major"],
   "Die oberen Fasern des M. trapezius heben die Scapula (Schulterzucken), die mittleren ziehen sie zurück, die unteren senken sie. Der M. levator scapulae hilft beim Heben."),
  ("¿Qué músculo superficial de la parte alta de la espalda encoge (eleva) los hombros?", ["Músculo serrato anterior", "Músculo dorsal ancho", "Músculo erector de la columna", "Músculo trapecio", "Músculo romboides mayor"],
   "Las fibras superiores del trapecio elevan la escápula (encogerse de hombros); las medias la retraen y las inferiores la descienden. El elevador de la escápula ayuda a la elevación."))

T("mu-85f6c024",
  ("Which is the broadest muscle of the back?", ["Erector spinae", "Serratus posterior inferior", "Trapezius", "Quadratus lumborum", "Latissimus dorsi"],
   "Latissimus dorsi is a broad triangular muscle covering the lower back and loin; it extends, adducts and medially rotates the arm (the climbing and swimming muscle)."),
  ("Quel est le muscle le plus large du dos ?", ["Muscle érecteur du rachis", "Muscle dentelé postérieur inférieur", "Muscle trapèze", "Muscle carré des lombes", "Muscle grand dorsal"],
   "Le grand dorsal est un vaste muscle triangulaire qui couvre le bas du dos et la région lombale ; il étend, adducte et tourne le bras en dedans (muscle du grimpeur et du nageur)."),
  ("Welches ist der breiteste Muskel des Rückens?", ["M. erector spinae", "M. serratus posterior inferior", "M. trapezius", "M. quadratus lumborum", "M. latissimus dorsi"],
   "Der M. latissimus dorsi ist ein breiter dreieckiger Muskel über dem unteren Rücken und der Lende; er streckt, adduziert und innenrotiert den Arm (Kletter- und Schwimmmuskel)."),
  ("¿Cuál es el músculo más ancho de la espalda?", ["Músculo erector de la columna", "Músculo serrato posterior inferior", "Músculo trapecio", "Músculo cuadrado lumbar", "Músculo dorsal ancho"],
   "El dorsal ancho es un amplio músculo triangular que cubre la parte baja de la espalda y la región lumbar; extiende, aduce y rota internamente el brazo (músculo de trepar y nadar)."))

T("mu-c0a357d6",
  ("Which muscle group runs along both sides of the spine and keeps the trunk upright?", ["Latissimus dorsi", "Serratus anterior", "Trapezius", "Rhomboids", "Erector spinae"],
   "From lateral to medial, erector spinae consists of the iliocostalis, longissimus and spinalis columns; it extends the spine and maintains upright posture."),
  ("Quel groupe musculaire longe les deux côtés de la colonne et maintient le tronc droit ?", ["Muscle grand dorsal", "Muscle dentelé antérieur", "Muscle trapèze", "Muscles rhomboïdes", "Muscle érecteur du rachis"],
   "De dehors en dedans, l'érecteur du rachis comprend l'ilio-costal, le longissimus et l'épineux ; il étend le rachis et assure la station droite."),
  ("Welche Muskelgruppe verläuft beidseits der Wirbelsäule und hält den Rumpf aufrecht?", ["M. latissimus dorsi", "M. serratus anterior", "M. trapezius", "Mm. rhomboidei", "M. erector spinae"],
   "Der M. erector spinae besteht von lateral nach medial aus M. iliocostalis, M. longissimus und M. spinalis; er streckt die Wirbelsäule und sichert die aufrechte Haltung."),
  ("¿Qué grupo muscular recorre ambos lados de la columna y mantiene erguido el tronco?", ["Músculo dorsal ancho", "Músculo serrato anterior", "Músculo trapecio", "Músculos romboides", "Músculo erector de la columna"],
   "De lateral a medial, el erector de la columna consta de iliocostal, longísimo y espinoso; extiende la columna y mantiene la postura erguida."))

T("mu-e2ce0107",
  ("Which is the most important (principal) muscle of respiration?", ["Sternocleidomastoid", "External intercostals", "Diaphragm", "Rectus abdominis", "Pectoralis major"],
   "In quiet breathing the diaphragm does most of the work of inspiration; when it contracts its dome descends and the vertical diameter of the thoracic cavity increases."),
  ("Quel est le principal muscle de la respiration ?", ["Muscle sterno-cléido-mastoïdien", "Muscles intercostaux externes", "Diaphragme", "Muscle droit de l'abdomen", "Muscle grand pectoral"],
   "En respiration calme, le diaphragme assure l'essentiel de l'inspiration ; en se contractant, sa coupole s'abaisse et le diamètre vertical du thorax augmente."),
  ("Welches ist der wichtigste Atemmuskel?", ["M. sternocleidomastoideus", "Mm. intercostales externi", "Zwerchfell", "M. rectus abdominis", "M. pectoralis major"],
   "Bei ruhiger Atmung leistet das Zwerchfell den Großteil der Einatmung; bei Kontraktion senkt sich seine Kuppel und der vertikale Durchmesser des Brustraums nimmt zu."),
  ("¿Cuál es el principal músculo de la respiración?", ["Músculo esternocleidomastoideo", "Músculos intercostales externos", "Diafragma", "Músculo recto del abdomen", "Músculo pectoral mayor"],
   "En la respiración tranquila el diafragma realiza la mayor parte de la inspiración; al contraerse su cúpula desciende y aumenta el diámetro vertical de la cavidad torácica."))

T("mu-37ce2eca",
  ("Which is the largest muscle on the front of the chest?", ["Pectoralis major", "Subclavius", "Deltoid", "Serratus anterior", "Pectoralis minor"],
   "Pectoralis major is the fan-shaped muscle covering the front of the chest; it adducts, medially rotates and flexes the arm."),
  ("Quel est le plus grand muscle de la face antérieure du thorax ?", ["Muscle grand pectoral", "Muscle subclavier", "Muscle deltoïde", "Muscle dentelé antérieur", "Muscle petit pectoral"],
   "Le grand pectoral est le muscle en éventail qui recouvre la face antérieure du thorax ; il adducte, tourne en dedans et fléchit le bras."),
  ("Welches ist der größte Muskel an der Vorderseite der Brust?", ["M. pectoralis major", "M. subclavius", "M. deltoideus", "M. serratus anterior", "M. pectoralis minor"],
   "Der M. pectoralis major bedeckt fächerförmig die vordere Brustwand; er adduziert, innenrotiert und beugt den Arm."),
  ("¿Cuál es el músculo más grande de la cara anterior del tórax?", ["Músculo pectoral mayor", "Músculo subclavio", "Músculo deltoides", "Músculo serrato anterior", "Músculo pectoral menor"],
   "El pectoral mayor es el músculo en abanico que cubre la cara anterior del tórax; aduce, rota internamente y flexiona el brazo."))

T("mu-9f5f0fd6",
  ("Which muscle gives the 'six-pack' appearance of the anterior abdominal wall?", ["External oblique", "Quadratus lumborum", "Pyramidalis", "Transversus abdominis", "Rectus abdominis"],
   "The tendinous intersections across rectus abdominis divide the muscle into segments and create its characteristic appearance."),
  ("Quel muscle donne l'aspect en « tablette de chocolat » de la paroi abdominale antérieure ?", ["Muscle oblique externe", "Muscle carré des lombes", "Muscle pyramidal", "Muscle transverse de l'abdomen", "Muscle droit de l'abdomen"],
   "Les intersections tendineuses du droit de l'abdomen le divisent en segments et donnent cet aspect caractéristique."),
  ("Welcher Muskel erzeugt das „Sixpack“-Bild der vorderen Bauchwand?", ["M. obliquus externus abdominis", "M. quadratus lumborum", "M. pyramidalis", "M. transversus abdominis", "M. rectus abdominis"],
   "Die Intersectiones tendineae des M. rectus abdominis teilen den Muskel in Felder und erzeugen das typische Bild."),
  ("¿Qué músculo da el aspecto de «tableta» de la pared abdominal anterior?", ["Músculo oblicuo externo", "Músculo cuadrado lumbar", "Músculo piramidal", "Músculo transverso del abdomen", "Músculo recto del abdomen"],
   "Las intersecciones tendinosas del recto del abdomen dividen el músculo en segmentos y crean su aspecto característico."))

T("mu-8818bd60",
  ("Of the three flat muscles of the anterolateral abdominal wall, which is the most superficial?", ["Latissimus dorsi", "Internal oblique", "Transversus abdominis", "External oblique", "Rectus abdominis"],
   "From superficial to deep: external oblique, internal oblique, transversus abdominis. The fibres of the external oblique run like 'hands in pockets' (downwards and forwards)."),
  ("Des trois muscles larges de la paroi antéro-latérale de l'abdomen, lequel est le plus superficiel ?", ["Muscle grand dorsal", "Muscle oblique interne", "Muscle transverse de l'abdomen", "Muscle oblique externe", "Muscle droit de l'abdomen"],
   "De la superficie à la profondeur : oblique externe, oblique interne, transverse. Les fibres de l'oblique externe ont la direction des « mains dans les poches » (en bas et en avant)."),
  ("Welcher der drei platten Muskeln der seitlichen Bauchwand liegt am oberflächlichsten?", ["M. latissimus dorsi", "M. obliquus internus abdominis", "M. transversus abdominis", "M. obliquus externus abdominis", "M. rectus abdominis"],
   "Von oberflächlich nach tief: M. obliquus externus, M. obliquus internus, M. transversus abdominis. Die Fasern des äußeren Schrägen verlaufen wie „Hände in den Hosentaschen“ (nach unten vorn)."),
  ("De los tres músculos planos de la pared anterolateral del abdomen, ¿cuál es el más superficial?", ["Músculo dorsal ancho", "Músculo oblicuo interno", "Músculo transverso del abdomen", "Músculo oblicuo externo", "Músculo recto del abdomen"],
   "De superficial a profundo: oblicuo externo, oblicuo interno, transverso. Las fibras del oblicuo externo siguen la dirección de las «manos en los bolsillos» (hacia abajo y adelante)."))

T("mu-20d486f6",
  ("Between which two points does the inguinal ligament run?", ["Xiphoid process and pubic tubercle", "Greater trochanter and pubic tubercle", "Anterior superior iliac spine and pubic tubercle", "Anterior inferior iliac spine and ischial tuberosity", "Iliac crest and pubic symphysis"],
   "The inguinal ligament is the rolled-under lower border of the external oblique aponeurosis; it runs from the ASIS to the pubic tubercle and is an important landmark of the groin."),
  ("Entre quels deux points s'étend le ligament inguinal ?", ["Processus xiphoïde et tubercule pubien", "Grand trochanter et tubercule pubien", "Épine iliaque antéro-supérieure et tubercule pubien", "Épine iliaque antéro-inférieure et tubérosité ischiatique", "Crête iliaque et symphyse pubienne"],
   "Le ligament inguinal est le bord inférieur enroulé de l'aponévrose de l'oblique externe ; il va de l'EIAS au tubercule pubien et constitue un repère important de l'aine."),
  ("Zwischen welchen zwei Punkten spannt sich das Leistenband (Lig. inguinale)?", ["Processus xiphoideus und Tuberculum pubicum", "Trochanter major und Tuberculum pubicum", "Spina iliaca anterior superior und Tuberculum pubicum", "Spina iliaca anterior inferior und Tuber ischiadicum", "Crista iliaca und Symphyse"],
   "Das Leistenband ist der eingerollte Unterrand der Aponeurose des M. obliquus externus; es zieht von der Spina iliaca anterior superior zum Tuberculum pubicum und ist eine wichtige Landmarke der Leiste."),
  ("¿Entre qué dos puntos se extiende el ligamento inguinal?", ["Apófisis xifoides y tubérculo del pubis", "Trocánter mayor y tubérculo del pubis", "Espina ilíaca anterosuperior y tubérculo del pubis", "Espina ilíaca anteroinferior y tuberosidad isquiática", "Cresta ilíaca y sínfisis del pubis"],
   "El ligamento inguinal es el borde inferior replegado de la aponeurosis del oblicuo externo; va de la EIAS al tubérculo del pubis y es una referencia importante de la ingle."))

T("mu-ecbf1e9c",
  ("Where does the linea alba run?", ["Along the lateral border of rectus", "Along the costal margin", "Between the ASIS and pubic tubercle", "From the umbilicus to the costal margin", "Between the xiphoid process and the pubic symphysis"],
   "The linea alba is the fibrous band between the two recti formed by the midline fusion of the aponeuroses of the abdominal muscles; the umbilicus lies on it."),
  ("Où s'étend la ligne blanche ?", ["Le long du bord latéral du droit", "Le long du rebord costal", "Entre l'EIAS et le tubercule pubien", "De l'ombilic au rebord costal", "Entre le processus xiphoïde et la symphyse pubienne"],
   "La ligne blanche est le raphé fibreux situé entre les deux droits, formé par l'union médiane des aponévroses des muscles abdominaux ; l'ombilic se trouve sur cette ligne."),
  ("Wo verläuft die Linea alba?", ["Entlang des Außenrands des M. rectus", "Entlang des Rippenbogens", "Zwischen Spina iliaca anterior superior und Tuberculum pubicum", "Vom Nabel zum Rippenbogen", "Zwischen Processus xiphoideus und Symphyse"],
   "Die Linea alba ist der fibröse Streifen zwischen beiden Mm. recti, gebildet durch die Vereinigung der Bauchmuskelaponeurosen in der Mittellinie; der Nabel liegt auf ihr."),
  ("¿Por dónde se extiende la línea alba?", ["A lo largo del borde lateral del recto", "A lo largo del reborde costal", "Entre la EIAS y el tubérculo del pubis", "Del ombligo al reborde costal", "Entre la apófisis xifoides y la sínfisis del pubis"],
   "La línea alba es la banda fibrosa entre ambos rectos formada por la unión en la línea media de las aponeurosis de los músculos abdominales; el ombligo está sobre ella."))

T("mu-6e45f64a",
  ("Which triangular muscle gives the shoulder its rounded contour?", ["Deltoid", "Supraspinatus", "Pectoralis major", "Teres major", "Trapezius"],
   "Deltoid arises from the clavicle, acromion and spine of the scapula and inserts on the deltoid tuberosity; it gives the shoulder its rounded contour and abducts the arm."),
  ("Quel muscle triangulaire donne à l'épaule son galbe arrondi ?", ["Muscle deltoïde", "Muscle supra-épineux", "Muscle grand pectoral", "Muscle grand rond", "Muscle trapèze"],
   "Le deltoïde naît de la clavicule, de l'acromion et de l'épine de la scapula et se termine sur la tubérosité deltoïdienne ; il donne le galbe de l'épaule et met le bras en abduction."),
  ("Welcher dreieckige Muskel gibt der Schulter ihre runde Kontur?", ["M. deltoideus", "M. supraspinatus", "M. pectoralis major", "M. teres major", "M. trapezius"],
   "Der M. deltoideus entspringt an Klavikula, Akromion und Spina scapulae und setzt an der Tuberositas deltoidea an; er formt die runde Schulterkontur und abduziert den Arm."),
  ("¿Qué músculo triangular da al hombro su contorno redondeado?", ["Músculo deltoides", "Músculo supraespinoso", "Músculo pectoral mayor", "Músculo redondo mayor", "Músculo trapecio"],
   "El deltoides nace de la clavícula, el acromion y la espina de la escápula y se inserta en la tuberosidad deltoidea; da el contorno redondeado del hombro y abduce el brazo."))

T("mu-b57e5057",
  ("Which muscles form the rotator cuff?", ["Deltoid, supraspinatus, infraspinatus and teres minor", "Supraspinatus, infraspinatus, teres minor and subscapularis", "Supraspinatus, teres major, teres minor and latissimus dorsi", "Supraspinatus, infraspinatus, teres major and subscapularis", "Subscapularis, pectoralis minor, teres minor and deltoid"],
   "The rotator cuff (SITS) is the dynamic stabiliser holding the humeral head in the glenoid. Teres major is not part of the rotator cuff."),
  ("Quels muscles forment la coiffe des rotateurs ?", ["Deltoïde, supra-épineux, infra-épineux et petit rond", "Supra-épineux, infra-épineux, petit rond et subscapulaire", "Supra-épineux, grand rond, petit rond et grand dorsal", "Supra-épineux, infra-épineux, grand rond et subscapulaire", "Subscapulaire, petit pectoral, petit rond et deltoïde"],
   "La coiffe des rotateurs est le stabilisateur dynamique qui maintient la tête humérale dans la glène. Le grand rond n'en fait pas partie."),
  ("Welche Muskeln bilden die Rotatorenmanschette?", ["Deltoideus, Supraspinatus, Infraspinatus und Teres minor", "Supraspinatus, Infraspinatus, Teres minor und Subscapularis", "Supraspinatus, Teres major, Teres minor und Latissimus dorsi", "Supraspinatus, Infraspinatus, Teres major und Subscapularis", "Subscapularis, Pectoralis minor, Teres minor und Deltoideus"],
   "Die Rotatorenmanschette ist der dynamische Stabilisator, der den Humeruskopf in der Pfanne hält. Der M. teres major gehört nicht dazu."),
  ("¿Qué músculos forman el manguito de los rotadores?", ["Deltoides, supraespinoso, infraespinoso y redondo menor", "Supraespinoso, infraespinoso, redondo menor y subescapular", "Supraespinoso, redondo mayor, redondo menor y dorsal ancho", "Supraespinoso, infraespinoso, redondo mayor y subescapular", "Subescapular, pectoral menor, redondo menor y deltoides"],
   "El manguito de los rotadores es el estabilizador dinámico que mantiene la cabeza humeral en la glena. El redondo mayor no forma parte de él."))

T("mu-19bfd68a",
  ("Which is the 'biceps' muscle on the front of the arm?", ["Coracobrachialis", "Brachialis", "Brachioradialis", "Biceps brachii", "Triceps brachii"],
   "Biceps brachii is the two-headed muscle on the front of the arm; it flexes the elbow and is a powerful supinator of the forearm."),
  ("Quel est le muscle « biceps » de la face antérieure du bras ?", ["Muscle coraco-brachial", "Muscle brachial", "Muscle brachio-radial", "Muscle biceps brachial", "Muscle triceps brachial"],
   "Le biceps brachial est le muscle à deux chefs de la face antérieure du bras ; il fléchit le coude et est un puissant supinateur de l'avant-bras."),
  ("Welcher ist der „Bizeps“ an der Vorderseite des Oberarms?", ["M. coracobrachialis", "M. brachialis", "M. brachioradialis", "M. biceps brachii", "M. triceps brachii"],
   "Der M. biceps brachii ist der zweiköpfige Muskel an der Vorderseite des Oberarms; er beugt den Ellenbogen und ist ein kräftiger Supinator des Unterarms."),
  ("¿Cuál es el «bíceps» de la cara anterior del brazo?", ["Músculo coracobraquial", "Músculo braquial", "Músculo braquiorradial", "Músculo bíceps braquial", "Músculo tríceps braquial"],
   "El bíceps braquial es el músculo de dos cabezas de la cara anterior del brazo; flexiona el codo y es un potente supinador del antebrazo."))
