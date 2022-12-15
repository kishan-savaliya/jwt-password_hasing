import os
from typing import Union,Any
from datetime import datetime,timedelta
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

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
