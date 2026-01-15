from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from core.auth import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


# pydantic model for token generation
class TokenRequest(BaseModel):
    username: str
    password: str


# generate token 
@router.post("/token")
def get_token(data: TokenRequest):
    # user creds
    if data.username != "admin" or data.password != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(subject=data.username)
    return {"access_token": token, "token_type": "bearer"}
