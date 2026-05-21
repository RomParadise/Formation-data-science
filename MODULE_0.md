# Module 0 — Mise en place de l'environnement

> Objectif : avoir un environnement Python professionnel, reproductible, versionné sur GitHub, prêt pour tous les modules suivants.
> Durée estimée : 2 à 4 heures.
> OS visé : macOS (toutes versions récentes).

---

## Vue d'ensemble — Ce qu'on va installer

| Outil | Rôle |
|-------|------|
| **Homebrew** | Gestionnaire de paquets macOS |
| **Git** | Versionner ton code |
| **pyenv** | Gérer plusieurs versions de Python |
| **Python 3.11.9** | Langage principal |
| **uv** | Gestionnaire de dépendances ultra-rapide (alternative moderne à pip/poetry) |
| **VS Code** | Éditeur (déjà installé chez toi) |
| **GitHub CLI (gh)** | Interagir avec GitHub en ligne de commande |

---

## Étape 1 — Installer Homebrew

### Pourquoi ?
Homebrew permet d'installer proprement tous les outils en ligne de commande sur Mac. C'est le standard.

### Comment ?
Ouvre l'application **Terminal** (ou directement dans VS Code via `Ctrl + ù`) et colle :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

À la fin de l'installation, le terminal te donnera **2 commandes** à exécuter pour ajouter Homebrew au PATH. Elles ressemblent à :

```bash
echo >> /Users/rperidy/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/rperidy/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Exécute-les exactement comme indiqué dans ton terminal.**

### Vérification
```bash
brew --version
```
Tu dois voir `Homebrew 4.x.x`.

---

## Étape 2 — Installer Git et configurer ton identité

### Pourquoi ?
Git versionne ton code. Chaque commit doit être signé avec ton nom + email (celui de ton compte GitHub).

### Comment ?
```bash
brew install git
```

Puis configure ton identité (remplace par tes vraies infos) :
```bash
git config --global user.name "RomParadise"
git config --global user.email "peridy.rom@gmail.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
```

### Vérification
```bash
git --version
git config --global --list
```

---

## Étape 3 — Installer pyenv et Python 3.11.9

### Pourquoi ?
- Le Python livré avec macOS est ancien et ne doit **jamais** être modifié.
- `pyenv` permet d'avoir plusieurs versions de Python en parallèle.
- Python 3.11 est la version "sweet spot" actuelle (stable, rapide, compatible avec tout l'écosystème data).

### Comment ?
```bash
brew install pyenv
```

Ajoute pyenv à ton shell (zsh) :
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```

Recharge ton shell :
```bash
source ~/.zshrc
```

Installe Python 3.11.9 (ça prend 2-3 minutes) :
```bash
pyenv install 3.11.9
pyenv global 3.11.9
```

### Vérification
```bash
python --version
which python
```
Tu dois voir `Python 3.11.9` et un chemin qui contient `.pyenv/shims/python`.

---

## Étape 4 — Installer uv (gestionnaire de paquets)

### Pourquoi ?
`uv` est l'outil moderne (créé par Astral, 2024) qui remplace `pip`, `virtualenv` et `poetry`. **10 à 100x plus rapide.** C'est ce qu'on utilise en 2026.

### Comment ?
```bash
brew install uv
```

### Vérification
```bash
uv --version
```

---

## Étape 5 — Installer GitHub CLI et se connecter

### Pourquoi ?
`gh` permet de créer/cloner des repos GitHub sans passer par le navigateur, et gère l'authentification proprement (pas de mot de passe à retaper).

### Comment ?
```bash
brew install gh
gh auth login
```

Réponds aux questions interactives :
- `What account do you want to log into?` → **GitHub.com**
- `What is your preferred protocol for Git operations?` → **HTTPS**
- `Authenticate Git with your GitHub credentials?` → **Yes**
- `How would you like to authenticate GitHub CLI?` → **Login with a web browser**

Copie le code affiché, appuie sur Entrée, ton navigateur s'ouvre, colle le code, valide.

### Vérification
```bash
gh auth status
```

---

## Étape 6 — Installer les extensions VS Code essentielles

Dans VS Code, ouvre l'onglet Extensions (`Cmd + Shift + X`) et installe :

1. **Python** (Microsoft) — id : `ms-python.python`
2. **Pylance** (Microsoft) — id : `ms-python.vscode-pylance`
3. **Jupyter** (Microsoft) — id : `ms-toolsai.jupyter`
4. **Ruff** (Astral) — id : `charliermarsh.ruff` — linter/formatter ultra-rapide
5. **GitLens** — id : `eamodio.gitlens`

Ou en une commande :
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension charliermarsh.ruff
code --install-extension eamodio.gitlens
```

---

## Étape 7 — Créer le projet `data-science-journey`

### 7.1 Créer le dossier et l'initialiser
```bash
mkdir -p ~/Documents/formation-data-science/data-science-journey
cd ~/Documents/formation-data-science/data-science-journey
```

### 7.2 Initialiser le projet Python avec uv
```bash
uv init --python 3.11.9
```

Ça crée :
- `pyproject.toml` — déclaration du projet et des dépendances
- `.python-version` — fige la version Python
- `main.py` — fichier exemple
- `README.md` — vide
- `.gitignore`

### 7.3 Ajouter les dépendances data science
```bash
uv add pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel
uv add --dev ruff pytest
```

uv crée automatiquement un environnement virtuel dans `.venv/` et un fichier `uv.lock` (à committer).

### 7.4 Écrire un README propre

Remplace le contenu de `README.md` par :

```markdown
# Data Science Journey

Mon parcours d'apprentissage pour devenir Data Scientist autonome.

## Stack
- Python 3.11.9 (gérée par pyenv)
- uv (gestion des dépendances)
- pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter

## Installation
\`\`\`bash
git clone https://github.com/<ton-user>/data-science-journey.git
cd data-science-journey
uv sync
\`\`\`

## Lancer un notebook
\`\`\`bash
uv run jupyter lab
\`\`\`

## Structure
- `module0/` — Mise en place
- `module1/` — Python pour la Data Science
- ...
```

(Remplace `<ton-user>` par ton vrai pseudo GitHub.)

### 7.5 Créer le notebook de vérification

```bash
mkdir module0
```

Crée le fichier `module0/check_env.ipynb` depuis VS Code (`Cmd + N` → enregistrer en `.ipynb`), et ajoute **3 cellules** :

**Cellule 1 (Markdown)**
```markdown
# Module 0 — Vérification de l'environnement
```

**Cellule 2 (Code)**
```python
import sys
import pandas as pd
import numpy as np
import matplotlib
import sklearn

print(f"Python  : {sys.version.split()[0]}")
print(f"pandas  : {pd.__version__}")
print(f"numpy   : {np.__version__}")
print(f"matplotlib: {matplotlib.__version__}")
print(f"sklearn : {sklearn.__version__}")
```

**Cellule 3 (Code)**
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), label="cos")
plt.legend()
plt.title("Hello Data Science")
plt.show()
```

**Important** : avant d'exécuter, en haut à droite du notebook, clique sur "Select Kernel" et choisis l'interpréteur situé dans `.venv/bin/python` de ton projet.

Exécute les 3 cellules. Tu dois voir les versions affichées et une courbe sinus/cosinus.

---

## Étape 8 — Premier commit et push sur GitHub

### 8.1 Initialiser git (si pas déjà fait par uv)
```bash
git init
```

### 8.2 Vérifier le `.gitignore`
Ouvre `.gitignore` et assure-toi qu'il contient au minimum :
```
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.DS_Store
```

Si certaines lignes manquent, ajoute-les.

### 8.3 Premier commit
```bash
git add .
git commit -m "chore: initial setup with uv, python 3.11 and data science deps"
```

### 8.4 Créer le repo distant et pousser
```bash
gh repo create data-science-journey --public --source=. --remote=origin --push
```

### Vérification
```bash
gh repo view --web
```
Ton navigateur s'ouvre sur ton repo GitHub. Tu dois voir ton README et tes fichiers.

---

## Livrables à me rendre

Une fois tout terminé, envoie-moi :

1. **Le lien GitHub** de ton repo `data-science-journey`.
2. **Une capture d'écran** du notebook `module0/check_env.ipynb` exécuté (versions + graphique).
3. **La sortie** de ces 4 commandes (copie-colle simple) :
   ```bash
   python --version
   uv --version
   git --version
   gh --version
   ```

---

## Erreurs fréquentes — Antisèche

| Symptôme | Cause probable | Solution |
|----------|----------------|----------|
| `command not found: brew` | PATH non chargé | Refais l'étape "ajouter au PATH" |
| `command not found: pyenv` | `.zshrc` pas rechargé | `source ~/.zshrc` ou ouvre un nouveau terminal |
| `pyenv install` échoue | Outils de compilation manquants | `xcode-select --install` |
| Kernel introuvable dans Jupyter | Mauvais interpréteur | Cmd+Shift+P → "Python: Select Interpreter" → `.venv/bin/python` |
| `gh: command not found` | Pas installé | `brew install gh` |
| Permission denied lors du push | Auth non faite | `gh auth login` |

---

## Critères de validation (auto-check)

Coche mentalement chaque point. **Tu dois pouvoir cocher les 8** avant de passer au Module 1 :

- [x] `brew --version` répond
- [x] `python --version` affiche **3.11.9**
- [x] `uv --version` répond
- [x] `gh auth status` me montre que je suis connecté
- [x] Mon repo GitHub `data-science-journey` est public et en ligne
- [x] Le notebook `module0/check_env.ipynb` s'exécute sans erreur
- [x] Le graphique sinus/cosinus s'affiche
- [x] Mon `.gitignore` exclut bien `.venv/` et `.DS_Store`

---

**Prêt ? Lance-toi sur l'Étape 1. Dès que tu bloques quelque part, copie-colle l'erreur exacte ici et on débogue ensemble. À la fin, partage-moi tes livrables et on attaque le Module 1.**
