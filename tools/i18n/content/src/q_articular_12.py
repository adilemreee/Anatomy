KIND = "questions"
SYSTEM = "articular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("ar-e5efb4d3",
  ("Which bone is the keystone of the lateral longitudinal arch of the foot?", ["Cuboid", "Medial cuneiform", "Head of the 5th metatarsal", "Head of the talus", "Navicular"],
   "The keystone of the medial longitudinal arch is the head of the talus, that of the lateral arch the cuboid. The lateral arch is low and close to the ground."),
  ("Quel os est la clé de voûte de l'arche longitudinale latérale du pied ?", ["Cuboïde", "Cunéiforme médial", "Tête du 5e métatarsien", "Tête du talus", "Naviculaire"],
   "La clé de voûte de l'arche longitudinale médiale est la tête du talus, celle de l'arche latérale le cuboïde. L'arche latérale est basse et proche du sol."),
  ("Welcher Knochen ist der Schlussstein des lateralen Längsgewölbes des Fußes?", ["Würfelbein", "Inneres Keilbein", "Kopf des 5. Mittelfußknochens", "Taluskopf", "Kahnbein"],
   "Schlussstein des medialen Längsgewölbes ist der Taluskopf, des lateralen das Würfelbein. Das laterale Gewölbe ist flach und liegt dem Boden nahe."),
  ("¿Qué hueso es la clave del arco longitudinal lateral del pie?", ["Cuboides", "Cuña medial", "Cabeza del 5.º metatarsiano", "Cabeza del astrágalo", "Navicular"],
   "La clave del arco longitudinal medial es la cabeza del astrágalo y la del lateral el cuboides. El arco lateral es bajo y está cerca del suelo."))

T("ar-ca751a1b",
  ("What is the most common cause of acquired flatfoot in adults?", ["Paralysis of tibialis anterior", "Tear of fibularis longus", "Achilles tendon rupture", "Shortening of the plantar fascia", "Tibialis posterior tendon dysfunction"],
   "Tibialis posterior is the most important dynamic support of the medial arch; degeneration and failure of its tendon lead to collapse of the medial arch and valgus of the heel."),
  ("Quelle est la cause la plus fréquente de pied plat acquis de l'adulte ?", ["Paralysie du tibial antérieur", "Rupture du long fibulaire", "Rupture du tendon calcanéen", "Rétraction de l'aponévrose plantaire", "Insuffisance du tendon du tibial postérieur"],
   "Le tibial postérieur est le principal soutien dynamique de l'arche médiale ; la dégénérescence et l'insuffisance de son tendon entraînent l'effondrement de l'arche et le valgus de l'arrière-pied."),
  ("Was ist die häufigste Ursache des erworbenen Plattfußes beim Erwachsenen?", ["Lähmung des M. tibialis anterior", "Riss des M. fibularis longus", "Achillessehnenruptur", "Verkürzung der Plantarfaszie", "Insuffizienz der Tibialis-posterior-Sehne"],
   "Der M. tibialis posterior ist die wichtigste dynamische Stütze des medialen Gewölbes; Degeneration und Insuffizienz seiner Sehne führen zum Einsinken des Gewölbes und zur Valgusstellung der Ferse."),
  ("¿Cuál es la causa más frecuente de pie plano adquirido del adulto?", ["Parálisis del tibial anterior", "Rotura del peroneo largo", "Rotura del tendón de Aquiles", "Acortamiento de la fascia plantar", "Insuficiencia del tendón del tibial posterior"],
   "El tibial posterior es el principal soporte dinámico del arco medial; la degeneración e insuficiencia de su tendón provocan el hundimiento del arco y el valgo del talón."))

T("ar-a91411e8",
  ("A patient who fell onto a plantarflexed foot has midfoot swelling and plantar ecchymosis; the radiograph shows a gap between the bases of the 1st and 2nd metatarsals. What is the most likely diagnosis?", ["Chopart dislocation", "Calcaneal fracture", "Lateral ankle ligament sprain", "Jones fracture", "Lisfranc (tarsometatarsal) injury"],
   "Plantar ecchymosis and a gap between the 1st and 2nd metatarsal bases are typical signs of a Lisfranc ligament injury; about one in five is missed at first presentation, so it needs careful assessment."),
  ("Un patient tombé sur un pied en flexion plantaire présente un gonflement du médio-pied et une ecchymose plantaire ; la radiographie montre un écart entre les bases des 1er et 2e métatarsiens. Quel est le diagnostic le plus probable ?", ["Luxation de Chopart", "Fracture du calcanéus", "Entorse du ligament latéral de la cheville", "Fracture de Jones", "Lésion de Lisfranc (tarso-métatarsienne)"],
   "L'ecchymose plantaire et l'écart entre les bases des 1er et 2e métatarsiens sont typiques d'une lésion du ligament de Lisfranc ; environ une sur cinq passe inaperçue au premier examen, d'où la nécessité d'une évaluation attentive."),
  ("Ein Patient ist auf den plantarflektierten Fuß gestürzt; Mittelfußschwellung und plantares Hämatom, im Röntgen ein Spalt zwischen den Basen des 1. und 2. Mittelfußknochens. Wahrscheinlichste Diagnose?", ["Chopart-Luxation", "Kalkaneusfraktur", "Außenbandverletzung des Sprunggelenks", "Jones-Fraktur", "Lisfranc-Verletzung (tarsometatarsal)"],
   "Plantares Hämatom und Spalt zwischen den Basen des 1. und 2. Mittelfußknochens sind typisch für eine Lisfranc-Bandverletzung; etwa jede fünfte wird bei der Erstvorstellung übersehen und muss daher sorgfältig abgeklärt werden."),
  ("Un paciente que cayó sobre el pie en flexión plantar presenta tumefacción del mediopié y equimosis plantar; la radiografía muestra separación entre las bases del 1.º y 2.º metatarsianos. ¿Cuál es el diagnóstico más probable?", ["Luxación de Chopart", "Fractura de calcáneo", "Esguince del ligamento lateral del tobillo", "Fractura de Jones", "Lesión de Lisfranc (tarsometatarsiana)"],
   "La equimosis plantar y la separación entre las bases del 1.º y 2.º metatarsianos son típicas de la lesión del ligamento de Lisfranc; aproximadamente una de cada cinco pasa desapercibida en la primera consulta, por lo que exige una valoración cuidadosa."))

T("ar-fe1c13ee",
  ("Which type of dens fracture has the highest risk of non-union?", ["Type I (tip of the dens)", "Type II (base of the dens)", "Hangman's fracture", "Type III (extending into the body of the axis)", "Jefferson fracture"],
   "In the Anderson–D'Alonzo classification a type II fracture crosses the base of the dens; non-union is frequent in this poorly vascularised region. Type III extends into the body of the axis and usually heals."),
  ("Quel type de fracture de la dent de l'axis a le plus haut risque de pseudarthrose ?", ["Type I (pointe de la dent)", "Type II (base de la dent)", "Fracture du pendu", "Type III (s'étendant au corps de l'axis)", "Fracture de Jefferson"],
   "Dans la classification d'Anderson et D'Alonzo, le type II traverse la base de la dent ; la pseudarthrose y est fréquente car la région est mal vascularisée. Le type III s'étend au corps de l'axis et consolide habituellement."),
  ("Welcher Densfrakturtyp hat das höchste Pseudarthroserisiko?", ["Typ I (Densspitze)", "Typ II (Densbasis)", "Hangman-Fraktur", "Typ III (bis in den Axiskörper)", "Jefferson-Fraktur"],
   "In der Klassifikation nach Anderson und D'Alonzo verläuft Typ II durch die Densbasis; in diesem schlecht durchbluteten Bereich ist die Pseudarthroserate hoch. Typ III reicht in den Axiskörper und heilt meist."),
  ("¿Qué tipo de fractura de la odontoides tiene mayor riesgo de seudoartrosis?", ["Tipo I (punta de la odontoides)", "Tipo II (base de la odontoides)", "Fractura del ahorcado", "Tipo III (se extiende al cuerpo del axis)", "Fractura de Jefferson"],
   "En la clasificación de Anderson y D'Alonzo el tipo II atraviesa la base de la odontoides; en esta zona poco vascularizada la seudoartrosis es frecuente. El tipo III llega al cuerpo del axis y suele consolidar."))

T("ar-55929b2d",
  ("Where does the sensory innervation of the facet (zygapophyseal) joints come from?", ["Anterior rami of the spinal nerves", "Sinuvertebral (recurrent meningeal) nerve", "Sympathetic trunk", "Medial branches of the posterior rami of the spinal nerves", "Lateral branches of the posterior rami"],
   "Each facet joint is supplied by the medial branches of the posterior rami of two adjacent levels. In facet pain these branches are targeted with blocks or radiofrequency ablation."),
  ("D'où vient l'innervation sensitive des articulations zygapophysaires ?", ["Rameaux antérieurs des nerfs spinaux", "Nerf sinu-vertébral (méningé récurrent)", "Tronc sympathique", "Rameaux médiaux des rameaux postérieurs des nerfs spinaux", "Rameaux latéraux des rameaux postérieurs"],
   "Chaque articulation zygapophysaire est innervée par les rameaux médiaux des rameaux postérieurs de deux étages voisins. Dans la douleur facettaire, on réalise sur eux des blocs ou une thermocoagulation par radiofréquence."),
  ("Woher stammt die sensible Innervation der Facettengelenke (Artt. zygapophysiales)?", ["Rr. anteriores der Spinalnerven", "N. sinuvertebralis (R. meningeus recurrens)", "Truncus sympathicus", "Rr. mediales der Rr. posteriores der Spinalnerven", "Rr. laterales der Rr. posteriores"],
   "Jedes Facettengelenk wird von den Rr. mediales der Rr. posteriores zweier benachbarter Segmente versorgt. Beim Facettenschmerz werden diese Äste blockiert oder mit Radiofrequenz denerviert."),
  ("¿De dónde procede la inervación sensitiva de las articulaciones facetarias (cigapofisarias)?", ["Ramos anteriores de los nervios espinales", "Nervio sinuvertebral (meníngeo recurrente)", "Tronco simpático", "Ramos mediales de los ramos posteriores de los nervios espinales", "Ramos laterales de los ramos posteriores"],
   "Cada articulación facetaria recibe los ramos mediales de los ramos posteriores de dos niveles vecinos. En el dolor facetario se bloquean o se tratan con radiofrecuencia."))

T("ar-dd990884",
  ("The sphenomandibular ligament is a remnant of which pharyngeal arch structure?", ["Cartilage of the 1st pharyngeal arch (Meckel's cartilage)", "Notochord", "3rd pharyngeal arch", "4th pharyngeal arch", "Cartilage of the 2nd pharyngeal arch (Reichert)"],
   "Meckel's cartilage gives rise to the malleus, incus and sphenomandibular ligament. Reichert's cartilage (2nd arch) forms the stapes, styloid process and stylohyoid ligament."),
  ("Le ligament sphéno-mandibulaire est un vestige de quelle structure des arcs pharyngiens ?", ["Cartilage du 1er arc pharyngien (cartilage de Meckel)", "Notochorde", "3e arc pharyngien", "4e arc pharyngien", "Cartilage du 2e arc pharyngien (Reichert)"],
   "Le cartilage de Meckel donne le marteau, l'enclume et le ligament sphéno-mandibulaire. Le cartilage de Reichert (2e arc) forme l'étrier, le processus styloïde et le ligament stylo-hyoïdien."),
  ("Das Lig. sphenomandibulare ist ein Rest welcher Schlundbogenstruktur?", ["Knorpel des 1. Schlundbogens (Meckel-Knorpel)", "Chorda dorsalis", "3. Schlundbogen", "4. Schlundbogen", "Knorpel des 2. Schlundbogens (Reichert)"],
   "Aus dem Meckel-Knorpel entstehen Hammer, Amboss und Lig. sphenomandibulare. Der Reichert-Knorpel (2. Bogen) bildet Steigbügel, Processus styloideus und Lig. stylohyoideum."),
  ("El ligamento esfenomandibular es un resto de ¿qué estructura de los arcos faríngeos?", ["Cartílago del 1.er arco faríngeo (cartílago de Meckel)", "Notocorda", "3.er arco faríngeo", "4.º arco faríngeo", "Cartílago del 2.º arco faríngeo (Reichert)"],
   "Del cartílago de Meckel derivan el martillo, el yunque y el ligamento esfenomandibular. El cartílago de Reichert (2.º arco) forma el estribo, la apófisis estiloides y el ligamento estilohioideo."))

T("ar-bead98f0",
  ("Which forearm ligament has fibres running in the opposite direction to those of the interosseous membrane?", ["Radial collateral ligament", "Annular ligament of the radius", "Oblique cord", "Quadrate ligament", "Dorsal radio-ulnar ligament"],
   "Fibres of the interosseous membrane run downwards and medially from radius to ulna, whereas the oblique cord descends laterally from the ulnar tuberosity to the radius. It supports the proximal radio-ulnar joint."),
  ("Quel ligament de l'avant-bras a des fibres orientées en sens inverse de celles de la membrane interosseuse ?", ["Ligament collatéral radial", "Ligament annulaire du radius", "Corde oblique", "Ligament carré", "Ligament radio-ulnaire dorsal"],
   "Les fibres de la membrane interosseuse descendent en dedans du radius vers l'ulna, tandis que la corde oblique descend en dehors de la tubérosité ulnaire vers le radius. Elle renforce l'articulation radio-ulnaire proximale."),
  ("Welches Unterarmband verläuft mit seinen Fasern entgegengesetzt zur Membrana interossea?", ["Lig. collaterale radiale", "Lig. anulare radii", "Chorda obliqua", "Lig. quadratum", "Lig. radioulnare dorsale"],
   "Die Fasern der Membrana interossea ziehen vom Radius nach distal-medial zur Ulna, die Chorda obliqua dagegen von der Tuberositas ulnae nach distal-lateral zum Radius. Sie stützt das proximale Radioulnargelenk."),
  ("¿Qué ligamento del antebrazo tiene fibras orientadas en sentido opuesto a las de la membrana interósea?", ["Ligamento colateral radial", "Ligamento anular del radio", "Cuerda oblicua", "Ligamento cuadrado", "Ligamento radiocubital dorsal"],
   "Las fibras de la membrana interósea descienden en sentido medial del radio al cúbito, mientras que la cuerda oblicua desciende en sentido lateral de la tuberosidad cubital al radio. Refuerza la articulación radiocubital proximal."))

T("ar-5ba07cbd",
  ("What is the ligament-poor area on the palmar side of the capitate, through which perilunate dislocations occur, called?", ["Anatomical snuffbox", "Space of Parona", "Carpal tunnel", "Guyon's canal", "Space of Poirier"],
   "The space of Poirier is the weak area between the radioscaphocapitate and radiolunate ligaments; in perilunate dislocation the capitate separates from the lunate here."),
  ("Comment appelle-t-on la zone pauvre en ligaments, à la face palmaire du capitatum, par où se produisent les luxations périlunaires ?", ["Tabatière anatomique", "Espace de Parona", "Canal carpien", "Canal de Guyon", "Espace de Poirier"],
   "L'espace de Poirier est la zone de faiblesse entre les ligaments radio-scapho-capital et radio-lunaire ; dans la luxation périlunaire, le capitatum s'y sépare du lunatum."),
  ("Wie heißt die bandarme Zone palmar am Kapitatum, über die perilunäre Luxationen entstehen?", ["Tabatière", "Parona-Raum", "Karpaltunnel", "Loge de Guyon", "Poirier-Raum"],
   "Der Poirier-Raum ist die Schwachstelle zwischen radioskaphokapitalem und radiolunärem Band; bei der perilunären Luxation trennt sich hier das Kapitatum vom Lunatum."),
  ("¿Cómo se llama la zona pobre en ligamentos de la cara palmar del hueso grande por donde se producen las luxaciones perisemilunares?", ["Tabaquera anatómica", "Espacio de Parona", "Túnel carpiano", "Canal de Guyon", "Espacio de Poirier"],
   "El espacio de Poirier es la zona débil entre los ligamentos radioescafogrande y radiosemilunar; en la luxación perisemilunar el hueso grande se separa aquí del semilunar."))

T("ar-31d4bdc3",
  ("Tears in which part of the TFCC do not heal because it is avascular, and require debridement?", ["Dorsal radio-ulnar ligament", "Peripheral (ulnar margin)", "Central (middle of the disc)", "Palmar radio-ulnar ligament", "ECU tendon sheath"],
   "Only the outer margin of the TFCC is well vascularised. Central tears do not heal and are treated by arthroscopic debridement, whereas peripheral tears are repaired."),
  ("Les déchirures de quelle partie du TFCC ne cicatrisent pas, car avasculaire, et nécessitent un débridement ?", ["Ligament radio-ulnaire dorsal", "Périphérique (bord ulnaire)", "Centrale (partie moyenne du disque)", "Ligament radio-ulnaire palmaire", "Gaine du tendon de l'ECU"],
   "Seul le bord périphérique du TFCC est bien vascularisé. Les déchirures centrales ne cicatrisent pas et sont traitées par débridement arthroscopique, les périphériques par suture."),
  ("Risse in welchem Teil des TFCC heilen wegen fehlender Durchblutung nicht und erfordern ein Débridement?", ["Dorsales radioulnares Band", "Peripher (ulnarer Rand)", "Zentral (Mitte des Diskus)", "Palmares radioulnares Band", "Sehnenscheide des ECU"],
   "Nur der äußere Rand des TFCC ist gut durchblutet. Zentrale Risse heilen nicht und werden arthroskopisch débridiert, periphere werden genäht."),
  ("Las roturas de ¿qué parte del CFCT no cicatrizan por ser avasculares y requieren desbridamiento?", ["Ligamento radiocubital dorsal", "Periférica (borde cubital)", "Central (parte media del disco)", "Ligamento radiocubital palmar", "Vaina del tendón del ECU"],
   "Solo el borde periférico del CFCT está bien vascularizado. Las roturas centrales no cicatrizan y se tratan con desbridamiento artroscópico; las periféricas se reparan."))

T("ar-c3fb2f81",
  ("Which condition, seen in people whose ulna is longer than the radius (ulnar positive variance), causes wear of the TFCC and lunate?", ["Madelung deformity", "Kienböck disease", "Carpal tunnel syndrome", "Ulnocarpal impaction syndrome", "De Quervain tenosynovitis"],
   "In ulnar positive variance the ulnar head presses on the TFCC and lunate, causing ulnar-sided pain and cartilage damage of the lunate. Kienböck disease is associated rather with ulnar negative variance."),
  ("Quelle affection, observée lorsque l'ulna est plus longue que le radius (variance ulnaire positive), use le TFCC et le lunatum ?", ["Déformation de Madelung", "Maladie de Kienböck", "Syndrome du canal carpien", "Syndrome d'impaction ulno-carpienne", "Ténosynovite de De Quervain"],
   "En variance ulnaire positive, la tête ulnaire comprime le TFCC et le lunatum, d'où douleur du bord ulnaire et lésions cartilagineuses du lunatum. La maladie de Kienböck est plutôt associée à une variance ulnaire négative."),
  ("Welches Krankheitsbild bei Ulna-Plus-Variante (Elle länger als Speiche) führt zum Verschleiß von TFCC und Lunatum?", ["Madelung-Deformität", "Morbus Kienböck", "Karpaltunnelsyndrom", "Ulnokarpales Impaktionssyndrom", "Tendovaginitis de Quervain"],
   "Bei Ulna-Plus-Variante drückt der Ulnakopf auf TFCC und Lunatum; es entstehen ulnarseitige Schmerzen und Knorpelschäden am Lunatum. Der Morbus Kienböck ist eher mit einer Ulna-Minus-Variante verbunden."),
  ("¿Qué cuadro, propio de personas con el cúbito más largo que el radio (varianza cubital positiva), desgasta el CFCT y el semilunar?", ["Deformidad de Madelung", "Enfermedad de Kienböck", "Síndrome del túnel carpiano", "Síndrome de impactación cubitocarpiana", "Tenosinovitis de De Quervain"],
   "En la varianza cubital positiva la cabeza del cúbito comprime el CFCT y el semilunar, con dolor del lado cubital y daño del cartílago del semilunar. La enfermedad de Kienböck se asocia más bien a varianza cubital negativa."))

T("ar-e6d0e58d",
  ("Which is the most important stabilising ligament of the thumb carpometacarpal joint?", ["Anterior oblique ligament ('beak ligament')", "Radial collateral ligament", "Volar plate", "Dorsoradial ligament", "Intermetacarpal ligament"],
   "The anterior oblique ligament runs from the tubercle of the trapezium to the anteromedial base of the 1st metacarpal; it is also the ligament that holds the small medial fragment in place in a Bennett fracture."),
  ("Quel est le ligament stabilisateur le plus important de l'articulation trapézo-métacarpienne ?", ["Ligament oblique antérieur (« ligament bec »)", "Ligament collatéral radial", "Plaque palmaire", "Ligament dorso-radial", "Ligament intermétacarpien"],
   "Le ligament oblique antérieur va du tubercule du trapèze à la partie antéro-médiale de la base du 1er métacarpien ; c'est aussi lui qui maintient en place le petit fragment médial dans la fracture de Bennett."),
  ("Welches ist das wichtigste stabilisierende Band des Daumensattelgelenks?", ["Vorderes schräges Band („Beak ligament“)", "Radiales Kollateralband", "Palmare Platte", "Dorsoradiales Band", "Intermetakarpales Band"],
   "Das vordere schräge Band zieht vom Tuberculum des Trapeziums zur ulnopalmaren Basis des 1. Mittelhandknochens; es hält bei der Bennett-Fraktur auch das kleine ulnare Fragment an seinem Platz."),
  ("¿Cuál es el ligamento estabilizador más importante de la articulación trapeciometacarpiana?", ["Ligamento oblicuo anterior («ligamento pico»)", "Ligamento colateral radial", "Placa volar", "Ligamento dorsorradial", "Ligamento intermetacarpiano"],
   "El ligamento oblicuo anterior va del tubérculo del trapecio a la parte anteromedial de la base del 1.er metacarpiano; también es el que mantiene en su sitio el pequeño fragmento medial en la fractura de Bennett."))

T("ar-17c5390c",
  ("In a Stener lesion, which structure becomes interposed between the torn ulnar collateral ligament and its attachment?", ["Volar plate", "Adductor pollicis aponeurosis", "Abductor pollicis brevis tendon", "Extensor pollicis longus tendon", "Sesamoid bone"],
   "When the ulnar collateral ligament of the thumb MCP joint ruptures, its end may come to lie on top of the adductor aponeurosis; the interposed aponeurosis prevents healing, so surgery is needed."),
  ("Dans la lésion de Stener, quelle structure s'interpose entre le ligament collatéral ulnaire rompu et son insertion ?", ["Plaque palmaire", "Aponévrose de l'adducteur du pouce", "Tendon du court abducteur du pouce", "Tendon du long extenseur du pouce", "Os sésamoïde"],
   "Lorsque le ligament collatéral ulnaire de la MCP du pouce se rompt, son extrémité peut se retrouver au-dessus de l'aponévrose de l'adducteur ; cette interposition empêche la cicatrisation et impose la chirurgie."),
  ("Welche Struktur schiebt sich bei der Stener-Läsion zwischen das abgerissene ulnare Kollateralband und seinen Ansatz?", ["Palmare Platte", "Aponeurose des M. adductor pollicis", "Sehne des M. abductor pollicis brevis", "Sehne des M. extensor pollicis longus", "Sesambein"],
   "Reißt das ulnare Kollateralband des Daumengrundgelenks, kann sein Ende auf der Adduktoraponeurose zu liegen kommen; die zwischengelagerte Aponeurose verhindert die Heilung, daher ist eine Operation nötig."),
  ("En la lesión de Stener, ¿qué estructura se interpone entre el ligamento colateral cubital roto y su inserción?", ["Placa volar", "Aponeurosis del aductor del pulgar", "Tendón del abductor corto del pulgar", "Tendón del extensor largo del pulgar", "Hueso sesamoideo"],
   "Cuando se rompe el colateral cubital de la MCF del pulgar, su extremo puede quedar sobre la aponeurosis del aductor; la aponeurosis interpuesta impide la cicatrización, por lo que se necesita cirugía."))

T("ar-dbeaf9b7",
  ("Which structure dislocates in a Monteggia fracture?", ["Head of the humerus", "Lunate", "Distal radio-ulnar joint", "Head of the ulna", "Head of the radius (proximal radio-ulnar joint)"],
   "In a Monteggia fracture a fracture of the proximal third of the ulna is accompanied by dislocation of the radial head. In a Galeazzi fracture a radial shaft fracture is accompanied by dislocation of the distal radio-ulnar joint."),
  ("Quelle structure se luxe dans la fracture de Monteggia ?", ["Tête humérale", "Lunatum", "Articulation radio-ulnaire distale", "Tête ulnaire", "Tête radiale (radio-ulnaire proximale)"],
   "Dans la fracture de Monteggia, une fracture du tiers proximal de l'ulna s'associe à une luxation de la tête radiale. Dans la fracture de Galeazzi, une fracture diaphysaire du radius s'associe à une luxation radio-ulnaire distale."),
  ("Welche Struktur luxiert bei der Monteggia-Fraktur?", ["Humeruskopf", "Lunatum", "Distales Radioulnargelenk", "Ulnakopf", "Radiuskopf (proximales Radioulnargelenk)"],
   "Bei der Monteggia-Fraktur ist eine Fraktur des proximalen Ulnadrittels mit einer Radiuskopfluxation verbunden. Bei der Galeazzi-Fraktur geht eine Radiusschaftfraktur mit einer Luxation im distalen Radioulnargelenk einher."),
  ("¿Qué estructura se luxa en la fractura de Monteggia?", ["Cabeza del húmero", "Semilunar", "Articulación radiocubital distal", "Cabeza del cúbito", "Cabeza del radio (radiocubital proximal)"],
   "En la fractura de Monteggia una fractura del tercio proximal del cúbito se acompaña de luxación de la cabeza del radio. En la de Galeazzi una fractura diafisaria del radio se acompaña de luxación radiocubital distal."))

T("ar-9db62430",
  ("Why is posterior dislocation of the sternoclavicular joint an emergency?", ["It injures the axillary nerve.", "The medial end of the clavicle can compress the great vessels and trachea behind it.", "The costoclavicular ligament never tears.", "It also dislocates the shoulder joint.", "It locks the acromioclavicular joint."],
   "In posterior dislocation the medial end of the clavicle can compress the brachiocephalic vessels, trachea and oesophagus; unlike anterior dislocation, it may therefore need urgent reduction."),
  ("Pourquoi la luxation postérieure de l'articulation sterno-claviculaire est-elle une urgence ?", ["Elle lèse le nerf axillaire.", "L'extrémité médiale de la clavicule peut comprimer les gros vaisseaux et la trachée en arrière.", "Le ligament costo-claviculaire ne se rompt jamais.", "Elle luxe aussi l'épaule.", "Elle bloque l'articulation acromio-claviculaire."],
   "Dans la luxation postérieure, l'extrémité médiale de la clavicule peut comprimer les vaisseaux brachio-céphaliques, la trachée et l'œsophage ; contrairement à la luxation antérieure, une réduction urgente peut être nécessaire."),
  ("Warum ist die hintere Luxation des Sternoklavikulargelenks ein Notfall?", ["Sie verletzt den N. axillaris.", "Das mediale Klavikulaende kann die dahinterliegenden großen Gefäße und die Trachea komprimieren.", "Das Lig. costoclaviculare reißt nie.", "Sie luxiert auch das Schultergelenk.", "Sie blockiert das Akromioklavikulargelenk."],
   "Bei der hinteren Luxation kann das mediale Klavikulaende brachiozephale Gefäße, Trachea und Ösophagus komprimieren; anders als bei der vorderen Luxation kann daher eine dringliche Reposition nötig sein."),
  ("¿Por qué la luxación posterior de la articulación esternoclavicular es una urgencia?", ["Lesiona el nervio axilar.", "El extremo medial de la clavícula puede comprimir los grandes vasos y la tráquea situados detrás.", "El ligamento costoclavicular nunca se rompe.", "También luxa el hombro.", "Bloquea la articulación acromioclavicular."],
   "En la luxación posterior el extremo medial de la clavícula puede comprimir los vasos braquiocefálicos, la tráquea y el esófago; a diferencia de la anterior, puede requerir reducción urgente."))

T("ar-684028b7",
  ("How much of the posterior surface of the femoral neck does the hip joint capsule enclose?", ["The medial 2/3", "All of it up to the greater trochanter", "The medial 1/3", "All of it", "Only the femoral head"],
   "Anteriorly the capsule reaches the intertrochanteric line and encloses the whole neck; posteriorly it covers only the medial 2/3 of the neck. Femoral neck fractures are therefore largely intracapsular."),
  ("Quelle part de la face postérieure du col fémoral la capsule de la hanche englobe-t-elle ?", ["Ses 2/3 médiaux", "La totalité jusqu'au grand trochanter", "Son 1/3 médial", "La totalité", "Seulement la tête fémorale"],
   "En avant, la capsule s'étend jusqu'à la ligne intertrochantérique et englobe tout le col ; en arrière, elle n'en couvre que les 2/3 médiaux. Les fractures du col sont donc en grande partie intracapsulaires."),
  ("Wie viel der Rückfläche des Schenkelhalses umschließt die Hüftgelenkkapsel?", ["Die medialen 2/3", "Alles bis zum Trochanter major", "Das mediale 1/3", "Den ganzen Hals", "Nur den Femurkopf"],
   "Vorn reicht die Kapsel bis zur Linea intertrochanterica und umschließt den ganzen Hals, hinten nur dessen mediale 2/3. Schenkelhalsfrakturen liegen daher größtenteils intrakapsulär."),
  ("¿Qué parte de la cara posterior del cuello femoral engloba la cápsula de la cadera?", ["Sus 2/3 mediales", "Toda hasta el trocánter mayor", "Su 1/3 medial", "Todo el cuello", "Solo la cabeza femoral"],
   "Por delante la cápsula llega a la línea intertrocantérea y engloba todo el cuello; por detrás solo cubre sus 2/3 mediales. Por eso las fracturas del cuello son en gran parte intracapsulares."))

T("ar-afbcdf8f",
  ("Which ligament limits excessive internal rotation of the hip joint?", ["Transverse acetabular ligament", "Pubofemoral ligament", "Zona orbicularis", "Ligament of the head of the femur", "Ischiofemoral ligament"],
   "The ischiofemoral ligament spirals from the ischium onto the posterior capsule; it is taut in internal rotation and extension."),
  ("Quel ligament limite la rotation médiale excessive de la hanche ?", ["Ligament transverse de l'acétabulum", "Ligament pubo-fémoral", "Zone orbiculaire", "Ligament de la tête fémorale", "Ligament ischio-fémoral"],
   "Le ligament ischio-fémoral s'enroule en spirale de l'ischium à la face postérieure de la capsule ; il se tend en rotation médiale et en extension."),
  ("Welches Band begrenzt die übermäßige Innenrotation im Hüftgelenk?", ["Lig. transversum acetabuli", "Lig. pubofemorale", "Zona orbicularis", "Lig. capitis femoris", "Lig. ischiofemorale"],
   "Das Lig. ischiofemorale zieht spiralig vom Sitzbein zur Kapselrückseite; es spannt sich bei Innenrotation und Streckung."),
  ("¿Qué ligamento limita la rotación interna excesiva de la cadera?", ["Ligamento transverso del acetábulo", "Ligamento pubofemoral", "Zona orbicular", "Ligamento de la cabeza del fémur", "Ligamento isquiofemoral"],
   "El ligamento isquiofemoral se enrolla en espiral del isquion a la cara posterior de la cápsula; se tensa en rotación interna y extensión."))

T("ar-eb063057",
  ("Which is the most important static stabiliser of the posterolateral corner of the knee?", ["Popliteofibular ligament", "Iliotibial tract", "Meniscofemoral ligament", "Tibial collateral ligament", "Oblique popliteal ligament"],
   "The posterolateral corner consists of the lateral collateral ligament, popliteus tendon, popliteofibular ligament and capsule; the popliteofibular ligament is the main static restraint to external rotation."),
  ("Quel est le stabilisateur statique le plus important du point d'angle postéro-latéral du genou ?", ["Ligament poplité-fibulaire", "Bandelette ilio-tibiale", "Ligament ménisco-fémoral", "Ligament collatéral tibial", "Ligament poplité oblique"],
   "Le point d'angle postéro-latéral comprend le ligament collatéral fibulaire, le tendon du poplité, le ligament poplité-fibulaire et la capsule ; le poplité-fibulaire est le principal frein statique de la rotation latérale."),
  ("Welches ist der wichtigste statische Stabilisator der posterolateralen Ecke des Knies?", ["Lig. popliteofibulare", "Tractus iliotibialis", "Lig. meniscofemorale", "Lig. collaterale tibiale", "Lig. popliteum obliquum"],
   "Die posterolaterale Ecke besteht aus Außenband, Popliteussehne, Lig. popliteofibulare und Kapsel; das Lig. popliteofibulare ist der wichtigste statische Stabilisator gegen Außenrotation."),
  ("¿Cuál es el estabilizador estático más importante de la esquina posterolateral de la rodilla?", ["Ligamento popliteoperoneo", "Cintilla iliotibial", "Ligamento meniscofemoral", "Ligamento colateral tibial", "Ligamento poplíteo oblicuo"],
   "La esquina posterolateral está formada por el colateral peroneo, el tendón del poplíteo, el ligamento popliteoperoneo y la cápsula; el popliteoperoneo es el principal freno estático de la rotación externa."))

T("ar-8f7a2217",
  ("In the dial test, increased external rotation at both 30° and 90° of knee flexion suggests what?", ["An isolated medial collateral ligament tear", "Patellar dislocation", "A medial meniscus tear", "Combined injury of the posterolateral corner and posterior cruciate ligament", "An isolated anterior cruciate ligament tear"],
   "Increased external rotation only at 30° suggests an isolated posterolateral corner injury; at both 30° and 90°, a combined injury of the posterolateral corner and PCL."),
  ("Au dial test, une rotation latérale augmentée à 30° et à 90° de flexion du genou évoque quoi ?", ["Une rupture isolée du ligament collatéral médial", "Une luxation de la patella", "Une lésion du ménisque médial", "Une lésion combinée du point d'angle postéro-latéral et du ligament croisé postérieur", "Une rupture isolée du ligament croisé antérieur"],
   "Une rotation latérale augmentée seulement à 30° évoque une lésion isolée du point d'angle postéro-latéral ; à 30° et à 90°, une lésion combinée du point d'angle postéro-latéral et du LCP."),
  ("Was spricht beim Dial-Test für eine vermehrte Außenrotation bei 30° und 90° Kniebeugung?", ["Isolierter Riss des Innenbandes", "Patellaluxation", "Innenmeniskusriss", "Kombinierte Verletzung von posterolateraler Ecke und hinterem Kreuzband", "Isolierter Riss des vorderen Kreuzbandes"],
   "Vermehrte Außenrotation nur bei 30° spricht für eine isolierte Verletzung der posterolateralen Ecke, bei 30° und 90° für eine kombinierte Verletzung von posterolateraler Ecke und HKB."),
  ("En la prueba del dial, ¿qué sugiere un aumento de la rotación externa a 30° y a 90° de flexión de rodilla?", ["Rotura aislada del ligamento colateral medial", "Luxación de rótula", "Rotura del menisco medial", "Lesión combinada de la esquina posterolateral y del ligamento cruzado posterior", "Rotura aislada del ligamento cruzado anterior"],
   "Un aumento de rotación externa solo a 30° sugiere lesión aislada de la esquina posterolateral; a 30° y 90°, lesión combinada de la esquina posterolateral y del LCP."))

T("ar-cf2d6b19",
  ("Which lateral ankle ligament contributes to both the talocrural and subtalar joints?", ["Posterior talofibular ligament", "Anterior talofibular ligament", "Interosseous talocalcaneal ligament", "Anterior tibiofibular ligament", "Calcaneofibular ligament"],
   "The calcaneofibular ligament runs from the lateral malleolus to the calcaneus and thus crosses both joints; it is assessed with the talar tilt test."),
  ("Quel ligament latéral de la cheville participe à la fois à la talo-crurale et à la sous-talienne ?", ["Ligament talo-fibulaire postérieur", "Ligament talo-fibulaire antérieur", "Ligament talo-calcanéen interosseux", "Ligament tibio-fibulaire antérieur", "Ligament calcanéo-fibulaire"],
   "Le ligament calcanéo-fibulaire va de la malléole latérale au calcanéus et croise donc les deux articulations ; il s'évalue par le test du bâillement talien."),
  ("Welches Außenband des Sprunggelenks wirkt sowohl auf das obere als auch auf das untere Sprunggelenk?", ["Lig. talofibulare posterius", "Lig. talofibulare anterius", "Lig. talocalcaneum interosseum", "Lig. tibiofibulare anterius", "Lig. calcaneofibulare"],
   "Das Lig. calcaneofibulare zieht vom Außenknöchel zum Calcaneus und überbrückt damit beide Gelenke; es wird mit dem Talar-Tilt-Test geprüft."),
  ("¿Qué ligamento lateral del tobillo actúa tanto sobre la talocrural como sobre la subastragalina?", ["Ligamento peroneoastragalino posterior", "Ligamento peroneoastragalino anterior", "Ligamento astragalocalcáneo interóseo", "Ligamento tibioperoneo anterior", "Ligamento peroneocalcáneo"],
   "El ligamento peroneocalcáneo va del maléolo lateral al calcáneo y cruza así ambas articulaciones; se valora con la prueba de inclinación astragalina."))

T("ar-f8a72f31",
  ("Which is the most important structure preventing lateral shift of the talus within the ankle mortise?", ["Calcaneofibular ligament", "Deep (tibiotalar) part of the deltoid ligament", "Long plantar ligament", "Tibionavicular part of the deltoid ligament", "Anterior talofibular ligament"],
   "The deep tibiotalar fibres of the deltoid ligament bind the talus to the medial malleolus; if they tear, the talus shifts laterally, the joint contact area decreases and osteoarthritis develops."),
  ("Quelle est la structure la plus importante empêchant la translation latérale du talus dans la mortaise ?", ["Ligament calcanéo-fibulaire", "Partie profonde (tibio-talienne) du ligament deltoïde", "Ligament plantaire long", "Partie tibio-naviculaire du ligament deltoïde", "Ligament talo-fibulaire antérieur"],
   "Les fibres tibio-taliennes profondes du ligament deltoïde fixent le talus à la malléole médiale ; si elles se rompent, le talus se décale en dehors, la surface de contact diminue et l'arthrose s'installe."),
  ("Welche Struktur verhindert am wichtigsten das Lateralgleiten des Talus in der Malleolengabel?", ["Lig. calcaneofibulare", "Tiefer (tibiotalarer) Anteil des Lig. deltoideum", "Lig. plantare longum", "Pars tibionavicularis des Lig. deltoideum", "Lig. talofibulare anterius"],
   "Die tiefen tibiotalaren Fasern des Lig. deltoideum binden den Talus an den Innenknöchel; reißen sie, verschiebt sich der Talus nach lateral, die Kontaktfläche nimmt ab und es entsteht Arthrose."),
  ("¿Cuál es la estructura más importante que impide el desplazamiento lateral del astrágalo en la mortaja?", ["Ligamento peroneocalcáneo", "Porción profunda (tibioastragalina) del ligamento deltoideo", "Ligamento plantar largo", "Porción tibionavicular del ligamento deltoideo", "Ligamento peroneoastragalino anterior"],
   "Las fibras tibioastragalinas profundas del deltoideo fijan el astrágalo al maléolo medial; si se rompen, el astrágalo se desplaza lateralmente, disminuye la superficie de contacto y aparece artrosis."))

T("ar-90e61aae",
  ("From the calcaneus, to which bones do the two limbs of the bifurcate ligament run?", ["Navicular and cuboid", "Talus and cuboid", "Cuboid and 5th metatarsal", "Navicular and medial cuneiform", "Talus and navicular"],
   "The calcaneonavicular and calcaneocuboid limbs of the Y-shaped bifurcate ligament lie on the dorsum of Chopart's joint; its sprain causes pain in front of the sinus tarsi."),
  ("Depuis le calcanéus, vers quels os se dirigent les deux faisceaux du ligament bifurqué ?", ["Naviculaire et cuboïde", "Talus et cuboïde", "Cuboïde et 5e métatarsien", "Naviculaire et cunéiforme médial", "Talus et naviculaire"],
   "Les faisceaux calcanéo-naviculaire et calcanéo-cuboïdien du ligament bifurqué en Y sont situés à la face dorsale de l'interligne de Chopart ; son entorse donne une douleur en avant du sinus du tarse."),
  ("Zu welchen Knochen ziehen die beiden Schenkel des Lig. bifurcatum vom Calcaneus aus?", ["Kahnbein und Würfelbein", "Talus und Würfelbein", "Würfelbein und 5. Mittelfußknochen", "Kahnbein und inneres Keilbein", "Talus und Kahnbein"],
   "Die kalkaneonavikulären und kalkaneokuboidalen Schenkel des Y-förmigen Lig. bifurcatum liegen dorsal auf der Chopart-Linie; seine Zerrung schmerzt vor dem Sinus tarsi."),
  ("Desde el calcáneo, ¿hacia qué huesos se dirigen los dos fascículos del ligamento bifurcado?", ["Navicular y cuboides", "Astrágalo y cuboides", "Cuboides y 5.º metatarsiano", "Navicular y cuña medial", "Astrágalo y navicular"],
   "Los fascículos calcaneonavicular y calcaneocuboideo del ligamento bifurcado en Y están en el dorso de la articulación de Chopart; su esguince produce dolor delante del seno del tarso."))

T("ar-c4078aba",
  ("What is the typical sign of talocalcaneal coalition on a lateral ankle radiograph?", ["Terry Thomas sign", "Anteater nose sign", "Double contour sign", "C sign", "Ring sign"],
   "In talocalcaneal coalition a continuous C-shaped contour forms between the dome of the talus and the sustentaculum tali. In calcaneonavicular coalition the oblique view shows the 'anteater nose'."),
  ("Quel est le signe typique de la synostose talo-calcanéenne sur la radiographie de profil de la cheville ?", ["Signe de Terry Thomas", "Signe du nez de fourmilier", "Signe du double contour", "Signe du C", "Signe de l'anneau"],
   "Dans la synostose talo-calcanéenne, un contour continu en forme de C relie le dôme du talus au sustentaculum tali. Dans la synostose calcanéo-naviculaire, le cliché oblique montre le « nez de fourmilier »."),
  ("Was ist das typische Zeichen einer talokalkanearen Koalition im seitlichen Röntgenbild des Sprunggelenks?", ["Terry-Thomas-Zeichen", "Ameisenbärnasen-Zeichen", "Doppelkontur-Zeichen", "C-Zeichen", "Ringzeichen"],
   "Bei talokalkanearer Koalition entsteht eine durchgehende C-förmige Kontur zwischen Taluskuppel und Sustentaculum tali. Bei kalkaneonavikulärer Koalition zeigt die Schrägaufnahme die „Ameisenbärnase“."),
  ("¿Cuál es el signo típico de la coalición astragalocalcánea en la radiografía lateral del tobillo?", ["Signo de Terry Thomas", "Signo del hocico de oso hormiguero", "Signo del doble contorno", "Signo de la C", "Signo del anillo"],
   "En la coalición astragalocalcánea se forma un contorno continuo en forma de C entre la cúpula del astrágalo y el sustentaculum tali. En la coalición calcaneonavicular la proyección oblicua muestra el «hocico de oso hormiguero»."))

T("ar-358bf10c",
  ("A skier who twisted the knee into external rotation reports sudden pain and instability; after ACL reconstruction, external rotation instability of the knee persists. Which injury may have been missed?", ["Pes anserinus bursitis", "Posterolateral corner injury of the knee", "Patellar tendon rupture", "Prepatellar bursitis", "Medial meniscus tear"],
   "Posterolateral corner injuries often accompany cruciate ligament injuries; if they are not recognised and repaired, the cruciate graft is overloaded and the reconstruction fails."),
  ("Un skieur dont le genou est parti en rotation latérale décrit une douleur brutale et une instabilité ; après reconstruction du LCA, l'instabilité en rotation latérale persiste. Quelle lésion a pu passer inaperçue ?", ["Bursite de la patte d'oie", "Lésion du point d'angle postéro-latéral du genou", "Rupture du tendon patellaire", "Bursite prépatellaire", "Lésion du ménisque médial"],
   "Les lésions du point d'angle postéro-latéral accompagnent souvent celles des ligaments croisés ; non reconnues et non réparées, elles surchargent la greffe du croisé et font échouer la reconstruction."),
  ("Ein Skifahrer mit Außenrotationstrauma des Knies berichtet über plötzlichen Schmerz und Instabilität; nach VKB-Plastik besteht weiter eine Außenrotationsinstabilität. Welche Verletzung wurde möglicherweise übersehen?", ["Bursitis anserina", "Verletzung der posterolateralen Ecke des Knies", "Patellasehnenruptur", "Bursitis praepatellaris", "Innenmeniskusriss"],
   "Verletzungen der posterolateralen Ecke begleiten häufig Kreuzbandverletzungen; werden sie nicht erkannt und versorgt, wird das Kreuzbandtransplantat überlastet und die Rekonstruktion scheitert."),
  ("Un esquiador que giró la rodilla en rotación externa refiere dolor súbito e inestabilidad; tras la reconstrucción del LCA persiste la inestabilidad en rotación externa. ¿Qué lesión pudo pasar desapercibida?", ["Bursitis de la pata de ganso", "Lesión de la esquina posterolateral de la rodilla", "Rotura del tendón rotuliano", "Bursitis prerrotuliana", "Rotura del menisco medial"],
   "Las lesiones de la esquina posterolateral acompañan a menudo a las de los ligamentos cruzados; si no se reconocen y reparan, el injerto del cruzado se sobrecarga y la reconstrucción fracasa."))
