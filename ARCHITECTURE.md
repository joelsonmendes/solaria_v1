# Arquitetura SolarIA V2 Foundation

Frontend → FastAPI → Auth/Tenant Context → SQLAlchemy Async → PostgreSQL

## Multi-tenant
Modelo inicial: banco compartilhado com `organization_id`. Toda entidade de negócio deverá possuir `organization_id`, e consultas normais sempre filtram pelo tenant do usuário autenticado.

## Perfis
- super_admin
- org_admin
- expert
- technician
- client

## Próxima fase
customers, plants, utility_accounts, invoices, invoice_items, documents, diagnostics, solar_scores, expansion_simulations, alerts e audit_logs.
