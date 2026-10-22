KIND = "questions"
SYSTEM = "cardiovascular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("cv-bbed1d1f",
  ("Where do the hepatic veins open?", ["Into the right renal vein", "Into the portal vein", "Into the superior vena cava", "Into the azygos vein", "Directly into the inferior vena cava"],
   "The three large hepatic veins open directly into the IVC on the posterior surface of the liver. The portal vein, by contrast, brings blood to the liver."),
  ("Où s'abouchent les veines hépatiques ?", ["Dans la veine rénale droite", "Dans la veine porte", "Dans la veine cave supérieure", "Dans la veine azygos", "Directement dans la veine cave inférieure"],
   "Les trois grosses veines hépatiques s'abouchent directement dans la VCI à la face postérieure du foie. La veine porte, elle, apporte le sang au foie."),
  ("Wohin münden die Lebervenen?", ["In die rechte Nierenvene", "In die Pfortader", "In die V. cava superior", "In die V. azygos", "Direkt in die V. cava inferior"],
   "Die drei großen Lebervenen münden an der Leberrückseite direkt in die V. cava inferior. Die Pfortader dagegen führt der Leber Blut zu."),
  ("¿Dónde desembocan las venas hepáticas?", ["En la vena renal derecha", "En la vena porta", "En la vena cava superior", "En la vena ácigos", "Directamente en la vena cava inferior"],
   "Las tres grandes venas hepáticas desembocan directamente en la VCI en la cara posterior del hígado. La porta, en cambio, lleva sangre al hígado."))

T("cv-2673b4e2",
  ("Which structures drain cerebrospinal fluid (CSF) into the superior sagittal sinus?", ["Choroid plexus", "Emissary veins", "Ependymal cells", "Bridging veins", "Arachnoid granulations (Pacchionian bodies)"],
   "CSF is produced by the choroid plexus and absorbed through the arachnoid granulations into the dural venous sinuses, especially the superior sagittal sinus."),
  ("Quelles structures drainent le liquide cérébro-spinal (LCS) dans le sinus sagittal supérieur ?", ["Plexus choroïdes", "Veines émissaires", "Cellules épendymaires", "Veines ponts", "Granulations arachnoïdiennes (de Pacchioni)"],
   "Le LCS est sécrété par les plexus choroïdes et résorbé par les granulations arachnoïdiennes dans les sinus veineux de la dure-mère, surtout le sinus sagittal supérieur."),
  ("Welche Strukturen leiten den Liquor in den Sinus sagittalis superior ab?", ["Plexus choroideus", "Vv. emissariae", "Ependymzellen", "Brückenvenen", "Arachnoidalzotten (Pacchioni-Granulationen)"],
   "Der Liquor wird im Plexus choroideus gebildet und über die Arachnoidalzotten in die Sinus durae matris, vor allem den Sinus sagittalis superior, resorbiert."),
  ("¿Qué estructuras drenan el líquido cefalorraquídeo (LCR) al seno sagital superior?", ["Plexos coroideos", "Venas emisarias", "Células ependimarias", "Venas puente", "Granulaciones aracnoideas (de Pacchioni)"],
   "El LCR se produce en los plexos coroideos y se reabsorbe por las granulaciones aracnoideas hacia los senos venosos durales, sobre todo el sagital superior."))

T("cv-05c8ce40",
  ("Where does the thoracic duct drain?", ["Into the inferior vena cava", "Into the azygos vein", "Into the right venous angle", "Into the left venous angle (junction of the left internal jugular and subclavian veins)", "Into the left atrium"],
   "The thoracic duct, which collects most of the body's lymph, opens at the junction of the left internal jugular and subclavian veins; lymph from the right upper body reaches the right venous angle via the right lymphatic duct."),
  ("Où se jette le conduit thoracique ?", ["Dans la veine cave inférieure", "Dans la veine azygos", "Dans l'angle veineux droit", "Dans l'angle veineux gauche (confluent jugulaire interne–subclavière gauche)", "Dans l'atrium gauche"],
   "Le conduit thoracique, qui collecte la majeure partie de la lymphe, se jette au confluent des veines jugulaire interne et subclavière gauches ; la lymphe de la moitié supérieure droite rejoint l'angle veineux droit par le conduit lymphatique droit."),
  ("Wohin mündet der Ductus thoracicus?", ["In die V. cava inferior", "In die V. azygos", "In den rechten Venenwinkel", "In den linken Venenwinkel (Vereinigung von linker V. jugularis interna und V. subclavia)", "In den linken Vorhof"],
   "Der Ductus thoracicus sammelt den größten Teil der Lymphe und mündet in den linken Venenwinkel; die Lymphe der rechten oberen Körperhälfte gelangt über den Ductus lymphaticus dexter in den rechten Venenwinkel."),
  ("¿Dónde desemboca el conducto torácico?", ["En la vena cava inferior", "En la vena ácigos", "En el ángulo venoso derecho", "En el ángulo venoso izquierdo (unión de la yugular interna y la subclavia izquierdas)", "En la aurícula izquierda"],
   "El conducto torácico, que recoge la mayor parte de la linfa, desemboca en la unión de la yugular interna y la subclavia izquierdas; la linfa de la mitad superior derecha llega al ángulo venoso derecho por el conducto linfático derecho."))

T("cv-9c435315",
  ("In the fetal circulation, which vessel brings oxygenated blood from the placenta to the fetus?", ["Umbilical vein", "Inferior vena cava", "Ductus arteriosus", "Umbilical arteries", "Internal iliac artery"],
   "The single umbilical vein brings oxygenated blood from the placenta; the two umbilical arteries carry deoxygenated blood to the placenta. Part of the blood bypasses the liver through the ductus venosus into the IVC."),
  ("Dans la circulation fœtale, quel vaisseau apporte le sang oxygéné du placenta au fœtus ?", ["Veine ombilicale", "Veine cave inférieure", "Canal artériel", "Artères ombilicales", "Artère iliaque interne"],
   "L'unique veine ombilicale apporte le sang oxygéné du placenta ; les deux artères ombilicales ramènent le sang désoxygéné au placenta. Une partie du sang court-circuite le foie par le canal veineux vers la VCI."),
  ("Welches Gefäß bringt im Fetalkreislauf sauerstoffreiches Blut von der Plazenta zum Fetus?", ["V. umbilicalis", "V. cava inferior", "Ductus arteriosus", "Aa. umbilicales", "A. iliaca interna"],
   "Die einzige Nabelvene bringt sauerstoffreiches Blut aus der Plazenta; die beiden Nabelarterien führen sauerstoffarmes Blut zur Plazenta. Ein Teil des Blutes umgeht über den Ductus venosus die Leber und gelangt in die V. cava inferior."),
  ("En la circulación fetal, ¿qué vaso lleva la sangre oxigenada de la placenta al feto?", ["Vena umbilical", "Vena cava inferior", "Conducto arterioso", "Arterias umbilicales", "Arteria ilíaca interna"],
   "La única vena umbilical trae sangre oxigenada de la placenta; las dos arterias umbilicales llevan sangre desoxigenada a la placenta. Parte de la sangre evita el hígado por el conducto venoso hacia la VCI."))

T("cv-35606634",
  ("Which nerve passes through the cavernous sinus itself (not in its wall)?", ["Trochlear nerve (IV)", "Ophthalmic nerve (V1)", "Oculomotor nerve (III)", "Abducens nerve (VI)", "Maxillary nerve (V2)"],
   "The internal carotid artery and the abducens nerve pass through the sinus; III, IV, V1 and V2 run in its lateral wall. That is why the abducens is usually the first nerve affected in cavernous sinus thrombosis and ICA aneurysm."),
  ("Quel nerf traverse le sinus caverneux lui-même (et non sa paroi) ?", ["Nerf trochléaire (IV)", "Nerf ophtalmique (V1)", "Nerf oculomoteur (III)", "Nerf abducens (VI)", "Nerf maxillaire (V2)"],
   "La carotide interne et le nerf abducens traversent le sinus ; III, IV, V1 et V2 cheminent dans sa paroi latérale. C'est pourquoi l'abducens est généralement le premier atteint dans la thrombose du sinus caverneux et l'anévrisme carotidien."),
  ("Welcher Nerv verläuft durch den Sinus cavernosus selbst (nicht in seiner Wand)?", ["N. trochlearis (IV)", "N. ophthalmicus (V1)", "N. oculomotorius (III)", "N. abducens (VI)", "N. maxillaris (V2)"],
   "A. carotis interna und N. abducens ziehen durch den Sinus; III, IV, V1 und V2 verlaufen in seiner Seitenwand. Deshalb ist bei Sinus-cavernosus-Thrombose und Karotisaneurysma meist zuerst der N. abducens betroffen."),
  ("¿Qué nervio atraviesa el propio seno cavernoso (no su pared)?", ["Nervio troclear (IV)", "Nervio oftálmico (V1)", "Nervio oculomotor (III)", "Nervio abducens (VI)", "Nervio maxilar (V2)"],
   "La carótida interna y el abducens pasan por el seno; III, IV, V1 y V2 discurren por su pared lateral. Por eso el abducens suele ser el primero afectado en la trombosis del seno cavernoso y en el aneurisma de la ACI."))

T("cv-91f6535e",
  ("A hypertensive patient has sudden, tearing chest pain radiating to the back and a marked blood pressure difference between the arms. What is the most likely diagnosis?", ["Acute myocardial infarction", "Aortic dissection", "Pulmonary embolism", "Pericarditis", "Pneumothorax"],
   "In aortic dissection the inner layer tears and blood enters between the wall layers; because branch origins can be involved, pulse and blood pressure differ between the arms. Involvement of the ascending aorta (Stanford A) is a surgical emergency."),
  ("Un patient hypertendu présente une douleur thoracique brutale, déchirante, irradiant dans le dos, avec une nette différence de pression artérielle entre les deux bras. Quel est le diagnostic le plus probable ?", ["Infarctus du myocarde aigu", "Dissection aortique", "Embolie pulmonaire", "Péricardite", "Pneumothorax"],
   "Dans la dissection aortique, l'intima se déchire et le sang s'insinue entre les couches de la paroi ; l'atteinte de l'origine des branches explique l'asymétrie des pouls et de la pression entre les bras. L'atteinte de l'aorte ascendante (Stanford A) est une urgence chirurgicale."),
  ("Ein Hypertoniker hat plötzliche, reißende, in den Rücken ausstrahlende Brustschmerzen und einen deutlichen Blutdruckunterschied zwischen beiden Armen. Wahrscheinlichste Diagnose?", ["Akuter Myokardinfarkt", "Aortendissektion", "Lungenembolie", "Perikarditis", "Pneumothorax"],
   "Bei der Aortendissektion reißt die Intima ein und Blut wühlt sich zwischen die Wandschichten; da Abgänge von Ästen betroffen sein können, entstehen Puls- und Blutdruckdifferenzen zwischen den Armen. Eine Beteiligung der Aorta ascendens (Stanford A) ist ein chirurgischer Notfall."),
  ("Un paciente hipertenso presenta dolor torácico súbito, desgarrador, irradiado a la espalda, con una clara diferencia de presión arterial entre ambos brazos. ¿Cuál es el diagnóstico más probable?", ["Infarto agudo de miocardio", "Disección aórtica", "Embolia pulmonar", "Pericarditis", "Neumotórax"],
   "En la disección aórtica se desgarra la íntima y la sangre penetra entre las capas de la pared; al afectarse el origen de las ramas aparecen diferencias de pulso y presión entre los brazos. La afectación de la aorta ascendente (Stanford A) es una urgencia quirúrgica."))

T("cv-5e60843b",
  ("An elderly patient with atrial fibrillation has sudden abdominal pain out of proportion to the examination findings. What is the most likely cause?", ["Superior mesenteric artery embolism", "Ruptured abdominal aortic aneurysm", "Renal artery embolism", "Inferior mesenteric artery thrombosis", "Coeliac trunk stenosis"],
   "Because the SMA leaves the aorta at a narrow angle, emboli from the heart often lodge there; early acute mesenteric ischaemia gives very few examination findings compared with the severity of the pain."),
  ("Un patient âgé en fibrillation atriale présente une douleur abdominale brutale, disproportionnée par rapport à l'examen. Quelle est la cause la plus probable ?", ["Embolie de l'artère mésentérique supérieure", "Rupture d'un anévrisme de l'aorte abdominale", "Embolie de l'artère rénale", "Thrombose de l'artère mésentérique inférieure", "Sténose du tronc cœliaque"],
   "L'AMS naissant de l'aorte selon un angle aigu, les emboles d'origine cardiaque s'y logent souvent ; au début, l'ischémie mésentérique aiguë donne très peu de signes d'examen au regard de l'intensité de la douleur."),
  ("Ein älterer Patient mit Vorhofflimmern hat plötzliche Bauchschmerzen, die in keinem Verhältnis zum Untersuchungsbefund stehen. Wahrscheinlichste Ursache?", ["Embolie der A. mesenterica superior", "Rupturiertes Bauchaortenaneurysma", "Nierenarterienembolie", "Thrombose der A. mesenterica inferior", "Stenose des Truncus coeliacus"],
   "Da die A. mesenterica superior in spitzem Winkel aus der Aorta abgeht, gelangen kardiale Emboli häufig dorthin; die akute Mesenterialischämie zeigt anfangs im Verhältnis zur Schmerzstärke kaum Untersuchungsbefunde."),
  ("Un paciente anciano con fibrilación auricular presenta dolor abdominal súbito, desproporcionado respecto a la exploración. ¿Cuál es la causa más probable?", ["Embolia de la arteria mesentérica superior", "Rotura de un aneurisma de aorta abdominal", "Embolia de la arteria renal", "Trombosis de la mesentérica inferior", "Estenosis del tronco celíaco"],
   "Como la AMS sale de la aorta en ángulo agudo, los émbolos cardíacos suelen alojarse en ella; al principio la isquemia mesentérica aguda da muy pocos hallazgos exploratorios en comparación con la intensidad del dolor."))

T("cv-21fae810",
  ("A patient who develops leg swelling and pain after a long flight is found to have deep vein thrombosis. What is the most serious complication?", ["Cellulitis", "Compartment syndrome", "Pulmonary embolism", "Lymphoedema", "Varicose veins"],
   "A clot in the deep leg veins can break off and travel via the IVC and right heart into the pulmonary artery; massive pulmonary embolism can cause sudden death."),
  ("Un patient qui présente un gonflement et une douleur de jambe après un long vol a une thrombose veineuse profonde. Quelle est la complication la plus grave ?", ["Cellulite", "Syndrome des loges", "Embolie pulmonaire", "Lymphœdème", "Varices"],
   "Un caillot des veines profondes de la jambe peut se détacher et gagner, par la VCI et le cœur droit, l'artère pulmonaire ; une embolie pulmonaire massive peut entraîner la mort subite."),
  ("Bei einem Patienten mit Beinschwellung und -schmerzen nach einem Langstreckenflug wird eine tiefe Venenthrombose festgestellt. Was ist die gefährlichste Komplikation?", ["Phlegmone", "Kompartmentsyndrom", "Lungenembolie", "Lymphödem", "Krampfadern"],
   "Ein Thrombus aus den tiefen Beinvenen kann sich lösen und über V. cava inferior und rechtes Herz in die Lungenarterie gelangen; eine massive Lungenembolie kann zum plötzlichen Tod führen."),
  ("A un paciente con hinchazón y dolor en la pierna tras un vuelo largo se le diagnostica trombosis venosa profunda. ¿Cuál es la complicación más grave?", ["Celulitis", "Síndrome compartimental", "Embolia pulmonar", "Linfedema", "Varices"],
   "Un coágulo de las venas profundas de la pierna puede desprenderse y llegar por la VCI y el corazón derecho a la arteria pulmonar; una embolia pulmonar masiva puede causar muerte súbita."))

T("cv-ac08c79d",
  ("Which of the following is NOT a component of tetralogy of Fallot?", ["Pulmonary stenosis (right ventricular outflow obstruction)", "Atrial septal defect", "Right ventricular hypertrophy", "Overriding aorta", "Ventricular septal defect"],
   "Tetralogy of Fallot consists of VSD, pulmonary stenosis, overriding aorta and right ventricular hypertrophy; it results from anterior displacement of the conal septum and is the most common cyanotic congenital heart disease."),
  ("Lequel des éléments suivants ne fait PAS partie de la tétralogie de Fallot ?", ["Sténose pulmonaire (obstacle à l'éjection du ventricule droit)", "Communication interatriale", "Hypertrophie ventriculaire droite", "Aorte à cheval sur le septum", "Communication interventriculaire"],
   "La tétralogie de Fallot associe CIV, sténose pulmonaire, aorte à cheval et hypertrophie ventriculaire droite ; elle résulte d'un déplacement antérieur du septum conal et c'est la cardiopathie congénitale cyanogène la plus fréquente."),
  ("Welcher der folgenden ist KEIN Bestandteil der Fallot-Tetralogie?", ["Pulmonalstenose (rechtsventrikuläre Ausflusstraktobstruktion)", "Vorhofseptumdefekt", "Rechtsventrikuläre Hypertrophie", "Überreitende Aorta", "Ventrikelseptumdefekt"],
   "Die Fallot-Tetralogie besteht aus VSD, Pulmonalstenose, überreitender Aorta und Rechtsherzhypertrophie; sie entsteht durch Vorverlagerung des Konusseptums und ist der häufigste zyanotische angeborene Herzfehler."),
  ("¿Cuál de los siguientes NO es un componente de la tetralogía de Fallot?", ["Estenosis pulmonar (obstrucción del tracto de salida del VD)", "Comunicación interauricular", "Hipertrofia ventricular derecha", "Aorta cabalgante", "Comunicación interventricular"],
   "La tetralogía de Fallot consta de CIV, estenosis pulmonar, aorta cabalgante e hipertrofia ventricular derecha; se debe al desplazamiento anterior del septo conal y es la cardiopatía congénita cianótica más frecuente."))

T("cv-5dd9592d",
  ("What is the valve guarding the opening of the coronary sinus called?", ["Tendon of Todaro", "Crista terminalis", "Eustachian valve", "Chiari network", "Thebesian valve (valve of the coronary sinus)"],
   "The Thebesian valve lies where the coronary sinus opens into the right atrium, the Eustachian valve at the IVC opening. The tendon of Todaro is the continuation of the Eustachian valve and a border of Koch's triangle."),
  ("Comment appelle-t-on la valvule qui garde l'orifice du sinus coronaire ?", ["Tendon de Todaro", "Crête terminale", "Valvule d'Eustachi", "Réseau de Chiari", "Valvule de Thebesius (valvule du sinus coronaire)"],
   "La valvule de Thebesius se trouve à l'abouchement du sinus coronaire dans l'atrium droit, la valvule d'Eustachi à l'orifice de la VCI. Le tendon de Todaro prolonge la valvule d'Eustachi et limite le triangle de Koch."),
  ("Wie heißt die Klappe an der Mündung des Sinus coronarius?", ["Todaro-Sehne", "Crista terminalis", "Eustachi-Klappe", "Chiari-Netzwerk", "Thebesius-Klappe (Valvula sinus coronarii)"],
   "Die Thebesius-Klappe liegt an der Mündung des Sinus coronarius in den rechten Vorhof, die Eustachi-Klappe an der Mündung der V. cava inferior. Die Todaro-Sehne setzt die Eustachi-Klappe fort und begrenzt das Koch-Dreieck."),
  ("¿Cómo se llama la válvula que protege el orificio del seno coronario?", ["Tendón de Todaro", "Cresta terminal", "Válvula de Eustaquio", "Red de Chiari", "Válvula de Tebesio (válvula del seno coronario)"],
   "La válvula de Tebesio está en la desembocadura del seno coronario en la aurícula derecha y la de Eustaquio en el orificio de la VCI. El tendón de Todaro continúa la válvula de Eustaquio y limita el triángulo de Koch."))

T("cv-9c344753",
  ("Which vascular anomaly causes dysphagia lusoria (difficulty swallowing)?", ["Coarctation of the aorta", "Left superior vena cava", "A right subclavian artery arising as the last branch of the aortic arch and passing behind the oesophagus", "Double aortic arch", "Patent ductus arteriosus"],
   "The aberrant right subclavian artery (arteria lusoria) is the last branch of the aortic arch and crosses to the right behind the oesophagus, which it can compress; it is the most common aortic arch anomaly. The right recurrent laryngeal nerve is then non-recurrent."),
  ("Quelle anomalie vasculaire provoque la dysphagie lusoria (trouble de la déglutition) ?", ["Coarctation de l'aorte", "Veine cave supérieure gauche", "Artère subclavière droite naissant en dernière branche de la crosse et passant derrière l'œsophage", "Double crosse aortique", "Persistance du canal artériel"],
   "L'artère subclavière droite aberrante (arteria lusoria) est la dernière branche de la crosse et passe à droite derrière l'œsophage, qu'elle peut comprimer ; c'est l'anomalie de la crosse la plus fréquente. Le nerf laryngé inférieur droit est alors non récurrent."),
  ("Welche Gefäßanomalie verursacht die Dysphagia lusoria (Schluckstörung)?", ["Aortenisthmusstenose", "Linke V. cava superior", "Rechte A. subclavia als letzter Ast des Aortenbogens, die hinter dem Ösophagus verläuft", "Doppelter Aortenbogen", "Offener Ductus arteriosus"],
   "Die aberrante rechte A. subclavia (A. lusoria) ist der letzte Ast des Aortenbogens und zieht hinter dem Ösophagus nach rechts, den sie komprimieren kann; sie ist die häufigste Aortenbogenanomalie. Der rechte N. laryngeus recurrens verläuft dann nicht rekurrent."),
  ("¿Qué anomalía vascular produce la disfagia lusoria (dificultad para tragar)?", ["Coartación de aorta", "Vena cava superior izquierda", "Arteria subclavia derecha que nace como última rama del cayado y pasa por detrás del esófago", "Doble cayado aórtico", "Conducto arterioso persistente"],
   "La subclavia derecha aberrante (arteria lusoria) es la última rama del cayado y cruza a la derecha por detrás del esófago, al que puede comprimir; es la anomalía del cayado más frecuente. El laríngeo recurrente derecho es entonces no recurrente."))

T("cv-4fc98b11",
  ("Which arteries are the most common source of hypertensive intracerebral haemorrhage?", ["Middle meningeal artery", "Basilar artery", "Cortical branches of the anterior cerebral artery", "Lenticulostriate arteries (perforating branches of the middle cerebral artery)", "Anterior communicating artery"],
   "The lenticulostriate arteries are thin end arteries arising at a right angle from the MCA; in chronic hypertension Charcot–Bouchard microaneurysms develop and cause basal ganglia (putaminal) haemorrhages."),
  ("Quelles artères sont la source la plus fréquente des hémorragies intracérébrales hypertensives ?", ["Artère méningée moyenne", "Artère basilaire", "Branches corticales de l'artère cérébrale antérieure", "Artères lenticulo-striées (perforantes de l'artère cérébrale moyenne)", "Artère communicante antérieure"],
   "Les artères lenticulo-striées sont de fines artères terminales naissant à angle droit de l'ACM ; dans l'hypertension chronique se forment des micro-anévrismes de Charcot-Bouchard, à l'origine d'hémorragies des noyaux gris centraux (putamen)."),
  ("Welche Arterien sind die häufigste Quelle hypertensiver intrazerebraler Blutungen?", ["A. meningea media", "A. basilaris", "Kortikale Äste der A. cerebri anterior", "Aa. lenticulostriatae (perforierende Äste der A. cerebri media)", "A. communicans anterior"],
   "Die Aa. lenticulostriatae sind dünne Endarterien, die rechtwinklig aus der A. cerebri media abgehen; bei chronischer Hypertonie entstehen Charcot-Bouchard-Mikroaneurysmen, die zu Stammganglienblutungen (Putamen) führen."),
  ("¿Qué arterias son la fuente más frecuente de la hemorragia intracerebral hipertensiva?", ["Arteria meníngea media", "Arteria basilar", "Ramas corticales de la cerebral anterior", "Arterias lenticuloestriadas (perforantes de la cerebral media)", "Arteria comunicante anterior"],
   "Las lenticuloestriadas son finas arterias terminales que salen en ángulo recto de la ACM; en la hipertensión crónica se forman microaneurismas de Charcot-Bouchard que producen hemorragias de los ganglios basales (putamen)."))

T("cv-79341972",
  ("Which artery does NOT contribute to Kiesselbach's area, the source of most nosebleeds?", ["Sphenopalatine artery", "Ascending pharyngeal artery", "Anterior ethmoidal artery", "Greater palatine artery", "Superior labial artery"],
   "Kiesselbach's (Little's) area on the anteroinferior septum is formed by anastomosing branches of the sphenopalatine, anterior ethmoidal, greater palatine and superior labial (facial) arteries."),
  ("Quelle artère ne participe PAS à la tache vasculaire de Kiesselbach, source de la plupart des épistaxis ?", ["Artère sphéno-palatine", "Artère pharyngienne ascendante", "Artère ethmoïdale antérieure", "Artère grande palatine", "Artère labiale supérieure"],
   "La tache vasculaire de Kiesselbach, à la partie antéro-inférieure du septum, est formée par l'anastomose de branches des artères sphéno-palatine, ethmoïdale antérieure, grande palatine et labiale supérieure (faciale)."),
  ("Welche Arterie ist NICHT am Locus Kiesselbachi beteiligt, der Quelle der meisten Nasenblutungen?", ["A. sphenopalatina", "A. pharyngea ascendens", "A. ethmoidalis anterior", "A. palatina major", "A. labialis superior"],
   "Der Locus Kiesselbachi am vorderen unteren Septum entsteht durch Anastomosen von Ästen der A. sphenopalatina, A. ethmoidalis anterior, A. palatina major und A. labialis superior (aus der A. facialis)."),
  ("¿Qué arteria NO participa en el área de Kiesselbach, origen de la mayoría de las epistaxis?", ["Arteria esfenopalatina", "Arteria faríngea ascendente", "Arteria etmoidal anterior", "Arteria palatina mayor", "Arteria labial superior"],
   "El área de Kiesselbach (de Little), en la parte anteroinferior del tabique, la forman anastomosis de ramas de las arterias esfenopalatina, etmoidal anterior, palatina mayor y labial superior (facial)."))

T("cv-c5892b74",
  ("What is the 'corona mortis', dangerous in hernia surgery?", ["The posterior trunk of the internal iliac artery", "An anastomosis between the inferior epigastric (external iliac system) and obturator arteries crossing over the pubis", "A connection between the right and left common iliac arteries", "The deep branch of the femoral artery", "An anastomosis between the superior and middle rectal arteries"],
   "In some people the obturator artery (or vein) arises from, or widely anastomoses with, the external iliac/inferior epigastric system and crosses the superior pubic ramus. If injured in femoral hernia or pelvic surgery, severe bleeding occurs."),
  ("Qu'est-ce que la « corona mortis », dangereuse en chirurgie herniaire ?", ["Le tronc postérieur de l'artère iliaque interne", "Une anastomose entre l'artère épigastrique inférieure (système iliaque externe) et l'artère obturatrice passant sur le pubis", "Une communication entre les deux artères iliaques communes", "La branche profonde de l'artère fémorale", "Une anastomose entre les artères rectales supérieure et moyenne"],
   "Chez certains sujets, l'artère (ou la veine) obturatrice naît du système iliaque externe/épigastrique inférieur ou s'y anastomose largement et croise la branche supérieure du pubis. Sa blessure lors d'une cure de hernie fémorale ou d'une chirurgie pelvienne provoque une hémorragie grave."),
  ("Was ist die bei Hernienoperationen gefährliche „Corona mortis“?", ["Der hintere Stamm der A. iliaca interna", "Eine über das Schambein ziehende Anastomose zwischen A. epigastrica inferior (Externa-System) und A. obturatoria", "Eine Verbindung zwischen rechter und linker A. iliaca communis", "Der tiefe Ast der A. femoralis", "Eine Anastomose zwischen A. rectalis superior und media"],
   "Bei manchen Menschen entspringt die A. (oder V.) obturatoria aus dem System der A. iliaca externa/epigastrica inferior oder anastomosiert breit damit und überquert den oberen Schambeinast. Wird sie bei Schenkelhernien- oder Beckenoperationen verletzt, kommt es zu schweren Blutungen."),
  ("¿Qué es la «corona mortis», peligrosa en la cirugía de las hernias?", ["El tronco posterior de la ilíaca interna", "Una anastomosis entre la epigástrica inferior (sistema ilíaco externo) y la obturatriz que cruza sobre el pubis", "Una comunicación entre las ilíacas comunes derecha e izquierda", "La rama profunda de la femoral", "Una anastomosis entre las rectales superior y media"],
   "En algunas personas la arteria (o vena) obturatriz nace del sistema ilíaco externo/epigástrico inferior o se anastomosa ampliamente con él y cruza la rama superior del pubis. Si se lesiona en la cirugía de la hernia femoral o pélvica se produce una hemorragia grave."))

T("cv-edca0ec0",
  ("What is the adult remnant of the ductus venosus?", ["Fossa ovalis", "Ligamentum arteriosum", "Ligamentum venosum", "Ligamentum teres hepatis", "Medial umbilical ligament"],
   "In the fetus the ductus venosus carries blood from the umbilical vein past the liver into the IVC; after birth it closes to become the ligamentum venosum. The umbilical vein becomes the ligamentum teres hepatis."),
  ("Quel est le vestige adulte du canal veineux (d'Arantius) ?", ["Fosse ovale", "Ligament artériel", "Ligament veineux", "Ligament rond du foie", "Ligament ombilical médial"],
   "Chez le fœtus, le canal veineux conduit le sang de la veine ombilicale vers la VCI en court-circuitant le foie ; après la naissance, il se ferme et devient le ligament veineux. La veine ombilicale devient le ligament rond du foie."),
  ("Was ist der Rest des Ductus venosus beim Erwachsenen?", ["Fossa ovalis", "Lig. arteriosum", "Lig. venosum", "Lig. teres hepatis", "Lig. umbilicale mediale"],
   "Beim Fetus leitet der Ductus venosus Blut aus der Nabelvene an der Leber vorbei in die V. cava inferior; nach der Geburt verschließt er sich zum Lig. venosum. Die Nabelvene wird zum Lig. teres hepatis."),
  ("¿Cuál es el resto adulto del conducto venoso?", ["Fosa oval", "Ligamento arterioso", "Ligamento venoso", "Ligamento redondo del hígado", "Ligamento umbilical medial"],
   "En el feto el conducto venoso lleva la sangre de la vena umbilical a la VCI evitando el hígado; tras el nacimiento se cierra y se convierte en el ligamento venoso. La vena umbilical se convierte en el ligamento redondo del hígado."))

T("cv-47659c1d",
  ("What is the adult remnant of the umbilical vein?", ["Ligamentum venosum", "Ligamentum teres hepatis (in the free edge of the falciform ligament)", "Ligamentum arteriosum", "Medial umbilical ligament", "Median umbilical ligament"],
   "After birth the umbilical vein becomes the ligamentum teres hepatis. In portal hypertension the paraumbilical veins around this ligament open up and contribute to caput medusae."),
  ("Quel est le vestige adulte de la veine ombilicale ?", ["Ligament veineux", "Ligament rond du foie (dans le bord libre du ligament falciforme)", "Ligament artériel", "Ligament ombilical médial", "Ligament ombilical médian"],
   "Après la naissance, la veine ombilicale devient le ligament rond du foie. Dans l'hypertension portale, les veines para-ombilicales qui l'accompagnent se dilatent et participent à la tête de méduse."),
  ("Was ist der Rest der Nabelvene beim Erwachsenen?", ["Lig. venosum", "Lig. teres hepatis (im freien Rand des Lig. falciforme)", "Lig. arteriosum", "Lig. umbilicale mediale", "Lig. umbilicale medianum"],
   "Nach der Geburt wird die Nabelvene zum Lig. teres hepatis. Bei portaler Hypertension öffnen sich die Vv. paraumbilicales um dieses Band und tragen zum Caput medusae bei."),
  ("¿Cuál es el resto adulto de la vena umbilical?", ["Ligamento venoso", "Ligamento redondo del hígado (en el borde libre del ligamento falciforme)", "Ligamento arterioso", "Ligamento umbilical medial", "Ligamento umbilical medio"],
   "Tras el nacimiento la vena umbilical se convierte en el ligamento redondo del hígado. En la hipertensión portal las venas paraumbilicales que lo acompañan se abren y contribuyen a la cabeza de medusa."))

T("cv-96f935f6",
  ("What is the adult remnant of the distal part of the umbilical artery?", ["Medial umbilical ligament", "Ligamentum teres hepatis", "Ligamentum arteriosum", "Ligamentum venosum", "Median umbilical ligament"],
   "The proximal part of the umbilical arteries stays patent as the superior vesical artery, the distal part becomes the medial umbilical ligament. The median umbilical ligament is the remnant of the urachus."),
  ("Quel est le vestige adulte de la partie distale de l'artère ombilicale ?", ["Ligament ombilical médial", "Ligament rond du foie", "Ligament artériel", "Ligament veineux", "Ligament ombilical médian"],
   "La partie proximale des artères ombilicales reste perméable sous forme d'artère vésicale supérieure, la partie distale devient le ligament ombilical médial. Le ligament ombilical médian est le vestige de l'ouraque."),
  ("Was ist der Rest des distalen Abschnitts der Nabelarterie beim Erwachsenen?", ["Lig. umbilicale mediale", "Lig. teres hepatis", "Lig. arteriosum", "Lig. venosum", "Lig. umbilicale medianum"],
   "Der proximale Teil der Nabelarterien bleibt als A. vesicalis superior offen, der distale wird zum Lig. umbilicale mediale. Das Lig. umbilicale medianum ist der Rest des Urachus."),
  ("¿Cuál es el resto adulto de la porción distal de la arteria umbilical?", ["Ligamento umbilical medial", "Ligamento redondo del hígado", "Ligamento arterioso", "Ligamento venoso", "Ligamento umbilical medio"],
   "La porción proximal de las arterias umbilicales sigue permeable como arteria vesical superior y la distal se convierte en el ligamento umbilical medial. El ligamento umbilical medio es el resto del uraco."))

T("cv-d6da7df0",
  ("What vessels are usually the source of a subdural haematoma?", ["Lenticulostriate arteries", "Anterior communicating artery", "Cavernous sinus", "Middle meningeal artery", "Bridging veins running from the cortex to the dural sinuses"],
   "A subdural haematoma forms between dura and arachnoid when bridging veins, stretched by brain atrophy in the elderly and alcoholics, tear; it develops slowly and is crescent-shaped. An epidural haematoma usually arises from the middle meningeal artery."),
  ("Quels vaisseaux sont habituellement à l'origine d'un hématome sous-dural ?", ["Artères lenticulo-striées", "Artère communicante antérieure", "Sinus caverneux", "Artère méningée moyenne", "Veines ponts allant du cortex aux sinus de la dure-mère"],
   "L'hématome sous-dural se forme entre dure-mère et arachnoïde par rupture des veines ponts, étirées par l'atrophie cérébrale chez le sujet âgé et l'alcoolique ; il se constitue lentement et a une forme en croissant. L'hématome extradural vient le plus souvent de l'artère méningée moyenne."),
  ("Aus welchen Gefäßen stammt ein subdurales Hämatom meist?", ["Aa. lenticulostriatae", "A. communicans anterior", "Sinus cavernosus", "A. meningea media", "Brückenvenen von der Hirnrinde zu den Duralsinus"],
   "Das subdurale Hämatom entsteht zwischen Dura und Arachnoidea durch Einriss von Brückenvenen, die bei Älteren und Alkoholkranken durch Hirnatrophie gedehnt sind; es entwickelt sich langsam und ist sichelförmig. Das epidurale Hämatom stammt meist aus der A. meningea media."),
  ("¿Qué vasos suelen originar el hematoma subdural?", ["Arterias lenticuloestriadas", "Arteria comunicante anterior", "Seno cavernoso", "Arteria meníngea media", "Venas puente que van de la corteza a los senos durales"],
   "El hematoma subdural se forma entre duramadre y aracnoides al romperse las venas puente, estiradas por la atrofia cerebral en ancianos y alcohólicos; evoluciona lentamente y tiene forma de semiluna. El epidural suele proceder de la arteria meníngea media."))

T("cv-2151bfd7",
  ("Which valveless venous network plays a role in the spread of prostate cancer to the spine?", ["Vertebral venous plexus (Batson's plexus)", "Pampiniform plexus", "Rectal venous plexus", "Portal system", "Pterygoid plexus"],
   "Batson's plexus is a valveless venous network around the spine connected with the pelvic veins; when intra-abdominal pressure rises blood can flow towards the spine, explaining spinal spread of tumours such as prostate and breast cancer."),
  ("Quel réseau veineux dépourvu de valvules intervient dans la dissémination du cancer de la prostate au rachis ?", ["Plexus veineux vertébral (de Batson)", "Plexus pampiniforme", "Plexus veineux rectal", "Système porte", "Plexus ptérygoïdien"],
   "Le plexus de Batson est un réseau veineux sans valvules autour du rachis, relié aux veines pelviennes ; lors d'une hausse de pression abdominale, le sang peut refluer vers le rachis, ce qui explique les métastases vertébrales des cancers de la prostate ou du sein."),
  ("Welches klappenlose Venengeflecht spielt bei der Metastasierung des Prostatakarzinoms in die Wirbelsäule eine Rolle?", ["Plexus venosus vertebralis (Batson-Plexus)", "Plexus pampiniformis", "Plexus venosus rectalis", "Pfortadersystem", "Plexus pterygoideus"],
   "Der Batson-Plexus ist ein klappenloses Venengeflecht um die Wirbelsäule mit Verbindung zu den Beckenvenen; bei erhöhtem Bauchdruck kann Blut zur Wirbelsäule fließen, was die Wirbelsäulenmetastasen etwa von Prostata- und Mammakarzinom erklärt."),
  ("¿Qué red venosa sin válvulas interviene en la diseminación del cáncer de próstata a la columna?", ["Plexo venoso vertebral (de Batson)", "Plexo pampiniforme", "Plexo venoso rectal", "Sistema porta", "Plexo pterigoideo"],
   "El plexo de Batson es una red venosa sin válvulas alrededor de la columna conectada con las venas pélvicas; al aumentar la presión abdominal la sangre puede fluir hacia la columna, lo que explica las metástasis vertebrales de tumores como el de próstata o mama."))

T("cv-88c74a4e",
  ("In May–Thurner syndrome, which compression predisposes to deep vein thrombosis of the left leg?", ["Compression of the left femoral vein under the inguinal ligament", "Compression of the inferior vena cava by the liver", "Compression of the left common iliac vein against the spine by the right common iliac artery", "Compression of the right external iliac vein by the sigmoid colon", "Compression of the left renal vein between the aorta and SMA"],
   "The right common iliac artery crosses in front of the left common iliac vein and presses it against L5; over time a fibrous band forms in the vein wall and left leg DVT develops."),
  ("Dans le syndrome de May-Thurner, quelle compression prédispose à la thrombose veineuse profonde de la jambe gauche ?", ["Compression de la veine fémorale gauche sous le ligament inguinal", "Compression de la veine cave inférieure par le foie", "Compression de la veine iliaque commune gauche contre le rachis par l'artère iliaque commune droite", "Compression de la veine iliaque externe droite par le côlon sigmoïde", "Compression de la veine rénale gauche entre l'aorte et l'AMS"],
   "L'artère iliaque commune droite croise en avant la veine iliaque commune gauche et l'écrase contre L5 ; avec le temps, un éperon fibreux se forme dans la paroi veineuse et une TVP de la jambe gauche survient."),
  ("Welche Kompression begünstigt beim May-Thurner-Syndrom eine tiefe Venenthrombose des linken Beins?", ["Kompression der linken V. femoralis unter dem Leistenband", "Kompression der V. cava inferior durch die Leber", "Kompression der linken V. iliaca communis gegen die Wirbelsäule durch die rechte A. iliaca communis", "Kompression der rechten V. iliaca externa durch das Sigma", "Kompression der linken Nierenvene zwischen Aorta und A. mesenterica superior"],
   "Die rechte A. iliaca communis kreuzt vor der linken V. iliaca communis und drückt sie gegen L5; mit der Zeit bildet sich ein fibröser Venensporn und es kommt zur Thrombose des linken Beins."),
  ("En el síndrome de May-Thurner, ¿qué compresión predispone a la trombosis venosa profunda de la pierna izquierda?", ["Compresión de la vena femoral izquierda bajo el ligamento inguinal", "Compresión de la vena cava inferior por el hígado", "Compresión de la vena ilíaca común izquierda contra la columna por la arteria ilíaca común derecha", "Compresión de la vena ilíaca externa derecha por el colon sigmoide", "Compresión de la vena renal izquierda entre la aorta y la AMS"],
   "La ilíaca común derecha cruza por delante de la vena ilíaca común izquierda y la comprime contra L5; con el tiempo se forma una banda fibrosa en la pared venosa y aparece TVP de la pierna izquierda."))

T("cv-ccd14bde",
  ("A patient who squeezed a boil beside the nose develops fever, eyelid swelling, exophthalmos and double vision on lateral gaze. Which nerve is affected first, and why?", ["Facial nerve – because it runs with the facial vein", "Optic nerve – because it lies in the wall of the sinus", "Oculomotor nerve – because it passes through the sinus", "Trochlear nerve – because it lies in the floor of the sinus", "Abducens nerve – because it runs freely through the cavernous sinus"],
   "Infection in the danger triangle of the face spreads via the angular vein and superior ophthalmic vein to the cavernous sinus. The abducens nerve, running freely inside the sinus beside the ICA, is usually the first affected; lateral gaze is restricted."),
  ("Un patient qui a pressé un furoncle de l'aile du nez présente fièvre, œdème palpébral, exophtalmie et diplopie dans le regard latéral. Quel nerf est atteint en premier et pourquoi ?", ["Nerf facial – car il chemine avec la veine faciale", "Nerf optique – car il est dans la paroi du sinus", "Nerf oculomoteur – car il traverse le sinus", "Nerf trochléaire – car il est dans le plancher du sinus", "Nerf abducens – car il traverse librement le sinus caverneux"],
   "L'infection du triangle dangereux de la face gagne le sinus caverneux par la veine angulaire et la veine ophtalmique supérieure. Le nerf abducens, libre dans le sinus à côté de la carotide interne, est généralement le premier touché ; le regard latéral est limité."),
  ("Ein Patient, der einen Furunkel neben der Nase ausgedrückt hat, entwickelt Fieber, Lidschwellung, Exophthalmus und Doppelbilder beim Seitblick. Welcher Nerv ist zuerst betroffen und warum?", ["N. facialis – weil er mit der V. facialis verläuft", "N. opticus – weil er in der Sinuswand liegt", "N. oculomotorius – weil er durch den Sinus zieht", "N. trochlearis – weil er am Sinusboden liegt", "N. abducens – weil er frei durch den Sinus cavernosus zieht"],
   "Eine Infektion im gefährlichen Gesichtsdreieck breitet sich über V. angularis und V. ophthalmica superior in den Sinus cavernosus aus. Der frei im Sinus neben der A. carotis interna verlaufende N. abducens ist meist zuerst betroffen; der Seitblick ist eingeschränkt."),
  ("Un paciente que se apretó un forúnculo junto a la nariz presenta fiebre, edema palpebral, exoftalmos y diplopía en la mirada lateral. ¿Qué nervio se afecta primero y por qué?", ["Nervio facial – porque acompaña a la vena facial", "Nervio óptico – porque está en la pared del seno", "Nervio oculomotor – porque atraviesa el seno", "Nervio troclear – porque está en el suelo del seno", "Nervio abducens – porque atraviesa libremente el seno cavernoso"],
   "La infección del triángulo peligroso de la cara se extiende por la vena angular y la oftálmica superior al seno cavernoso. El abducens, libre dentro del seno junto a la ACI, suele ser el primero afectado; se limita la mirada lateral."))
