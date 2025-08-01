from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..Shared.MiddleWares.loginMiddlewWare import validateToken

security = HTTPBearer()

def _jwtAuth(credentials: HTTPAuthorizationCredentials = Depends(security), expectedRoles: list = None):
    token = credentials.credentials
    is_valid, result = validateToken(token, expectedRoles)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result["error"],
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result

def jwtAuth(expectedRoles: list = None):
    def wrapper(credentials: HTTPAuthorizationCredentials = Depends(security)):
        return _jwtAuth(credentials, expectedRoles=expectedRoles)
    return Depends(wrapper)
