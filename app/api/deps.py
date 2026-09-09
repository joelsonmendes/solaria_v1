from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import decode_token
from app.db.session import get_db
from app.models.user import User,UserRole
bearer_scheme=HTTPBearer(auto_error=False)
async def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(bearer_scheme),db:AsyncSession=Depends(get_db)):
    if not credentials: raise HTTPException(status_code=401,detail="Autenticação necessária")
    try: payload=decode_token(credentials.credentials)
    except ValueError: raise HTTPException(status_code=401,detail="Token inválido ou expirado")
    if payload.get("type")!="access": raise HTTPException(status_code=401,detail="Tipo de token inválido")
    result=await db.execute(select(User).where(User.id==payload.get("sub")))
    user=result.scalar_one_or_none()
    if not user or not user.is_active: raise HTTPException(status_code=401,detail="Usuário inexistente ou inativo")
    return user
def require_roles(*roles):
    async def dependency(user:User=Depends(get_current_user)):
        if user.role not in roles: raise HTTPException(status_code=403,detail="Permissão insuficiente")
        return user
    return dependency
