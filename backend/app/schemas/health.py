"""Esquemas de respuesta para los endpoints de estado."""

from pydantic import BaseModel


class RootResponse(BaseModel):
    proyecto: str
    mensaje: str


class HealthResponse(BaseModel):
    status: str
    service: str
