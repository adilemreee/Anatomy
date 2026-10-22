KIND = "questions"
SYSTEM = "muscular"
E = {}


def T(id, en, fr, de, es):
    E[id] = {"en": list(en), "fr": list(fr), "de": list(de), "es": list(es)}


T("mu-df74918e",
  ("Which fibres of trapezius retract the scapula (towards the spine)?", ["None; trapezius does not retract the scapula", "Upper (descending) fibres", "Lower (ascending) fibres", "Middle (transverse) fibres", "Only the clavicular fibres"],
   "The middle fibres of trapezius retract the scapula. The upper fibres elevate it, the lower fibres depress it; upper and lower fibres together rotate it upwards."),
  ("Quelles fibres du trapèze rapprochent la scapula du rachis (rétraction) ?", ["Aucune ; le trapèze ne rétracte pas la scapula", "Fibres supérieures (descendantes)", "Fibres inférieures (ascendantes)", "Fibres moyennes (transverses)", "Seulement les fibres claviculaires"],
   "Les fibres moyennes du trapèze rétractent la scapula. Les supérieures l'élèvent, les inférieures l'abaissent ; ensemble, supérieures et inférieures la font tourner vers le haut."),
  ("Welche Fasern des M. trapezius ziehen die Scapula nach hinten (zur Wirbelsäule)?", ["Keine; der Trapezius retrahiert die Scapula nicht", "Obere (absteigende) Fasern", "Untere (aufsteigende) Fasern", "Mittlere (quere) Fasern", "Nur die klavikulären Fasern"],
   "Die mittleren Fasern des M. trapezius retrahieren die Scapula. Die oberen heben, die unteren senken sie; obere und untere Fasern zusammen drehen sie nach oben."),
  ("¿Qué fibras del trapecio retraen la escápula (hacia la columna)?", ["Ninguna; el trapecio no retrae la escápula", "Fibras superiores (descendentes)", "Fibras inferiores (ascendentes)", "Fibras medias (transversas)", "Solo las fibras claviculares"],
   "Las fibras medias del trapecio retraen la escápula. Las superiores la elevan y las inferiores la descienden; juntas, superiores e inferiores la rotan hacia arriba."))

T("mu-0d5e6a60",
  ("What happens in the thoracic cavity when the diaphragm contracts?", ["The anteroposterior diameter of the chest decreases.", "The ribs are pulled down and expiration occurs.", "The dome rises and thoracic volume decreases.", "Intra-abdominal pressure falls.", "The dome descends and the vertical diameter of the chest increases."],
   "When the diaphragm contracts its dome flattens and descends; the vertical diameter of the thoracic cavity increases and air flows in. Meanwhile intra-abdominal pressure rises."),
  ("Que se passe-t-il dans le thorax quand le diaphragme se contracte ?", ["Le diamètre antéro-postérieur du thorax diminue.", "Les côtes sont abaissées et c'est l'expiration.", "La coupole s'élève et le volume thoracique diminue.", "La pression intra-abdominale baisse.", "La coupole s'abaisse et le diamètre vertical du thorax augmente."],
   "En se contractant, le diaphragme aplatit et abaisse sa coupole ; le diamètre vertical du thorax augmente et l'air entre. Pendant ce temps, la pression intra-abdominale augmente."),
  ("Was geschieht im Brustraum, wenn sich das Zwerchfell kontrahiert?", ["Der Sagittaldurchmesser des Thorax nimmt ab.", "Die Rippen werden gesenkt und es kommt zur Ausatmung.", "Die Kuppel steigt und das Thoraxvolumen nimmt ab.", "Der intraabdominelle Druck sinkt.", "Die Kuppel senkt sich und der vertikale Thoraxdurchmesser nimmt zu."],
   "Bei Kontraktion flacht die Zwerchfellkuppel ab und senkt sich; der vertikale Durchmesser des Brustraums nimmt zu und Luft strömt ein. Dabei steigt der intraabdominelle Druck."),
  ("¿Qué ocurre en la cavidad torácica cuando se contrae el diafragma?", ["Disminuye el diámetro anteroposterior del tórax.", "Las costillas descienden y se produce la espiración.", "La cúpula asciende y disminuye el volumen torácico.", "Disminuye la presión intraabdominal.", "La cúpula desciende y aumenta el diámetro vertical del tórax."],
   "Al contraerse, la cúpula del diafragma se aplana y desciende; aumenta el diámetro vertical de la cavidad torácica y entra el aire. Mientras tanto, aumenta la presión intraabdominal."))

T("mu-2efd9cbe",
  ("What is the main action of serratus anterior?", ["Pulling the scapula forwards (protraction) and rotating it upwards", "Medially rotating the arm", "Pulling the ribs down", "Depressing and pushing the scapula back", "Retracting the scapula"],
   "Serratus anterior holds the scapula against the chest wall, pulls it forwards (the 'boxer's muscle') and, with trapezius, rotates it upwards so the arm can be raised above 90°."),
  ("Quelle est l'action principale du dentelé antérieur ?", ["Porter la scapula en avant (protraction) et la faire tourner vers le haut", "Tourner le bras en dedans", "Abaisser les côtes", "Abaisser et reculer la scapula", "Rétracter la scapula"],
   "Le dentelé antérieur plaque la scapula contre le thorax, la porte en avant (muscle du boxeur) et, avec le trapèze, la fait tourner vers le haut pour élever le bras au-delà de 90°."),
  ("Was ist die Hauptwirkung des M. serratus anterior?", ["Die Scapula nach vorn ziehen (Protraktion) und nach oben drehen", "Den Arm innenrotieren", "Die Rippen senken", "Die Scapula senken und zurückschieben", "Die Scapula retrahieren"],
   "Der M. serratus anterior hält die Scapula am Brustkorb, zieht sie nach vorn („Boxermuskel“) und dreht sie mit dem Trapezius nach oben, damit der Arm über 90° gehoben werden kann."),
  ("¿Cuál es la acción principal del serrato anterior?", ["Llevar la escápula hacia delante (protracción) y rotarla hacia arriba", "Rotar internamente el brazo", "Descender las costillas", "Descender y empujar hacia atrás la escápula", "Retraer la escápula"],
   "El serrato anterior mantiene la escápula contra la pared torácica, la lleva hacia delante (músculo del boxeador) y, con el trapecio, la rota hacia arriba para elevar el brazo por encima de 90°."))

T("mu-ae88dbac",
  ("Which nerve supplies subclavius?", ["Lateral pectoral nerve", "Phrenic nerve", "Dorsal scapular nerve", "Long thoracic nerve", "Nerve to subclavius (C5–C6)"],
   "The nerve to subclavius is a small branch of the upper trunk of the brachial plexus; it sometimes gives an accessory phrenic nerve that joins the phrenic nerve."),
  ("Quel nerf innerve le muscle subclavier ?", ["Nerf pectoral latéral", "Nerf phrénique", "Nerf dorsal de la scapula", "Nerf thoracique long", "Nerf du subclavier (C5–C6)"],
   "Le nerf du subclavier est une petite branche du tronc supérieur du plexus brachial ; il donne parfois un nerf phrénique accessoire qui rejoint le phrénique."),
  ("Welcher Nerv innerviert den M. subclavius?", ["N. pectoralis lateralis", "N. phrenicus", "N. dorsalis scapulae", "N. thoracicus longus", "N. subclavius (C5–C6)"],
   "Der N. subclavius ist ein kleiner Ast des oberen Primärstrangs des Plexus brachialis; er gibt manchmal einen Nebenphrenikus ab, der sich dem N. phrenicus anschließt."),
  ("¿Qué nervio inerva el músculo subclavio?", ["Nervio pectoral lateral", "Nervio frénico", "Nervio dorsal de la escápula", "Nervio torácico largo", "Nervio del subclavio (C5–C6)"],
   "El nervio del subclavio es una pequeña rama del tronco superior del plexo braquial; a veces da un nervio frénico accesorio que se une al frénico."))

T("mu-366192ec",
  ("What is the main function of transversus abdominis?", ["Bending the trunk forwards", "Rotating the trunk", "Compressing the abdominal wall to raise intra-abdominal pressure", "Tilting the pelvis forwards", "Raising the ribs"],
   "With its horizontal fibres transversus abdominis tightens the abdominal wall like a belt; it raises intra-abdominal pressure in coughing, straining, childbirth and forced expiration, and stabilises the trunk."),
  ("Quelle est la fonction principale du transverse de l'abdomen ?", ["Fléchir le tronc en avant", "Faire tourner le tronc", "Comprimer la paroi abdominale pour augmenter la pression intra-abdominale", "Antéverser le bassin", "Élever les côtes"],
   "Par ses fibres horizontales, le transverse serre la paroi abdominale comme une ceinture ; il augmente la pression intra-abdominale lors de la toux, de la poussée, de l'accouchement et de l'expiration forcée, et stabilise le tronc."),
  ("Was ist die Hauptfunktion des M. transversus abdominis?", ["Den Rumpf nach vorn beugen", "Den Rumpf drehen", "Die Bauchwand zusammenpressen und den intraabdominellen Druck erhöhen", "Das Becken nach vorn kippen", "Die Rippen heben"],
   "Mit seinen queren Fasern schnürt der M. transversus abdominis die Bauchwand wie ein Gürtel; er erhöht den intraabdominellen Druck beim Husten, Pressen, Gebären und forcierter Ausatmung und stabilisiert den Rumpf."),
  ("¿Cuál es la función principal del transverso del abdomen?", ["Flexionar el tronco hacia delante", "Rotar el tronco", "Comprimir la pared abdominal y aumentar la presión intraabdominal", "Inclinar la pelvis hacia delante", "Elevar las costillas"],
   "Con sus fibras horizontales el transverso ciñe la pared abdominal como un cinturón; aumenta la presión intraabdominal al toser, pujar, en el parto y en la espiración forzada, y estabiliza el tronco."))

T("mu-05477470",
  ("Which is the main structure forming the anterior wall of the inguinal canal?", ["Transversalis fascia", "Inguinal ligament", "External oblique aponeurosis", "Inguinal falx (conjoint tendon)", "Rectus abdominis"],
   "The anterior wall of the inguinal canal is the external oblique aponeurosis (reinforced laterally by internal oblique fibres), the posterior wall the transversalis fascia (medially the conjoint tendon), and the floor the inguinal ligament."),
  ("Quelle est la principale structure formant la paroi antérieure du canal inguinal ?", ["Fascia transversalis", "Ligament inguinal", "Aponévrose de l'oblique externe", "Faux inguinale (tendon conjoint)", "Muscle droit de l'abdomen"],
   "La paroi antérieure du canal inguinal est l'aponévrose de l'oblique externe (renforcée en dehors par l'oblique interne), la paroi postérieure le fascia transversalis (en dedans le tendon conjoint), et le plancher le ligament inguinal."),
  ("Welche Struktur bildet hauptsächlich die Vorderwand des Leistenkanals?", ["Fascia transversalis", "Lig. inguinale", "Aponeurose des M. obliquus externus abdominis", "Falx inguinalis (Conjoint tendon)", "M. rectus abdominis"],
   "Die Vorderwand des Leistenkanals bildet die Externusaponeurose (lateral durch Fasern des M. obliquus internus verstärkt), die Hinterwand die Fascia transversalis (medial die Falx inguinalis), den Boden das Leistenband."),
  ("¿Cuál es la principal estructura que forma la pared anterior del conducto inguinal?", ["Fascia transversalis", "Ligamento inguinal", "Aponeurosis del oblicuo externo", "Hoz inguinal (tendón conjunto)", "Músculo recto del abdomen"],
   "La pared anterior del conducto inguinal es la aponeurosis del oblicuo externo (reforzada lateralmente por fibras del oblicuo interno), la posterior la fascia transversalis (medialmente el tendón conjunto) y el suelo el ligamento inguinal."))

T("mu-adf21325",
  ("Which of the following is NOT a part of levator ani?", ["Puborectalis", "Pubococcygeus", "Coccygeus", "Puboprostaticus/pubovaginalis", "Iliococcygeus"],
   "Levator ani consists of puborectalis, pubococcygeus (with pubovaginalis/puboprostaticus fibres) and iliococcygeus. Coccygeus is a separate muscle of the pelvic diaphragm."),
  ("Lequel des suivants n'est PAS une partie de l'élévateur de l'anus ?", ["Pubo-rectal", "Pubo-coccygien", "Muscle coccygien", "Pubo-prostatique/pubo-vaginal", "Ilio-coccygien"],
   "L'élévateur de l'anus comprend le pubo-rectal, le pubo-coccygien (avec ses fibres pubo-vaginales/pubo-prostatiques) et l'ilio-coccygien. Le coccygien est un muscle distinct du diaphragme pelvien."),
  ("Welcher der folgenden ist KEIN Teil des M. levator ani?", ["M. puborectalis", "M. pubococcygeus", "M. coccygeus", "M. puboprostaticus/pubovaginalis", "M. iliococcygeus"],
   "Der M. levator ani besteht aus M. puborectalis, M. pubococcygeus (mit pubovaginalen/puboprostatischen Fasern) und M. iliococcygeus. Der M. coccygeus ist ein eigener Muskel des Diaphragma pelvis."),
  ("¿Cuál de los siguientes NO forma parte del elevador del ano?", ["Puborrectal", "Pubococcígeo", "Músculo coccígeo", "Puboprostático/pubovaginal", "Iliococcígeo"],
   "El elevador del ano consta de puborrectal, pubococcígeo (con fibras pubovaginales/puboprostáticas) e iliococcígeo. El coccígeo es un músculo aparte del diafragma pélvico."))

T("mu-730ee30b",
  ("Which nerve supplies teres minor?", ["Lower subscapular nerve", "Axillary nerve", "Thoracodorsal nerve", "Radial nerve", "Suprascapular nerve"],
   "The axillary nerve supplies deltoid and teres minor. Supraspinatus and infraspinatus are supplied by the suprascapular nerve, subscapularis and teres major by the subscapular nerves."),
  ("Quel nerf innerve le petit rond ?", ["Nerf subscapulaire inférieur", "Nerf axillaire", "Nerf thoraco-dorsal", "Nerf radial", "Nerf suprascapulaire"],
   "Le nerf axillaire innerve le deltoïde et le petit rond. Le supra- et l'infra-épineux sont innervés par le nerf suprascapulaire, le subscapulaire et le grand rond par les nerfs subscapulaires."),
  ("Welcher Nerv innerviert den M. teres minor?", ["N. subscapularis inferior", "N. axillaris", "N. thoracodorsalis", "N. radialis", "N. suprascapularis"],
   "Der N. axillaris innerviert M. deltoideus und M. teres minor. M. supraspinatus und infraspinatus werden vom N. suprascapularis, M. subscapularis und M. teres major von den Nn. subscapulares versorgt."),
  ("¿Qué nervio inerva el redondo menor?", ["Nervio subescapular inferior", "Nervio axilar", "Nervio toracodorsal", "Nervio radial", "Nervio supraescapular"],
   "El nervio axilar inerva el deltoides y el redondo menor. El supraespinoso y el infraespinoso los inerva el supraescapular; el subescapular y el redondo mayor, los nervios subescapulares."))

T("mu-69780f6b",
  ("What is the innervation of brachialis?", ["Median nerve", "Axillary nerve", "Radial nerve only", "Ulnar nerve", "Mainly the musculocutaneous nerve (its lateral part also receives radial fibres)"],
   "The three muscles of the anterior arm compartment (biceps, brachialis, coracobrachialis) are supplied by the musculocutaneous nerve; the lateral part of brachialis additionally receives fibres from the radial nerve."),
  ("Quelle est l'innervation du muscle brachial ?", ["Nerf médian", "Nerf axillaire", "Nerf radial seul", "Nerf ulnaire", "Surtout le nerf musculo-cutané (sa partie latérale reçoit aussi des fibres du radial)"],
   "Les trois muscles de la loge antérieure du bras (biceps, brachial, coraco-brachial) sont innervés par le musculo-cutané ; la partie latérale du brachial reçoit en plus des fibres du nerf radial."),
  ("Wie wird der M. brachialis innerviert?", ["N. medianus", "N. axillaris", "Nur N. radialis", "N. ulnaris", "Hauptsächlich N. musculocutaneus (lateraler Anteil auch vom N. radialis)"],
   "Die drei Muskeln der vorderen Oberarmloge (Biceps, Brachialis, Coracobrachialis) werden vom N. musculocutaneus innerviert; der laterale Anteil des M. brachialis erhält zusätzlich Fasern vom N. radialis."),
  ("¿Cuál es la inervación del músculo braquial?", ["Nervio mediano", "Nervio axilar", "Solo el nervio radial", "Nervio cubital", "Sobre todo el musculocutáneo (su parte lateral recibe también fibras del radial)"],
   "Los tres músculos del compartimento anterior del brazo (bíceps, braquial, coracobraquial) los inerva el musculocutáneo; la parte lateral del braquial recibe además fibras del radial."))

T("mu-e17dab33",
  ("What are the function and innervation of anconeus?", ["Flexes the elbow – radial nerve", "Assists elbow extension – radial nerve", "Extends the wrist – ulnar nerve", "Flexes the elbow – musculocutaneous nerve", "Supinates the forearm – median nerve"],
   "Anconeus is a small muscle running from the lateral epicondyle to the lateral surface of the olecranon; it assists triceps and tenses the elbow joint capsule."),
  ("Quelles sont la fonction et l'innervation de l'anconé ?", ["Fléchit le coude – nerf radial", "Aide à l'extension du coude – nerf radial", "Étend le poignet – nerf ulnaire", "Fléchit le coude – nerf musculo-cutané", "Met l'avant-bras en supination – nerf médian"],
   "L'anconé est un petit muscle allant de l'épicondyle latéral à la face latérale de l'olécrâne ; il aide le triceps et tend la capsule du coude."),
  ("Welche Funktion und Innervation hat der M. anconeus?", ["Beugt den Ellenbogen – N. radialis", "Unterstützt die Ellenbogenstreckung – N. radialis", "Streckt das Handgelenk – N. ulnaris", "Beugt den Ellenbogen – N. musculocutaneus", "Supiniert den Unterarm – N. medianus"],
   "Der M. anconeus ist ein kleiner Muskel vom Epicondylus lateralis zur Außenseite des Olekranons; er unterstützt den Triceps und spannt die Ellenbogengelenkkapsel."),
  ("¿Cuáles son la función y la inervación del ancóneo?", ["Flexiona el codo – nervio radial", "Ayuda a la extensión del codo – nervio radial", "Extiende la muñeca – nervio cubital", "Flexiona el codo – nervio musculocutáneo", "Supina el antebrazo – nervio mediano"],
   "El ancóneo es un músculo pequeño que va del epicóndilo lateral a la cara lateral del olécranon; ayuda al tríceps y tensa la cápsula del codo."))

T("mu-36c5af6d",
  ("What is the order of the superficial forearm flexors from lateral (radial) to medial (ulnar)?", ["Flexor carpi radialis, pronator teres, flexor carpi ulnaris, palmaris longus", "Pronator teres, palmaris longus, flexor carpi radialis, flexor carpi ulnaris", "Pronator teres, flexor carpi radialis, palmaris longus, flexor carpi ulnaris", "Palmaris longus, flexor carpi radialis, pronator teres, flexor carpi ulnaris", "Flexor carpi ulnaris, palmaris longus, flexor carpi radialis, pronator teres"],
   "Placing the right hand on the chest with the thumb lateral, you can count the four muscles: PT, FCR, PL, FCU. All arise from the common flexor origin on the medial epicondyle; FDS lies deep to them."),
  ("Quel est l'ordre des fléchisseurs superficiels de l'avant-bras de dehors (radial) en dedans (ulnaire) ?", ["Fléchisseur radial du carpe, rond pronateur, fléchisseur ulnaire du carpe, long palmaire", "Rond pronateur, long palmaire, fléchisseur radial du carpe, fléchisseur ulnaire du carpe", "Rond pronateur, fléchisseur radial du carpe, long palmaire, fléchisseur ulnaire du carpe", "Long palmaire, fléchisseur radial du carpe, rond pronateur, fléchisseur ulnaire du carpe", "Fléchisseur ulnaire du carpe, long palmaire, fléchisseur radial du carpe, rond pronateur"],
   "En posant la main droite sur la poitrine, pouce en dehors, on compte les quatre muscles : RP, FRC, LP, FUC. Tous naissent du tendon commun des fléchisseurs sur l'épicondyle médial ; le fléchisseur superficiel des doigts est plus profond."),
  ("Wie ist die Reihenfolge der oberflächlichen Unterarmbeuger von radial nach ulnar?", ["Flexor carpi radialis, Pronator teres, Flexor carpi ulnaris, Palmaris longus", "Pronator teres, Palmaris longus, Flexor carpi radialis, Flexor carpi ulnaris", "Pronator teres, Flexor carpi radialis, Palmaris longus, Flexor carpi ulnaris", "Palmaris longus, Flexor carpi radialis, Pronator teres, Flexor carpi ulnaris", "Flexor carpi ulnaris, Palmaris longus, Flexor carpi radialis, Pronator teres"],
   "Legt man die rechte Hand mit dem Daumen außen auf die Brust, kann man die vier Muskeln abzählen: PT, FCR, PL, FCU. Alle entspringen dem gemeinsamen Beugerursprung am Epicondylus medialis; der M. flexor digitorum superficialis liegt tiefer."),
  ("¿Cuál es el orden de los flexores superficiales del antebrazo de lateral (radial) a medial (cubital)?", ["Flexor radial del carpo, pronador redondo, flexor cubital del carpo, palmar largo", "Pronador redondo, palmar largo, flexor radial del carpo, flexor cubital del carpo", "Pronador redondo, flexor radial del carpo, palmar largo, flexor cubital del carpo", "Palmar largo, flexor radial del carpo, pronador redondo, flexor cubital del carpo", "Flexor cubital del carpo, palmar largo, flexor radial del carpo, pronador redondo"],
   "Colocando la mano derecha sobre el pecho con el pulgar por fuera se cuentan los cuatro músculos: PR, FRC, PL, FCC. Todos nacen del origen común de los flexores en el epicóndilo medial; el flexor superficial de los dedos está por debajo."))

T("mu-6e2f450b",
  ("Where do the FDS and FDP tendons insert in the fingers?", ["Both on the proximal phalanx", "FDS on the middle phalanx, FDP on the distal phalanx", "Both on the distal phalanx", "FDS on the distal phalanx, FDP on the middle phalanx", "FDS on the metacarpal head, FDP on the middle phalanx"],
   "The FDS tendon splits in two at the level of the proximal phalanx (Camper's chiasm), and the FDP tendon passes through the split to reach the distal phalanx. DIP flexion is therefore produced only by FDP."),
  ("Où se terminent les tendons du FDS et du FDP dans les doigts ?", ["Tous deux sur la phalange proximale", "FDS sur la phalange moyenne, FDP sur la phalange distale", "Tous deux sur la phalange distale", "FDS sur la phalange distale, FDP sur la phalange moyenne", "FDS sur la tête métacarpienne, FDP sur la phalange moyenne"],
   "Le tendon du fléchisseur superficiel se divise en deux au niveau de la phalange proximale (chiasma de Camper) et le tendon du profond passe par cette boutonnière pour atteindre la phalange distale. La flexion de l'IPD dépend donc du seul fléchisseur profond."),
  ("Wo setzen die Sehnen von FDS und FDP an den Fingern an?", ["Beide an der Grundphalanx", "FDS an der Mittelphalanx, FDP an der Endphalanx", "Beide an der Endphalanx", "FDS an der Endphalanx, FDP an der Mittelphalanx", "FDS am Metakarpalkopf, FDP an der Mittelphalanx"],
   "Die FDS-Sehne spaltet sich auf Höhe der Grundphalanx (Chiasma tendinum, Camper), die FDP-Sehne zieht durch diesen Schlitz zur Endphalanx. Die Beugung im DIP-Gelenk erfolgt daher nur durch den FDP."),
  ("¿Dónde se insertan los tendones del FDS y del FDP en los dedos?", ["Ambos en la falange proximal", "FDS en la falange media, FDP en la falange distal", "Ambos en la falange distal", "FDS en la falange distal, FDP en la falange media", "FDS en la cabeza del metacarpiano, FDP en la falange media"],
   "El tendón del flexor superficial se divide en dos a la altura de la falange proximal (quiasma de Camper) y el del profundo pasa por esa hendidura hasta la falange distal. Por eso la flexión de la IFD depende solo del flexor profundo."))

T("mu-c1a77b62",
  ("Which muscle allows the index finger to be extended independently of the other fingers?", ["Abductor pollicis longus", "Extensor digitorum", "Extensor digiti minimi", "Extensor pollicis longus", "Extensor indicis"],
   "Extensor indicis is one of the deep forearm extensors and allows independent extension of the index finger (pointing). Its tendon is often used in tendon transfers."),
  ("Quel muscle permet d'étendre l'index indépendamment des autres doigts ?", ["Muscle long abducteur du pouce", "Muscle extenseur des doigts", "Muscle extenseur du petit doigt", "Muscle long extenseur du pouce", "Muscle extenseur de l'index"],
   "L'extenseur de l'index fait partie des extenseurs profonds de l'avant-bras et permet l'extension indépendante de l'index (montrer du doigt). Son tendon est souvent utilisé pour les transferts tendineux."),
  ("Welcher Muskel ermöglicht es, den Zeigefinger unabhängig von den anderen Fingern zu strecken?", ["M. abductor pollicis longus", "M. extensor digitorum", "M. extensor digiti minimi", "M. extensor pollicis longus", "M. extensor indicis"],
   "Der M. extensor indicis gehört zu den tiefen Unterarmstreckern und ermöglicht die unabhängige Streckung des Zeigefingers (Zeigen). Seine Sehne wird oft für Sehnentransfers genutzt."),
  ("¿Qué músculo permite extender el índice independientemente de los otros dedos?", ["Músculo abductor largo del pulgar", "Músculo extensor de los dedos", "Músculo extensor del meñique", "Músculo extensor largo del pulgar", "Músculo extensor del índice"],
   "El extensor del índice es uno de los extensores profundos del antebrazo y permite la extensión independiente del índice (señalar). Su tendón se usa a menudo en transferencias tendinosas."))

T("mu-b5a54a42",
  ("Mallet finger is an injury of which structure?", ["Collateral ligament of the MCP joint", "Volar plate of the PIP joint", "Terminal part of the extensor tendon inserting on the distal phalanx", "Central slip of the extensor tendon", "Insertion of the FDP tendon on the distal phalanx"],
   "A blow to the fingertip ruptures the end of the extensor tendon on the distal phalanx, and the patient cannot actively extend the DIP joint. A central slip injury causes a boutonnière deformity."),
  ("Le doigt en maillet est une lésion de quelle structure ?", ["Ligament collatéral de la MCP", "Plaque palmaire de l'IPP", "Partie terminale de l'extenseur insérée sur la phalange distale", "Bandelette médiane de l'extenseur", "Insertion du FDP sur la phalange distale"],
   "Un choc sur le bout du doigt rompt l'extrémité du tendon extenseur sur la phalange distale et le patient ne peut plus étendre activement l'IPD. La lésion de la bandelette médiane donne une déformation en boutonnière."),
  ("Der Hammerfinger (Mallet-Finger) ist eine Verletzung welcher Struktur?", ["Kollateralband des MCP-Gelenks", "Palmare Platte des PIP-Gelenks", "Endsehne des Strecksehnenapparats an der Endphalanx", "Mittelzügel der Strecksehne", "Ansatz der FDP-Sehne an der Endphalanx"],
   "Ein Stoß auf die Fingerkuppe zerreißt das Ende der Strecksehne an der Endphalanx; der Patient kann das DIP-Gelenk nicht aktiv strecken. Eine Mittelzügelverletzung führt zur Knopflochdeformität."),
  ("El dedo en martillo es una lesión de ¿qué estructura?", ["Ligamento colateral de la MCF", "Placa volar de la IFP", "Porción terminal del tendón extensor insertada en la falange distal", "Cintilla central del tendón extensor", "Inserción del FDP en la falange distal"],
   "Un golpe en la punta del dedo rompe el extremo del tendón extensor en la falange distal y el paciente no puede extender activamente la IFD. La lesión de la cintilla central produce la deformidad en ojal."))

T("mu-73d28bd6",
  ("What is the main action of piriformis?", ["Adduction of the hip", "Flexion of the knee", "Flexion of the hip", "Lateral rotation of the hip", "Medial rotation of the hip"],
   "Piriformis arises from the anterior surface of the sacrum, passes through the greater sciatic foramen and inserts on the greater trochanter; it laterally rotates the hip and abducts it when flexed."),
  ("Quelle est l'action principale du muscle piriforme ?", ["Adduction de la hanche", "Flexion du genou", "Flexion de la hanche", "Rotation latérale de la hanche", "Rotation médiale de la hanche"],
   "Le piriforme naît de la face antérieure du sacrum, traverse le grand foramen ischiatique et se termine sur le grand trochanter ; il tourne la hanche en dehors et l'abducte quand elle est fléchie."),
  ("Was ist die Hauptwirkung des M. piriformis?", ["Adduktion der Hüfte", "Beugung des Knies", "Beugung der Hüfte", "Außenrotation der Hüfte", "Innenrotation der Hüfte"],
   "Der M. piriformis entspringt an der Vorderfläche des Kreuzbeins, zieht durch das Foramen ischiadicum majus und setzt am Trochanter major an; er rotiert die Hüfte nach außen und abduziert sie in Beugestellung."),
  ("¿Cuál es la acción principal del piriforme?", ["Aducción de la cadera", "Flexión de la rodilla", "Flexión de la cadera", "Rotación externa de la cadera", "Rotación interna de la cadera"],
   "El piriforme nace de la cara anterior del sacro, atraviesa el agujero ciático mayor y se inserta en el trocánter mayor; rota externamente la cadera y la abduce cuando está flexionada."))

T("mu-c21bde83",
  ("What is the order of the deep lateral rotators of the hip from superior to inferior?", ["Obturator internus, piriformis, quadratus femoris, gemellus superior, gemellus inferior", "Piriformis, obturator internus, gemellus superior, gemellus inferior, quadratus femoris", "Quadratus femoris, gemellus inferior, obturator internus, gemellus superior, piriformis", "Gemellus superior, piriformis, gemellus inferior, obturator internus, quadratus femoris", "Piriformis, gemellus superior, obturator internus, gemellus inferior, quadratus femoris"],
   "With gluteus maximus removed, from top to bottom one sees piriformis, gemellus superior, the obturator internus tendon, gemellus inferior and quadratus femoris; obturator externus lies deeper."),
  ("Quel est l'ordre des rotateurs latéraux profonds de la hanche de haut en bas ?", ["Obturateur interne, piriforme, carré fémoral, jumeau supérieur, jumeau inférieur", "Piriforme, obturateur interne, jumeau supérieur, jumeau inférieur, carré fémoral", "Carré fémoral, jumeau inférieur, obturateur interne, jumeau supérieur, piriforme", "Jumeau supérieur, piriforme, jumeau inférieur, obturateur interne, carré fémoral", "Piriforme, jumeau supérieur, obturateur interne, jumeau inférieur, carré fémoral"],
   "Après ablation du grand glutéal, on voit de haut en bas le piriforme, le jumeau supérieur, le tendon de l'obturateur interne, le jumeau inférieur et le carré fémoral ; l'obturateur externe est plus profond."),
  ("Wie ist die Reihenfolge der tiefen Außenrotatoren der Hüfte von oben nach unten?", ["Obturatorius internus, Piriformis, Quadratus femoris, Gemellus superior, Gemellus inferior", "Piriformis, Obturatorius internus, Gemellus superior, Gemellus inferior, Quadratus femoris", "Quadratus femoris, Gemellus inferior, Obturatorius internus, Gemellus superior, Piriformis", "Gemellus superior, Piriformis, Gemellus inferior, Obturatorius internus, Quadratus femoris", "Piriformis, Gemellus superior, Obturatorius internus, Gemellus inferior, Quadratus femoris"],
   "Nach Entfernen des M. gluteus maximus sieht man von oben nach unten M. piriformis, M. gemellus superior, die Sehne des M. obturatorius internus, M. gemellus inferior und M. quadratus femoris; der M. obturatorius externus liegt tiefer."),
  ("¿Cuál es el orden de los rotadores externos profundos de la cadera de arriba abajo?", ["Obturador interno, piriforme, cuadrado femoral, gemelo superior, gemelo inferior", "Piriforme, obturador interno, gemelo superior, gemelo inferior, cuadrado femoral", "Cuadrado femoral, gemelo inferior, obturador interno, gemelo superior, piriforme", "Gemelo superior, piriforme, gemelo inferior, obturador interno, cuadrado femoral", "Piriforme, gemelo superior, obturador interno, gemelo inferior, cuadrado femoral"],
   "Retirado el glúteo mayor se ven de arriba abajo el piriforme, el gemelo superior, el tendón del obturador interno, el gemelo inferior y el cuadrado femoral; el obturador externo está más profundo."))

T("mu-3710da53",
  ("What are the actions of sartorius?", ["Only extends the knee", "Adducts and medially rotates the hip", "Only flexes the hip", "Flexes, abducts and laterally rotates the hip; flexes the knee", "Extends the hip and extends the knee"],
   "Sartorius performs all the movements of sitting cross-legged: hip flexion, abduction and lateral rotation, and knee flexion. It is supplied by the femoral nerve."),
  ("Quelles sont les actions du sartorius ?", ["Il étend seulement le genou", "Il adducte et tourne la hanche en dedans", "Il fléchit seulement la hanche", "Il fléchit, abducte et tourne la hanche en dehors ; il fléchit le genou", "Il étend la hanche et le genou"],
   "Le sartorius réalise tous les mouvements de la position du tailleur : flexion, abduction et rotation latérale de la hanche, et flexion du genou. Il est innervé par le nerf fémoral."),
  ("Welche Bewegungen führt der M. sartorius aus?", ["Streckt nur das Knie", "Adduziert und innenrotiert die Hüfte", "Beugt nur die Hüfte", "Beugt, abduziert und außenrotiert die Hüfte; beugt das Knie", "Streckt Hüfte und Knie"],
   "Der M. sartorius führt alle Bewegungen des Schneidersitzes aus: Hüftbeugung, -abduktion und -außenrotation sowie Kniebeugung. Er wird vom N. femoralis innerviert."),
  ("¿Cuáles son las acciones del sartorio?", ["Solo extiende la rodilla", "Aduce y rota internamente la cadera", "Solo flexiona la cadera", "Flexiona, abduce y rota externamente la cadera; flexiona la rodilla", "Extiende la cadera y la rodilla"],
   "El sartorio realiza todos los movimientos de sentarse con las piernas cruzadas: flexión, abducción y rotación externa de la cadera y flexión de la rodilla. Lo inerva el nervio femoral."))

T("mu-488b8c00",
  ("Which muscle forms the medial border of the femoral triangle?", ["Iliopsoas", "Adductor longus", "Pectineus", "Gracilis", "Sartorius"],
   "The femoral triangle is bounded above by the inguinal ligament, laterally by sartorius and medially by the medial border of adductor longus. Its floor is formed by iliopsoas, pectineus and adductor longus."),
  ("Quel muscle forme le bord médial du triangle fémoral ?", ["Muscle ilio-psoas", "Muscle long adducteur", "Muscle pectiné", "Muscle gracile", "Muscle sartorius"],
   "Le triangle fémoral est limité en haut par le ligament inguinal, en dehors par le sartorius et en dedans par le bord médial du long adducteur. Son plancher est formé par l'ilio-psoas, le pectiné et le long adducteur."),
  ("Welcher Muskel bildet die mediale Grenze des Trigonum femorale?", ["M. iliopsoas", "M. adductor longus", "M. pectineus", "M. gracilis", "M. sartorius"],
   "Das Trigonum femorale wird oben vom Leistenband, lateral vom M. sartorius und medial vom Innenrand des M. adductor longus begrenzt. Den Boden bilden M. iliopsoas, M. pectineus und M. adductor longus."),
  ("¿Qué músculo forma el borde medial del triángulo femoral?", ["Músculo iliopsoas", "Músculo aductor largo", "Músculo pectíneo", "Músculo grácil", "Músculo sartorio"],
   "El triángulo femoral está limitado arriba por el ligamento inguinal, lateralmente por el sartorio y medialmente por el borde medial del aductor largo. Su suelo lo forman el iliopsoas, el pectíneo y el aductor largo."))

T("mu-0aeb820d",
  ("Which spinal segment does the patellar (knee) reflex mainly test?", ["S1", "L5", "L2", "S2", "L4"],
   "The patellar reflex runs through the femoral nerve and segments L2–L4, especially L4. The Achilles reflex tests S1, the biceps reflex C5 and the triceps reflex C7."),
  ("Quel segment médullaire le réflexe rotulien teste-t-il principalement ?", ["S1", "L5", "L2", "S2", "L4"],
   "Le réflexe rotulien passe par le nerf fémoral et les segments L2–L4, surtout L4. Le réflexe achilléen teste S1, le bicipital C5 et le tricipital C7."),
  ("Welches Rückenmarkssegment prüft der Patellarsehnenreflex vor allem?", ["S1", "L5", "L2", "S2", "L4"],
   "Der Patellarsehnenreflex verläuft über den N. femoralis und die Segmente L2–L4, vor allem L4. Der Achillessehnenreflex prüft S1, der Bizepsreflex C5, der Trizepsreflex C7."),
  ("¿Qué segmento medular explora principalmente el reflejo rotuliano?", ["S1", "L5", "L2", "S2", "L4"],
   "El reflejo rotuliano pasa por el nervio femoral y los segmentos L2–L4, sobre todo L4. El aquíleo explora S1, el bicipital C5 y el tricipital C7."))
