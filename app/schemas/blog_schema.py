from pydantic import BaseModel
from typing import Union

# class Blog(BaseModel):
#     id : int
#     name : str
#     description : str

# class Show_blog(BaseModel):
#     title : str
#     body : str
#     class Config():
#         orm_mode = True

class CreateUser(BaseModel):
    id : int
    email : str
    password : str

class DisplyUser(BaseModel):
    email : str
    password : str

    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInDB(User):
    hashed_password: str

class TokenData(BaseModel):
    username: Union[str, None] = None

# class TokenPayload(BaseModel):
#     access_token : str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzExNjYyMzAsInN1YiI6IjQifQ.whUWFd_qfsCzv7z3KwCGdMb4qfjlxHWbaWf78lq9XiU"
