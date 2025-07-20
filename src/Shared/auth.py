from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..Shared.MiddleWares.loginMiddlewWare import validateToken

security = HTTPBearer()

def jwtAuth(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    is_valid, result = validateToken(token)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result["error"],
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result