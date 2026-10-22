KIND = "questions"
SYSTEM = "cardiovascular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("cv-a877168d",
  ("How many chambers does the heart have?", ["3", "6", "5", "4 (two atria, two ventricles)", "2"],
   "The heart consists of two atria and two ventricles. The right side pumps deoxygenated blood to the lungs, the left side oxygenated blood to the body."),
  ("Combien de cavités le cœur possède-t-il ?", ["3", "6", "5", "4 (deux atriums, deux ventricules)", "2"],
   "Le cœur comprend deux atriums (oreillettes) et deux ventricules. Le cœur droit envoie le sang désoxygéné aux poumons, le cœur gauche le sang oxygéné à l'organisme."),
  ("Wie viele Höhlen hat das Herz?", ["3", "6", "5", "4 (zwei Vorhöfe, zwei Kammern)", "2"],
   "Das Herz besteht aus zwei Vorhöfen und zwei Kammern. Die rechte Seite pumpt sauerstoffarmes Blut in die Lunge, die linke sauerstoffreiches Blut in den Körper."),
  ("¿Cuántas cavidades tiene el corazón?", ["3", "6", "5", "4 (dos aurículas, dos ventrículos)", "2"],
   "El corazón tiene dos aurículas y dos ventrículos. El lado derecho bombea sangre desoxigenada a los pulmones y el izquierdo sangre oxigenada al cuerpo."))

T("cv-94d9d190",
  ("What is the double-layered sac surrounding the heart called?", ["Pleura", "Peritoneum", "Pericardium", "Endocardium", "Myocardium"],
   "The pericardium is a sac with an outer fibrous layer and an inner serous layer (parietal and visceral). The endocardium lines the inside of the heart, the myocardium is the heart muscle."),
  ("Comment appelle-t-on le sac à double feuillet qui entoure le cœur ?", ["Plèvre", "Péritoine", "Péricarde", "Endocarde", "Myocarde"],
   "Le péricarde est un sac formé d'un feuillet fibreux externe et d'un feuillet séreux interne (pariétal et viscéral). L'endocarde tapisse l'intérieur du cœur, le myocarde est le muscle cardiaque."),
  ("Wie heißt der doppelwandige Beutel, der das Herz umhüllt?", ["Pleura", "Peritoneum", "Perikard (Herzbeutel)", "Endokard", "Myokard"],
   "Das Perikard ist ein Beutel aus einer äußeren fibrösen und einer inneren serösen Schicht (parietal und viszeral). Das Endokard kleidet das Herz innen aus, das Myokard ist der Herzmuskel."),
  ("¿Cómo se llama el saco de doble capa que rodea el corazón?", ["Pleura", "Peritoneo", "Pericardio", "Endocardio", "Miocardio"],
   "El pericardio es un saco con una capa fibrosa externa y una serosa interna (parietal y visceral). El endocardio tapiza el interior del corazón y el miocardio es el músculo cardíaco."))

T("cv-3db2d7ed",
  ("Which valve lies between the right atrium and the right ventricle?", ["Aortic valve", "Mitral valve", "Pulmonary valve", "Eustachian valve", "Tricuspid valve"],
   "The right atrioventricular valve has three cusps (tricuspid). Between the left atrium and left ventricle lies the two-cusped mitral valve."),
  ("Quelle valve se trouve entre l'atrium droit et le ventricule droit ?", ["Valve aortique", "Valve mitrale", "Valve pulmonaire", "Valvule d'Eustachi", "Valve tricuspide"],
   "La valve atrio-ventriculaire droite a trois cuspides (tricuspide). Entre l'atrium et le ventricule gauches se trouve la valve mitrale à deux cuspides."),
  ("Welche Klappe liegt zwischen rechtem Vorhof und rechter Kammer?", ["Aortenklappe", "Mitralklappe", "Pulmonalklappe", "Eustachi-Klappe", "Trikuspidalklappe"],
   "Die rechte Atrioventrikularklappe hat drei Segel (Trikuspidalklappe). Zwischen linkem Vorhof und linker Kammer liegt die zweisegelige Mitralklappe."),
  ("¿Qué válvula está entre la aurícula derecha y el ventrículo derecho?", ["Válvula aórtica", "Válvula mitral", "Válvula pulmonar", "Válvula de Eustaquio", "Válvula tricúspide"],
   "La válvula auriculoventricular derecha tiene tres valvas (tricúspide). Entre la aurícula y el ventrículo izquierdos está la válvula mitral, de dos valvas."))

T("cv-d1d99274",
  ("Which valve lies between the left atrium and the left ventricle?", ["Aortic valve", "Tricuspid valve", "Pulmonary valve", "Thebesian valve", "Mitral (bicuspid) valve"],
   "The mitral valve has two cusps, anterior and posterior; they are attached by chordae tendineae to the papillary muscles of the left ventricle."),
  ("Quelle valve se trouve entre l'atrium gauche et le ventricule gauche ?", ["Valve aortique", "Valve tricuspide", "Valve pulmonaire", "Valvule de Thebesius", "Valve mitrale (bicuspide)"],
   "La valve mitrale a deux cuspides, antérieure et postérieure ; elles sont reliées par les cordages tendineux aux muscles papillaires du ventricule gauche."),
  ("Welche Klappe liegt zwischen linkem Vorhof und linker Kammer?", ["Aortenklappe", "Trikuspidalklappe", "Pulmonalklappe", "Thebesius-Klappe", "Mitralklappe (Bikuspidalklappe)"],
   "Die Mitralklappe hat zwei Segel, ein vorderes und ein hinteres; sie sind über Chordae tendineae an den Papillarmuskeln der linken Kammer befestigt."),
  ("¿Qué válvula está entre la aurícula izquierda y el ventrículo izquierdo?", ["Válvula aórtica", "Válvula tricúspide", "Válvula pulmonar", "Válvula de Tebesio", "Válvula mitral (bicúspide)"],
   "La mitral tiene dos valvas, anterior y posterior, unidas por cuerdas tendinosas a los músculos papilares del ventrículo izquierdo."))

T("cv-26a232bf",
  ("Which heart chamber has the thickest wall?", ["All four chambers have equal walls", "Right atrium", "Right ventricle", "Left ventricle", "Left atrium"],
   "The left ventricle has the thickest wall because it pumps blood at high pressure to the whole body; it is about three times thicker than the right ventricle."),
  ("Quelle cavité cardiaque a la paroi la plus épaisse ?", ["Les quatre cavités ont la même paroi", "Atrium droit", "Ventricule droit", "Ventricule gauche", "Atrium gauche"],
   "Le ventricule gauche a la paroi la plus épaisse car il propulse le sang à haute pression dans tout l'organisme ; elle est environ trois fois plus épaisse que celle du ventricule droit."),
  ("Welche Herzhöhle hat die dickste Wand?", ["Alle vier Höhlen haben gleich dicke Wände", "Rechter Vorhof", "Rechte Kammer", "Linke Kammer", "Linker Vorhof"],
   "Die linke Kammer hat die dickste Wand, weil sie das Blut mit hohem Druck in den ganzen Körper pumpt; sie ist etwa dreimal so dick wie die rechte Kammer."),
  ("¿Qué cavidad cardíaca tiene la pared más gruesa?", ["Las cuatro cavidades tienen igual pared", "Aurícula derecha", "Ventrículo derecho", "Ventrículo izquierdo", "Aurícula izquierda"],
   "El ventrículo izquierdo tiene la pared más gruesa porque bombea la sangre a alta presión a todo el cuerpo; es unas tres veces más gruesa que la del derecho."))

T("cv-d6a24725",
  ("Which chamber forms the tip (apex) of the heart?", ["Left ventricle", "Right ventricle", "Left atrium", "Right atrium", "Left auricle"],
   "The apex of the heart is formed by the left ventricle and is felt in the left 5th intercostal space just medial to the midclavicular line (apex beat)."),
  ("Quelle cavité forme la pointe (apex) du cœur ?", ["Ventricule gauche", "Ventricule droit", "Atrium gauche", "Atrium droit", "Auricule gauche"],
   "L'apex du cœur est formé par le ventricule gauche et se palpe dans le 5e espace intercostal gauche, juste en dedans de la ligne médio-claviculaire (choc de pointe)."),
  ("Welche Höhle bildet die Herzspitze (Apex)?", ["Linke Kammer", "Rechte Kammer", "Linker Vorhof", "Rechter Vorhof", "Linkes Herzohr"],
   "Die Herzspitze wird von der linken Kammer gebildet und ist im linken 5. Interkostalraum knapp medial der Medioklavikularlinie tastbar (Herzspitzenstoß)."),
  ("¿Qué cavidad forma la punta (ápex) del corazón?", ["Ventrículo izquierdo", "Ventrículo derecho", "Aurícula izquierda", "Aurícula derecha", "Orejuela izquierda"],
   "El ápex del corazón lo forma el ventrículo izquierdo y se palpa en el 5.º espacio intercostal izquierdo, justo medial a la línea medioclavicular (latido de la punta)."))

T("cv-412b75c1",
  ("What are the arteries supplying the heart muscle called?", ["Bronchial arteries", "Intercostal arteries", "Pulmonary arteries", "Coronary arteries", "Pericardiacophrenic arteries"],
   "The right and left coronary arteries arise from the aortic sinuses at the root of the ascending aorta and supply the heart wall; their occlusion causes myocardial infarction."),
  ("Comment appelle-t-on les artères qui irriguent le muscle cardiaque ?", ["Artères bronchiques", "Artères intercostales", "Artères pulmonaires", "Artères coronaires", "Artères péricardo-phréniques"],
   "Les artères coronaires droite et gauche naissent des sinus aortiques à la racine de l'aorte ascendante et irriguent la paroi cardiaque ; leur occlusion provoque l'infarctus du myocarde."),
  ("Wie heißen die Arterien, die den Herzmuskel versorgen?", ["Aa. bronchiales", "Aa. intercostales", "Aa. pulmonales", "Koronararterien (Aa. coronariae)", "Aa. pericardiacophrenicae"],
   "Die rechte und linke Koronararterie entspringen aus den Aortensinus an der Wurzel der Aorta ascendens und versorgen die Herzwand; ihr Verschluss verursacht einen Herzinfarkt."),
  ("¿Cómo se llaman las arterias que irrigan el músculo cardíaco?", ["Arterias bronquiales", "Arterias intercostales", "Arterias pulmonares", "Arterias coronarias", "Arterias pericardiofrénicas"],
   "Las coronarias derecha e izquierda nacen de los senos aórticos en la raíz de la aorta ascendente e irrigan la pared cardíaca; su oclusión causa infarto de miocardio."))

T("cv-7d873071",
  ("What is the heart's natural pacemaker called?", ["Bundle of His", "Sinoatrial (SA) node", "Moderator band", "Purkinje fibres", "Atrioventricular (AV) node"],
   "The SA node lies in the right atrium beside the opening of the superior vena cava and initiates the heartbeat. The impulse then passes to the AV node, bundle of His, bundle branches and Purkinje fibres."),
  ("Comment appelle-t-on le stimulateur (pacemaker) naturel du cœur ?", ["Faisceau de His", "Nœud sinusal (sino-atrial)", "Bandelette modératrice", "Fibres de Purkinje", "Nœud atrio-ventriculaire"],
   "Le nœud sinusal se trouve dans l'atrium droit près de l'abouchement de la veine cave supérieure et déclenche les battements. L'influx gagne ensuite le nœud atrio-ventriculaire, le faisceau de His, ses branches et les fibres de Purkinje."),
  ("Wie heißt der natürliche Schrittmacher des Herzens?", ["His-Bündel", "Sinusknoten (Nodus sinuatrialis)", "Moderatorband", "Purkinje-Fasern", "AV-Knoten"],
   "Der Sinusknoten liegt im rechten Vorhof neben der Mündung der V. cava superior und löst den Herzschlag aus. Die Erregung läuft dann über AV-Knoten, His-Bündel, Tawara-Schenkel und Purkinje-Fasern."),
  ("¿Cómo se llama el marcapasos natural del corazón?", ["Haz de His", "Nodo sinoauricular (SA)", "Banda moderadora", "Fibras de Purkinje", "Nodo auriculoventricular (AV)"],
   "El nodo SA está en la aurícula derecha junto a la desembocadura de la vena cava superior e inicia el latido. El impulso pasa luego al nodo AV, al haz de His, sus ramas y las fibras de Purkinje."))

T("cv-05cc936f",
  ("From which heart chamber does the pulmonary circulation begin?", ["Coronary sinus", "Right ventricle", "Left ventricle", "Right atrium", "Left atrium"],
   "The pulmonary circulation starts from the right ventricle with the pulmonary trunk and ends in the left atrium via the pulmonary veins. The systemic circulation starts from the left ventricle with the aorta."),
  ("De quelle cavité cardiaque part la circulation pulmonaire ?", ["Sinus coronaire", "Ventricule droit", "Ventricule gauche", "Atrium droit", "Atrium gauche"],
   "La circulation pulmonaire part du ventricule droit par le tronc pulmonaire et se termine dans l'atrium gauche par les veines pulmonaires. La circulation systémique part du ventricule gauche par l'aorte."),
  ("Aus welcher Herzhöhle beginnt der Lungenkreislauf?", ["Sinus coronarius", "Rechte Kammer", "Linke Kammer", "Rechter Vorhof", "Linker Vorhof"],
   "Der Lungenkreislauf beginnt in der rechten Kammer mit dem Truncus pulmonalis und endet über die Lungenvenen im linken Vorhof. Der Körperkreislauf beginnt in der linken Kammer mit der Aorta."),
  ("¿De qué cavidad cardíaca parte la circulación pulmonar?", ["Seno coronario", "Ventrículo derecho", "Ventrículo izquierdo", "Aurícula derecha", "Aurícula izquierda"],
   "La circulación pulmonar parte del ventrículo derecho por el tronco pulmonar y termina en la aurícula izquierda por las venas pulmonares. La sistémica parte del ventrículo izquierdo por la aorta."))

T("cv-ec83a847",
  ("Which is the largest artery distributing oxygenated blood to the whole body?", ["Common carotid artery", "Inferior vena cava", "Pulmonary trunk", "Subclavian artery", "Aorta"],
   "The aorta leaves the left ventricle; through its ascending part, arch, thoracic and abdominal parts it carries blood to the whole systemic circulation."),
  ("Quelle est la plus grande artère qui distribue le sang oxygéné à tout l'organisme ?", ["Artère carotide commune", "Veine cave inférieure", "Tronc pulmonaire", "Artère subclavière", "Aorte"],
   "L'aorte naît du ventricule gauche ; par ses segments ascendant, crosse, thoracique et abdominal, elle irrigue toute la circulation systémique."),
  ("Welches ist die größte Arterie, die sauerstoffreiches Blut im ganzen Körper verteilt?", ["A. carotis communis", "V. cava inferior", "Truncus pulmonalis", "A. subclavia", "Aorta"],
   "Die Aorta entspringt der linken Kammer; mit Aorta ascendens, Aortenbogen, Pars thoracica und abdominalis versorgt sie den ganzen Körperkreislauf."),
  ("¿Cuál es la arteria más grande que distribuye la sangre oxigenada a todo el cuerpo?", ["Arteria carótida común", "Vena cava inferior", "Tronco pulmonar", "Arteria subclavia", "Aorta"],
   "La aorta sale del ventrículo izquierdo; con sus porciones ascendente, cayado, torácica y abdominal lleva sangre a toda la circulación sistémica."))

T("cv-7e929d6e",
  ("Which vessel carries deoxygenated blood from the heart to the lungs?", ["Aorta", "Pulmonary trunk (pulmonary artery)", "Superior vena cava", "Bronchial arteries", "Pulmonary veins"],
   "The pulmonary arteries are the only arteries carrying deoxygenated blood; they leave the right ventricle and go to the lungs."),
  ("Quel vaisseau transporte le sang désoxygéné du cœur vers les poumons ?", ["Aorte", "Tronc pulmonaire (artère pulmonaire)", "Veine cave supérieure", "Artères bronchiques", "Veines pulmonaires"],
   "Les artères pulmonaires sont les seules artères à transporter du sang désoxygéné ; elles partent du ventricule droit vers les poumons."),
  ("Welches Gefäß bringt sauerstoffarmes Blut vom Herzen zur Lunge?", ["Aorta", "Truncus pulmonalis (Lungenarterie)", "V. cava superior", "Aa. bronchiales", "Lungenvenen"],
   "Die Lungenarterien sind die einzigen Arterien mit sauerstoffarmem Blut; sie verlassen die rechte Kammer und ziehen zur Lunge."),
  ("¿Qué vaso lleva la sangre desoxigenada del corazón a los pulmones?", ["Aorta", "Tronco pulmonar (arteria pulmonar)", "Vena cava superior", "Arterias bronquiales", "Venas pulmonares"],
   "Las arterias pulmonares son las únicas arterias que llevan sangre desoxigenada; salen del ventrículo derecho hacia los pulmones."))

T("cv-98ef52a0",
  ("Which veins carry oxygenated blood?", ["Jugular veins", "Pulmonary veins", "Portal vein", "Superior and inferior venae cavae", "Coronary veins"],
   "The pulmonary veins bring oxygenated blood from the lungs to the left atrium; they are the only veins carrying oxygenated blood."),
  ("Quelles veines transportent du sang oxygéné ?", ["Veines jugulaires", "Veines pulmonaires", "Veine porte", "Veines caves supérieure et inférieure", "Veines coronaires"],
   "Les veines pulmonaires ramènent le sang oxygéné des poumons à l'atrium gauche ; ce sont les seules veines qui transportent du sang oxygéné."),
  ("Welche Venen führen sauerstoffreiches Blut?", ["Vv. jugulares", "Lungenvenen (Vv. pulmonales)", "V. portae", "V. cava superior und inferior", "Herzvenen"],
   "Die Lungenvenen bringen sauerstoffreiches Blut von der Lunge zum linken Vorhof; sie sind die einzigen Venen mit sauerstoffreichem Blut."),
  ("¿Qué venas llevan sangre oxigenada?", ["Venas yugulares", "Venas pulmonares", "Vena porta", "Venas cavas superior e inferior", "Venas coronarias"],
   "Las venas pulmonares llevan la sangre oxigenada de los pulmones a la aurícula izquierda; son las únicas venas que transportan sangre oxigenada."))

T("cv-37cfee07",
  ("What is the part of the aorta that curves to the left and backwards after leaving the heart called?", ["Ascending aorta", "Descending aorta", "Aortic bulb", "Aortic arch", "Aortic bifurcation"],
   "After rising, the ascending aorta curves backwards over the left main bronchus at T4 to form the aortic arch; three large branches to the head, neck and arms arise from the arch."),
  ("Comment appelle-t-on la partie de l'aorte qui s'incurve vers la gauche et en arrière après sa sortie du cœur ?", ["Aorte ascendante", "Aorte descendante", "Bulbe aortique", "Crosse (arc) de l'aorte", "Bifurcation aortique"],
   "Après son trajet ascendant, l'aorte s'incurve en arrière au-dessus de la bronche principale gauche en T4 pour former la crosse ; trois grosses branches destinées à la tête, au cou et aux membres supérieurs en naissent."),
  ("Wie heißt der Abschnitt der Aorta, der sich nach dem Herzaustritt nach links hinten krümmt?", ["Aorta ascendens", "Aorta descendens", "Bulbus aortae", "Arcus aortae (Aortenbogen)", "Bifurcatio aortae"],
   "Nach dem Aufstieg krümmt sich die Aorta ascendens auf Höhe T4 über den linken Hauptbronchus nach hinten und bildet den Aortenbogen; aus ihm gehen drei große Äste zu Kopf, Hals und Armen ab."),
  ("¿Cómo se llama la parte de la aorta que se curva hacia la izquierda y atrás tras salir del corazón?", ["Aorta ascendente", "Aorta descendente", "Bulbo aórtico", "Cayado (arco) de la aorta", "Bifurcación aórtica"],
   "Tras ascender, la aorta se curva hacia atrás sobre el bronquio principal izquierdo a la altura de T4 y forma el cayado; de él salen tres grandes ramas para la cabeza, el cuello y los brazos."))

T("cv-94dfc545",
  ("Which artery is used to take the pulse in the neck?", ["Subclavian artery", "Common carotid artery", "Vertebral artery", "Internal jugular vein", "Superior thyroid artery"],
   "The carotid pulse is taken at the level of the thyroid cartilage along the anterior border of sternocleidomastoid; in emergencies it is the most reliable central pulse."),
  ("Quelle artère utilise-t-on pour prendre le pouls au cou ?", ["Artère subclavière", "Artère carotide commune", "Artère vertébrale", "Veine jugulaire interne", "Artère thyroïdienne supérieure"],
   "Le pouls carotidien se prend à hauteur du cartilage thyroïde, le long du bord antérieur du sterno-cléido-mastoïdien ; en urgence, c'est le pouls central le plus fiable."),
  ("An welcher Arterie wird am Hals der Puls getastet?", ["A. subclavia", "A. carotis communis", "A. vertebralis", "V. jugularis interna", "A. thyroidea superior"],
   "Der Karotispuls wird in Höhe des Schildknorpels am Vorderrand des M. sternocleidomastoideus getastet; im Notfall ist er der zuverlässigste zentrale Puls."),
  ("¿En qué arteria se toma el pulso en el cuello?", ["Arteria subclavia", "Arteria carótida común", "Arteria vertebral", "Vena yugular interna", "Arteria tiroidea superior"],
   "El pulso carotídeo se toma a la altura del cartílago tiroides, en el borde anterior del esternocleidomastoideo; en urgencias es el pulso central más fiable."))

T("cv-f01b4115",
  ("Which neck artery supplies the anterior and middle parts of the brain and the eye?", ["External carotid artery", "Subclavian artery", "Vertebral artery", "Internal carotid artery", "Facial artery"],
   "The internal carotid artery enters the skull without giving branches in the neck; it supplies the eye through the ophthalmic artery and most of the hemispheres through the anterior and middle cerebral arteries."),
  ("Quelle artère du cou irrigue les parties antérieure et moyenne du cerveau et l'œil ?", ["Artère carotide externe", "Artère subclavière", "Artère vertébrale", "Artère carotide interne", "Artère faciale"],
   "La carotide interne pénètre dans le crâne sans donner de branche cervicale ; elle irrigue l'œil par l'artère ophtalmique et la majeure partie des hémisphères par les artères cérébrales antérieure et moyenne."),
  ("Welche Halsarterie versorgt vorderes und mittleres Gehirn sowie das Auge?", ["A. carotis externa", "A. subclavia", "A. vertebralis", "A. carotis interna", "A. facialis"],
   "Die A. carotis interna tritt ohne Halsäste in den Schädel ein; sie versorgt über die A. ophthalmica das Auge und über die A. cerebri anterior und media den größten Teil der Hemisphären."),
  ("¿Qué arteria del cuello irriga las partes anterior y media del cerebro y el ojo?", ["Arteria carótida externa", "Arteria subclavia", "Arteria vertebral", "Arteria carótida interna", "Arteria facial"],
   "La carótida interna entra en el cráneo sin dar ramas en el cuello; irriga el ojo por la arteria oftálmica y la mayor parte de los hemisferios por las cerebrales anterior y media."))

T("cv-8d543b43",
  ("What is the arterial ring at the base of the brain connecting the carotid and vertebrobasilar systems called?", ["Palmar arch", "Circle of Willis (circulus arteriosus cerebri)", "Venous arch", "Cavernous sinus", "Aortic arch"],
   "The circle of Willis links the anterior and posterior circulations and can provide collateral flow when an artery is occluded; most brain aneurysms develop on this ring."),
  ("Comment appelle-t-on l'anneau artériel de la base du cerveau qui relie les systèmes carotidien et vertébro-basilaire ?", ["Arcade palmaire", "Polygone de Willis (cercle artériel du cerveau)", "Arcade veineuse", "Sinus caverneux", "Crosse de l'aorte"],
   "Le polygone de Willis relie les circulations antérieure et postérieure et peut assurer une suppléance quand une artère s'occlut ; la plupart des anévrismes cérébraux se développent sur cet anneau."),
  ("Wie heißt der Arterienring an der Hirnbasis, der Karotis- und Vertebrobasilarsystem verbindet?", ["Arcus palmaris", "Circulus arteriosus cerebri (Willisii)", "Arcus venosus", "Sinus cavernosus", "Aortenbogen"],
   "Der Circulus arteriosus verbindet vorderen und hinteren Kreislauf und kann bei Verschluss einer Arterie einen Kollateralfluss ermöglichen; die meisten Hirnaneurysmen entstehen an diesem Ring."),
  ("¿Cómo se llama el anillo arterial de la base del cerebro que une los sistemas carotídeo y vertebrobasilar?", ["Arco palmar", "Polígono de Willis (círculo arterial del cerebro)", "Arco venoso", "Seno cavernoso", "Cayado de la aorta"],
   "El polígono de Willis une las circulaciones anterior y posterior y puede aportar flujo colateral si se ocluye una arteria; la mayoría de los aneurismas cerebrales se forman en este anillo."))

T("cv-40ea677c",
  ("The basilar artery is formed by the union of which arteries?", ["Internal carotid and vertebral arteries", "The two vertebral arteries", "The two internal carotid arteries", "The two subclavian arteries", "The two posterior cerebral arteries"],
   "The right and left vertebral arteries join at the pontomedullary junction to form the basilar artery, which supplies the brainstem, cerebellum and occipital lobe."),
  ("L'artère basilaire est formée par la réunion de quelles artères ?", ["Carotide interne et artère vertébrale", "Les deux artères vertébrales", "Les deux carotides internes", "Les deux artères subclavières", "Les deux artères cérébrales postérieures"],
   "Les artères vertébrales droite et gauche s'unissent à la jonction bulbo-pontique pour former l'artère basilaire, qui irrigue le tronc cérébral, le cervelet et le lobe occipital."),
  ("Aus der Vereinigung welcher Arterien entsteht die A. basilaris?", ["A. carotis interna und A. vertebralis", "Beide Aa. vertebrales", "Beide Aa. carotides internae", "Beide Aa. subclaviae", "Beide Aa. cerebri posteriores"],
   "Rechte und linke A. vertebralis vereinigen sich an der Grenze von Pons und Medulla zur A. basilaris; sie versorgt Hirnstamm, Kleinhirn und Okzipitallappen."),
  ("¿La arteria basilar se forma por la unión de qué arterias?", ["Carótida interna y arteria vertebral", "Las dos arterias vertebrales", "Las dos carótidas internas", "Las dos subclavias", "Las dos cerebrales posteriores"],
   "Las vertebrales derecha e izquierda se unen en el límite entre puente y bulbo para formar la basilar, que irriga el tronco del encéfalo, el cerebelo y el lóbulo occipital."))

T("cv-02933170",
  ("Into which two branches does the brachial artery divide in front of the elbow?", ["Radial and ulnar arteries", "Profunda brachii and radial arteries", "Axillary and subclavian arteries", "Superficial and deep palmar arches", "Anterior and posterior interosseous arteries"],
   "The brachial artery divides in the cubital fossa, at the level of the neck of the radius, into the radial and ulnar arteries."),
  ("En quelles deux branches l'artère brachiale se divise-t-elle au pli du coude ?", ["Artères radiale et ulnaire", "Artère profonde du bras et artère radiale", "Artères axillaire et subclavière", "Arcades palmaires superficielle et profonde", "Artères interosseuses antérieure et postérieure"],
   "L'artère brachiale se divise dans la fosse cubitale, à hauteur du col du radius, en artères radiale et ulnaire."),
  ("In welche zwei Äste teilt sich die A. brachialis in der Ellenbeuge?", ["A. radialis und A. ulnaris", "A. profunda brachii und A. radialis", "A. axillaris und A. subclavia", "Oberflächlicher und tiefer Hohlhandbogen", "A. interossea anterior und posterior"],
   "Die A. brachialis teilt sich in der Fossa cubitalis in Höhe des Radiushalses in A. radialis und A. ulnaris."),
  ("¿En qué dos ramas se divide la arteria braquial delante del codo?", ["Arterias radial y cubital", "Arteria braquial profunda y arteria radial", "Arterias axilar y subclavia", "Arcos palmares superficial y profundo", "Arterias interóseas anterior y posterior"],
   "La braquial se divide en la fosa cubital, a la altura del cuello del radio, en las arterias radial y cubital."))

T("cv-0111f3a8",
  ("Which artery is most often used to take the pulse at the wrist?", ["Anterior interosseous artery", "Ulnar artery", "Superficial palmar arch", "Radial artery", "Brachial artery"],
   "The radial pulse is easily felt on the thumb side of the wrist over the lower end of the radius."),
  ("Quelle artère utilise-t-on le plus souvent pour prendre le pouls au poignet ?", ["Artère interosseuse antérieure", "Artère ulnaire", "Arcade palmaire superficielle", "Artère radiale", "Artère brachiale"],
   "Le pouls radial se palpe facilement du côté du pouce, sur l'extrémité inférieure du radius."),
  ("An welcher Arterie wird der Puls am Handgelenk am häufigsten getastet?", ["A. interossea anterior", "A. ulnaris", "Arcus palmaris superficialis", "A. radialis", "A. brachialis"],
   "Der Radialispuls ist an der Daumenseite des Handgelenks über dem distalen Radius leicht tastbar."),
  ("¿En qué arteria se toma con más frecuencia el pulso en la muñeca?", ["Arteria interósea anterior", "Arteria cubital", "Arco palmar superficial", "Arteria radial", "Arteria braquial"],
   "El pulso radial se palpa fácilmente en el lado del pulgar de la muñeca, sobre el extremo inferior del radio."))

T("cv-b50a69cf",
  ("Into which arteries does the abdominal aorta divide at its lower end?", ["Femoral arteries", "Common iliac arteries", "Superior and inferior mesenteric arteries", "Internal iliac arteries", "Renal arteries"],
   "The abdominal aorta divides at L4 into the right and left common iliac arteries, which in turn divide into internal and external iliac arteries."),
  ("En quelles artères l'aorte abdominale se divise-t-elle à son extrémité inférieure ?", ["Artères fémorales", "Artères iliaques communes", "Artères mésentériques supérieure et inférieure", "Artères iliaques internes", "Artères rénales"],
   "L'aorte abdominale se divise en L4 en artères iliaques communes droite et gauche, qui se divisent à leur tour en iliaques internes et externes."),
  ("In welche Arterien teilt sich die Bauchaorta an ihrem unteren Ende?", ["Aa. femorales", "Aa. iliacae communes", "A. mesenterica superior und inferior", "Aa. iliacae internae", "Aa. renales"],
   "Die Bauchaorta teilt sich in Höhe L4 in die rechte und linke A. iliaca communis, die sich ihrerseits in A. iliaca interna und externa aufteilen."),
  ("¿En qué arterias se divide la aorta abdominal en su extremo inferior?", ["Arterias femorales", "Arterias ilíacas comunes", "Arterias mesentéricas superior e inferior", "Arterias ilíacas internas", "Arterias renales"],
   "La aorta abdominal se divide a la altura de L4 en las ilíacas comunes derecha e izquierda, que a su vez se dividen en ilíacas internas y externas."))

T("cv-a0f7e29b",
  ("Which arteries supply the kidneys?", ["Lumbar arteries", "Suprarenal arteries", "Renal arteries", "Testicular arteries", "Superior mesenteric artery"],
   "The renal arteries arise from both sides of the abdominal aorta at L1–L2; about one fifth of the cardiac output goes to the kidneys."),
  ("Quelles artères irriguent les reins ?", ["Artères lombales", "Artères surrénales", "Artères rénales", "Artères testiculaires", "Artère mésentérique supérieure"],
   "Les artères rénales naissent des deux côtés de l'aorte abdominale en L1–L2 ; environ un cinquième du débit cardiaque va aux reins."),
  ("Welche Arterien versorgen die Nieren?", ["Aa. lumbales", "Aa. suprarenales", "Aa. renales", "Aa. testiculares", "A. mesenterica superior"],
   "Die Nierenarterien entspringen in Höhe L1–L2 beidseits der Bauchaorta; etwa ein Fünftel des Herzzeitvolumens fließt durch die Nieren."),
  ("¿Qué arterias irrigan los riñones?", ["Arterias lumbares", "Arterias suprarrenales", "Arterias renales", "Arterias testiculares", "Arteria mesentérica superior"],
   "Las arterias renales nacen a ambos lados de la aorta abdominal a la altura de L1–L2; alrededor de una quinta parte del gasto cardíaco va a los riñones."))

T("cv-b6985d99",
  ("Which is the main artery of the thigh?", ["Internal iliac artery", "Obturator artery", "Anterior tibial artery", "Femoral artery", "Popliteal artery"],
   "The external iliac artery becomes the femoral artery after passing under the inguinal ligament; it runs the length of the thigh and becomes the popliteal artery behind the knee."),
  ("Quelle est l'artère principale de la cuisse ?", ["Artère iliaque interne", "Artère obturatrice", "Artère tibiale antérieure", "Artère fémorale", "Artère poplitée"],
   "L'artère iliaque externe devient l'artère fémorale après son passage sous le ligament inguinal ; elle parcourt toute la cuisse et devient l'artère poplitée derrière le genou."),
  ("Welches ist die Hauptarterie des Oberschenkels?", ["A. iliaca interna", "A. obturatoria", "A. tibialis anterior", "A. femoralis", "A. poplitea"],
   "Die A. iliaca externa heißt nach dem Durchtritt unter dem Leistenband A. femoralis; sie durchzieht den Oberschenkel und wird hinter dem Knie zur A. poplitea."),
  ("¿Cuál es la arteria principal del muslo?", ["Arteria ilíaca interna", "Arteria obturatriz", "Arteria tibial anterior", "Arteria femoral", "Arteria poplítea"],
   "La ilíaca externa pasa a llamarse femoral tras cruzar bajo el ligamento inguinal; recorre todo el muslo y se convierte en poplítea detrás de la rodilla."))
