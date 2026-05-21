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

### Concepts à maîtriser absolument

| Concept | Pourquoi c'est crucial |
|---|---|
| **Types & structures** (list, dict, set, tuple) | 80% de ton code en data = manipuler des collections |
| **Comprehensions** (`[x*2 for x in xs]`) | Code plus court, plus rapide qu'une boucle |
| **Fonctions pures + type hints** | Code testable, auto-documenté |
| **Classes** | Encapsuler logique métier (modèles, pipelines) |
| **Gestion d'erreurs** | Un job batch qui plante à 3h du matin sans message clair = catastrophe |
| **Modules & imports** | Organiser un projet > 100 lignes |
| **Tests unitaires** | Garantir que ton code marche après chaque modification |
| **Linting (ruff) + PEP8** | Code lisible par toute l'équipe |

### Lectures conseillées (optionnelles mais utiles)

- *Automate the Boring Stuff with Python* (gratuit en ligne).
- PEP 8 : https://peps.python.org/pep-0008/
- Documentation `typing` : https://docs.python.org/3/library/typing.html

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
