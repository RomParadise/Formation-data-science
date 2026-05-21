# Module 1 — Python pour la Data Science

> Objectif : maîtriser le Python "pro" qu'on utilise au quotidien en Data Science.
> Durée estimée : 2 semaines (10 à 15 heures de travail effectif).
> Pré-requis : Module 0 terminé.

---

## Vue d'ensemble

À la fin de ce module, tu seras capable de :

1. Manipuler les types et structures Python natifs avec aisance (list, dict, set, tuple).
2. Écrire des fonctions propres avec **type hints** et **docstrings**.
3. Construire des classes simples (OOP de base).
4. Lire/écrire des fichiers (CSV, JSON, texte).
5. Gérer les erreurs proprement (`try/except`).
6. Écrire des tests unitaires avec **pytest**.
7. Respecter **PEP8** et faire passer **ruff** sans warning.

---

## Partie A — Théorie / Besoins

### Pourquoi Python en Data Science ?

- **Lisible** : proche du pseudo-code, idéal pour communiquer un raisonnement.
- **Ecosystème** : NumPy, pandas, scikit-learn, PyTorch, TensorFlow… tout est en Python.
- **Polyvalent** : script, notebook, API, microservice, ML pipeline.

---

## Concept 1 — Fonctions, type hints et docstrings

### Fonction de base

Une fonction prend des données en entrée et retourne un résultat. En data science, on écrit des **fonctions pures** : pas d'effets de bord, même entrée = même sortie.

```python
def add(a, b):
    return a + b
```

### Type hints (annotations de types)

Python est un langage dynamique, mais on peut (et doit) annoter les types pour rendre le code lisible et détectable par les outils.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Bonjour {name}"

# Avec des types complexes
def mean(values: list[float]) -> float:
    return sum(values) / len(values)

# Valeur optionnelle (peut être None)
def find(items: list[str], target: str) -> str | None:
    for item in items:
        if item == target:
            return item
    return None
```

### Docstrings

La docstring documente ce que fait la fonction. Elle s'écrit juste après `def`, entre triple guillemets :

```python
def word_count(text: str) -> dict[str, int]:
    """Return word frequencies sorted by descending count.

    Args:
        text: Input text to analyze.

    Returns:
        Dict mapping each lowercase word to its frequency.
    """
    # ton code ici
```

---

## Concept 2 — Structures de données natives

### dict (dictionnaire)

Un dictionnaire associe des **clés** à des **valeurs**. C'est la structure la plus utilisée en data.

```python
# Créer
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Lire
print(scores["Alice"])    # 95
print(scores.get("Zoe", 0))  # 0 (valeur par défaut si clé absente)

# Ajouter / modifier
scores["Zoe"] = 78

# Itérer
for name, score in scores.items():
    print(f"{name} : {score}")

# Trier par valeur décroissante
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
# → {"Alice": 95, "Charlie": 92, "Bob": 87, "Zoe": 78}
```

### list comprehension

Au lieu d'écrire une boucle for + append, on peut créer une liste en une ligne :

```python
# Boucle classique
numbers = []
for x in range(10):
    numbers.append(x * 2)

# Équivalent en comprehension (préféré)
numbers = [x * 2 for x in range(10)]

# Avec condition
evens = [x for x in range(20) if x % 2 == 0]
```

---

## Concept 3 — Gestion d'erreurs (try/except)

En production, les données peuvent être sales, les fichiers absents, les valeurs invalides. On doit gérer ça proprement.

```python
# Lever une erreur
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro")
    return a / b

# Attraper une erreur
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Erreur : {e}")

# Plusieurs types d'erreurs
try:
    f = open("data.csv")
except FileNotFoundError:
    print("Fichier introuvable")
except PermissionError:
    print("Pas les droits pour lire ce fichier")
```

Les types d'erreurs courants :
| Exception | Quand |
|---|---|
| `ValueError` | Valeur invalide (ex: nombre négatif) |
| `KeyError` | Clé absente dans un dict |
| `FileNotFoundError` | Fichier inexistant |
| `TypeError` | Mauvais type passé à une fonction |
| `ZeroDivisionError` | Division par zéro |

---

## Concept 4 — Expressions régulières (regex) — pour l'Exercice 1

### C'est quoi ?

Une regex est un **motif de texte** qui permet de rechercher, extraire ou remplacer des parties d'une chaîne. Le module Python s'appelle `re`.

### Les patterns de base

| Pattern | Signification | Exemple |
|---|---|---|
| `\w` | Un caractère mot (lettre, chiffre, `_`) | `a`, `Z`, `3` |
| `\W` | Tout ce qui n'est PAS un caractère mot | `,`, `!`, ` ` |
| `\s` | Espace blanc (espace, tabulation, saut de ligne) | ` `, `\t` |
| `[abc]` | Un caractère parmi a, b ou c | `a` ou `b` ou `c` |
| `[^abc]` | Tout sauf a, b, c | `z`, `1` |
| `+` | Un ou plusieurs du caractère précédent | `\w+` = un mot entier |
| `*` | Zéro ou plusieurs | |

### Utilisation pratique

```python
import re

text = "Bonjour, monde! Hello world."

# Trouver tous les mots (séquences de caractères word)
words = re.findall(r"\w+", text)
# → ["Bonjour", "monde", "Hello", "world"]

# Remplacer la ponctuation par rien
clean = re.sub(r"[^\w\s]", "", text)
# → "Bonjour monde Hello world"

# Remplacer la ponctuation par un espace
clean2 = re.sub(r"[,\.!?;:]", " ", text)
# → "Bonjour  monde  Hello world "
```

### La méthode la plus simple pour les mots

```python
import re

def get_words(text: str) -> list[str]:
    """Extrait tous les mots d'un texte, en minuscules."""
    return re.findall(r"\w+", text.lower())

print(get_words("Hello, World! Hello."))
# → ["hello", "world", "hello"]
```

### Compter avec un dict

```python
words = ["hello", "world", "hello", "hello"]

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 0 + 1

# Façon plus courte avec .get()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# → {"hello": 3, "world": 1}
```

Tu as maintenant tous les outils pour faire l'Exercice 1.

---

## Concept 5 — Classes et programmation orientée objet — pour l'Exercice 2

### Pourquoi les classes ?

Une classe regroupe des **données** (attributs) et des **comportements** (méthodes) dans un seul objet. En data science on en a besoin pour modéliser des entités : un utilisateur, une transaction, un modèle ML.

### Anatomie d'une classe

```python
class Dog:
    # __init__ est le constructeur : appelé quand on crée un objet
    def __init__(self, name: str, age: int):
        self.name = name    # attribut d'instance
        self.age = age

    # méthode : fonction liée à l'objet
    def bark(self) -> str:
        return f"{self.name} dit : Woof!"

    def is_puppy(self) -> bool:
        return self.age < 2


# Créer un objet (instance)
rex = Dog("Rex", 3)
luna = Dog("Luna", 1)

print(rex.bark())       # "Rex dit : Woof!"
print(luna.is_puppy())  # True
print(rex.name)         # "Rex"
```

**`self`** : représente l'instance elle-même. Toujours premier paramètre des méthodes.

### Classe avec historique

```python
class ShoppingCart:
    def __init__(self, owner: str):
        self.owner = owner
        self.items: list[dict] = []   # liste vide au départ
        self.total: float = 0.0

    def add_item(self, name: str, price: float) -> None:
        if price <= 0:
            raise ValueError(f"Prix invalide : {price}")
        self.items.append({"name": name, "price": price})
        self.total += price

    def remove_last(self) -> None:
        if not self.items:
            raise ValueError("Le panier est vide")
        item = self.items.pop()         # retire le dernier élément
        self.total -= item["price"]

    def summary(self) -> str:
        return f"{self.owner} : {len(self.items)} article(s), total = {self.total:.2f}€"


# Utilisation
cart = ShoppingCart("Alice")
cart.add_item("MacBook", 899.0)
cart.add_item("Souris", 29.0)
print(cart.summary())  # "Alice : 2 article(s), total = 928.00€"
```

Tu vois le principe ? `BankAccount` sera très similaire à `ShoppingCart`.

---

## Concept 6 — Module `csv` — pour l'Exercice 3

Python a un module natif `csv` pour lire des fichiers CSV sans pandas.

```python
import csv

# Lire un fichier CSV
with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)   # chaque ligne devient un dict
    for row in reader:
        print(row)
        # → {"date": "2026-01-15", "product": "MacBook Pro", "price": "899.00"}
```

`DictReader` utilise la première ligne comme noms de colonnes. Les valeurs sont toutes des **chaînes de caractères** — il faut convertir en float pour faire des calculs :

```python
price = float(row["price"])   # "899.00" → 899.0
```

---

## Concept 7 — Tests unitaires avec pytest

### Pourquoi tester ?

Un test vérifie automatiquement qu'une fonction fait ce qu'on attend. Quand tu modifies du code, les tests te disent immédiatement si tu as cassé quelque chose.

### Structure d'un test

```python
# fichier test_xxx.py

def test_nom_descriptif():
    # 1. Prépare les données
    texte = "bonjour monde"

    # 2. Appelle la fonction
    resultat = word_count(texte)

    # 3. Vérifie le résultat
    assert resultat == {"bonjour": 1, "monde": 1}
```

`assert` vérifie que l'expression est vraie. Si ce n'est pas le cas, le test échoue avec un message clair.

### Tester qu'une erreur est bien levée

```python
import pytest

def test_valeur_negative_leve_erreur():
    with pytest.raises(ValueError):
        ma_fonction(-1)    # doit lever ValueError
```

### Lancer les tests

```bash
# Tous les tests d'un fichier
uv run pytest module1/tests/test_word_count.py -v

# Tous les tests du module
uv run pytest module1/ -v

# Le -v (verbose) affiche chaque test avec son statut
```

---

## Concept 8 — PEP8 et ruff

PEP8 = les conventions de style Python. `ruff` les vérifie automatiquement.

Les règles les plus importantes :
```python
# ❌ Mauvais
def f(l,x):
    if x==None:
        return 0
    return l[0]+x

# ✅ Bon
def compute(values: list[float], extra: float | None) -> float:
    if extra is None:
        return 0.0
    return values[0] + extra
```

Règles clés :
- Espaces autour des opérateurs : `a + b` pas `a+b`
- Pas d'espace avant `:` dans les defs : `def f(a, b):` pas `def f( a,b ) :`
- `is None` / `is not None` (jamais `== None`)
- Noms explicites : `word_count` pas `wc` ou `f`
- 2 lignes vides entre les fonctions

Vérifier ton fichier :
```bash
uv run ruff check module1/word_count.py
# Si rien ne s'affiche = pas d'erreur ✓
```

---

## Partie B — Mise en pratique

> Tous les fichiers vont dans `~/Documents/formation-data-science/data-science-journey/module1/`.

### Préparation du dossier

Dans le **Terminal.app**, depuis la racine du projet :

```bash
cd ~/Documents/formation-data-science/data-science-journey
mkdir -p module1/tests
touch module1/__init__.py module1/tests/__init__.py
```

Vérifie que `ruff` et `pytest` sont bien installés (faits au Module 0) :

```bash
uv run ruff --version
uv run pytest --version
```

---

## Exercice 1 — `word_count`

### Énoncé
Écrire une fonction qui compte la fréquence des mots d'un texte.

### Spécifications
- Signature : `def word_count(text: str) -> dict[str, int]`
- Insensible à la casse (`"Bonjour bonjour"` → `{"bonjour": 2}`).
- Ignore la ponctuation (`,`, `.`, `!`, `?`, `;`, `:`).
- Retourne un dict trié par valeur décroissante.
- Si `text` est vide, retourne `{}`.

### À créer
Fichier `module1/word_count.py` :

```python
"""Word frequency counter."""


def word_count(text: str) -> dict[str, int]:
    """Return word frequencies sorted by descending count.

    Args:
        text: Input text to analyze.

    Returns:
        Dict mapping each lowercase word to its frequency.
    """
    # TODO: implement
    raise NotImplementedError
```

### Tests à faire passer
Fichier `module1/tests/test_word_count.py` :

```python
from module1.word_count import word_count


def test_empty_string():
    assert word_count("") == {}


def test_simple():
    assert word_count("hello world hello") == {"hello": 2, "world": 1}


def test_case_insensitive():
    assert word_count("Bonjour bonjour BONJOUR") == {"bonjour": 3}


def test_punctuation():
    result = word_count("Hello, world! Hello.")
    assert result == {"hello": 2, "world": 1}


def test_sorted_descending():
    result = word_count("a b b c c c")
    assert list(result.keys()) == ["c", "b", "a"]
```

### Lancer les tests
```bash
cd ~/Documents/formation-data-science/data-science-journey
uv run pytest module1/tests/test_word_count.py -v
```

### Indices (si tu bloques)
- Module utile : `re` (regex) ou simplement `str.replace`.
- Pour trier un dict par valeur : `dict(sorted(d.items(), key=lambda x: x[1], reverse=True))`.
- `collections.Counter` peut aider mais essaie d'abord sans.

---

## Exercice 2 — Classe `BankAccount`

### Énoncé
Modéliser un compte bancaire avec historique des opérations.

### Spécifications
- Classe `BankAccount(owner: str, balance: float = 0.0)`.
- Méthode `deposit(amount: float) -> None` : ajoute au solde, refuse si `amount <= 0`.
- Méthode `withdraw(amount: float) -> None` : retire du solde, refuse si `amount <= 0` ou si solde insuffisant.
- Attribut `history: list[dict]` : chaque opération est un dict `{"type": "deposit"|"withdraw", "amount": float, "balance_after": float}`.
- Refus = lever une `ValueError` avec un message clair.

### À créer
Fichier `module1/bank_account.py`.

### Tests à faire passer
Fichier `module1/tests/test_bank_account.py` :

```python
import pytest
from module1.bank_account import BankAccount


def test_initial_balance():
    acc = BankAccount("Alice")
    assert acc.balance == 0.0
    assert acc.history == []


def test_deposit():
    acc = BankAccount("Alice")
    acc.deposit(100)
    assert acc.balance == 100
    assert acc.history[-1] == {"type": "deposit", "amount": 100, "balance_after": 100}


def test_withdraw():
    acc = BankAccount("Alice", balance=200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_deposit_negative_raises():
    acc = BankAccount("Alice")
    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_withdraw_insufficient_raises():
    acc = BankAccount("Alice", balance=10)
    with pytest.raises(ValueError):
        acc.withdraw(100)


def test_history_order():
    acc = BankAccount("Alice")
    acc.deposit(100)
    acc.deposit(50)
    acc.withdraw(30)
    assert len(acc.history) == 3
    assert acc.balance == 120
```

### Lancer
```bash
uv run pytest module1/tests/test_bank_account.py -v
```

---

## Exercice 3 — Lire un CSV "à la main"

### Énoncé
Sans utiliser `pandas`, lire un fichier CSV et calculer la moyenne d'une colonne numérique.

### Préparation
Crée le fichier `module1/data/sales.csv` avec ce contenu :

```csv
date,product,quantity,price
2026-01-15,MacBook Pro 13,2,899.00
2026-01-16,iMac 21,1,749.50
2026-01-17,MacBook Air,3,599.00
2026-01-18,MacBook Pro 13,1,899.00
2026-01-19,iMac 27,2,1299.00
```

(Référence OKAMAC : prix moyen MacBook reconditionné.)

### Spécifications
Fichier `module1/csv_reader.py`, fonction :

```python
def column_mean(csv_path: str, column: str) -> float:
    """Return arithmetic mean of a numeric column in a CSV file.

    Raises:
        FileNotFoundError: if csv_path doesn't exist.
        KeyError: if column doesn't exist.
        ValueError: if column contains non-numeric values.
    """
```

- Utilise **uniquement** le module `csv` de la stdlib (pas pandas).
- Gère les 3 erreurs ci-dessus.

### Tests à faire passer
Fichier `module1/tests/test_csv_reader.py` :

```python
import pytest
from module1.csv_reader import column_mean

CSV = "module1/data/sales.csv"


def test_mean_price():
    assert column_mean(CSV, "price") == pytest.approx(889.10, rel=1e-3)


def test_mean_quantity():
    assert column_mean(CSV, "quantity") == pytest.approx(1.8, rel=1e-3)


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        column_mean("nope.csv", "price")


def test_missing_column():
    with pytest.raises(KeyError):
        column_mean(CSV, "nonexistent")


def test_non_numeric_column():
    with pytest.raises(ValueError):
        column_mean(CSV, "product")
```

### Lancer
```bash
uv run pytest module1/tests/test_csv_reader.py -v
```

---

## Exercice 4 — Refactoring d'un script "sale"

### Énoncé
On te file un script qui marche mais qui est moche. Tu dois le rendre **propre, typé, testé, conforme PEP8**.

### À créer
Fichier `module1/legacy_script.py` (script de départ — copie-le tel quel) :

```python
import sys

def f(l):
    s = 0
    n = 0
    for x in l:
        if x != None:
            s = s + x
            n = n + 1
    if n == 0:
        return 0
    return s / n

def g(l, t):
    r = []
    for x in l:
        if x > t:
            r.append(x)
    return r

def main():
    data = [10, 20, None, 30, None, 40, 50]
    print("moyenne:", f(data))
    print("sup a 25:", g([x for x in data if x != None], 25))

if __name__ == "__main__":
    main()
```

### Ta mission
Crée `module1/clean_script.py` qui :

1. Renomme les fonctions de manière explicite (`mean_ignore_none`, `filter_above`).
2. Ajoute des **type hints** complets.
3. Ajoute des **docstrings** (style Google).
4. Remplace `!= None` par `is not None` (PEP8).
5. Utilise les `Optional` corrects (`list[float | None]`).
6. Passe `uv run ruff check module1/clean_script.py` sans erreur.

Puis crée `module1/tests/test_clean_script.py` avec au moins 4 tests qui passent.

### Vérification finale
```bash
uv run ruff check module1/clean_script.py
uv run pytest module1/tests/test_clean_script.py -v
```

---

## Validation du module

### Tout faire passer d'un coup
```bash
cd ~/Documents/formation-data-science/data-science-journey
uv run ruff check module1/
uv run pytest module1/ -v
```

Tu dois voir :
- Aucune erreur ruff.
- **Tous les tests verts** (au moins 20 tests au total).

### Commit
```bash
git add module1/
git commit -m "feat(module1): word_count, BankAccount, csv_reader, clean_script + tests"
git push
```

---

## Livrables à me rendre

1. **Lien direct vers le dossier `module1/`** sur ton repo GitHub.
2. **Sortie de** `uv run pytest module1/ -v` (copier-coller).
3. **Sortie de** `uv run ruff check module1/`.
4. Une question (au moins) sur un concept que tu as trouvé difficile.

---

## Erreurs fréquentes — Antisèche

| Symptôme | Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'module1'` | Tu lances pytest depuis le mauvais dossier | Lance depuis la racine du projet |
| `ImportError: attempted relative import` | Mauvais path dans `from ... import` | Utilise des imports absolus : `from module1.xxx import yyy` |
| `ruff` signale `E711` | Tu as écrit `x == None` | Utilise `x is None` |
| Tests `pytest.approx` échouent | Comparaison float stricte | Toujours `pytest.approx` pour les floats |
| `KeyError` au lieu de `ValueError` | Mauvais type d'exception levée | Relis l'énoncé, lève le bon type |

---

## Checklist de fin de module

- [ ] `module1/word_count.py` + 5 tests passent
- [ ] `module1/bank_account.py` + 6 tests passent
- [ ] `module1/csv_reader.py` + 5 tests passent
- [ ] `module1/clean_script.py` + 4 tests passent
- [ ] `uv run ruff check module1/` ne renvoie aucune erreur
- [ ] `uv run pytest module1/ -v` : 100% vert
- [ ] Code committé et pushé sur GitHub

---

**Prêt ? Commence par l'Exercice 1 (`word_count`). Crée le fichier, écris ta première implémentation, lance les tests. Dès que tu bloques, copie-colle l'erreur ici et on débogue.**
