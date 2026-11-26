"""Punto de entrada de la API de AgroPort Ica.

Ejecución local (desde la raíz del repositorio):
    uvicorn backend.app.main:app --reload
"""

from fastapi import FastAPI

from backend.app.core.config import Settings, get_settings
from backend.app.routers import health, root

DESCRIPTION = (
    "API del sistema **AgroPort Ica** para la planificación agroexportadora de la "
    "región Ica. Integra información agrícola y portuaria (MongoDB Atlas) con la "
    "información generada por el sistema (PostgreSQL en Supabase)."
)


def create_app(settings: Settings | None = None) -> FastAPI:
    """Construye y configura la aplicación FastAPI."""
    settings = settings or get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=DESCRIPTION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.state.settings = settings

    app.include_router(root.router)
    app.include_router(health.router, prefix=settings.api_prefix)

    return app


app = create_app()
