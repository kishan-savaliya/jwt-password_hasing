from pydantic import BaseModel

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

class TokenSchema(BaseModel):
    email : str
    password : str
