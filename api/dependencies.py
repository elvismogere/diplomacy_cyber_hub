from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils.security import SecurityUtils
from datetime import datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Validate JWT token and return current user"""
    try:
        payload = SecurityUtils.verify_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_organization(organization_id: str):
    """Get organization details"""
    # Implement organization retrieval logic
    pass
