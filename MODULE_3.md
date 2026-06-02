# Module 3 — Visualisation de données

> Objectif : savoir transformer un DataFrame en graphique **lisible**, **honnête** et qui **raconte une histoire**.
> Durée estimée : 2 semaines (15-20 heures).
> Pré-requis : Module 2 terminé (NumPy & Pandas).

---

## Vue d'ensemble

À la fin de ce module, tu seras capable de :

1. Choisir le bon type de graphique en fonction de la question posée.
2. Produire des graphiques propres avec **matplotlib** (la base) et **seaborn** (le confort).
3. Créer des graphiques **interactifs** avec **plotly**.
4. Détecter et corriger les principales erreurs de dataviz (axes trompeurs, 3D inutile, surcharge…).
5. Présenter une analyse sous forme de "data story" claire pour un non-technique.

---

## Partie A — Théorie

## Concept 1 — Pourquoi la visualisation ?

Un Data Scientist passe une bonne moitié de son temps à **communiquer**. Tu peux avoir le meilleur modèle du monde, si ton dashboard n'est pas lisible, personne ne s'en servira.

Trois rôles principaux de la dataviz :

1. **Exploration** (EDA — Exploratory Data Analysis) : comprendre rapidement la forme des données.
2. **Diagnostic** : repérer un outlier, une corrélation, un biais.
3. **Communication** : convaincre un décideur, un PM, un client.

> Règle d'or : un graphique doit pouvoir être compris **sans le code** qui l'a produit, en moins de 10 secondes.

---

## Concept 2 — Choisir le bon graphique

Le type de graphique dépend de la **question** que tu te poses.

| Question | Type de graphique | Exemple |
|---|---|---|
| Comparer des catégories | Barplot (`bar`, `barh`) | Ventes par produit |
| Évolution dans le temps | Line plot (`plot`) | Cours d'une action |
| Distribution d'une variable | Histogramme (`hist`), boxplot | Répartition des âges |
| Relation entre 2 variables | Scatter plot | Prix vs surface |
| Part d'un tout | Camembert (`pie`) — **à éviter** | Préférer un barplot |
| Corrélations multiples | Heatmap | Matrice de corrélation |
| Plusieurs distributions | Violin plot, boxplot groupé | Salaires par poste |

### Anti-patterns à bannir

- **Camemberts à plus de 5 parts** → illisible, préférer un barplot trié.
- **Axes 3D** → presque toujours inutile, ça déforme la perception.
- **Axe Y qui ne commence pas à 0** sur un barplot → mensonge visuel.
- **Trop de couleurs** → max 5-6 couleurs distinctes par graphique.
- **Légendes redondantes** → si l'axe X dit déjà "années", pas besoin de légende "années".

---

## Concept 3 — Matplotlib : la base

Matplotlib est la **bibliothèque socle**. Toutes les autres (seaborn, pandas plot…) sont construites au-dessus. Connaître matplotlib = pouvoir customiser n'importe quoi.

### Anatomie d'un graphique

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))   # une figure + un axe
ax.plot([1, 2, 3], [10, 20, 15])         # tracer
ax.set_title("Mon titre")
ax.set_xlabel("Axe X")
ax.set_ylabel("Axe Y")
ax.legend(["Ma série"])
plt.tight_layout()
plt.show()
```

- `fig` = la **figure** entière (la fenêtre).
- `ax` = un **axe** dedans (un sous-graphique).

### Plusieurs graphiques côte à côte

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))   # 1 ligne, 2 colonnes
axes[0].plot([1, 2, 3], [4, 5, 6])
axes[0].set_title("Gauche")
axes[1].bar(["a", "b", "c"], [10, 20, 15])
axes[1].set_title("Droite")
plt.tight_layout()
plt.show()
```

### Sauvegarder un graphique

```python
fig.savefig("mon_graph.png", dpi=150, bbox_inches="tight")
```

---

## Concept 4 — Pandas plot (le raccourci)

Tu peux dessiner directement depuis un DataFrame :

```python
df["prix"].plot(kind="hist", bins=30)
df.plot(x="annee", y="ventes", kind="line")
df.groupby("produit")["prix"].mean().plot(kind="barh")
```

Sous le capot, c'est du matplotlib. Pratique pour l'EDA, mais limité dès qu'on veut un truc soigné.

---

## Concept 5 — Seaborn : matplotlib en plus joli

Seaborn ajoute :
- Un style par défaut beaucoup plus propre.
- Des graphiques statistiques de haut niveau (boxplot, violin, pairplot, heatmap).
- Une intégration parfaite avec les DataFrames Pandas.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# Boxplot du prix par catégorie
sns.boxplot(data=df, x="categorie", y="prix")
plt.show()

# Scatter plot avec une 3ème variable en couleur
sns.scatterplot(data=df, x="surface", y="prix", hue="ville")
plt.show()

# Heatmap d'une matrice de corrélation
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
```

### Graphiques utiles à connaître

| Fonction | À quoi ça sert |
|---|---|
| `sns.histplot` | Histogramme amélioré |
| `sns.boxplot` | Distribution + outliers |
| `sns.violinplot` | Distribution détaillée |
| `sns.scatterplot` | Nuage de points |
| `sns.lineplot` | Évolution dans le temps |
| `sns.heatmap` | Matrice (corrélations, confusion…) |
| `sns.pairplot` | Toutes les paires de variables d'un dataset |
| `sns.countplot` | Compter les occurrences d'une catégorie |

---

## Concept 6 — Plotly : l'interactif

Plotly permet de **zoomer, survoler, filtrer** directement dans le graphique. Indispensable pour les dashboards.

```python
import plotly.express as px

fig = px.scatter(
    df,
    x="surface",
    y="prix",
    color="ville",
    size="nb_pieces",
    hover_data=["adresse"],
    title="Prix immobilier",
)
fig.show()
```

Plotly Express (`px`) couvre 90 % des besoins. Pour du sur-mesure, il y a `plotly.graph_objects` (`go`).

### Graphiques classiques

```python
px.bar(df, x="produit", y="ventes")
px.line(df, x="date", y="cours", color="action")
px.histogram(df, x="prix", nbins=30)
px.box(df, x="categorie", y="prix")
px.pie(df, names="region", values="ventes")     # à utiliser avec parcimonie
```

---

## Concept 7 — Storytelling avec un graphique

Un bon graphique répond à **une seule question**. Trois niveaux de finition :

1. **Brouillon** (pendant l'EDA) : valeurs par défaut, on s'en fout du style.
2. **Présentable** : titre clair, axes labellisés, unités, légende lisible.
3. **Publication** : annotations, mise en avant d'un point clé, couleurs cohérentes avec la marque.

### Checklist avant de montrer un graphique

- [ ] Le **titre** énonce la conclusion, pas juste le sujet. Exemple : ❌ "Ventes par mois" → ✅ "Les ventes ont doublé entre janvier et juin".
- [ ] Les **axes** sont labellisés avec les **unités** (€, %, kg…).
- [ ] L'**axe Y commence à 0** (sauf cas justifié comme un cours boursier).
- [ ] Pas de **3D**, pas d'**effets** inutiles.
- [ ] Une **couleur** par catégorie, et c'est cohérent dans tout le rapport.
- [ ] **Annotations** sur les points clés (ex: "pic du COVID en mars 2020").

---

## Concept 8 — Couleurs et palettes

- Les couleurs **portent du sens**. Évite l'arc-en-ciel par défaut.
- Pour des données **catégorielles** : palette qualitative (`tab10`, `Set2`).
- Pour des données **ordonnées** (du froid au chaud) : palette séquentielle (`viridis`, `Blues`).
- Pour des données **divergentes** (négatif vs positif) : palette divergente (`coolwarm`, `RdBu`).
- Pense aux **daltoniens** : `viridis` et `cividis` sont sûres.

```python
sns.set_palette("Set2")
sns.color_palette("viridis", as_cmap=True)
```

---

## Partie B — Mise en pratique

Tous les fichiers vont dans `module3/`. Tu utiliseras des **notebooks** comme au module 2.

### Préparation

Dans le **Terminal.app**, depuis la racine du projet :

```bash
cd ~/Documents/formation-data-science/data-science-journey
source .venv/bin/activate
uv add matplotlib seaborn plotly
mkdir -p module3/data
mkdir -p module3/exports
```

Crée 3 notebooks dans `module3/` :
- `01_reproduction_graphiques.ipynb`
- `02_dashboard_plotly.ipynb`
- `03_critique_visuelle.ipynb`

---

## Exercice 1 — Reproduire 5 graphiques

### Objectif
Apprendre matplotlib/seaborn en **copiant** des graphiques existants. C'est l'exercice classique des designers : on apprend en imitant.

### Dataset

Tu vas utiliser le dataset **Gapminder** (PIB, espérance de vie, population par pays/année). Il est intégré à plotly :

```python
import plotly.express as px
df = px.data.gapminder()
df.head()
```

Colonnes : `country`, `continent`, `year`, `lifeExp`, `pop`, `gdpPercap`.

### Les 5 graphiques à reproduire

Pour chaque graphique, **une cellule markdown** qui explique :
- Quelle question le graphique répond.
- Pourquoi tu as choisi ce type de graphique.

Puis **une cellule code** qui le produit.

---

**Graphique 1 — Évolution de l'espérance de vie mondiale (line plot)**

- Axe X : `year`.
- Axe Y : espérance de vie moyenne mondiale (pondérée ou non, à toi de voir).
- Une ligne par continent.
- Titre, axes labellisés, légende propre.

Indice :
```python
data = df.groupby(["year", "continent"])["lifeExp"].mean().reset_index()
```

---

**Graphique 2 — Top 10 pays les plus peuplés en 2007 (barplot horizontal)**

- Filtre `year == 2007`.
- Tri décroissant.
- Affiche la valeur au bout de chaque barre.

Indice : `ax.bar_label(ax.containers[0])`.

---

**Graphique 3 — Distribution du PIB/habitant en 2007 (histogramme + log)**

- L'axe X doit être **en échelle logarithmique** (le PIB varie sur 4 ordres de grandeur).
- Indice : `ax.set_xscale("log")`.

---

**Graphique 4 — Espérance de vie vs PIB en 2007 (scatter)**

- Axe X : `gdpPercap` (en log).
- Axe Y : `lifeExp`.
- Couleur : continent.
- Taille : population.
- Tu reproduis le célèbre graphique de Hans Rosling.

Indice : avec seaborn, `sns.scatterplot(..., size="pop", hue="continent", sizes=(20, 1000))`.

---

**Graphique 5 — Heatmap espérance de vie par continent × décennie**

- Crée une colonne `decade` (ex: `(df["year"] // 10) * 10`).
- Pivote pour avoir continent en lignes, decade en colonnes, espérance de vie moyenne en valeur.
- `sns.heatmap(..., annot=True, fmt=".1f", cmap="YlGn")`.

### À me rendre
- Le notebook avec les 5 graphiques.
- Pour chacun, **une phrase** qui résume ce qu'on observe.

---

## Exercice 2 — Dashboard interactif Plotly

### Objectif
Construire un mini-dashboard interactif sur des ventes fictives. Tu vas générer le dataset toi-même.

### Données de départ

Dans `02_dashboard_plotly.ipynb`, cellule 1 :

```python
import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")
n = len(dates)

df = pd.DataFrame({
    "date": np.repeat(dates, 3),
    "produit": np.tile(["MacBook Air", "MacBook Pro", "iMac"], n),
    "ventes": rng.integers(0, 50, size=n * 3),
    "region": rng.choice(["Paris", "Lyon", "Marseille", "Bordeaux"], size=n * 3),
})
df["chiffre_affaires"] = df["ventes"] * df["produit"].map({
    "MacBook Air": 1100,
    "MacBook Pro": 1900,
    "iMac": 1500,
})
df.head()
```

### Questions à traiter

1. **Évolution mensuelle du CA** (line plot Plotly)
   - Agrège par mois (`df.resample("MS", on="date")`).
   - Une ligne par produit.
   - `px.line(...)`.

2. **CA total par région** (barplot)
   - `px.bar(...)`, trié par CA décroissant.

3. **Répartition des ventes par produit et par région** (sunburst ou treemap)
   - `px.sunburst(df, path=["region", "produit"], values="ventes")`.

4. **Boxplot du CA quotidien par produit**
   - `px.box(df, x="produit", y="chiffre_affaires")`.

5. **Carte de chaleur** : CA par mois × produit.
   - Astuce : passe par un `pivot_table` puis `px.imshow(...)`.

6. **Sauvegarde** : exporte un des graphiques en HTML interactif :
   ```python
   fig.write_html("module3/exports/dashboard_ca_mensuel.html")
   ```

### À me rendre
- Le notebook.
- Le fichier HTML exporté.
- 3 lignes de conclusion : quel produit / région / période ressort ?

---

## Exercice 3 — Critique visuelle

### Objectif
Affûter ton œil critique. Tu vas prendre un **mauvais graphique** et le **refaire correctement**.

### Étape 1 — Le mauvais graphique (à reproduire)

Dans `03_critique_visuelle.ipynb`, cellule 1, tu vas générer **volontairement** un graphique horrible :

```python
import matplotlib.pyplot as plt
import numpy as np

categories = ["Janv", "Févr", "Mars", "Avril", "Mai", "Juin"]
ventes_a = [120, 122, 121, 123, 124, 125]
ventes_b = [100, 105, 110, 115, 118, 120]

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(categories, ventes_a, color="red", label="Produit A")
ax.bar(categories, ventes_b, color="green", bottom=ventes_a, label="Produit B", alpha=0.3)
ax.set_ylim(95, 250)   # axe tronqué : MENSONGE
ax.set_title("VENTES !!!", fontsize=20)
ax.legend(loc="lower right", fontsize=6)
plt.show()
```

### Étape 2 — Cellule markdown : la critique

Liste au moins **5 problèmes** de ce graphique. Indices :
- L'axe Y commence-t-il à 0 ?
- Les couleurs sont-elles bien choisies (rouge/vert = piège pour les daltoniens) ?
- Le titre est-il informatif ?
- L'opacité sur la deuxième série, c'est judicieux ?
- La taille de la légende ?
- Le type de graphique (empilé) est-il pertinent pour comparer A et B ?

### Étape 3 — Le bon graphique

Refais-le proprement. Suggestions :
- Barplot **groupé** (côte à côte), pas empilé.
- Axe Y qui commence à 0.
- Couleurs sobres et accessibles (palette `Set2` ou `tab10`).
- Titre qui dit ce qu'on voit ("Le Produit B rattrape progressivement le Produit A").
- Légende de taille normale, bien placée.

### Étape 4 — Bonus

Refais le même graphique en **seaborn** puis en **plotly**. Compare le temps de code pour chacun.

### À me rendre
- Les 2 (ou 3) versions du graphique.
- La liste des problèmes identifiés.
- Une conclusion : laquelle des 3 bibliothèques tu préfères pour ce cas, et pourquoi.

---

## Validation du module

### Vérifications dans le terminal

```bash
cd ~/Documents/formation-data-science/data-science-journey
uv run ruff check module3/
ls module3/
ls module3/exports/
```

Tu dois voir tes 3 notebooks + le dossier `exports/` avec au moins un fichier HTML.

### Commit

```bash
git add module3/
git commit -m "feat(module3): dataviz matplotlib seaborn plotly"
git push
```

---

## Livrables à me rendre

1. **Lien GitHub** vers le dossier `module3/`.
2. **Pour chaque notebook**, capture (ou lien) des graphiques principaux :
   - Ex1 : les 5 graphiques.
   - Ex2 : les 5 visualisations + lien vers le HTML interactif.
   - Ex3 : le mauvais graphique + ta version corrigée.
3. **Tes critiques markdown** de l'Ex3 (les 5 problèmes identifiés).
4. **2-3 questions** sur ce qui t'a bloqué ou surpris.

---

## Erreurs fréquentes — Antisèche

| Symptôme | Cause | Solution |
|---|---|---|
| Le graphique ne s'affiche pas | Tu as oublié `plt.show()` ou `fig.show()` | Ajoute-le en fin de cellule |
| Les labels sont coupés | Marges trop petites | `plt.tight_layout()` |
| Texte des axes illisible / chevauchant | Labels trop longs | `plt.xticks(rotation=45)` |
| Couleurs incohérentes entre 2 graphiques | Palette non fixée | `sns.set_palette("Set2")` au début |
| Plotly ne s'affiche pas dans le notebook | Renderer non configuré | `import plotly.io as pio; pio.renderers.default = "vscode"` |
| Heatmap avec valeurs invisibles | `annot=False` par défaut | `sns.heatmap(..., annot=True, fmt=".2f")` |
| `KeyError` dans `px.line` | Nom de colonne mal orthographié | Vérifie `df.columns` |

---

## Checklist de fin de module

- [ ] Notebook 1 : 5 graphiques reproduits, chacun avec sa phrase d'observation
- [ ] Notebook 2 : dashboard Plotly (5 visus) + 1 HTML exporté
- [ ] Notebook 3 : mauvais graphique + critique + version corrigée
- [ ] `ruff check module3/` clean
- [ ] Tout est committé et pushé

---

**Prêt ? Commence par l'Exercice 1 (reproduction). Lis les Concepts 3 (matplotlib) et 5 (seaborn) avant. Pour le graphique de Hans Rosling, regarde sa fameuse TED talk de 2006 si tu veux comprendre la puissance d'une bonne dataviz. Dès que tu bloques, copie-colle ton code ici.**
