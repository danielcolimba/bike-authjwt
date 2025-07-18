# Bike Auth Service

Microservicio de autenticación JWT para el sistema de bicicletas, desarrollado con Django REST Framework.

## 🚀 Tecnologías

- **Django 5.2.4** - Framework web
- **Django REST Framework** - API REST
- **JWT** - Autenticación por tokens
- **PostgreSQL** - Base de datos
- **Docker** - Contenedorización

## ⚡ Inicio Rápido

```bash
# Con Docker Compose (recomendado)
docker-compose up -d auth

# Localmente
python manage.py runserver 8001
```

**URL del servicio:** http://localhost:8001

## 📡 API Endpoints

- `POST /auth/register/` - Registro de usuarios
- `POST /auth/login/` - Inicio de sesión
- `POST /auth/refresh/` - Renovar token
- `GET /auth/profile/` - Perfil del usuario

**Autenticación:** Bearer Token en header `Authorization`
