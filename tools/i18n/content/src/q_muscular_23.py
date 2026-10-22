KIND = "questions"
SYSTEM = "muscular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("mu-4133a9b8",
  ("Which spinal segment does the biceps tendon reflex mainly test?", ["C8", "C7", "C5", "C3", "T1"],
   "The biceps reflex runs through the musculocutaneous nerve and tests C5–C6, especially C5. The brachioradialis reflex is for C6, the triceps reflex for C7."),
  ("Quel segment médullaire le réflexe bicipital teste-t-il principalement ?", ["C8", "C7", "C5", "C3", "T1"],
   "Le réflexe bicipital passe par le nerf musculo-cutané et teste C5–C6, surtout C5. Le réflexe stylo-radial correspond à C6, le tricipital à C7."),
  ("Welches Segment prüft der Bizepssehnenreflex vor allem?", ["C8", "C7", "C5", "C3", "T1"],
   "Der Bizepssehnenreflex verläuft über den N. musculocutaneus und prüft C5–C6, vor allem C5. Der Brachioradialisreflex steht für C6, der Trizepsreflex für C7."),
  ("¿Qué segmento medular explora principalmente el reflejo bicipital?", ["C8", "C7", "C5", "C3", "T1"],
   "El reflejo bicipital pasa por el musculocutáneo y explora C5–C6, sobre todo C5. El braquiorradial corresponde a C6 y el tricipital a C7."))

T("mu-ef6cce8c",
  ("Which of the following muscles is NOT in the anterior compartment of the leg?", ["Fibularis brevis", "Extensor digitorum longus", "Tibialis anterior", "Fibularis tertius", "Extensor hallucis longus"],
   "The anterior compartment contains tibialis anterior, EHL, EDL and fibularis tertius, supplied by the deep fibular nerve. Fibularis brevis is in the lateral compartment (superficial fibular nerve)."),
  ("Lequel de ces muscles n'appartient PAS à la loge antérieure de la jambe ?", ["Muscle court fibulaire", "Muscle long extenseur des orteils", "Muscle tibial antérieur", "Muscle troisième fibulaire", "Muscle long extenseur de l'hallux"],
   "La loge antérieure contient le tibial antérieur, le long extenseur de l'hallux, le long extenseur des orteils et le troisième fibulaire, innervés par le nerf fibulaire profond. Le court fibulaire est dans la loge latérale (nerf fibulaire superficiel)."),
  ("Welcher dieser Muskeln liegt NICHT in der vorderen Loge des Unterschenkels?", ["M. fibularis brevis", "M. extensor digitorum longus", "M. tibialis anterior", "M. fibularis tertius", "M. extensor hallucis longus"],
   "Die vordere Loge enthält M. tibialis anterior, M. extensor hallucis longus, M. extensor digitorum longus und M. fibularis tertius, innerviert vom N. fibularis profundus. Der M. fibularis brevis liegt in der lateralen Loge (N. fibularis superficialis)."),
  ("¿Cuál de estos músculos NO está en el compartimento anterior de la pierna?", ["Músculo peroneo corto", "Músculo extensor largo de los dedos", "Músculo tibial anterior", "Músculo peroneo tercero", "Músculo extensor largo del dedo gordo"],
   "El compartimento anterior contiene el tibial anterior, el extensor largo del dedo gordo, el extensor largo de los dedos y el peroneo tercero, inervados por el peroneo profundo. El peroneo corto está en el compartimento lateral (peroneo superficial)."))

T("mu-7996df31",
  ("Where do the two heads of gastrocnemius arise?", ["From the posterior surfaces of the tibia and fibula", "From the posterior surfaces of the medial and lateral femoral condyles", "From the patella and patellar ligament", "From the ischial tuberosity", "From the soleal line"],
   "Because gastrocnemius arises from the femoral condyles it also crosses the knee and helps flex it. Soleus arises from the tibia and fibula and does not cross the knee."),
  ("D'où naissent les deux chefs du gastrocnémien ?", ["Des faces postérieures du tibia et de la fibula", "Des faces postérieures des condyles fémoraux médial et latéral", "De la patella et du ligament patellaire", "De la tubérosité ischiatique", "De la ligne du soléaire"],
   "Comme il naît des condyles fémoraux, le gastrocnémien croise aussi le genou et aide à le fléchir. Le soléaire naît du tibia et de la fibula et ne croise pas le genou."),
  ("Wo entspringen die beiden Köpfe des M. gastrocnemius?", ["An der Rückfläche von Tibia und Fibula", "An der Rückfläche des medialen und lateralen Femurkondylus", "An Patella und Lig. patellae", "Am Tuber ischiadicum", "An der Linea musculi solei"],
   "Da der M. gastrocnemius an den Femurkondylen entspringt, überquert er auch das Knie und hilft es zu beugen. Der M. soleus entspringt an Tibia und Fibula und überquert das Knie nicht."),
  ("¿Dónde se originan las dos cabezas del gastrocnemio?", ["En las caras posteriores de la tibia y el peroné", "En las caras posteriores de los cóndilos femorales medial y lateral", "En la rótula y el ligamento rotuliano", "En la tuberosidad isquiática", "En la línea del sóleo"],
   "Como nace de los cóndilos femorales, el gastrocnemio cruza también la rodilla y ayuda a flexionarla. El sóleo nace de la tibia y el peroné y no cruza la rodilla."))

T("mu-d1e6dcde",
  ("Which nerve supplies popliteus?", ["Femoral nerve", "Tibial nerve", "Common fibular nerve", "Saphenous nerve", "Obturator nerve"],
   "Popliteus is the muscle in the floor of the popliteal fossa; it unlocks the knee from full extension and is supplied by the tibial nerve."),
  ("Quel nerf innerve le muscle poplité ?", ["Nerf fémoral", "Nerf tibial", "Nerf fibulaire commun", "Nerf saphène", "Nerf obturateur"],
   "Le poplité est le muscle du plancher de la fosse poplitée ; il « déverrouille » le genou en extension complète et est innervé par le nerf tibial."),
  ("Welcher Nerv innerviert den M. popliteus?", ["N. femoralis", "N. tibialis", "N. fibularis communis", "N. saphenus", "N. obturatorius"],
   "Der M. popliteus liegt am Boden der Kniekehle; er entriegelt das in voller Streckung verriegelte Knie und wird vom N. tibialis innerviert."),
  ("¿Qué nervio inerva el músculo poplíteo?", ["Nervio femoral", "Nervio tibial", "Nervio peroneo común", "Nervio safeno", "Nervio obturador"],
   "El poplíteo es el músculo del suelo de la fosa poplítea; «desbloquea» la rodilla desde la extensión completa y lo inerva el nervio tibial."))

T("mu-3811c4d1",
  ("Which muscles are in the first (most superficial) layer of the sole of the foot?", ["Extensor digitorum brevis and extensor hallucis brevis", "Plantar and dorsal interossei", "Quadratus plantae and the lumbricals", "Abductor hallucis, flexor digitorum brevis and abductor digiti minimi", "Flexor hallucis brevis and adductor hallucis"],
   "The plantar muscles form four layers: 1. abductor hallucis, FDB, abductor digiti minimi; 2. quadratus plantae, lumbricals; 3. FHB, adductor hallucis, FDMB; 4. interossei."),
  ("Quels muscles forment la première couche (la plus superficielle) de la plante du pied ?", ["Court extenseur des orteils et court extenseur de l'hallux", "Interosseux plantaires et dorsaux", "Carré plantaire et lombricaux", "Abducteur de l'hallux, court fléchisseur des orteils et abducteur du petit orteil", "Court fléchisseur de l'hallux et adducteur de l'hallux"],
   "Les muscles plantaires forment quatre couches : 1. abducteur de l'hallux, court fléchisseur des orteils, abducteur du petit orteil ; 2. carré plantaire, lombricaux ; 3. court fléchisseur et adducteur de l'hallux, court fléchisseur du petit orteil ; 4. interosseux."),
  ("Welche Muskeln bilden die erste (oberflächlichste) Schicht der Fußsohle?", ["M. extensor digitorum brevis und M. extensor hallucis brevis", "Mm. interossei plantares und dorsales", "M. quadratus plantae und Mm. lumbricales", "M. abductor hallucis, M. flexor digitorum brevis und M. abductor digiti minimi", "M. flexor hallucis brevis und M. adductor hallucis"],
   "Die Fußsohlenmuskeln bilden vier Schichten: 1. M. abductor hallucis, M. flexor digitorum brevis, M. abductor digiti minimi; 2. M. quadratus plantae, Mm. lumbricales; 3. M. flexor hallucis brevis, M. adductor hallucis, M. flexor digiti minimi brevis; 4. Mm. interossei."),
  ("¿Qué músculos forman la primera capa (la más superficial) de la planta del pie?", ["Extensor corto de los dedos y extensor corto del dedo gordo", "Interóseos plantares y dorsales", "Cuadrado plantar y lumbricales", "Abductor del dedo gordo, flexor corto de los dedos y abductor del quinto dedo", "Flexor corto del dedo gordo y aductor del dedo gordo"],
   "Los músculos plantares forman cuatro capas: 1.ª abductor del dedo gordo, flexor corto de los dedos, abductor del quinto dedo; 2.ª cuadrado plantar, lumbricales; 3.ª flexor corto y aductor del dedo gordo, flexor corto del quinto dedo; 4.ª interóseos."))

T("mu-cb57c01f",
  ("A basketball player landing from a jump reports pain at the front of the knee and cannot actively extend it; the patella lies higher than normal. What is the most likely diagnosis?", ["Anterior cruciate ligament tear", "Patellar tendon (patellar ligament) rupture", "Medial meniscus tear", "Quadriceps tendon rupture", "Patellar dislocation"],
   "When the patellar ligament ruptures, quadriceps pulls the patella upwards (patella alta) and, with the extensor mechanism disrupted, the knee cannot be actively extended. In a quadriceps tendon rupture the patella stays low (patella baja)."),
  ("Un basketteur qui retombe d'un saut décrit une douleur à l'avant du genou et ne peut l'étendre activement ; la patella est plus haute que la normale. Quel est le diagnostic le plus probable ?", ["Rupture du ligament croisé antérieur", "Rupture du tendon (ligament) patellaire", "Lésion du ménisque médial", "Rupture du tendon quadricipital", "Luxation de la patella"],
   "Quand le ligament patellaire se rompt, le quadriceps attire la patella vers le haut (patella alta) et, l'appareil extenseur étant interrompu, le genou ne peut être étendu activement. Dans la rupture du tendon quadricipital, la patella reste basse (patella baja)."),
  ("Ein Basketballspieler landet nach einem Sprung, klagt über Schmerzen vorn am Knie und kann es nicht aktiv strecken; die Patella steht höher als normal. Wahrscheinlichste Diagnose?", ["Riss des vorderen Kreuzbandes", "Ruptur der Patellasehne (Lig. patellae)", "Innenmeniskusriss", "Quadrizepssehnenruptur", "Patellaluxation"],
   "Reißt das Lig. patellae, zieht der Quadrizeps die Patella nach oben (Patellahochstand) und das Knie kann bei unterbrochenem Streckapparat nicht aktiv gestreckt werden. Bei der Quadrizepssehnenruptur steht die Patella tief (Patella baja)."),
  ("Un jugador de baloncesto que aterriza de un salto refiere dolor en la parte anterior de la rodilla y no puede extenderla activamente; la rótula está más alta de lo normal. ¿Cuál es el diagnóstico más probable?", ["Rotura del ligamento cruzado anterior", "Rotura del tendón (ligamento) rotuliano", "Rotura del menisco medial", "Rotura del tendón cuadricipital", "Luxación de rótula"],
   "Cuando se rompe el ligamento rotuliano, el cuádriceps tira de la rótula hacia arriba (rótula alta) y, al estar interrumpido el aparato extensor, la rodilla no puede extenderse activamente. En la rotura del tendón cuadricipital la rótula queda baja (patella baja)."))

T("mu-e59cf28c",
  ("Which is the only palatal muscle supplied by the mandibular nerve (V3)?", ["Palatoglossus", "Levator veli palatini", "Palatopharyngeus", "Musculus uvulae", "Tensor veli palatini"],
   "All palatal muscles are supplied by the vagus through the pharyngeal plexus; the only exception is tensor veli palatini, derived from the 1st arch (V3). Tensor tympani is likewise supplied by V3."),
  ("Quel est le seul muscle du voile du palais innervé par le nerf mandibulaire (V3) ?", ["Muscle palato-glosse", "Muscle élévateur du voile du palais", "Muscle palato-pharyngien", "Muscle de la luette", "Muscle tenseur du voile du palais"],
   "Tous les muscles du voile sont innervés par le vague via le plexus pharyngien ; seule exception, le tenseur du voile du palais, issu du 1er arc (V3). Le tenseur du tympan est lui aussi innervé par V3."),
  ("Welcher ist der einzige Gaumenmuskel, der vom N. mandibularis (V3) innerviert wird?", ["M. palatoglossus", "M. levator veli palatini", "M. palatopharyngeus", "M. uvulae", "M. tensor veli palatini"],
   "Alle Gaumenmuskeln werden über den Plexus pharyngeus vom N. vagus innerviert; einzige Ausnahme ist der aus dem 1. Bogen stammende M. tensor veli palatini (V3). Auch der M. tensor tympani wird von V3 versorgt."),
  ("¿Cuál es el único músculo del paladar inervado por el nervio mandibular (V3)?", ["Músculo palatogloso", "Músculo elevador del velo del paladar", "Músculo palatofaríngeo", "Músculo de la úvula", "Músculo tensor del velo del paladar"],
   "Todos los músculos del paladar los inerva el vago a través del plexo faríngeo; la única excepción es el tensor del velo del paladar, derivado del 1.er arco (V3). El tensor del tímpano también lo inerva V3."))

T("mu-6fb5ef1a",
  ("Which option gives the innervation of the middle ear muscles correctly?", ["Both glossopharyngeal nerve", "Both facial nerve", "Tensor tympani – vagus; stapedius – facial", "Tensor tympani – facial; stapedius – mandibular", "Tensor tympani – mandibular nerve (V3); stapedius – facial nerve (VII)"],
   "Tensor tympani derives from the 1st arch (V3), stapedius from the 2nd arch (VII). Facial nerve lesions proximal to the nerve to stapedius cause hyperacusis."),
  ("Quelle proposition donne correctement l'innervation des muscles de l'oreille moyenne ?", ["Tous deux par le glosso-pharyngien", "Tous deux par le facial", "Tenseur du tympan – vague ; stapédien – facial", "Tenseur du tympan – facial ; stapédien – mandibulaire", "Tenseur du tympan – nerf mandibulaire (V3) ; stapédien – nerf facial (VII)"],
   "Le tenseur du tympan dérive du 1er arc (V3), le stapédien du 2e arc (VII). Les lésions du facial en amont du nerf du stapédien entraînent une hyperacousie."),
  ("Welche Angabe zur Innervation der Mittelohrmuskeln ist richtig?", ["Beide N. glossopharyngeus", "Beide N. facialis", "M. tensor tympani – N. vagus; M. stapedius – N. facialis", "M. tensor tympani – N. facialis; M. stapedius – N. mandibularis", "M. tensor tympani – N. mandibularis (V3); M. stapedius – N. facialis (VII)"],
   "Der M. tensor tympani stammt aus dem 1. Bogen (V3), der M. stapedius aus dem 2. Bogen (VII). Fazialisläsionen proximal des N. stapedius verursachen eine Hyperakusis."),
  ("¿Qué opción indica correctamente la inervación de los músculos del oído medio?", ["Ambos el glosofaríngeo", "Ambos el facial", "Tensor del tímpano – vago; estapedio – facial", "Tensor del tímpano – facial; estapedio – mandibular", "Tensor del tímpano – nervio mandibular (V3); estapedio – nervio facial (VII)"],
   "El tensor del tímpano deriva del 1.er arco (V3) y el estapedio del 2.º (VII). Las lesiones del facial proximales al nervio del estapedio producen hiperacusia."))

T("mu-568138c7",
  ("From which vertebrae does the right crus of the diaphragm arise?", ["Bodies of L1–L3", "Bodies of L1–L2", "Bodies of L3–L5", "Bodies of T12–L1", "Bodies of T10–T12"],
   "The right crus arises from the bodies of L1–L3, the shorter left crus from L1–L2. Fibres of the right crus encircle the oesophagus like a sling to form the oesophageal hiatus."),
  ("De quelles vertèbres naît le pilier droit du diaphragme ?", ["Corps de L1–L3", "Corps de L1–L2", "Corps de L3–L5", "Corps de T12–L1", "Corps de T10–T12"],
   "Le pilier droit naît des corps de L1 à L3, le pilier gauche, plus court, de L1–L2. Les fibres du pilier droit entourent l'œsophage comme une fronde et forment le hiatus œsophagien."),
  ("Von welchen Wirbeln entspringt das rechte Zwerchfellcrus?", ["Wirbelkörper L1–L3", "Wirbelkörper L1–L2", "Wirbelkörper L3–L5", "Wirbelkörper T12–L1", "Wirbelkörper T10–T12"],
   "Das rechte Crus entspringt an den Wirbelkörpern L1–L3, das kürzere linke an L1–L2. Fasern des rechten Crus umschlingen den Ösophagus und bilden den Hiatus oesophageus."),
  ("¿De qué vértebras se origina el pilar derecho del diafragma?", ["Cuerpos de L1–L3", "Cuerpos de L1–L2", "Cuerpos de L3–L5", "Cuerpos de T12–L1", "Cuerpos de T10–T12"],
   "El pilar derecho nace de los cuerpos de L1–L3 y el izquierdo, más corto, de L1–L2. Las fibras del pilar derecho rodean el esófago como un lazo y forman el hiato esofágico."))

T("mu-2b4b7a06",
  ("What are the most common type and site of congenital diaphragmatic hernia?", ["Morgagni hernia – anteromedial, mostly on the right", "Bochdalek hernia – anteromedial, mostly on the right", "Hiatal hernia – oesophageal opening", "Bochdalek hernia – posterolateral, mostly on the left", "Morgagni hernia – posterolateral, on the left"],
   "A Bochdalek hernia forms posterolaterally (most often on the left) when the pleuroperitoneal membrane fails to close, causing lung hypoplasia in the newborn. A Morgagni hernia is rarer and anteromedial."),
  ("Quels sont le type et le siège les plus fréquents de la hernie diaphragmatique congénitale ?", ["Hernie de Morgagni – antéro-médiale, surtout à droite", "Hernie de Bochdalek – antéro-médiale, surtout à droite", "Hernie hiatale – orifice œsophagien", "Hernie de Bochdalek – postéro-latérale, surtout à gauche", "Hernie de Morgagni – postéro-latérale, à gauche"],
   "La hernie de Bochdalek se forme en région postéro-latérale (le plus souvent à gauche) par défaut de fermeture de la membrane pleuro-péritonéale et entraîne une hypoplasie pulmonaire chez le nouveau-né. La hernie de Morgagni est plus rare et antéro-médiale."),
  ("Welches sind Typ und Lage der häufigsten angeborenen Zwerchfellhernie?", ["Morgagni-Hernie – anteromedial, meist rechts", "Bochdalek-Hernie – anteromedial, meist rechts", "Hiatushernie – Ösophagusöffnung", "Bochdalek-Hernie – posterolateral, meist links", "Morgagni-Hernie – posterolateral, links"],
   "Die Bochdalek-Hernie entsteht posterolateral (meist links) durch fehlenden Verschluss der Membrana pleuroperitonealis und führt beim Neugeborenen zur Lungenhypoplasie. Die Morgagni-Hernie ist seltener und liegt anteromedial."),
  ("¿Cuáles son el tipo y la localización más frecuentes de la hernia diafragmática congénita?", ["Hernia de Morgagni – anteromedial, sobre todo derecha", "Hernia de Bochdalek – anteromedial, sobre todo derecha", "Hernia de hiato – orificio esofágico", "Hernia de Bochdalek – posterolateral, sobre todo izquierda", "Hernia de Morgagni – posterolateral, izquierda"],
   "La hernia de Bochdalek se forma en la región posterolateral (casi siempre izquierda) por falta de cierre de la membrana pleuroperitoneal y causa hipoplasia pulmonar en el recién nacido. La de Morgagni es más rara y anteromedial."))

T("mu-64e5a84c",
  ("What is the typical arm position in Erb–Duchenne palsy (upper trunk, C5–C6)?", ["Arm normal, only thumb opposition lost", "Arm adducted and medially rotated, forearm extended and pronated ('waiter's tip')", "Arm abducted and laterally rotated, forearm flexed", "Wrist drop (wrist in flexion)", "Clawed fingers, arm normal"],
   "In C5–C6 injury deltoid, supraspinatus, infraspinatus, biceps and brachialis are paralysed; the arm hangs adducted and medially rotated, the forearm extended and pronated. It results from birth trauma and forced widening of the shoulder–neck angle."),
  ("Quelle est la position typique du membre dans la paralysie d'Erb-Duchenne (tronc supérieur, C5–C6) ?", ["Membre normal, seule l'opposition du pouce est perdue", "Bras en adduction et rotation médiale, avant-bras en extension et pronation (« pourboire du serveur »)", "Bras en abduction et rotation latérale, avant-bras fléchi", "Main tombante (poignet fléchi)", "Doigts en griffe, bras normal"],
   "Dans l'atteinte C5–C6, le deltoïde, le supra- et l'infra-épineux, le biceps et le brachial sont paralysés ; le bras pend en adduction et rotation médiale, l'avant-bras en extension et pronation. Elle survient lors d'un traumatisme obstétrical par écartement forcé de l'épaule et du cou."),
  ("Welche typische Armhaltung zeigt die Erb-Duchenne-Lähmung (oberer Primärstrang, C5–C6)?", ["Arm normal, nur Daumenopposition verloren", "Arm adduziert und innenrotiert, Unterarm gestreckt und proniert („Kellnerhaltung“)", "Arm abduziert und außenrotiert, Unterarm gebeugt", "Fallhand (Handgelenk gebeugt)", "Krallenfinger, Arm normal"],
   "Bei Schädigung von C5–C6 sind M. deltoideus, M. supraspinatus, M. infraspinatus, M. biceps und M. brachialis gelähmt; der Arm hängt adduziert und innenrotiert, der Unterarm gestreckt und proniert. Ursache sind Geburtstraumen mit Überdehnung des Schulter-Hals-Winkels."),
  ("¿Cuál es la posición típica del brazo en la parálisis de Erb-Duchenne (tronco superior, C5–C6)?", ["Brazo normal, solo se pierde la oposición del pulgar", "Brazo en aducción y rotación interna, antebrazo en extensión y pronación («propina del camarero»)", "Brazo en abducción y rotación externa, antebrazo flexionado", "Mano caída (muñeca en flexión)", "Dedos en garra, brazo normal"],
   "En la lesión C5–C6 se paralizan el deltoides, el supraespinoso, el infraespinoso, el bíceps y el braquial; el brazo cuelga en aducción y rotación interna, con el antebrazo extendido y en pronación. Se debe a traumatismo obstétrico con separación forzada del hombro y el cuello."))

T("mu-0fe418f7",
  ("Which muscles are most affected in Klumpke palsy (lower trunk, C8–T1)?", ["Rotator cuff muscles", "Triceps and anconeus", "Forearm supinators", "Deltoid and biceps", "Intrinsic muscles of the hand"],
   "Injury of the C8–T1 roots (traction of the arm in excessive abduction) affects all intrinsic hand muscles and produces a claw hand; if T1 sympathetic fibres are involved, Horner syndrome may accompany it."),
  ("Quels muscles sont les plus touchés dans la paralysie de Klumpke (tronc inférieur, C8–T1) ?", ["Muscles de la coiffe des rotateurs", "Triceps et anconé", "Supinateurs de l'avant-bras", "Deltoïde et biceps", "Muscles intrinsèques de la main"],
   "L'atteinte des racines C8–T1 (traction du bras en abduction forcée) touche tous les muscles intrinsèques de la main et donne une main en griffe ; si les fibres sympathiques de T1 sont lésées, un syndrome de Claude Bernard-Horner peut s'y associer."),
  ("Welche Muskeln sind bei der Klumpke-Lähmung (unterer Primärstrang, C8–T1) am stärksten betroffen?", ["Rotatorenmanschette", "Triceps und Anconeus", "Supinatoren des Unterarms", "Deltoideus und Biceps", "Intrinsische Handmuskeln"],
   "Die Schädigung der Wurzeln C8–T1 (Zug am Arm in starker Abduktion) betrifft alle intrinsischen Handmuskeln und führt zur Krallenhand; sind sympathische T1-Fasern beteiligt, kann ein Horner-Syndrom hinzukommen."),
  ("¿Qué músculos se afectan más en la parálisis de Klumpke (tronco inferior, C8–T1)?", ["Músculos del manguito rotador", "Tríceps y ancóneo", "Supinadores del antebrazo", "Deltoides y bíceps", "Músculos intrínsecos de la mano"],
   "La lesión de las raíces C8–T1 (tracción del brazo en abducción forzada) afecta a todos los músculos intrínsecos de la mano y produce una mano en garra; si se lesionan las fibras simpáticas de T1 puede asociarse un síndrome de Horner."))

T("mu-4c3ad44c",
  ("When the radial nerve is injured in a fracture of the middle third of the humerus, why is triceps brachii usually spared?", ["The branches to triceps leave before the nerve enters the spiral groove.", "Triceps is supplied by the axillary nerve.", "Triceps is supplied by the ulnar nerve.", "Triceps has a double innervation.", "The nerve does not pass through triceps in the spiral groove."],
   "In the upper arm, before entering the radial groove, the radial nerve gives its branches to the long and medial heads of triceps. In a mid-shaft fracture elbow extension is therefore mostly preserved, while wrist drop develops."),
  ("Lorsque le nerf radial est lésé dans une fracture du tiers moyen de l'humérus, pourquoi le triceps est-il habituellement épargné ?", ["Ses rameaux naissent avant l'entrée du nerf dans le sillon du nerf radial.", "Le triceps est innervé par le nerf axillaire.", "Le triceps est innervé par le nerf ulnaire.", "Le triceps a une double innervation.", "Le nerf ne traverse pas le triceps dans le sillon."],
   "À la partie haute du bras, avant d'entrer dans le sillon du nerf radial, le nerf donne ses rameaux aux chefs long et médial du triceps. Dans une fracture diaphysaire moyenne, l'extension du coude est donc le plus souvent conservée et une main tombante apparaît."),
  ("Warum bleibt bei einer Verletzung des N. radialis im Rahmen einer Humerusschaftfraktur (mittleres Drittel) der M. triceps meist verschont?", ["Die Trizepsäste gehen ab, bevor der Nerv in den Sulcus nervi radialis eintritt.", "Der Triceps wird vom N. axillaris innerviert.", "Der Triceps wird vom N. ulnaris innerviert.", "Der Triceps ist doppelt innerviert.", "Der Nerv zieht im Sulcus nicht durch den Triceps."],
   "Im oberen Oberarm gibt der N. radialis vor Eintritt in den Sulcus nervi radialis seine Äste zum Caput longum und mediale des Triceps ab. Bei der Schaftfraktur bleibt die Ellenbogenstreckung daher meist erhalten, es entsteht eine Fallhand."),
  ("Cuando el nervio radial se lesiona en una fractura del tercio medio del húmero, ¿por qué suele respetarse el tríceps braquial?", ["Sus ramas salen antes de que el nervio entre en el surco del nervio radial.", "El tríceps lo inerva el nervio axilar.", "El tríceps lo inerva el nervio cubital.", "El tríceps tiene doble inervación.", "El nervio no atraviesa el tríceps en el surco."],
   "En la parte alta del brazo, antes de entrar en el surco del nervio radial, el nervio da sus ramas a las cabezas larga y medial del tríceps. Por eso en la fractura diafisaria media la extensión del codo suele conservarse y aparece mano caída."))

T("mu-06305979",
  ("A rugby player whose finger was forcibly extended while grabbing an opponent's jersey cannot actively flex the DIP joint (jersey finger). Which tendon has ruptured?", ["Lumbrical", "Flexor digitorum superficialis", "Flexor digitorum profundus", "Terminal part of the extensor tendon", "Palmar interosseous"],
   "In jersey finger the FDP tendon avulses from the base of the distal phalanx; the ring finger is most often affected. Because only FDP flexes the DIP joint, this movement is lost."),
  ("Un rugbyman dont le doigt a été étendu de force en agrippant le maillot d'un adversaire ne peut plus fléchir activement l'IPD (« jersey finger »). Quel tendon est rompu ?", ["Lombrical", "Fléchisseur superficiel des doigts", "Fléchisseur profond des doigts", "Partie terminale de l'extenseur", "Interosseux palmaire"],
   "Dans le jersey finger, le tendon du fléchisseur profond s'arrache de la base de la phalange distale, le plus souvent à l'annulaire. Comme seul le fléchisseur profond fléchit l'IPD, ce mouvement est perdu."),
  ("Einem Rugbyspieler wurde beim Festhalten am Trikot des Gegners der Finger gewaltsam gestreckt; er kann das DIP-Gelenk nicht aktiv beugen („Jersey finger“). Welche Sehne ist gerissen?", ["M. lumbricalis", "M. flexor digitorum superficialis", "M. flexor digitorum profundus", "Endsehne des Streckapparats", "M. interosseus palmaris"],
   "Beim Jersey finger reißt die FDP-Sehne an der Basis der Endphalanx aus; am häufigsten ist der Ringfinger betroffen. Da nur der FDP das DIP-Gelenk beugt, fällt diese Bewegung aus."),
  ("A un jugador de rugby se le extendió el dedo a la fuerza al agarrar la camiseta del rival y no puede flexionar activamente la IFD («dedo de jersey»). ¿Qué tendón se ha roto?", ["Lumbrical", "Flexor superficial de los dedos", "Flexor profundo de los dedos", "Porción terminal del extensor", "Interóseo palmar"],
   "En el dedo de jersey el tendón del flexor profundo se arranca de la base de la falange distal, sobre todo en el anular. Como solo el flexor profundo flexiona la IFD, este movimiento se pierde."))

T("mu-fd7114cd",
  ("Which nerve supplies quadratus femoris?", ["Inferior gluteal nerve", "Nerve to quadratus femoris (L4–S1)", "Nerve to obturator internus", "Obturator nerve", "Tibial division of the sciatic nerve"],
   "Quadratus femoris and gemellus inferior are supplied by the nerve to quadratus femoris from the sacral plexus. Obturator internus and gemellus superior are supplied by the nerve to obturator internus."),
  ("Quel nerf innerve le muscle carré fémoral ?", ["Nerf glutéal inférieur", "Nerf du carré fémoral (L4–S1)", "Nerf de l'obturateur interne", "Nerf obturateur", "Contingent tibial du nerf ischiatique"],
   "Le carré fémoral et le jumeau inférieur sont innervés par le nerf du carré fémoral, branche du plexus sacral. L'obturateur interne et le jumeau supérieur sont innervés par le nerf de l'obturateur interne."),
  ("Welcher Nerv innerviert den M. quadratus femoris?", ["N. gluteus inferior", "N. musculi quadrati femoris (L4–S1)", "N. musculi obturatorii interni", "N. obturatorius", "Tibialer Anteil des N. ischiadicus"],
   "M. quadratus femoris und M. gemellus inferior werden vom N. musculi quadrati femoris aus dem Plexus sacralis innerviert. M. obturatorius internus und M. gemellus superior versorgt der N. musculi obturatorii interni."),
  ("¿Qué nervio inerva el cuadrado femoral?", ["Nervio glúteo inferior", "Nervio del cuadrado femoral (L4–S1)", "Nervio del obturador interno", "Nervio obturador", "División tibial del nervio ciático"],
   "El cuadrado femoral y el gemelo inferior los inerva el nervio del cuadrado femoral, del plexo sacro. El obturador interno y el gemelo superior los inerva el nervio del obturador interno."))

T("mu-5f7018d9",
  ("Which muscles form the floor of the femoral triangle?", ["Iliopsoas, pectineus and adductor longus", "Adductor magnus and semimembranosus", "Vastus medialis and vastus intermedius", "Sartorius and gracilis", "Gluteus medius and minimus"],
   "From lateral to medial the floor of the femoral triangle is formed by iliopsoas, pectineus and adductor longus; its roof is the fascia lata and cribriform fascia."),
  ("Quels muscles forment le plancher du triangle fémoral ?", ["Ilio-psoas, pectiné et long adducteur", "Grand adducteur et semi-membraneux", "Vaste médial et vaste intermédiaire", "Sartorius et gracile", "Moyen et petit glutéaux"],
   "De dehors en dedans, le plancher du triangle fémoral est formé par l'ilio-psoas, le pectiné et le long adducteur ; son toit est formé par le fascia lata et le fascia criblé."),
  ("Welche Muskeln bilden den Boden des Trigonum femorale?", ["M. iliopsoas, M. pectineus und M. adductor longus", "M. adductor magnus und M. semimembranosus", "M. vastus medialis und M. vastus intermedius", "M. sartorius und M. gracilis", "M. gluteus medius und minimus"],
   "Den Boden des Trigonum femorale bilden von lateral nach medial M. iliopsoas, M. pectineus und M. adductor longus; das Dach sind Fascia lata und Fascia cribrosa."),
  ("¿Qué músculos forman el suelo del triángulo femoral?", ["Iliopsoas, pectíneo y aductor largo", "Aductor mayor y semimembranoso", "Vasto medial y vasto intermedio", "Sartorio y grácil", "Glúteos medio y menor"],
   "De lateral a medial, el suelo del triángulo femoral lo forman el iliopsoas, el pectíneo y el aductor largo; su techo es la fascia lata y la fascia cribiforme."))

T("mu-617924a3",
  ("Which hamstring muscle tears most often in sprinters?", ["Short head of biceps femoris", "Hamstring part of adductor magnus", "Semitendinosus", "Long head of biceps femoris", "Semimembranosus"],
   "The long head of biceps femoris is the most frequently injured hamstring because it is overstretched eccentrically at the end of the swing phase of running."),
  ("Quel ischio-jambier se rompt le plus souvent chez les sprinteurs ?", ["Chef court du biceps fémoral", "Partie ischio-jambière du grand adducteur", "Semi-tendineux", "Chef long du biceps fémoral", "Semi-membraneux"],
   "Le chef long du biceps fémoral est l'ischio-jambier le plus souvent lésé, car il est fortement étiré en excentrique à la fin de la phase oscillante de la course."),
  ("Welcher ischiokrurale Muskel reißt bei Sprintern am häufigsten?", ["Caput breve des M. biceps femoris", "Ischiokruraler Anteil des M. adductor magnus", "M. semitendinosus", "Caput longum des M. biceps femoris", "M. semimembranosus"],
   "Das Caput longum des M. biceps femoris ist der am häufigsten verletzte ischiokrurale Muskel, da es am Ende der Schwungphase beim Laufen exzentrisch überdehnt wird."),
  ("¿Qué isquiotibial se rompe con más frecuencia en los velocistas?", ["Cabeza corta del bíceps femoral", "Porción isquiotibial del aductor mayor", "Semitendinoso", "Cabeza larga del bíceps femoral", "Semimembranoso"],
   "La cabeza larga del bíceps femoral es el isquiotibial que más se lesiona porque se estira excéntricamente en exceso al final de la fase de balanceo de la carrera."))

T("mu-ea64d105",
  ("What is the function of quadratus plantae?", ["Abducting the big toe", "Everting the foot", "Extending the toes", "Raising the medial arch", "Correcting the oblique pull of the FDL tendon so the toes flex straight"],
   "Quadratus plantae runs from the calcaneus to the lateral border of the FDL tendon; it corrects FDL's oblique pull from behind the medial malleolus so that the toes flex straight. It is supplied by the lateral plantar nerve."),
  ("Quelle est la fonction du carré plantaire ?", ["Mettre l'hallux en abduction", "Mettre le pied en éversion", "Étendre les orteils", "Élever l'arche médiale", "Corriger la traction oblique du long fléchisseur des orteils pour une flexion rectiligne"],
   "Le carré plantaire va du calcanéus au bord latéral du tendon du long fléchisseur des orteils ; il corrige la traction oblique de ce tendon venu de derrière la malléole médiale pour que les orteils fléchissent dans l'axe. Il est innervé par le nerf plantaire latéral."),
  ("Was ist die Funktion des M. quadratus plantae?", ["Die Großzehe abduzieren", "Den Fuß evertieren", "Die Zehen strecken", "Das mediale Längsgewölbe heben", "Den schrägen Zug der FDL-Sehne ausgleichen, damit die Zehen gerade gebeugt werden"],
   "Der M. quadratus plantae zieht vom Calcaneus zum Außenrand der Sehne des M. flexor digitorum longus; er gleicht deren schrägen Zug hinter dem Innenknöchel aus, sodass die Zehen gerade gebeugt werden. Er wird vom N. plantaris lateralis innerviert."),
  ("¿Cuál es la función del cuadrado plantar?", ["Abducir el dedo gordo", "Evertir el pie", "Extender los dedos", "Elevar el arco medial", "Corregir la tracción oblicua del tendón del FDL para que los dedos se flexionen en línea recta"],
   "El cuadrado plantar va del calcáneo al borde lateral del tendón del flexor largo de los dedos; corrige su tracción oblicua desde detrás del maléolo medial para que los dedos se flexionen rectos. Lo inerva el nervio plantar lateral."))

T("mu-e51f982b",
  ("After total hip replacement a patient cannot lift the foot (foot drop) and has numbness on the outer side of the leg. What is the most likely damage?", ["Femoral nerve injury", "Tibial nerve injury", "Obturator nerve injury", "Injury of the fibular division of the sciatic nerve", "Superior gluteal nerve injury"],
   "In hip surgery the fibular division of the sciatic nerve, more superficial and protected by less connective tissue, is injured more often; dorsiflexion and eversion are lost, with sensory loss on the outer leg."),
  ("Après une prothèse totale de hanche, un patient ne peut relever le pied (pied tombant) et présente une hypoesthésie de la face latérale de la jambe. Quelle est la lésion la plus probable ?", ["Lésion du nerf fémoral", "Lésion du nerf tibial", "Lésion du nerf obturateur", "Lésion du contingent fibulaire du nerf ischiatique", "Lésion du nerf glutéal supérieur"],
   "En chirurgie de hanche, le contingent fibulaire du nerf ischiatique, plus superficiel et moins protégé par le tissu conjonctif, est le plus souvent lésé ; on perd la flexion dorsale et l'éversion, avec une hypoesthésie de la face latérale de la jambe."),
  ("Nach einer Hüfttotalendoprothese kann ein Patient den Fuß nicht heben (Fallfuß) und hat Taubheit an der Außenseite des Unterschenkels. Welche Schädigung ist am wahrscheinlichsten?", ["Läsion des N. femoralis", "Läsion des N. tibialis", "Läsion des N. obturatorius", "Läsion des fibularen Anteils des N. ischiadicus", "Läsion des N. gluteus superior"],
   "Bei Hüftoperationen wird der oberflächlicher gelegene und durch weniger Bindegewebe geschützte fibulare Anteil des N. ischiadicus häufiger verletzt; Dorsalextension und Eversion fallen aus, dazu Sensibilitätsverlust an der Unterschenkelaußenseite."),
  ("Tras una prótesis total de cadera el paciente no puede levantar el pie (pie caído) y tiene entumecimiento en la cara lateral de la pierna. ¿Cuál es la lesión más probable?", ["Lesión del nervio femoral", "Lesión del nervio tibial", "Lesión del nervio obturador", "Lesión de la división peronea del nervio ciático", "Lesión del nervio glúteo superior"],
   "En la cirugía de cadera se lesiona con más frecuencia la división peronea del ciático, más superficial y menos protegida por tejido conjuntivo; se pierden la flexión dorsal y la eversión, con pérdida sensitiva en la cara lateral de la pierna."))
