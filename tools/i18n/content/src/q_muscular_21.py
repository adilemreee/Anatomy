KIND = "questions"
SYSTEM = "muscular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("mu-e4aeb253",
  ("Which is the main muscle that extends the elbow?", ["Brachialis", "Pronator teres", "Biceps brachii", "Triceps brachii", "Brachioradialis"],
   "Triceps brachii is the three-headed muscle on the back of the arm; it inserts on the olecranon and extends the elbow, assisted by anconeus."),
  ("Quel est le principal muscle extenseur du coude ?", ["Muscle brachial", "Muscle rond pronateur", "Muscle biceps brachial", "Muscle triceps brachial", "Muscle brachio-radial"],
   "Le triceps brachial est le muscle à trois chefs de la face postérieure du bras ; il se termine sur l'olécrâne et étend le coude, aidé par l'anconé."),
  ("Welcher ist der wichtigste Strecker des Ellenbogens?", ["M. brachialis", "M. pronator teres", "M. biceps brachii", "M. triceps brachii", "M. brachioradialis"],
   "Der M. triceps brachii ist der dreiköpfige Muskel an der Rückseite des Oberarms; er setzt am Olekranon an und streckt den Ellenbogen, unterstützt vom M. anconeus."),
  ("¿Cuál es el principal músculo extensor del codo?", ["Músculo braquial", "Músculo pronador redondo", "Músculo bíceps braquial", "Músculo tríceps braquial", "Músculo braquiorradial"],
   "El tríceps braquial es el músculo de tres cabezas de la cara posterior del brazo; se inserta en el olécranon y extiende el codo, ayudado por el ancóneo."))

T("mu-b6e8a730",
  ("In general, what movement do the muscles of the anterior (flexor) compartment of the forearm produce?", ["They only open the fingers", "They extend the elbow", "They flex the wrist and fingers", "They only supinate the forearm", "They extend the wrist and fingers"],
   "The anterior forearm compartment contains the wrist and finger flexors and the pronators; most arise from the medial epicondyle and are supplied by the median nerve. The posterior compartment contains the extensors."),
  ("De façon générale, quel mouvement produisent les muscles de la loge antérieure (fléchisseurs) de l'avant-bras ?", ["Ils ouvrent seulement les doigts", "Ils étendent le coude", "Ils fléchissent le poignet et les doigts", "Ils assurent seulement la supination", "Ils étendent le poignet et les doigts"],
   "La loge antérieure de l'avant-bras contient les fléchisseurs du poignet et des doigts et les pronateurs ; la plupart naissent de l'épicondyle médial et sont innervés par le nerf médian. La loge postérieure contient les extenseurs."),
  ("Welche Bewegung führen die Muskeln der vorderen (Beuger-)Loge des Unterarms im Allgemeinen aus?", ["Sie strecken nur die Finger", "Sie strecken den Ellenbogen", "Sie beugen Handgelenk und Finger", "Sie supinieren nur den Unterarm", "Sie strecken Handgelenk und Finger"],
   "Die vordere Unterarmloge enthält Hand- und Fingerbeuger sowie die Pronatoren; die meisten entspringen am Epicondylus medialis und werden vom N. medianus innerviert. Die hintere Loge enthält die Strecker."),
  ("En general, ¿qué movimiento realizan los músculos del compartimento anterior (flexor) del antebrazo?", ["Solo abren los dedos", "Extienden el codo", "Flexionan la muñeca y los dedos", "Solo supinan el antebrazo", "Extienden la muñeca y los dedos"],
   "El compartimento anterior del antebrazo contiene los flexores de la muñeca y los dedos y los pronadores; la mayoría nace del epicóndilo medial y los inerva el mediano. El compartimento posterior contiene los extensores."))

T("mu-6af834e1",
  ("What is the muscular bulge at the base of the thumb called?", ["Hollow of the palm", "Interosseous space", "Anatomical snuffbox", "Thenar eminence", "Hypothenar eminence"],
   "The thenar eminence is formed by abductor pollicis brevis, flexor pollicis brevis and opponens pollicis; the bulge at the base of the little finger is the hypothenar eminence."),
  ("Comment appelle-t-on le relief musculaire à la base du pouce ?", ["Creux de la paume", "Espace interosseux", "Tabatière anatomique", "Éminence thénar", "Éminence hypothénar"],
   "L'éminence thénar est formée par le court abducteur, le court fléchisseur et l'opposant du pouce ; le relief à la base de l'auriculaire est l'éminence hypothénar."),
  ("Wie heißt der Muskelwulst an der Daumenbasis?", ["Hohlhand", "Interossealraum", "Tabatière", "Daumenballen (Thenar)", "Kleinfingerballen (Hypothenar)"],
   "Der Daumenballen wird von M. abductor pollicis brevis, M. flexor pollicis brevis und M. opponens pollicis gebildet; der Wulst an der Kleinfingerbasis ist der Kleinfingerballen."),
  ("¿Cómo se llama el relieve muscular de la base del pulgar?", ["Hueco de la palma", "Espacio interóseo", "Tabaquera anatómica", "Eminencia tenar", "Eminencia hipotenar"],
   "La eminencia tenar la forman el abductor corto, el flexor corto y el oponente del pulgar; el relieve de la base del meñique es la eminencia hipotenar."))

T("mu-ecb2c9e2",
  ("Which nerve supplies most of the small (intrinsic) muscles of the hand?", ["Axillary nerve", "Musculocutaneous nerve", "Ulnar nerve", "Radial nerve", "Median nerve"],
   "The ulnar nerve supplies the hypothenar muscles, interossei, 3rd–4th lumbricals, adductor pollicis and the deep head of FPB. The median nerve supplies the thenar muscles and the 1st–2nd lumbricals."),
  ("Quel nerf innerve la plupart des petits muscles (intrinsèques) de la main ?", ["Nerf axillaire", "Nerf musculo-cutané", "Nerf ulnaire", "Nerf radial", "Nerf médian"],
   "Le nerf ulnaire innerve les muscles hypothénariens, les interosseux, les 3e–4e lombricaux, l'adducteur du pouce et le chef profond du court fléchisseur. Le médian innerve les thénariens et les 1er–2e lombricaux."),
  ("Welcher Nerv innerviert die meisten kleinen (intrinsischen) Handmuskeln?", ["N. axillaris", "N. musculocutaneus", "N. ulnaris", "N. radialis", "N. medianus"],
   "Der N. ulnaris versorgt die Hypothenarmuskeln, die Mm. interossei, die Mm. lumbricales 3–4, den M. adductor pollicis und den tiefen Kopf des M. flexor pollicis brevis. Der N. medianus versorgt die Thenarmuskeln und die Mm. lumbricales 1–2."),
  ("¿Qué nervio inerva la mayoría de los músculos pequeños (intrínsecos) de la mano?", ["Nervio axilar", "Nervio musculocutáneo", "Nervio cubital", "Nervio radial", "Nervio mediano"],
   "El cubital inerva los hipotenares, los interóseos, los lumbricales 3.º–4.º, el aductor del pulgar y la cabeza profunda del flexor corto. El mediano inerva los tenares y los lumbricales 1.º–2.º."))

T("mu-0e70d6e5",
  ("Which is the largest and most superficial muscle of the gluteal region?", ["Tensor fasciae latae", "Gluteus maximus", "Gluteus minimus", "Piriformis", "Gluteus medius"],
   "Gluteus maximus is the most superficial and largest muscle of the buttock; it is the strongest extensor of the hip and is used in rising from sitting and climbing stairs."),
  ("Quel est le muscle le plus grand et le plus superficiel de la région glutéale ?", ["Muscle tenseur du fascia lata", "Muscle grand glutéal", "Muscle petit glutéal", "Muscle piriforme", "Muscle moyen glutéal"],
   "Le grand glutéal est le muscle le plus superficiel et le plus volumineux de la fesse ; c'est le plus puissant extenseur de la hanche, sollicité pour se lever d'une chaise ou monter les escaliers."),
  ("Welcher ist der größte und oberflächlichste Muskel der Gesäßregion?", ["M. tensor fasciae latae", "M. gluteus maximus", "M. gluteus minimus", "M. piriformis", "M. gluteus medius"],
   "Der M. gluteus maximus ist der oberflächlichste und größte Gesäßmuskel; er ist der stärkste Hüftstrecker und wird beim Aufstehen aus dem Sitzen und beim Treppensteigen eingesetzt."),
  ("¿Cuál es el músculo más grande y superficial de la región glútea?", ["Músculo tensor de la fascia lata", "Músculo glúteo mayor", "Músculo glúteo menor", "Músculo piriforme", "Músculo glúteo medio"],
   "El glúteo mayor es el músculo más superficial y voluminoso de la nalga; es el extensor más potente de la cadera y se usa al levantarse de una silla y al subir escaleras."))

T("mu-cfe6d009",
  ("Which is the strongest flexor of the hip?", ["Gracilis", "Pectineus", "Sartorius", "Iliopsoas", "Gluteus maximus"],
   "Iliopsoas (psoas major and iliacus) inserts on the lesser trochanter and is the strongest flexor of the hip."),
  ("Quel est le plus puissant fléchisseur de la hanche ?", ["Muscle gracile", "Muscle pectiné", "Muscle sartorius", "Muscle ilio-psoas", "Muscle grand glutéal"],
   "L'ilio-psoas (grand psoas et iliaque) se termine sur le petit trochanter et est le plus puissant fléchisseur de la hanche."),
  ("Welcher ist der stärkste Beuger des Hüftgelenks?", ["M. gracilis", "M. pectineus", "M. sartorius", "M. iliopsoas", "M. gluteus maximus"],
   "Der M. iliopsoas (M. psoas major und M. iliacus) setzt am Trochanter minor an und ist der stärkste Hüftbeuger."),
  ("¿Cuál es el flexor más potente de la cadera?", ["Músculo grácil", "Músculo pectíneo", "Músculo sartorio", "Músculo iliopsoas", "Músculo glúteo mayor"],
   "El iliopsoas (psoas mayor e ilíaco) se inserta en el trocánter menor y es el flexor más potente de la cadera."))

T("mu-c868aa3f",
  ("Which hip abductor keeps the pelvis level when standing on one leg during walking?", ["Gluteus medius", "Iliopsoas", "Gluteus maximus", "Piriformis", "Adductor longus"],
   "Gluteus medius (and minimus) abducts the hip on the stance side and prevents the opposite side of the pelvis from dropping. Its paralysis produces a positive Trendelenburg sign."),
  ("Quel abducteur de hanche maintient le bassin horizontal en appui unipodal lors de la marche ?", ["Muscle moyen glutéal", "Muscle ilio-psoas", "Muscle grand glutéal", "Muscle piriforme", "Muscle long adducteur"],
   "Le moyen glutéal (et le petit) abducte la hanche du côté de l'appui et empêche le bassin de basculer du côté opposé. Sa paralysie donne un signe de Trendelenburg."),
  ("Welcher Hüftabduktor hält beim Gehen im Einbeinstand das Becken waagerecht?", ["M. gluteus medius", "M. iliopsoas", "M. gluteus maximus", "M. piriformis", "M. adductor longus"],
   "Der M. gluteus medius (und minimus) abduziert die Hüfte des Standbeins und verhindert das Absinken der Gegenseite des Beckens. Seine Lähmung führt zum Trendelenburg-Zeichen."),
  ("¿Qué abductor de la cadera mantiene nivelada la pelvis al apoyarse en una pierna durante la marcha?", ["Músculo glúteo medio", "Músculo iliopsoas", "Músculo glúteo mayor", "Músculo piriforme", "Músculo aductor largo"],
   "El glúteo medio (y el menor) abduce la cadera del lado de apoyo e impide que la pelvis caiga del lado opuesto. Su parálisis produce el signo de Trendelenburg."))

T("mu-43cd6d79",
  ("Which four-headed muscle on the front of the thigh extends the knee?", ["Gracilis", "Quadriceps femoris", "Adductor magnus", "Sartorius", "Biceps femoris"],
   "Quadriceps femoris consists of rectus femoris and the three vasti; its common tendon encloses the patella and, via the patellar ligament, inserts on the tibial tuberosity to extend the knee."),
  ("Quel muscle à quatre chefs de la face antérieure de la cuisse étend le genou ?", ["Muscle gracile", "Muscle quadriceps fémoral", "Muscle grand adducteur", "Muscle sartorius", "Muscle biceps fémoral"],
   "Le quadriceps comprend le droit fémoral et les trois vastes ; son tendon commun englobe la patella et, par le ligament patellaire, se termine sur la tubérosité tibiale pour étendre le genou."),
  ("Welcher vierköpfige Muskel an der Vorderseite des Oberschenkels streckt das Knie?", ["M. gracilis", "M. quadriceps femoris", "M. adductor magnus", "M. sartorius", "M. biceps femoris"],
   "Der M. quadriceps femoris besteht aus M. rectus femoris und drei Mm. vasti; seine gemeinsame Sehne umschließt die Patella und setzt über das Lig. patellae an der Tuberositas tibiae an, um das Knie zu strecken."),
  ("¿Qué músculo de cuatro cabezas de la cara anterior del muslo extiende la rodilla?", ["Músculo grácil", "Músculo cuádriceps femoral", "Músculo aductor mayor", "Músculo sartorio", "Músculo bíceps femoral"],
   "El cuádriceps femoral consta del recto femoral y los tres vastos; su tendón común engloba la rótula y, por el ligamento rotuliano, se inserta en la tuberosidad tibial para extender la rodilla."))

T("mu-91b50ba3",
  ("What movement do the hamstring muscles on the back of the thigh produce at the knee?", ["No movement", "Adduction", "Abduction", "Flexion (bending)", "Extension (straightening)"],
   "The hamstrings (biceps femoris, semitendinosus, semimembranosus) extend the hip and flex the knee."),
  ("Quel mouvement les ischio-jambiers de la face postérieure de la cuisse produisent-ils au genou ?", ["Aucun mouvement", "Adduction", "Abduction", "Flexion", "Extension"],
   "Les ischio-jambiers (biceps fémoral, semi-tendineux, semi-membraneux) étendent la hanche et fléchissent le genou."),
  ("Welche Bewegung führen die ischiokruralen Muskeln an der Oberschenkelrückseite im Knie aus?", ["Keine Bewegung", "Adduktion", "Abduktion", "Flexion (Beugen)", "Extension (Strecken)"],
   "Die ischiokrurale Muskulatur (M. biceps femoris, M. semitendinosus, M. semimembranosus) streckt die Hüfte und beugt das Knie."),
  ("¿Qué movimiento producen en la rodilla los isquiotibiales de la cara posterior del muslo?", ["Ningún movimiento", "Aducción", "Abducción", "Flexión", "Extensión"],
   "Los isquiotibiales (bíceps femoral, semitendinoso, semimembranoso) extienden la cadera y flexionan la rodilla."))

T("mu-9430014d",
  ("What is the common function of the muscles of the medial compartment of the thigh?", ["Lateral rotation of the hip", "Dorsiflexion of the foot", "Moving the thigh away from the midline (abduction)", "Extending the knee", "Bringing the thigh towards the midline (adduction)"],
   "The medial compartment muscles – adductor longus, brevis, magnus, gracilis and pectineus – adduct the thigh; most are supplied by the obturator nerve."),
  ("Quelle est la fonction commune des muscles de la loge médiale de la cuisse ?", ["Rotation latérale de la hanche", "Flexion dorsale du pied", "Écarter la cuisse de la ligne médiane (abduction)", "Étendre le genou", "Rapprocher la cuisse de la ligne médiane (adduction)"],
   "Les muscles de la loge médiale – long, court et grand adducteurs, gracile et pectiné – adductent la cuisse ; la plupart sont innervés par le nerf obturateur."),
  ("Was ist die gemeinsame Funktion der Muskeln der medialen Oberschenkelloge?", ["Außenrotation der Hüfte", "Dorsalextension des Fußes", "Wegführen des Oberschenkels (Abduktion)", "Streckung des Knies", "Heranführen des Oberschenkels zur Mittellinie (Adduktion)"],
   "Die Muskeln der medialen Loge – M. adductor longus, brevis, magnus, M. gracilis und M. pectineus – adduzieren den Oberschenkel; die meisten werden vom N. obturatorius innerviert."),
  ("¿Cuál es la función común de los músculos del compartimento medial del muslo?", ["Rotación externa de la cadera", "Flexión dorsal del pie", "Separar el muslo de la línea media (abducción)", "Extender la rodilla", "Acercar el muslo a la línea media (aducción)"],
   "Los músculos del compartimento medial – aductores largo, corto y mayor, grácil y pectíneo – aducen el muslo; la mayoría los inerva el nervio obturador."))

T("mu-f30b91ef",
  ("Which muscle group forms the calf and inserts on the heel via the Achilles tendon?", ["Triceps surae (gastrocnemius and soleus)", "Fibularis longus and brevis", "Tibialis anterior and EHL", "Popliteus and plantaris", "Tibialis posterior and FDL"],
   "The two heads of gastrocnemius and soleus insert on the calcaneal tuberosity through the common Achilles tendon; they are the strongest plantar flexors of the ankle (rising on tiptoe)."),
  ("Quel groupe musculaire forme le mollet et se termine sur le talon par le tendon calcanéen (d'Achille) ?", ["Triceps sural (gastrocnémien et soléaire)", "Long et court fibulaires", "Tibial antérieur et long extenseur de l'hallux", "Poplité et plantaire", "Tibial postérieur et long fléchisseur des orteils"],
   "Les deux chefs du gastrocnémien et le soléaire se terminent sur la tubérosité calcanéenne par le tendon calcanéen commun ; ce sont les plus puissants fléchisseurs plantaires de la cheville (se dresser sur la pointe des pieds)."),
  ("Welche Muskelgruppe bildet die Wade und setzt über die Achillessehne an der Ferse an?", ["M. triceps surae (Gastrocnemius und Soleus)", "M. fibularis longus und brevis", "M. tibialis anterior und M. extensor hallucis longus", "M. popliteus und M. plantaris", "M. tibialis posterior und M. flexor digitorum longus"],
   "Die beiden Köpfe des M. gastrocnemius und der M. soleus setzen über die gemeinsame Achillessehne am Tuber calcanei an; sie sind die stärksten Plantarflexoren des Sprunggelenks (Zehenstand)."),
  ("¿Qué grupo muscular forma la pantorrilla y se inserta en el talón por el tendón de Aquiles?", ["Tríceps sural (gastrocnemio y sóleo)", "Peroneos largo y corto", "Tibial anterior y extensor largo del dedo gordo", "Poplíteo y plantar", "Tibial posterior y flexor largo de los dedos"],
   "Las dos cabezas del gastrocnemio y el sóleo se insertan en la tuberosidad del calcáneo por el tendón de Aquiles común; son los flexores plantares más potentes del tobillo (ponerse de puntillas)."))

T("mu-4b00481c",
  ("Which muscles are found in the lateral compartment of the leg?", ["Tibialis posterior and flexor digitorum longus", "Gastrocnemius and soleus", "Popliteus and plantaris", "Fibularis longus and fibularis brevis", "Tibialis anterior and extensor hallucis longus"],
   "The lateral compartment contains fibularis longus and brevis; they evert the foot and are supplied by the superficial fibular nerve."),
  ("Quels muscles trouve-t-on dans la loge latérale de la jambe ?", ["Tibial postérieur et long fléchisseur des orteils", "Gastrocnémien et soléaire", "Poplité et plantaire", "Long fibulaire et court fibulaire", "Tibial antérieur et long extenseur de l'hallux"],
   "La loge latérale contient le long et le court fibulaires ; ils mettent le pied en éversion et sont innervés par le nerf fibulaire superficiel."),
  ("Welche Muskeln liegen in der lateralen Loge des Unterschenkels?", ["M. tibialis posterior und M. flexor digitorum longus", "M. gastrocnemius und M. soleus", "M. popliteus und M. plantaris", "M. fibularis longus und M. fibularis brevis", "M. tibialis anterior und M. extensor hallucis longus"],
   "Die laterale Loge enthält M. fibularis longus und brevis; sie evertieren den Fuß und werden vom N. fibularis superficialis innerviert."),
  ("¿Qué músculos se encuentran en el compartimento lateral de la pierna?", ["Tibial posterior y flexor largo de los dedos", "Gastrocnemio y sóleo", "Poplíteo y plantar", "Peroneo largo y peroneo corto", "Tibial anterior y extensor largo del dedo gordo"],
   "El compartimento lateral contiene los peroneos largo y corto; evierten el pie y los inerva el nervio peroneo superficial."))

T("mu-26fd811e",
  ("What type of muscle tissue are skeletal muscles made of?", ["Non-striated cardiac muscle", "Striated, voluntary muscle", "Cardiac muscle", "Smooth, voluntary muscle", "Smooth, involuntary muscle"],
   "Skeletal muscles are cross-striated and voluntary, not involuntary; they are supplied by somatic motor nerves. Smooth muscle is found in the walls of internal organs, cardiac muscle in the heart."),
  ("De quel type de tissu musculaire sont faits les muscles squelettiques ?", ["Muscle cardiaque non strié", "Muscle strié volontaire", "Muscle cardiaque", "Muscle lisse volontaire", "Muscle lisse involontaire"],
   "Les muscles squelettiques sont striés et volontaires ; ils sont innervés par des nerfs moteurs somatiques. Le muscle lisse se trouve dans la paroi des viscères, le muscle cardiaque dans le cœur."),
  ("Aus welcher Art von Muskelgewebe bestehen die Skelettmuskeln?", ["Nicht quergestreifte Herzmuskulatur", "Quergestreifte, willkürliche Muskulatur", "Herzmuskulatur", "Glatte, willkürliche Muskulatur", "Glatte, unwillkürliche Muskulatur"],
   "Skelettmuskeln sind quergestreift und willkürlich; sie werden von somatomotorischen Nerven versorgt. Glatte Muskulatur findet sich in den Wänden der Eingeweide, Herzmuskulatur im Herzen."),
  ("¿De qué tipo de tejido muscular están formados los músculos esqueléticos?", ["Músculo cardíaco no estriado", "Músculo estriado voluntario", "Músculo cardíaco", "Músculo liso voluntario", "Músculo liso involuntario"],
   "Los músculos esqueléticos son estriados y voluntarios; los inervan nervios motores somáticos. El músculo liso está en la pared de las vísceras y el cardíaco en el corazón."))

T("mu-f3107df4",
  ("Which is the smallest skeletal muscle of the body?", ["Arytenoid", "Procerus", "Levator palpebrae superioris", "Stapedius", "Tensor tympani"],
   "Stapedius is a muscle of about 1 mm in the middle ear attached to the stapes; it damps stapes movement in loud sound, protecting the inner ear, and is supplied by the facial nerve."),
  ("Quel est le plus petit muscle squelettique du corps ?", ["Muscle aryténoïdien", "Muscle procérus", "Muscle releveur de la paupière supérieure", "Muscle stapédien", "Muscle tenseur du tympan"],
   "Le muscle stapédien, d'environ 1 mm, s'insère sur l'étrier dans l'oreille moyenne ; il freine l'étrier lors des sons forts pour protéger l'oreille interne et est innervé par le nerf facial."),
  ("Welches ist der kleinste Skelettmuskel des Körpers?", ["M. arytenoideus", "M. procerus", "M. levator palpebrae superioris", "M. stapedius", "M. tensor tympani"],
   "Der etwa 1 mm große M. stapedius setzt im Mittelohr am Steigbügel an; er dämpft bei lautem Schall dessen Bewegung, schützt so das Innenohr und wird vom N. facialis innerviert."),
  ("¿Cuál es el músculo esquelético más pequeño del cuerpo?", ["Músculo aritenoideo", "Músculo prócer", "Músculo elevador del párpado superior", "Músculo estapedio", "Músculo tensor del tímpano"],
   "El estapedio, de aproximadamente 1 mm, se inserta en el estribo en el oído medio; frena su movimiento ante sonidos fuertes para proteger el oído interno y lo inerva el facial."))

T("mu-87a9939b",
  ("What is the bony attachment of a muscle that stays fixed during movement called?", ["Aponeurosis", "Insertion", "Origin", "Tendon sheath", "Muscle belly"],
   "The origin is usually the proximal, fixed attachment; the insertion is the attachment on the bone that moves. When a muscle contracts, the insertion approaches the origin."),
  ("Comment appelle-t-on l'attache osseuse d'un muscle qui reste fixe pendant le mouvement ?", ["Aponévrose", "Terminaison (insertion)", "Origine", "Gaine tendineuse", "Corps (ventre) musculaire"],
   "L'origine est en général l'attache proximale fixe ; la terminaison est l'attache sur l'os mobile. Quand le muscle se contracte, la terminaison se rapproche de l'origine."),
  ("Wie heißt der Knochenansatz eines Muskels, der bei der Bewegung fest bleibt?", ["Aponeurose", "Ansatz (Insertio)", "Ursprung (Origo)", "Sehnenscheide", "Muskelbauch (Venter)"],
   "Der Ursprung ist meist die proximale, feste Anheftung; der Ansatz liegt am bewegten Knochen. Bei der Kontraktion nähert sich der Ansatz dem Ursprung."),
  ("¿Cómo se llama la inserción ósea de un músculo que permanece fija durante el movimiento?", ["Aponeurosis", "Inserción", "Origen", "Vaina tendinosa", "Vientre muscular"],
   "El origen suele ser la inserción proximal fija; la inserción es la unión al hueso que se mueve. Al contraerse el músculo, la inserción se acerca al origen."))

T("mu-68e69843",
  ("Where does temporalis arise?", ["From the pterygoid process", "From the mastoid process", "From the superior nuchal line", "From the zygomatic arch", "From the temporal fossa and temporal fascia"],
   "Temporalis arises from the floor of the temporal fossa and the fascia covering it; it passes deep to the zygomatic arch to insert on the coronoid process."),
  ("D'où naît le muscle temporal ?", ["Du processus ptérygoïde", "Du processus mastoïde", "De la ligne nucale supérieure", "De l'arcade zygomatique", "De la fosse temporale et du fascia temporal"],
   "Le temporal naît du plancher de la fosse temporale et du fascia qui la recouvre ; il passe sous l'arcade zygomatique pour se terminer sur le processus coronoïde."),
  ("Wo entspringt der M. temporalis?", ["Am Processus pterygoideus", "Am Processus mastoideus", "An der Linea nuchae superior", "Am Arcus zygomaticus", "In der Fossa temporalis und an der Fascia temporalis"],
   "Der M. temporalis entspringt am Boden der Fossa temporalis und an der sie bedeckenden Faszie; er zieht unter dem Jochbogen hindurch zum Processus coronoideus."),
  ("¿Dónde se origina el músculo temporal?", ["En la apófisis pterigoides", "En la apófisis mastoides", "En la línea nucal superior", "En el arco cigomático", "En la fosa temporal y la fascia temporal"],
   "El temporal se origina en el suelo de la fosa temporal y en la fascia que la cubre; pasa por debajo del arco cigomático para insertarse en la apófisis coronoides."))

T("mu-a88fccee",
  ("What is the main function of buccinator?", ["Pressing the cheek against the teeth to keep food between them during chewing, and blowing", "Opening the mouth", "Protruding the tongue", "Raising the corner of the mouth", "Closing the jaw"],
   "Buccinator is the muscular layer of the cheek; it stops food escaping between cheek and teeth and tightens the cheek when blowing (playing the trumpet). It is supplied by the facial nerve and pierced by the parotid duct."),
  ("Quelle est la fonction principale du buccinateur ?", ["Plaquer la joue contre les dents pour maintenir le bol entre elles et souffler", "Ouvrir la bouche", "Tirer la langue", "Élever l'angle de la bouche", "Fermer la mâchoire"],
   "Le buccinateur forme la couche musculaire de la joue ; il empêche les aliments de passer entre joue et dents et tend la joue pour souffler (trompette). Il est innervé par le nerf facial et traversé par le conduit parotidien."),
  ("Was ist die Hauptfunktion des M. buccinator?", ["Die Wange an die Zähne drücken, um den Bissen zwischen den Zähnen zu halten, und Blasen", "Den Mund öffnen", "Die Zunge herausstrecken", "Den Mundwinkel heben", "Den Kiefer schließen"],
   "Der M. buccinator bildet die Muskelschicht der Wange; er verhindert, dass Nahrung zwischen Wange und Zähne gerät, und spannt die Wange beim Blasen (Trompete). Er wird vom N. facialis innerviert und vom Ductus parotideus durchbohrt."),
  ("¿Cuál es la función principal del buccinador?", ["Apretar la mejilla contra los dientes para mantener el bolo entre ellos al masticar, y soplar", "Abrir la boca", "Sacar la lengua", "Elevar la comisura bucal", "Cerrar la mandíbula"],
   "El buccinador es la capa muscular de la mejilla; impide que el alimento se escape entre mejilla y dientes y tensa la mejilla al soplar (tocar la trompeta). Lo inerva el facial y lo atraviesa el conducto parotídeo."))

T("mu-20439cf3",
  ("Which muscle pulls the corner of the mouth down (sad expression)?", ["Levator anguli oris", "Levator labii superioris", "Depressor anguli oris", "Zygomaticus major", "Risorius"],
   "Depressor anguli oris runs from the lower border of the mandible to the corner of the mouth and pulls it down. Zygomaticus major pulls the corner upwards and outwards (smiling)."),
  ("Quel muscle abaisse l'angle de la bouche (expression triste) ?", ["Muscle élévateur de l'angle de la bouche", "Muscle élévateur de la lèvre supérieure", "Muscle abaisseur de l'angle de la bouche", "Muscle grand zygomatique", "Muscle risorius"],
   "L'abaisseur de l'angle de la bouche va du bord inférieur de la mandibule à la commissure et l'abaisse. Le grand zygomatique tire la commissure en haut et en dehors (sourire)."),
  ("Welcher Muskel zieht den Mundwinkel nach unten (trauriger Ausdruck)?", ["M. levator anguli oris", "M. levator labii superioris", "M. depressor anguli oris", "M. zygomaticus major", "M. risorius"],
   "Der M. depressor anguli oris zieht vom Unterrand des Unterkiefers zum Mundwinkel und senkt ihn. Der M. zygomaticus major zieht den Mundwinkel nach oben außen (Lächeln)."),
  ("¿Qué músculo desciende la comisura de la boca (expresión triste)?", ["Músculo elevador del ángulo de la boca", "Músculo elevador del labio superior", "Músculo depresor del ángulo de la boca", "Músculo cigomático mayor", "Músculo risorio"],
   "El depresor del ángulo de la boca va del borde inferior de la mandíbula a la comisura y la desciende. El cigomático mayor tira de la comisura hacia arriba y afuera (sonrisa)."))

T("mu-c19c6bea",
  ("Which muscle divides the neck into anterior and posterior triangles?", ["Scalenus anterior", "Trapezius", "Sternocleidomastoid", "Digastric", "Omohyoid"],
   "The anterior triangle lies in front of SCM, the posterior triangle between SCM and trapezius. Omohyoid and digastric subdivide these triangles into smaller ones."),
  ("Quel muscle divise le cou en triangles antérieur et postérieur ?", ["Muscle scalène antérieur", "Muscle trapèze", "Muscle sterno-cléido-mastoïdien", "Muscle digastrique", "Muscle omo-hyoïdien"],
   "Le triangle antérieur est en avant du SCM, le triangle postérieur entre le SCM et le trapèze. L'omo-hyoïdien et le digastrique subdivisent ces triangles en triangles plus petits."),
  ("Welcher Muskel teilt den Hals in vorderes und seitliches Halsdreieck?", ["M. scalenus anterior", "M. trapezius", "M. sternocleidomastoideus", "M. digastricus", "M. omohyoideus"],
   "Vor dem M. sternocleidomastoideus liegt das vordere, zwischen ihm und dem M. trapezius das seitliche Halsdreieck. M. omohyoideus und M. digastricus unterteilen sie in kleinere Dreiecke."),
  ("¿Qué músculo divide el cuello en triángulos anterior y posterior?", ["Músculo escaleno anterior", "Músculo trapecio", "Músculo esternocleidomastoideo", "Músculo digástrico", "Músculo omohioideo"],
   "El triángulo anterior está delante del ECM y el posterior entre el ECM y el trapecio. El omohioideo y el digástrico los subdividen en triángulos más pequeños."))

T("mu-ca04a98c",
  ("Where does scalenus anterior arise?", ["From the occipital bone", "From the posterior tubercles of the C1–C4 transverse processes", "From the T1–T4 spinous processes", "From the anterior tubercles of the C3–C6 transverse processes", "From the 1st rib"],
   "Scalenus anterior arises from the anterior tubercles of the C3–C6 transverse processes and inserts on the scalene tubercle of the 1st rib; the phrenic nerve descends on its front."),
  ("D'où naît le muscle scalène antérieur ?", ["De l'os occipital", "Des tubercules postérieurs des processus transverses de C1–C4", "Des processus épineux de T1–T4", "Des tubercules antérieurs des processus transverses de C3–C6", "De la 1re côte"],
   "Le scalène antérieur naît des tubercules antérieurs des processus transverses de C3 à C6 et se termine sur le tubercule du scalène de la 1re côte ; le nerf phrénique descend sur sa face antérieure."),
  ("Wo entspringt der M. scalenus anterior?", ["Am Hinterhauptsbein", "An den Tubercula posteriora der Querfortsätze C1–C4", "An den Dornfortsätzen T1–T4", "An den Tubercula anteriora der Querfortsätze C3–C6", "An der 1. Rippe"],
   "Der M. scalenus anterior entspringt an den Tubercula anteriora der Querfortsätze C3–C6 und setzt am Tuberculum m. scaleni anterioris der 1. Rippe an; auf ihm zieht der N. phrenicus abwärts."),
  ("¿Dónde se origina el músculo escaleno anterior?", ["En el occipital", "En los tubérculos posteriores de las apófisis transversas de C1–C4", "En las apófisis espinosas de T1–T4", "En los tubérculos anteriores de las apófisis transversas de C3–C6", "En la 1.ª costilla"],
   "El escaleno anterior se origina en los tubérculos anteriores de las apófisis transversas de C3–C6 y se inserta en el tubérculo escaleno de la 1.ª costilla; el nervio frénico desciende por su cara anterior."))
