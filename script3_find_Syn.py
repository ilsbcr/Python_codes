import re

def extract_bracketed_numbers(text):
    """Extracts numbers enclosed in square brackets from the given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        list: A list containing the extracted numbers as strings.
    """

    pattern = r"\[(\d+)\]"  # Regex pattern to match digits within brackets
    matches = re.findall(pattern, text)
    return matches

# Get user input
#user_text = input("Enter your text: ")

user_text = """Table Des Matières

Chapitre 3 : Conception de ’architecture
1.1. Introduction	2
1.2. Notion de la Cyber Sécurité	2
1.2.1. Défis de la Cyber Sécurité	3
a. Protection des Données Sensibles	3
b. Protection de la Réputation	3
c. Continuité des Activités (Business Continuity)	4
d. Respect de la Réglementation	4
e. Innovation et Développement des Technologies au Quotidien	4
f. Compétences et Sensibilisation	5
1.3. Catégories d’Attaques et Identification des Vulnérabilités	5
1.3.1. Vulnérabilités de la Sécurité Informatique	5
a. Vulnérabilité Logicielle	6
b. Vulnérabilité Matérielle	7
1.3.2. Catégories d’Attaques	7
a. Injection SQL	7
b. Botnet	8
c. Déni de Service (DoS)	8
d. Force Brute (Brute Force)	8
e. Cross-Site Scripting (XSS)	8
1.4. Mécanismes de Protection des Systèmes Informatiques	9
1.4.1. Contrôle d’Accès au Niveau de l’Hôte	9
1.4.2. Contrôle d’Accès au Niveau du Réseau	9
1.4.3. Autre Contrôle d’Accès	10
1.5. Systèmes de Détection d’Intrusions (Ids)	11
1.5.1. Principes et Généralités d’un IDS	11
1.5.2. Classifications des IDSs	11
a. Selon l'Approche de Détection	11
b. Selon l'Emplacement Surveillé	13
c. Selon l'Architecture	15
d. Selon la Fréquence d’Utilisation	16
e. Selon la Réponse aux Evénements	17
f. Selon la Source de Données	18
1.5.3. Limitations des IDSs Traditionnels	19
1.7. Conclusion	20

	

CHAPITRE  1 
   PRINCIPES    FONDAMENTAUX DE  
      LA    SÉCURITÉ    INFORMATIQUE
_________________________
Introduction
La conception de l'architecture en matière de cybersécurité est un processus crucial pour garantir la protection des systèmes informatiques et des données sensibles. Dans ce chapitre, nous aborderons les différents aspects de la cyber-sécurité, en mettant l'accent sur les défis auxquels font face les organisations, les différentes catégories d'attaques et de vulnérabilités, ainsi que les mesures de protection des systèmes informatiques contre ces activités malveillantes. En particulier, nous explorerons également les principes et les classifications des systèmes de détection d'intrusions (IDS), ainsi que leurs limitations.

Notion de la Cyber Sécurité
À l’ère numérique actuelle, le recours croissant aux technologies de l’information et des communications (TICs) a rendu le monde plus interconnecté, efficace et interactif. Cependant, cette dépendance à l’égard des systèmes de TIC a créé des faiblesses et des menaces qui font de la cyber-sécurité une priorité mondiale [36]. Car englobe la protection des actifs numériques, des systèmes et des réseaux contre l’accès illégal, l’abus, la perturbation ou la destruction des actifs.
 Cette discipline avec ces multiples facettes met en évidence une interaction complexe de considérations techniques, juridiques et éthiques. Elle vise à équilibrer la protection de la valeur essentielle avec les défis en constante évolution des cyber-menaces, qui vont des virus informatiques de base aux types sophistiqués d’activités de cybercriminalité et de cyber-espionnage. Par conséquent, la cyber-sécurité comprend un ensemble complet de techniques, de processus et de pratiques conçus pour protéger la triade « DIC » [36]. Cette protection s’applique aux données au repos (stockées) et en transit (transmises via les réseaux), tout en assurant l’authentification et la non-répudiation des utilisateurs et de leurs actions. En mettant en œuvre ces mesures, la cyber-sécurité s’efforce d’atténuer les risques associés à la cybercriminalité, aux cyberattaques et à d’autres activités malveillantes susceptibles de compromettre les données, l’infrastructure ou les opérations numériques [94].
Défis de la Cyber Sécurité
Les défis de la sécurité de l’information ne cessent de croître. Les cyber-attaques peuvent causer des dommages aux entreprises, aux gouvernements et aux particuliers [36]. Ils peuvent entraîner des pertes financières, des vols de données, des atteintes à la réputation et des perturbations cruciales de l’infrastructure. Certains des défis importants en matière de cyber-sécurité (sans vouloir être exhaustif) sont mentionnés ci-dessous.

Protection des Données Sensibles
Les systèmes informatiques stockent et manipulent des données sensibles, telles que des informations personnelles, des données financières ou des secrets commerciaux. Ces systèmes font face à des défis quotidiens pour protéger ces données contre le vol, la corruption ou la destruction [36].

Protection de la Réputation
L’ère numérique a transformé le fonctionnement des organisations et des entreprises, mais elle a amplifié les risques pour leur réputation. En plus de protéger des données et des systèmes importants, la défense de leur image publique contre les cyber-menaces est devenue un défi critique et distinct. L’interconnexion des entreprises modernes crée de nombreux points d’attaque, érodant la confiance. Les difficultés à attribuer les attaques et à équilibrer la sécurité avec la confidentialité ajoutent à la complexité. De plus, l’erreur humaine demeure une menace, et la rapidité du flux d’information peut rapidement transformer un petit problème en une crise majeure de réputation.
Continuité des Activités (Business Continuity)
La dépendance constante des entreprises à l’égard de leurs systèmes de TI crée un besoin critique en matière de planification de la continuité des activités. Une cyber-attaque peut perturber ou interrompre les activités des entreprises, elle peut également entraîner d’importantes pertes financières et ruiner la réputation [37]. qui crée un défi pour s’assurer que ces informations et services sont toujours disponibles.

Respect de la Réglementation
La cyber-sécurité présente divers défis en termes de conformité réglementaire, de protection des données et de normes industrielles. Des réglementations telles que le Règlement général sur la protection des données (RGPD) pour la confidentialité des données personnelles et des normes spécifiques à l’industrie créent un fardeau exigeant pour les mesures de sécurité. Il peut être complexe d’établir un équilibre entre des pratiques de sécurité robustes et la collecte, le stockage et le traitement conformes des données sensibles, ce qui nécessite une gestion et une expertise techniques minutieuses . De plus, la sécurisation des systèmes de paiement, un aspect essentiel du commerce électronique et des institutions financières, exige une stricte conformité aux normes de sécurité spécifiques de l’industrie pour protéger les transactions et prévenir les opérations frauduleuses [36].
Ces défis de conformité nécessitent non seulement de comprendre des réglementations et des normes complexes, mais aussi de mettre en œuvre des solutions techniques qui garantissent à la fois le respect de la loi et une sécurité efficace.

Innovation et Développement des Technologies au Quotidien
L’innovation et le développement quotidiens des technologies sont une arme à double tranchant pour la cyber-sécurité. Bien qu’elle ouvre la porte à des avancées incroyables, elle crée également un paysage de menaces en constante évolution. Les cybercriminels savent exploiter les nouvelles vulnérabilités pour forcer les professionnels de la cyber-sécurité à rester en veille. Cette course aux armements en cours exige une adaptation continue, les chercheurs développant de nouvelles mesures de sécurité alors même que les attaquants conçoivent des outils toujours plus sophistiqués.



Compétences et Sensibilisation
Le besoin de personnel qualifié en cyber-sécurité et l’obligation de sensibilisation des utilisateurs aux risques et à la réglementation, les professionnels de la cyber-sécurité doivent également développer des compétences au-delà de l’expertise technique, y compris la créativité, l’innovation et les compétences non techniques, traiter efficacement les risques de cybersécurité [36].

  Pour relever ces défis, les organisations doivent investir dans une sécurité robuste, cultiver une culture de sensibilisation à la sécurité et suivre les mises à jour et les développements en matière de cyber-sécurité. En prenant ces mesures, les entreprises peuvent renforcer leur résilience, atténuer les risques et protéger leur réputation à l’ère de la vulnérabilité numérique.

Catégories d’Attaques et Identification des Vulnérabilités
Tout ordinateur ou appareil, est potentiellement vulnérable aux attaques. Une attaque informatique est une suite d’actions effectuées par un logiciel malveillant exploitant une vulnérabilité pour obtenir un contrôle total ou partiel du système victime afin de compromettre les propriétés de sa sécurité informatique. Les attaques devraient être caractérisées par les méthodes d’attaque, les vulnérabilités exploitées et l’opportunité [95]. Dans ce qui suit, nous présentons les vulnérabilités existantes et leurs éventuelles attaques.

Vulnérabilités de la Sécurité Informatique
La vulnérabilité est une faille connue ou suspectée dans la conception du matériel ou du logiciel qui expose le système à la pénétration ou ses informations à la divulgation accidentelle [96], Une vulnérabilité peut aussi être appelée : "erreur", "défaut" ou "faiblesse".
L’attaquant peut obtenir une extra autorité du système informatique en utilisant sa vulnérabilité, puis casser la sécurité de ce système en accédant ou améliorant l'autorité d'accès. La vulnérabilité comprend tous les facteurs qui peuvent conduire à menacer ou à compromettre la sécurité du système informatique (l’intégrité, la convivialité, le secret, la fiabilité ou la contrôlabilité) [97].

Généralement, la vulnérabilité elle-même ne peut pas causer des dommages à la sécurité du système, mais l'attaquant peut utiliser une vulnérabilité et effectuer différentes actions malveillantes dans un système informatique. Ainsi, chaque jour, nous apprenons que des nouvelles vulnérabilités sont découvertes  dans les programmes et réseaux informatiques, les rapports de sécurité publient des chiffres inquiétants et rapportent que les nombres de failles sont en augmentation continue.

Dans la littérature plusieurs classifications de la vulnérabilité ont été proposées afin de mieux caractériser ce domaine de la sécurité informatique. Dans ce qui suit, nous en présentons les deux principaux types qui sont : la vulnérabilité logicielle et la vulnérabilité matérielle.

Vulnérabilité Logicielle
Les logiciels constituent un premier niveau d’abstraction à partir duquel un attaquant peut mettre en défaut la sécurité d’un système informatique. Dans ce contexte, le terme système logiciel doit être pris dans son sens le plus général. Il désigne tous types de logiciels dans un système informatique, couvrant aussi bien les programmes d’application, le système d’exploitation et son noyau [98].

La plupart des systèmes logiciels contiennent des vulnérabilités, c’est-à-dire des fautes de conception, de programmation ou de configuration [100]. Un attaquant peut alors exploiter ces vulnérabilités comme autant de vecteurs d’attaque pour effectuer différentes actions malveillantes dans un système informatique. Une attaque, à ce niveau d’abstraction, repose sur l’exploitation d’une fonctionnalité logicielle vulnérable à des fins malveillantes.

La plupart des vulnérabilités identifiées par analyse sont associées à une manière incorrecte de traiter les entrées fournies par un utilisateur du système, si ces entrées ne sont pas traitées correctement avant de les utiliser à l'intérieur du programme, elles peuvent générer un comportement inattendu du système [99]. Par exemple, certaines vulnérabilités connues et fréquentes sont discutées dans la section des catégories d’attaques suivantes.
 
Vulnérabilité Matérielle
De la même façon que les systèmes logiciels, les systèmes matériels peuvent contenir des fonctionnalités matérielles vulnérables. Toutefois, celles-ci sont moins courantes que les vulnérabilités logicielles et dans la majorité des cas, elles ne sont pas exploitables.
Comme exemple, le bogue matériel découvert dans les processeurs Pentium en décembre 1997 aurait pu être utilisé pour perpétrer des attaques contre la disponibilité. En effet, lorsqu’un processeur Pentium exécutait la séquence d’instructions lock cmpxchg8b eax (correspondant à la séquence d’octets 0xF00FC7C8), celui-ci se bloquait aussitôt. L’instruction cmpxchg8b eax n’étant pas valide, l’exécution de celle-ci déclenche une exception matérielle. Une personne malintentionnée pourrait profiter de ce bogue matériel pour provoquer des dénis de service simplement en exécutant un programme contenant cette séquence d’instructions [98].

Catégories d’Attaques
Les attaques de sécurité informatique sont devenues monnaie courante dans le paysage numérique actuel, avec des méthodes toujours plus sophistiquées utilisées par les cybercriminels pour compromettre la sécurité des systèmes et des données. Dans cette section, nous allons nous concentrer sur les attaques les plus connues, en expliquant leurs mécanismes, ainsi que leurs impacts sur la sécurité des systèmes informatiques.

Injection SQL
Les injections SQL représentent une faille de sécurité grave dans les applications Web qui utilisent des bases de données SQL. Elles surviennent lorsque les entrées des utilisateurs ne sont pas correctement nettoyées avant d'être utilisées pour générer des requêtes SQL, permettant aux attaquants d'injecter du code SQL malveillant et d'obtenir un accès illégal à la base de données [36]. Pour prévenir les injections SQL, les développeurs doivent utiliser des instructions préparées ou des requêtes paramétrées pour séparer le code SQL des données utilisateur, réduisant ainsi le risque de compromission du système et soulignant l'importance des pratiques de codage sécurisé et de la formation des développeurs en matière de sécurité.



Botnet
Une attaque de botnet implique un réseau d'appareils compromis contrôlés par un cybercriminel pour mener des activités malveillantes, telles que des attaques DDoS. Ces attaques posent des menaces importantes en raison de leur nature dynamique et flexible, rendant les méthodes de détection traditionnelles inefficaces contre l'évolution des tactiques de botnet. Les vulnérabilités associées aux attaques de botnets incluent la possibilité de mettre à jour les bots et de changer les codes pour échapper à la détection, créant ainsi des botnets indétectables pouvant être constitués de millions de machines infectées[38].

Déni de Service (DoS)
Les attaques par déni de service visent à rendre un système ou un réseau indisponible pour les utilisateurs en le submergeant de trafic ou en épuisant ses ressources informatiques. Les attaques distribuées par déni de service (DDoS) exploitent des botnets, des réseaux d'appareils compromis, pour amplifier l'attaque. Mirai, l'un des plus grands botnets pour les attaques DDoS, a été construit à partir d'appareils IoT non sécurisés comme les routeurs et les caméras IP. Les attaques d'amplification exploitent des tiers comme les serveurs DNS pour augmenter le trafic d'attaque [36]. Les attaques DoS persistent en raison d'externalités, où les responsables de la sécurité ne sont pas incités à traiter les vulnérabilités, et peuvent être utilisées pour extorquer des rançons.

Force Brute (Brute Force)
Une attaque par force brute est un type de cyber-attaque visant un large éventail d'appareils et de systèmes d'authentification. L'attaquant tente de deviner un mot de passe ou une clé de chiffrement en essayant toutes les combinaisons possibles à l'aide d'outils et de techniques logiciels pour automatiser le processus. Cette attaque est efficace contre les mots de passe faibles ou les clés de cryptage facilement devinables.

Cross-Site Scripting (XSS)
Les attaques de cross-site scripting (XSS) consistent à injecter des scripts malveillants dans un site Web, qui sont ensuite exécutés par le navigateur de l'utilisateur, entraînant potentiellement un accès non autorisé à des données sensibles ou une compromission du système. Les vulnérabilités associées aux attaques XSS résultent souvent d'une validation insuffisante des entrées utilisateur ou d'un échappement insuffisant de la sortie, permettant aux attaquants d'injecter des scripts malveillants.

Mécanismes de Protection des Systèmes Informatiques
La protection des systèmes informatiques contre les cyber-menaces est un objectif essentiel à l’ère numérique d’aujourd’hui. La cyber-sécurité est d’une importance capitale pour la protection des informations et des données fournies par les clients, en particulier dans le secteur bancaire où les technologies et les appareils numériques sont de plus en plus utilisés [39]. L’importance de la sécurité numérique est une préoccupation primordiale pour tous les individus, et les mesures à prendre après l’incident sont cruciales pour réduire les dommages, rétablir le contrôle et identifier les acteurs d’attaque impliqués [40]. Il est essentiel de comprendre les mécanismes de protection des systèmes informatiques pour prévenir les attaques et minimiser le risque de cyber-menaces pour les fournisseurs et les clients .
Contrôle d’Accès au Niveau de l’Hôte
Le contrôle d’accès au niveau de l’hôte est un mécanisme de protection des systèmes informatiques. Il s’agit de réguler l’accès à des hôtes ou appareils individuels au sein d’un réseau. Diverses méthodologies peuvent être utilisées pour mettre en œuvre le contrôle d’accès, y compris les mots de passe, la vérification biométrique et les cartes à puce. En outre, des pare-feu et des systèmes de détection d’intrusion peuvent être utilisés pour renforcer le contrôle d’accès, empêchant ainsi tout accès non autorisé aux hôtes [41].
Contrôle d’Accès au Niveau du Réseau
Le contrôle d’accès au niveau du réseau est une autre approche importante pour protéger les systèmes informatiques en limitant l’accès au réseau dans son ensemble. Les experts mettent en œuvre des contrôles d’accès au réseau en utilisant des technologies comme les pare-feu, les réseaux privés virtuels (VPN), les serveurs proxy, ainsi que les systèmes de détection d’intrusions. De plus, la segmentation du réseau en segments plus petits, chacun avec son propre ensemble de règles d’accès, peut être une bonne option pour améliorer la sécurité du réseau [42].


Autre Contrôle d’Accès
En plus du contrôle d’accès au niveau de l’hôte et du réseau, des mesures de sécurité  modernes telles que le contrôle d’accès dynamique, basé sur les rôles, basé sur les attributs, discrétionnaire et obligatoire offrent plus de flexibilité, d’évolutivité et de capacités de gestion d’accès contextuel.
D’autres mécanismes de sécurité englobent l’utilisation du chiffrement pour protéger les données en transit et au repos. Le chiffrement implique la transformation de données en clair en texte chiffré indéchiffrable. De ce fait , même si les attaquants accèdent au système, ils auront des difficultés à accéder aux données. La mise en œuvre de protocoles sécurisés tels que Secure Sockets Layer (SSL) et Transport Layer Security (TLS), qui fournissent un cryptage et une authentification de bout en bout, peut être un excellent moyen d’améliorer le contrôle d’accès [43].
Les mesures de sécurité que les utilisateurs doivent appliquer dans une politique de sécurité et mettre en œuvre lors de l'utilisation d'un système informatique, font partie de l’approche préventive. Il est en fait presque impossible d'offrir une sécurité totalement sûre contre chaque attaque potentielle en raison de la quantité croissante et de la complexité des attaques ainsi que de l'évolution des systèmes informatiques. La stratégie détective, qui est le deuxième niveau de protection, doit être mise en œuvre par une politique de sécurité afin de répondre à cela.

L'utilisation de l'approche détective facilite l'identification rapide des intrusions potentielles dans un système informatique. Cela permet de réagir rapidement et d'empêcher toute interférence avec le fonctionnement normal de celui-ci. L'approche détective est l'une des mesures de sécurité distinctes qui constituent la détection d'intrusion. Le processus d'identification de l'activité non autorisée provenant ou se dirigeant vers un système informatique par analyse comportementale est appelé détection d'intrusion.





Systèmes de Détection d’Intrusions (IDS)
Une intrusion est fondamentalement toute sorte d'activité illégale qui est effectuée par des attaquants, utilisant le système informatique sans autorisation (intrusion externe) ou des individus qui ont un accès légitime au système mais qui abusent de leurs privilèges (intrusion interne), pour endommager les ressources réseau ou les nœuds de capteurs. Un IDS est un mécanisme permettant de détecter de telles activités illégales ou malveillantes. Il est considéré comme une deuxième ligne de défense capable de protéger le réseau contre les intrus [122]. C’est un ensemble de composants logiciels et matériels qui permet d’écouter le trafic réseau de façon furtive dans le but de détecter des activités anormales qui pourraient être assimilées à des intrusions.
Les systèmes de détection d’intrusion  jouent un rôle central dans la protection des systèmes contre les accès illicites et les actions malveillantes. Les principes fondamentaux et les aspects généraux des IDS sont ancrés dans leur capacité à identifier les menaces à la sécurité et à y réagir en temps réel [44] [45]. Les IDS sont conçus pour examiner le trafic réseau et les opérations du système pour détecter les indications d’accès non autorisé, d’utilisation abusive ou d’autres activités malveillantes.
Principes et Généralités d’un IDS
Un système de détection d’intrusion est tout matériel ou logiciel chargé de surveiller un actif contre toute effraction qui permet de compromettre les services de base de la sécurité des informations [101]. Cependant,  un IDS peut être défini comme un mécanisme de surveillance pour détecter les menaces internes ou externes qui affectent le bon fonctionnement du système. La principale fonction de l'IDS est la surveillance des activités des utilisateurs et le comportement du réseau sur différentes couches [123]. La précision de la détection d'intrusion est généralement mesurée en termes d'erreurs positives (fausses alarmes) et d'erreurs négatives (attaques non détectées). La performance d'un IDS augmente en augmentant le taux de détection précis tout en minimisant les erreurs positives et négatives. Un IDS se compose principalement de trois parties essentielles à savoir : (1) Le module de surveillance (Monitoring), chargé principalement de la surveillance du trafic réseau, des évènements internes au sein du réseau, ainsi que l'utilisation des ressources. (2)  Le module d'analyse et de détection, considéré comme le noyau de l'IDS qui détermine si le flux d’événements contient ou pas des éléments ou des caractéristiques d’une activité malveillante. Cette décision est prise à partir d'une analyse du comportement et des activités du réseau. Et (3) l'alarme ; Activation de l'alarme en cas d'une détection d'une intrusion.
Classifications des IDSs
Les systèmes de détection d’intrusions sont classés en différentes catégories en fonction de divers critères, notamment leur méthode de détection, leur emplacement dans le réseau, leur fonctionnement et leur mode de déploiement. Chacune de ces catégories offre ses propres avantages et inconvénients. Dans ce qui suit, nous présentons les différentes facettes selon lesquelles un IDS peut être classé.
Selon l'Approche de Détection
Le modèle créé dans l'étape d'analyse est une structure de données qui décrit, par un ensemble de caractéristiques (attributs), un profil donné. A partir de celui-ci, nous distinguons deux types d'approches de détection: l'approche par scénarios.

Approche par scénarios
L'approche par scénarios (appelée aussi, à base de signature/connaissances) effectue l'analyse des événements capturés en comparant ces derniers avec un modèle décrivant les comportements anormaux d'un ensemble d'intrusions connues au préalable. Si une relation subsiste, le système classe l'événement comme étant une intrusion [102].
Ce type d'approche est très efficace pour la détection d'intrusions qui sont déjà décrites dans le modèle de référence. Cependant, l'approche par scénarios est jugée être dépendante du type de système informatique surveillé. De plus, elle présente des limites quant à la détection des nouvelles intrusions qui ne sont pas connues au préalable. Une solution à ce problème réside dans la mise à jour régulière du modèle de référence d'une manière manuelle, chose qui n'est pas facilement réalisable, ou bien d'une manière automatique par le biais des méthodes d'apprentissage supervisé [103]. Cette dernière n'est pas facile aussi car elle nécessite l'utilisation de données d'apprentissage étiquetées manuellement par des experts de sécurité. Malgré ces lacunes, les IDS utilisant l'approche par scénarios sont les plus commercialisés, dû à leur efficacité pour la détection d'intrusions connues avec un minimum de fausses alertes. 



Approche comportementale
A l’opposé de l’approche par scénario, l’approche comportementale (également appelé IDS à base d’anomalies) permet d'analyser des événements capturés par comparaison de ces derniers avec un modèle décrivant les comportements normaux du système surveillé. L’écart par rapport au comportement notoire est appelé anomalie, tandis que le profil est le comportement normal attendu. Ainsi, toute déviation (i.e. dépassement d’un seuil spécifié) par rapport aux comportements normaux définis est considérée comme une intrusion et vice-versa.
L'approche comportementale peut être statique ou dynamique [103]. Elle est statique lorsque le comportement est invariable (e.g. les séquences d'appels systèmes). Elle est dynamique lorsque le comportement est variable. Dans le deuxième type, le comportement dynamique correspond à des profils définissant les activités habituelles des usagers ou l'historique d'utilisation des réseaux et machines.
Ce mécanisme  est apparu comme étant une solution au problème posé par l'approche par scénarios, et qui concerne la détection des attaques nouvelles et imprévues. Elle permet de détecter les intrusions indépendamment du type du système, des vulnérabilités du système, de l'environnement et du type d'intrusions, ce qui permet d'améliorer le taux de détection [104]. Cependant, son inconvénient majeur est l'augmentation du taux des fausses alertes. Cela est dû à la difficulté de définition des comportements normaux et aux changements dynamiques des profils définis dans le modèle. Un autre inconvénient est que ce type d'approche ne permet pas de donner des informations sur l'attaque détectée ce qui rend la tâche ultérieure de diagnostic difficile. 

Note : En fait, une approche supplémentaire  dite à base de spécifications, et dérivée de l’approche comportementale de façon directe [105]. La différence est que les règles sont définies manuellement pour chaque spécification par un expert, ce qui diminue considérablement le taux des faux positifs. De plus, seuls les comportements anormaux sont détectés, au lieu de détecter leur éventuel effet [106].

Selon l'Emplacement Surveillé
Selon la source des données à surveiller, un IDS est classé en trois catégories: IDS machine (ou HIDS: Host-based Intrusion Detection System), IDS réseau (ou NIDS: Network-based Intrusion Detection System) et IDS hybride.
Système de détection basé sur la machine  (HIDS)
Les HIDS visent à surveiller une seule machine (hôte) qui peut être un ordinateur personnel, un smartphone, un serveur ou tout autre équipement informatique. Son rôle consiste à analyser tous les événements de sécurité qui se passent sur cette machine. Il permet de surveiller les menaces qui peuvent affecter un système de plusieurs manières, notamment l’accès et la modification des fichiers système, et l’occupation inutile et permanente des ressources [107].
Les HIDS étaient premièrement introduits en réponse aux concepts de traces d'audit. L'utilisation de fichiers d'audit pour la détection des intrusions attaquant une machine, souffre cependant de plusieurs faiblesses. En particulier, les fichiers d'audit contenant des données brutes ne sont pas facilement réalisables, et souvent difficile à interpréter [108]. A cet effet, les chercheurs ont pensé à l'analyse des appels systèmes générés par le système d'exploitation lors de l'exécution d'un programme. L'hypothèse soutenue dans ce contexte est que seul le programme en cours d'exécution pourra affecter le système et que toute intrusion doit forcément laisser des traces dans les appels systèmes exécutés par le système d'exploitation.

Système de détection basé sur la machine  (NIDS)
Les NIDS visent à surveiller un réseau d'objets informatiques (PCs, équipements d’interconnexion, etc.) en analysant les paquets entrants et sortants du réseau. De plus, ce type d’IDS est destiné à détecter l’intrusion dans les données transmises par le sous-réseau aux utilisateurs rattachés. En d’autres termes, les NIDS permettent également d'analyser les paquets circulant à l'intérieur du réseau surveillé. Ainsi, les données collectées pour les IDSs réseau peuvent être de différents niveaux de granularité.
Généralement, ces systèmes intègrent un module qui facilite la tâche de collecte des paquets à partir du réseau. Les données collectées à partir des NIDS sont de grandeur différente à celle des HIDSs en termes de volume, puisqu’elles sont décrites par un grand nombre d'attributs de différents types [109].

Système de détection hybride (Hybrid IDS)
Les IDS hybrides constituent une hybridation entre les deux types d’IDS (voir les HIDS et les NIDS). Cette hybridation permet aux NIDS d’analyser les paquets circulant dans tout le réseau surveillé alors que chaque HIDS est dédié à surveiller une seule machine dans le réseau et cela en analysant les paquets qui lui sont destinés [110]. D’une façon formelle, Les IDS hybrides contiennent des agents qui jouent le rôle de communication entre HIDS et NIDS. Ces agents peuvent être soit des agents mobiles qui visitent chaque hôte et effectuent le processus de détection, soit des agents centraux qui parcourent l’ensemble du réseau pour détecter les anomalies de trafic.
Pour optimiser le rendement du système, les IDS hybrides sont formés en se basant sur le type de l'approche adoptée par chacun des IDSs qui les constitue. Cela dit, les IDS hybrides adoptent une combinaison entre les deux types d'approches précédemment parlés (voir l’approche par scénario, et l’approche comportementale).
Selon l'Architecture
Un IDS est une combinaison de plusieurs agents (modules) assurant les tâches de l'audit, l'analyse et la réponse aux intrusions. Selon l'organisation fonctionnelle de ces systèmes, un IDS peut avoir l’une des architectures suivantes.

IDS autonome
Chaque agent d’une telle architecture possède son propre moteur de détection d’intrusion,  qui détecte les intrusions pour ce nœud uniquement. Les données collectées par cet agent spécifique sont utilisées pour comparer avec l’activité malveillante lors de la prise de décision. Ce type d’architecture est robuste grâce au fonctionnement indépendant de chaque IDS.  

IDS centralisé
La tâche d'audit est assurée par plusieurs systèmes, responsables de la collecte des données de différentes ressources. Ils représentent les agents de surveillance « Monitoring Agents ». Les données collectées sont envoyées à un seul système central dit « manager », responsable de l'analyse et de la réponse aux intrusions. Ces données sont ensuite analysées, et si une tentative d’intrusion est découverte, elle est bloquée par l’action de l’IDS associé. Les autres IDS ne sont pas impliqués dans cette décision.

IDS distribué (coopératif)
La tâche d'audit est assurée par plusieurs agents de surveillance subordonnés. L'analyse et la réponse aux intrusions sont distribuées entre ces agents et le module central (le manager). Leur fonction est de détecter les intrusions en surveillant les données d’audit locales. De ce fait, l’identification d’une intrusion repose sur la décision collaborative de tous les IDS associés. Un point qui différencie cette architecture de la précédente est que les résultats d’audit sont partagés avec les nœuds voisins. Cela aide à fournir un mécanisme de détection distribué et coopératif pour la résolution des attaques [111]. Ce mécanisme est généralement utilisé dans une situation où un seul IDS n’est pas entièrement sûr de l’occurrence d’une activité intrusive.


Note : À l'origine d’une architecture distribuée, on trouve l’architecture à base d’agents mobiles. Issue du concept distribué, cette variante dispose d’agents avec des logiciels spécialisés et peuvent se déplacer librement aux différents emplacements,  pour visiter chaque nœud du réseau [112]. Tous les nœuds sont censés installer un logiciel agent, et par lequel, ils ont la capacité de corréler les activités suspectes trouvées dans les nœuds surveillés.

IDS hiérarchique
L’architecture hiérarchique  divise le réseau en  clusters (groupes) multicouches où chaque cluster a peu de nœuds (agents)  avec un manager central. Là aussi, la tâche d'audit est assurée par plusieurs agents de surveillance, mais qui travaillent avec différents managers. Les nœuds qui collectent les données à partir d'une machine sont liés à un manager machine « Host Manager ». Les nœuds qui collectent les données à partir du réseau sont liés à un manager réseau « Network Manager ». Chaque manager joue un rôle de premier plan et a plus de responsabilités que les nœuds ordinaires. Un IDS plus sophistiqué est installé sur l’entête du cluster. Des IDS ordinaires et légers sont installés sur les nœuds restants du cluster. 
Cette architecture réduit le risque d’attaques passives telles que les écoutes clandestines. Contrairement à l’architecture distribuée, cette architecture ne nécessite pas de coopération et le surcoût de communication est réduit.
Selon la Fréquence d’Utilisation
La fréquence d'utilisation d'un IDS signifie le nombre de fois que le système est lancé pour analyser les événements capturés. Selon ce critère, nous distinguons deux types de détection ; la détection en temps réel (continue / online) et la détection en batch (périodique/offline).

Détection en temps réel (continue / en ligne)
Dans ce type de système, la détection de l'intrusion doit se faire au moment de sa production. Cela est réalisé en lançant la tâche d'analyse plusieurs fois à intervalles de temps très réduits (e.g. chaque seconde). L'avantage de la détection en permanence est qu'elle permet de détecter l'intrusion rapidement (action immédiate) ce qui l'empêchera de se propager dans le système et causer d'éventuels dégâts, assurant la précision et la rapidité du traitement en même temps [113] [114].

Détection en batch (périodique / hors-ligne)
Dans ce type de système, la tâche d'analyse est lancée périodiquement (e.g. chaque semaine). Ainsi, la détection de l'intrusion ne se fait pas au moment de sa production, ce qui peut mettre le fonctionnement du système face au risque intrusif. L’outil de détection prend une vue d’ensemble du système ou du réseau connecté et l’analyse pour la détection d’intrusion. Si une intrusion est détectée, elle est empêchée de nuire au réseau. D’autre part, si l’intrusion n’est pas détectée, il attend la prochaine période à venir, pour en apercevoir.
La détection en batch peut être utilisée dans des environnements de simulations qui ont pour objectif la modélisation des signatures d'attaques pour la création des bases de signatures. En outre, elle constitue une alternative pour les chercheurs afin d'évaluer leurs systèmes [114].


Selon la Réponse aux Événements
A l'issue de la phase d'analyse, le système doit réagir à l'ensemble des intrusions détectées. Selon que le système déclenche des traitements ou non, nous distinguons deux types de systèmes ; les IDS passifs et les IDS actifs.

IDS actif :
Un IDS actif détecte les menaces dans un système et répond activement en bloquant / prévenant les menaces détectées. Si une attaque apparaît, ce type d’IDS exécute un plan d'actions dans le but d'entraver cette attaque. Le plan d'action peut porter sur l'attaquant du système (supprimer ses outils, supprimer sa plateforme, etc.) ou bien sur le système informatique surveillé lui-même (arrêter les processus affectés par l'attaque, arrêter la connexion réseau, etc.).

IDS passif :
Un IDS passif surveille uniquement le système en silence et ne joue aucun rôle direct dans la prévention de la menace. Si une attaque apparaît, ce type d’IDS ne déclenche aucune action pour bouleverser le plan de cette attaque. Au lieu de cela, il se contente d'envoyer un signal à l'administrateur de sécurité, ou toute autre entité responsable de bloquer la menace [115].
Selon la Source de Données
Les outils de détection d’intrusions ne détectent pas directement les actions intrusives, mais leurs manifestations lors d’interactions avec les entités du système d’informations. Les capteurs observent ces interactions par le biais des sources de données présentées ci-dessous. La source de données utilisée pour détecter les intrusions est une caractéristique essentielle des IDS. On distingue trois catégories de sources : le trafic réseau, les audits système et les audits applicatifs.

Données du système d'exploitation (audit système)
Ce sont les données de trace d'audit produites par le système d'exploitation d'un hôte (audit système). Dans ce cas, les IDS analysent des données d’audit produites par le système d’exploitation des hôtes sur lesquels ils sont installés. Ils sont généralement utilisés dans le cas où la vérification se fait de temps en temps [116]. L'avantage principal des données d'audit du système est la précision d'information. Sur cette base, un système de détection peut réduire le nombre de faux positifs, tout en fournissant des informations détaillées concernant les circonstances de l'attaque [117].
Malheureusement, le volume d’événements généré par les systèmes d’audits peut être considérable, ce qui peut avoir un impact très important sur les performances de la machine surveillée. De plus, la couverture de l’IDS est limitée à un seul hôte, si bien que les administrateurs de sécurité sont amenés à déployer plusieurs sondes, ce qui rend complexe la tâche d’administration [117]. 

Données du flux réseau (audit réseau)
Ce sont les données du trafic réseau, représentées par des flux de paquets. Ces IDSs utilisent les capteurs pour observer le réseau, et collecter les paquets de données qui circulent sur ce réseau afin d'effectuer une analyse pour détecter les intrusions qui se manifestent par une interaction réseau entre l’attaquant et la victime [118].
L’avantage majeur de cette source de données réside avant tout dans sa simplicité d’utilisation vis-à-vis de son environnement [119]. A condition qu’une sonde soit positionnée à un endroit stratégique. Une seule sonde peut surveiller l’activité des utilisateurs dans l’ensemble d’un réseau.



Données applicatives :
La troisième catégorie de source de données est constituée des audits applicatifs. Les données à analyser sont produites directement par une application. (e.g. les fichiers logs générés par: un serveur web, ftp, base de données…etc). Un log d'application peut fournir des informations au profit d'un environnement distribué.
L’avantage de cette approche est que les données produites sont très synthétiques ; elles sont sémantiquement riches et leur volume est modéré, ainsi les IDS basés audit applicatif peuvent fonctionner souvent dans les environnements cryptés. Malheureusement, l’analyse faite par les sondes peut ainsi être plus complexe. Par exemple, une requête HTTP à un serveur web et sa réponse donne lieu à une séquence de plusieurs paquets IP au niveau du réseau, alors qu’elle ne donne lieu qu’à une seule ligne dans le fichier d’audit de ce même serveur web [119] [120].
Limitations des IDSs Traditionnels
Comme tout autre système, les systèmes conventionnels de détection d’intrusion présentent de nombreuses lacunes [121], ce qui les rend moins efficaces dans l’identification et l’atténuation des cyber-menaces contemporaines. D’une part, ils présentent un rapport entre le taux des fausses alarmes élevé et les attaques non détectées. D’autre part,  leur dépendance aux règles et signatures statiques représente un  inconvénient important, par lequel peuvent être contournées sans effort par les cyber-adversaires . En outre, ces IDS traditionnels exigent souvent des ressources, ce qui pose des défis dans leur déploiement et leur gestion au sein d’infrastructures de réseau étendues . L’intégration d’algorithmes d’apprentissage machine a été suggérée comme un remède potentiel à ces problèmes, compte tenu de leur capacité à s’adapter aux menaces dynamiques et à améliorer la précision de détection [46] [47].

Conclusion
Dans ce chapitre, nous avons examiné les différents concepts de base concernant la sécurité informatique. Dans un premier temps, nous avons présenté l’importance de la cyber-sécurité dans l’environnement organisationnel, ainsi que les défis auxquels sont confrontées les organisations. Par la suite, nous avons exposé les problèmes (exprimés en vulnérabilités) et leurs différentes attaques relatives.  Nous avons également étudié les mécanismes de protection des systèmes informatiques, en mettant l'accent sur les principes et les classifications des systèmes de détection d'intrusions (IDS), tout en soulignant leurs limitations. Il est crucial pour toute organisation de prendre en compte ces éléments lors de la conception de son architecture informatique afin de garantir une protection adéquate contre les menaces cybernétiques. A la fin de ce chapitre, nous espérons avoir recueilli des connaissances afin d’entamer notre recherche.
"""
user_text2 ="""CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Table Des Matières
Chapitre 3 : conception de l’architecture
3.1. Introduction .................................................................................................... 2
3.2. Application de l’apprentissage federe a la detection d’intrusions ................. 2
3.3. Architecture proposee .................................................................................... 4
3.3.1. Différents acteurs du système.............................................................. 4
a. Agent d’entrainement ............................................................................. 4
b. Agent d’inférence ................................................................................... 5
3.3.2. Serveur central ..................................................................................... 5
a. présentation. ........................................................................................... 6
b. traitements. ............................................................................................. 6
3.3.3. Emplacement des composants ............................................................. 6
a. serveur central. ....................................................................................... 7
b. agents d'entraînement (réseau externe). ................................................. 7
c. agents d'inférence (réseau interne/externe). ........................................... 7
3.3.4. Données échangées .............................................................................. 7
a. Chiffrement des données ........................................................................ 8
b. Schéma de cheon-kim-kim-song (ckks) ................................................ 9
c. Encapsulation et transfère des données .................................................. 9
3.4. Methodes et techniques employees .............................................................. 10
3.4.1. Model d’apprentissage ...................................................................... 10
3.4.2. Technique d’agrégation ..................................................................... 11
3.4.3. Filtrage d’agents ................................................................................ 11
3.5. Donnees d’apprentissage ............................................................................. 13
3.5.1. Choix des jeux de données ................................................................ 14
3.5.2. Jeu de données cse-cic-ids 2018........................................................ 14
3.5.3. Jeu de données adfa 2019 .................................................................. 15
3.5.4. Défis et préoccupations ..................................................................... 16
a.
Données non identiques et indépendantes (non-iid) ................... 16
b.
Déséquilibrage de classes ........................................................... 16
3.6. Conclusion ................................................................................................... 17
Page 1 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
PARTIE II : DEVELOPPEMENT DU TRAVAIL
CHAPITRE 3
CONCEPTION DE L’ARCHITECTURE
_________________________
3.1. Introduction
Dans ce chapitre, nous proposons une architecture de détection d'intrusions basée sur
l'apprentissage fédéré. Nous détaillons les principaux aspects de notre architecture,
notamment les techniques à utiliser et les jeux de données à adopter. En particulier, nous
mettons en évidence l'importance des choix de ces solutions, en réponse à une revue
approfondie de la littérature existante.
Des approches sophistiquées et adaptatives à nos besoins, telles que l'agrégation et le
filtrage d'agents, seront mises en œuvre pour concevoir une architecture résiliente aux défis
attendus. Nous sélectionnons le modèle d'apprentissage le plus adapté ainsi que des jeux de
données sophistiqués pour garantir la performance et la généralisation de notre architecture.
Enfin, nous discutons des défis et des préoccupations associés à l'apprentissage fédéré
concernant les données, et proposons des solutions pour les surmonter.
3.2. Application de l’Apprentissage Fédéré à la Détection d’Intrusions
L'application de l'apprentissage fédéré à la détection d’intrusions représente une avancée
prometteuse dans le domaine de la sécurité des systèmes informatiques. Plusieurs recherches
mettent en lumière cette approche novatrice [2], qui exploite ses capacités pour entraîner des
modèles de détection d’intrusions de manière distribuée, sans pour autant compromettre la
confidentialité des données des utilisateurs [27][28][29]. En adoptant des solutions de
l’actualité, tel que les techniques à base d’apprentissage profond, nous feront l’objet d’une
étude rigoureuse afin de définir une architecture répartis, permettant ainsi aux dispositifs
terminaux (i.e. hôte ou toute entité possédant les ressources nécessaires) de tirer parti de leurs
données locales pour améliorer la précision de la détection d’intrusions, tout en évitant le
transfert de données sensibles vers le serveur central. La
décentralisation de notre
architecture représente une stratégie viable afin de développer des systèmes de détection
d'intrusions pour les réseaux informatiques. L’architecture proposée est illustrée par la figure
3.1.
Page 2 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
De nombreuses approches proposées [17][26][30], telles que l'utilisation des mécanismes
de filtrage pour la sélection d’agents, et l'adoption d'algorithmes d'agrégation efficaces,
représentent des pistes de recherche importantes que nous avons explorées pour surmonter les
défis1 liés à l’architecture décentralisée [12]. Dans notre quête pour améliorer notre
architecture, nous nous sommes penchés sur diverses stratégies et techniques, allant de la
répartition des agents, jusqu'à l’inférence finale. Celles-ci revêtent une importance cruciale
dans le cadre de notre étude de manière à optimiser notre solution.
Les IDSs basés sur l'apprentissage centralisé ne fonctionnent pas bien sur les données
inconnues. Bien que les algorithmes d'apprentissage obtiennent des résultats de haute
précision sur les ensembles de test, ils ont une faible précision de détection sur les données
inconnues [1]. Cependant, définir une architecture nous mène à identifier les suivantes
questions :





Quelle structure du paradigme à adopté ?
Comment positionner les différents composants ?
Que faire pour surmonter les défis de sécurité exigés (type altération et interception) ?
Quelle est le modèle d’apprentissage et choix du jeu de données ?
Qu’en est-il de la scalabilité ?
Figure 3.1 : Architecture décentralisé proposée (apprentissage fédéré)
1
Défis consistant en l’efficacité du système et hétérogénéité des données, qui entravent le développement de
l’apprentissage fédéré.
Page 3 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.3. Architecture Proposée
En effet, le choix de notre architecture se justifie par des raisons et des besoins de
souplesse et d’adaptabilité. Notre architecture est indépendante de toute plateforme matérielle
et logicielle (hétérogénéité). Cependant, il est possible d’ajouter et de retirer des stations
clientes2 ainsi que de faire évoluer le serveur lui-même, tout en gardant la même architecture
de base (redimensionnement). De plus, les données du serveur sont gérées de façon
centralisée, les clients restent donc individuels et indépendants de l’entité centrale (intégrité).
Pour notre architecture, nous avons adopté le modèle cross-silos (inter-organisationnel)
avec des données d'entraînement diversifiées. En intégrant des données provenant de
différentes sources, le modèle cross-silos à base d'apprentissage vertical nous permet
d'enrichir la diversité du système, et ainsi de conduire à un modèle global plus robuste et
généralisable. Ce choix fait de notre architecture une solution envisageable.
3.3.1. Différents Acteurs du Système
L’architecture que nous avons proposée consiste à mettre en place deux types d'agents
distincts : un dédié à la partie d'entraînement, lequel on fera appel pour générer/produire un
modèle local, et un autre pour la partie d'inférence, entité externe qui utilise le modèle global.
Ce découplage d’exécutions permet de diviser une seule entité cliente en deux parties
fonctionnelles différentes3, assurant ainsi une séparation claire des procédures, une haute
fiabilité de sécurité, réduction de la charge du traitement et une meilleure gestion des trafics
qui leurs sont associés.
a. Agent d’Entrainement
En utilisant un modèle à base de réseaux de neurones profond, chaque dispositif pourra
effectuer un entraînement local sur une partie des données qui lui est propre. Les mise à jours
du modèle local sont ensuit communiquées au serveur central pour but d’agrégation. Une fois
le modèle global transmis à l'agent d’entrainement, celui-ci procédera les mêmes étapes à
nouveau pour l'itération suivante, tenant compte du nouveau modèle.
2
Un cliente fait référence à un agent fonctionnel, traité par le serveur individuellement des autres.
Dans les résultats ultérieurs, on notera par Entité d’entrainement ; la partie productif du modèle, et Entité
d’inférence ; la partie consommatrice du modèle.
3
Page 4 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
b. Agent d’Inférence
A la fin de chaque cycle d’apprentissage, le serveur transmit le modèle global à tous les
agents associés, y-compris l’agent d’inférence. C’est alors à ce dernier de faire preuve
d'efficacité en réalisant des prédictions sur de nouvelles données. En s'appuyant sur le modèle
mis à jour, l'agent d'inférence contribue à identifier rapidement les tentatives d’intrusions
potentielles tout en gardant l’abstraction du modèle globale.
En adoptant une telle structure, nous favorisons ainsi la tolérance aux pannes issues des
points de défaillance uniques, évitant ainsi la nécessité de dépendre entièrement d'un seul
composant pour le bon fonctionnement du système.
3.3.2. Serveur Central
Dans le cadre de notre architecture, où la mise en place d'un serveur soit essentielle, nous
avons conçu un serveur central ayant les ressources nécessaires, et doté d’une capacité de
traitement raisonnable. Celui-ci est responsable de l'agrégation et de la sélection des agents
tout au long du processus d'apprentissage. Son rôle consiste à coordonner les échanges
d’informations entre les différents agents.
Au niveau du serveur, nous avons choisi d'opter pour une approche en deux niveaux (2-
tier) afin d'assurer la scalabilité du système, en termes de taux de traitement. Ceci fait de cette
stratégie une solution idéale pour un rendement optimal des performances. Cependant, le
serveur est constitué de deux parties collaboratives4, désignées par ; la présentation et
logique de traitements. La figure 3.2 représente le modèle employé.
Figure 3.2 : Modèle Gartner Group
4
Considérant la classification de Gartner Group, nous avons choisie d’omettre la partie gestion des données
puisque le serveur n’est pas doté de données confidentielles aux usagés.
Page 5 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
 Présentation : Une interface prise en charge par le serveur central. Cette organisation
présente l'avantage de faire des traitements d’encapsulation-décapsulation sur les données
transmis depuis et vers les clients. Cela compris ; des prétraitements (et éventuellement post-
traitements) sur des données reçues (resp. envoyées aux clients associés).
 Traitements : Le serveur est responsable de deux parts de traitements ; la partie de
filtrage des clients pertinents suivant un certain critère de sélection, et l’agrégation des
données soumis par ces clients, pour en former un modèle global. Ce traitement peut
nécessiter des ressources considérablement importantes, relatives au nombre de clients
auxquels le serveur fera partie.
3.3.3. Emplacement des Composants
Dans le paradigme « coss-silos », où les agents d'entrainement appartiennent à une entité
externe (par ex : une autre entreprise), une architecture en DMZ devrait être ajustée pour
accommoder ce scénario. Le principal objectif de cette DMZ réside dans la garantie de la
sécurité, tout en facilitant la communication entre les composants internes et externes. Les
différents composants sont positionnés de manière suivant la figure 3.3.
Figure 3.3 : Architecture en DMZ
Page 6 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
 Serveur Central : Le serveur, qui coordonne la communication entre le réseau interne de
du système (agents d'inférence) et le réseau externe (agents d’entrainement appartenant à des
entités externes), doit résider dans la DMZ. Il sert de passerelle sécurisée pour la
communication entre les composants internes et externes.
 Agents d'Entraînement (Réseau Externe) : Les agents d'entraînement, chargés de
générer des modèles locaux et opérant dans différents emplacements, restent donc dans le
réseau externe. Ils manipulent des données sensibles pour chaque emplacement lors de la
phase d'entraînement, et donc ne sont pas directement exposés à une entité particulière.
 Agents d'Inférence (Réseau Interne/Externe) : Les agents d'inférence, qui peuvent
appartenir à des entités externes, opèrent en dehors de la DMZ dans le réseau externe. Ces
entités peuvent être d'autres entreprises ou systèmes qui utilisent le modèle global à distance
pour des tâches d'inférence. Ils peuvent également faire partie du réseau interne, où ils sont
utilisés par la même organisation à des fins internes, et sont traités comme des entités
accédant aux services fournis par le serveur dans la DMZ.
Cette approche est adoptée pour la raison suivante ; considérant une architecture sans
DMZ, où il n’y a pas de séparation entre les entités internes et externes. En cas de
détournement du serveur (i.e. tentative d’altération), notre réseau interne (et éventuellement
tous les agents d'inférence) sera affecté par cette tentative destructive. Cependant, l’approche
proposée nous permet de réduire considérablement le point de défaillance unique.
3.3.4. Données échangées
Bien que les données d'entraînement ne soient visibles que pour l'agent qui les détient, il en
existe néanmoins des données circulant entre le serveur et ces agents, chose qui fait de
l'approche fédérée un principe fondamental. Selon notre architecture proposée, ces données
échangées reposent principalement sur un flux de paramètres associés aux modèles
d’apprentissage. Ces paramètres sont représentés par les poids et éventuellement les biais des
réseaux de neurones utilisés dans le processus d'entraînement.
De nombreuses revues exposent les principaux conflits liés aux données transférées durant
le processus d’apprentissage [24][26], ce qui nous sollicite à prendre en compte certaines
mesures de sécurité.
Les défis énoncés dans ce contexte peuvent être classés en deux
catégories (voir la sécurité, et la communication5) selon leur impact à affecter les
aspects critiques de l’apprentissage fédéré, touchant ainsi au bon fonctionnement du système.
5
Assurer une communication légère en bande passante, dépend le plus souvent par la complexité liée à la
définition de l’architecture du modèle d’apprentissage (par ex : taille, profondeur ...etc.).
Page 7 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
a. Chiffrement des Données
Garantir la confidentialité des données est une préoccupation principale dans
l'apprentissage fédéré. Pour protéger les informations sensibles, Plusieurs techniques de
protection des données ont été mise à disposition, telles que le chiffrement, l'agrégation
sécurisée et la confidentialité différentielle [15][17][21]. Ces méthodes protègent la
confidentialité des données individuelles pendant l'entraînement et l'agrégation du modèle.
L'application de l'apprentissage fédéré pour la détection d'intrusions est récente, et sa
combinaison avec les technologies de sécurité avancées telles que les registres distribués est
encore plus récente [13].
Les mécanismes de préservation de confidentialité peuvent être divisés en deux groupes ;
des mécanismes qui chiffrent ou obscurcissent les gradients et empêchent les parties
malveillantes de tirer des conclusions sur l'ensemble de données, et des mécanismes qui
masquent l'identité des parties participantes [17]. Cependant, notre objectif est de fournir un
degré de confidentialité en adoptant le chiffrement homomorphe.
Après une analyse approfondie, nous avons identifié Pyfhel, Concrete-ML et TenSEAL
comme les bibliothèques Python les plus adaptées pour le chiffrement homomorphe dans le
cadre de notre projet [35]. Pour implémenter le chiffrement homomorphe, nous exploitons la
bibliothèque TenSEAL, basée sur la bibliothèque Microsoft SEAL6, pour réaliser des
opérations de cryptage homomorphe sur les tenseurs, offrant ainsi des performances élevées
et la facilité d'utilisation.
Tableau 3.1: Comparaison détaillée sur les différentes technologies
Bibliothèque
Caractéristique
Basée surPyfhel
HELibConcrete-ML
---TenSEAL
Microsoft SEAL
Niveau de sécurité
DocumentationElevé
Complète et
détailléeVariable
LimitéeElevé
Bien documentée
PerformancesRapidesDépendantes du
contextePerformantes
Convivialité
Fonctionnalités
Support actifFacile à utiliser
Large éventail
OuiConviviale
Limitées
VariableConviviale
Complètes
Actif
6
Cette bibliothèque permet de prend en charge les schémas BGV et CKKS, mais pourrait nous présenter des
limitations par rapport à des bibliothèques plus orientées vers la recherche.
Page 8 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
b. Schéma de Cheon-Kim-Kim-Song (CKKS)
Le schéma de Cheon-Kim-Kim-Song (CKKS) est un schéma de chiffrement homomorphe
(FHE), qui nous permet de faire des opérations d'addition et de multiplication à la fois sur des
données chiffrées [32]. Contrairement aux schémas de chiffrement homomorphe (SHE),
CKKS nous permettra de prend en charge la multiplication homomorphique avec une limite
constante sur le niveau de bruit. Cette limite peut être réduite grâce à un processus de
"bootstrapping", qui ré-encrypte le texte chiffré tout en réduisant le bruit [31]. Concernant
notre architecture fédérée, le CKKS nous offre la possibilité d’effectuer des calculs sécurisés
sur des données chiffrées, raison pour laquelle nous avons opté pour une telle mesure.
Habituellement, un processus d’apprentissage fédéré vertical (VFL) admet que tous les
participants sont authentiques. Dans le cas de deux parties, par exemple, celles-ci sont non
coopératives, et au mieux, le concurrent est lésé. Le concept de sécurité est que l'adversaire
ne pourrait apprendre que des données de l'utilisateur compromises mais pas des données
provenant d'un autre client sauf celles qui sont exposées par les entrées et les sorties [22][23].
Il est à noter que nous assumons que le serveur est une entité de confiance. Cependant, même
si le chiffrement homomorphe est utilisé pour sécuriser les données, les agents doivent avoir
confiance en le serveur centralisé. Sinon, des fuites de données se produiront [16].
c. Encapsulation et Transfère des Données
Il est essentiel d'assurer l'intégrité, en évitant toute altération ou perte de données pendant
leur transfert. D’après la technologie7 employée pour notre architecture, nous nous
contenterons d’utiliser les communications TCP/IP comme protocole de transport pour les
échanges entre le serveur et les clients. Notre solution est relative à la fiabilité, où la
transmission soit critique et que des retards ou des pertes de données ne sont pas acceptables.
Cela nous garanti, entre outre, une communication fiable et sécurisée entre les différents
composants du système.
7
Cette technologie, basée sur HTTP/2 fait référence à Flower (fonctionnant sous la convention de RPC) que
nous allons aborder dans le chapitre suivant.
Page 9 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.4. Méthodes et Techniques Employées
Il est à noter que notre choix de méthodes et de techniques a été mené par une inspection
approfondie de la littérature existante [4][5], offrant un aperçu des solutions actuelles. Cette
couverture nous a conduits à bien concevoir notre architecture, tenant compte des différents
aspects critique de chaque technique.
3.4.1. Model d’Apprentissage
Selon la littérature, le choix du modèle d’apprentissage représente une décision
déterminante lors de la conception de l’architecture. Plusieurs études [4][6][8] ont pu définir
un large éventail de modèles en démontrant leur efficacité dans le contexte de la détection
d’intrusions [4]. Avec une fréquence accrue des attaques réseau, les chercheurs accordent
plus d'attention à la sécurité réseau [5], mais seulement quelques-uns d'entre eux ont exploité
l'apprentissage profond bien qu'ils n'aient pas complètement exploré les applications de
l'apprentissage profond en ce qui concerne les NIDSs [1]. Cependant, les modèles à base de
réseaux de neurones profonds, ont prouvé leur capacité à apprendre des représentations à
partir des parquets d’en-têtes, faisant ainsi un choix avantageux pour notre architecture, où
les agents d’entrainement peuvent bénéficier d’une partie d'apprentissage locale sur leurs
propres données, tout en contribuant à l'amélioration d'un modèle global.
Ayant consulté une variété d’applications, notamment l’application des réseaux récurrents
RNNs [4][5], l’applications des GANs [6], ainsi que celles des Auto-encoders [4][6], nous
avons trouver que la meilleure solution consiste en appliquant les réseaux de neurones
profonds. le choix de cette solution se justifie par le fait que, dans l‘apprentissage fédéré, il
est nécessaire de tenir compte de plusieurs facteurs, tels que la taille, la complexité et les
contraintes de calcul au niveau des agents d’inférence. L'idée principale de l'utilisation des
architectures neuronales profondes est qu'elles aident à réduire automatiquement la
complexité du trafic réseau. Elles identifient des corrélations dans les données sans nécessiter
un algorithme explicite de sélection des caractéristiques ou un expert du domaine. De plus,
elles sont efficaces pour détecter les exploits « zero-day » et les attaques avancées [1].
Cependant, le choix du modèle doit être capable de fournir un équilibre entre performance
(i.e. précision et temps de réponse) et complexité.
Page 10 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Parlant du modèle, nous avons adopté une architecture profonde composée de plusieurs
couches, permettant une représentation complexe des données et une meilleure capacité de
généralisation. De plus, Nous avons également utilisé la régularisation lors de l’apprentissage
afin d’éviter la situation de sur-apprentissage et ainsi favoriser une meilleur convergence du
modèle globale. Mise à part la précision, le temps de détection doit également être pris en
compte. Plus une intrusion est détectée rapidement, plus les administrateurs réseau seront
alertés pour prendre les mesures nécessaires [1]. En appliquant ce modèle, nous avons pu
obtenir une architecture adaptable aux exigences de notre système d’apprentissage fédéré.
3.4.2. Technique d’Agrégation
Après l'acheminement de l'entraînement des différents modèles locaux, les agents
concernés peuvent alors communiquer leurs changements au serveur central. Ce dernier est
chargé de les combiner pour former un modèle global en utilisant la technique d'agrégation
FedAvg. Ce choix est le résultat d'une étude approfondie de l'état de l'art. Nous avons
sélectionné la technique d'agrégation FedAvg appropriée pour notre architecture, car elle
permet de réduire la quantité de données transmises entre les appareils et le serveur central,
ce qui peut être bénéfique en termes de bande passante et de consommation d'énergie.
3.4.3. Filtrage d’Agents
Pour prendre en charge un grand nombre de dispositifs, nous pouvons appliquer la
procédure de sélection des clients pour choisir une fraction à entraîner lors d'un cycle
d’exécution. En filtrant les agents avant l'agrégation, on peut ainsi exclure les agents de base
fiabilité, ce qui permet d'améliorer la rentabilité et la qualité de notre architecture.
De nombreux algorithmes de sélection des nœuds (agents) sont proposés pour améliorer
l'efficacité de l'apprentissage fédéré [18][21][14]. De ce fait, Nous avons réalisé une revue
approfondie de la littérature portant sur les techniques de sélection d’agents dans le cadre de
l'apprentissage fédéré. Cette revue nous a permis d'analyser en détail les différentes
approches de filtrage existantes.
Page 11 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Pour notre architecture, nous avons choisi d’implémenter le détecteur des clients
empoisonnés, proposé par [20] au niveau du
serveur,
pour identifier les clients
potentiellement empoisonnés et limiter leur participation à l'agrégation du modèle de
détection d'intrusion global. Il est important de réduire l'influence des clients empoisonnés sur
le modèle de détection d'intrusion global. A cet effet, l’intégration de ce mécanisme à notre
système, nous permet, en outre, de réduire la charge de traitement au niveau du serveur,
d'éliminer les agents susceptibles d'être empoisonnés, et de favoriser une convergence
efficace du modèle global.
Figure 3.4 : Coordination entre différents acteurs
Page 12 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5. Données d’apprentissage
Un système de détection d'intrusion idéal devrait être capable de détecter une grande
variété d'attaques. Il devrait également avoir un taux de détection élevé avec un faible taux de
fausses alertes. Ainsi, un ensemble de données de qualité, actuel et diversifié aura un impact
considérable sur la précision de notre modèle [1][4].
Certaines études que nous avons consultées montrent que de nombreux ensembles de
données ont été publiés au cours des dernières années, et que la communauté travaille
continuellement à la création de nouvelles données pour la détection d'intrusions [3][5]. Les
données utilisées pour la recherche peuvent être soit réalistes (capturées), soit synthétiques
(générées). Pour les données réalistes, celles-ci sont capturées soit au format basé sur les
paquets, soit au format basé sur les flux, soit à un format indéfini [3], toute en gardant
l’aspect de confidentialité8.



Format basé sur les paquets9 : destiné aux HIDSs, en miroitant les ports sur les dispositifs
réseau, englobant des informations de contenu complètes.
Format basé sur les flux10 : destiné aux NIDSs, dans lesquels elles sont agrégées et
contiennent généralement uniquement des métadonnées des connexions réseau.
Format indéfini: aucun cadre spécifique pour la capture de données, cette catégorie
pourrait être constituée de données basées sur les flux qui ont été enrichis avec des
informations supplémentaires à partir de données basées sur les paquets.
Il est à noter que la plupart des systèmes d'intrusion s'appuient sur des ensembles de
données obsolètes, et qu'ils ne reflètent donc plus les nouveaux types d'attaques [1][5]. A cet
effet, il serait judicieux pour nous de choisir soigneusement un ensemble, considérant la
qualité et la pertinence. La principale raison du manque de disponibilité des ensembles de
données d'intrusion est que la construction de nouveaux ensembles nécessite souvent une
expertise en matière de connaissances. Un autre problème majeur que nous avons constatés
est que les attaquants trouvent de nouvelles techniques pour éviter la détection, ce qui rend
nécessaire l'intégration continue de nouveaux types d'attaques à ceux existants [1].
8
Les données capturées doivent être traitées avec précaution. Certains attributs peuvent être tirés de façon
anonyme, d'autres doivent être omis si besoin.
9
Les métadonnées disponibles dépendent des protocoles réseau et de transport utilisés. Voir 3.5 de l’annexe.
10
En considérant la direction des flux, Les données réseau basées sur les flux peuvent être capturées soit de
manière unidirectionnelle soit bidirectionnelle.
Page 13 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5.1. Choix des Jeux de Données
Dans le même contexte, Une méthode que nous avons consultée [3], nous a fourni une
classification en 5 propriétés distinctes (à savoir ; les informations générales, la nature, le
volume, l’environnent et l’évaluation), par lesquelles nous pouvons facilement conclure une
analyse11 sur chacun des ensembles de données. En revanche, Les auteurs, ayant cités ; « Le
jeu de données parfait devrait être à jour, correctement étiqueté, disponible publiquement,
contient du trafic réseau réel avec toutes sortes d'attaques et de comportements d'utilisateurs
normaux ainsi que leurs contenus, et couvre une longue période. Cependant, un tel jeu de
données n'existe pas et ne sera (probablement) jamais créé.», montrent que, même dans le
respect de la confidentialité, et dans un environnement réel, un jeu de données comportant
toutes les attaques récentes ne peut être entièrement étiqueté qu’après l’apparition de
nouvelles attaques [3][5]. Cependant, nous visons à anticiper l’évaluation de notre système
avec un jeu de données décrivant plus qu’un format particulier (i.e. de nature diversifiée),
puisque suivant le paradigme fédéré, et éventuellement dans l’environnement réel, différents
données depuis des sources distincts et éloignées existent. En couvrant un certain nombre de
revues12 [5][6], nous avons pu déduire notre choix concernant le jeu de données approprié.
Notre approche sera mise en œuvre pour éviter la convergence vers un ensemble spécifique,
évaluer le système dans un contexte plus général, et d’imitez le comportement d’un HIDS et
d’un NIDS à la fois.
3.5.2. Jeu de Données CSE-CIC-IDS 2018
L’ensemble de données (CSE-CIC-IDS 2018) est proposé par le Centre de la sécurité des
télécommunications
(CSE) et l’institut canadien de cyber-sécurité (CIC) en 2018. Cet
ensemble, faisant partie du group13 des ensemble à base de flux réseaux, comprend sept
scénarios d'attaque différents, notamment Heartbleed, Brute-force, DoS , DDoS , les
attaques Web, Botnet et les attaques d'infiltration [6][10]. Plusieurs revues sur cet ensemble
ont été élaborées ces dernières années, nous permettant d’avoir un aperçu bien précis et
détaillé de cet ensemble [10][1][4][6]. Ce jeu de données, constitué de plus de 16 million
d’exemples, et de 80 attributs au total, est mené d’un attribut complémentaire représentant la
classe correspondante à chaque donnée associée. Selon l’étiquette, deux profils peuvent se
caractérisés à partir de cet ensemble, voir B-profil et M-profil.
11
Les auteurs n'ont pas élaboré de score d'évaluation pour ne pas comparer les différents ensembles.
L'importance de certaines propriétés ne devrait pas être jugée de manière critique.
12
Dont certaines d'entre elles sont fondées sur les stratégies de recherche SLR, PRISMA, et SnowBall.
13
Selon la contribution de l’étude [6], où ils ont pu classer les jeux suivant sept groups d’ensemble distincts.
Page 14 sur 99CHAPITRE 3 : Conception de l’Architecture


PARTIE II
Profil Bénin (B-Profil) : Résume le comportement typique des utilisateurs normaux. Il
encapsule les comportements des entités utilisatrices dans un ensemble de caractéristiques
telles que la taille des paquets, le nombre de paquets par flux, la taille du contenu et les
motifs du contenu [9].
Profil Malveillant (M-Profil) : Vise à décrire de manière claire un scénario d'attaque. Il
a fallu utiliser des agents autonomes et des compilateurs pour interpréter et exécuter ces
scénarios [9].
3.5.3. Jeu de Données ADFA 2013
Les ensembles de données utilisés pour évaluer les HIDS ne sont pas facilement
disponibles en raison de problèmes de sécurité et de confidentialité. Cependant, il existe de
nombreux ensembles de données disponibles publiquement, tels que ADFA-LD, et ADFA-
WD qui sont couramment utilisés comme références [8].
Des chercheurs de l'Académie de la Force de Défense Australienne (ADFA) ont créé
deux ensembles de données, voir ADFA-LD «Linux-based» et ADFA-WD «Windows-
based», en tant qu'ensembles de données publics représentant la structure et la méthodologie
des attaques modernes. Les ensembles de données contiennent des enregistrements d'appels
système, à partir des systèmes d'exploitation Linux et Windows à la fois. Certaines instances
d'attaque dans ADFA-LD ont été dérivées de nouveaux logiciels malveillants « zero-day », ce
qui rend cet ensemble de données approprié pour mettre en évidence notre propre architecture
fédérée en matière de détection d'intrusions.
ADFA a été développé comme étant une référence moderne pour les IDS basés sur les
hôtes (HIDS). L'ensemble de données étiqueté ADFA14 est le successeur de la collection
KDD, utilisant les dernières failles et techniques d’intrusion disponibles [33]. Cet ensemble a
été utilisé par les chercheurs pour évaluer les performances de leurs approches proposées de
détection et de prévention des intrusions [10], la raison pour la quelle nous avons choisi le jeu
de données comme étant le référentiel des comportements des hôtes.
14
En plus du manque de diversité et de la variété des attaques, les comportements de certaines attaques dans cet
ensemble de données ne sont pas bien séparés du comportement normal [10].
Page 15 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5.4. Défis et Préoccupations
En pratique, les données entre les nœuds sont généralement non-IID. De plus, la quantité
de données distribuées sur chaque nœud est toujours déséquilibrée. Par conséquent, le télé-
versement fréquent de modèles sur des agents particuliers, a le potentiel d'attirer la
divergence vers le modèle global et de provoquer un sur-ajustement à des ensembles de
données spécifiques [18]. Cette divergence envers les données, peut nuire à l’apprentissage
fédéré du model global, et ainsi compromettre sa capacité à généraliser correctement. Par
conséquent, le rendement apporté à notre system sera affecté.
a. Données non identiques et indépendantes (non-IID)
Dans des scénarios réalistes, les données des clients sont confirmées comme non
indépendantes et identiquement distribuées (non-IID), contrairement aux scénarios IID
idéalement supposés dans de nombreuses méthodologies de recherche. Dans les systèmes de
détection d'intrusion basés sur l'apprentissage fédéré, certains clients (dispositifs) peuvent ne
présenter que du trafic malveillant tandis que d'autres peuvent présenter du trafic normal ou
être composés de différents types de trafic malveillant [20]. Ainsi, des études ont révélé que
le taux de convergence peut être réduit par des facteurs tels que l'entraînement sur de petites
données non-IID [19].
Cependant, notre expérience sera menée sur des ensembles de données IID et non-IID à la
fois, pour vérifier l'efficacité de notre approche. Dans le cas de notre étude, nous
commençons par partitionner les données d'entraînement originales en ensembles
d'entraînement non-IID disjoints, pour rapprocher le scénario typique. Notre expérimentation
sera menée sous différentes situations possibles pour simuler le comportement réel des
agents faisant face à la situation des données non-IID.
b. Déséquilibrage de classes
Consultant diverses études, les ensembles de la littérature (y compris ceux que nous
utilisons) sont confrontés à une contrainte connue sous le nom du problème de
déséquilibrement de classe, où la distribution des données de trafic réseau est inégale, avec
des exemples normaux apparaissant plus fréquemment que les exemples d'attaque. Ce
déséquilibre peut affecter les performances de notre modèle, en particulier pour les classes
d'attaques minoritaires [2][5].
Page 16 sur 99CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Selon les contributions qui ont été faites, nous avons constaté qu'il existe des techniques
de ré-échantillonnage [2] (telles que le oversampling, le undersampling et le hybrid
sampling), et l’approche coût-sensitive [5], qui peuvent être solutions pour surmonter les
ensembles de données déséquilibrés. Dans le cas de notre étude, nous avons préférer
d’appliquer une technique de ré-échantillonnage (l’augmentation des données en particulier)
pour son efficacité à contourner le problème.
3.6. Conclusion
Dans ce chapitre, nous avons présenté une nouvelle architecture d'apprentissage fédéré
pour les systèmes de détection d'intrusions (IDS). L'architecture proposée tire parti des
avantages de l'apprentissage fédéré, tout en abordant les défis spécifiques au domaine des
IDSs.
Nous avons décrit les différents acteurs impliqués dans le système, ainsi que leurs
emplacements relatifs. Nous avons décrit le processus d'échange de données, en mettant
l'accent sur le chiffrement des données et les mécanismes de transfert sécurisé entre les
entités participantes. De plus, nous avons discuté des méthodes et des techniques utilisées
dans l'architecture, telles que le choix du modèle d'apprentissage, la technique d'agrégation et
le filtrage des agents. Enfin, nous avons abordé les défis associés aux données d'entraînement
dans les IDS fédérés, notamment les données non-IID et le déséquilibrement des classes, en
soulignant l'adaptabilité de notre architecture envers différents scénarios.
Page 17 sur 99 """

user_text3 = """ Sommaire
Chapitre 1 : Étude de l’état de l’art
1 . 1 . Introduction ....................................................................................................................... 1
1 . 2 . La securite informatique.................................................................................................... 1
1 . 3 . Defis de la securite informatique ...................................................................................... 2
1 . 3 . 1 . Protection des données ...........................................................................................3
1 . 3 . 2 . Protection de la réputation .....................................................................................3
1 . 3 . 3 . Continuité d’activités .............................................................................................3
1 . 3 . 4 . Innovation des technologies ...................................................................................3
1 . 3 . 5 . Sensibilisation ........................................................................................................4
1 . 4 . Vulnerabilités et attaques informatiques ........................................................................... 4
1 . 4 . 1 . Vulnérabilité des systèmes informatiques .............................................................4
a). Vulnérabilité logicielle ...........................................................................................5
b). Vulnérabilité matérielle ..........................................................................................6
1 . 4 . 2 . Classification de kendall ........................................................................................6
1 . 4 . 3 . Catégories d’attaques .............................................................................................7
a). Injection SQL .........................................................................................................7
b). Botnet .....................................................................................................................7
c). Cross-site script (XSS) ...........................................................................................8
d). Force brute .............................................................................................................8
1 . 5 . Mecanismes de protection des systemes informatiques .................................................... 8
1 . 5 . 1 . Contrôle d’accès au niveau de l’hôte .....................................................................9
1 . 5 . 2 . Contrôle d’accès au niveau du réseau ....................................................................9
1 . 5 . 3 . Autres contrôles d’accès ........................................................................................9
1 . 6 . Systeme de detection d’intrusions (IDS) ......................................................................... 10
1 . 6 . 1 . Principes et généralités.........................................................................................11
1 . 6 . 2 . Différentes classification......................................................................................11
a). Selon l’approche de détection ..............................................................................12
b). Selon l'emplacement surveillé ..............................................................................13
c). Selon l’architecture...............................................................................................15
d). Selon la fréquence d’utilisation ............................................................................16
e). Selon la réponse aux événements .........................................................................17
f). Selon la source de données ...................................................................................18
1 . 6 . 3 . Limitations des systèmes traditionnels ................................................................19
1 . 7 . Conclusion ....................................................................................................................... 21CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I :
PARTIE I
ETUDE DE L’ETAT DE L’ART
CHAPITRE 1
PRINCIPES FONDAMENTAUX DE
LA SÉCURITÉ INFORMATIQUE
_________________________
1.1. Introduction
La conception de l'architecture en matière de cybersécurité est un processus crucial pour
garantir la protection des systèmes informatiques et des données sensibles. Cependant,
protéger les systèmes informatiques contre toutes les attaques qui sont en évolution rapide en
nombre et en complexité, est une tâche difficile. Ce chapitre vise à donner une vue globale
sur le domaine de la sécurité informatique et ses différentes facettes. Dans ce chapitre, nous
aborderons les différents aspects de la cyber-sécurité, en mettant l'accent sur les différents
défis auxquels font face les organisations, afin de mettre en place une politique de sécurité
qui intervient à différents niveaux. Nous introduisons également les différentes catégories
d'attaques et de vulnérabilités, ainsi que les mesures de protection des systèmes informatiques
contre ces activités malveillantes. En particulier, nous explorerons les principes et les
classifications d’un système de détection d'intrusions (IDS), qui constitue l’objet de notre
étude, en soulignant les limitations concernant leur fonctionnement traditionnel.
1.2. La sécurité informatique
À l’ère numérique actuelle, le recours croissant aux technologies de l’information et des
communications (TICs) a rendu le monde plus interconnecté, efficace et interactif.
Cependant, cette dépendance à l’égard des systèmes de TIC a créé des faiblesses et des
menaces qui font de la sécurité informatique une priorité mondiale [36]. Car englobe la
protection des actifs numériques, des systèmes et des réseaux contre l’accès illégal, l’abus, la
perturbation ou la destruction des actifs1.
1
Un actif est une ressource importante pour une organisation, qui peut être physique ou virtuelle. Il peut s'agir
d'un ensemble de données, d'un système informatique, d'une application, ou de toute autre ressource jugée être
exposée aux différents risques pour une organisation.
Page 1 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
D’une façon formelle, la sécurité informatique « cyber security » est relative à la
protection accordée à un système d'information automatisé afin d'atteindre des objectifs
applicables aux ressources du système d'information (y compris le matériel, logiciels, micro
logiciels, informations ou données et télécommunications).
Cette discipline avec ces multiples facettes met en évidence une interaction complexe de
considérations techniques, juridiques et éthiques. Elle vise à équilibrer la protection de la
valeur essentielle avec les défis en constante évolution des cyber-menaces, qui vont des virus
informatiques de base aux types sophistiqués d’activités de cybercriminalité et de cyber-
espionnage. Par conséquent, la cyber-sécurité comprend un ensemble complet de techniques,
de processus et de pratiques conçus pour préserver la confidentialité, l’intégrité et la
disponibilité des données [36]. Cette protection s’applique aux données au repos (stockées) et
en transit (transmises via les réseaux), tout en assurant l’authentification et l’imputabilité2 des
utilisateurs et de leurs actions. En mettant en œuvre ces mesures, la cyber-sécurité s’efforce
d’atténuer les risques associés à la cybercriminalité, aux cyberattaques et à d’autres activités
malveillantes susceptibles de compromettre les données, l’infrastructure ou les opérations
numériques [94].
1.3. Défis de la sécurité informatique
Les défis de la sécurité de l’information ne cessent de croître. Les cyber-attaques peuvent
causer des dommages aux entreprises, aux gouvernements et aux particuliers [36]. Ils peuvent
entraîner des pertes financières, des vols de données, des atteintes à la réputation et des
perturbations cruciales de l’infrastructure.
Les utilisateurs malintentionnés sont devenus de plus en plus spécialistes et collaborent au
développement d’actions plus sophistiquées et difficilement détectables. Cette évolution
rapide de la complexité des actions rend la tâche des responsables de la sécurité informatique
d’avantages complexe. Il est observé que la motivation des « hackers » à beaucoup changée.
Une action malveillante peut être lancée pour des raisons politiques ou financières, mais aussi
pour simplement bouleverser l’ordre d’une organisation. Certains des défis importants en
matière de cyber-sécurité (sans être exhaustif) sont mentionnés ci-dessous.
2
A ce critère, s’ajoutent ceux qui contribuent à confirmer d’une part la véracité, et l’authenticité, et d’autre part,
la traçabilité et la non-répudiation d’une entité ou une action.
Page 2 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
1.3.1. Protection des données
Les systèmes informatiques stockent et manipulent des données sensibles, telles que des
informations personnelles, des données financières ou des secrets commerciaux. Ces
systèmes font face à des défis quotidiens pour protéger ces données contre le vol, la
corruption ou la destruction [36].
1.3.2. Protection de la réputation
L’ère numérique a transformé le fonctionnement des organisations et des entreprises,
mais elle a amplifié les risques pour leur réputation. En plus de protéger des données et des
systèmes importants, la défense de leur image publique contre les cyber-menaces est devenue
un défi critique et distinct. L’interconnexion des entreprises modernes crée de nombreux
points d’attaque, érodant la confiance. Les difficultés à attribuer les attaques et à équilibrer la
sécurité avec la confidentialité ajoutent à la complexité. De plus, l’erreur humaine demeure
une menace, et la rapidité du flux d’information peut rapidement transformer un petit
problème en une crise majeure de réputation.
1.3.3. Continuité d’activités
La dépendance constante des entreprises à l’égard de leurs systèmes de TI crée un besoin
critique en matière de planification de la continuité des activités. Une cyber-attaque peut
perturber ou interrompre les activités des entreprises, elle peut également entraîner
d’importantes pertes financières et ruiner la réputation [37]. Ce qui crée un défi pour
s’assurer que ces informations et services sont toujours disponibles.
1.3.4. Innovation des technologies
L’innovation et le développement quotidiens des technologies sont une arme à double
tranchant pour la cyber-sécurité. Bien qu’elle ouvre la porte à des avancées incroyables, elle
crée également un paysage de menaces en constante évolution. Les cybercriminels savent
exploiter les nouvelles vulnérabilités pour forcer les professionnels de la cyber-sécurité à
rester en veille. Cette course aux armements en cours exige une adaptation continue, les
chercheurs développant de nouvelles mesures de sécurité alors même que les attaquants
conçoivent des outils toujours plus sophistiqués.
Page 3 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
1.3.5. Sensibilisation
Le besoin de personnel qualifié en cyber-sécurité et l’obligation de sensibilisation des
utilisateurs aux risques et à la réglementation, les professionnels de la cyber-sécurité doivent
également développer des compétences au-delà de l’expertise technique, y compris la
créativité, l’innovation et les compétences techniques, afin de pouvoir traiter efficacement les
risques de cybersécurité [36].
Pour relever ces défis, les organisations doivent investir dans une sécurité robuste,
cultiver une culture de sensibilisation à la sécurité et suivre les mises à jour et les
développements en matière de cyber-sécurité. En prenant ces mesures, les entreprises peuvent
renforcer leur résilience, atténuer les risques et protéger leur réputation à l’ère de la
vulnérabilité numérique.
1.4. Vulnérabilités et attaques informatiques
Tout ordinateur ou appareil, est potentiellement vulnérable aux attaques. Une attaque
informatique est une suite d’actions effectuées par un logiciel3 malveillant exploitant une
vulnérabilité pour obtenir un contrôle total ou partiel du système victime afin de
compromettre les propriétés de sa sécurité informatique. Généralement, le succès d’une
attaque repose sur la présence des failles et des vulnérabilités dans les réseaux et les systèmes
informatiques. Ceci motive les pirates à exécuter facilement leurs tâches en utilisant des
programmes malicieux. Ces menaces informatiques peuvent être divisées en deux types : les
vulnérabilités et les programmes malveillants. Dans la section suivante, nous définissons
l’interprétation d’une vulnérabilité, ainsi que ses aspects liés aux systèmes informatiques.
1.4.1. Vulnérabilité des systèmes informatiques
La vulnérabilité est une faille connue ou suspectée dans la conception du matériel ou du
logiciel qui expose le système à la pénétration ou ses informations à la divulgation
accidentelle [96], Une vulnérabilité peut aussi être appelée : "erreur", "défaut" ou "faiblesse".
L’attaquant peut obtenir une extra autorité du système informatique en utilisant sa
vulnérabilité, puis casser la sécurité de ce système en accédant ou améliorant l'autorité
d'accès. La vulnérabilité comprend tous les facteurs qui peuvent conduire à menacer ou à
3
Bien évidement, puisqu’on parle d’une attaque dans le contexte informatique, seul un logiciel représente le
moyen auquel l’attaquant est censé être muni pour sa tentative d’accès.
Page 4 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
compromettre la sécurité du système informatique (l’intégrité, la convivialité, le secret, la
fiabilité ou la contrôlabilité) [97].
Généralement, la vulnérabilité elle-même ne peut pas causer des dommages à la sécurité
du système, mais l'attaquant peut utiliser une vulnérabilité et effectuer différentes actions
malveillantes dans un système informatique. Ainsi, chaque jour, nous apprenons que des
nouvelles vulnérabilités sont découvertes dans les programmes et réseaux informatiques, les
rapports de sécurité publient des chiffres inquiétants et rapportent que les nombres de failles
sont en augmentation continue.
Dans la littérature plusieurs classifications de la vulnérabilité ont été proposées afin de
mieux caractériser ce domaine de la sécurité informatique. Dans ce qui suit, nous en
présentons les deux principaux types qui sont : la vulnérabilité logicielle et la vulnérabilité
matérielle.
a). Vulnérabilité logicielle
Les logiciels constituent un premier niveau d’abstraction à partir duquel un attaquant peut
mettre en défaut la sécurité d’un système informatique. Dans ce contexte, le terme système
logiciel doit être pris dans son sens le plus général. Il désigne tous types de logiciels dans un
système informatique, couvrant aussi bien les programmes d’application, le système
d’exploitation et son noyau [98].
La plupart des systèmes logiciels contiennent des vulnérabilités, c’est-à-dire des fautes de
conception, de programmation ou de configuration [100]. Un attaquant peut alors exploiter
ces vulnérabilités comme autant de vecteurs d’attaque pour effectuer différentes actions
malveillantes dans un système informatique. Une attaque, à ce niveau d’abstraction, repose
sur l’exploitation d’une fonctionnalité logicielle vulnérable à des fins malveillantes.
La plupart des vulnérabilités identifiées par analyse4 sont associées à une manière
incorrecte de traiter les entrées fournies par un utilisateur du système, si ces entrées ne sont
pas traitées correctement avant de les utiliser à l'intérieur du programme, elles peuvent
générer un comportement inattendu du système [99]. Par exemple, certaines vulnérabilités
connues et fréquentes sont discutées dans la section des catégories d’attaques suivantes.
4
L’analyse de vulnérabilités se divise généralement en deux types : l'analyse statique, qui examine le code
source pour identifier les failles potentielles sans exécuter le programme, et l'analyse dynamique, qui teste le
programme en cours d'exécution pour détecter les vulnérabilités.
Page 5 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
b). Vulnérabilité matérielle
De la même façon que les systèmes logiciels, les systèmes matériels peuvent contenir des
fonctionnalités matérielles vulnérables. Toutefois, celles-ci sont moins courantes que les
vulnérabilités logicielles et dans la majorité des cas, elles ne sont pas exploitables. Comme
exemple, le bogue matériel découvert dans les processeurs Pentium en décembre 1997 aurait
pu être utilisé pour perpétrer des attaques contre la disponibilité. En effet, lorsqu’un
processeur Pentium exécutait une séquence d’instructions données, celui-ci se bloquait
aussitôt. Il s’est révélé que cette instruction n’étant en fait pas valide, l’exécution de celle-ci
déclenche une exception matérielle. Une personne malintentionnée pourrait profiter de ce
bogue matériel pour provoquer des dénis de service simplement en exécutant un programme
contenant cette séquence d’instructions [98].
Dans le même contexte, Les attaques devraient être caractérisées par les méthodes
d’attaque, les vulnérabilités exploitées et l’opportunité [95]. Les attaques informatiques sont
classées suivant plusieurs angles de vues. Elles peuvent être classées selon leurs effets sur les
ressources du système informatique (attaques passives ou actives 5), selon leur localisation
(attaques internes ou externes6), ou bien selon leurs scénarios d’intrusions (classification de
Kendall) [124]. Dans ce qui suit, nous présentons le concept le plus généralement utilisé par
la majorité des études, le concept de kendall et ses éventuelles classes d’attaques.
1.4.2. Classification de Kendall
Cette classification provient des travaux de Kendall, qui consistent à simuler des
scénarios d'intrusions réalistes avec divers degrés de sophistication et de furtivité. Il propose
de regrouper ces intrusions en quatre catégories : DoS, Probe, U2R et R2L.
- Denial of Service : Les attaques DoS visent à rendre un système informatique indisponible
en épuisant ses ressources, empêchant ainsi les utilisateurs légitimes de l'utiliser.
- Probing : Les attaques Probe visent à recueillir des informations sur les ressources d'un
système ou à détecter des vulnérabilités potentielles.
5
Les attaques passives visent l’obtention d’information, tandis que les attaques actives visent la modification
d’information. Contrairement aux attaques actives qui sont plus critiques, les attaques actives n’affect pas le
comportement du système, et donc ne sont pas facilement détectables.
6
Les attaques internes sont engendrées par des utilisateurs internes au système informatiques qui tentent
d’abuser de leurs droits et privilèges. Les attaques externes sont causées par des utilisateurs externes au système
et qui tentent d’accéder aux ressources d’une manière illégitime.
Page 6 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
- User to Root : Les attaques U2R visent à obtenir les privilèges d'un super utilisateur à partir
d'un compte utilisateur normal en exploitant les failles du système.
- Remote to Local : Les attaques R2L tentent d'obtenir un accès légitime à une ressource pour
laquelle l'attaquant n'a pas de compte utilisateur.
1.4.3. Catégories d’attaques
Nous avons abordé précédemment une classification formelle des attaques, qui nous
permet entre outre, de regrouper plusieurs types d’actions selon leur scénario typique. Or, les
attaques de sécurité informatique sont devenues monnaie courante dans le paysage numérique
actuel, avec des méthodes toujours plus sophistiquées utilisées par les cybercriminels pour
compromettre la sécurité des systèmes et des données. Ce qui nous mène à identifier les
techniques les plus courantes, en respect à la classification de kendall. Dans cette section,
nous allons nous concentrer sur les attaques les plus connues, en expliquant leurs
mécanismes, ainsi que leurs impacts sur la sécurité des systèmes informatiques.
a). Injection SQL
Les injections SQL représentent une faille de sécurité grave dans les applications Web qui
utilisent des bases de données SQL. Elles surviennent lorsque les entrées des utilisateurs ne
sont pas correctement nettoyées avant d'être utilisées pour générer des requêtes SQL,
permettant aux attaquants d'injecter du code SQL malveillant et d'obtenir un accès illégal à la
base de données [36]. Pour prévenir les injections SQL, les développeurs doivent utiliser des
instructions préparées ou des requêtes paramétrées pour séparer le code SQL des données
utilisateur, réduisant ainsi le risque de compromission du système et soulignant l'importance
des pratiques de codage sécurisé et de la formation des développeurs en matière de sécurité.
b). Botnet
Une attaque de botnet implique un réseau d'appareils compromis contrôlés par un
cybercriminel pour mener des activités malveillantes, telles que des attaques DDoS. Ces
attaques posent des menaces importantes en raison de leur nature dynamique et flexible,
rendant les méthodes de détection traditionnelles inefficaces contre l'évolution des tactiques
de botnet. Les vulnérabilités associées aux attaques de botnets incluent la possibilité de
mettre à jour les bots et de changer les codes pour échapper à la détection, créant ainsi des
botnets indétectables pouvant être constitués de millions de machines infectées [38].
Page 7 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
c). Cross-site script (XSS)
Les attaques de cross-site scripting (XSS) consistent à injecter des scripts malveillants
dans un site Web, qui sont ensuite exécutés par le navigateur de l'utilisateur, entraînant
potentiellement un accès non autorisé à des données sensibles ou une compromission du
système. Les vulnérabilités associées aux attaques XSS résultent souvent d'une validation
insuffisante des entrées utilisateur ou d'un échappement insuffisant de la sortie, permettant
aux attaquants d'injecter des scripts malveillants.
d). Force brute
Une attaque par force brute est un type de cyber-attaque visant un large éventail
d'appareils et de systèmes d'authentification. L'attaquant tente de deviner un mot de passe ou
une clé de chiffrement en essayant toutes les combinaisons possibles à l'aide d'outils et de
techniques logiciels pour automatiser le processus. Cette attaque est efficace contre les mots
de passe faibles ou les clés de cryptage facilement devinables.
1.5. Mécanismes de protection des systèmes informatiques
La protection des systèmes informatiques contre les cyber-menaces est un objectif
essentiel à l’ère numérique d’aujourd’hui. La cyber-sécurité est d’une importance capitale
pour la protection des informations et des données fournies par les clients, en particulier dans
le secteur bancaire où les technologies et les appareils numériques sont de plus en plus
utilisés [39].
L’importance de la sécurité numérique est une préoccupation primordiale pour tous les
individus, et les mesures à prendre après l’incident sont cruciales pour réduire les dommages,
rétablir le contrôle et identifier les acteurs d’attaque impliqués [40]. Il est essentiel de
comprendre les mécanismes de protection des systèmes informatiques pour prévenir les
attaques et minimiser le risque de cyber-menaces pour les fournisseurs et les clients. Ces
mécanismes de sécurité peuvent être utilisés pour assurer les propriétés de sécurité définies
dans une politique donnée. En fonction des attaques anticipées, différents moyens doivent
être appliqués pour satisfaire les propriétés souhaitées. Deux principales catégories de
mesures contre les attaques peuvent être identifiées, à savoir la prévention des attaques et leur
détection.
L’approche détective regroupe tous technique et méthode pour détecter immédiatement
les accès illégitimes aux systèmes informatique et la manipulation de données protégées.
Page 8 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
Cette approche basée généralement sur la modélisation du comportement normal du système,
considère certaine déviation par rapport a ce modèle comme une opération indésirable ou
attaques. L’approche préventive quant à elle, permet de prévenir ou de se défendre contre les
attaques avant qu'elles ne puissent réellement atteindre les objectifs de sécurité et affecter la
cible. Un outil important dans cette catégorie est le contrôle d'accès.
1.5.1. Contrôle d’accès au niveau de l’hôte
Le contrôle d’accès au niveau de l’hôte est un mécanisme de protection des systèmes
informatiques. Il s’agit de réguler l’accès à des hôtes ou appareils individuels. Diverses
méthodologies peuvent être utilisées pour mettre en œuvre le contrôle d’accès, y compris les
mots de passe, la vérification biométrique et les cartes à puce. En outre, des pare-feu et des
systèmes de détection et de prévention d’intrusions peuvent être utilisés pour renforcer le
contrôle d’accès, empêchant ainsi tout accès non autorisé aux hôtes [41].
1.5.2. Contrôle d’accès au niveau du réseau
Le contrôle d’accès au niveau du réseau est une autre approche importante pour protéger
les systèmes informatiques en limitant l’accès au réseau dans son ensemble. Les experts
mettent en œuvre des contrôles d’accès au réseau en utilisant des technologies comme les
pare-feu, les réseaux privés virtuels (VPN), les serveurs proxy, ainsi que les systèmes de
détection d’intrusions, pour la protection des réseaux. De plus, la segmentation du réseau en
segments plus petits, chacun avec son propre ensemble de règles d’accès, peut être une bonne
option pour améliorer la sécurité du réseau [42].
1.5.3. Autres contrôles d’accès
En plus du contrôle d’accès au niveau de l’hôte et du réseau, des mesures de sécurité
modernes telles que le contrôle d’accès dynamique, basé sur les rôles, basé sur les attributs,
discrétionnaire et obligatoire offrent plus de flexibilité, d’évolutivité et de capacités de
gestion d’accès contextuel.
D’autres mécanismes de sécurité englobent l’utilisation du chiffrement pour protéger les
données en transit et au repos. Le chiffrement implique la transformation de données en clair
en texte chiffré indéchiffrable. De ce fait, même si les attaquants accèdent au système, ils
auront des difficultés à accéder aux données. La mise en œuvre de protocoles sécurisés tels
que Secure Sockets Layer (SSL) et Transport Layer Security (TLS), qui fournissent un
Page 9 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
cryptage et une authentification de bout en bout, peut être un excellent moyen d’améliorer le
contrôle d’accès [43].
Les mesures de sécurité que les utilisateurs doivent appliquer dans une politique de
sécurité et mettre en œuvre lors de l'utilisation d'un système informatique, font partie de
l’approche préventive. Il est en fait presque impossible d'offrir une sécurité totalement sûre
contre chaque attaque potentielle en raison de la quantité croissante et de la complexité des
attaques ainsi que de l'évolution des systèmes informatiques. La stratégie détective, qui est le
deuxième niveau de protection, doit être mise en œuvre par une politique de sécurité afin de
répondre à cela.
L'utilisation de l'approche détective facilite l'identification rapide des intrusions
potentielles dans un système informatique. Cela permet de réagir rapidement et d'empêcher
toute interférence avec le fonctionnement normal de celui-ci. L'approche détective est l'une
des mesures de sécurité distinctes qui constituent la détection d'intrusion. Le processus
d'identification de l'activité non autorisée provenant ou se dirigeant vers un système
informatique par analyse comportementale est appelé détection d'intrusion.
1.6. Système de détection d’intrusions
Une intrusion est fondamentalement toute sorte d'activité illégale qui est effectuée par des
attaquants, pour endommager les ressources réseau ou les nœuds de capteurs. Un IDS est un
mécanisme permettant de détecter de telles activités illégales ou malveillantes. Il est
considéré comme une deuxième ligne de défense capable de protéger le réseau contre les
intrus [122]. C’est un ensemble de composants logiciels et matériels qui permet d’écouter le
trafic circulé de façon furtive dans le but de détecter des activités anormales qui pourraient
être assimilées à des intrusions.
Les systèmes de détection d’intrusions jouent un rôle central dans la protection des
systèmes contre les accès illicites et les actions malveillantes. Les principes fondamentaux et
les aspects généraux des IDS sont ancrés dans leur capacité à identifier les menaces à la
sécurité et à y réagir en temps réel [44] [45]. Les IDS sont conçus pour examiner le trafic et
les opérations du système pour détecter les indications d’accès non autorisé, d’utilisation
abusive ou d’autres activités malveillantes.
Page 10 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
1.6.1. Principes et généralités
Un système de détection d’intrusion est tout matériel ou logiciel chargé de surveiller un
actif contre toute effraction qui permet de compromettre les services de base de la sécurité
des informations [101]. Cependant,
un IDS peut être défini comme un mécanisme de
surveillance pour détecter les menaces internes ou externes qui affectent le bon
fonctionnement du système. La principale fonction de l'IDS est la surveillance des activités
des utilisateurs et le comportement du réseau sur différentes couches [123]. La précision de la
détection d'intrusion est généralement mesurée en termes d'erreurs positives (fausses alarmes)
et d'erreurs négatives (attaques non détectées). La performance d'un IDS augmente en
augmentant le taux de détection précis tout en minimisant les erreurs positives et négatives.
Un IDS se compose principalement de trois parties essentielles à savoir : (1) Le module de
surveillance (Monitoring), chargé principalement de la surveillance du trafic, des évènements
internes au sein du réseau, ainsi que l'utilisation des ressources. (2) Le module d'analyse et
de détection, considéré comme le noyau de l'IDS qui détermine si le flux d’événements
contient ou pas des éléments ou des caractéristiques d’une activité malveillante. Cette
décision est prise à partir d'une analyse du comportement et des activités issues. Et (3)
l'alarme ; Activation de l'alarme en cas d'une détection d'une intrusion.
1.6.2. Différentes classification
Les systèmes de détection d’intrusions sont classés en différentes catégories en fonction
de divers critères, notamment leur méthode de détection, leur emplacement dans le réseau,
leur fonctionnement et leur mode de déploiement. Chacune de ces catégories offre ses
propres avantages et inconvénients. Dans ce qui suit, nous présentons les différentes facettes
selon lesquelles un IDS peut être classé. Pour chaque classification, un tableau récapitulatif
représentant l’ensemble des avantages et des inconvénients sera présenté dans la section ... de
l’annexe.
Page 11 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
a). Selon l’approche de détection
Le modèle créé dans l'étape d'analyse est une structure de données qui décrit, par un
ensemble de caractéristiques (attributs), un profil donné. A partir de celui-ci, nous
distinguons deux types d'approches7 de détection: l'approche par scénarios.
 Approche par scénarios
L'approche par scénarios (appelée aussi, à base de signature/connaissances) effectue
l'analyse des événements capturés en comparant ces derniers avec un modèle décrivant les
comportements anormaux d'un ensemble d'intrusions connues au préalable. Si une relation
subsiste, le système classe l'événement comme étant une intrusion [102].
Ce type d'approche est très efficace pour la détection d'intrusions qui sont déjà décrites
dans le modèle de référence. Cependant, l'approche par scénarios est jugée être dépendante
du type de système informatique surveillé. De plus, elle présente des limites quant à la
détection des nouvelles intrusions qui ne sont pas connues au préalable. Une solution à ce
problème réside dans la mise à jour régulière du modèle de référence d'une manière manuelle,
chose qui n'est pas facilement réalisable, ou bien d'une manière automatique par le biais des
méthodes d'apprentissage supervisé [103]. Cette dernière n'est pas facile aussi car elle
nécessite l'utilisation de données d'apprentissage étiquetées manuellement par des experts de
sécurité. Malgré ces lacunes, les IDS utilisant l'approche par scénarios sont les plus
commercialisés, dû à leur efficacité pour la détection d'intrusions connues avec un minimum
de fausses alertes.
 Approche comportementale
A l’opposé de l’approche par scénario, l’approche comportementale (également appelé
IDS à base d’anomalies) permet d'analyser des événements capturés par comparaison de ces
derniers avec un modèle décrivant les comportements normaux du système surveillé. L’écart
par rapport au comportement notoire est appelé anomalie, tandis que le profil est le
comportement normal attendu. Ainsi, toute déviation (i.e. dépassement d’un seuil spécifié)
par rapport aux comportements normaux définis est considérée comme une intrusion et vice-
versa.
7
Afin d’assurer un IDS avec un minimum de défauts, plusieurs solutions hybrides utilisent la combinaison de
ces deux approches. Les approches hybrides appliquées ont prouvé leur efficacité en termes de détection
d’intrusions.
Page 12 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
L'approche comportementale peut être statique ou dynamique [103]. Elle est statique
lorsque le comportement est invariable (e.g. les séquences d'appels systèmes). Elle est
dynamique lorsque le comportement est variable. Dans le deuxième type, le comportement
dynamique correspond à des profils définissant les activités habituelles des usagers ou
l'historique d'utilisation des réseaux et machines.
Ce mécanisme est apparu comme étant une solution au problème posé par l'approche par
scénarios, et qui concerne la détection des attaques nouvelles et imprévues. Elle permet de
détecter les intrusions indépendamment du type du système, des vulnérabilités du système, de
l'environnement et du type d'intrusions, ce qui permet d'améliorer le taux de détection [104].
Cependant, son inconvénient majeur est l'augmentation du taux des fausses alertes. Cela est
dû à la difficulté de définition des comportements normaux et aux changements dynamiques
des profils définis dans le modèle. Un autre inconvénient est que ce type d'approche ne
permet pas de donner des informations sur l'attaque détectée ce qui rend la tâche ultérieure de
diagnostic difficile.
Note : En fait, une approche supplémentaire dite à base de
spécifications, et dérivée de l’approche comportementale de
façon directe [105]. La différence est que les règles sont
définies manuellement pour chaque spécification par un expert,
ce qui diminue considérablement le taux des faux positifs. De
plus, seuls les comportements anormaux sont détectés, au lieu
de détecter leur éventuel effet [106].
b). Selon l'emplacement surveillé
Selon la source des données à surveiller, un IDS est classé en trois catégories: IDS
machine (ou HIDS: Host-based Intrusion Detection System), IDS réseau (ou NIDS: Network-
based Intrusion Detection System) et IDS hybride.
 Système de détection basé sur la machine (HIDS)
Les HIDS visent à surveiller une seule machine (hôte) qui peut être un ordinateur
personnel, un smartphone, un serveur ou tout autre équipement informatique. Son rôle
consiste à analyser8 tous les événements de sécurité qui se passent sur cette machine. Il
8
Bien que le HIDS soit indépendant du réseau, il peut cependant effectuer une simple et concise analyse des
paquets réseaux arrivants vers la machine cible.
Page 13 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
permet de surveiller les menaces qui peuvent affecter un système de plusieurs manières,
notamment l’accès et la modification des fichiers système, et l’occupation inutile et
permanente des ressources [107].
Les HIDS étaient premièrement introduits en réponse aux concepts de traces d'audit 9.
L'utilisation de fichiers d'audit pour la détection des intrusions attaquant une machine, souffre
cependant de plusieurs faiblesses. En particulier, les fichiers d'audit contenant des données
brutes ne sont pas facilement réalisables, et souvent difficile à interpréter [108]. A cet effet,
les chercheurs ont pensé à l'analyse des appels systèmes générés par le système d'exploitation
lors de l'exécution d'un programme. L'hypothèse soutenue dans ce contexte est que seul le
programme en cours d'exécution pourra affecter le système et que toute intrusion doit
forcément laisser des traces dans les appels systèmes exécutés par le système d'exploitation.
 Système de détection basé sur le réseau (NIDS)
Les NIDS visent à surveiller un réseau d'objets informatiques (PCs, équipements
d’interconnexion, etc.) en analysant les paquets entrants et sortants du réseau. De plus, ce
type d’IDS est destiné à détecter l’intrusion dans les données transmises par le sous-réseau
aux utilisateurs rattachés. En d’autres termes, les NIDS permettent également d'analyser les
paquets circulant à l'intérieur du réseau surveillé. Ainsi, les données collectées pour les IDS
réseau peuvent être de différents niveaux de granularité.
Généralement, ces systèmes intègrent un module qui facilite la tâche de collecte des
paquets à partir du réseau. Les données collectées à partir des NIDS sont de grandeur
différente à celle des HIDS en termes de volume, puisqu’elles sont décrites par un grand
nombre d'attributs de différents types [109].
 Système de détection hybride (HybridIDS)
Les IDS hybrides constituent une hybridation entre les deux types d’IDS (voir les HIDS
et les NIDS). Cette hybridation permet aux NIDS d’analyser les paquets circulant dans tout le
réseau surveillé alors que chaque HIDS est dédié à surveiller une seule machine dans le
réseau et cela en analysant les paquets qui lui sont destinés [110]. D’une façon formelle, Les
IDS hybrides contiennent des agents qui jouent le rôle de communication entre HIDS et
NIDS. Ces agents peuvent être soit des agents mobiles qui visitent chaque hôte et effectuent
9
Traces d'audit « logs », font référence aux séquences chronologiques des événements de sécurité, après les
avoir collectées et stockées dans un fichier dit journal d'audit.
Page 14 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
le processus de détection, soit des agents centraux qui parcourent l’ensemble du réseau pour
détecter les anomalies de trafic.
Pour optimiser le rendement du système, les IDS hybrides sont formés en se basant sur le
type de l'approche adoptée par chacun des IDSs qui les constitue. Cela dit, les IDS hybrides
adoptent une combinaison entre les deux types d'approches précédemment parlés (voir
l’approche par scénario, et l’approche comportementale).
c). Selon l’architecture
Un IDS est une combinaison de plusieurs agents (modules) assurant les tâches de l'audit,
l'analyse et la réponse aux intrusions. Selon l'organisation fonctionnelle de ces systèmes, un
IDS peut avoir l’une des architectures suivantes.
 Système de détection autonome
Chaque agent d’une telle architecture possède son propre moteur de détection d’intrusion,
qui détecte les intrusions pour ce nœud uniquement. Les données collectées par cet agent
spécifique sont utilisées pour comparer avec l’activité malveillante lors de la prise de
décision. Ce type d’architecture est robuste grâce au fonctionnement indépendant de chaque
IDS.
 Système de détection centralisé
La tâche d'audit est assurée par plusieurs systèmes, responsables de la collecte des
données de différentes ressources. Ils représentent les agents de surveillance « Monitoring
Agents ». Les données collectées sont envoyées à un seul système central dit « manager »,
responsable de l'analyse et de la réponse aux intrusions. Ces données sont ensuite analysées,
et si une tentative d’intrusion est découverte, elle est bloquée par l’action de l’IDS associé.
Les autres IDS ne sont pas impliqués dans cette décision.
 Système de détection distribué (coopératif)
La tâche d'audit est assurée par plusieurs agents de surveillance subordonnés. L'analyse et
la réponse aux intrusions sont distribuées entre ces agents et le module central (le manager).
Leur fonction est de détecter les intrusions en surveillant les données d’audit locales. De ce
Page 15 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
fait, l’identification d’une intrusion repose sur la décision collaborative de tous les IDS
associés. Un point qui différencie cette architecture de la précédente est que les résultats
d’audit sont partagés avec les nœuds voisins. Cela aide à fournir un mécanisme de détection
distribué et coopératif pour la résolution des attaques [111]. Ce mécanisme est généralement
utilisé dans une situation où un seul IDS n’est pas entièrement sûr de l’occurrence d’une
activité intrusive.
Note : À l'origine d’une architecture distribuée, on trouve
l’architecture à base d’agents mobiles. Issue du concept
distribué, cette variante dispose d’agents avec des logiciels
spécialisés et peuvent se déplacer librement aux différents
emplacements, pour visiter chaque nœud du réseau [112]. Tous
les nœuds sont censés installer un logiciel agent, et par lequel,
ils ont la capacité de corréler les activités suspectes trouvées
dans les nœuds surveillés.
 Système de détection hiérarchique
L’architecture hiérarchique divise le réseau en clusters (groupes) multicouches où
chaque cluster a peu de nœuds (agents) avec un manager central. Là aussi, la tâche d'audit est
assurée par plusieurs agents de surveillance, mais qui travaillent avec différents managers.
Les nœuds qui collectent les données à partir d'une machine sont liés à un manager machine
« Host Manager ». Les nœuds qui collectent les données à partir du réseau sont liés à un
manager réseau « Network Manager ». Chaque manager joue un rôle de premier plan et a
plus de responsabilités que les nœuds ordinaires. Un IDS plus sophistiqué est installé sur
l’entête du cluster. Des IDS ordinaires et légers sont installés sur les nœuds restants du
cluster.
Cette architecture réduit le risque d’attaques passives telles que les écoutes clandestines.
Contrairement à l’architecture distribuée, cette architecture ne nécessite pas de coopération et
le surcoût de communication est réduit.
d). Selon la fréquence d’utilisation
La fréquence d'utilisation d'un IDS signifie le nombre de fois que le système est lancé
pour analyser les événements capturés. Selon ce critère, nous distinguons deux types de
Page 16 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
détection ; la détection en temps réel (continue / online) et la détection en batch
(périodique/offline).
 Détection en temps réel (continu/ enligne)
Dans ce type de système, la détection de l'intrusion doit se faire au moment de sa
production. Cela est réalisé en lançant la tâche d'analyse plusieurs fois à intervalles de temps
très réduits (e.g. chaque seconde). L'avantage de la détection en permanence est qu'elle
permet de détecter l'intrusion rapidement (action immédiate) ce qui l'empêchera de se
propager dans le système et causer d'éventuels dégâts, assurant la précision et la rapidité du
traitement en même temps [113] [114].
 Détection par lots (périodique/ hors-ligne)
Dans ce type de système, la tâche d'analyse est lancée périodiquement (e.g. chaque
semaine). Ainsi, la détection de l'intrusion ne se fait pas au moment de sa production, ce qui
peut mettre le fonctionnement du système face au risque intrusif. L’outil de détection prend
une vue d’ensemble du système ou du réseau connecté et l’analyse pour la détection
d’intrusion. Si une intrusion est détectée, elle est empêchée de nuire au réseau. D’autre part,
si l’intrusion n’est pas détectée, il attend la prochaine période à venir, pour en apercevoir.
La détection en batch peut être utilisée dans des environnements de simulations qui ont
pour objectif la modélisation des signatures d'attaques pour la création des bases de
signatures. En outre, elle constitue une alternative pour les chercheurs afin d'évaluer leurs
systèmes [114].
e). Selon la réponse aux événements
A l'issue de la phase d'analyse, le système doit réagir à l'ensemble des intrusions
détectées. Selon que le système déclenche des traitements ou non, nous distinguons deux
types de systèmes ; les IDS passifs et les IDS actifs.
Page 17 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
 Système actif
Un IDS actif détecte les menaces dans un système et répond activement en bloquant /
prévenant les menaces détectées. Si une attaque apparaît, ce type10 d’IDS exécute un plan
d'actions dans le but d'entraver cette attaque. Le plan d'action peut porter sur l'attaquant du
système (supprimer ses outils, supprimer sa plateforme, etc.) ou bien sur le système
informatique surveillé lui-même (arrêter les processus affectés par l'attaque, arrêter la
connexion réseau, etc.).
 Système passif
Un IDS passif surveille uniquement le système en silence et ne joue aucun rôle direct
dans la prévention de la menace. Si une attaque apparaît, ce type d’IDS ne déclenche aucune
action pour bouleverser le plan de cette attaque. Au lieu de cela, il se contente d'envoyer un
signal à l'administrateur de sécurité, ou toute autre entité responsable de bloquer la menace
[115].
f). Selon la source de données
Les outils de détection d’intrusions ne détectent pas directement les actions intrusives,
mais leurs manifestations lors d’interactions avec les entités du système d’informations. Les
capteurs observent ces interactions par le biais des sources de données présentées ci-dessous.
La source de données utilisée pour détecter les intrusions est une caractéristique essentielle
des IDS. On distingue trois catégories de sources : le trafic réseau, les audits système et les
audits applicatifs.
 Données du système d'exploitation (audit système)
Ce sont les données de trace d'audit produites par le système d'exploitation d'un hôte
(audit système). Dans ce cas, les IDS analysent des données d’audit produites par le système
d’exploitation des hôtes sur lesquels ils sont installés. Ils sont généralement utilisés dans le
cas où la vérification se fait de temps en temps [116]. L'avantage principal des données
d'audit du système est la précision d'information. Sur cette base, un système de détection peut
réduire le nombre de faux positifs, tout en fournissant des informations détaillées concernant
les circonstances de l'attaque [117].
10
Etant donné que l’IDS actif lui-même empêche la menace après sa détection sans aide extérieure, il est donc
également appelé système de détection et de prévention des intrusions (IDPS). Les IDPS sont largement utilisés
pour protéger les systèmes en temps réel.
Page 18 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
Malheureusement, le volume d’événements généré par les systèmes d’audits peut être
considérable, ce qui peut avoir un impact très important sur les performances de la machine
surveillée. De plus, la couverture de l’IDS est limitée à un seul hôte, si bien que les
administrateurs de sécurité sont amenés à déployer plusieurs sondes, ce qui rend complexe la
tâche d’administration [117].
 Données du flux réseau (audit réseau)
Ce sont les données du trafic réseau, représentées par des flux de paquets. Ces IDSs
utilisent les capteurs pour observer le réseau, et collecter les paquets de données qui circulent
sur ce réseau afin d'effectuer une analyse pour détecter les intrusions qui se manifestent par
une interaction réseau entre l’attaquant et la victime [118].
L’avantage majeur de cette source de données réside avant tout dans sa simplicité
d’utilisation vis-à-vis de son environnement [119]. A condition qu’une sonde soit positionnée
à un endroit stratégique. Une seule sonde peut surveiller l’activité des utilisateurs dans
l’ensemble d’un réseau.
 Données applicatives
La troisième catégorie de source de données est constituée des audits applicatifs. Les
données à analyser sont produites directement par une application. (e.g. les fichiers logs
générés par: un serveur web, ftp, base de données…etc.). Un log d'application peut fournir
des informations au profit d'un environnement distribué.
L’avantage de cette approche est que les données produites sont très synthétiques ; elles
sont sémantiquement riches et leur volume est modéré, ainsi les IDS basés audit applicatif
peuvent fonctionner souvent dans les environnements cryptés. Malheureusement, l’analyse
faite par les sondes peut ainsi être plus complexe. Par exemple, une requête HTTP à un
serveur web et sa réponse donne lieu à une séquence de plusieurs paquets IP au niveau du
réseau, alors qu’elle ne donne lieu qu’à une seule ligne dans le fichier d’audit de ce même
serveur web [119] [120].
1.6.3. Limitations des systèmes traditionnels
Comme tout autre système, les systèmes conventionnels de détection d’intrusion
présentent de nombreuses lacunes [121], ce qui les rend moins efficaces dans l’identification
et l’atténuation des cyber-menaces contemporaines. D’une part, ils présentent un rapport
Page 19 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
entre le taux des fausses alarmes élevé et les attaques non détectées. D’autre part, leur
dépendance aux règles et signatures statiques représente un inconvénient important, par
lequel peuvent être contournées sans effort par les cyber-adversaires. En outre, ces IDS
traditionnels exigent souvent des ressources, ce qui pose des défis 11 dans leur déploiement et
leur gestion au sein d’infrastructures de réseau étendues. L’intégration d’algorithmes
d’apprentissage machine a été suggérée comme un remède potentiel à ces problèmes, compte
tenu de leur capacité à s’adapter aux menaces dynamiques et à améliorer la précision de
détection [46] [47].
Les systèmes de détection d’intrusions doivent être en parfaite harmonie avec l’évolution
et la complexité des systèmes et les nouvelles technologies informatiques comme les réseaux
MANET, la Data mining et le Cloud Computing a titre d’exemples. Ceci dit, un IDS ne doit,
dans un aucun cas, manquer de détecter une intrusion. Or, il faut admettre qu'il est plutôt
difficile de satisfaire à cette exigence car il est presque impossible d'avoir une connaissance
globale des attaques passées, présentes et futures. Bien que les IDS sont très efficaces dans la
détection des activités malveillantes et des tentatives d’outrepasser les autres mécanismes de
sécurité, avec l’évolution des technologies réseaux caractérisés par une grande dynamique de
changement et des mutations rapides, les IDS classiques ont une tache très complexe. Ils ne
peuvent faire face aux problèmes de pertinence, et de gérances car les vitesses de transfert
sont trop élevées ainsi que la détection dans un environnement engendrent un grand nombre
d’attaques.
11
Ces défis lesquels nous essayerons de surmonter, seront l’objet de notre étude dans le chapitre 3. Cependant, il
est utile de concevoir un système qui soit plus généralisable en adoptant un paradigme de détection
collaborative.
Page 20 sur 20CHAPITRE 1 : Principes fondamentaux de la sécurité informatique
PARTIE I
1.7. Conclusion
Dans ce chapitre, nous avons examiné les différents concepts de base concernant la
sécurité informatique. Dans un premier temps, nous avons présenté l’importance de la cyber-
sécurité dans l’environnement organisationnel, ainsi que les défis auxquels sont confrontées
les organisations. Par la suite, nous avons exposé les problèmes (exprimés en vulnérabilités)
et leurs différentes attaques relatives. Nous avons également étudié les mécanismes de
protection des systèmes informatiques, en mettant l'accent sur les principes et les
classifications des systèmes de détection d'intrusions (IDS), tout en soulignant leurs
limitations. Il est crucial pour toute organisation de prendre en compte ces éléments lors de la
conception de son architecture informatique afin de garantir une protection adéquate contre
les menaces cybernétiques. A la fin de ce chapitre, nous espérons avoir recueilli de bonnes
connaissances pré-requises afin d’entamer notre recherche.
Page 21 sur 20 """

ch2 = """ CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
Sommaire
Chapitre 2 : Principes Fondamentaux sur l’Intelligence Artificielle
2.1. Introduction................................................................................................... 2
2.2. L’intelligence artificielle .............................................................................. 2
2.2.1. Définition et objectifs ........................................................................ 3
2.2.2. L’apprentissage machine ................................................................... 3
a). Apprentissage profonds ....................................................................... 3
b). Apprentissage par transfert .................................................................. 4
2.3. Methodes d’apprentissage profond............................................................... 4
2.3.1. Techniques prédictives ...................................................................... 5
a). Réseau de neurones profond (FNN) .................................................... 5
b). Réseau de neurones récurent (RNN) ................................................... 5
2.3.2. Techniques génératives ..................................................................... 5
a). Réseau générative (GAN) .................................................................... 5
b). Auto encoder ........................................................................................ 6
2.4. Facettes d’apprentissage ............................................................................... 6
2.4.1. Selon le mode de supervision ............................................................ 6
a). Apprentissage supervise ...................................................................... 6
b). Apprentissage non-supervise ............................................................... 6
c). Apprentissage par renforcement .......................................................... 7
2.4.2. Selon l’emplacement des données..................................................... 8
a). Apprentissage centralisé ...................................................................... 8
b). Apprentissage distribué (collaboratif) ................................................. 8
2.4.3. Limitations de l’apprentissage traditionnel ....................................... 8
2.5. Apprentissage federe .................................................................................... 9
2.5.1. Définition et généralités .................................................................. 10
2.5.2. Avantages à l’apprentissage traditionnel (centralisé) ..................... 10
2.5.3. Processus d’apprentissage distribué ................................................ 11
2.5.4. Classification de l’apprentissage fédéré .......................................... 12
a). Selon l’architecture ............................................................................ 12
b). Selon la distribution des données ...................................................... 13
c). Selon le model d’apprentissage ......................................................... 14
a). Attaques d’empoisonnement ............................................................. 17
b). Attaques par porte dérobée ................................................................ 17
2.6. Conclusion .................................................................................................. 18
Page 1 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
CHAPITRE 2
PRINCIPES FONDAMENTAUX
SUR L’INTELLIGENCE ARTIFICIELLE
_________________________
2.1. Introduction
Le présent chapitre explore les concepts avancés de l'intelligence artificielle (IA), en
commençant par définir l'IA et ses objectifs, puis se concentre sur l'apprentissage machine, en
particulier l'apprentissage profond et l'apprentissage par transfert. Les méthodes
d'apprentissage profond sont examinées en détail, incluant les techniques prédictives telles
que les réseaux de neurones profonds (FNN), ainsi que les techniques génératives comme les
réseaux génératifs adversaires (GAN). Ensuite, nous aborderons les différentes facettes de
l'apprentissage, notamment selon le mode de supervision et selon l'emplacement des données.
Nous discuterons également des limitations de l'apprentissage traditionnel avant de se
concentrer sur l'apprentissage fédéré. Ce dernier est défini, et ses avantages par rapport à
l'apprentissage centralisé sont présentés. Le processus d'apprentissage distribué, incluant
l'agrégation centrale, est décrit, ainsi que les différentes classifications de l'apprentissage
fédéré basées sur l'architecture, la distribution des données et le modèle. Enfin, le chapitre
conclut en abordant les défis et les préoccupations liés à l'apprentissage fédéré, notamment
les attaques d'empoisonnement et par porte dérobée.
2.2. L’intelligence artificielle
L’intelligence artificielle (IA) est un domaine en évolution rapide qui transforme notre
monde de nombreuses façons. Des recommandations de films et des assistants vocaux à la
conduite autonome et aux diagnostics médicaux automatisés, l’IA touche de plus en plus la
vie des gens. La technologie a connu des progrès significatifs au cours des cinq dernières
années, avec des outils d’IA tels que les contrôles grammaticaux, l’auto-complétion,
l’organisation et la recherche automatiques de photos personnelles et la reconnaissance
vocale devenant monnaie courante.
L’IA transforme chaque étape de la vie, intégrant
l’information, analysant les données et améliorant la prise de décision.
Page 2 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.2.1. Définition et objectifs
L’IA est une technologie qui permet aux machines d’imiter diverses compétences
humaines complexes. Elle implique généralement le développement de machines capables
d’effectuer des tâches qui nécessiteraient normalement l’intelligence humaine. Les objectifs
traditionnels de la recherche en IA comprennent le raisonnement, la représentation des
connaissances, la planification, l’apprentissage, le traitement du langage naturel, la perception
et le soutien à la robotique. L’IA devrait continuer à avoir un impact sur nos vies au cours des
prochaines années, avec des applications potentielles dans des domaines tels que la
découverte de médicaments, la prise de décision et l’assistance de base.
2.2.2. L’apprentissage machine
L’apprentissage automatique (ML), un sous-ensemble de l’intelligence artificielle (IA),
dote les systèmes de la capacité d’augmenter et d’affiner de manière autonome leurs
performances à partir de l’apprentissage expérientiel.ML est défini comme "le domaine
d’étude qui permet aux ordinateurs d’apprendre sans être explicitement programmés" [50].
Cela implique l’utilisation d’algorithmes qui apprennent et font des prédictions ou des
décisions basées sur des données. Les algorithmes de ML peuvent être classés en trois
catégories : l’apprentissage supervisé, l’apprentissage non supervisé et l’apprentissage par
renforcement, chacun conçu pour traiter des types de problèmes distincts.
a). Apprentissage profonds
L’Apprentissage profond (Deep Learning), un sous-ensemble du ML, se concentre sur
les réseaux neuronaux avec de nombreuses couches (donc "profondes"). Ces réseaux de
neurones profonds sont conçus pour imiter la façon de travailler du cerveau humain, traitant
des données en couches pour extraire des caractéristiques profondes de l’entrée. DL est
largement appliqué dans divers domaines d’application tels que la santé, la reconnaissance
visuelle, l’analyse de texte, la cybersécurité et bien d’autres [51][52][54].
L’importance du deep learning réside dans sa capacité à extraire automatiquement les
fonctionnalités des données, permettant un traitement plus précis et efficace. De plus, DL
améliore les performances des modèles d’apprentissage automatique traditionnels en
fournissant un cadre d’apprentissage plus robuste et flexible. Les algorithmes DL utilisent de
grandes quantités de données et de puissance de calcul pour apprendre des modèles
complexes, réalisant des avancées significatives dans des domaines tels que la reconnaissance
d’images, le traitement du langage naturel et la conduite autonome [51].
Page 3 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
Bien que le ML et le DL soient des sous-ensembles de l’intelligence artificielle, la
principale différence réside dans leurs capacités. Les algorithmes ML apprennent
généralement des relations linéaires, tandis que les algorithmes DL apprennent des modèles
hiérarchiques, ce qui leur permet de traiter des données avec des structures complexes. DL est
donc souvent préféré pour les tâches qui impliquent des données non structurées telles que
des images et du texte.
b). Apprentissage par transfert
L’apprentissage par transfert est une approche populaire de l’apprentissage où un modèle
développé pour une tâche est réutilisé comme point de départ pour un modèle sur une
deuxième tâche. C’est une technique qui raccourcit le temps nécessaire pour développer et
améliorer les modèles en exploitant les modèles trouvés dans des tâches similaires. Cela
accélère non seulement le processus de entrainement, mais nécessite également moins de
données, ce qui est un avantage significatif dans les domaines où l’acquisition de données
étiquetées est coûteuse ou longue.
En outre, il peut conduire à une erreur de généralisation plus faible et une meilleure
performance du modèle, en particulier lorsque les tâches initiales et cibles sont étroitement
liées. Cependant, l’apprentissage par transfert a aussi ses inconvénients, son efficacité peut
être limitée si les tâches initiales et cibles sont très différentes et partagent peu de points
communs. Il peut également conduire à un transfert négatif si les connaissances transférées
sont trompeuses pour la nouvelle tâche. Il s’agit de modèles formés sur de grands ensembles
de données de référence, tels que ImageNet pour les tâches de classification d’images et
BERT pour les tâches de traitement du langage naturel. Ces modèles pré-entraînés capturent
des caractéristiques générales ou des représentations des tâches originales, qui peuvent
ensuite être affinées ou adaptées pour une tâche spécifique. Cette approche s’est avérée
efficace dans divers domaines, améliorant considérablement la performance des modèles sur
les tâches avec des données étiquetées limitées[28].
2.3. Méthodes d’apprentissage profond
Après avoir défini l'apprentissage profond comme une sous-discipline de l'apprentissage
machine qui utilise des réseaux de neurones artificiels pour modéliser et résoudre des
problèmes complexes, nous nous penchons sur les diverses méthodes qui composent ce
domaine. Les techniques d'apprentissage profond peuvent être divisées en deux catégories
principales : les techniques prédictives et les techniques génératives.
Page 4 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.3.1. Techniques prédictives
Les techniques d’apprentissage prédictives visent à générer de nouvelles données à partir
de modèles existants. Ces méthodes permettent de traiter et de comprendre des données
complexes, ouvrant ainsi la voie à des applications innovantes et puissantes de l'intelligence
artificielle. Dans ce qui suit, nous exposant les modèles les plus connus.
a). Réseau de neurones profond (FNN)
Les FNNs sont le type le plus simple de réseau de neurones artificiels. L’information ne
circule que dans une seule direction, de la couche d’entrée , en passant par les couches
cachées jusqu’à la couche de sortie, sans boucles de rétroaction. Le rendre simple et efficace
pour de nombreuses tâches telles que la classification des images, la reconnaissance vocale et
le traitement du langage naturel [52][54].
b). Réseau de neurones récurent (RNN)
Les RNNs sont un type de réseau de neurones conçu pour traiter des données
séquentielles. Par conséquent, ils peuvent se souvenir des informations des étapes de temps
précédentes, ce qui les rend idéales pour les tâches d’apprentissage profond telles que la
prédiction de séries chronologiques et le traitement du langage naturel. La mémoire à long
terme (LSTM) et les unités récurrentes synchronisées (GRUs) sont deux types de Réseaux de
neurones récurrents particulièrement efficaces pour les tâches impliquant des dépendances à
long terme dans les données [52][54].
2.3.2. Techniques génératives
Les techniques génératives, en revanche, se concentrent sur la création de nouvelles
données à partir de modèles appris. Ces méthodes permettent de générer des échantillons qui
ressemblent à ceux du jeu de données original, ouvrant ainsi des possibilités pour divers
applications telles que la création d'images ou de texte.
a). Réseau générative (GAN)
Les GANs sont une classe d’algorithmes DL qui se composent de deux réseaux : un
générateur apprend à générer de nouveaux échantillons de données similaires à l’ensemble de
données donné et un discriminateur qui tente de distinguer ces données générées des données
réelles. La concurrence entre ces deux réseaux permet aux GAN de générer des données très
réalistes. Ils sont largement utilisés dans l’apprentissage profond pour des tâches telles que la
génération d’images, la génération vidéo et la génération de texte [52].
Page 5 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
b). Auto encoder
Les auto encodeurs sont un type de réseau de neurones conçu pour apprendre des
représentations efficaces des données. Ils fonctionnent en codant l’entrée dans une
représentation compressée, puis en décodant cette représentation dans le format original [52].
Les AEs sont couramment utilisés pour des tâches telles que la détection d’anomalies, la
réduction de la dimensionnalité et la modélisation générative.
2.4. Facettes d’apprentissage
L'apprentissage machine représente une discipline clé de l'intelligence artificielle, offrant
des méthodes sophistiquées pour extraire des connaissances à partir de données. Pour mieux
comprendre et organiser ce domaine vaste et complexe, il est essentiel d'explorer ses
différentes classifications, permettant de classifier les techniques d'apprentissage en fonction
de divers critères.
2.4.1. Selon le mode de supervision
L'une des caractéristiques fondamentales de l'apprentissage machine réside dans la
manière dont les données sont utilisées pour entraîner les modèles. Ce critère est souvent
classifié selon le mode de supervision, qui définit la nature et la disponibilité des étiquettes ou
annotations associées aux données d'entraînement.
a). Apprentissage supervise
L’apprentissage supervisé est un type d’apprentissage automatique où un algorithme
apprend à partir de données d’entraînement étiquetées pour trouver la relation entre les
caractéristiques d’entrée et les étiquettes de sortie. , et fait des prévisions fondées sur ces
données. Un avantage majeur de l’apprentissage supervisé est sa capacité à fournir une
précision et une précision élevées, tandis que ses principaux inconvénients sont la nécessité
d’une intervention humaine pour étiqueter les données et nécessite une quantité substantielle
de données étiquetées. Les algorithmes populaires incluent des algorithmes de classification
comme les arbres de décision et des algorithmes de régression comme la régression linéaire.
L’apprentissage supervisé a de vastes applications, notamment dans la reconnaissance
d’images et la détection de pourriels [52][56].
b). Apprentissage non-supervise
L’apprentissage non supervisé, d’autre part, est un type d’apprentissage automatique où
l’algorithme est formé sur des données non étiquetées pour découvrir des modèles, des
Page 6 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
relations ou des structures dans les données sans aucune connaissance préalable ou
orientation. Son principal avantage est de découvrir des modèles cachés ou des groupes de
données sans intervention humaine. Cependant, le manque de données étiquetées peut rendre
difficile l’évaluation de la performance des algorithmes d’apprentissage non supervisés, la
précision est également inférieure à celle de l’apprentissage supervisé. Les techniques
d’apprentissage non supervisées les plus courantes comprennent le regroupement (p. ex., k-
moyennes, regroupement hiérarchique) et l’association comme Apriori. L’apprentissage non
supervisé est largement utilisé dans la segmentation de la clientèle, la détection des
anomalies, les systèmes de recommandation et l’analyse exploratoire des données[52][54].
 Apprentissage semi-supervisé
L’apprentissage semi-supervisé est une sorte d’apprentissage qui utilise une petite
quantité de données étiquetées et une grande quantité de données non étiquetées tout au long
du processus de entrainement. Ce type d’apprentissage est avantageux parce qu’il peut
atteindre une plus grande précision que l’apprentissage non supervisé en utilisant des données
étiquetées et peut traiter de plus grandes quantités de données que l’apprentissage supervisé
en utilisant des données non étiquetées. Cependant, un inconvénient est qu’il peut produire
des résultats moins précis que l’apprentissage supervisé [48]. Les réseaux antagonistes
génératifs (GANs) sont un type populaire d’algorithme d’apprentissage semi-supervisé qui
peut générer de nouveaux échantillons de données similaires aux données d’entraînement.
L’apprentissage semi-supervisé a des applications dans de nombreux domaines, y compris
dans la reconnaissance vocale et la classification de contenu Web.
c). Apprentissage par renforcement
L’apprentissage par renforcement est un type d’apprentissage automatique inspiré par la
psychologie comportementale, où un agent apprend à prendre des décisions en interagissant
avec un environnement et en recevant des récompenses ou des pénalités pour ses actions.
Cette approche est avantageuse car elle permet d’apprendre des comportements complexes et
de prendre des décisions dans des environnements dynamiques. Cependant, il a des limites
car il nécessite une fonction de récompense bien définie et peut être difficile à concevoir et à
former [49]. Certains algorithmes populaires incluent Q-learning et Deep Q-learning, qui
utilisent des valeurs Q pour estimer la récompense future attendue d’une action particulière
dans un état donné. L’apprentissage par renforcement est largement utilisé dans la robotique,
le jeu, les véhicules autonomes et les systèmes de recommandation, où l’objectif est
Page 7 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
d’apprendre une politique optimale grâce à l’expérience et à la rétroaction de
l’environnement.
2.4.2. Selon l’emplacement des données
Il s’agit d’un critère d’apprentissage qui fait référence à l’impact de la localisation des
données sur le processus d’apprentissage. De plus, l’emplacement du stockage et du
traitement des données peut avoir un impact sur l’efficacité et l’efficience d’un modèle
d’apprentissage.
a). Apprentissage centralisé
L’apprentissage centralisé des données, une méthodologie conventionnelle, implique
l’agrégation et le traitement de toutes les données à un seul emplacement ou serveur. Cette
technique confère l’avantage de posséder un ensemble de données harmonisé et cohérent,
améliorant ainsi la précision et la fiabilité des modèles résultants. Cependant, cela soulève
également des préoccupations concernant la confidentialité et la sécurité des données, ainsi
que les coûts et le temps élevés associés au transport des données.
b). Apprentissage distribué (collaboratif)
D’autre part, l’apprentissage distribué des données est une approche plus moderne qui
permet aux données de rester à leur emplacement d’origine. Dans cette méthode, plusieurs
modèles locaux sont formés sur leurs données respectives, et leurs apprentissages sont
partagés et combinés pour former un modèle global. Cette approche répond aux
préoccupations en matière de protection de la vie privée liées à l’apprentissage centralisé et
réduit le besoin de transport des données. Cependant, il nécessite des algorithmes
sophistiqués pour assurer la cohérence et la précision du modèle global. Elle nécessite
également des mécanismes de communication et de synchronisation robustes entre les
modèles locaux.
2.4.3. Limitations de l’apprentissage traditionnel
Les méthodes traditionnelles d’apprentissage de l’IA sont confrontées à des limites
importantes, en particulier dans les scénarios où la collecte centralisée de données et la
entrainement sur les modèles sont peu pratiques ou posent des risques pour la vie privée. Les
approches d’apprentissage automatique centralisées nécessitent une entrainement dans une
machine centrale et entraînent une consommation d’énergie, ainsi que des violations
potentielles de la vie privée. De plus, l’évolutivité de l’apprentissage traditionnel de l’IA est
Page 8 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
limitée lorsqu’il s’agit de traiter des ensembles de données massifs et diversifiés répartis sur
divers appareils ou organisations. Ces limites entravent l’efficacité et l’efficience de
l’apprentissage traditionnel de l’IA dans les environnements modernes riches en données. En
conséquence, l’émergence de l’apprentissage fédéré s’est imposée comme une solution
prometteuse pour relever ces défis en permettant une entrainement sur les modèles
collaboratifs tout en préservant la confidentialité des données et la décentralisation. Cela
soulève la question suivante : comment pouvons-nous gérer ces limites?
2.5. Apprentissage fédéré
Le Federated Learning (FL) est devenu une technologie essentielle dans le domaine de
l’apprentissage par l’IA, offrant une approche unique aux modèles d’entrainement tout en
préservant la confidentialité et la sécurité des données. L’importance de FL réside dans sa
capacité à faciliter la coopération multipartite en matière de données, un aspect crucial dans
le monde actuel axé sur les données où la confidentialité des utilisateurs est primordiale. En
permettant aux données de rester sur les périphériques de périphérie et non centralisées dans
un seul emplacement, FL assure une protection accrue de la vie privée, ce qui en fait une
solution fondamentale dans le domaine en pleine croissance de l’informatique de
confidentialité.
Page 9 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.5.1. Définition et généralités
L’apprentissage fédéré (FL) est une technique décentralisée utilisée dans le machine
learning et le deep learning qui permet à plusieurs clients de collaborer sur un modèle partagé
sans partager leurs données brutes. Cette approche a attiré beaucoup d’attention en raison de
son potentiel pour relever les défis liés au cloisonnement des données dans des applications
industrielles réelles. Google a proposé un apprentissage fédéré afin de répondre aux
préoccupations en matière de confidentialité des propriétaires de données, lorsque le partage
de données est limité, par exemple dans les services de santé ou les services financiers.
S’assurer que les données restent sur les appareils et ne quittent jamais l’environnement local
[21][52][16].
2.5.2. Avantages à l’apprentissage traditionnel (centralisé)
L’un des principaux avantages de FL est sa voie technologique légère et son
déploiement, ce qui en fait une solution courante pour diverses applications informatiques de
confidentialité, telles que la segmentation avancée de la collecte d’images médicales dans le
secteur de la santé. Cependant, malgré ses nombreux avantages, FL fait face à des défis,
l’efficacité de la communication étant une préoccupation notable. Pour résoudre ce problème,
des algorithmes comme FedAvg ont été introduits pour optimiser FL en incorporant le calcul
local, les techniques de compression de communication, et le chevauchement de calcul et de
communication. Bien que la LF offre des avantages inégalés en matière de protection de la
vie privée, son efficacité et sa sécurité de la communication demeurent un domaine à
améliorer, ce qui souligne le besoin continu de progrès dans cet aspect essentiel de
l’apprentissage fédéré [16].
Federated Learning (FL) est un nouveau paradigme d’apprentissage de l’IA qui
privilégie la confidentialité et la sécurité des données. Contrairement aux méthodes
conventionnelles qui centralisent les données pour le traitement, FL permet la entrainement
de modèles locaux sur des appareils individuels, éliminant le partage de données. Cette
méthode renforce non seulement la confidentialité des données, mais atténue également le
risque de violation de données et d’accès non autorisé. Une étude comparative a révélé que
FL a atteint un taux de précision de 76 % dans la classification des images, dépassant les
méthodes traditionnelles [55]. En outre, la mise en œuvre réussie de FL dans divers secteurs,
notamment les soins de santé, a démontré son potentiel pour répondre aux limites des
méthodes d’apprentissage traditionnelles, en particulier dans les contextes où la
confidentialité des données est primordiale.
Page 10 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.5.3. Processus d’apprentissage distribué
Le processus d’apprentissage fédéré comprend généralement les étapes suivantes, telles
qu’elles sont définies dans les articles [21][14] :
1. Initialisation du modèle : Un modèle global est initialisé et partagé avec tous les appareils
ou organisations sélectionnés.
2. entrainement locale : Chaque appareil ou organisation forme le modèle sur ses données
locales de façon indépendante, sans partager les données.
3. Envoyer les paramètres locaux : Les modèles ou paramètres formés localement sont
renvoyés à un serveur central ou à un coordinateur .
4. Agrégation des paramètres : regroupe les mises à jour des modèles pour créer un nouveau
modèle global.
5. Distribution du modèle : Le modèle global mis à jour est ensuite distribué aux appareils ou
organisations sélectionnés, en remplacement de leurs modèles locaux.
6. Itération : Les étapes 2 à 4 sont répétées jusqu’à ce que le modèle global converge ou
qu’un nombre prédéterminé d’itérations soit atteint.
Ce processus itératif permet d’améliorer le modèle global sans avoir à centraliser les
données d’entrainement, tout en préservant la confidentialité et la sécurité des données
locales. Ce processus se répète jusqu'à ce que l'ensemble du processus d'entraînement
converge, ou jusqu'à ce qu'un nombre prédéterminé de tours de communication ait été
exécuté [26].
Page 11 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
 Agrégation central
Les algorithmes d’agrégation fédérée jouent un rôle crucial dans le processus
d’apprentissage fédéré car ils déterminent comment les mises à jour de modèles formés
localement à partir de différents appareils ou organisations sont combinées ou agrégées pour
former une mise à jour de modèle globale.
L’algorithme d’agrégation fédérée le plus largement utilisé est l’algorithme de moyenne
fédéré (FedAvg), qui a été introduit pour la première fois. FedAvg est un algorithme simple
et efficace qui calcule la moyenne des mises à jour du modèle de chaque appareil ou
organisation et utilise cette moyenne comme nouveau modèle global. Cependant, FedAvg
s’est avéré vulnérable à l’hétérogénéité des données et aux contraintes de communication.
Pour remédier à ces limites, les chercheurs ont proposé diverses modifications à FedAvg,
comme FedProx , qui ajoute un terme proximal à la fonction objective pour traiter
l’hétérogénéité des données, et FedNova , qui utilise une nouvelle stratégie d’agrégation pour
améliorer l’efficacité de la communication[25][30].
Le choix de la technique d’agrégation dépend de facteurs tels que le paramètre
d’apprentissage fédéré (par exemple, le nombre d’appareils, la distribution des données),
l’architecture du modèle, les exigences de convergence et les contraintes de communication.
Différentes techniques peuvent offrir des avantages en termes de vitesse de convergence, de
robustesse aux données non-IID (données qui ne sont pas réparties de manière identique et
indépendante entre les appareils) et d’efficacité de la communication.
2.5.4. Classification de l’apprentissage fédéré
La FL est divisée en différentes catégories en fonction de divers facteurs. Les
classifications principales sont basées sur la distribution des données entre les
périphériques/clients périphériques, l’architecture et les modèles d’apprentissage [21].
a). Selon l’architecture
L’architecture des systèmes d’apprentissage fédérés peut être conçue en modes
centralisés ou décentralisés en fonction des interactions entre les différents éléments.
 Architecture centralisée
Dans l’approche centralisée, un serveur central coordonne la communication avec
diverses sources de données, sélectionne les clients participants, agrège les modèles locaux en
Page 12 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
un modèle global et distribue le modèle mis à jour. Cependant, les architectures centralisées
peuvent être vulnérables à des points de défaillance uniques.
 Architecture décentralisée
Les approches décentralisées manquent d’un serveur central pour la gestion et la
coordination, au lieu d’avoir des pairs coordonnés entre eux ou de tirer parti de la technologie
blockchain pour faciliter le partage et l’agrégation de modèles locaux dans un cadre distribué.
Alors que les architectures décentralisées comme p2pFL nécessitent une coordination plus
complexe pour communiquer et agréger les mises à jour de modèles sur tous les nœuds, elles
offrent une plus grande flexibilité et robustesse. La conception architecturale doit établir un
juste équilibre entre la confidentialité des données, la précision du modèle et l’efficacité de la
communication en fonction des exigences spécifiques de l’application et des contraintes du
système [21].
b). Selon la distribution des données
Lors de la entrainement de modèles sur des sources de données, l’apprentissage fédéré
prend en compte la manière dont les données sont distribuées entre elles. L’apprentissage
fédéré optimise la entrainement sur les modèles en tirant parti des données distribuées entre
plusieurs sources. La distribution des données entre ces sources est une considération
cruciale. De ce fait, il existe deux distributions primaires couramment rencontrées dans FL
qui sont cross-device et cross silos [21].
 Inter-organisationnel (cross-silos)
L'apprentissage fédéré entre silos devient pertinent lorsque des entités participantes,
comme des entreprises ou des institutions, entraînent un modèle sur leurs données locales.
Les principaux défis, incluent l'efficacité et la rapidité du développement des modèles, la
confidentialité et la sécurité des données, ainsi que l'encouragement de la coopération et des
incitations à la collaboration [26]. Cette approche permet l’intégration de données provenant
de sources multiples, ce qui améliore la robustesse et la précision globales du modèle [21].
 Inter-appareils (cross-device)
Cette configuration implique une multitude de petits appareils géographiquement
distribués, comme des smartphones et des dispositifs en périphérie, chacun ayant une petite
quantité de données et une capacité de calcul limitée [26]. Lors de l’entraînent inter-appareils,
le modèle est distribué entre les appareils périphériques, où il est formé localement sur les
Page 13 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
données de chaque appareil. Cette approche permet de former le modèle à diverses sources de
données, ce qui peut améliorer les performances du modèle.
c). Selon le model d’apprentissage
Une autre mesure pour la catégorisation des types de FL est le modèle d’apprentissage.
Le modèle peut être formé de différentes manières telles que l’apprentissage fédéré
horizontal, l’apprentissage fédéré vertical et l’apprentissage fédéré [54][21].
 Model horizontal
Le concept de HFL, ou apprentissage fédéré basé sur les échantillons, est
fondamentalement associé aux espaces de caractéristiques homogènes. Cependant, dans des
situations avec des espaces de caractéristiques hétérogènes, HFL a la limitation de n'utiliser
que les caractéristiques communes, laissant ainsi les caractéristiques spécifiques aux
participants inexploitées. Plus précisément, HFL est défini pour des ensembles de données
partageant le même espace de caractéristiques, mais distincts dans l'espace des identifiants
d'échantillons [26]. Horizontal FL implique la collaboration de plusieurs clients avec des
espaces de fonctionnalités de données similaires, tels que le projet GBoard centralisé de
Google [54].
Page 14 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
 Model vertical
L’apprentissage vertical, également appelé Feature Space FL, utilise différents
ensembles de fonctionnalités à travers les sources de données qui peuvent ou non avoir le
même espace d’échantillon, nécessitant des techniques comme l’alignement des entités et la
modélisation des données [54]. VFL démontre sa capacité à construire un modèle de méta-
apprentissage robuste en assimilant des sous-modèles dérivés d'un ensemble diversifié
d'entités. Ces sous-modèles sont entraînés localement avec des données partitionnées
verticalement et présentant des caractéristiques variées[26].
Note: Mise-à-part le modèle, l’apprentissage fédéré par transfert applique un modèle pré-
entraîné à partir d’un ensemble de données similaire pour résoudre un problème différent
[16][54]. Cette approche est utilisée lorsque deux ensembles de données varient dans l'espace
des identifiants d'échantillons et dans l'espace des caractéristiques [26].
Page 15 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.5.5. Défis et préoccupations
L'apprentissage fédéré permet à diverses entités de collaborer sur des modèles malgré
leurs différences. Les défis incluent des coûts de communication élevés, l'hétérogénéité des
systèmes
et
les
préoccupations
de
confidentialité
[26].
Après avoir collecté les paramètres modifiés des clients, le serveur effectuera une moyenne
pondérée de ces paramètres en fonction de la taille des données. Cependant, lorsque le
serveur transmet les paramètres agrégés aux clients pour la synchronisation du modèle, ces
informations peuvent être divulguées car des agents d'espionnage peuvent exister. Ainsi, la
sécurité du côté serveur est également importante. De même, les clients téléchargent leurs
résultats d'apprentissage, y compris les valeurs des paramètres et les poids, sur le serveur,
mais ils peuvent ne pas faire confiance au serveur car un serveur suspect pourrait examiner
les données soumises pour en déduire des informations privées [23].
Alors que l'apprentissage fédéré trouve son applicabilité dans divers domaines,
comprendre et relever les défis uniques de sécurité et de confidentialité devient encore plus
crucial [22].Bien que l'apprentissage fédéré assure que les données des utilisateurs soient
conservées localement, certaines méthodes d'attaque peuvent récupérer des informations
privées à partir des gradients, des paramètres de modèle, et certains attaquants peuvent lancer
des attaques par appartenance pour inférer l'existence de certaines propriétés [12].
Page 16 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
a). Attaques d’empoisonnement
Les attaques par empoisonnement (poisoning attacks) dans l'apprentissage machine visent
à compromettre l'intégrité et les performances des modèles en introduisant des données
malveillantes ou en manipulant les mises à jour des modèles [21]. Ces attaques peuvent se
manifester
sous
deux
formes
principales
:
l'empoisonnement
des
données
et
l'empoisonnement des modèles. Dans l'empoisonnement des données, des entrées incorrectes
ou biaisées sont injectées dans le processus d’entrainement, dégradant ainsi la précision et
induisant des comportements indésirables dans le modèle. L'empoisonnement des modèles,
en revanche, implique l'envoi de mises à jour de modèles malveillantes pour corrompre
l'agrégation finale des paramètres du modèle global. Ces attaques posent des défis
significatifs en matière de sécurité et de fiabilité, nécessitant des contre-mesures robustes
telles que l'agrégation sécurisée, la détection d'anomalies et des techniques de validation
rigoureuses pour protéger l'intégrité des systèmes d'apprentissage machine [22][23].
Bien que plusieurs solutions aient été proposées pour contourner les défis de
confidentialité, peu d'entre elles ont incorporé des techniques pour surmonter les attaques
d'empoisonnement des données, ce qui met en lumière les différentes vulnérabilités à travers
lesquelles les attaquants peuvent exploiter [11].
b). Attaques par porte dérobée
Les attaques par porte dérobée visent à créer une "porte dérobée" dans le modèle,
permettant à un attaquant de déclencher un comportement spécifique ou une mauvaise
classification lorsqu'il est présenté avec des motifs d'entrée spécifiques. Ces portes dérobées
sont souvent injectées pendant l'entraînement et peuvent poser une menace significative, en
particulier dans les scénarios où les modèles sont partagés entre plusieurs appareils et
utilisateurs [22]. Les fuites de confidentialité peuvent provenir d'un adversaire unique,
comme un utilisateur de FL, le serveur central ou un tiers, ou de multiples adversaires
collusifs. La collusion peut impliquer le serveur central et augmente le risque de fuites de
données, surtout lorsque plusieurs adversaires travaillent ensemble [24].
Page 17 sur 18CHAPITRE 2 : Principes Fondamentaux sur l’Intelligence Artificielle
PARTIE I
2.6. Conclusion
Dans ce chapitre, nous avons parcouru un large éventail de concepts et de techniques
essentiels à la compréhension et à l'application de l'intelligence artificielle. Nous avons
débuté par définir l'IA et ses objectifs, et nous avons exploré en profondeur les différentes
méthodes d'apprentissage, notamment l'apprentissage profond et l'apprentissage par transfert.
En parcourant ces notions, nous avons renforcé notre compréhension collective des forces et
des défis de l'intelligence artificielle moderne. Ensuite, nous avons étudié les techniques
prédictives et génératives, tout en examinant les facettes variées de l'apprentissage selon le
mode de supervision et l'emplacement des données. Nous avons également mis en lumière les
limitations de l'apprentissage traditionnel, ce qui nous a conduit à approfondir l'apprentissage
fédéré. Enfin nous avons également abordé les défis et les préoccupations liés à cette
approche, notamment les attaques d'empoisonnement et par porte dérobée.
Page 18 sur 18 """

ch3 = """ CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Table des matières
Chapitre 3 : conception de l’architecture
3.1. Introduction................................................................................................... 2
3.2. Application de l’apprentissage federe a la detection d’intrusions................ 2
3.3. Architecture proposee ................................................................................... 4
3.3.1. Differents acteurs du systeme ................................................................... 4
a). Agent d’entrainement ..................................................................................... 4
b). Agent d’inference ........................................................................................... 5
c). Serveur central ................................................................................................ 5
........................................................................................... 6
............................................................................................. 6
3.3.2. Emplacement des composants .................................................................. 6
........................................................................................ 7
................................................. 7
........................................... 7
3.3.3. Donnees echangees ................................................................................... 7
a). Chiffrement des donnees ................................................................................ 8
chiffrement rsa ................................................................................................... 8
b). Encapsulation et transfere des donnees .......................................................... 9
3.4. Methodes et techniques employees .............................................................. 9
3.4.1. Model d’apprentissage .............................................................................. 9
3.4.2. Technique d’agregation .......................................................................... 10
3.4.3. Filtrage d’agents...................................................................................... 10
3.5. Donnees d’apprentissage ............................................................................ 12
3.5.1. Choix des jeux de donnees...................................................................... 13
3.5.2. Jeu de donnees CSE-CIC-IDS 2018 ....................................................... 13
3.5.3. Jeu de donnees ADFA 2013 ................................................................... 14
3.5.4. Defis et preoccupations ........................................................................... 15
a). Donnees non identiques et independantes (non-IID) ................................... 15
b). Desequilibrage de classes ............................................................................. 15
3.6. Conclusion .................................................................................................. 16
Page 1 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
PARTIE II : DEVELOPPEMENT DU TRAVAIL
CHAPITRE 3
CONCEPTION DE L’ARCHITECTURE
_________________________
3.1. Introduction
Dans ce chapitre, nous proposons une architecture de détection d'intrusions basée sur
l'apprentissage fédéré. Nous détaillons les principaux aspects de notre architecture,
notamment les techniques à utiliser et les jeux de données à adopter. En particulier, nous
mettons en évidence l'importance des choix de ces solutions, en réponse à une revue
approfondie de la littérature existante.
Des approches sophistiquées et adaptatives à nos besoins, telles que l'agrégation et le
filtrage d'agents, seront mises en œuvre pour concevoir une architecture résiliente aux défis
attendus. Nous sélectionnons le modèle d'apprentissage le plus adapté ainsi que des jeux de
données sophistiqués pour garantir la performance et la généralisation de notre architecture.
Enfin, nous discutons des défis et des préoccupations associés à l'apprentissage fédéré
concernant les données, et proposons des solutions pour les surmonter.
3.2. Application de l’Apprentissage Fédéré à la Détection d’Intrusions
L'application de l'apprentissage fédéré à la détection d’intrusions représente une avancée
prometteuse dans le domaine de la sécurité des systèmes informatiques. Plusieurs recherches
mettent en lumière cette approche novatrice [2], qui exploite ses capacités pour entraîner des
modèles de détection d’intrusions de manière distribuée, sans pour autant compromettre la
confidentialité des données des utilisateurs [27][28][29]. En adoptant des solutions de
l’actualité, tel que les techniques à base d’apprentissage profond, nous feront l’objet d’une
étude rigoureuse afin de définir une architecture répartis, permettant ainsi aux dispositifs
terminaux (i.e. hôte ou toute entité possédant les ressources nécessaires) de tirer parti de leurs
données locales pour améliorer la précision de la détection d’intrusions, tout en évitant le
transfert de données sensibles vers le serveur central. La
décentralisation de notre
architecture représente une stratégie viable afin de développer des systèmes de détection
d'intrusions pour les réseaux informatiques. L’architecture proposée est illustrée par la figure
3.1.
Page 2 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
De nombreuses approches proposées [17][26][30], telles que l'utilisation des mécanismes
de filtrage pour la sélection d’agents, et l'adoption d'algorithmes d'agrégation efficaces,
représentent des pistes de recherche importantes que nous avons explorées pour surmonter les
défis1 liés à l’architecture décentralisée [12]. Dans notre quête pour améliorer notre
architecture, nous nous sommes penchés sur diverses stratégies et techniques, allant de la
répartition des agents, jusqu'à l’inférence finale. Celles-ci revêtent une importance cruciale
dans le cadre de notre étude de manière à optimiser notre solution.
Les IDSs basés sur l'apprentissage centralisé ne fonctionnent pas bien sur les données
inconnues. Bien que les algorithmes d'apprentissage obtiennent des résultats de haute
précision sur les ensembles de test, ils ont une faible précision de détection sur les données
inconnues [1]. Cependant, définir une architecture nous mène à identifier les suivantes
questions :





Quelle structure du paradigme à adopté ?
Comment positionner les différents composants ?
Que faire pour surmonter les défis de sécurité exigés (type altération et interception) ?
Quelle est le modèle d’apprentissage et choix du jeu de données ?
Qu’en est-il de la scalabilité ?
Figure 3.1 : Architecture décentralisé proposée (apprentissage fédéré)
1
Défis consistant en l’efficacité du système et hétérogénéité des données, qui entravent le développement de
l’apprentissage fédéré.
Page 3 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.3. Architecture Proposée
En effet, le choix de notre architecture se justifie par des raisons et des besoins de
souplesse et d’adaptabilité. Notre architecture est indépendante de toute plateforme matérielle
et logicielle (hétérogénéité). Cependant, il est possible d’ajouter et de retirer des stations
clientes2 ainsi que de faire évoluer le serveur lui-même, tout en gardant la même architecture
de base (redimensionnement). De plus, les données du serveur sont gérées de façon
centralisée, les clients restent donc individuels et indépendants de l’entité centrale (intégrité).
Pour notre architecture, nous avons adopté le modèle cross-silos (inter-organisationnel)
avec des données d'entraînement diversifiées. En intégrant des données provenant de
différentes sources, le modèle cross-silos à base d'apprentissage vertical nous permet
d'enrichir la diversité du système, et ainsi de conduire à un modèle global plus robuste et
généralisable. Ce choix fait de notre architecture une solution envisageable.
3.3.1. Différents Acteurs du Système
L’architecture que nous avons proposée consiste à mettre en place deux types d'agents
distincts : un dédié à la partie d'entraînement, lequel on fera appel pour générer/produire un
modèle local, et un autre pour la partie d'inférence, entité externe qui utilise le modèle global.
Ce découplage d’exécutions permet de diviser une seule entité cliente en deux parties
fonctionnelles différentes3, assurant ainsi une séparation claire des procédures, une haute
fiabilité de sécurité, réduction de la charge du traitement et une meilleure gestion des trafics
qui leurs sont associés.
a). Agent d’Entrainement
En utilisant un modèle à base de réseaux de neurones profond, chaque dispositif pourra
effectuer un entraînement local sur une partie des données qui lui est propre. Les mise à jours
du modèle local sont ensuit communiquées au serveur central pour but d’agrégation. Une fois
le modèle global transmis à l'agent d’entrainement, celui-ci procédera les mêmes étapes à
nouveau pour l'itération suivante, tenant compte du nouveau modèle.
2
Un cliente fait référence à un agent fonctionnel, traité par le serveur individuellement des autres.
Dans les résultats ultérieurs, on notera par Entité d’entrainement ; la partie productif du modèle, et Entité
d’inférence ; la partie consommatrice du modèle.
3
Page 4 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
b). Agent d’Inférence
A la fin de chaque cycle d’apprentissage, le serveur transmit le modèle global à tous les
agents associés, y-compris l’agent d’inférence. C’est alors à ce dernier de faire preuve
d'efficacité en réalisant des prédictions sur de nouvelles données. En s'appuyant sur le modèle
mis à jour, l'agent d'inférence contribue à identifier rapidement les tentatives d’intrusions
potentielles tout en gardant l’abstraction du modèle globale.
En adoptant une telle structure, nous favorisons ainsi la tolérance aux pannes issues des
points de défaillance uniques, évitant ainsi la nécessité de dépendre entièrement d'un seul
composant pour le bon fonctionnement du système.
c). Serveur Central
Dans le cadre de notre architecture, où la mise en place d'un serveur soit essentielle, nous
avons conçu un serveur central ayant les ressources nécessaires, et doté d’une capacité de
traitement raisonnable. Celui-ci est responsable de l'agrégation et de la sélection des agents
tout au long du processus d'apprentissage. Son rôle consiste à coordonner les échanges
d’informations entre les différents agents.
Au niveau du serveur, nous avons choisi d'opter pour une approche en deux niveaux (2-
tier) afin d'assurer la scalabilité du système, en termes de taux de traitement. Ceci fait de cette
stratégie une solution idéale pour un rendement optimal des performances. Cependant, le
serveur est constitué de deux parties collaboratives4, désignées par ; la présentation et
logique de traitements. La figure 3.2 représente le modèle employé.
Figure 3.2 : Modèle Gartner Group
4
Considérant la classification de Gartner Group, nous avons choisie d’omettre la partie gestion des données
puisque le serveur n’est pas doté de données confidentielles aux usagés.
Page 5 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
 Présentation : Une interface prise en charge par le serveur central. Cette organisation
présente l'avantage de faire des traitements d’encapsulation-décapsulation sur les données
transmis depuis et vers les clients. Cela compris ; des prétraitements (et éventuellement post-
traitements) sur des données reçues (resp. envoyées aux clients associés).
 Traitements : Le serveur est responsable de deux parts de traitements ; la partie de
filtrage des clients pertinents suivant un certain critère de sélection, et l’agrégation des
données soumis par ces clients, pour en former un modèle global. Ce traitement peut
nécessiter des ressources considérablement importantes, relatives au nombre de clients
auxquels le serveur fera partie.
3.3.2. Emplacement des Composants
Dans le paradigme « coss-silos », où les agents d'entrainement appartiennent à une entité
externe (par ex : une autre entreprise), une architecture en DMZ devrait être ajustée pour
accommoder ce scénario. Le principal objectif de cette DMZ réside dans la garantie de la
sécurité, tout en facilitant la communication entre les composants internes et externes. Les
différents composants sont positionnés de manière suivant la figure 3.3.
Figure 3.3 : Architecture en DMZ
Page 6 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
 Serveur Central : Le serveur, qui coordonne la communication entre le réseau interne de
du système (agents d'inférence) et le réseau externe (agents d’entrainement appartenant à des
entités externes), doit résider dans la DMZ. Il sert de passerelle sécurisée pour la
communication entre les composants internes et externes.
 Agents d'Entraînement (Réseau Externe) : Les agents d'entraînement, chargés de
générer des modèles locaux et opérant dans différents emplacements, restent donc dans le
réseau externe. Ils manipulent des données sensibles pour chaque emplacement lors de la
phase d'entraînement, et donc ne sont pas directement exposés à une entité particulière.
 Agents d'Inférence (Réseau Interne/Externe) : Les agents d'inférence, qui peuvent
appartenir à des entités externes, opèrent en dehors de la DMZ dans le réseau externe. Ces
entités peuvent être d'autres entreprises ou systèmes qui utilisent le modèle global à distance
pour des tâches d'inférence. Ils peuvent également faire partie du réseau interne, où ils sont
utilisés par la même organisation à des fins internes, et sont traités comme des entités
accédant aux services fournis par le serveur dans la DMZ.
Cette approche est adoptée pour la raison suivante ; considérant une architecture sans
DMZ, où il n’y a pas de séparation entre les entités internes et externes. En cas de
détournement du serveur (i.e. tentative d’altération), notre réseau interne (et éventuellement
tous les agents d'inférence) sera affecté par cette tentative destructive. Cependant, l’approche
proposée nous permet de réduire considérablement le point de défaillance unique.
3.3.3. Données échangées
Bien que les données d'entraînement ne soient visibles que pour l'agent qui les détient, il en
existe néanmoins des données circulant entre le serveur et ces agents, chose qui fait de
l'approche fédérée un principe fondamental. Selon notre architecture proposée, ces données
échangées reposent principalement sur un flux de paramètres associés aux modèles
d’apprentissage. Ces paramètres sont représentés par les poids et éventuellement les biais des
réseaux de neurones utilisés dans le processus d'entraînement.
De nombreuses revues exposent les principaux conflits liés aux données transférées durant
le processus d’apprentissage [24][26], ce qui nous sollicite à prendre en compte certaines
mesures de sécurité.
Les défis énoncés dans ce contexte peuvent être classés en deux
catégories (voir la sécurité, et la communication5) selon leur impact à affecter les
aspects critiques de l’apprentissage fédéré, touchant ainsi au bon fonctionnement du système.
5
Assurer une communication légère en bande passante, dépend le plus souvent par la complexité liée à la
définition de l’architecture du modèle d’apprentissage (par ex : taille, profondeur ...etc.).
Page 7 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
a). Chiffrement des Données
Garantir la confidentialité des données est une préoccupation principale dans
l'apprentissage fédéré. Pour protéger les informations sensibles, Plusieurs techniques de
protection des données ont été mise à disposition, telles que le chiffrement, l'agrégation
sécurisée et la confidentialité différentielle [15][17][21]. Ces méthodes protègent la
confidentialité des données individuelles pendant l'entraînement et l'agrégation du modèle.
L'application de l'apprentissage fédéré pour la détection d'intrusions est récente, et sa
combinaison avec les technologies de sécurité avancées telles que les registres distribués est
encore plus récente [13].
Les mécanismes de préservation de confidentialité peuvent être divisés en deux groupes ;
des mécanismes qui chiffrent ou obscurcissent les gradients et empêchent les parties
malveillantes de tirer des conclusions sur l'ensemble de données, et des mécanismes qui
masquent l'identité des parties participantes [17]. Cependant, notre objectif est de fournir un
degré de confidentialité en adoptant le chiffrement RSA.
 Chiffrement RSA
Nous utilisons des certificats numériques 2 en conjonction avec l'algorithme RSA1 pour
authentifier les clients, chiffrer et déchiffrer les données. Aussi pour échanger et stocker les
clés de manière sécurisée. L'authentification du client consiste à vérifier l'identité des
participants au réseau pour s'assurer que seuls les entités autorisées ont accès au réseau [59].
Le chiffrement, d’autre part , fait référence au transfert sécurisé de données sur un réseau tout
en les protégeant de tout accès et interception illicites [60]. En combinant ces deux
composants importants, nous établissons une communication sécurisée robuste qui garantit
l'intégrité et la confidentialité des données échangées sur le réseau.
Habituellement, un processus d’apprentissage fédéré vertical (VFL) admet que tous les
participants sont authentiques. Dans le cas de deux parties, par exemple, celles-ci sont non
coopératives, et au mieux, le concurrent est lésé. Le concept de sécurité est que l'adversaire
ne pourrait apprendre que des données de l'utilisateur compromises mais pas des données
provenant d'un autre client sauf celles qui sont exposées par les entrées et les sorties [22][23].
Il est à noter que nous assumons que le serveur est une entité de confiance. Cependant, même
si le chiffrement homomorphe est utilisé pour sécuriser les données, les agents doivent avoir
confiance en le serveur centralisé. Sinon, des fuites de données se produiront [16].
Page 8 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
b). Encapsulation et Transfère des Données
Il est essentiel d'assurer l'intégrité, en évitant toute altération ou perte de données pendant
leur transfert. D’après la technologie6 employée pour notre architecture, nous nous
contenterons d’utiliser les communications TCP/IP comme protocole de transport pour les
échanges entre le serveur et les clients. Notre solution est relative à la fiabilité, où la
transmission soit critique et que des retards ou des pertes de données ne sont pas acceptables.
Cela nous garanti, entre outre, une communication fiable et sécurisée entre les différents
composants du système.
3.4. Méthodes et Techniques Employées
Il est à noter que notre choix de méthodes et de techniques a été mené par une inspection
approfondie de la littérature existante [4][5], offrant un aperçu des solutions actuelles. Cette
couverture nous a conduits à bien concevoir notre architecture, tenant compte des différents
aspects critique de chaque technique.
3.4.1. Model d’Apprentissage
Selon la littérature, le choix du modèle d’apprentissage représente une décision
déterminante lors de la conception de l’architecture. Plusieurs études [4][6][8] ont pu définir
un large éventail de modèles en démontrant leur efficacité dans le contexte de la détection
d’intrusions [4]. Avec une fréquence accrue des attaques réseau, les chercheurs accordent
plus d'attention à la sécurité réseau [5], mais seulement quelques-uns d'entre eux ont exploité
l'apprentissage profond bien qu'ils n'aient pas complètement exploré les applications de
l'apprentissage profond en ce qui concerne les NIDSs [1]. Cependant, les modèles à base de
réseaux de neurones profonds, ont prouvé leur capacité à apprendre des représentations à
partir des parquets d’en-têtes, faisant ainsi un choix avantageux pour notre architecture, où
les agents d’entrainement peuvent bénéficier d’une partie d'apprentissage locale sur leurs
propres données, tout en contribuant à l'amélioration d'un modèle global.
Ayant consulté une variété d’applications, notamment l’application des réseaux récurrents
RNNs [4][5], l’applications des GANs [6], ainsi que celles des Auto-encoders [4][6], nous
avons trouver que la meilleure solution consiste en appliquant les réseaux de neurones
profonds. le choix de cette solution se justifie par le fait que, dans l‘apprentissage fédéré, il
6
Cette technologie, basée sur HTTP/2 fait référence à Flower (fonctionnant sous la convention de RPC) que
nous allons aborder dans le chapitre suivant.
Page 9 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
est nécessaire de tenir compte de plusieurs facteurs, tels que la taille, la complexité et les
contraintes de calcul au niveau des agents d’inférence. L'idée principale de l'utilisation des
architectures neuronales profondes est qu'elles aident à réduire automatiquement la
complexité du trafic réseau. Elles identifient des corrélations dans les données sans nécessiter
un algorithme explicite de sélection des caractéristiques ou un expert du domaine. De plus,
elles sont efficaces pour détecter les exploits « zero-day » et les attaques avancées [1].
Cependant, le choix du modèle doit être capable de fournir un équilibre entre performance
(i.e. précision et temps de réponse) et complexité.
Parlant du modèle, nous avons adopté une architecture profonde composée de plusieurs
couches, permettant une représentation complexe des données et une meilleure capacité de
généralisation. De plus, Nous avons également utilisé la régularisation lors de l’apprentissage
afin d’éviter la situation de sur-apprentissage et ainsi favoriser une meilleur convergence du
modèle globale. Mise à part la précision, le temps de détection doit également être pris en
compte. Plus une intrusion est détectée rapidement, plus les administrateurs réseau seront
alertés pour prendre les mesures nécessaires [1]. En appliquant ce modèle, nous avons pu
obtenir une architecture adaptable aux exigences de notre système d’apprentissage fédéré.
3.4.2. Technique d’Agrégation
Après l'acheminement de l'entraînement des différents modèles locaux, les agents
concernés peuvent alors communiquer leurs changements au serveur central. Ce dernier est
chargé de les combiner pour former un modèle global en utilisant la technique d'agrégation
FedAvg. Ce choix est le résultat d'une étude approfondie de l'état de l'art. Nous avons
sélectionné la technique d'agrégation FedAvg appropriée pour notre architecture, car elle
permet de réduire la quantité de données transmises entre les appareils et le serveur central,
ce qui peut être bénéfique en termes de bande passante et de consommation d'énergie.
3.4.3. Filtrage d’Agents
Pour prendre en charge un grand nombre de dispositifs, nous pouvons appliquer la
procédure de sélection des clients pour choisir une fraction à entraîner lors d'un cycle
d’exécution. En filtrant les agents avant l'agrégation, on peut ainsi exclure les agents de base
fiabilité, ce qui permet d'améliorer la rentabilité et la qualité de notre architecture.
Page 10 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
De nombreux algorithmes de sélection des nœuds (agents) sont proposés pour améliorer
l'efficacité de l'apprentissage fédéré [18][21][14]. De ce fait, Nous avons réalisé une revue
approfondie de la littérature portant sur les techniques de sélection d’agents dans le cadre de
l'apprentissage fédéré. Cette revue nous a permis d'analyser en détail les différentes
approches de filtrage existantes.
Pour notre architecture, nous avons choisi d’implémenter le détecteur des clients
empoisonnés, proposé par [20] au niveau du
serveur,
pour identifier les clients
potentiellement empoisonnés et limiter leur participation à l'agrégation du modèle de
détection d'intrusion global. Il est important de réduire l'influence des clients empoisonnés sur
le modèle de détection d'intrusion global. A cet effet, l’intégration de ce mécanisme à notre
système, nous permet, en outre, de réduire la charge de traitement au niveau du serveur,
d'éliminer les agents susceptibles d'être empoisonnés, et de favoriser une convergence
efficace du modèle global.
Figure 3.4 : Coordination entre différents acteurs
Page 11 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5. Données d’apprentissage
Un système de détection d'intrusion idéal devrait être capable de détecter une grande
variété d'attaques. Il devrait également avoir un taux de détection élevé avec un faible taux de
fausses alertes. Ainsi, un ensemble de données de qualité, actuel et diversifié aura un impact
considérable sur la précision de notre modèle [1][4].
Certaines études que nous avons consultées montrent que de nombreux ensembles de
données ont été publiés au cours des dernières années, et que la communauté travaille
continuellement à la création de nouvelles données pour la détection d'intrusions [3][5]. Les
données utilisées pour la recherche peuvent être soit réalistes (capturées), soit synthétiques
(générées). Pour les données réalistes, celles-ci sont capturées soit au format basé sur les
paquets, soit au format basé sur les flux, soit à un format indéfini [3], toute en gardant
l’aspect de confidentialité7. 

Format basé sur les paquets8 : destiné aux HIDSs, en miroitant les ports sur les dispositifs
réseau, englobant des informations de contenu complètes.
Format basé sur les flux9 : destiné aux NIDSs, dans lesquels elles sont agrégées et
contiennent généralement uniquement des métadonnées des connexions réseau.
Format indéfini: aucun cadre spécifique pour la capture de données, cette catégorie
pourrait être constituée de données basées sur les flux qui ont été enrichis avec des
informations supplémentaires à partir de données basées sur les paquets.
Il est à noter que la plupart des systèmes d'intrusion s'appuient sur des ensembles de
données obsolètes, et qu'ils ne reflètent donc plus les nouveaux types d'attaques [1][5]. A cet
effet, il serait judicieux pour nous de choisir soigneusement un ensemble, considérant la
qualité et la pertinence. La principale raison du manque de disponibilité des ensembles de
données d'intrusion est que la construction de nouveaux ensembles nécessite souvent une
expertise en matière de connaissances. Un autre problème majeur que nous avons constatés
est que les attaquants trouvent de nouvelles techniques pour éviter la détection, ce qui rend
nécessaire l'intégration continue de nouveaux types d'attaques à ceux existants [1].
7
Les données capturées doivent être traitées avec précaution. Certains attributs peuvent être tirés de façon
anonyme, d'autres doivent être omis si besoin.
8
Les métadonnées disponibles dépendent des protocoles réseau et de transport utilisés. Voir 3.5 de l’annexe.
9
En considérant la direction des flux, Les données réseau basées sur les flux peuvent être capturées soit de
manière unidirectionnelle soit bidirectionnelle.
Page 12 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5.1. Choix des Jeux de Données
Dans le même contexte, Une méthode que nous avons consultée [3], nous a fourni une
classification en 5 propriétés distinctes (à savoir ; les informations générales, la nature, le
volume, l’environnent et l’évaluation), par lesquelles nous pouvons facilement conclure une
analyse10 sur chacun des ensembles de données. En revanche, Les auteurs, ayant cités ; « Le
jeu de données parfait devrait être à jour, correctement étiqueté, disponible publiquement,
contient du trafic réseau réel avec toutes sortes d'attaques et de comportements d'utilisateurs
normaux ainsi que leurs contenus, et couvre une longue période. Cependant, un tel jeu de
données n'existe pas et ne sera (probablement) jamais créé.», montrent que, même dans le
respect de la confidentialité, et dans un environnement réel, un jeu de données comportant
toutes les attaques récentes ne peut être entièrement étiqueté qu’après l’apparition de
nouvelles attaques [3][5]. Cependant, nous visons à anticiper l’évaluation de notre système
avec un jeu de données décrivant plus qu’un format particulier (i.e. de nature diversifiée),
puisque suivant le paradigme fédéré, et éventuellement dans l’environnement réel, différents
données depuis des sources distincts et éloignées existent. En couvrant un certain nombre de
revues11 [5][6], nous avons pu déduire notre choix concernant le jeu de données approprié.
Notre approche sera mise en œuvre pour éviter la convergence vers un ensemble spécifique,
évaluer le système dans un contexte plus général, et d’imitez le comportement d’un HIDS et
d’un NIDS à la fois.
3.5.2. Jeu de Données CSE-CIC-IDS 2018
L’ensemble de données (CSE-CIC-IDS 2018) est proposé par le Centre de la sécurité des
télécommunications
(CSE) et l’institut canadien de cyber-sécurité (CIC) en 2018. Cet
ensemble, faisant partie du group12 des ensemble à base de flux réseaux, comprend sept
scénarios d'attaque différents, notamment Heartbleed, Brute-force, DoS , DDoS , les
attaques Web, Botnet et les attaques d'infiltration [6][10]. Plusieurs revues sur cet ensemble
ont été élaborées ces dernières années, nous permettant d’avoir un aperçu bien précis et
détaillé de cet ensemble [10][1][4][6]. Ce jeu de données, constitué de plus de 16 million
d’exemples, et de 80 attributs au total, est mené d’un attribut complémentaire représentant la
classe correspondante à chaque donnée associée. Selon l’étiquette, deux profils peuvent se
caractérisés à partir de cet ensemble, voir B-profil et M-profil.
10
Les auteurs n'ont pas élaboré de score d'évaluation pour ne pas comparer les différents ensembles.
L'importance de certaines propriétés ne devrait pas être jugée de manière critique.
11
Dont certaines d'entre elles sont fondées sur les stratégies de recherche SLR, PRISMA, et SnowBall.
12
Selon la contribution de l’étude [6], où ils ont pu classer les jeux suivant sept groups d’ensemble distincts.
Page 13 sur 16CHAPITRE 3 : Conception de l’Architecture


PARTIE II
Profil Bénin (B-Profil) : Résume le comportement typique des utilisateurs normaux. Il
encapsule les comportements des entités utilisatrices dans un ensemble de caractéristiques
telles que la taille des paquets, le nombre de paquets par flux, la taille du contenu et les
motifs du contenu [9].
Profil Malveillant (M-Profil) : Vise à décrire de manière claire un scénario d'attaque. Il
a fallu utiliser des agents autonomes et des compilateurs pour interpréter et exécuter ces
scénarios [9].
3.5.3. Jeu de Données ADFA 2013
Les ensembles de données utilisés pour évaluer les HIDS ne sont pas facilement
disponibles en raison de problèmes de sécurité et de confidentialité. Cependant, il existe de
nombreux ensembles de données disponibles publiquement, tels que ADFA-LD, et ADFA-
WD qui sont couramment utilisés comme références [8].
Des chercheurs de l'Académie de la Force de Défense Australienne (ADFA) ont créé
deux ensembles de données, voir ADFA-LD «Linux-based» et ADFA-WD «Windows-
based», en tant qu'ensembles de données publics représentant la structure et la méthodologie
des attaques modernes. Les ensembles de données contiennent des enregistrements d'appels
système, à partir des systèmes d'exploitation Linux et Windows à la fois. Certaines instances
d'attaque dans ADFA-LD ont été dérivées de nouveaux logiciels malveillants « zero-day », ce
qui rend cet ensemble de données approprié pour mettre en évidence notre propre architecture
fédérée en matière de détection d'intrusions.
ADFA a été développé comme étant une référence moderne pour les IDS basés sur les
hôtes (HIDS). L'ensemble de données étiqueté ADFA13 est le successeur de la collection
KDD, utilisant les dernières failles et techniques d’intrusion disponibles [33]. Cet ensemble a
été utilisé par les chercheurs pour évaluer les performances de leurs approches proposées de
détection et de prévention des intrusions [10], la raison pour la quelle nous avons choisi le jeu
de données comme étant le référentiel des comportements des hôtes.
13
En plus du manque de diversité et de la variété des attaques, les comportements de certaines attaques dans cet
ensemble de données ne sont pas bien séparés du comportement normal [10].
Page 14 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
3.5.4. Défis et Préoccupations
En pratique, les données entre les nœuds sont généralement non-IID. De plus, la quantité
de données distribuées sur chaque nœud est toujours déséquilibrée. Par conséquent, le télé-
versement fréquent de modèles sur des agents particuliers, a le potentiel d'attirer la
divergence vers le modèle global et de provoquer un sur-ajustement à des ensembles de
données spécifiques [18]. Cette divergence envers les données, peut nuire à l’apprentissage
fédéré du model global, et ainsi compromettre sa capacité à généraliser correctement. Par
conséquent, le rendement apporté à notre system sera affecté.
a). Données non identiques et indépendantes (non-IID)
Dans des scénarios réalistes, les données des clients sont confirmées comme non
indépendantes et identiquement distribuées (non-IID), contrairement aux scénarios IID
idéalement supposés dans de nombreuses méthodologies de recherche. Dans les systèmes de
détection d'intrusion basés sur l'apprentissage fédéré, certains clients (dispositifs) peuvent ne
présenter que du trafic malveillant tandis que d'autres peuvent présenter du trafic normal ou
être composés de différents types de trafic malveillant [20]. Ainsi, des études ont révélé que
le taux de convergence peut être réduit par des facteurs tels que l'entraînement sur de petites
données non-IID [19].
Cependant, notre expérience sera menée sur des ensembles de données IID et non-IID à la
fois, pour vérifier l'efficacité de notre approche. Dans le cas de notre étude, nous
commençons par partitionner les données d'entraînement originales en ensembles
d'entraînement non-IID disjoints, pour rapprocher le scénario typique. Notre expérimentation
sera menée sous différentes situations possibles pour simuler le comportement réel des
agents faisant face à la situation des données non-IID.
b). Déséquilibrage de classes
Consultant diverses études, les ensembles de la littérature (y compris ceux que nous
utilisons) sont confrontés à une contrainte connue sous le nom du problème de
déséquilibrement de classe, où la distribution des données de trafic réseau est inégale, avec
des exemples normaux apparaissant plus fréquemment que les exemples d'attaque. Ce
déséquilibre peut affecter les performances de notre modèle, en particulier pour les classes
d'attaques minoritaires [2][5].
Page 15 sur 16CHAPITRE 3 : Conception de l’Architecture
PARTIE II
Selon les contributions qui ont été faites, nous avons constaté qu'il existe des techniques
de ré-échantillonnage [2] (telles que le oversampling, le undersampling et le hybrid
sampling), et l’approche coût-sensitive [5], qui peuvent être solutions pour surmonter les
ensembles de données déséquilibrés. Dans le cas de notre étude, nous avons préférer
d’appliquer une technique de ré-échantillonnage (l’augmentation des données en particulier)
pour son efficacité à contourner le problème.
3.6. Conclusion
Dans ce chapitre, nous avons présenté une nouvelle architecture d'apprentissage fédéré
pour les systèmes de détection d'intrusions (IDS). L'architecture proposée tire parti des
avantages de l'apprentissage fédéré, tout en abordant les défis spécifiques au domaine des
IDSs.
Nous avons décrit les différents acteurs impliqués dans le système, ainsi que leurs
emplacements relatifs. Nous avons décrit le processus d'échange de données, en mettant
l'accent sur le chiffrement des données et les mécanismes de transfert sécurisé entre les
entités participantes. De plus, nous avons discuté des méthodes et des techniques utilisées
dans l'architecture, telles que le choix du modèle d'apprentissage, la technique d'agrégation et
le filtrage des agents. Enfin, nous avons abordé les défis associés aux données d'entraînement
dans les IDS fédérés, notamment les données non-IID et le déséquilibrement des classes, en
soulignant l'adaptabilité de notre architecture envers différents scénarios.
"""
# Extract numbers
extracted_numbers = extract_bracketed_numbers(ch3)


# Print the results
if extracted_numbers:
    print("Extracted numbers:", extracted_numbers)
else:
    print("No numbers found within square brackets in the input text.")

