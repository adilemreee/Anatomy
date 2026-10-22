KIND = "questions"
SYSTEM = "skeletal"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("sk-efcc65cb",
  ("Which muscle attaches to the mastoid process?", ["Temporalis", "Masseter", "Trapezius", "Platysma", "Sternocleidomastoid"],
   "The SCM arises from the sternum and clavicle and attaches to the mastoid process and the lateral part of the superior nuchal line. The mastoid process is absent at birth and develops in childhood under the pull of the muscle."),
  ("Quel muscle s'insère sur le processus mastoïde ?", ["Temporal", "Masséter", "Trapèze", "Platysma", "Sterno-cléido-mastoïdien"],
   "Le SCM naît du sternum et de la clavicule et s'insère sur le processus mastoïde et la partie latérale de la ligne nucale supérieure. Le processus mastoïde est absent à la naissance et se développe dans l'enfance sous la traction du muscle."),
  ("Welcher Muskel setzt am Warzenfortsatz an?", ["M. temporalis", "M. masseter", "M. trapezius", "Platysma", "M. sternocleidomastoideus"],
   "Der SCM entspringt an Sternum und Klavikula und setzt am Processus mastoideus und am lateralen Teil der Linea nuchae superior an. Der Warzenfortsatz fehlt bei Geburt und entwickelt sich in der Kindheit durch den Muskelzug."),
  ("¿Qué músculo se inserta en la apófisis mastoides?", ["Temporal", "Masetero", "Trapecio", "Platisma", "Esternocleidomastoideo"],
   "El ECM nace del esternón y la clavícula y se inserta en la apófisis mastoides y la parte lateral de la línea nucal superior. La mastoides no existe al nacer y se desarrolla en la infancia por la tracción del músculo."))

T("sk-299c3612",
  ("Which structure does NOT pass through the foramen magnum?", ["Internal jugular vein", "Vertebral arteries", "Anterior spinal artery", "Medulla oblongata", "Spinal root of the accessory nerve"],
   "The medulla oblongata and its meninges, the vertebral and spinal arteries and the spinal roots of the accessory nerve pass through the foramen magnum. The internal jugular vein begins at the jugular foramen."),
  ("Quelle structure ne passe PAS par le foramen magnum ?", ["Veine jugulaire interne", "Artères vertébrales", "Artère spinale antérieure", "Moelle allongée", "Racine spinale du nerf accessoire"],
   "Par le foramen magnum passent la moelle allongée et ses méninges, les artères vertébrales et spinales et les racines spinales du nerf accessoire. La veine jugulaire interne naît au foramen jugulaire."),
  ("Welche Struktur zieht NICHT durch das Foramen magnum?", ["V. jugularis interna", "Aa. vertebrales", "A. spinalis anterior", "Medulla oblongata", "Spinale Wurzel des N. accessorius"],
   "Durch das Foramen magnum ziehen Medulla oblongata mit Hirnhäuten, Aa. vertebrales und spinales sowie die spinalen Wurzeln des N. accessorius. Die V. jugularis interna beginnt am Foramen jugulare."),
  ("¿Qué estructura NO pasa por el agujero magno?", ["Vena yugular interna", "Arterias vertebrales", "Arteria espinal anterior", "Bulbo raquídeo", "Raíz espinal del nervio accesorio"],
   "Por el agujero magno pasan el bulbo y sus meninges, las arterias vertebrales y espinales y las raíces espinales del nervio accesorio. La vena yugular interna empieza en el agujero yugular."))

T("sk-94a4fb4f",
  ("Where does the sphenoidal sinus open into the nasal cavity?", ["Inferior nasal meatus", "Superior nasal meatus", "Sphenoethmoidal recess", "Middle nasal meatus", "Nasopharynx"],
   "The sphenoidal sinus opens into the sphenoethmoidal recess above and behind the superior concha. The posterior ethmoidal cells open into the superior meatus; the frontal, maxillary and anterior ethmoidal sinuses into the middle meatus; the nasolacrimal duct into the inferior meatus."),
  ("Où le sinus sphénoïdal s'ouvre-t-il dans la cavité nasale ?", ["Méat nasal inférieur", "Méat nasal supérieur", "Récessus sphéno-ethmoïdal", "Méat nasal moyen", "Nasopharynx"],
   "Le sinus sphénoïdal s'ouvre dans le récessus sphéno-ethmoïdal, au-dessus et en arrière du cornet supérieur. Les cellules ethmoïdales postérieures s'ouvrent dans le méat supérieur ; les sinus frontal, maxillaire et ethmoïdal antérieur dans le méat moyen ; le conduit lacrymo-nasal dans le méat inférieur."),
  ("Wo mündet die Keilbeinhöhle in die Nasenhöhle?", ["Unterer Nasengang", "Oberer Nasengang", "Recessus sphenoethmoidalis", "Mittlerer Nasengang", "Nasopharynx"],
   "Die Keilbeinhöhle mündet in den Recessus sphenoethmoidalis oberhalb und hinter der oberen Muschel. Die hinteren Siebbeinzellen münden in den oberen, Stirn-, Kiefer- und vordere Siebbeinhöhlen in den mittleren, der Tränennasengang in den unteren Nasengang."),
  ("¿Dónde se abre el seno esfenoidal en la cavidad nasal?", ["Meato nasal inferior", "Meato nasal superior", "Receso esfenoetmoidal", "Meato nasal medio", "Nasofaringe"],
   "El seno esfenoidal se abre en el receso esfenoetmoidal, por encima y detrás del cornete superior. Las celdillas etmoidales posteriores se abren en el meato superior; los senos frontal, maxilar y etmoidal anterior en el medio; el conducto nasolagrimal en el inferior."))

T("sk-f4bad9ce",
  ("Which muscles attach to the lateral plate of the pterygoid process of the sphenoid?", ["Masseter and temporalis", "Digastric and stylohyoid", "Tensor veli palatini and levator veli palatini", "Buccinator and superior pharyngeal constrictor", "Lateral pterygoid and medial pterygoid"],
   "The lower head of the lateral pterygoid arises from the outer surface of the lateral plate and the deep head of the medial pterygoid from its inner surface. The tendon of tensor veli palatini turns around the hamulus at the tip of the medial plate."),
  ("Quels muscles s'insèrent sur la lame latérale du processus ptérygoïde du sphénoïde ?", ["Masséter et temporal", "Digastrique et stylo-hyoïdien", "Tenseur et élévateur du voile du palais", "Buccinateur et constricteur supérieur du pharynx", "Ptérygoïdien latéral et ptérygoïdien médial"],
   "Le chef inférieur du ptérygoïdien latéral naît de la face externe de la lame latérale et le chef profond du ptérygoïdien médial de sa face interne. Le tendon du tenseur du voile du palais se réfléchit autour de l'hamulus de la lame médiale."),
  ("Welche Muskeln entspringen an der Lamina lateralis des Processus pterygoideus?", ["M. masseter und M. temporalis", "M. digastricus und M. stylohyoideus", "M. tensor und M. levator veli palatini", "M. buccinator und M. constrictor pharyngis superior", "M. pterygoideus lateralis und M. pterygoideus medialis"],
   "Der untere Kopf des M. pterygoideus lateralis entspringt an der Außenfläche der Lamina lateralis, der tiefe Kopf des M. pterygoideus medialis an ihrer Innenfläche. Um den Hamulus der Lamina medialis zieht die Sehne des M. tensor veli palatini."),
  ("¿Qué músculos se insertan en la lámina lateral de la apófisis pterigoides del esfenoides?", ["Masetero y temporal", "Digástrico y estilohioideo", "Tensor y elevador del velo del paladar", "Buccinador y constrictor superior de la faringe", "Pterigoideo lateral y pterigoideo medial"],
   "La cabeza inferior del pterigoideo lateral nace de la cara externa de la lámina lateral y la cabeza profunda del pterigoideo medial de su cara interna. El tendón del tensor del velo del paladar rodea el gancho de la lámina medial."))

T("sk-24639fbf",
  ("Which is the thickest wall of the orbit?", ["Lateral wall", "Floor", "Medial wall", "Apex of the orbit", "Roof"],
   "The lateral wall, formed by the zygomatic bone and greater wing of the sphenoid, is the thickest. The thinnest is the medial wall with the lamina papyracea of the ethmoid; blow-out fractures most often involve the floor."),
  ("Quelle est la paroi la plus épaisse de l'orbite ?", ["Paroi latérale", "Plancher", "Paroi médiale", "Apex de l'orbite", "Toit"],
   "La paroi latérale, formée par le zygomatique et la grande aile du sphénoïde, est la plus épaisse. La plus mince est la paroi médiale (lame papyracée de l'ethmoïde) ; les fractures en blow-out touchent surtout le plancher."),
  ("Welche ist die dickste Wand der Orbita?", ["Laterale Wand", "Boden", "Mediale Wand", "Orbitaspitze", "Dach"],
   "Die laterale Wand aus Jochbein und großem Keilbeinflügel ist die dickste. Die dünnste ist die mediale Wand mit der Lamina papyracea des Siebbeins; Blow-out-Frakturen betreffen meist den Boden."),
  ("¿Cuál es la pared más gruesa de la órbita?", ["Pared lateral", "Suelo", "Pared medial", "Vértice orbitario", "Techo"],
   "La pared lateral, formada por el cigomático y el ala mayor del esfenoides, es la más gruesa. La más delgada es la medial (lámina papirácea del etmoides); las fracturas en blow-out afectan sobre todo al suelo."))

T("sk-fe9c4d6f",
  ("Which nerve passes through the inferior orbital fissure?", ["Infraorbital nerve", "Trochlear nerve", "Lacrimal nerve", "Frontal nerve", "Abducens nerve"],
   "The maxillary nerve enters the orbit from the pterygopalatine fossa through the inferior orbital fissure and becomes the infraorbital nerve. The frontal, lacrimal, trochlear and abducens nerves pass through the superior orbital fissure."),
  ("Quel nerf passe par la fissure orbitaire inférieure ?", ["Nerf infra-orbitaire", "Nerf trochléaire", "Nerf lacrymal", "Nerf frontal", "Nerf abducens"],
   "Le nerf maxillaire entre dans l'orbite depuis la fosse ptérygo-palatine par la fissure orbitaire inférieure et devient le nerf infra-orbitaire. Les nerfs frontal, lacrymal, trochléaire et abducens passent par la fissure orbitaire supérieure."),
  ("Welcher Nerv zieht durch die Fissura orbitalis inferior?", ["N. infraorbitalis", "N. trochlearis", "N. lacrimalis", "N. frontalis", "N. abducens"],
   "Der N. maxillaris gelangt aus der Flügelgaumengrube durch die Fissura orbitalis inferior in die Orbita und heißt dann N. infraorbitalis. N. frontalis, lacrimalis, trochlearis und abducens ziehen durch die Fissura orbitalis superior."),
  ("¿Qué nervio pasa por la fisura orbitaria inferior?", ["Nervio infraorbitario", "Nervio troclear", "Nervio lagrimal", "Nervio frontal", "Nervio abducens"],
   "El nervio maxilar entra en la órbita desde la fosa pterigopalatina por la fisura orbitaria inferior y pasa a llamarse infraorbitario. Los nervios frontal, lagrimal, troclear y abducens pasan por la fisura orbitaria superior."))

T("sk-50fc7e36",
  ("Which opening connects the pterygopalatine fossa with the middle cranial fossa?", ["Foramen spinosum", "Optic canal", "Foramen ovale", "Foramen rotundum", "Superior orbital fissure"],
   "The maxillary nerve (V2) passes from the middle cranial fossa to the pterygopalatine fossa through the foramen rotundum. The foramen ovale and spinosum open into the infratemporal fossa."),
  ("Quel orifice relie la fosse ptérygo-palatine à la fosse crânienne moyenne ?", ["Foramen épineux", "Canal optique", "Foramen ovale", "Foramen rond", "Fissure orbitaire supérieure"],
   "Le nerf maxillaire (V2) passe de la fosse crânienne moyenne à la fosse ptérygo-palatine par le foramen rond. Les foramens ovale et épineux débouchent dans la fosse infratemporale."),
  ("Welche Öffnung verbindet die Flügelgaumengrube mit der mittleren Schädelgrube?", ["Foramen spinosum", "Canalis opticus", "Foramen ovale", "Foramen rotundum", "Fissura orbitalis superior"],
   "Der N. maxillaris (V2) zieht durch das Foramen rotundum von der mittleren Schädelgrube in die Flügelgaumengrube. Foramen ovale und spinosum öffnen sich zur Fossa infratemporalis."),
  ("¿Qué orificio comunica la fosa pterigopalatina con la fosa craneal media?", ["Agujero espinoso", "Conducto óptico", "Agujero oval", "Agujero redondo", "Fisura orbitaria superior"],
   "El nervio maxilar (V2) pasa de la fosa craneal media a la pterigopalatina por el agujero redondo. Los agujeros oval y espinoso se abren a la fosa infratemporal."))

T("sk-c03603d8",
  ("Between the two halves of which bone is the metopic suture?", ["Mandible", "Parietal bone", "Sphenoid bone", "Occipital bone", "Frontal bone"],
   "At birth the frontal bone is in two halves; the metopic suture between them usually closes at 1–2 years. In some adults it remains open and can be mistaken for a fracture line on X-ray."),
  ("Entre les deux moitiés de quel os se trouve la suture métopique ?", ["Mandibule", "Pariétal", "Sphénoïde", "Occipital", "Frontal"],
   "À la naissance, le frontal est formé de deux moitiés ; la suture métopique qui les sépare se ferme en général vers 1–2 ans. Elle persiste chez certains adultes et peut être confondue avec un trait de fracture."),
  ("Zwischen den beiden Hälften welches Knochens liegt die Stirnnaht (Sutura metopica)?", ["Unterkiefer", "Scheitelbein", "Keilbein", "Hinterhauptsbein", "Stirnbein"],
   "Das Stirnbein besteht bei Geburt aus zwei Hälften; die Stirnnaht dazwischen schließt sich meist mit 1–2 Jahren. Bei manchen Erwachsenen bleibt sie offen und kann im Röntgen mit einer Frakturlinie verwechselt werden."),
  ("¿Entre las dos mitades de qué hueso está la sutura metópica?", ["Mandíbula", "Parietal", "Esfenoides", "Occipital", "Frontal"],
   "Al nacer el frontal tiene dos mitades; la sutura metópica entre ellas suele cerrarse a los 1–2 años. En algunos adultos persiste y puede confundirse con una fractura en la radiografía."))

T("sk-af9c3b69",
  ("Between which bones does the posterior fontanelle lie?", ["The two parietal bones and the occipital bone", "Sphenoid and temporal", "Parietal, temporal and occipital", "The two frontal and two parietal bones", "Frontal, parietal, temporal and sphenoid"],
   "The triangular posterior fontanelle lies at the lambda, between the two parietal bones and the occipital bone, and closes at 2–3 months. The anterior fontanelle lies at the bregma between the frontal and parietal bones."),
  ("Entre quels os se situe la fontanelle postérieure ?", ["Les deux pariétaux et l'occipital", "Sphénoïde et temporal", "Pariétal, temporal et occipital", "Les deux frontaux et les deux pariétaux", "Frontal, pariétal, temporal et sphénoïde"],
   "La fontanelle postérieure, triangulaire, se trouve au lambda, entre les deux pariétaux et l'occipital, et se ferme vers 2–3 mois. La fontanelle antérieure est au bregma, entre frontal et pariétaux."),
  ("Zwischen welchen Knochen liegt die kleine (hintere) Fontanelle?", ["Den beiden Scheitelbeinen und dem Hinterhauptsbein", "Keilbein und Schläfenbein", "Scheitel-, Schläfen- und Hinterhauptsbein", "Den beiden Stirn- und Scheitelbeinen", "Stirn-, Scheitel-, Schläfen- und Keilbein"],
   "Die dreieckige kleine Fontanelle liegt am Lambda zwischen beiden Scheitelbeinen und dem Hinterhauptsbein und schließt sich mit 2–3 Monaten. Die große Fontanelle liegt am Bregma zwischen Stirn- und Scheitelbeinen."),
  ("¿Entre qué huesos se sitúa la fontanela posterior?", ["Los dos parietales y el occipital", "Esfenoides y temporal", "Parietal, temporal y occipital", "Los dos frontales y los dos parietales", "Frontal, parietal, temporal y esfenoides"],
   "La fontanela posterior, triangular, está en el lambda, entre los dos parietales y el occipital, y se cierra a los 2–3 meses. La anterior está en el bregma, entre frontal y parietales."))

T("sk-7e5d8299",
  ("At which vertebral level does the hyoid bone usually lie?", ["C1", "C5", "C3", "C6", "T1"],
   "The hyoid lies at the level of C3. The upper border of the thyroid cartilage corresponds to C4 and the cricoid cartilage to C6."),
  ("À quel niveau vertébral se trouve habituellement l'os hyoïde ?", ["C1", "C5", "C3", "C6", "T1"],
   "L'os hyoïde se situe en regard de C3. Le bord supérieur du cartilage thyroïde correspond à C4 et le cartilage cricoïde à C6."),
  ("In welcher Wirbelhöhe liegt das Zungenbein gewöhnlich?", ["C1", "C5", "C3", "C6", "T1"],
   "Das Zungenbein liegt in Höhe C3. Der Oberrand des Schildknorpels entspricht C4, der Ringknorpel C6."),
  ("¿A qué nivel vertebral suele estar el hueso hioides?", ["C1", "C5", "C3", "C6", "T1"],
   "El hioides está a la altura de C3. El borde superior del cartílago tiroides corresponde a C4 y el cricoides a C6."))

T("sk-337e8167",
  ("Which group of teeth is absent in the primary (deciduous) dentition?", ["Premolars", "Central incisors", "Canines", "Lateral incisors", "Molars"],
   "The primary dentition has 20 teeth: in each half-jaw 2 incisors, 1 canine and 2 molars; there are no deciduous premolars. The permanent premolars erupt in place of the deciduous molars."),
  ("Quel groupe de dents n'existe pas dans la denture temporaire (dents de lait) ?", ["Prémolaires", "Incisives centrales", "Canines", "Incisives latérales", "Molaires"],
   "La denture temporaire compte 20 dents : par hémi-arcade 2 incisives, 1 canine et 2 molaires ; il n'y a pas de prémolaires temporaires. Les prémolaires définitives remplacent les molaires temporaires."),
  ("Welche Zahngruppe fehlt im Milchgebiss?", ["Prämolaren", "Mittlere Schneidezähne", "Eckzähne", "Seitliche Schneidezähne", "Molaren"],
   "Das Milchgebiss hat 20 Zähne: je Kieferhälfte 2 Schneidezähne, 1 Eckzahn und 2 Molaren; Milchprämolaren gibt es nicht. Die bleibenden Prämolaren brechen an der Stelle der Milchmolaren durch."),
  ("¿Qué grupo de dientes falta en la dentición temporal (de leche)?", ["Premolares", "Incisivos centrales", "Caninos", "Incisivos laterales", "Molares"],
   "La dentición temporal tiene 20 dientes: en cada hemiarcada 2 incisivos, 1 canino y 2 molares; no hay premolares temporales. Los premolares permanentes erupcionan en lugar de los molares temporales."))

T("sk-acf4fff3",
  ("Which permanent tooth erupts first?", ["1st molar (about 6 years)", "1st premolar", "Central incisor", "Canine", "3rd molar"],
   "The first permanent tooth to erupt, behind the deciduous teeth, is the 1st molar (the 'six-year molar'); the last is the 3rd molar (wisdom tooth)."),
  ("Quelle dent définitive fait éruption en premier ?", ["1re molaire (vers 6 ans)", "1re prémolaire", "Incisive centrale", "Canine", "3e molaire"],
   "La première dent définitive à apparaître, en arrière des dents temporaires, est la 1re molaire (« dent de 6 ans ») ; la dernière est la 3e molaire (dent de sagesse)."),
  ("Welcher bleibende Zahn bricht zuerst durch?", ["1. Molar (etwa mit 6 Jahren)", "1. Prämolar", "Mittlerer Schneidezahn", "Eckzahn", "3. Molar"],
   "Der erste bleibende Zahn, der hinter den Milchzähnen durchbricht, ist der 1. Molar („Sechsjahrmolar“); der letzte ist der 3. Molar (Weisheitszahn)."),
  ("¿Qué diente permanente erupciona primero?", ["1.er molar (hacia los 6 años)", "1.er premolar", "Incisivo central", "Canino", "3.er molar"],
   "El primer diente permanente en erupcionar, detrás de los temporales, es el 1.er molar («molar de los 6 años»); el último es el 3.er molar (muela del juicio)."))

T("sk-5476a288",
  ("A heart-shaped body and a small round vertebral foramen are typical of which vertebrae?", ["Cervical vertebrae", "Lumbar vertebrae", "Coccygeal vertebrae", "Sacral vertebrae", "Thoracic vertebrae"],
   "Thoracic vertebrae have a heart-shaped body and a small round vertebral foramen; there are facets for the ribs on the body and transverse processes. In cervical vertebrae the foramen is triangular and wide."),
  ("Un corps en forme de cœur et un petit foramen vertébral arrondi caractérisent quelles vertèbres ?", ["Cervicales", "Lombales", "Coccygiennes", "Sacrales", "Thoraciques"],
   "Les vertèbres thoraciques ont un corps en forme de cœur et un petit foramen vertébral arrondi ; le corps et les processus transverses portent des surfaces costales. Aux vertèbres cervicales le foramen est triangulaire et large."),
  ("Ein herzförmiger Körper und ein kleines rundes Wirbelloch sind typisch für welche Wirbel?", ["Halswirbel", "Lendenwirbel", "Steißwirbel", "Kreuzbeinwirbel", "Brustwirbel"],
   "Brustwirbel haben einen herzförmigen Körper und ein kleines rundes Wirbelloch; Körper und Querfortsätze tragen Rippengelenkflächen. Bei Halswirbeln ist das Loch dreieckig und weit."),
  ("¿Un cuerpo en forma de corazón y un agujero vertebral pequeño y redondo son típicos de qué vértebras?", ["Cervicales", "Lumbares", "Coccígeas", "Sacras", "Torácicas"],
   "Las vértebras torácicas tienen cuerpo en forma de corazón y agujero vertebral pequeño y redondo; el cuerpo y las apófisis transversas tienen carillas costales. En las cervicales el agujero es triangular y amplio."))

T("sk-6bfe54be",
  ("Which are the primary curvatures of the vertebral column?", ["Thoracic and sacral kyphosis", "Lumbar lordosis and sacral kyphosis", "Cervical and lumbar lordosis", "Cervical lordosis and thoracic kyphosis", "Thoracic kyphosis and lumbar lordosis"],
   "The thoracic and sacral kyphoses, remnants of the fetal C-shaped curve, are the primary curvatures; the cervical and lumbar lordoses develop after birth (secondary curvatures)."),
  ("Quelles sont les courbures primaires de la colonne vertébrale ?", ["Cyphoses thoracique et sacrale", "Lordose lombale et cyphose sacrale", "Lordoses cervicale et lombale", "Lordose cervicale et cyphose thoracique", "Cyphose thoracique et lordose lombale"],
   "Les cyphoses thoracique et sacrale, vestiges de la courbure fœtale en C, sont les courbures primaires ; les lordoses cervicale et lombale apparaissent après la naissance (courbures secondaires)."),
  ("Welche sind die primären Krümmungen der Wirbelsäule?", ["Brust- und Sakralkyphose", "Lendenlordose und Sakralkyphose", "Hals- und Lendenlordose", "Halslordose und Brustkyphose", "Brustkyphose und Lendenlordose"],
   "Brust- und Sakralkyphose, Reste der fetalen C-Krümmung, sind die primären Krümmungen; Hals- und Lendenlordose entstehen nach der Geburt (sekundäre Krümmungen)."),
  ("¿Cuáles son las curvaturas primarias de la columna vertebral?", ["Cifosis torácica y sacra", "Lordosis lumbar y cifosis sacra", "Lordosis cervical y lumbar", "Lordosis cervical y cifosis torácica", "Cifosis torácica y lordosis lumbar"],
   "Las cifosis torácica y sacra, restos de la curva fetal en C, son las curvaturas primarias; las lordosis cervical y lumbar aparecen tras el nacimiento (secundarias)."))

T("sk-a4798013",
  ("Through which intervertebral foramen does the L4 spinal nerve exit?", ["Between T12 and L1", "Between L5 and S1", "Between L4 and L5", "Between L3 and L4", "Between L2 and L3"],
   "In the thoracic and lumbar regions the spinal nerves exit below the vertebra of the same number; the L4 nerve is in the L4–L5 foramen. A posterolateral L4–L5 disc herniation, however, usually compresses the next root, L5."),
  ("Par quel foramen intervertébral sort le nerf spinal L4 ?", ["Entre T12 et L1", "Entre L5 et S1", "Entre L4 et L5", "Entre L3 et L4", "Entre L2 et L3"],
   "Aux étages thoracique et lombal, les nerfs spinaux sortent sous la vertèbre de même numéro ; le nerf L4 passe dans le foramen L4–L5. Une hernie discale postéro-latérale L4–L5 comprime cependant le plus souvent la racine suivante, L5."),
  ("Durch welches Foramen intervertebrale tritt der Spinalnerv L4 aus?", ["Zwischen T12 und L1", "Zwischen L5 und S1", "Zwischen L4 und L5", "Zwischen L3 und L4", "Zwischen L2 und L3"],
   "Im Brust- und Lendenbereich treten die Spinalnerven unterhalb des gleichnamigen Wirbels aus; L4 liegt im Foramen L4–L5. Ein posterolateraler Bandscheibenvorfall L4–L5 komprimiert jedoch meist die nächste Wurzel, L5."),
  ("¿Por qué agujero intervertebral sale el nervio espinal L4?", ["Entre T12 y L1", "Entre L5 y S1", "Entre L4 y L5", "Entre L3 y L4", "Entre L2 y L3"],
   "En las regiones torácica y lumbar los nervios espinales salen por debajo de la vértebra del mismo número; L4 pasa por el agujero L4–L5. Sin embargo, una hernia discal posterolateral L4–L5 suele comprimir la raíz siguiente, L5."))

T("sk-d8cdddd6",
  ("Which muscle attaches to the rough area (tuberosity) on the outer surface of the 2nd rib?", ["Serratus anterior", "Scalenus anterior", "Pectoralis minor", "Pectoralis major", "Subclavius"],
   "The 2nd rib is atypical: it is twice as long as the 1st and has a tuberosity on its outer surface for the first digitation of serratus anterior. Pectoralis minor attaches to ribs 3–5, scalenus anterior and subclavius to the 1st rib."),
  ("Quel muscle s'insère sur la zone rugueuse (tubérosité) de la face externe de la 2e côte ?", ["Dentelé antérieur", "Scalène antérieur", "Petit pectoral", "Grand pectoral", "Subclavier"],
   "La 2e côte est atypique : deux fois plus longue que la 1re, elle porte sur sa face externe la tubérosité de la première digitation du dentelé antérieur. Le petit pectoral s'insère sur les 3e–5e côtes, le scalène antérieur et le subclavier sur la 1re."),
  ("Welcher Muskel setzt an der rauen Fläche (Tuberositas) der Außenseite der 2. Rippe an?", ["M. serratus anterior", "M. scalenus anterior", "M. pectoralis minor", "M. pectoralis major", "M. subclavius"],
   "Die 2. Rippe ist atypisch: doppelt so lang wie die 1. und mit einer Tuberositas für die erste Zacke des M. serratus anterior an der Außenfläche. Pectoralis minor setzt an der 3.–5. Rippe an, Scalenus anterior und Subclavius an der 1."),
  ("¿Qué músculo se inserta en la zona rugosa (tuberosidad) de la cara externa de la 2.ª costilla?", ["Serrato anterior", "Escaleno anterior", "Pectoral menor", "Pectoral mayor", "Subclavio"],
   "La 2.ª costilla es atípica: es el doble de larga que la 1.ª y en su cara externa tiene la tuberosidad de la primera digitación del serrato anterior. El pectoral menor se inserta en las costillas 3.ª–5.ª y el escaleno anterior y el subclavio en la 1.ª."))

T("sk-b9394d0e",
  ("With the arms hanging at the sides, the inferior angle of the scapula corresponds to which vertebral level?", ["T2", "T10", "T7", "L1", "T4"],
   "The superior angle of the scapula lies at T2, the medial end of its spine at T3 and the inferior angle at T7. The inferior angle is used as a surface landmark in chest examination and thoracentesis."),
  ("Bras le long du corps, l'angle inférieur de la scapula correspond à quel niveau vertébral ?", ["T2", "T10", "T7", "L1", "T4"],
   "L'angle supérieur de la scapula est en regard de T2, l'extrémité médiale de l'épine de T3 et l'angle inférieur de T7. L'angle inférieur sert de repère pour l'examen du thorax et la ponction pleurale."),
  ("Welcher Wirbelhöhe entspricht der untere Schulterblattwinkel bei hängenden Armen?", ["T2", "T10", "T7", "L1", "T4"],
   "Der obere Schulterblattwinkel liegt in Höhe T2, das mediale Ende der Spina in Höhe T3 und der untere Winkel in Höhe T7. Der untere Winkel dient als Orientierungspunkt bei Thoraxuntersuchung und Pleurapunktion."),
  ("Con los brazos colgando, ¿a qué nivel vertebral corresponde el ángulo inferior de la escápula?", ["T2", "T10", "T7", "L1", "T4"],
   "El ángulo superior de la escápula está a nivel de T2, el extremo medial de la espina de T3 y el ángulo inferior de T7. El ángulo inferior se usa como referencia en la exploración del tórax y la toracocentesis."))

T("sk-c935a47a",
  ("With which part of the ulna does the trochlea of the humerus articulate?", ["Head of ulna", "Radial notch", "Trochlear notch", "Ulnar styloid process", "Ulnar tuberosity"],
   "The pulley-shaped trochlea of the humerus fits into the trochlear notch of the ulna between the olecranon and coronoid process, forming the humeroulnar hinge joint. The capitulum articulates with the head of the radius."),
  ("Avec quelle partie de l'ulna s'articule la trochlée humérale ?", ["Tête de l'ulna", "Incisure radiale", "Incisure trochléaire", "Processus styloïde de l'ulna", "Tubérosité ulnaire"],
   "La trochlée humérale, en forme de poulie, s'emboîte dans l'incisure trochléaire de l'ulna entre l'olécrâne et le processus coronoïde, formant l'articulation huméro-ulnaire en charnière. Le capitulum s'articule avec la tête radiale."),
  ("Mit welchem Teil der Ulna artikuliert die Trochlea humeri?", ["Caput ulnae", "Incisura radialis", "Incisura trochlearis", "Processus styloideus ulnae", "Tuberositas ulnae"],
   "Die rollenförmige Trochlea humeri greift in die Incisura trochlearis der Ulna zwischen Olecranon und Processus coronoideus und bildet das Humeroulnargelenk (Scharniergelenk). Das Capitulum artikuliert mit dem Radiusköpfchen."),
  ("¿Con qué parte del cúbito se articula la tróclea humeral?", ["Cabeza del cúbito", "Escotadura radial", "Escotadura troclear", "Apófisis estiloides cubital", "Tuberosidad cubital"],
   "La tróclea humeral, en forma de polea, encaja en la escotadura troclear del cúbito entre el olécranon y la coronoides, formando la articulación humerocubital en bisagra. El cóndilo humeral se articula con la cabeza del radio."))

T("sk-fffabda4",
  ("Which muscle attaches to the radial tuberosity?", ["Brachialis", "Biceps brachii", "Triceps brachii", "Supinator", "Pronator teres"],
   "The biceps brachii tendon attaches to the radial tuberosity below the neck of the radius, which makes it a powerful supinator. Brachialis attaches to the ulnar tuberosity, pronator teres to the middle of the lateral surface of the radius."),
  ("Quel muscle s'insère sur la tubérosité radiale ?", ["Brachial", "Biceps brachial", "Triceps brachial", "Supinateur", "Rond pronateur"],
   "Le tendon du biceps brachial s'insère sur la tubérosité radiale sous le col du radius, ce qui en fait un puissant supinateur. Le brachial s'insère sur la tubérosité ulnaire, le rond pronateur au milieu de la face latérale du radius."),
  ("Welcher Muskel setzt an der Tuberositas radii an?", ["M. brachialis", "M. biceps brachii", "M. triceps brachii", "M. supinator", "M. pronator teres"],
   "Die Bizepssehne setzt an der Tuberositas radii unterhalb des Radiushalses an; daher ist der Bizeps ein kräftiger Supinator. Der M. brachialis setzt an der Tuberositas ulnae, der M. pronator teres an der Mitte der Radiusaußenfläche an."),
  ("¿Qué músculo se inserta en la tuberosidad del radio?", ["Braquial", "Bíceps braquial", "Tríceps braquial", "Supinador", "Pronador redondo"],
   "El tendón del bíceps braquial se inserta en la tuberosidad del radio, bajo el cuello, lo que lo convierte en un potente supinador. El braquial se inserta en la tuberosidad cubital y el pronador redondo en la mitad de la cara lateral del radio."))

T("sk-afaac4c9",
  ("Which are the lateral (radial) attachments of the flexor retinaculum?", ["Tubercle of the scaphoid and tubercle of the trapezium", "Capitate and trapezoid", "Base of 1st metacarpal and lunate", "Pisiform and hook of hamate", "Radial styloid and lunate"],
   "The flexor retinaculum attaches laterally to the tubercles of the scaphoid and trapezium and medially to the pisiform and hook of hamate, forming the roof of the carpal tunnel."),
  ("Quelles sont les insertions latérales (radiales) du rétinaculum des fléchisseurs ?", ["Tubercule du scaphoïde et tubercule du trapèze", "Capitatum et trapézoïde", "Base du 1er métacarpien et lunatum", "Pisiforme et hamulus de l'hamatum", "Styloïde radiale et lunatum"],
   "Le rétinaculum des fléchisseurs s'insère en dehors sur les tubercules du scaphoïde et du trapèze, en dedans sur le pisiforme et l'hamulus de l'hamatum ; il forme le toit du canal carpien."),
  ("Welches sind die lateralen (radialen) Ansätze des Retinaculum flexorum?", ["Tuberculum ossis scaphoidei und Tuberculum ossis trapezii", "Kopfbein und kleines Vieleckbein", "Basis des 1. Mittelhandknochens und Mondbein", "Erbsenbein und Hamulus ossis hamati", "Processus styloideus radii und Mondbein"],
   "Das Retinaculum flexorum setzt lateral an den Höckern von Kahnbein und großem Vieleckbein, medial an Erbsenbein und Hamulus ossis hamati an und bildet das Dach des Karpaltunnels."),
  ("¿Cuáles son las inserciones laterales (radiales) del retináculo flexor?", ["Tubérculo del escafoides y tubérculo del trapecio", "Grande y trapezoide", "Base del 1.er metacarpiano y semilunar", "Pisiforme y gancho del ganchoso", "Estiloides radial y semilunar"],
   "El retináculo flexor se inserta lateralmente en los tubérculos del escafoides y del trapecio y medialmente en el pisiforme y el gancho del ganchoso, formando el techo del túnel carpiano."))

T("sk-63af94e3",
  ("The skin dimples at the lower back (dimples of Venus) mark which bony landmark, at which vertebral level?", ["Highest point of the iliac crest – L4", "Posterior superior iliac spine – S2", "Anterior superior iliac spine – L4", "Ischial spine – S3", "Ischial tuberosity – S4"],
   "The dimples over the sacroiliac region mark the PSIS and correspond to S2; this level is also where the dural sac and subarachnoid space end."),
  ("Les fossettes cutanées du bas du dos (fossettes de Vénus) repèrent quel relief osseux et à quel niveau vertébral ?", ["Point le plus haut de la crête iliaque – L4", "Épine iliaque postéro-supérieure – S2", "Épine iliaque antéro-supérieure – L4", "Épine ischiatique – S3", "Tubérosité ischiatique – S4"],
   "Les fossettes de la région sacro-iliaque repèrent les EIPS et correspondent à S2, niveau où se terminent aussi le sac dural et l'espace sous-arachnoïdien."),
  ("Welchen Knochenpunkt markieren die Hautgrübchen am unteren Rücken (Venusgrübchen), und in welcher Höhe?", ["Höchster Punkt des Beckenkamms – L4", "Spina iliaca posterior superior – S2", "Spina iliaca anterior superior – L4", "Spina ischiadica – S3", "Tuber ischiadicum – S4"],
   "Die Grübchen über der Iliosakralregion markieren die SIPS in Höhe S2; in dieser Höhe enden auch Duralsack und Subarachnoidalraum."),
  ("¿Qué referencia ósea marcan los hoyuelos de la parte baja de la espalda (hoyuelos de Venus) y a qué nivel vertebral?", ["Punto más alto de la cresta ilíaca – L4", "Espina ilíaca posterosuperior – S2", "Espina ilíaca anterosuperior – L4", "Espina isquiática – S3", "Tuberosidad isquiática – S4"],
   "Los hoyuelos de la región sacroilíaca marcan las EIPS y corresponden a S2, nivel en el que también terminan el saco dural y el espacio subaracnoideo."))

T("sk-736237ad",
  ("Which muscle attaches to the pectineal line of the femur?", ["Vastus medialis", "Gluteus maximus", "Adductor longus", "Iliopsoas", "Pectineus"],
   "Pectineus arises from the pecten pubis and attaches to the pectineal line below the lesser trochanter. Iliopsoas attaches to the lesser trochanter, gluteus maximus to the gluteal tuberosity."),
  ("Quel muscle s'insère sur la ligne pectinée du fémur ?", ["Vaste médial", "Grand fessier", "Long adducteur", "Ilio-psoas", "Pectiné"],
   "Le pectiné naît du pecten du pubis et s'insère sur la ligne pectinée sous le petit trochanter. L'ilio-psoas s'insère sur le petit trochanter, le grand fessier sur la tubérosité glutéale."),
  ("Welcher Muskel setzt an der Linea pectinea des Femurs an?", ["M. vastus medialis", "M. gluteus maximus", "M. adductor longus", "M. iliopsoas", "M. pectineus"],
   "Der M. pectineus entspringt am Pecten ossis pubis und setzt an der Linea pectinea unterhalb des Trochanter minor an. Der M. iliopsoas setzt am Trochanter minor, der M. gluteus maximus an der Tuberositas glutea an."),
  ("¿Qué músculo se inserta en la línea pectínea del fémur?", ["Vasto medial", "Glúteo mayor", "Aductor largo", "Iliopsoas", "Pectíneo"],
   "El pectíneo nace de la cresta pectínea del pubis y se inserta en la línea pectínea, bajo el trocánter menor. El iliopsoas se inserta en el trocánter menor y el glúteo mayor en la tuberosidad glútea."))
