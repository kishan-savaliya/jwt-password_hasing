# from fastapi import Depends, HTTPException, status
# from datetime import datetime
# from app.schemas.blog_schema import CreateUser,TokenPayload
# from app.utils.blog_utils import (
#     algorthm,jwt_secret_key
# )
# from typing import Union,Any
# from pydantic import ValidationError
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt
# from replit import db

# reuseble_Oauth = OAuth2PasswordBearer(
#     tokenUrl = '/login',
#     scheme_name = 'JWT'
# )

# def get_current_user(token:str = Depends(reuseble_Oauth)) -> CreateUser:
#     try:
#         payload = jwt.decode(
#             token,jwt_secret_key,algorithms=[algorthm]
#         )
#         token_data = TokenPayload(payload)
#     #     print(token_data)
#         if datetime.fromtimestamp(token_data.exp) < datetime.now():
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Token expired",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#     except(jwt.JWTError,ValidationError):
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     user: Union[dict[str, Any], None] = db.get(token_data.sub, None)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Could not find user",
#         )

#     return CreateUser(user)
