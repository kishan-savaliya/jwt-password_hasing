import os
from fastapi import Depends, HTTPException, status
from typing import Union,Any
from datetime import datetime,timedelta
from passlib.context import CryptContext
from jose import jwt,JWTError
from app.schemas.blog_schema import TokenData,UserInDB,User
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

reuseble_OAuth = OAuth2PasswordBearer(
    tokenUrl = '/token',
)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

access_token_expire_mintue = 30
refresh_token_expire_minute = 60 * 24 * 7 # 7 days
algorthm = "HS256"
jwt_secret_key = os.getenv('JWT_SECRET_KEY')   # should be kept secret
jwt_refresh_key = os.getenv('JWT_REFRESH_SECRET_KEY')

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(subject: Union[str,Any],expires_delta: int = None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=access_token_expire_mintue)

    to_encode = {'exp': expires_delta,'sub':str(subject)}
    encode_jwt = jwt.encode(to_encode,jwt_secret_key,algorthm)

    return encode_jwt

def create_refresh_token(subject: Union[str,Any],expires_delta: int = None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=refresh_token_expire_minute)

    to_encode = {'exp': expires_delta,'sub':str(subject)}
    encode_jwt = jwt.encode(to_encode,jwt_refresh_key,algorthm)

    return encode_jwt

def get_current_user(token:str = Depends(reuseble_OAuth)):
    try:
        payload = jwt.decode(token,jwt_secret_key,algorithms = [algorthm])
        # print(payload)
        username: str = payload.get('sub')
        # print(username)
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = TokenData(username=username)
        # print(token_data)
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    user = get_user(fake_users_db,username=token_data.username)
    # print(user)
    if user is None:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
