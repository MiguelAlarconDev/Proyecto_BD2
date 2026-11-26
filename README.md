# AgroPort Ica

Sistema de información para la planificación agroexportadora de la región Ica.
Proyecto del curso **Base de Datos II**.

## Descripción

AgroPort Ica integra información agrícola y portuaria almacenada en bases de datos
SQL y NoSQL para apoyar la planificación logística de la agroexportación: consulta
de lugares de producción, infraestructura portuaria, evaluación de certificaciones,
estimación de producción y generación de recomendaciones logísticas preliminares.

## Problemática

Deficiente integración de la información agrícola y portuaria para la planificación
logística de la agroexportación en la región Ica. Los datos de producción y los de
infraestructura portuaria se encuentran dispersos y en formatos distintos, lo que
dificulta su análisis conjunto.

## Solución propuesta

Un backend que integra tres bases de datos independientes en la nube y expone una
API REST para consultar la información, evaluar certificaciones, estimar la
producción y generar recomendaciones logísticas preliminares.

## Arquitectura general

| Componente | Tecnología | Responsabilidad |
|---|---|---|
| Base de datos agrícola | MongoDB Atlas (1) | Dataset de lugares de producción agrícola de Ica |
| Base de datos portuaria | MongoDB Atlas (2) | Dataset de infraestructura portuaria del Perú (2022-2026) |
| Base de datos relacional | PostgreSQL (Supabase) | Información generada por el sistema |
| Backend | Python + FastAPI | Integración de las tres fuentes y lógica de negocio |
| Frontend | Pendiente | Pendiente de definición |

Detalle completo en [docs/architecture.md](docs/architecture.md).

## Tecnologías

- Python 3.14
- FastAPI 0.165
- Uvicorn (servidor ASGI)
- Pydantic / pydantic-settings (validación y configuración)
- pytest + FastAPI TestClient (pruebas)

## Estructura de carpetas

```text
Proyecto_BD2/
├── backend/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Fábrica create_app() e instancia `app`
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py        # Configuración desde variables de entorno
│   │   ├── database/            # Conexiones (pendiente)
│   │   ├── adapters/            # Traducción de esquemas externos (pendiente)
│   │   ├── repositories/        # Acceso a datos (pendiente)
│   │   ├── models/              # Modelos de dominio (pendiente)
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── health.py        # Esquemas de respuesta de / y /health
│   │   ├── services/            # Lógica de negocio (pendiente)
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── root.py          # GET /
│   │       └── health.py        # GET /api/v1/health
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_health.py
│   └── requirements.txt
├── docs/
│   └── architecture.md
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md
```

## Configuración del entorno virtual

Desde la raíz del repositorio, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación por la política de ejecución:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## Instalación de dependencias

```powershell
python -m pip install -r backend\requirements.txt
```

## Variables de entorno

Copiar la plantilla y completar los valores cuando el equipo proporcione las credenciales:

```powershell
Copy-Item .env.example .env
```

El archivo `.env` está excluido de Git. **Nunca** se deben versionar credenciales.
La aplicación inicia correctamente aunque las variables de conexión estén vacías
o aunque `.env` no exista.

## Gestión segura de credenciales

Este repositorio es **público**. Ningún integrante del equipo debe subir al
repositorio contraseñas, tokens, claves de API ni cadenas de conexión completas,
en ningún archivo (código, documentación, notas, capturas o mensajes de commit).

- Las credenciales se guardan solo en el archivo `.env` local de cada integrante.
- `.env.example` contiene únicamente los **nombres** de las variables, con valores vacíos.
- Las credenciales se comparten por un canal privado del equipo, nunca mediante Git.
- En la documentación, usar marcadores como `mongodb+srv://<usuario>:<contraseña>@<host>/`.
- Antes de cada commit, revisar `git status` y `git diff --cached`.
- Si una credencial llega a publicarse, se debe **rotar de inmediato** en el servicio
  correspondiente (MongoDB Atlas, Supabase). Eliminar el archivo no basta, porque el
  valor permanece en el historial de Git.

## Ejecución local

Desde la raíz del repositorio, con el entorno virtual activo:

```powershell
uvicorn backend.app.main:app --reload
```

- API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints disponibles

| Método | Ruta | Descripción | Respuesta |
|---|---|---|---|
| GET | `/` | Información básica de la API | `{"proyecto": "AgroPort Ica", "mensaje": "API funcionando correctamente"}` |
| GET | `/api/v1/health` | Estado de la aplicación | `{"status": "ok", "service": "agroport-backend"}` |
| GET | `/docs` | Documentación Swagger UI | HTML |
| GET | `/redoc` | Documentación ReDoc | HTML |
| GET | `/openapi.json` | Esquema OpenAPI | JSON |

> El health check solo confirma que la aplicación está en ejecución. **No** verifica
> la conectividad con las bases de datos.

## Ejecución de pruebas

Desde la raíz del repositorio:

```powershell
python -m pytest
```

La configuración (`pytest.ini`) define la ruta de las pruebas y el `pythonpath`.

## Estado actual del desarrollo

**Fase 1 — Inicialización y estructura base del backend: completada.**

- [x] Estructura modular del backend
- [x] Aplicación FastAPI con Swagger y ReDoc
- [x] Endpoints `/` y `/api/v1/health`
- [x] Configuración por variables de entorno (`.env.example`)
- [x] Pruebas automatizadas
- [ ] Conexión a MongoDB Atlas agrícola (pendiente de credenciales y esquema)
- [ ] Conexión a MongoDB Atlas portuario (desplegado; pendiente de credenciales y esquema)
- [ ] Conexión a PostgreSQL en Supabase (pendiente)
- [ ] Adaptadores, repositorios y modelos según esquemas reales
- [ ] Lógica de negocio agroexportadora
- [ ] Frontend
