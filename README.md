# SolarIA V2 — Backend Foundation

Fundação full-stack do SolarIA com FastAPI + PostgreSQL + autenticação JWT + estrutura multiempresa.

## Incluído
- PostgreSQL 16 via Docker Compose
- API FastAPI
- SQLAlchemy 2 assíncrono
- JWT access + refresh token
- Hash seguro de senha
- Perfis: super_admin, org_admin, expert, technician, client
- Isolamento multiempresa por organization_id
- Cadastro de organização
- Login
- Endpoint /me
- Gestão de membros da empresa
- Health check

## Executar
1. Copie `.env.example` para `.env`.
2. Rode `docker compose up --build`.
3. Abra `http://localhost:8000/docs`.

## Fluxo inicial
POST `/api/v1/auth/register-organization`

```json
{
  "organization_name": "Solar Acre Engenharia",
  "document": "12.345.678/0001-00",
  "admin_name": "Administrador",
  "admin_email": "admin@empresa.com",
  "password": "SenhaForte123!"
}
```

POST `/api/v1/auth/login`

GET `/api/v1/auth/me` com `Authorization: Bearer <token>`

## Regra multiempresa
Toda entidade de negócio deverá carregar `organization_id`, e o backend sempre deriva o tenant do usuário autenticado. O front-end não deve escolher livremente o tenant.
