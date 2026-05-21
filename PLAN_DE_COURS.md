# Plan de cours — Devenir Data Scientist autonome

> Objectif final : être capable de postuler à un poste de **Data Scientist** avec un portfolio solide, une maîtrise des fondamentaux mathématiques, du code Python, du Machine Learning, du Deep Learning et du MLOps.

Structure de chaque module :
- **Partie A — Besoins / Théorie** : pourquoi on apprend ça, à quoi ça sert en entreprise.
- **Partie B — Mise en pratique** : exercices concrets, à me rendre, que je corrigerai.

Rythme suggéré : 2 modules / mois (12 mois au total). Adaptable selon ta disponibilité.

---

## Module 0 — Mise en place de l'environnement (Semaine 0)

### A. Besoins
- Avoir un environnement Python reproductible (versions, dépendances).
- Comprendre Git/GitHub pour publier ton portfolio.
- Outils standards du métier : Jupyter, VS Code, terminal.

### B. Exercices
1. Installer `pyenv` + `poetry` (ou `uv`) sur ton Mac.
2. Créer un repo GitHub `data-science-journey` avec un README.
3. Lancer un notebook Jupyter qui affiche `pandas.__version__`.
4. Faire ton premier commit + push.

**Livrables** : lien GitHub + capture du notebook.

---

## Module 1 — Python pour la Data Science (Semaines 1-2)

### A. Besoins
- 90 % du travail d'un Data Scientist se fait en Python.
- Maîtriser : types, structures (list/dict/set), compréhensions, fonctions, classes, gestion d'erreurs, modules.
- Connaître les bonnes pratiques : PEP8, typing, tests unitaires.

### B. Exercices
1. Écrire une fonction `word_count(text: str) -> dict[str, int]` avec tests `pytest`.
2. Implémenter une classe `BankAccount` (deposit, withdraw, history).
3. Lire un CSV "à la main" (sans pandas) et calculer la moyenne d'une colonne.
4. Refactoriser un script donné (je te le fournirai) en respectant PEP8 + typing.

**Livrables** : dossier `module1/` avec code + tests qui passent.

---

## Module 2 — NumPy & Pandas (Semaines 3-4)

### A. Besoins
- NumPy = calcul vectoriel rapide (base de tout ML).
- Pandas = manipulation de données tabulaires (le quotidien).
- Comprendre : broadcasting, indexing, groupby, merge, pivot.

### B. Exercices
1. Recoder une moyenne mobile en NumPy (sans boucle Python).
2. Sur le dataset **Titanic** : taux de survie par classe / sexe / âge.
3. Sur le dataset **Airbnb Paris** : top 10 quartiers par prix médian.
4. Nettoyer un dataset "sale" (NaN, doublons, types incohérents) que je te fournirai.

**Livrables** : 4 notebooks commentés.

---

## Module 3 — Visualisation de données (Semaines 5-6)

### A. Besoins
- Communiquer un résultat = 50 % du métier.
- Outils : `matplotlib`, `seaborn`, `plotly`.
- Principes : choix du bon graphique, lisibilité, storytelling.

### B. Exercices
1. Reproduire 5 graphiques d'un article du journal *Les Échos* / *FT*.
2. Dashboard interactif Plotly sur les ventes d'une boutique fictive.
3. Critique visuelle : prendre un mauvais graphique et le refaire.

**Livrables** : notebook + 1 article LinkedIn "5 erreurs de dataviz".

---

## Module 4 — Statistiques & Probabilités (Semaines 7-9)

### A. Besoins
- Base mathématique indispensable pour interpréter un modèle.
- Notions clés : variables aléatoires, lois (normale, binomiale, Poisson), TCL, intervalles de confiance, tests d'hypothèses (t-test, chi², ANOVA), corrélation vs causalité, p-value.

### B. Exercices
1. Simuler 10 000 lancers de dés et vérifier le TCL.
2. A/B test : déterminer si une nouvelle page web convertit mieux (jeu de données fourni).
3. Calculer un intervalle de confiance à 95 % "à la main" puis avec `scipy`.
4. Détecter une corrélation fallacieuse dans un dataset piégé.

**Livrables** : notebook + résumé d'1 page sur "p-value expliquée à un PM".

---

## Module 5 — Algèbre linéaire & Calcul (Semaine 10)

### A. Besoins
- Comprendre ce qu'il se passe SOUS les modèles ML.
- Vecteurs, matrices, produit scalaire, valeurs propres, gradient, dérivées partielles.

### B. Exercices
1. Implémenter une régression linéaire "à la main" (formule fermée + descente de gradient).
2. PCA from scratch sur le dataset Iris, comparé à `sklearn`.

**Livrables** : 2 notebooks.

---

## Module 6 — SQL & Bases de données (Semaines 11-12)

### A. Besoins
- En entreprise, la donnée vit dans une base. Savoir l'extraire est non négociable.
- Maîtriser : SELECT, JOIN, GROUP BY, fenêtrage (window functions), CTE, sous-requêtes.

### B. Exercices
1. 50 exercices sur [sql-practice.com](https://www.sql-practice.com) ou DataLemur.
2. Sur une base SQLite que je te fournirai : top clients, cohortes mensuelles, rétention.
3. Connecter Python à PostgreSQL et charger un résultat dans un DataFrame.

**Livrables** : fichier `.sql` + notebook.

---

## Module 7 — Machine Learning supervisé (Semaines 13-16)

### A. Besoins
- Le cœur du métier.
- Algorithmes : régression linéaire/logistique, k-NN, arbres, Random Forest, Gradient Boosting (XGBoost/LightGBM), SVM.
- Concepts : train/test split, cross-validation, overfitting, métriques (RMSE, accuracy, precision/recall, F1, AUC), feature engineering.

### B. Exercices
1. Prédire le prix d'une maison (Boston / California housing).
2. Classification : prédire le churn télécom (jeu Kaggle).
3. Comparer 5 algos sur le même dataset avec cross-validation.
4. Compétition Kaggle "Titanic" — viser le top 20 %.

**Livrables** : 4 notebooks + 1 soumission Kaggle.

---

## Module 8 — Machine Learning non supervisé (Semaines 17-18)

### A. Besoins
- Quand on n'a pas de label : segmentation client, détection d'anomalies, réduction de dimension.
- Algos : K-means, DBSCAN, hiérarchique, PCA, t-SNE, UMAP, Isolation Forest.

### B. Exercices
1. Segmenter les clients d'un e-commerce (RFM + K-means).
2. Visualiser MNIST en 2D avec t-SNE.
3. Détecter des transactions frauduleuses (Isolation Forest).

**Livrables** : 3 notebooks.

---

## Module 9 — Feature Engineering & Pipelines (Semaines 19-20)

### A. Besoins
- 80 % de la performance vient des features, pas du modèle.
- Outils : `sklearn.pipeline`, `ColumnTransformer`, encoding (one-hot, target, frequency), scaling, feature selection.

### B. Exercices
1. Construire un pipeline complet reproductible (preprocessing + modèle + grid search).
2. Feature engineering avancé sur un dataset de séries temporelles (lags, rolling, encodages cycliques).

**Livrables** : 2 notebooks + pipeline sérialisé (`joblib`).

---

## Module 10 — Deep Learning (Semaines 21-24)

### A. Besoins
- Indispensable pour vision, NLP, audio.
- Frameworks : **PyTorch** (recommandé) ou TensorFlow/Keras.
- Notions : neurones, backpropagation, fonctions d'activation, optimizers (SGD, Adam), CNN, RNN/LSTM, Transformers, transfer learning.

### B. Exercices
1. Réseau dense from scratch en NumPy (1 hidden layer).
2. CNN sur CIFAR-10 avec PyTorch.
3. Fine-tuning d'un modèle Hugging Face (BERT) pour classification de sentiments en français.
4. Mini-projet libre (ex. classifier des photos de MacBook par modèle — clin d'œil OKAMAC).

**Livrables** : 4 notebooks + 1 modèle entraîné publié sur Hugging Face Hub.

---

## Module 11 — NLP & LLMs (Semaines 25-26)

### A. Besoins
- Domaine ultra demandé en 2026.
- Notions : tokenisation, embeddings (Word2Vec, BERT), RAG, fine-tuning, prompt engineering, évaluation de LLM.

### B. Exercices
1. Construire un moteur de recherche sémantique sur tes propres documents (FAISS + embeddings).
2. Chatbot RAG simple avec LangChain ou LlamaIndex.
3. Évaluer 3 prompts différents sur une tâche de résumé.

**Livrables** : 1 application Streamlit déployée.

---

## Module 12 — Séries temporelles (Semaine 27)

### A. Besoins
- Prévision de ventes, de stocks, de cours.
- Méthodes : ARIMA, SARIMA, Prophet, modèles ML (LightGBM avec lags), modèles DL (LSTM, N-BEATS).

### B. Exercices
1. Prévoir les ventes mensuelles d'une chaîne de magasins.
2. Comparer Prophet vs LightGBM vs SARIMA.

**Livrables** : 1 notebook avec benchmark.

---

## Module 13 — MLOps & Mise en production (Semaines 28-30)

### A. Besoins
- Un modèle qui dort dans un notebook ne vaut rien. Savoir le déployer = facteur différenciant énorme à l'embauche.
- Outils : Docker, FastAPI, MLflow, DVC, GitHub Actions, cloud (AWS / GCP basics).

### B. Exercices
1. Servir un modèle scikit-learn via une API FastAPI.
2. Dockeriser l'API et la pousser sur Docker Hub.
3. Mettre en place MLflow pour tracker tes expériences.
4. Pipeline CI/CD GitHub Actions : lint + tests + build Docker.
5. Déployer l'API sur Render / Railway / Fly.io (gratuit).

**Livrables** : repo GitHub complet + URL de l'API en ligne.

---

## Module 14 — Big Data (Semaine 31)

### A. Besoins
- Quand les données ne tiennent plus en RAM : **Spark** (PySpark), **Polars**, **DuckDB**.

### B. Exercices
1. Refaire un traitement Pandas en Polars et mesurer le gain.
2. Mini-job PySpark sur un dataset > 1 GB.

**Livrables** : 2 notebooks + benchmark.

---

## Module 15 — Projet portfolio final (Semaines 32-36)

### A. Besoins
- Un projet end-to-end qui prouve toutes tes compétences.
- Format type : problème métier réel → collecte/scraping → EDA → modélisation → API → dashboard → article de blog.

### B. Idées de projets (choisir 1 ou proposer)
- Prédiction du prix de revente de MacBooks selon spec/état (parfait pour ton contexte OKAMAC).
- Détection automatique de défauts sur photos de produits reconditionnés.
- Système de recommandation de configuration Mac selon profil utilisateur.

**Livrables** :
- Repo GitHub propre (README, tests, CI).
- Application déployée.
- Article Medium / LinkedIn expliquant la démarche.
- Vidéo de démo de 3 min.

---

## Module 16 — Préparation aux entretiens (Semaines 37-40)

### A. Besoins
- Entretiens Data Scientist = 4 axes : coding (LeetCode easy/medium), SQL, ML théorique, cas business.
- Soft skills : savoir vulgariser, structurer une réponse (méthode STAR).

### B. Exercices
1. 30 problèmes LeetCode (tags : array, hash, two pointers).
2. 20 questions SQL niveau medium/hard.
3. 50 questions ML théoriques (biais/variance, régularisation, etc.) — je te ferai un quiz.
4. 3 cas business simulés (je joue le recruteur).
5. Préparer CV + LinkedIn + lettre type.

**Livrables** : CV finalisé + 5 candidatures envoyées.

---

## Ressources transverses recommandées

- **Livres** : *Hands-On Machine Learning* (Géron), *Python for Data Analysis* (McKinney), *The Elements of Statistical Learning*.
- **Cours en ligne** : fast.ai, DeepLearning.ai (Coursera), Kaggle Learn.
- **Pratique régulière** : Kaggle, DataLemur, LeetCode.
- **Veille** : newsletter *The Batch*, *Data Elixir*, podcasts *DataFramed*.

---

## Suivi de progression

| Module | Statut | Date début | Date fin | Notes |
|--------|--------|------------|----------|-------|
| 0 | ⬜ | | | |
| 1 | ⬜ | | | |
| 2 | ⬜ | | | |
| ... | | | | |

---

**Prochaine étape immédiate** : dis-moi quand tu es prêt pour le **Module 0**, je te donne les premiers exos en détail et je corrige ton code au fur et à mesure.
