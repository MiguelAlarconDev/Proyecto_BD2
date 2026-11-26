"""Health check de la aplicación.

Solo indica que el proceso de la API está en ejecución. No verifica ni
afirma conectividad con MongoDB Atlas ni con Supabase.
"""

from fastapi import APIRouter

from backend.app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse, summary="Estado de la aplicación")
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="agroport-backend")
