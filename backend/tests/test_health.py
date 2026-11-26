"""Pruebas de los endpoints base y de la documentación de la API."""

import pytest
from fastapi.testclient import TestClient

from backend.app.core.config import Settings
from backend.app.main import app, create_app

DB_ENV_VARS = (
    "MONGODB_AGRICOLA_URI",
    "MONGODB_AGRICOLA_DATABASE",
    "MONGODB_AGRICOLA_COLLECTION",
    "MONGODB_PORTUARIO_URI",
    "MONGODB_PORTUARIO_DATABASE",
    "MONGODB_PORTUARIO_COLLECTION",
    "POSTGRESQL_URI",
)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_root_responde_200(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_root_devuelve_informacion_esperada(client: TestClient) -> None:
    response = client.get("/")
    assert response.json() == {
        "proyecto": "AgroPort Ica",
        "mensaje": "API funcionando correctamente",
    }


def test_health_responde_200(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200


def test_health_devuelve_estructura_esperada(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.json() == {"status": "ok", "service": "agroport-backend"}


def test_openapi_disponible(client: TestClient) -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "AgroPort Ica API"
    assert schema["info"]["version"] == "0.1.0"
    assert "/api/v1/health" in schema["paths"]


@pytest.mark.parametrize("ruta", ["/docs", "/redoc"])
def test_documentacion_interactiva_disponible(client: TestClient, ruta: str) -> None:
    response = client.get(ruta)
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_app_funciona_sin_bases_de_datos_configuradas(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Se eliminan las variables de entorno y se ignora cualquier archivo .env
    for var in DB_ENV_VARS:
        monkeypatch.delenv(var, raising=False)
    settings = Settings(_env_file=None)

    assert settings.mongodb_agricola_uri == ""
    assert settings.mongodb_portuario_uri == ""
    assert settings.postgresql_uri == ""

    with TestClient(create_app(settings)) as isolated_client:
        assert isolated_client.get("/").status_code == 200
        health = isolated_client.get("/api/v1/health")
        assert health.status_code == 200
        assert health.json()["status"] == "ok"
