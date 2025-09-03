import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

# Choisir le bon fichier .env
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")  # par défaut "development"
print(f"Chargement du fichier .env pour l'environnement: {ENVIRONMENT}")
if ENVIRONMENT == "production":
    env_file = BASE_DIR / ".env.production"
else:
    env_file = BASE_DIR / ".env.local"

environ.Env.read_env(env_file)
