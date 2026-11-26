"""Configuración de la aplicación leída desde variables de entorno y `.env`.

Las variables de conexión a bases de datos son opcionales: la aplicación
debe iniciar aunque estén vacías.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/app/core/config.py -> raíz del repositorio
PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Aplicación
    app_name: str = "AgroPort Ica API"
    app_env: str = "development"
    app_version: str = "0.1.0"
    api_prefix: str = "/api/v1"

    # MongoDB Atlas 1: lugares de producción agrícola de Ica
    mongodb_agricola_uri: str = ""
    mongodb_agricola_database: str = ""
    mongodb_agricola_collection: str = ""

    # MongoDB Atlas 2: infraestructura portuaria del Perú (2022-2026)
    mongodb_portuario_uri: str = ""
    mongodb_portuario_database: str = ""
    mongodb_portuario_collection: str = ""

    # PostgreSQL (Supabase): información generada por el sistema
    postgresql_uri: str = ""


@lru_cache
def get_settings() -> Settings:
    """Devuelve una instancia única de configuración."""
    return Settings()
