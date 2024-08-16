import re

def extract_bracketed_numbers(text):
    """Extracts numbers enclosed in square brackets from the given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        list: A list containing the extracted numbers as strings.
    """

    pattern = r"{\d+}"  # Regex pattern to match digits within brackets
    matches = re.findall(pattern, text)
    return matches


# Get user input
#user_text = input("Enter your text: ")

ch1 = """ 
\chapter{ Chapitre 4 : Implémentation et déploiement}
\lhead{\textit{Chapitre \thechapter }}
\rhead{\textit{Implémentation et déploiement}}


\section{Introduction} 
Ce chapitre présente l'environnement logiciel et matériel utilisé dans notre recherche ainsi l’analyse des résultats obtenus à travers différentes métriques de performance. Nous détaillerons les expérimentations proposées, en comparant les résultats après optimisation dans un cadre d'apprentissage centralisé, puis les performances de l'apprentissage fédéré avec et sans la protection de la confidentialité différentielle (DP). 

 
 
\subsection{Environnement Logiciel }
\subsubsection{Le langage python et ces bibliothèques}
 En ce qui concerne l’apprentissage machine, nous avons rendu notre solution compatible avec les bibliothèques Python les plus populaires. Ainsi, nous utilisons le langage Python dans sa version 3.12.3,  Il est généralement utilisé pour sa simplicité, portabilité, efficacité et surtout pour sa capacité à offrir divers modules afin de mieux s’adapter aux besoins des chercheurs, Nous avons utilisé scikit-learn qui est une bibliothèque d’apprentissage statistique , elle est utilisée largement dans les application d’intelligence artificielle et de la science des données.  On a également installé les modules pandas et  Numpy  pour tout ce qui concerne la manipulation des données,  

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=2cm , angle=360]{Frames/python.jpeg}
    \caption{ Logo de python}
    \label{fig: Logo de python}
\end{figure}
\newpage
 Nous avons utilisé PyTorch pour l'entraînement des modèles d’apprentissage machine dans notre projet. PyTorch est une bibliothèque de deep learning populaire, reconnue pour sa flexibilité et sa possibilité de  création et de la manipulation de réseaux de neurones, et est ainsi utilisée par la communauté scientifique. 

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=15cm , angle=360]{Frames/pytorch.png}
    \caption{  Logo des bibliothèques Python.}
    \label{fig:  logo des bibliothèques Python.}
\end{figure}

\subsubsection{Le framework flower }
 Pour implémenter l'apprentissage fédéré dans notre projet, nous avons utilisé le framework Flower. Flower est un framework open-source conçu spécifiquement pour la mise en œuvre d’une architecture fédérée.\cite{93}
 \newline
 \newline
 Depuis \cite{89} La conception de Flower repose sur quelques principes directeurs :
 \newline
 
\textbf{Personnalisable :}
 Les systèmes d’apprentissage fédérés varient énormément d’un cas d’utilisation à l’autre. Flower permet un large éventail de configurations différentes en fonction des besoins de chaque cas d’utilisation individuel.

\textbf{Extensible :}
 Flower est née d’un projet de recherche à l’Université d’Oxford, il a donc été construit avec la recherche en IA à l’esprit. De nombreux composants peuvent être étendus et remplacés pour construire de nouveaux systèmes de pointe.

\textbf{Indépendant du cadre :}
 Différents cadres d’apprentissage automatique ont des forces différentes. Flower peut être utilisé avec n’importe quel cadre d’apprentissage automatique

\textbf{Compréhensible :}
 Flower est écrit avec la maintenabilité à l’esprit. La communauté est encouragée à lire et à contribuer au code de base.


 \newline
 Grâce à Flower, nous avons pu entraîner efficacement des modèles sur plusieurs nœuds tout en garantissant la confidentialité des données.
 \newline
 \begin{figure} [hbt!]
    \centering
    \includegraphics[width=3cm , angle=360]{Frames/flower.jpeg}
    \caption{  Logo de flower framework.}
    \label{fig:  logo de flower framework.}
\end{figure}

 \newline
 L'intégration de PyTorch avec Flower nous a permis de développer et d'entraîner des modèles complexes de manière distribuée, tout en bénéficiant des capacités avancées de PyTorch en termes de performance et de modularité.

 


\subsubsection{Le protocole GRPC }
Le protocole Google remote procedure call (GRPC) améliore l’efficacité de la communication entre les différents composants du système Federated Learning. Au sein de Flower, le protocole GRPC joue un rôle crucial dans la gestion des interactions entre le serveur central et les clients participants. Cette communication fluide, facilitée par GRPC, garantit que le processus d’apprentissage  est rapide, fluide et fiable. par intégration du protocole GRPC dans Flower, les performances et l’évolutivité des systèmes d’apprentissage fédéré sont considérablement améliorées, ce qui les rend plus pratiques et efficaces dans un large éventail d’applications.

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=3cm , angle=360]{Frames/grpc.png}
    \caption{  Logo de protocole GRPC.}
    \label{fig:  logo de protocole GRPC.}
\end{figure}


\subsection{Environnement de mise en œuvre  }

\subsubsection{L’outil Jupyter Lab }
 Jupyter lab est un environnement interactif basé sur un navigateur Web. Il peut être considéré comme un laboratoire de développement très utile grâce à ses fonctionnalités avancées, on peut citer par exemple sa capacité à lire différents fichiers à la fois comme les figures, les tableaux, les graphes ainsi que plusieurs d’autres types afin de mieux visualiser le projet. Il s'agit d'un outil essentiel pour les data scientists et les programmeurs , Ainsi on peut également rattacher des noyaux de différents fichiers afin de les exécuter en un seul block, ce qui permet de mieux s’organiser\cite{90}.

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=3cm , angle=360]{Frames/jupyter.jpeg}
    \caption{ Logo de Jupyter Lab}
    \label{fig:  logo de Jupyter Lab.}
\end{figure}
\newline
\newline

\subsubsection{La plateforme kaggle }
 Il est évident que l’apprentissage automatique prend beaucoup de temps d’exécution surtout quant il s’agit de traiter des jeux de données immenses, c’est pour cela que de nombreuse plateformes telles que Kaggle et GoogleCOLAB nous ont été misent a disposition en fournissant une durée de CPU, de GPU, et de TPU allant jusqu'à 37 heures par semaine, afin de pouvoir exécuter simultanément des programmes en arrière plan, tout en sauvegardant les résultats pour les consulter ultérieurement. Pour notre recherche, nous avons créé des espaces personnels sur la plateforme Kaggle pour exécuter plusieurs portions de programme en parallèle, ce qui nous permet de gagner un temps considérable.
 
 \begin{figure} [hbt!]
    \centering
    \includegraphics[width=4cm , angle=360]{Frames/kagggle.png}
    \caption{  Logo de kaggle.}
    \label{fig:  logo de kaggle.}
\end{figure}

\subsection{Environnement Matériel}
  Pour l'implémentation de notre projet, nous avons utilisé trois ordinateurs portables avec les configurations matérielles présentées dans ce qui suit :


\begin{table}[hbt!]
    \centering
    \begin{tabular}{|p{3.5cm}|p{4cm}|p{4cm}|p{4cm}|}
        \hline
        Caractéristiques & Dell Latitude 5420 & Lenovo Yoga 11E & Dell Latitude E6540 \\
        \hline
        Processeur & - Intel Core i5-1145G7 & - Intel® Celeron(R) CPU N3150 & - Intel® Core™ i5-4210M \\
        \hline
        Mémoire RAM & - 8 Go DDR4 & - 8 Go DDR3 & - 8 Go DDR3 \\
        \hline
        Stockage & - 512 Go SSD & - 256 Go SSD & - 512 Go HDD \\
        \hline
        Système d’exploitation & - Windows 11 Pro & - Windows 10 Pro & - Ubuntu 22.04.4 LTS \\
        \hline
    \end{tabular}
    \caption{Configurations matérielles (Machines)}
\end{table}
\newline
Ainsi pour la simulation réel , le CERIST nous a offert une machine performante avec l'accès à distance  pour l'entraînement de notre modèle d'apprentissage fédéré , la machine a les configurations matérielles suivante : 

\newline
\begin{table}[hbt!]
    \centering
\begin{tabular}{ | m{5cm} | m{10cm}| } 
  \hline
  Caractéristiques & QEMU Standard PC (i440FX + PIIX)
  \\
  \hline
  Processeur & - Common KVM Intel processor × 20 core
 \\ 
  \hline
  Memoire RAM & 19.5 Go
  \\ 
  \hline
   Stockage & 236.2 Go
  \\ 
  \hline
   Système d’exploitation & Ubuntu 24.04 LTS
 \\ 
  \hline
\end{tabular}
    \caption{Configurations matérielles (Google Cloud) }
\end{table}


\subsection{Méthodologie de mise en oeuvre }

\subsubsection{ Prétraitement des Données }

Avant de pouvoir passer les ensembles de données à l'algorithme d'entraînement du réseau neuronal, ils doivent être prétraités pour changer leur format sans détruire leurs Caractéristiques intrinsèques, tout en maintenant l'approche scientifique dans la conception du modèle IDS requis. Lors de l'étape de prétraitement, les actions suivantes ont été effectuées :
\newline
\newline
\begin{itemize}
    \item Les fichiers de flux de réseau ont été agrégés en un seul fichier.
    \item Les lignes vides et dupliquées ont été supprimées des ensembles de données.
    \item Les colonnes (caractéristiques) représentant le temps et les identifiants de flux comme ("Flow ID" et "Timestamp") ont été supprimées.
    \item Les valeurs infinies, NA et NAN ont été éliminées.
    \item Les données de la colonne 'Label' ont été encodées.
    \item L'ensemble des données a été normalisé en utilisant la fonction MinMaxScaler de la bibliothèque scikit-learn. La normalisation a été appliquée uniquement aux caractéristiques, mais la colonne 'Label', qui contient une description qualitative de chaque flux, a été laissée avec une représentation entière puisque cela facilitera un processus de prédiction plus clair pour les classes cibles.
\newline
\newline
\end{itemize}
Après l'achèvement de l'étape de prétraitement, les fichiers d'ensembles de données (9 fichiers au total) ont été agrégés à environ 485 Mo (compressés et stockés au format feather) pour CSE-CIC-IDS2018. Cela permet le traitement et le mélange inter-ensembles de données.\\
Bien que les données de classe normale soient significativement plus que celles anormales, nous avons assuré un équilibre de classe à l'aide de technique de réduction de données (undersampling). Puisque l'apprentissage est supervisé, nous avons utilisé ces proportions de données avec étiquette Booléenne (1/0) représentant la présence/absence d'une intrusion.

\subsubsection{ Sélection d'attributs }

 Avant que cet ensemble de données ne puisse être transmis à l'algorithme d'entraînement du réseau neuronal, le nombre de caractéristiques (attributs) de l’nsemble doit être réduit afin que le temps d'évaluation de l'algorithme du réseau neuronal soit plus réaliste. La réduction des caractéristiques présente une large gamme d'avantages, notamment \\
 \textbf{(1)} l'amélioration des performances de prédiction en surmontant le risque de la dimensionnalité,\\ 
 \textbf{(2)} la réduction des besoins en mesure et en stockage,\\ 
 \textbf{(3)} la réduction de la durée de l'entraînement et \\ 
 \textbf{(4)} la facilitation de la visualisation et de la compréhension des données.
\newline
\newline
 Tout d'abord, les colonnes (caractéristiques) qui représentent des informations d'adresse d'hôtes arbitraires qui changent d'une configuration à l'autre, comme ("Source IP", "Source Port" et "Destination IP"), ont été supprimées. La caractéristique ("Destination Port") a été conservée car elle est fortement corrélée avec le type de trafic.
\newline
\newline
 Deuxièmement, nous avons constaté qu’il y a un certain nombre de caractéristiques dans les deux ensembles de données qui n'ont pas de variance, ce qui, en conclusion, n'a aucun effet sur le processus d'entraînement, donc ces caractéristiques (8 au total) ont été éliminées. D’autre part, le test de corrélation à montrer la présence de nombreux attributs fortement corrélés entre eux, ce qui nous amène à éliminer (22 attributs au total), partant du principe que, plus les attributs sont corrélés entre eux, moins on obtient de performances. Le résultat de cette étape est un vecteur de 50 attributs qui sera utilisé dans la prochaine étape de construction du modèle d'algorithme du réseau neuronal.

 \begin{figure} [hbt!]
    \centering
    \includegraphics[width=10cm , angle=360]{Frames/correlation.png}
    \caption{Matrice de corrélation}
    \label{fig:  Matrice de corrélation.}
\end{figure}


\subsubsection{ Répartition des données }
  un apprentissage adéquat, Nous avons divisé le jeu de données en deux sous-ensembles initiales, une partie pour l'entraînement des modèles locaux (80\%), soit 4.673.509 exemples, et une partie dédiée pour le test final (20\%), soit 1.168.378 exemples. Leur proportion est ajustée en fonction du taux de rendement. Le processus est illustré par la figure suivante:

  
   \begin{figure} [hbt!]
    \centering
    \includegraphics[width=18cm , angle=360]{Frames/fig4.2 Stratégie d’apprentissage.png}
    \caption{  Stratégie d’apprentissage.}
    \label{fig:  Stratégie d’apprentissage.}
\end{figure}


 Les données d'entraînement servent à entraîner les modèles locaux, et sont répartis entres les différents agents d'entraînement de façon aléatoire. Une partie supplémentaire à celle d'entraînement (45\%) est assurée au niveau de chaque agent. Cette partie, dite de validation stratifiés \footnote{ \textsf{La stratification signifie que le partage des données est respecté par des proportions de classes uniformes. Ce terme est à ne pas confondre avec l'équilibre entre les différentes étiquettes du même ensemble.}}, sera considérée comme référence pour l'évaluation des modèles locaux et le suivi de leurs résultats.  Les données de test quant à elles, sont statiques tout au long du processus d'apprentissage.\\ \\ \\ Cet ensemble représente des données non identifiées auparavant par le modèle global, et ont pour but d'évaluer ses performances. 

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=18cm , angle=360]{Frames/Stratégie d’apprentissage2.png.png}
    \caption{Division de la dataset}
    \label{ Division de la dataset.}
\end{figure}

\subsection{  Architecture du modèle}
 Nous avons développé un modèle en multi-couches cachées, avec 12 couches optimisées pour NIDS. La première couche est la couche d'entrée qui reçoit les valeurs des caractéristiques du jeu de données. Ensuite, l'étape suivante consiste en quatre couches répétitives, avec une couche de Normalisation placée après chaque paire de couches linéaires suivie d'une couche Dropout pour améliorer la précision. \\ \\La dernière couche est la couche de sortie, généralement utilisée dans le contexte de la classification et de la prévision des classes d'attaques. Elle comprend un neurone pour la classe prédite, donnant la probabilité de cette classe. Ainsi, sa valeur doit être strictement supérieure à 0.5 pour que le résultat d'une requête soit identifié comme une intrusion. La fonction d'activation Sigmoïde a été utilisée dans la couche de sortie.
\newline

 Pour le processus d'apprentissage, nous avons utilisé l'optimiseur de Descente de Gradient Stochastique (SGD) représenté dans l'équation ci-dessous. En plus de cela, nous avons appliqué le Momentum ainsi qu'un scheduler pour accélérer la convergence et améliorer la vitesse et la stabilité de l'algorithme de descente de gradient au fil des époques. 

\[
\theta_{t+1} = \theta_t - \eta \nabla_{\theta} J(\theta; x^{(i)}; y^{(i)})
\]

où :
\begin{itemize}
    \item $\theta_t$ est le vecteur des paramètres au pas de temps $t$.
    \item $\eta$ est le taux d'apprentissage.
    \item $\nabla_{\theta} J(\theta; x^{(i)}; y^{(i)})$ est le gradient de la fonction de coût $J$ par rapport aux paramètres $\theta$, calculé pour l'exemple de données $(x^{(i)}, y^{(i)})$.
\end{itemize}



 

\subsection{  Optimisation du modèle }
 Pour obtenir de bons résultats, il est essentiel d'ajuster le modèle pour qu'il soit plus généralisé aux données et améliore ses performances. À cette fin, nous avons effectué un processus d'optimisation sur notre modèle dans le but de réduire le risque d'erreurs de prédiction et ainsi améliorer ses performances. Dans ce but, nous avons utilisé la technique de recherche par grille (ParameterGrid de la bibliothèque sklearn) pour ajuster deux configurations principales : la structure du modèle et ses éventuels hyper-paramètres. 
\newline

 La structure mentionnée précédemment, composée de trois couches avec 4 sous-couches chacune, doit être ajustée. L'espace exploré est donc l'accumulation de toutes les combinaisons possibles, soit 86 itérations sur 10 divisions de validation croisée. La structure résultante est représentée dans le récapitulatif ci-dessous. Après avoir obtenu la meilleure structure possible \footnote{ \textsf{Évidemment, le terme "meilleure" est relatif à notre étude de cas, selon l'espace prédéfini. Toutefois, il n'est pas garanti que ces résultats ne soient pas soumis à un optimum local.}}, nous avons procédé à une deuxième optimisation des hyper-paramètres, tels que le taux d'apprentissage (LR) et le momentum, puisqu’ils sont détermi-
 nants pour l'apprentissage du modèle. le LR et le momentum ont été ajustés conjointement sur une plage de valeurs définie. Une fois l'optimisation achevée, la configuration résultante de notre modèle est jugée pertinente pour passer à la phase d'apprentissage, tout en améliorant les performances.\\

    
\begin{table}[h!]
\centering
\begin{tabular}{|l|l|l|}
\hline
\textbf{Paramètre} & \textbf{Type} & \textbf{Champs} \\
\hline
\textit{dropout\_rate} & flottant & [0.1 - 0.45] \\
\textit{layer1\_dim} & entier & [32 - 256] \\
\textit{layer2\_dim} & entier & [32 - 256] \\
\textit{layer3\_dim} & entier & [32 - 256] \\
\hline
\end{tabular}
\caption{Les couches du modèle}
\end{table}
\newpage

\begin{verbatim}
          
            #------------------------ première couche
            torch.nn.Linear(input_dim, layer1_dim),
            torch.nn.BatchNorm1d(layer1_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=dropout_rate),
            #------------------------ deuxième couche
            torch.nn.Linear(layer1_dim, layer2_dim),
            torch.nn.BatchNorm1d(layer2_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=dropout_rate),
            #------------------------troisième couche
            torch.nn.Linear(layer2_dim, layer3_dim),
            torch.nn.BatchNorm1d(layer3_dim),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=dropout_rate),
            #------------------------couche de sortie
            torch.nn.Linear(layer3_dim, output_dim),
            torch.nn.Sigmoid(),
        )   
                    Structure du modèle
\end{verbatim}


\section {Discussion des Résultats}
\subsection {Métriques de performance}
Pour évaluer les performances de notre modèle, nous avons utilisé un ensemble de métriques rigoureuses, couramment employées dans le domaine du Machine Learning. Ces métriques incluent :\\

\begin{itemize}
    \item \textbf{Exactitude (Accuracy) :}    L'exactitude, aussi taux de réussite global, représente la proportion de prédictions correctes (positives et négatives) parmi toutes les prédictions effectuées par le modèle. Autrement dit, elle mesure la capacité globale du modèle à prédire correctement les éléments, qu'ils soient positifs ou négatifs.\\
    \[
        \text{Exactitude} = \frac{TP + TN}{TP + TN + FP + FN}
    \]
    \\
    où $TP$ : vrais positifs, $TN$ : vrais négatifs, $FP$ : faux positifs et $FN$ : faux négatifs.\\
    
    \item \textbf{Précision (Precision) :}  La précision représente la proportion de prédictions positives correctes parmi toutes les prédictions positives effectuées par le modèle. En d'autres termes, elle mesure la capacité du modèle à identifier correctement les éléments positifs.
    \[
        \text{Précision} = \frac{TP}{TP + FP}
    \]
    
    \item \textbf{L'entropie croisée binaire (Binary Cross-Entropy) :} Cette métrique, représe-
    nte la perte (Loss) du modèle soumis à l'étude. Cette fonction mesure la différence entre la distribution de probabilité prédite par le modèle et la distribution réelle des classes. Une valeur faible d'entropie croisée binaire indique une meilleure concordance entre les prédictions et la réalité. Elle est définie par l'équation suivante :
     \[
    \text{BCELoss} = - \left( y_{\text{true}} \cdot \log(y_{\text{pred}}) + (1 - y_{\text{true}}) \cdot \log(1 - y_{\text{pred}}) \right)
     \]
    \item \textbf{Le rappel (Recall) :} Il exprime la capacité du modèle à identifier correctement tous les exemples positifs. Un rappel élevé est crucial pour les situations où il est primordial de ne pas manquer d'éléments pertinents. Elle est définie par l'équation suivante :
    \[
        \text{Rappel} = \frac{TP}{TP + FN}
    \]
    
    \item \textbf{La mesure F1 (F1-score) :} Elle combine la précision et le rappel en une seule métrique, offrant un compromis équilibré entre les deux.
    \[
        \text{F1-score} = 2 \times \frac{\text{Rappel} \times \text{Précision}}{\text{Rappel} + \text{Précision}}
    \]
    
    \item \textbf{Le taux de faux positifs (False Positive Rate - FPR) :} Il mesure la proportion d'échantillons négatifs incorrectement classés comme positifs. Un FPR faible est crucial pour minimiser les erreurs qui pourraient avoir des conséquences importantes.
    \[
        \text{FPR} = \frac{FP}{FP + TN}
    \]
    
    \item \textbf{La matrice de confusion :} Elle présente un tableau croisé récapitulatif des résultats de classification, permettant d'analyser en détail les types d'erreurs commises par le modèle.
\end{itemize}

L'utilisation de ces métriques complémentaires nous a permis d'obtenir une évaluation complète et précise des performances de notre modèle.\\


Nous avons évalué notre modèle en utilisant les metrique parlé précédemment  , pour comprendre à quel point notre modèle est précis et à quel point il s'ajuste bien aux données d'entraînement, de validation et de test. Cette évaluation se divise en deux types, soit une évaluation locale où chaque dispositif local a évalué son modèle sur des données de validation locales. Ainsi qu’une évaluation globale où Le modèle agrégé a été évalué sur un ensemble de données de test centralisé pour mesurer sa performance globale.  

 
\subsection {Les  Expérimentation proposées}
Pour expérimenter l'apprentissage fédéré, nous avons élaboré trois scénarios distincts. Le premier scénario représente l'optimisation du modèle après plusieurs itérations d'apprentissage fédéré, visant à améliorer ses performances. Le deuxième scénario introduit l'intégration du principe de confidentialité différentielle (DP), assurant la protection des données individuelles tout en maintenant l'efficacité de l'apprentissage. Enfin, le troisième scénario explore les effets d'agents empoisonnés, qui peuvent perturber le processus d'apprentissage fédéré en introduisant des données malveillantes.












\subsection {Résultats après l'optimisation (apprentissage centralisé)}

Dans le but d'optimisation de la structure de notre modèle, nous avons exploré différents hyperparamètres, notamment le nombre de neurones et le taux de dropout pour chaque couche. À travers notre expérimentation, nous avons identifié les cinq meilleures configurations qui maximisent l'exactitude du modèle. La figure 4.10 illustrant l'évolution du nombre de neurones par couche en fonction de l'exactitude (et la perte) du modèle est présentée ci-dessous. Cette analyse est complétée par un tableau 4.4 récapitulatif qui présente les résultats optimaux, mettant en évidence les configurations choisies pour notre modèle, et leur impact sur l'exactitude obtenue.


\begin{figure} [hbt!]
    \centering
    \includegraphics[width=15cm , angle=360]{Frames/figure 4.3.png}
    \caption{Evolution des performances par l'optimisation des couches}
    \label{fig:figure 4.3}
\end{figure}

Dans notre seconde expérience, nous avons mis l'accent sur les hyperparamètres spécifi-
ques à l'apprentissage, notamment le learning rate et le momentum utilisés dans l'optimiseur SGD. Notre objectif était d'évaluer l'impact de différentes combinaisons de ces hyperparamètres sur l'exactitude (accuracy) du modèle. À travers une série de configurations expérimentales, nous avons généré la figure 4.11 qui représente le learning rate, le momentum et l'exactitude obtenue. Cette représentation permet une visualisation intuitive entre ces hyper-paramètres et leur influence sur la performance globale du modèle. Les résultats montrent clairement les zones de l'espace des hyperparamètres où les meilleures performances en termes d'exactitude sont atteintes, offrant ainsi la meilleure configuration pour notre modèle. Les résultats sont également présentés dans le tableau 4.4


\begin{figure} [hbt!]
    \centering
    \includegraphics[width=15cm , angle=360]{Frames/figure 4.4 .png}
    \caption{Evolution des performances par l'optimisation des hyperparamètres}
    \label{fig:figure 4.4}
\end{figure}


\begin{table}[h!]
\centering
\resizebox{\textwidth}{!}{%
\begin{tabular}{|>{\centering\arraybackslash\small}m{1.5cm}|>{\centering\arraybackslash\small}m{1.5cm}|>{\centering\arraybackslash\small}m{1.5cm}|>{\centering\arraybackslash\small}m{1.5cm}|>{\centering\arraybackslash\small}m{2.5cm}|>{\centering\arraybackslash\small}m{1.5cm}|>{\centering\arraybackslash\small}m{2.5cm}|>{\centering\arraybackslash\small}m{1.5cm}|}
\hline
\multicolumn{4}{|c|}{\textbf{\small paramètres de structure}} & \multicolumn{2}{c|}{\textbf{\small paramètres d’apprentissage}} & \multicolumn{2}{c|}{\textbf{\small performance}} \\
\hline
\textbf{\tiny dropout\_rate} & \textbf{\tiny layer1\_dim} & \textbf{\tiny layer2\_dim} & \textbf{\tiny layer3\_dim} & \textbf{\tiny learning\_rate (1e-4)} & \textbf{\tiny momentum} & \textbf{\tiny Exactitude (\%)} & \textbf{\tiny Loss (1e-5)} \\
\hline
0.10 & 256 & 160 & 96 & 5,0 & 0.6 & 87,2028 & 7,1
\\
\hline
0.15 & 256 & 160 & 96 & 50,0 & 0.6 & 87,2162 & 6,9 
\\
\hline
0.10 & 256 & 160 & 96 & 50,0 & 0.5 & 87,0674 & 6.0 \\
\hline
0.25 & 256 & 192 & 32 & 50,0 & 0.6 & 87,3524 & 6.8 \\
\hline
\textbf{0.40} & \textbf{224} & \textbf{96} & \textbf{64} & \textbf{5,0} & \textbf{0.8} & \textbf{87,3802} & \textbf{5.9} \\
\hline

\hline
\end{tabular}}
\caption{Récapitulatif des meilleures configurations obtenus }

\end{table}



Les résultats obtenus lors de l'étape d'optimisation nous permettent de fournir une base de référence pour la phase suivante de notre étude, soit l'apprentissage. Cela dit, l'optimisation, nous permettra de consolider nos choix préliminaires en mettant à l'épreuve la capacité du modèle à généraliser et à produire des résultats prédictifs \footnote{\textsf{résultats obtenus suivant 10 scissions de validations}} robustes pour la phase suivante.

\section*{Résultats de l'apprentissage fédéré}

Pour ce scénario, nous avons lancé 10 agents d'entraînement possédant 1/10 de l'ensemble de données initial. Nous avons également défini 5 epochs pour qu’un cycle soit achevé. Le processus d'apprentissage aura 100 cycles (rounds) au total. La figure 4.12 montre le résultat de cette simulation. Analysant cette figure, on a observé que la perte de notre modèle diminue, indiquant ainsi une amélioration dans sa capacité à ajuster ses prédictions par rapport aux valeurs réelles attendues. Cependant, il nous reste à poser la question suivante : pourquoi avons-nous le scénario où la perte diminue tandis que l'exactitude reste stable ?
\newline

\begin{figure} [hbt!]
    \centering
    \includegraphics[width=15cm , angle=360]{Frames/Fig 4.5.png}
    \caption{ Evolution des performances du modèle global}
    \label{fig:figure 4.5}
\end{figure}


En premier lieu, nous pouvons penser que la diminution de la perte signifie généraleme-
nt que le modèle a pu optimiser ses paramètres pour mieux correspondre aux données d'entraînement. Cela se traduit par une réduction de l'erreur moyenne sur ces données. Cependant, bien que la perte et l'exactitude soient liées au progrès général du modèle, elles peuvent être influencées différemment par des facteurs tels que le facteur non-IID sur les classes de nos données. En fait, si les classes dans les données sont de nature non-IID (ce qui est le cas pour notre étude), l'exactitude peut ne pas être très sensible aux changements dans les classes minoritaires. Le modèle peut ainsi améliorer sa capacité à prédire les classes majoritaires tout en n'étant pas encore performant sur les classes minoritaires. Ce qui a conduit à la stabilité de l'exactitude, car la majorité des prédictions sont correctes pour les exemples majoritaires, mais une amélioration de la perte montre que le modèle affine ses prédictions globales.


\subsection{Résultats de l’apprentissage fédéré avec DP}
Avec l'utilisation des mêmes configuration ,  après l'exécution de la version de DP  on obtient les résultat suivant : 
\newline

\begin{figure}[htbp]
    \centering
    \includegraphics[width=15cm, angle=360]{Frames/fig-4.6:.png}
    \caption{ Evolution des performances avec et sans l'intégration du DP}
    \label{fig:figure 4.6}
\end{figure}

Le graphique présenté illustre l'évolution des performances locales des agents 1 à 10 après 500 epochs, en comparant les versions avec et sans Differential Privacy (DP). L'analyse met en évidence un compromis entre la précision des performances et la protection de la confidentialité des données. Cela dit, nous sommes confrontés à une balance entre sécurité et performance, D’autre part, nous assumons que cette différence de précision est négligeable afin de garantir la sécurité.

\subsection{Comparaison des Résultats}

En comparant les résultats obtenus des phases précédentes, on voit bien une augmentation significative des performances du modèle après son optimisation. Cela met en évidence l'importance de la configuration sur l’apprentissage. Or, ces performances qui en découlent sont le résultat d’un apprentissage centralisé. Cela dit, les données apprises proviennent d’une même source, et présentent donc un risque de détournement. A cet effet, nous avons procédé à la phase d’apprentissage fédéré.

Dans le contexte de l’apprentissage fédéré, nous avons veillé à ce que tous les agents d'entraînement soient de confiance. En d’autres termes, toutes les entités participantes ne présentent aucun risque d’usurpation. En revanche, l'expérimentation démontre que le système est très sensible au phénomène d'empoisonnement, ce qui présente un inconvénient en termes de fiabilité. La figure 4.14 illustre le scénario ou on a explicitement injecté des agents empoisonnés dans notre architecture, ce qui a considérablement affecté les performances. Un tel résultat semble logique puisque le fait d’incorporer des entités pareils influence l’apprentissage et donc la convergence du modèle global. 


\begin{figure}[htbp]
\centering
\includegraphics[width=15cm , angle=360]{Frames/fig-4.7.png}
\caption{Empoisonnement des agents}
\end{figure}

Pour un récapitulatif, en apprentissage fédéré, on a observé des résultats meilleurs que ceux de l’apprentissage centralisé. Cela signifie que le modèle atteint un équilibre entre la précision et le rappel. Un score TN élevé nous indique que le modèle a à la fois une faible proportion de faux positifs (précision élevée) et une faible proportion de faux négatifs (rappel élevé), ce qui est souhaitable dans la mise en œuvre de notre architecture. La figure 4.15 est utilisée pour visualiser les résultats globaux, tandis qu'une matrice de confusion finale offre une évaluation détaillée de la capacité du modèle à classer correctement les données. Ces éléments combinés fournissent une analyse complète et comparative des performances de l'apprentissage fédéré dans les différents contextes étudiés.

\begin{figure}[htbp]
\centering
\includegraphics[width=15cm]{Frames/fig_4.15.png}
\caption{Matrice de confusion}
\end{figure}

\textbf{\\Vrais positifs (TP) :} 525 186. Il s’agit du nombre de cas normales que le modèle a correctement classé comme normale.\\
\textbf{Faux positifs (FP) :} 34 471. Il s’agit du nombre d’instances normales que le modèle a incorrectement classées comme intrusion.\\
\textbf{Faux négatifs (FN) :} 80 379. C’est le nombre de cas d’intrusion que le modèle a incorrectement classés comme normaux.\\
\textbf{Vrais négatifs (TN) :} 528 342. C’est le nombre d’instances d'intrusions que le modèle a correctement classées.

Sur la base de ces résultats, nous pouvons voir que le modèle est plus susceptible de faire des faux négatifs (défaut de détecter une intrusion) que des faux positifs (identification incorrecte d’une instance normale comme une intrusion). Cela peut être engendre par l'effet du déséquilibre des données, ce qui pourrait poser un problème si le coût d’un faux négatif est élevé.

\newpage
\section{Conclusion}
Ce chapitre a permis d'analyser et de discuter les résultats obtenus à travers différentes expérimentations et optimisations. Les métriques de performance initiales ont fourni une base de comparaison essentielle pour évaluer les améliorations apportées par les différentes méthodes d'apprentissage, notamment l'apprentissage centralisé et l'apprentissage fédéré, avec et sans ajout de confidentialité différentielle (DP).






 """

# Extract numbers
extracted_numbers = extract_bracketed_numbers(ch1)
#extracted_numbers = extract_bracketed_numbers(ch2)
#extracted_numbers = extract_bracketed_numbers(ch3)
#extracted_numbers = extract_bracketed_numbers(ch4)


# Print the results
if extracted_numbers:
    print("Extracted numbers:", extracted_numbers)
else:
    print("No numbers found within square brackets in the input text.")
