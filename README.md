# FastIA — Template modulaire (Streamlit + FastAPI) avec Docker, tests et CI

Ce dépôt fournit un socle minimaliste, reproductible et extensible :
- **Frontend** : Streamlit + Loguru
- **Backend** : FastAPI + Pydantic + Loguru
- **Conteneurisation** : Docker + Docker Compose
- **Tests** : pytest (tests unitaires sur la logique métier)
- **CI** : GitHub Actions (exécute les tests à chaque push/PR)

---

## 1) Architecture

```text
.
├── docker-compose.yml
├── README.md
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── backend/
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── modules/
│   │   └── calcul.py
│   └── tests/
│       └── test_calcul.py
└── .github/
    └── workflows/
        └── test.yml
```

### Rôle des composants
- **frontend/app.py** : interface Streamlit (saisie d’un entier, affichage du résultat).
- **backend/main.py** : API FastAPI avec 3 routes (`/`, `/health`, `/calcul`).
- **backend/modules/calcul.py** : logique métier (fonction `calcul(x)`).
- **backend/tests/test_calcul.py** : test unitaire pytest.
- **docker-compose.yml** : lance uniquement le frontend et le backend.
- **.github/workflows/test.yml** : CI GitHub Actions.

---

## 2) API — Routes

Base URL : `http://localhost:8000`

| Méthode | Route | Description |
|--------|-------|-------------|
| GET | `/` | Message de bienvenue |
| GET | `/health` | Vérification de l’état |
| POST | `/calcul` | Retourne le carré d’un entier |

---

## 3) Lancement via Docker (recommandé)

### Prérequis
- Docker Desktop démarré
- Docker Compose

### Démarrage
```bash
docker compose up --build
```

### Accès
- Frontend : http://localhost:8501
- Backend : http://localhost:8000
- Docs API : http://localhost:8000/docs

### Arrêt
```bash
docker compose down
```

---

## 4) Lancement hors Docker (optionnel)

### Environnement virtuel
```bash
python -m venv .venv
```

Activation :
- Linux/Mac : `source .venv/bin/activate`
- Windows : `.venv\Scripts\Activate.ps1`

### Installation
```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### Backend
```bash
cd backend
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
streamlit run app.py
```

---

## 5) Tests

### Lancer pytest

Linux/Mac :
```bash
PYTHONPATH=. pytest
```

Windows PowerShell :
```powershell
$env:PYTHONPATH="."
pytest
```

---

## 6) Intégration Continue (CI)

Le workflow `.github/workflows/test.yml` lance automatiquement les tests à chaque push ou pull request.

---

## 7) Conformité au brief
- Séparation frontend / backend
- API avec 3 routes
- Validation Pydantic
- Logique métier testée
- Docker Compose fonctionnel
- Tests automatisés et CI opérationnelle
