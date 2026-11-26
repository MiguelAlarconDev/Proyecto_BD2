"""Endpoint raíz de la API (fuera del prefijo versionado)."""

from fastapi import APIRouter

from backend.app.schemas.health import RootResponse

router = APIRouter(tags=["root"])


@router.get("/", response_model=RootResponse, summary="Información básica de la API")
def read_root() -> RootResponse:
    return RootResponse(proyecto="AgroPort Ica", mensaje="API funcionando correctamente")
