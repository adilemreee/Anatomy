KIND = "questions"
SYSTEM = "skeletal"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("sk-fecd544c",
  ("Which muscle attaches to the adductor tubercle of the femur?", ["Adductor magnus (hamstring part)", "Vastus medialis", "Adductor longus", "Gracilis", "Semimembranosus"],
   "The vertical (hamstring) part of adductor magnus, which comes from the ischial tuberosity, attaches to the adductor tubercle above the medial epicondyle; this part is supplied by the tibial part of the sciatic nerve."),
  ("Quel muscle s'insère sur le tubercule de l'adducteur du fémur ?", ["Grand adducteur (partie ischio-jambière)", "Vaste médial", "Long adducteur", "Gracile", "Semi-membraneux"],
   "La partie verticale (ischio-jambière) du grand adducteur, venue de la tubérosité ischiatique, s'insère sur le tubercule de l'adducteur au-dessus de l'épicondyle médial ; elle est innervée par la partie tibiale du nerf sciatique."),
  ("Welcher Muskel setzt am Tuberculum adductorium des Femurs an?", ["M. adductor magnus (ischiokruraler Teil)", "M. vastus medialis", "M. adductor longus", "M. gracilis", "M. semimembranosus"],
   "Der senkrechte (ischiokrurale) Teil des M. adductor magnus vom Sitzbeinhöcker setzt am Tuberculum adductorium oberhalb des Epicondylus medialis an; er wird vom tibialen Anteil des N. ischiadicus innerviert."),
  ("¿Qué músculo se inserta en el tubérculo del aductor del fémur?", ["Aductor mayor (porción isquiotibial)", "Vasto medial", "Aductor largo", "Grácil", "Semimembranoso"],
   "La porción vertical (isquiotibial) del aductor mayor, procedente de la tuberosidad isquiática, se inserta en el tubérculo del aductor por encima del epicóndilo medial; la inerva la porción tibial del ciático."))

T("sk-d46b7610",
  ("To which pit on the femoral head does the ligament of the head of the femur attach?", ["Trochanteric fossa", "Acetabular fossa", "Fovea of the head of the femur", "Intertrochanteric line", "Intercondylar fossa"],
   "The ligament of the head of the femur runs from the acetabular notch to the fovea capitis in the middle of the femoral head; the acetabular branch of the obturator artery runs within it."),
  ("Dans quelle fossette de la tête fémorale s'insère le ligament de la tête fémorale ?", ["Fosse trochantérique", "Fosse acétabulaire", "Fovéa de la tête fémorale", "Ligne intertrochantérique", "Fosse intercondylaire"],
   "Le ligament de la tête fémorale va de l'incisure acétabulaire à la fovéa capitis au centre de la tête ; il contient la branche acétabulaire de l'artère obturatrice."),
  ("In welcher Grube des Femurkopfs setzt das Lig. capitis femoris an?", ["Fossa trochanterica", "Fossa acetabuli", "Fovea capitis femoris", "Linea intertrochanterica", "Fossa intercondylaris"],
   "Das Lig. capitis femoris zieht von der Incisura acetabuli zur Fovea capitis in der Mitte des Femurkopfs; in ihm verläuft der R. acetabularis der A. obturatoria."),
  ("¿En qué fosita de la cabeza femoral se inserta el ligamento de la cabeza del fémur?", ["Fosa trocantérea", "Fosa acetabular", "Fóvea de la cabeza del fémur", "Línea intertrocantérea", "Fosa intercondílea"],
   "El ligamento de la cabeza del fémur va de la escotadura acetabular a la fóvea en el centro de la cabeza femoral; por él discurre la rama acetabular de la arteria obturatriz."))

T("sk-3e7d0e42",
  ("Which feature distinguishes the female pelvis from the male pelvis?", ["The pelvic inlet is heart-shaped.", "The subpubic angle is wider.", "The ischial spines project further inwards.", "The pelvis is deeper and narrower.", "The sacrum is longer and narrower."],
   "The female pelvis is wider and shallower: the inlet is oval, the subpubic angle wider than 90°, the sacrum short and broad and the ischial spines less prominent. The other options are features of the male pelvis."),
  ("Quelle caractéristique distingue le bassin féminin du bassin masculin ?", ["Le détroit supérieur est en forme de cœur.", "L'angle sous-pubien est plus ouvert.", "Les épines ischiatiques sont plus saillantes en dedans.", "Le bassin est plus profond et plus étroit.", "Le sacrum est plus long et plus étroit."],
   "Le bassin féminin est plus large et moins profond : détroit supérieur ovale, angle sous-pubien supérieur à 90°, sacrum court et large, épines ischiatiques peu saillantes. Les autres propositions caractérisent le bassin masculin."),
  ("Welches Merkmal unterscheidet das weibliche vom männlichen Becken?", ["Der Beckeneingang ist herzförmig.", "Der Schambogenwinkel ist weiter.", "Die Sitzbeinstacheln ragen stärker nach innen.", "Das Becken ist tiefer und enger.", "Das Kreuzbein ist länger und schmaler."],
   "Das weibliche Becken ist breiter und flacher: Eingang oval, Schambogenwinkel über 90°, Kreuzbein kurz und breit, Sitzbeinstacheln wenig vorspringend. Die anderen Antworten beschreiben das männliche Becken."),
  ("¿Qué rasgo distingue la pelvis femenina de la masculina?", ["El estrecho superior tiene forma de corazón.", "El ángulo subpubiano es más amplio.", "Las espinas isquiáticas sobresalen más hacia dentro.", "La pelvis es más profunda y estrecha.", "El sacro es más largo y estrecho."],
   "La pelvis femenina es más ancha y menos profunda: estrecho superior oval, ángulo subpubiano mayor de 90°, sacro corto y ancho y espinas isquiáticas poco prominentes. Las demás opciones son rasgos masculinos."))

T("sk-54c3cd19",
  ("With which of the following bones does the talus NOT articulate?", ["Tibia", "Cuboid", "Fibula", "Navicular", "Calcaneus"],
   "The talus articulates above with the tibia and fibula (ankle joint), below with the calcaneus (subtalar joint) and in front with the navicular (talonavicular joint). The cuboid lies in front of the calcaneus."),
  ("Avec lequel de ces os le talus ne s'articule-t-il PAS ?", ["Tibia", "Cuboïde", "Fibula", "Naviculaire", "Calcanéus"],
   "Le talus s'articule en haut avec le tibia et la fibula (talo-crurale), en bas avec le calcanéus (sous-talienne) et en avant avec le naviculaire (talo-naviculaire). Le cuboïde est en avant du calcanéus."),
  ("Mit welchem der folgenden Knochen artikuliert der Talus NICHT?", ["Tibia", "Würfelbein", "Fibula", "Kahnbein", "Calcaneus"],
   "Der Talus artikuliert oben mit Tibia und Fibula (oberes Sprunggelenk), unten mit dem Calcaneus (unteres Sprunggelenk) und vorn mit dem Kahnbein. Das Würfelbein liegt vor dem Calcaneus."),
  ("¿Con cuál de los siguientes huesos NO se articula el astrágalo?", ["Tibia", "Cuboides", "Peroné", "Navicular", "Calcáneo"],
   "El astrágalo se articula arriba con la tibia y el peroné (tobillo), abajo con el calcáneo (subastragalina) y delante con el navicular. El cuboides está delante del calcáneo."))

T("sk-d6509a0e",
  ("Which is the largest of the three cuneiform bones?", ["Medial cuneiform", "Intermediate cuneiform", "Cuboid", "Lateral cuneiform", "All three are the same size"],
   "The medial cuneiform is the largest and the intermediate the smallest. The shortness of the intermediate cuneiform allows the base of the 2nd metatarsal to lock between the medial and lateral cuneiforms."),
  ("Quel est le plus grand des trois cunéiformes ?", ["Cunéiforme médial", "Cunéiforme intermédiaire", "Cuboïde", "Cunéiforme latéral", "Les trois ont la même taille"],
   "Le cunéiforme médial est le plus grand, l'intermédiaire le plus petit. La brièveté de l'intermédiaire permet à la base du 2e métatarsien de s'encastrer entre les cunéiformes médial et latéral."),
  ("Welches der drei Keilbeine ist das größte?", ["Mediales Keilbein", "Mittleres Keilbein", "Würfelbein", "Laterales Keilbein", "Alle drei sind gleich groß"],
   "Das mediale Keilbein ist das größte, das mittlere das kleinste. Durch die Kürze des mittleren Keilbeins kann sich die Basis des 2. Mittelfußknochens zwischen medialem und lateralem Keilbein verankern."),
  ("¿Cuál es el mayor de los tres cuneiformes?", ["Cuneiforme medial", "Cuneiforme intermedio", "Cuboides", "Cuneiforme lateral", "Los tres tienen el mismo tamaño"],
   "El cuneiforme medial es el mayor y el intermedio el menor. La cortedad del intermedio permite que la base del 2.º metatarsiano quede encajada entre los cuneiformes medial y lateral."))

T("sk-75fb3209",
  ("A construction worker who fell from a height has a heel fracture. Which associated injury must always be looked for?", ["Thoracolumbar vertebral fracture", "Distal radius fracture", "Skull fracture", "Patella fracture", "Clavicle fracture"],
   "In a fall onto the feet the load is transmitted axially to the spine; about 10% of calcaneal fractures are accompanied by a thoracolumbar (especially L1) compression fracture, which must not be missed."),
  ("Un ouvrier tombé d'une hauteur présente une fracture du talon. Quelle lésion associée faut-il toujours rechercher ?", ["Fracture vertébrale thoraco-lombale", "Fracture du radius distal", "Fracture du crâne", "Fracture de la patella", "Fracture de la clavicule"],
   "Lors d'une chute sur les pieds, la charge se transmet axialement au rachis ; environ 10 % des fractures du calcanéus s'accompagnent d'un tassement thoraco-lombal (surtout L1), à ne pas méconnaître."),
  ("Ein Bauarbeiter hat nach einem Sturz aus der Höhe eine Fersenbeinfraktur. Nach welcher Begleitverletzung muss stets gesucht werden?", ["Thorakolumbale Wirbelfraktur", "Distale Radiusfraktur", "Schädelfraktur", "Patellafraktur", "Klavikulafraktur"],
   "Beim Sturz auf die Füße wird die Last axial auf die Wirbelsäule übertragen; etwa 10 % der Kalkaneusfrakturen gehen mit einer thorakolumbalen (besonders L1) Kompressionsfraktur einher, die nicht übersehen werden darf."),
  ("Un albañil que cayó desde altura tiene una fractura de talón. ¿Qué lesión asociada debe buscarse siempre?", ["Fractura vertebral toracolumbar", "Fractura del radio distal", "Fractura de cráneo", "Fractura de rótula", "Fractura de clavícula"],
   "En una caída sobre los pies la carga se transmite axialmente a la columna; alrededor del 10 % de las fracturas de calcáneo se acompañan de un aplastamiento toracolumbar (sobre todo L1), que no debe pasarse por alto."))

T("sk-32bbaef0",
  ("A 1st rib fracture is found after a road traffic accident. What should this finding suggest first?", ["Osteoporosis", "A simple, trivial fracture", "High-energy trauma and injury to the subclavian artery and brachial plexus beneath it", "Pathological fracture (metastasis)", "Costochondritis"],
   "The 1st rib is short, thick and well protected, so it breaks only with high-energy trauma. Since the subclavian artery, subclavian vein and lower trunk of the brachial plexus cross it, vascular and nerve injury must be looked for."),
  ("Une fracture de la 1re côte est découverte après un accident de la route. Que doit-elle évoquer d'abord ?", ["Une ostéoporose", "Une fracture simple sans gravité", "Un traumatisme violent et une lésion de l'artère subclavière et du plexus brachial sous-jacents", "Une fracture pathologique (métastase)", "Une chondrite costale"],
   "La 1re côte, courte, épaisse et protégée, ne se fracture que lors de traumatismes violents. L'artère et la veine subclavières et le tronc inférieur du plexus brachial la croisant, il faut rechercher une lésion vasculo-nerveuse."),
  ("Nach einem Verkehrsunfall wird eine Fraktur der 1. Rippe festgestellt. Woran sollte man zuerst denken?", ["Osteoporose", "Eine einfache, harmlose Fraktur", "Hochrasanztrauma und Verletzung von A. subclavia und Plexus brachialis darunter", "Pathologische Fraktur (Metastase)", "Kostochondritis"],
   "Die 1. Rippe ist kurz, kräftig und gut geschützt und bricht nur bei Hochrasanztraumen. Da A. und V. subclavia sowie der untere Primärstrang des Plexus brachialis über sie ziehen, muss nach Gefäß- und Nervenverletzungen gesucht werden."),
  ("Tras un accidente de tráfico se detecta una fractura de la 1.ª costilla. ¿Qué debe sugerir primero?", ["Osteoporosis", "Una fractura simple sin importancia", "Traumatismo de alta energía y lesión de la arteria subclavia y el plexo braquial subyacentes", "Fractura patológica (metástasis)", "Costocondritis"],
   "La 1.ª costilla es corta, gruesa y protegida, y solo se fractura con traumatismos de alta energía. Como la cruzan la arteria y la vena subclavias y el tronco inferior del plexo braquial, hay que buscar lesiones vasculares y nerviosas."))

T("sk-26bde07f",
  ("Which canals connect the Haversian canals with each other and with the periosteum at right angles?", ["Canaliculi", "Sharpey's fibres", "Lacunae", "Volkmann's canals", "Nutrient canal"],
   "Volkmann's canals run perpendicular to the long axis of the bone and connect the vessels of the Haversian canals with each other and with periosteal and endosteal vessels. Canaliculi are fine channels containing the processes of osteocytes."),
  ("Quels canaux relient perpendiculairement les canaux de Havers entre eux et au périoste ?", ["Canalicules", "Fibres de Sharpey", "Lacunes", "Canaux de Volkmann", "Canal nourricier"],
   "Les canaux de Volkmann, perpendiculaires au grand axe de l'os, relient les vaisseaux des canaux de Havers entre eux et aux vaisseaux périostés et endostés. Les canalicules sont de fins conduits contenant les prolongements des ostéocytes."),
  ("Welche Kanäle verbinden die Havers-Kanäle rechtwinklig miteinander und mit dem Periost?", ["Canaliculi", "Sharpey-Fasern", "Lakunen", "Volkmann-Kanäle", "Canalis nutricius"],
   "Volkmann-Kanäle verlaufen quer zur Längsachse und verbinden die Gefäße der Havers-Kanäle untereinander sowie mit Periost- und Endostgefäßen. Canaliculi sind feine Kanälchen für die Fortsätze der Osteozyten."),
  ("¿Qué conductos unen perpendicularmente los conductos de Havers entre sí y con el periostio?", ["Canalículos", "Fibras de Sharpey", "Lagunas", "Conductos de Volkmann", "Conducto nutricio"],
   "Los conductos de Volkmann son perpendiculares al eje del hueso y unen los vasos de los conductos de Havers entre sí y con los vasos periósticos y endósticos. Los canalículos son conductillos que alojan las prolongaciones de los osteocitos."))

T("sk-eddc1dd9",
  ("Which is the most common type of growth plate fracture in children (Salter–Harris)?", ["Type II", "Type I", "Type IV", "Type III", "Type V"],
   "In a Salter–Harris type II fracture the line passes through the growth plate and exits through the metaphysis (Thurston–Holland fragment); it is the most common type and has a good prognosis. Type V (crush) has the worst prognosis and is often recognised late."),
  ("Quel est le type le plus fréquent de fracture du cartilage de croissance chez l'enfant (Salter–Harris) ?", ["Type II", "Type I", "Type IV", "Type III", "Type V"],
   "Dans le type II de Salter–Harris, le trait traverse le cartilage de croissance et ressort par la métaphyse (fragment de Thurston–Holland) ; c'est le plus fréquent et son pronostic est bon. Le type V (écrasement) est le plus grave et souvent reconnu tardivement."),
  ("Welche Epiphysenfugenfraktur (Salter–Harris) ist bei Kindern am häufigsten?", ["Typ II", "Typ I", "Typ IV", "Typ III", "Typ V"],
   "Bei Salter–Harris Typ II verläuft die Frakturlinie durch die Fuge und tritt durch die Metaphyse aus (Thurston-Holland-Fragment); sie ist am häufigsten und prognostisch günstig. Typ V (Stauchung) hat die schlechteste Prognose und wird oft spät erkannt."),
  ("¿Cuál es el tipo más frecuente de fractura de la placa de crecimiento en niños (Salter–Harris)?", ["Tipo II", "Tipo I", "Tipo IV", "Tipo III", "Tipo V"],
   "En el tipo II de Salter–Harris el trazo atraviesa la placa y sale por la metáfisis (fragmento de Thurston–Holland); es el más frecuente y de buen pronóstico. El tipo V (compresión) es el de peor pronóstico y suele diagnosticarse tarde."))

T("sk-05b258c2",
  ("Which nerve does NOT pass through the common tendinous ring (annulus of Zinn)?", ["Oculomotor nerve", "Abducens nerve", "Nasociliary nerve", "Trochlear nerve", "Optic nerve"],
   "Through the annulus of Zinn pass the optic nerve and ophthalmic artery (optic canal), the two branches of the oculomotor nerve, the nasociliary nerve and the abducens nerve. The trochlear, frontal and lacrimal nerves pass above and outside the ring."),
  ("Quel nerf ne passe PAS dans l'anneau tendineux commun (anneau de Zinn) ?", ["Nerf oculomoteur", "Nerf abducens", "Nerf nasociliaire", "Nerf trochléaire", "Nerf optique"],
   "Par l'anneau de Zinn passent le nerf optique et l'artère ophtalmique (canal optique), les deux branches de l'oculomoteur, le nasociliaire et l'abducens. Le trochléaire, le frontal et le lacrymal passent au-dessus, hors de l'anneau."),
  ("Welcher Nerv zieht NICHT durch den Anulus tendineus communis (Zinn-Ring)?", ["N. oculomotorius", "N. abducens", "N. nasociliaris", "N. trochlearis", "N. opticus"],
   "Durch den Zinn-Ring ziehen N. opticus und A. ophthalmica (Canalis opticus), die beiden Äste des N. oculomotorius, der N. nasociliaris und der N. abducens. N. trochlearis, frontalis und lacrimalis verlaufen oberhalb, außerhalb des Rings."),
  ("¿Qué nervio NO pasa por el anillo tendinoso común (anillo de Zinn)?", ["Nervio oculomotor", "Nervio abducens", "Nervio nasociliar", "Nervio troclear", "Nervio óptico"],
   "Por el anillo de Zinn pasan el nervio óptico y la arteria oftálmica (conducto óptico), las dos ramas del oculomotor, el nasociliar y el abducens. El troclear, el frontal y el lagrimal pasan por encima, fuera del anillo."))

T("sk-7c5f6944",
  ("Which opening connects the pterygopalatine fossa with the nasal cavity?", ["Inferior orbital fissure", "Pterygomaxillary fissure", "Greater palatine canal", "Sphenopalatine foramen", "Pterygoid canal"],
   "The sphenopalatine foramen connects the pterygopalatine fossa with the upper back part of the nasal cavity; the sphenopalatine artery and nasal nerves pass through it. The pterygomaxillary fissure opens into the infratemporal fossa."),
  ("Quel orifice relie la fosse ptérygo-palatine à la cavité nasale ?", ["Fissure orbitaire inférieure", "Fissure ptérygo-maxillaire", "Grand canal palatin", "Foramen sphéno-palatin", "Canal ptérygoïdien"],
   "Le foramen sphéno-palatin relie la fosse ptérygo-palatine à la partie postéro-supérieure de la cavité nasale ; l'artère sphéno-palatine et les nerfs nasaux le traversent. La fissure ptérygo-maxillaire ouvre sur la fosse infratemporale."),
  ("Welche Öffnung verbindet die Flügelgaumengrube mit der Nasenhöhle?", ["Fissura orbitalis inferior", "Fissura pterygomaxillaris", "Canalis palatinus major", "Foramen sphenopalatinum", "Canalis pterygoideus"],
   "Das Foramen sphenopalatinum verbindet die Flügelgaumengrube mit dem hinteren oberen Teil der Nasenhöhle; A. sphenopalatina und Nasennerven ziehen hindurch. Die Fissura pterygomaxillaris öffnet sich zur Fossa infratemporalis."),
  ("¿Qué orificio comunica la fosa pterigopalatina con la cavidad nasal?", ["Fisura orbitaria inferior", "Fisura pterigomaxilar", "Conducto palatino mayor", "Agujero esfenopalatino", "Conducto pterigoideo"],
   "El agujero esfenopalatino comunica la fosa pterigopalatina con la parte posterosuperior de la cavidad nasal; por él pasan la arteria esfenopalatina y los nervios nasales. La fisura pterigomaxilar se abre a la fosa infratemporal."))

T("sk-1960c9a2",
  ("Which nerves unite to form the nerve of the pterygoid canal (Vidian nerve)?", ["Chorda tympani and lingual nerve", "Deep petrosal nerve and internal carotid nerve", "Greater and lesser petrosal nerves", "Lesser petrosal nerve and chorda tympani", "Greater petrosal nerve and deep petrosal nerve"],
   "The greater petrosal nerve (parasympathetic fibres of VII) and the deep petrosal nerve (sympathetic fibres from the carotid plexus) unite to form the Vidian nerve, which reaches the pterygopalatine ganglion."),
  ("Quels nerfs s'unissent pour former le nerf du canal ptérygoïdien (nerf vidien) ?", ["Corde du tympan et nerf lingual", "Nerf pétreux profond et nerf carotidien interne", "Grand et petit nerfs pétreux", "Petit nerf pétreux et corde du tympan", "Grand nerf pétreux et nerf pétreux profond"],
   "Le grand nerf pétreux (fibres parasympathiques du VII) et le nerf pétreux profond (fibres sympathiques du plexus carotidien) s'unissent pour former le nerf vidien, qui gagne le ganglion ptérygo-palatin."),
  ("Welche Nerven vereinigen sich zum N. canalis pterygoidei (N. Vidianus)?", ["Chorda tympani und N. lingualis", "N. petrosus profundus und N. caroticus internus", "N. petrosus major und N. petrosus minor", "N. petrosus minor und Chorda tympani", "N. petrosus major und N. petrosus profundus"],
   "Der N. petrosus major (parasympathische Fasern des VII) und der N. petrosus profundus (sympathische Fasern aus dem Karotisplexus) vereinigen sich zum N. Vidianus, der zum Ganglion pterygopalatinum zieht."),
  ("¿Qué nervios se unen para formar el nervio del conducto pterigoideo (nervio vidiano)?", ["Cuerda del tímpano y nervio lingual", "Nervio petroso profundo y nervio carotídeo interno", "Nervios petrosos mayor y menor", "Nervio petroso menor y cuerda del tímpano", "Nervio petroso mayor y nervio petroso profundo"],
   "El nervio petroso mayor (fibras parasimpáticas del VII) y el petroso profundo (fibras simpáticas del plexo carotídeo) se unen para formar el nervio vidiano, que llega al ganglio pterigopalatino."))

T("sk-1f5f4838",
  ("Premature closure of the sagittal suture (craniosynostosis) leads to which head shape?", ["Trigonocephaly (triangular forehead)", "Brachycephaly (short, wide head)", "Oxycephaly (tower skull)", "Plagiocephaly (asymmetric head)", "Scaphocephaly (long, narrow head)"],
   "Growth stops perpendicular to the closed suture and increases parallel to it. In sagittal synostosis the head cannot grow sideways and lengthens front to back (scaphocephaly); it is the most common craniosynostosis. Metopic synostosis causes trigonocephaly."),
  ("La fermeture prématurée de la suture sagittale (craniosténose) entraîne quelle forme de crâne ?", ["Trigonocéphalie (front triangulaire)", "Brachycéphalie (crâne court et large)", "Oxycéphalie (crâne en tour)", "Plagiocéphalie (crâne asymétrique)", "Scaphocéphalie (crâne long et étroit)"],
   "La croissance s'arrête perpendiculairement à la suture fermée et augmente parallèlement à elle. Dans la synostose sagittale, le crâne ne peut s'élargir et s'allonge d'avant en arrière (scaphocéphalie) ; c'est la craniosténose la plus fréquente. La synostose métopique donne une trigonocéphalie."),
  ("Welche Kopfform entsteht durch einen vorzeitigen Verschluss der Pfeilnaht (Kraniosynostose)?", ["Trigonozephalie (dreieckige Stirn)", "Brachyzephalie (kurzer, breiter Kopf)", "Oxyzephalie (Turmschädel)", "Plagiozephalie (asymmetrischer Kopf)", "Skaphozephalie (langer, schmaler Kopf)"],
   "Senkrecht zur verschlossenen Naht hört das Wachstum auf, parallel dazu nimmt es zu. Bei Sagittalnahtsynostose kann der Kopf nicht in die Breite wachsen und wird lang (Skaphozephalie); sie ist die häufigste Kraniosynostose. Die Stirnnahtsynostose verursacht eine Trigonozephalie."),
  ("¿Qué forma de cabeza produce el cierre prematuro de la sutura sagital (craneosinostosis)?", ["Trigonocefalia (frente triangular)", "Braquicefalia (cabeza corta y ancha)", "Oxicefalia (cráneo en torre)", "Plagiocefalia (cabeza asimétrica)", "Escafocefalia (cabeza larga y estrecha)"],
   "El crecimiento se detiene en perpendicular a la sutura cerrada y aumenta en paralelo a ella. En la sinostosis sagital la cabeza no puede ensancharse y se alarga (escafocefalia); es la craneosinostosis más frecuente. La sinostosis metópica produce trigonocefalia."))

T("sk-3de5d43b",
  ("Where does the fracture line run in a Le Fort I fracture?", ["Through the orbits, separating the face completely from the skull.", "Through the neck of the mandible.", "Pyramidally through the nasal root and orbital floor.", "Horizontally across the maxilla just above the floor of the nose.", "Only through the zygomatic arch."],
   "Le Fort I separates the lower maxilla carrying the tooth sockets (floating palate). Le Fort II is a pyramidal fracture (nasal root, orbital floor), Le Fort III a craniofacial separation (through the orbits and zygomatic arches)."),
  ("Où passe le trait de fracture dans une fracture de Le Fort I ?", ["À travers les orbites, séparant complètement la face du crâne.", "Par le col de la mandibule.", "De façon pyramidale par la racine du nez et le plancher orbitaire.", "Horizontalement à travers le maxillaire, juste au-dessus du plancher des fosses nasales.", "Uniquement par l'arcade zygomatique."],
   "Le Fort I détache la partie basse du maxillaire portant les alvéoles dentaires (palais flottant). Le Fort II est pyramidale (racine du nez, plancher orbitaire), Le Fort III une disjonction cranio-faciale (à travers les orbites et les arcades zygomatiques)."),
  ("Wo verläuft die Frakturlinie bei einer Le-Fort-I-Fraktur?", ["Durch die Augenhöhlen; das Gesicht wird vollständig vom Schädel getrennt.", "Durch den Unterkieferhals.", "Pyramidenförmig durch Nasenwurzel und Orbitaboden.", "Waagerecht durch den Oberkiefer knapp oberhalb des Nasenbodens.", "Nur durch den Jochbogen."],
   "Le Fort I trennt den unteren Oberkiefer mit den Zahnfächern ab (schwimmender Gaumen). Le Fort II ist pyramidenförmig (Nasenwurzel, Orbitaboden), Le Fort III eine kraniofaziale Absprengung (durch Augenhöhlen und Jochbögen)."),
  ("¿Por dónde pasa el trazo de fractura en una fractura de Le Fort I?", ["Por las órbitas, separando por completo la cara del cráneo.", "Por el cuello de la mandíbula.", "De forma piramidal por la raíz nasal y el suelo orbitario.", "Horizontalmente a través del maxilar, justo por encima del suelo nasal.", "Solo por el arco cigomático."],
   "Le Fort I separa la parte inferior del maxilar con los alvéolos dentarios (paladar flotante). Le Fort II es piramidal (raíz nasal, suelo orbitario) y Le Fort III una disyunción craneofacial (a través de las órbitas y los arcos cigomáticos)."))

T("sk-0ba9ff30",
  ("Between which vertebrae does the C5 spinal nerve exit?", ["Between C4 and C5", "Between C7 and T1", "Between C6 and C7", "Between C5 and C6", "Between C3 and C4"],
   "In the cervical region there are 8 nerves and 7 vertebrae; nerves C1–C7 exit above the vertebra of the same number and C8 exits between C7 and T1. A C5–C6 disc herniation therefore compresses the C6 root."),
  ("Entre quelles vertèbres sort le nerf spinal C5 ?", ["Entre C4 et C5", "Entre C7 et T1", "Entre C6 et C7", "Entre C5 et C6", "Entre C3 et C4"],
   "À l'étage cervical, il y a 8 nerfs pour 7 vertèbres ; les nerfs C1 à C7 sortent au-dessus de la vertèbre de même numéro, C8 entre C7 et T1. Une hernie C5–C6 comprime donc la racine C6."),
  ("Zwischen welchen Wirbeln tritt der Spinalnerv C5 aus?", ["Zwischen C4 und C5", "Zwischen C7 und T1", "Zwischen C6 und C7", "Zwischen C5 und C6", "Zwischen C3 und C4"],
   "Im Halsbereich gibt es 8 Nerven und 7 Wirbel; C1–C7 treten oberhalb des gleichnamigen Wirbels aus, C8 zwischen C7 und T1. Ein Bandscheibenvorfall C5–C6 komprimiert daher die Wurzel C6."),
  ("¿Entre qué vértebras sale el nervio espinal C5?", ["Entre C4 y C5", "Entre C7 y T1", "Entre C6 y C7", "Entre C5 y C6", "Entre C3 y C4"],
   "En la región cervical hay 8 nervios y 7 vértebras; los nervios C1–C7 salen por encima de la vértebra del mismo número y C8 entre C7 y T1. Por eso una hernia C5–C6 comprime la raíz C6."))

T("sk-0380b366",
  ("At about what age does the Y-shaped (triradiate) cartilage joining the three bones of the acetabulum ossify?", ["1–2 years", "After 40 years", "15–17 years", "25–30 years", "5–7 years"],
   "The ilium, ischium and pubis are separated in the acetabulum by a Y-shaped cartilage; it ossifies at the end of puberty (15–17 years), making the hip bone a single bone."),
  ("Vers quel âge s'ossifie le cartilage en Y (triradié) qui unit les trois os de l'acétabulum ?", ["1–2 ans", "Après 40 ans", "15–17 ans", "25–30 ans", "5–7 ans"],
   "L'ilium, l'ischium et le pubis sont séparés dans l'acétabulum par un cartilage en Y ; il s'ossifie à la fin de la puberté (15–17 ans), et l'os coxal devient un os unique."),
  ("In welchem Alter verknöchert die Y-Fuge, die die drei Knochen der Hüftpfanne verbindet?", ["1–2 Jahre", "Nach dem 40. Lebensjahr", "15–17 Jahre", "25–30 Jahre", "5–7 Jahre"],
   "Darmbein, Sitzbein und Schambein werden in der Hüftpfanne durch die Y-Fuge getrennt; sie verknöchert am Ende der Pubertät (15–17 Jahre), und das Hüftbein wird zu einem einzigen Knochen."),
  ("¿Aproximadamente a qué edad se osifica el cartílago en Y (trirradiado) que une los tres huesos del acetábulo?", ["1–2 años", "Después de los 40", "15–17 años", "25–30 años", "5–7 años"],
   "El ilion, el isquion y el pubis están separados en el acetábulo por un cartílago en Y; se osifica al final de la pubertad (15–17 años) y el coxal se convierte en un solo hueso."))

T("sk-57138661",
  ("Which is the narrowest anteroposterior diameter of the birth canal?", ["Diagonal conjugate", "Interspinous diameter", "Obstetric conjugate", "Anatomical (true) conjugate", "Transverse diameter"],
   "The obstetric conjugate is the distance between the promontory and the nearest point on the back of the symphysis and is the narrowest anteroposterior diameter of the pelvic inlet. On examination the diagonal conjugate is measured and 1.5–2 cm subtracted."),
  ("Quel est le plus petit diamètre antéro-postérieur de la filière pelvienne ?", ["Conjugué diagonal", "Diamètre bi-épineux", "Conjugué obstétrical", "Conjugué anatomique (vrai)", "Diamètre transverse"],
   "Le conjugué obstétrical est la distance entre le promontoire et le point le plus proche de la face postérieure de la symphyse ; c'est le plus petit diamètre antéro-postérieur du détroit supérieur. On mesure le conjugué diagonal et on retranche 1,5–2 cm."),
  ("Welcher ist der engste gerade (anteroposteriore) Durchmesser des Geburtskanals?", ["Conjugata diagonalis", "Interspinaldurchmesser", "Conjugata obstetrica", "Conjugata anatomica (vera)", "Querdurchmesser"],
   "Die Conjugata obstetrica ist der Abstand zwischen Promontorium und nächstem Punkt der Symphysenhinterfläche und der engste gerade Durchmesser des Beckeneingangs. Gemessen wird die Conjugata diagonalis, von der 1,5–2 cm abgezogen werden."),
  ("¿Cuál es el diámetro anteroposterior más estrecho del canal del parto?", ["Conjugado diagonal", "Diámetro biespinoso", "Conjugado obstétrico", "Conjugado anatómico (verdadero)", "Diámetro transverso"],
   "El conjugado obstétrico es la distancia entre el promontorio y el punto más cercano de la cara posterior de la sínfisis y es el diámetro anteroposterior más estrecho del estrecho superior. En la exploración se mide el conjugado diagonal y se restan 1,5–2 cm."))

T("sk-082df539",
  ("Which muscle attaches to the trochanteric fossa of the femur?", ["Quadratus femoris", "Gluteus medius", "Piriformis", "Iliopsoas", "Obturator externus"],
   "The trochanteric fossa, on the inner surface of the greater trochanter, is the attachment of obturator externus. Piriformis attaches to the upper border of the greater trochanter and quadratus femoris to the quadrate tubercle."),
  ("Quel muscle s'insère dans la fosse trochantérique du fémur ?", ["Carré fémoral", "Moyen fessier", "Piriforme", "Ilio-psoas", "Obturateur externe"],
   "La fosse trochantérique, à la face médiale du grand trochanter, reçoit l'obturateur externe. Le piriforme s'insère sur le bord supérieur du grand trochanter et le carré fémoral sur le tubercule carré."),
  ("Welcher Muskel setzt in der Fossa trochanterica des Femurs an?", ["M. quadratus femoris", "M. gluteus medius", "M. piriformis", "M. iliopsoas", "M. obturatorius externus"],
   "Die Fossa trochanterica an der Innenseite des Trochanter major ist der Ansatz des M. obturatorius externus. Der M. piriformis setzt am Oberrand des Trochanter major, der M. quadratus femoris am Tuberculum quadratum an."),
  ("¿Qué músculo se inserta en la fosa trocantérea del fémur?", ["Cuadrado femoral", "Glúteo medio", "Piriforme", "Iliopsoas", "Obturador externo"],
   "La fosa trocantérea, en la cara interna del trocánter mayor, es la inserción del obturador externo. El piriforme se inserta en el borde superior del trocánter mayor y el cuadrado femoral en el tubérculo cuadrado."))

T("sk-2b105744",
  ("What is the main reason for the high risk of avascular necrosis after fractures of the neck of the talus?", ["The growth plate of the talus stays open in adults", "The talus is supplied only by the fibular artery", "The talus has many muscle attachments", "Blood reaches the body of the talus retrogradely from the neck", "The periosteum of the talus is thick"],
   "Most of the talus is covered by articular cartilage and it has no muscle attachments; blood flows to the body mainly through branches of the artery of the tarsal canal, retrogradely from the neck. A neck fracture cuts these vessels and causes necrosis of the body (Hawkins)."),
  ("Quelle est la principale raison du risque élevé de nécrose avasculaire après une fracture du col du talus ?", ["Le cartilage de croissance du talus reste ouvert chez l'adulte", "Le talus n'est vascularisé que par l'artère fibulaire", "Le talus a de nombreuses insertions musculaires", "Le sang arrive au corps du talus de façon rétrograde depuis le col", "Le périoste du talus est épais"],
   "Le talus est en grande partie recouvert de cartilage et sans insertion musculaire ; le corps est vascularisé surtout par les branches de l'artère du canal du tarse, de façon rétrograde depuis le col. Une fracture du col interrompt ces vaisseaux et provoque une nécrose du corps (Hawkins)."),
  ("Was ist der Hauptgrund für das hohe Nekroserisiko nach Talushalsfrakturen?", ["Die Wachstumsfuge des Talus bleibt beim Erwachsenen offen", "Der Talus wird nur von der A. fibularis versorgt", "Am Talus setzen viele Muskeln an", "Das Blut erreicht den Taluskörper retrograd vom Hals her", "Das Periost des Talus ist dick"],
   "Der Talus ist größtenteils von Gelenkknorpel überzogen und hat keine Muskelansätze; der Körper wird vor allem über Äste der A. canalis tarsi retrograd vom Hals her versorgt. Eine Halsfraktur unterbricht diese Gefäße und führt zur Nekrose des Körpers (Hawkins)."),
  ("¿Cuál es la razón principal del alto riesgo de necrosis avascular tras las fracturas del cuello del astrágalo?", ["La placa de crecimiento del astrágalo permanece abierta en el adulto", "El astrágalo solo lo irriga la arteria peronea", "El astrágalo tiene muchas inserciones musculares", "La sangre llega al cuerpo del astrágalo de forma retrógrada desde el cuello", "El periostio del astrágalo es grueso"],
   "El astrágalo está cubierto en gran parte por cartílago y carece de inserciones musculares; el cuerpo recibe sangre sobre todo por ramas de la arteria del conducto tarsiano, de forma retrógrada desde el cuello. Una fractura del cuello interrumpe estos vasos y causa necrosis del cuerpo (Hawkins)."))

T("sk-6d6ca7d5",
  ("In a Bennett fracture, which muscle pulls the main (distal) fragment proximally and laterally?", ["Adductor pollicis", "Flexor pollicis longus", "Abductor pollicis longus", "Opponens pollicis", "Extensor pollicis longus"],
   "A Bennett fracture is an intra-articular fracture-dislocation of the base of the 1st metacarpal. The small medial fragment, held by the anterior oblique ligament, stays in place; APL, attached to the base of the 1st metacarpal, pulls the main fragment proximally and laterally."),
  ("Dans la fracture de Bennett, quel muscle attire le fragment principal (distal) en haut et en dehors ?", ["Adducteur du pouce", "Long fléchisseur du pouce", "Long abducteur du pouce", "Opposant du pouce", "Long extenseur du pouce"],
   "La fracture de Bennett est une fracture-luxation articulaire de la base du 1er métacarpien. Le petit fragment médial, retenu par le ligament oblique antérieur, reste en place ; le long abducteur du pouce, inséré sur la base du 1er métacarpien, attire le fragment principal en haut et en dehors."),
  ("Welcher Muskel zieht bei der Bennett-Fraktur das Hauptfragment (distal) nach proximal und lateral?", ["M. adductor pollicis", "M. flexor pollicis longus", "M. abductor pollicis longus", "M. opponens pollicis", "M. extensor pollicis longus"],
   "Die Bennett-Fraktur ist eine intraartikuläre Luxationsfraktur der Basis des 1. Mittelhandknochens. Das kleine mediale Fragment bleibt, vom vorderen schrägen Band gehalten, an Ort; der an der Basis ansetzende M. abductor pollicis longus zieht das Hauptfragment nach proximal und lateral."),
  ("En la fractura de Bennett, ¿qué músculo tracciona del fragmento principal (distal) hacia proximal y lateral?", ["Aductor del pulgar", "Flexor largo del pulgar", "Abductor largo del pulgar", "Oponente del pulgar", "Extensor largo del pulgar"],
   "La fractura de Bennett es una fractura-luxación intraarticular de la base del 1.er metacarpiano. El pequeño fragmento medial, sujeto por el ligamento oblicuo anterior, queda en su sitio; el abductor largo del pulgar, insertado en la base, tracciona del fragmento principal hacia proximal y lateral."))

T("sk-786f3165",
  ("A motorcyclist has a pelvic ring fracture and is haemodynamically unstable. What is the most common source of bleeding in pelvic fractures?", ["Presacral and pelvic venous plexuses and fractured bone surfaces", "Femoral artery", "Abdominal aorta", "Inferior vena cava", "Common iliac artery"],
   "About 80–90% of bleeding in pelvic fractures comes from the venous plexuses and fractured cancellous bone; closing the ring with a pelvic binder is therefore the first step. Arterial bleeding is treated by angioembolisation."),
  ("Un motard présente une fracture de l'anneau pelvien avec instabilité hémodynamique. Quelle est la source la plus fréquente du saignement ?", ["Plexus veineux présacrés et pelviens et surfaces osseuses fracturées", "Artère fémorale", "Aorte abdominale", "Veine cave inférieure", "Artère iliaque commune"],
   "Environ 80–90 % des hémorragies des fractures du bassin proviennent des plexus veineux et de l'os spongieux fracturé ; la fermeture de l'anneau par une ceinture pelvienne est donc la première mesure. Le saignement artériel se traite par artério-embolisation."),
  ("Ein Motorradfahrer hat eine Beckenringfraktur und ist kreislaufinstabil. Was ist die häufigste Blutungsquelle bei Beckenfrakturen?", ["Präsakrale und pelvine Venengeflechte sowie Frakturflächen", "A. femoralis", "Aorta abdominalis", "V. cava inferior", "A. iliaca communis"],
   "Etwa 80–90 % der Blutungen bei Beckenfrakturen stammen aus den Venenplexus und der frakturierten Spongiosa; der Verschluss des Rings mit einer Beckenschlinge ist daher die erste Maßnahme. Arterielle Blutungen werden angioembolisiert."),
  ("Un motorista presenta una fractura del anillo pélvico con inestabilidad hemodinámica. ¿Cuál es la fuente de sangrado más frecuente en las fracturas pélvicas?", ["Plexos venosos presacros y pélvicos y superficies óseas fracturadas", "Arteria femoral", "Aorta abdominal", "Vena cava inferior", "Arteria ilíaca común"],
   "Alrededor del 80–90 % de las hemorragias de las fracturas pélvicas proceden de los plexos venosos y del hueso esponjoso fracturado; por eso cerrar el anillo con un cinturón pélvico es la primera medida. El sangrado arterial se trata con angioembolización."))
