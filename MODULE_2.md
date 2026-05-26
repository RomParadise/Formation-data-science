# Module 2 — NumPy & Pandas

> Objectif : maîtriser les deux bibliothèques fondamentales du quotidien en data science.
> Durée estimée : 2 semaines (15-20 heures).
> Pré-requis : Module 1 terminé.

---

## Vue d'ensemble

À la fin de ce module, tu seras capable de :

1. Manipuler des tableaux NumPy (création, indexing, broadcasting, opérations vectorisées).
2. Charger un dataset avec Pandas (CSV, Excel, JSON).
3. Explorer et nettoyer un dataset (NaN, doublons, types).
4. Filtrer, trier, grouper, joindre des DataFrames.
5. Calculer des statistiques par groupe (groupby).
6. Comprendre la différence entre `.loc`, `.iloc`, et le boolean indexing.

---

## Partie A — Théorie

## Concept 1 — Pourquoi NumPy ?

### Le problème des listes Python

```python
# Avec une liste Python, multiplier chaque élément par 2
prices = [10, 20, 30, 40]
doubled = []
for p in prices:
    doubled.append(p * 2)
# → [20, 40, 60, 80]
```

C'est lisible mais **lent** sur de gros volumes (millions de valeurs).

### La solution NumPy

NumPy stocke les données dans un tableau **contigu en mémoire** et applique les opérations en C compilé. Résultat : 10 à 100× plus rapide.

```python
import numpy as np

prices = np.array([10, 20, 30, 40])
doubled = prices * 2     # opération sur tout le tableau d'un coup
# → array([20, 40, 60, 80])
```

C'est ce qu'on appelle la **vectorisation** : pas de boucle Python, tout se passe en interne.

---

## Concept 2 — Créer des tableaux NumPy

```python
import numpy as np

# Depuis une liste
a = np.array([1, 2, 3, 4])

# Tableau de zéros / uns
zeros = np.zeros(5)             # [0. 0. 0. 0. 0.]
ones = np.ones((3, 2))          # tableau 3x2 de 1

# Séquences
r = np.arange(0, 10, 2)         # [0 2 4 6 8]
l = np.linspace(0, 1, 5)        # [0. 0.25 0.5 0.75 1.]

# Aléatoire
rng = np.random.default_rng(seed=42)
rand = rng.random(5)            # 5 valeurs entre 0 et 1
normal = rng.normal(0, 1, 100)  # 100 valeurs gaussiennes

# Propriétés
a.shape    # (4,) — forme du tableau
a.dtype    # int64 — type des éléments
a.ndim     # 1 — nombre de dimensions
```

### Tableaux 2D (matrices)

```python
m = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
m.shape   # (2, 3)
m[0, 1]   # 2 (ligne 0, colonne 1)
m[:, 0]   # [1, 4] (toute la colonne 0)
m[1, :]   # [4, 5, 6] (toute la ligne 1)
```

---

## Concept 3 — Indexing et slicing

```python
a = np.array([10, 20, 30, 40, 50])

a[0]       # 10
a[-1]      # 50 (dernier)
a[1:4]     # [20, 30, 40]
a[::2]     # [10, 30, 50] (un sur deux)
```

### Boolean indexing (très utilisé)

On sélectionne les éléments selon une condition.

```python
ages = np.array([18, 25, 16, 35, 12, 42])

# Masque booléen
mask = ages >= 18
# → [True, True, False, True, False, True]

# Sélection
adults = ages[mask]
# → [18, 25, 35, 42]

# Plus court
adults = ages[ages >= 18]

# Combinaisons (utiliser & et |, pas and/or)
young_adults = ages[(ages >= 18) & (ages <= 30)]
# → [18, 25]
```

---

## Concept 4 — Broadcasting

Le broadcasting permet d'opérer entre tableaux de formes différentes sans boucle.

```python
prices = np.array([100, 200, 300])
tva = 1.20

# Le scalaire est "diffusé" sur tout le tableau
prices_with_tva = prices * tva
# → [120, 240, 360]

# Entre deux tableaux compatibles
quantities = np.array([1, 2, 3])
totals = prices * quantities
# → [100, 400, 900]

# Soustraire la moyenne (centrer les données)
data = np.array([10, 20, 30, 40, 50])
centered = data - data.mean()
# → [-20, -10, 0, 10, 20]
```

---

## Concept 5 — Opérations vectorisées utiles

```python
a = np.array([1, 4, 9, 16, 25])

a.sum()      # 55
a.mean()     # 11.0
a.min()      # 1
a.max()      # 25
a.std()      # écart-type
np.sqrt(a)   # [1. 2. 3. 4. 5.]
np.log(a)    # log naturel

# Sur un tableau 2D, axis= contrôle l'axe
m = np.array([[1, 2], [3, 4], [5, 6]])
m.sum(axis=0)   # [9, 12]   (somme par colonne)
m.sum(axis=1)   # [3, 7, 11] (somme par ligne)
```

---

## Concept 6 — Pandas : DataFrame et Series

### Series = colonne 1D avec un index

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
s["a"]     # 10
s.mean()   # 20.0
```

### DataFrame = tableau 2D (lignes × colonnes nommées)

```python
df = pd.DataFrame({
    "produit": ["MacBook Pro", "iMac", "MacBook Air"],
    "prix": [899, 749, 599],
    "stock": [5, 2, 10],
})

#        produit  prix  stock
# 0   MacBook Pro   899      5
# 1          iMac   749      2
# 2   MacBook Air   599     10
```

### Inspection rapide

```python
df.head()         # 5 premières lignes
df.tail(3)        # 3 dernières
df.shape          # (3, 3)
df.columns        # ['produit', 'prix', 'stock']
df.dtypes         # type de chaque colonne
df.info()         # résumé complet
df.describe()     # statistiques descriptives (count, mean, std, min, max, quartiles)
```

---

## Concept 7 — Charger un fichier

```python
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
```

---

## Concept 8 — Sélectionner des colonnes et des lignes

### Sélectionner une colonne (= Series)

```python
df["prix"]              # Series
df[["prix", "stock"]]   # DataFrame à 2 colonnes
```

### Filtrer des lignes (boolean indexing)

```python
df[df["prix"] > 700]
df[(df["prix"] > 600) & (df["stock"] >= 5)]
df[df["produit"].str.contains("MacBook")]
```

### `.loc` vs `.iloc`

| Méthode | Sélection par |
|---|---|
| `.loc` | **étiquette** (nom de colonne, valeur d'index) |
| `.iloc` | **position** (numéro de ligne / colonne) |

```python
df.loc[0, "prix"]         # 899 (par étiquette)
df.iloc[0, 1]             # 899 (par position : ligne 0, colonne 1)

df.loc[df["prix"] > 700, ["produit", "prix"]]   # filtre + sélection
```

---

## Concept 9 — Valeurs manquantes (NaN)

`NaN` = "Not a Number", équivalent de `None` pour pandas.

```python
df.isna()           # DataFrame de booléens
df.isna().sum()     # nombre de NaN par colonne

# Supprimer les lignes avec au moins un NaN
df_clean = df.dropna()

# Remplacer les NaN
df["prix"] = df["prix"].fillna(df["prix"].mean())   # par la moyenne
df["categorie"] = df["categorie"].fillna("inconnu")  # par une valeur
```

---

## Concept 10 — groupby

C'est l'opération **la plus utilisée** en data science : grouper par une colonne et calculer une stat par groupe.

```python
ventes = pd.DataFrame({
    "produit": ["Mac", "iPhone", "Mac", "iPhone", "Mac"],
    "prix": [1000, 800, 1100, 850, 950],
    "vendeur": ["A", "A", "B", "B", "A"],
})

# Prix moyen par produit
ventes.groupby("produit")["prix"].mean()
# produit
# Mac       1016.67
# iPhone     825.00

# Plusieurs agrégations en même temps
ventes.groupby("produit")["prix"].agg(["mean", "min", "max", "count"])

# Grouper par plusieurs colonnes
ventes.groupby(["produit", "vendeur"])["prix"].mean()
```

---

## Concept 11 — Trier, ajouter, modifier

```python
# Trier
df.sort_values("prix", ascending=False)
df.sort_values(["categorie", "prix"], ascending=[True, False])

# Ajouter une colonne calculée
df["prix_ttc"] = df["prix"] * 1.20

# Modifier conditionnellement
df["categorie"] = df["prix"].apply(lambda p: "cher" if p > 1000 else "abordable")

# Renommer
df = df.rename(columns={"prix": "price_ht"})
```

---

## Concept 12 — Joindre des DataFrames (merge)

Équivalent du JOIN SQL.

```python
clients = pd.DataFrame({"id": [1, 2, 3], "nom": ["Alice", "Bob", "Charlie"]})
commandes = pd.DataFrame({"client_id": [1, 1, 2], "montant": [50, 75, 100]})

# Jointure
merged = commandes.merge(clients, left_on="client_id", right_on="id", how="left")
```

`how=` peut être `"left"`, `"right"`, `"inner"`, `"outer"`.

---

## Partie B — Mise en pratique

Tous les fichiers vont dans `module2/`. Tu utiliseras des **notebooks** (`.ipynb`) cette fois — c'est l'outil naturel pour explorer des données.

### Préparation

Dans le **Terminal.app**, depuis la racine du projet :

```bash
cd ~/Documents/formation-data-science/data-science-journey
mkdir -p module2/data
```

Crée les notebooks vides depuis VS Code (`Cmd + N` → enregistrer en `.ipynb`) :
- `module2/01_numpy_moyenne_mobile.ipynb`
- `module2/02_titanic.ipynb`
- `module2/03_airbnb.ipynb`
- `module2/04_dataset_sale.ipynb`

N'oublie pas de **sélectionner le kernel `.venv`** en haut à droite de chaque notebook (comme au Module 0).

---

## Exercice 1 — Moyenne mobile en NumPy

### Énoncé
Implémenter une moyenne mobile (rolling mean) **sans boucle Python**, en utilisant uniquement NumPy.

### Notebook `01_numpy_moyenne_mobile.ipynb`

**Cellule 1 (markdown)** — Titre et explication :
```markdown
# Moyenne mobile en NumPy

La moyenne mobile sur fenêtre k consiste à remplacer chaque valeur par la moyenne des k valeurs précédentes (elle-même incluse).

Exemple avec k=3 sur [1, 2, 3, 4, 5] :
- position 2 : (1+2+3)/3 = 2.0
- position 3 : (2+3+4)/3 = 3.0
- position 4 : (3+4+5)/3 = 4.0

Les k-1 premières positions sont sans valeur.
```

**Cellule 2 (code)** — Imports + données :
```python
import numpy as np

prices = np.array([100, 102, 101, 105, 110, 108, 112, 115, 113, 118])
```

**Cellule 3 (code)** — Implémentation :
```python
def moving_average(arr: np.ndarray, window: int) -> np.ndarray:
    """Moyenne mobile sans boucle Python.

    Indice : utilise np.cumsum() pour calculer une somme cumulée,
    puis fais la différence entre deux positions pour obtenir la somme glissante.
    """
    # À TOI DE JOUER
    raise NotImplementedError


# Test rapide
print(moving_average(prices, 3))
```

### Indices

- `np.cumsum([1, 2, 3, 4, 5])` → `[1, 3, 6, 10, 15]`
- Pour avoir la somme des éléments `[i-k+1 : i+1]`, fais `cumsum[i] - cumsum[i-k]`.
- Tu peux remplir le début (positions 0 à k-2) avec `np.nan`.

### Vérification
Pour `prices` avec `window=3`, tu dois obtenir :
```
[nan, nan, 101.0, 102.67, 105.33, 107.67, 110.0, 111.67, 113.33, 115.33]
```

Compare avec la méthode pandas pour valider :
```python
import pandas as pd
pd.Series(prices).rolling(3).mean().values
```

---

## Exercice 2 — Titanic

### Énoncé
Sur le dataset **Titanic**, calculer plusieurs taux de survie.

### Préparation du dataset
Dans le notebook `02_titanic.ipynb` :

```python
import pandas as pd

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(URL)
df.head()
```

Colonnes utiles :
- `Survived` (0/1)
- `Pclass` (1, 2, 3 — classe)
- `Sex` (male/female)
- `Age`
- `Fare`

### Questions à répondre dans le notebook

1. **Aperçu global** : `df.info()`, `df.describe()`, `df.isna().sum()`. Combien de passagers ? Combien de NaN par colonne ?

2. **Taux de survie global** : pourcentage de survivants.

3. **Taux de survie par classe** : utilise `groupby` sur `Pclass`.

4. **Taux de survie par sexe**.

5. **Taux de survie croisé classe × sexe** : `groupby(["Pclass", "Sex"])["Survived"].mean()`.

6. **Tranches d'âge** : crée une colonne `AgeGroup` avec :
   - "enfant" si Age < 18
   - "adulte" si 18 ≤ Age < 60
   - "senior" si Age ≥ 60
   - "inconnu" si NaN

   Puis taux de survie par `AgeGroup`.

7. **Conclusion (cellule markdown)** : en 3-4 lignes, explique ce que les données révèlent.

### Indice pour la question 6
```python
def age_group(age):
    if pd.isna(age):
        return "inconnu"
    if age < 18:
        return "enfant"
    # à toi de continuer

df["AgeGroup"] = df["Age"].apply(age_group)
```

---

## Exercice 3 — Airbnb Paris

### Énoncé
Trouver les 10 quartiers de Paris les plus chers en médiane.

### Préparation
Pour simplifier, on va utiliser un dataset inside Airbnb. Dans le notebook `03_airbnb.ipynb` :

```python
import pandas as pd

URL = "http://data.insideairbnb.com/france/ile-de-france/paris/2024-09-06/visualisations/listings.csv"
df = pd.read_csv(URL)
df.head()
```

> Si l'URL ne marche plus, va sur http://insideairbnb.com/get-the-data/ section Paris et prends le `listings.csv` "summary".

Colonnes utiles :
- `neighbourhood`
- `price`
- `room_type`
- `minimum_nights`

### Questions à traiter

1. **Nettoyage du prix** : la colonne `price` est parfois en string (ex: `"$120.00"`). Convertis-la en float.

   ```python
   # Si c'est déjà du float, skip. Sinon :
   df["price"] = (
       df["price"]
       .astype(str)
       .str.replace("$", "", regex=False)
       .str.replace(",", "", regex=False)
       .astype(float)
   )
   ```

2. **Filtres logiques** : garde uniquement les logements où :
   - `price` entre 20 et 1000 (on enlève les valeurs aberrantes)
   - `minimum_nights` ≤ 30

3. **Top 10 quartiers par prix médian** :
   ```python
   df.groupby("neighbourhood")["price"].median().sort_values(ascending=False).head(10)
   ```

4. **Bonus** : Prix médian par `room_type` (Entire home, Private room, etc.).

5. **Visualisation** : trace un barplot des top 10 :
   ```python
   import matplotlib.pyplot as plt

   top10 = df.groupby("neighbourhood")["price"].median().sort_values(ascending=False).head(10)
   top10.plot(kind="barh")
   plt.xlabel("Prix médian (€/nuit)")
   plt.title("Top 10 quartiers Airbnb Paris")
   plt.tight_layout()
   plt.show()
   ```

6. **Conclusion (cellule markdown)** : 3 lignes sur ce que tu observes.

---

## Exercice 4 — Nettoyer un dataset "sale"

### Énoncé
On simule un dataset OKAMAC avec des problèmes typiques : NaN, doublons, types incohérents, valeurs aberrantes.

### Données de départ

Dans le notebook `04_dataset_sale.ipynb`, cellule 1 :

```python
import pandas as pd
import numpy as np

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 11],
    "modele": ["MacBook Air", "MacBook Pro", "iMac 21", None, "MacBook Air",
               "MacBook Pro", "iMac 27", "MacBook Air", "MacBook Pro", "iMac 21",
               "MacBook Air", "MacBook pro"],   # casse incohérente
    "annee": [2020, 2021, 2019, 2022, 2020, 2021, "2018", 2020, 2021, 2019, 2020, 2021],
    "prix": ["599", "899", "749", "699", "550", "950", "1299", None, "920", "740", "550", "99999"],
    "etat": ["bon", "très bon", "correct", "neuf", "bon", "très bon", "bon",
             "correct", "très bon", None, "bon", "très bon"],
}

df = pd.DataFrame(data)
df
```

### Étapes de nettoyage à effectuer

Crée une cellule par étape avec une cellule markdown qui explique ce que tu fais.

1. **Détecter les NaN** : `df.isna().sum()`.

2. **Détecter les doublons** : `df.duplicated()` puis `df[df.duplicated()]`. Combien tu en as ?

3. **Supprimer les doublons** : `df = df.drop_duplicates()` (par défaut, sur toutes les colonnes — ici tu peux faire `subset="id"` car l'id doit être unique).

4. **Corriger le type de `annee`** : actuellement c'est un mélange int/str. Convertis tout en int :
   ```python
   df["annee"] = df["annee"].astype(int)
   ```

5. **Corriger le type de `prix`** : convertis en float.

6. **Normaliser `modele`** : tout en title case pour gérer "MacBook pro" vs "MacBook Pro" :
   ```python
   df["modele"] = df["modele"].str.title()
   ```

7. **Gérer les NaN** :
   - `modele` NaN → ligne à supprimer (impossible à imputer).
   - `prix` NaN → remplacer par la médiane du modèle correspondant. Indice :
     ```python
     df["prix"] = df.groupby("modele")["prix"].transform(lambda s: s.fillna(s.median()))
     ```
   - `etat` NaN → remplacer par `"inconnu"`.

8. **Détecter les outliers de prix** : le 99999 est aberrant. Utilise la règle classique : tout ce qui est > Q3 + 1.5 × IQR est suspect.
   ```python
   q1 = df["prix"].quantile(0.25)
   q3 = df["prix"].quantile(0.75)
   iqr = q3 - q1
   limite_haute = q3 + 1.5 * iqr
   outliers = df[df["prix"] > limite_haute]
   ```

9. **Décision** : supprime les outliers du DataFrame.

10. **Vérification finale** : affiche `df.info()` et `df.describe()`. Plus aucun NaN, types corrects, pas d'outliers.

### Sauvegarde

```python
df.to_csv("module2/data/okamac_clean.csv", index=False)
```

---

## Validation du module

### Vérifications dans le terminal

```bash
cd ~/Documents/formation-data-science/data-science-journey
uv run ruff check module2/
ls module2/
```

Tu dois voir tes 4 notebooks + le dossier `data/`.

### Commit
```bash
git add module2/
git commit -m "feat(module2): numpy moving avg, titanic, airbnb, cleaning"
git push
```

---

## Livrables à me rendre

1. **Lien GitHub** vers le dossier `module2/`.
2. **Pour chaque notebook**, l'output principal :
   - Ex1 : valeur retournée par `moving_average(prices, 3)`.
   - Ex2 : taux de survie croisé classe × sexe.
   - Ex3 : top 10 quartiers + le barplot.
   - Ex4 : `df.info()` et `df.describe()` final.
3. **Tes conclusions markdown** des Ex2 et Ex3.
4. **2-3 questions** sur des concepts qui t'ont surpris ou bloqué.

---

## Erreurs fréquentes — Antisèche

| Symptôme | Cause | Solution |
|---|---|---|
| `SettingWithCopyWarning` | Tu modifies une vue d'un DataFrame | Utilise `.loc[]` ou `.copy()` |
| `KeyError: 'nom_colonne'` | Faute de frappe ou espace dans le nom | Vérifie `df.columns` |
| `TypeError` avec `&` ou `\|` | Tu utilises `and`/`or` | Utilise `&`/`\|` avec parenthèses |
| `ValueError` lors du `groupby` | NaN dans la colonne de groupage | `df.dropna(subset=["col"])` avant |
| Le barplot ne s'affiche pas | Kernel ≠ `.venv` | Sélectionne le bon kernel |

---

## Checklist de fin de module

- [ ] Notebook 1 : `moving_average` fonctionne et le résultat correspond à `pandas.rolling`
- [ ] Notebook 2 : 6 questions Titanic traitées + conclusion
- [ ] Notebook 3 : Top 10 quartiers + barplot + conclusion
- [ ] Notebook 4 : Dataset nettoyé sauvegardé, plus aucun NaN/outlier
- [ ] `ruff check module2/` clean
- [ ] Tout est committé et pushé

---

**Prêt ? Commence par l'Exercice 1 (NumPy). Lis le Concept 5 (opérations vectorisées) et le Concept 2 (création) si tu as un doute. Pour l'algo de la moyenne mobile, l'astuce `cumsum` est dans les indices. Dès que tu bloques, copie-colle ton code ici.**
