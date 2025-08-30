from .base import *
import dj_database_url
from config.env import env

DEBUG=env.bool('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

DATABASES = {
    "default": dj_database_url.config(
        default=env("DATABASE_URL"),
        conn_max_age=600,  # garde les connexions ouvertes pour les performances
    )
}