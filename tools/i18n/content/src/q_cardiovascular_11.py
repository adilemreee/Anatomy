KIND = "questions"
SYSTEM = "cardiovascular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("cv-82eb6ab5",
  ("What are the terminal branches of the popliteal artery?", ["Anterior and posterior tibial arteries", "Dorsalis pedis and fibular arteries", "Femoral and profunda femoris arteries", "Superior genicular arteries", "Medial and lateral plantar arteries"],
   "The popliteal artery divides at the lower border of popliteus into the anterior and posterior tibial arteries; the fibular artery arises from the posterior tibial artery."),
  ("Quelles sont les branches terminales de l'artère poplitée ?", ["Artères tibiales antérieure et postérieure", "Artères dorsale du pied et fibulaire", "Artères fémorale et profonde de la cuisse", "Artères supérieures du genou", "Artères plantaires médiale et latérale"],
   "L'artère poplitée se divise au bord inférieur du muscle poplité en artères tibiales antérieure et postérieure ; l'artère fibulaire naît de la tibiale postérieure."),
  ("Was sind die Endäste der A. poplitea?", ["A. tibialis anterior und A. tibialis posterior", "A. dorsalis pedis und A. fibularis", "A. femoralis und A. profunda femoris", "Aa. genus superiores", "A. plantaris medialis und lateralis"],
   "Die A. poplitea teilt sich am Unterrand des M. popliteus in A. tibialis anterior und posterior; die A. fibularis entspringt aus der A. tibialis posterior."),
  ("¿Cuáles son las ramas terminales de la arteria poplítea?", ["Arterias tibiales anterior y posterior", "Arterias dorsal del pie y peronea", "Arterias femoral y femoral profunda", "Arterias geniculares superiores", "Arterias plantares medial y lateral"],
   "La poplítea se divide en el borde inferior del músculo poplíteo en las tibiales anterior y posterior; la peronea nace de la tibial posterior."))

T("cv-2167b2de",
  ("Where is the posterior tibial pulse taken?", ["Behind the knee", "In front of the lateral malleolus", "Behind the medial malleolus", "In the groin", "On the dorsum of the foot"],
   "The posterior tibial artery is superficial between the medial malleolus and the Achilles tendon, where its pulse is taken."),
  ("Où prend-on le pouls tibial postérieur ?", ["Derrière le genou", "En avant de la malléole latérale", "En arrière de la malléole médiale", "Au pli de l'aine", "Sur le dos du pied"],
   "L'artère tibiale postérieure est superficielle entre la malléole médiale et le tendon calcanéen ; c'est là qu'on prend son pouls."),
  ("Wo wird der Puls der A. tibialis posterior getastet?", ["In der Kniekehle", "Vor dem Außenknöchel", "Hinter dem Innenknöchel", "In der Leiste", "Auf dem Fußrücken"],
   "Die A. tibialis posterior liegt zwischen Innenknöchel und Achillessehne oberflächlich; dort wird ihr Puls getastet."),
  ("¿Dónde se toma el pulso tibial posterior?", ["Detrás de la rodilla", "Delante del maléolo lateral", "Detrás del maléolo medial", "En la ingle", "En el dorso del pie"],
   "La tibial posterior es superficial entre el maléolo medial y el tendón de Aquiles; ahí se toma su pulso."))

T("cv-d0b5e87d",
  ("Which is the largest vein of the body?", ["Internal jugular vein", "Inferior vena cava", "Hepatic portal vein", "Superior vena cava", "Femoral vein"],
   "The inferior vena cava carries the blood of all body parts below the diaphragm to the right atrium and is the largest vein of the body."),
  ("Quelle est la plus grosse veine du corps ?", ["Veine jugulaire interne", "Veine cave inférieure", "Veine porte hépatique", "Veine cave supérieure", "Veine fémorale"],
   "La veine cave inférieure ramène à l'atrium droit le sang de toutes les régions situées sous le diaphragme ; c'est la plus grosse veine du corps."),
  ("Welches ist die größte Vene des Körpers?", ["V. jugularis interna", "V. cava inferior", "V. portae hepatis", "V. cava superior", "V. femoralis"],
   "Die untere Hohlvene führt das Blut aller Körperteile unterhalb des Zwerchfells zum rechten Vorhof und ist die größte Vene des Körpers."),
  ("¿Cuál es la vena más grande del cuerpo?", ["Vena yugular interna", "Vena cava inferior", "Vena porta hepática", "Vena cava superior", "Vena femoral"],
   "La vena cava inferior lleva a la aurícula derecha la sangre de todas las regiones por debajo del diafragma; es la vena más grande del cuerpo."))

T("cv-ad43d739",
  ("Which main vein brings blood from the head, neck and arms to the heart?", ["Coronary sinus", "Azygos vein", "Hepatic portal vein", "Superior vena cava", "Inferior vena cava"],
   "The superior vena cava is formed by the union of the two brachiocephalic veins and brings blood from regions above the diaphragm to the right atrium."),
  ("Quelle grande veine ramène au cœur le sang de la tête, du cou et des membres supérieurs ?", ["Sinus coronaire", "Veine azygos", "Veine porte hépatique", "Veine cave supérieure", "Veine cave inférieure"],
   "La veine cave supérieure naît de la réunion des deux veines brachio-céphaliques et ramène à l'atrium droit le sang des régions situées au-dessus du diaphragme."),
  ("Welche Hauptvene führt das Blut von Kopf, Hals und Armen zum Herzen?", ["Sinus coronarius", "V. azygos", "V. portae hepatis", "V. cava superior", "V. cava inferior"],
   "Die obere Hohlvene entsteht aus dem Zusammenfluss der beiden Vv. brachiocephalicae und führt das Blut der Regionen oberhalb des Zwerchfells zum rechten Vorhof."),
  ("¿Qué vena principal lleva al corazón la sangre de la cabeza, el cuello y los brazos?", ["Seno coronario", "Vena ácigos", "Vena porta hepática", "Vena cava superior", "Vena cava inferior"],
   "La vena cava superior se forma por la unión de las dos braquiocefálicas y lleva a la aurícula derecha la sangre de las regiones por encima del diafragma."))

T("cv-7aff291e",
  ("Which is the longest vein of the body?", ["Small saphenous vein", "Inferior vena cava", "Cephalic vein", "Femoral vein", "Great saphenous vein"],
   "The great saphenous vein is the superficial vein running along the medial side of the leg from the dorsum of the foot to the groin; it is the longest vein of the body."),
  ("Quelle est la plus longue veine du corps ?", ["Petite veine saphène", "Veine cave inférieure", "Veine céphalique", "Veine fémorale", "Grande veine saphène"],
   "La grande veine saphène est la veine superficielle qui monte à la face médiale du membre inférieur, du dos du pied jusqu'à l'aine ; c'est la plus longue veine du corps."),
  ("Welches ist die längste Vene des Körpers?", ["V. saphena parva", "V. cava inferior", "V. cephalica", "V. femoralis", "V. saphena magna"],
   "Die V. saphena magna ist die oberflächliche Vene, die an der Innenseite des Beins vom Fußrücken bis zur Leiste zieht; sie ist die längste Vene des Körpers."),
  ("¿Cuál es la vena más larga del cuerpo?", ["Vena safena menor", "Vena cava inferior", "Vena cefálica", "Vena femoral", "Vena safena mayor"],
   "La safena mayor es la vena superficial que recorre la cara medial del miembro inferior desde el dorso del pie hasta la ingle; es la vena más larga del cuerpo."))

T("cv-a4e595f7",
  ("Which vein carries nutrient-rich blood from the digestive tract to the liver?", ["Renal vein", "Hepatic veins", "Inferior vena cava", "Hepatic portal vein", "Azygos vein"],
   "The portal vein carries blood from the stomach, intestines, spleen and pancreas to the liver; blood filtered by the liver returns to the IVC via the hepatic veins."),
  ("Quelle veine transporte vers le foie le sang riche en nutriments venant du tube digestif ?", ["Veine rénale", "Veines hépatiques", "Veine cave inférieure", "Veine porte hépatique", "Veine azygos"],
   "La veine porte conduit au foie le sang de l'estomac, de l'intestin, de la rate et du pancréas ; le sang filtré par le foie rejoint la VCI par les veines hépatiques."),
  ("Welche Vene bringt das nährstoffreiche Blut aus dem Verdauungstrakt zur Leber?", ["V. renalis", "Vv. hepaticae", "V. cava inferior", "V. portae hepatis", "V. azygos"],
   "Die Pfortader bringt das Blut von Magen, Darm, Milz und Pankreas zur Leber; das von der Leber gefilterte Blut gelangt über die Lebervenen in die V. cava inferior."),
  ("¿Qué vena lleva al hígado la sangre rica en nutrientes del tubo digestivo?", ["Vena renal", "Venas hepáticas", "Vena cava inferior", "Vena porta hepática", "Vena ácigos"],
   "La vena porta lleva al hígado la sangre del estómago, el intestino, el bazo y el páncreas; la sangre filtrada por el hígado vuelve a la VCI por las venas hepáticas."))

T("cv-eec7bdee",
  ("Which structure prevents backflow of blood in veins?", ["Venous valves", "Elastic membrane", "Thick muscle layer of the tunica media", "Precapillary sphincters", "Papillary muscles"],
   "Valves, especially in the leg veins, make blood flow one way towards the heart. Valve incompetence leads to varicose veins."),
  ("Quelle structure empêche le reflux du sang dans les veines ?", ["Valvules veineuses", "Membrane élastique", "Épaisse couche musculaire de la média", "Sphincters précapillaires", "Muscles papillaires"],
   "Les valvules, surtout dans les veines des membres inférieurs, imposent un écoulement unidirectionnel vers le cœur. Leur insuffisance entraîne des varices."),
  ("Welche Struktur verhindert den Rückfluss des Blutes in den Venen?", ["Venenklappen", "Elastische Membran", "Dicke Muskelschicht der Tunica media", "Präkapilläre Sphinkter", "Papillarmuskeln"],
   "Venenklappen, besonders in den Beinvenen, sorgen für den Einbahnfluss zum Herzen. Eine Klappeninsuffizienz führt zu Krampfadern."),
  ("¿Qué estructura impide el reflujo de la sangre en las venas?", ["Válvulas venosas", "Membrana elástica", "Gruesa capa muscular de la túnica media", "Esfínteres precapilares", "Músculos papilares"],
   "Las válvulas, sobre todo en las venas de las piernas, hacen que la sangre fluya en un solo sentido hacia el corazón. Su insuficiencia produce varices."))

T("cv-a92d99f7",
  ("In which phase of the cardiac cycle do the coronary arteries fill most?", ["Ejection", "Atrial systole", "Systole", "Diastole", "Isovolumetric contraction"],
   "In systole the contracting myocardium compresses the coronary vessels; left ventricular coronary flow occurs mainly in diastole. That is why coronary perfusion falls in tachycardia, when diastole shortens."),
  ("Pendant quelle phase du cycle cardiaque les artères coronaires se remplissent-elles le plus ?", ["Éjection", "Systole atriale", "Systole", "Diastole", "Contraction isovolumique"],
   "En systole, le myocarde contracté comprime les vaisseaux coronaires ; le débit coronaire du ventricule gauche est surtout diastolique. C'est pourquoi la perfusion coronaire baisse en cas de tachycardie, quand la diastole raccourcit."),
  ("In welcher Phase des Herzzyklus füllen sich die Koronararterien am stärksten?", ["Austreibung", "Vorhofsystole", "Systole", "Diastole", "Isovolumetrische Anspannung"],
   "In der Systole drückt das kontrahierte Myokard die Koronargefäße zusammen; der Koronarfluss der linken Kammer erfolgt vor allem in der Diastole. Deshalb sinkt bei Tachykardie mit verkürzter Diastole die Koronarperfusion."),
  ("¿En qué fase del ciclo cardíaco se llenan más las arterias coronarias?", ["Eyección", "Sístole auricular", "Sístole", "Diástole", "Contracción isovolumétrica"],
   "En sístole el miocardio contraído comprime los vasos coronarios; el flujo coronario del ventrículo izquierdo es sobre todo diastólico. Por eso en la taquicardia, al acortarse la diástole, disminuye la perfusión coronaria."))

T("cv-6061f2af",
  ("Into which two branches does the left main coronary artery divide?", ["Anterior interventricular branch (LAD) and circumflex branch", "Right marginal branch and circumflex branch", "Anterior and posterior interventricular branches", "Circumflex and posterior interventricular branches", "Sinuatrial nodal artery and atrioventricular nodal artery"],
   "The left main coronary is a short trunk; it divides into the LAD, descending in the anterior interventricular groove, and the circumflex branch, which runs in the left AV groove around to the back of the heart."),
  ("En quelles deux branches le tronc commun de la coronaire gauche se divise-t-il ?", ["Rameau interventriculaire antérieur (IVA) et rameau circonflexe", "Rameau marginal droit et rameau circonflexe", "Rameaux interventriculaires antérieur et postérieur", "Rameau circonflexe et rameau interventriculaire postérieur", "Artère du nœud sinusal et artère du nœud atrio-ventriculaire"],
   "Le tronc commun gauche est court ; il se divise en IVA, qui descend dans le sillon interventriculaire antérieur, et en circonflexe, qui contourne le cœur dans le sillon atrio-ventriculaire gauche."),
  ("In welche zwei Äste teilt sich der Hauptstamm der linken Koronararterie?", ["R. interventricularis anterior (RIVA) und R. circumflexus", "R. marginalis dexter und R. circumflexus", "R. interventricularis anterior und posterior", "R. circumflexus und R. interventricularis posterior", "A. nodi sinuatrialis und A. nodi atrioventricularis"],
   "Der linke Hauptstamm ist kurz; er teilt sich in den RIVA, der im Sulcus interventricularis anterior absteigt, und den R. circumflexus, der in der linken AV-Furche zur Herzhinterwand zieht."),
  ("¿En qué dos ramas se divide el tronco de la coronaria izquierda?", ["Rama interventricular anterior (DA) y rama circunfleja", "Rama marginal derecha y rama circunfleja", "Ramas interventriculares anterior y posterior", "Rama circunfleja y rama interventricular posterior", "Arteria del nodo sinoauricular y arteria del nodo auriculoventricular"],
   "El tronco coronario izquierdo es corto; se divide en la descendente anterior, que baja por el surco interventricular anterior, y la circunfleja, que rodea el corazón por el surco AV izquierdo hasta la cara posterior."))

T("cv-4e8377fa",
  ("Where does the coronary sinus open?", ["Into the right atrium", "Into the right ventricle", "Into the superior vena cava", "Into the left atrium", "Into the azygos vein"],
   "The coronary sinus lies in the AV groove on the back of the heart, collects most of the cardiac veins and opens into the right atrium between the IVC opening and the tricuspid valve."),
  ("Où s'abouche le sinus coronaire ?", ["Dans l'atrium droit", "Dans le ventricule droit", "Dans la veine cave supérieure", "Dans l'atrium gauche", "Dans la veine azygos"],
   "Le sinus coronaire se trouve dans le sillon atrio-ventriculaire à la face postérieure du cœur ; il recueille la plupart des veines cardiaques et s'abouche dans l'atrium droit entre l'orifice de la VCI et la valve tricuspide."),
  ("Wohin mündet der Sinus coronarius?", ["In den rechten Vorhof", "In die rechte Kammer", "In die V. cava superior", "In den linken Vorhof", "In die V. azygos"],
   "Der Sinus coronarius liegt in der AV-Furche der Herzhinterwand, sammelt die meisten Herzvenen und mündet zwischen der Öffnung der V. cava inferior und der Trikuspidalklappe in den rechten Vorhof."),
  ("¿Dónde desemboca el seno coronario?", ["En la aurícula derecha", "En el ventrículo derecho", "En la vena cava superior", "En la aurícula izquierda", "En la vena ácigos"],
   "El seno coronario está en el surco AV de la cara posterior del corazón, recoge la mayoría de las venas cardíacas y desemboca en la aurícula derecha entre el orificio de la VCI y la válvula tricúspide."))

T("cv-428cedc8",
  ("How do the semilunar (aortic and pulmonary) valves differ from the AV valves?", ["They have four cusps.", "They have no chordae tendineae or papillary muscles.", "They close in systole.", "They are not attached to the fibrous skeleton.", "They lie inside the ventricle."],
   "Semilunar valves consist of three half-moon cusps that close when their pockets fill as blood starts to flow back; they have no chordae tendineae or papillary muscle support."),
  ("En quoi les valves sigmoïdes (aortique et pulmonaire) diffèrent-elles des valves atrio-ventriculaires ?", ["Elles ont quatre valvules.", "Elles n'ont ni cordages tendineux ni muscles papillaires.", "Elles se ferment en systole.", "Elles ne s'attachent pas au squelette fibreux.", "Elles se trouvent dans le ventricule."],
   "Les valves sigmoïdes comportent trois valvules en nid de pigeon qui se ferment lorsque leurs poches se remplissent au début du reflux ; elles n'ont ni cordages ni muscles papillaires."),
  ("Worin unterscheiden sich die Taschenklappen (Aorten- und Pulmonalklappe) von den AV-Klappen?", ["Sie haben vier Taschen.", "Sie haben keine Chordae tendineae und keine Papillarmuskeln.", "Sie schließen sich in der Systole.", "Sie sind nicht am Herzskelett befestigt.", "Sie liegen in der Kammer."],
   "Taschenklappen bestehen aus drei halbmondförmigen Taschen, die sich schließen, wenn sie sich beim beginnenden Rückfluss füllen; sie haben weder Chordae tendineae noch Papillarmuskeln."),
  ("¿En qué se diferencian las válvulas semilunares (aórtica y pulmonar) de las AV?", ["Tienen cuatro valvas.", "No tienen cuerdas tendinosas ni músculos papilares.", "Se cierran en sístole.", "No se fijan al esqueleto fibroso.", "Están dentro del ventrículo."],
   "Las semilunares tienen tres valvas en media luna que se cierran cuando sus bolsillos se llenan al empezar el reflujo; no tienen cuerdas tendinosas ni músculos papilares."))

T("cv-77a5a53e",
  ("The first heart sound (S1) is produced by the closure of what?", ["The ductus arteriosus", "The aortic valve only", "The mitral and tricuspid (AV) valves", "The foramen ovale", "The aortic and pulmonary valves"],
   "S1 is produced by closure of the AV valves at the start of ventricular systole, S2 by closure of the semilunar valves at the end of systole."),
  ("Le premier bruit du cœur (B1) est produit par la fermeture de quoi ?", ["Du canal artériel", "De la seule valve aortique", "Des valves mitrale et tricuspide (atrio-ventriculaires)", "Du foramen ovale", "Des valves aortique et pulmonaire"],
   "B1 est dû à la fermeture des valves atrio-ventriculaires au début de la systole ventriculaire, B2 à celle des valves sigmoïdes à la fin de la systole."),
  ("Der erste Herzton (S1) entsteht durch den Schluss wovon?", ["Des Ductus arteriosus", "Nur der Aortenklappe", "Der Mitral- und Trikuspidalklappe (AV-Klappen)", "Des Foramen ovale", "Der Aorten- und Pulmonalklappe"],
   "Der 1. Herzton entsteht durch den Schluss der AV-Klappen zu Beginn der Kammersystole, der 2. durch den Schluss der Taschenklappen am Ende der Systole."),
  ("¿El primer ruido cardíaco (R1) se produce por el cierre de qué?", ["Del conducto arterioso", "Solo de la válvula aórtica", "De las válvulas mitral y tricúspide (AV)", "Del foramen oval", "De las válvulas aórtica y pulmonar"],
   "R1 se debe al cierre de las válvulas AV al inicio de la sístole ventricular y R2 al de las semilunares al final de la sístole."))

T("cv-dacff9e8",
  ("From which aortic sinus does the right coronary artery arise, and in which groove does it run?", ["Right aortic sinus – anterior interventricular groove", "Non-coronary sinus – posterior interventricular groove", "Left aortic sinus – anterior interventricular groove", "Left aortic sinus – left AV groove", "Right aortic sinus – right atrioventricular (coronary) groove"],
   "The right coronary artery arises from the right aortic sinus, passes between the right auricle and the pulmonary trunk into the right AV groove and runs around to the back of the heart."),
  ("De quel sinus aortique naît la coronaire droite et dans quel sillon chemine-t-elle ?", ["Sinus aortique droit – sillon interventriculaire antérieur", "Sinus non coronaire – sillon interventriculaire postérieur", "Sinus aortique gauche – sillon interventriculaire antérieur", "Sinus aortique gauche – sillon atrio-ventriculaire gauche", "Sinus aortique droit – sillon atrio-ventriculaire (coronaire) droit"],
   "La coronaire droite naît du sinus aortique droit, passe entre l'auricule droit et le tronc pulmonaire, gagne le sillon atrio-ventriculaire droit et contourne le cœur jusqu'à sa face postérieure."),
  ("Aus welchem Aortensinus entspringt die rechte Koronararterie und in welcher Furche verläuft sie?", ["Rechter Aortensinus – Sulcus interventricularis anterior", "Akoronarer Sinus – Sulcus interventricularis posterior", "Linker Aortensinus – Sulcus interventricularis anterior", "Linker Aortensinus – linke AV-Furche", "Rechter Aortensinus – rechte AV-Furche (Sulcus coronarius)"],
   "Die rechte Koronararterie entspringt aus dem rechten Aortensinus, zieht zwischen rechtem Herzohr und Truncus pulmonalis in die rechte AV-Furche und läuft um das Herz zur Hinterwand."),
  ("¿De qué seno aórtico nace la coronaria derecha y por qué surco discurre?", ["Seno aórtico derecho – surco interventricular anterior", "Seno no coronario – surco interventricular posterior", "Seno aórtico izquierdo – surco interventricular anterior", "Seno aórtico izquierdo – surco AV izquierdo", "Seno aórtico derecho – surco auriculoventricular (coronario) derecho"],
   "La coronaria derecha nace del seno aórtico derecho, pasa entre la orejuela derecha y el tronco pulmonar, entra en el surco AV derecho y rodea el corazón hasta la cara posterior."))

T("cv-fcb9d64c",
  ("At which level does the aortic arch begin and end?", ["At C7", "At T12", "At L1", "At the xiphoid process (T9)", "At the sternal angle (T4–T5)"],
   "The aortic arch begins and ends in the plane through the sternal angle; this plane also corresponds to the tracheal bifurcation and the level where the azygos vein enters the SVC."),
  ("À quel niveau la crosse de l'aorte commence-t-elle et se termine-t-elle ?", ["En C7", "En T12", "En L1", "Au processus xiphoïde (T9)", "À l'angle sternal (T4–T5)"],
   "La crosse de l'aorte commence et se termine dans le plan passant par l'angle sternal ; ce plan correspond aussi à la bifurcation trachéale et à l'abouchement de la veine azygos dans la VCS."),
  ("In welcher Höhe beginnt und endet der Aortenbogen?", ["Bei C7", "Bei T12", "Bei L1", "Am Processus xiphoideus (T9)", "Am Angulus sterni (T4–T5)"],
   "Der Aortenbogen beginnt und endet in der Ebene durch den Angulus sterni; diese Ebene entspricht auch der Trachealbifurkation und der Mündung der V. azygos in die V. cava superior."),
  ("¿A qué nivel empieza y termina el cayado de la aorta?", ["En C7", "En T12", "En L1", "En la apófisis xifoides (T9)", "En el ángulo esternal (T4–T5)"],
   "El cayado aórtico empieza y termina en el plano que pasa por el ángulo esternal; este plano corresponde también a la bifurcación traqueal y a la desembocadura de la ácigos en la VCS."))

T("cv-d81fb0e2",
  ("At which vertebral levels do the coeliac trunk, superior mesenteric artery and inferior mesenteric artery arise, respectively?", ["T11, L1, L2", "T10, L1, L4", "T12, L1, L3", "L1, L2, L3", "T12, L2, L4"],
   "The coeliac trunk arises from the front of the aorta at T12, the SMA at L1 and the IMA at L3; the renal arteries arise at L1–L2 and the bifurcation is at L4."),
  ("À quels niveaux vertébraux naissent respectivement le tronc cœliaque, l'artère mésentérique supérieure et l'artère mésentérique inférieure ?", ["T11, L1, L2", "T10, L1, L4", "T12, L1, L3", "L1, L2, L3", "T12, L2, L4"],
   "Le tronc cœliaque naît de la face antérieure de l'aorte en T12, l'AMS en L1 et l'AMI en L3 ; les artères rénales naissent en L1–L2 et la bifurcation se fait en L4."),
  ("In welchen Wirbelhöhen entspringen Truncus coeliacus, A. mesenterica superior und A. mesenterica inferior?", ["T11, L1, L2", "T10, L1, L4", "T12, L1, L3", "L1, L2, L3", "T12, L2, L4"],
   "Der Truncus coeliacus entspringt bei T12, die A. mesenterica superior bei L1 und die A. mesenterica inferior bei L3 aus der Aortenvorderwand; die Nierenarterien bei L1–L2, die Bifurkation liegt bei L4."),
  ("¿A qué niveles vertebrales nacen, respectivamente, el tronco celíaco, la mesentérica superior y la mesentérica inferior?", ["T11, L1, L2", "T10, L1, L4", "T12, L1, L3", "L1, L2, L3", "T12, L2, L4"],
   "El tronco celíaco nace de la cara anterior de la aorta en T12, la AMS en L1 y la AMI en L3; las renales nacen en L1–L2 y la bifurcación está en L4."))

T("cv-1938d272",
  ("Where do the gonadal (testicular/ovarian) arteries arise?", ["From the internal iliac artery", "From the abdominal aorta, below the renal arteries (L2)", "From the renal artery", "From the inferior mesenteric artery", "From the external iliac artery"],
   "Because the gonads develop near the kidneys, their arteries arise high from the abdominal aorta and lengthen as the gonads descend. The left gonadal vein drains into the left renal vein."),
  ("D'où naissent les artères gonadiques (testiculaires/ovariques) ?", ["De l'artère iliaque interne", "De l'aorte abdominale, sous les artères rénales (L2)", "De l'artère rénale", "De l'artère mésentérique inférieure", "De l'artère iliaque externe"],
   "Les gonades se développant près des reins, leurs artères naissent haut sur l'aorte abdominale et s'allongent lors de leur descente. La veine gonadique gauche se jette dans la veine rénale gauche."),
  ("Wo entspringen die Keimdrüsenarterien (A. testicularis/ovarica)?", ["Aus der A. iliaca interna", "Aus der Bauchaorta unterhalb der Nierenarterien (L2)", "Aus der A. renalis", "Aus der A. mesenterica inferior", "Aus der A. iliaca externa"],
   "Da die Keimdrüsen nahe den Nieren entstehen, entspringen ihre Arterien hoch aus der Bauchaorta und verlängern sich beim Deszensus. Die linke Keimdrüsenvene mündet in die linke Nierenvene."),
  ("¿De dónde nacen las arterias gonadales (testiculares/ováricas)?", ["De la ilíaca interna", "De la aorta abdominal, por debajo de las renales (L2)", "De la arteria renal", "De la mesentérica inferior", "De la ilíaca externa"],
   "Como las gónadas se desarrollan cerca de los riñones, sus arterias nacen alto en la aorta abdominal y se alargan durante su descenso. La vena gonadal izquierda drena en la renal izquierda."))

T("cv-aeedc854",
  ("Through which opening does the vertebral artery enter the skull?", ["Carotid canal", "Foramen magnum", "Foramen lacerum", "Jugular foramen", "Foramen ovale"],
   "The vertebral artery ascends through the C6–C1 transverse foramina, winds over the posterior arch of the atlas and enters the skull through the foramen magnum."),
  ("Par quel orifice l'artère vertébrale pénètre-t-elle dans le crâne ?", ["Canal carotidien", "Foramen magnum", "Foramen déchiré", "Foramen jugulaire", "Foramen ovale"],
   "L'artère vertébrale monte dans les foramens transversaires de C6 à C1, contourne l'arc postérieur de l'atlas et entre dans le crâne par le foramen magnum."),
  ("Durch welche Öffnung tritt die A. vertebralis in den Schädel ein?", ["Canalis caroticus", "Foramen magnum", "Foramen lacerum", "Foramen jugulare", "Foramen ovale"],
   "Die A. vertebralis steigt durch die Foramina transversaria C6–C1 auf, windet sich über den hinteren Atlasbogen und tritt durch das Foramen magnum in den Schädel."),
  ("¿Por qué orificio entra la arteria vertebral en el cráneo?", ["Conducto carotídeo", "Agujero magno", "Agujero rasgado", "Agujero yugular", "Agujero oval"],
   "La vertebral asciende por los agujeros transversos de C6 a C1, rodea el arco posterior del atlas y entra en el cráneo por el agujero magno."))

T("cv-ae5c2252",
  ("What is the main area supplied by the middle cerebral artery?", ["Occipital lobe and visual cortex", "Lateral surface of the hemisphere (face and arm motor-sensory areas, language centres)", "Brainstem and cerebellum", "Medial surface of the hemisphere (leg area)", "Thalamus and hippocampus"],
   "In MCA occlusion there is marked weakness and sensory loss of the opposite face and arm, with aphasia in the dominant hemisphere; the leg is less affected."),
  ("Quel est le territoire principal de l'artère cérébrale moyenne ?", ["Lobe occipital et cortex visuel", "Face latérale de l'hémisphère (aires motrices et sensitives de la face et du membre supérieur, centres du langage)", "Tronc cérébral et cervelet", "Face médiale de l'hémisphère (aire du membre inférieur)", "Thalamus et hippocampe"],
   "Dans l'occlusion de l'ACM, on observe un déficit moteur et sensitif marqué de la face et du membre supérieur controlatéraux, avec aphasie si l'hémisphère est dominant ; le membre inférieur est moins touché."),
  ("Welches Gebiet versorgt die A. cerebri media hauptsächlich?", ["Okzipitallappen und Sehrinde", "Laterale Hemisphärenfläche (motorische und sensible Areale für Gesicht und Arm, Sprachzentren)", "Hirnstamm und Kleinhirn", "Mediale Hemisphärenfläche (Beinareal)", "Thalamus und Hippocampus"],
   "Beim Mediaverschluss treten ausgeprägte Lähmung und Sensibilitätsstörung von Gesicht und Arm der Gegenseite auf, bei dominanter Hemisphäre eine Aphasie; das Bein ist weniger betroffen."),
  ("¿Cuál es el territorio principal de la arteria cerebral media?", ["Lóbulo occipital y corteza visual", "Cara lateral del hemisferio (áreas motoras y sensitivas de cara y brazo, centros del lenguaje)", "Tronco del encéfalo y cerebelo", "Cara medial del hemisferio (área de la pierna)", "Tálamo e hipocampo"],
   "En la oclusión de la ACM hay debilidad y pérdida sensitiva marcadas de la cara y el brazo contralaterales, con afasia si el hemisferio es dominante; la pierna se afecta menos."))

T("cv-81f7e82f",
  ("In anterior cerebral artery occlusion, where is the paralysis most marked?", ["In both eyes", "In the leg on the same side", "In the leg on the opposite side", "In the face on the same side", "In the face and arm on the opposite side"],
   "The ACA supplies the medial surface of the hemisphere, including the leg area of the motor cortex; its occlusion causes marked weakness and sensory loss in the opposite leg."),
  ("Dans l'occlusion de l'artère cérébrale antérieure, où la paralysie est-elle la plus marquée ?", ["Aux deux yeux", "Au membre inférieur homolatéral", "Au membre inférieur controlatéral", "À la face homolatérale", "À la face et au membre supérieur controlatéraux"],
   "L'ACA irrigue la face médiale de l'hémisphère, dont l'aire motrice du membre inférieur ; son occlusion entraîne un déficit moteur et sensitif marqué du membre inférieur controlatéral."),
  ("Wo ist die Lähmung beim Verschluss der A. cerebri anterior am deutlichsten?", ["An beiden Augen", "Im gleichseitigen Bein", "Im gegenseitigen Bein", "Im gleichseitigen Gesicht", "In Gesicht und Arm der Gegenseite"],
   "Die A. cerebri anterior versorgt die mediale Hemisphärenfläche mit dem Beinareal des motorischen Kortex; ihr Verschluss führt zu ausgeprägter Lähmung und Sensibilitätsstörung des gegenseitigen Beins."),
  ("En la oclusión de la arteria cerebral anterior, ¿dónde es más marcada la parálisis?", ["En ambos ojos", "En la pierna del mismo lado", "En la pierna del lado opuesto", "En la cara del mismo lado", "En la cara y el brazo del lado opuesto"],
   "La ACA irriga la cara medial del hemisferio, incluida el área motora de la pierna; su oclusión produce debilidad y pérdida sensitiva marcadas en la pierna contralateral."))

T("cv-9199711f",
  ("At the lower border of which muscle does the axillary artery become the brachial artery?", ["Upper border of latissimus dorsi", "Coracobrachialis", "Pectoralis minor", "Deltoid", "Teres major"],
   "The axillary artery extends from the outer border of the 1st rib to the lower border of teres major, where it becomes the brachial artery."),
  ("Au bord inférieur de quel muscle l'artère axillaire devient-elle l'artère brachiale ?", ["Bord supérieur du grand dorsal", "Coraco-brachial", "Petit pectoral", "Deltoïde", "Grand rond"],
   "L'artère axillaire s'étend du bord latéral de la 1re côte au bord inférieur du grand rond, où elle devient l'artère brachiale."),
  ("Am Unterrand welches Muskels wird die A. axillaris zur A. brachialis?", ["Oberrand des M. latissimus dorsi", "M. coracobrachialis", "M. pectoralis minor", "M. deltoideus", "M. teres major"],
   "Die A. axillaris reicht vom Außenrand der 1. Rippe bis zum Unterrand des M. teres major; dort wird sie zur A. brachialis."),
  ("¿En el borde inferior de qué músculo la arteria axilar pasa a ser braquial?", ["Borde superior del dorsal ancho", "Coracobraquial", "Pectoral menor", "Deltoides", "Redondo mayor"],
   "La axilar se extiende desde el borde externo de la 1.ª costilla hasta el borde inferior del redondo mayor, donde pasa a ser la braquial."))

T("cv-ac2759c4",
  ("Which artery mainly forms the deep palmar arch?", ["Ulnar artery", "Median artery", "Anterior interosseous artery", "Radial artery", "Brachial artery"],
   "The radial artery enters the palm through the 1st interosseous space to form the deep arch, which is completed by the deep branch of the ulnar artery. The superficial arch is mainly the ulnar artery."),
  ("Quelle artère forme principalement l'arcade palmaire profonde ?", ["Artère ulnaire", "Artère médiane", "Artère interosseuse antérieure", "Artère radiale", "Artère brachiale"],
   "L'artère radiale pénètre dans la paume par le 1er espace interosseux pour former l'arcade profonde, complétée par la branche profonde de l'ulnaire. L'arcade superficielle est surtout formée par l'ulnaire."),
  ("Welche Arterie bildet hauptsächlich den tiefen Hohlhandbogen?", ["A. ulnaris", "A. mediana", "A. interossea anterior", "A. radialis", "A. brachialis"],
   "Die A. radialis tritt durch den 1. Zwischenknochenraum in die Hohlhand und bildet den tiefen Bogen, der vom R. palmaris profundus der A. ulnaris vervollständigt wird. Der oberflächliche Bogen stammt vorwiegend aus der A. ulnaris."),
  ("¿Qué arteria forma principalmente el arco palmar profundo?", ["Arteria cubital", "Arteria mediana", "Arteria interósea anterior", "Arteria radial", "Arteria braquial"],
   "La radial entra en la palma por el 1.er espacio interóseo y forma el arco profundo, que completa la rama profunda de la cubital. El arco superficial lo forma sobre todo la cubital."))

T("cv-069cff78",
  ("Which is the largest branch of the femoral artery in the thigh?", ["Superficial circumflex iliac artery", "Superficial epigastric artery", "Descending genicular artery", "Profunda femoris artery", "External pudendal artery"],
   "The profunda femoris arises about 4 cm below the inguinal ligament and is the main artery of the thigh muscles; it gives circumflex and perforating branches."),
  ("Quelle est la plus grosse branche de l'artère fémorale à la cuisse ?", ["Artère circonflexe iliaque superficielle", "Artère épigastrique superficielle", "Artère descendante du genou", "Artère profonde de la cuisse", "Artère pudendale externe"],
   "L'artère profonde de la cuisse naît environ 4 cm sous le ligament inguinal ; c'est l'artère principale des muscles de la cuisse, qui donne les circonflexes et les perforantes."),
  ("Welches ist der größte Ast der A. femoralis am Oberschenkel?", ["A. circumflexa ilium superficialis", "A. epigastrica superficialis", "A. descendens genus", "A. profunda femoris", "A. pudenda externa"],
   "Die A. profunda femoris entspringt etwa 4 cm unterhalb des Leistenbands und ist die Hauptarterie der Oberschenkelmuskulatur; sie gibt die Aa. circumflexae und perforantes ab."),
  ("¿Cuál es la rama más grande de la arteria femoral en el muslo?", ["Arteria circunfleja ilíaca superficial", "Arteria epigástrica superficial", "Arteria genicular descendente", "Arteria femoral profunda", "Arteria pudenda externa"],
   "La femoral profunda nace unos 4 cm por debajo del ligamento inguinal y es la arteria principal de los músculos del muslo; da las circunflejas y las perforantes."))
