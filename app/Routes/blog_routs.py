from fastapi import Depends,APIRouter,status,HTTPException
from app.models.blog_model import UserAuth
from sqlalchemy.orm import Session
from app.utils.blog_utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from app.database.database import engine , SessionLocal
from app.schemas.blog_schema import CreateUser,DisplyUser

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

app = APIRouter()

@app.post('/signup',summary='create new user',response_model=DisplyUser)
def create_user(request:CreateUser,db:Session = Depends(get_db)):

    new_user = UserAuth(email = request.email, password = get_hashed_password(request.password))
    if new_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password',
        )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post('/login',summary='create access and refresh token for user')
def user_login(request:CreateUser,db:Session = Depends(get_db)):

    if not db.query(UserAuth.id).filter(UserAuth.email == request.email).count():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password',
        )

    else:
        User = (db.query(UserAuth.id,UserAuth.password).filter(UserAuth.email == request.email).first())
        # print(User)
        user_id = User.id
        user_password = User.password

        if verify_password(request.password,user_password):

            access_token = create_access_token(user_id)
            refresh_token = create_refresh_token(user_id)
            
            return {
                'access_token' : access_token,
                'refresh_token' : refresh_token,
            }

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect email or password',
            )
            






































# @app.delete("/login/{id}")
# def userdata(id,db:Session = Depends(get_db)):
#     db.query(UserAuth).filter(UserAuth.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "done" 

# @app.get("/")
# def hello():
#     return "hello"

# @app.post("/blog")
# def adddata(request:Blog , db:Session = Depends(get_db)):
#     new_user = UserBlog(id = request.id,name=request.name,description = request.description)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/blog")
# def alluserdata(db:Session = Depends(get_db)):
#     user = db.query(UserBlog).all()
#     return user     

# @app.get("/blog/{id}")
# def userdata(id,db:Session = Depends(get_db)):
#     user = db.query(UserBlog).filter(UserBlog.id == id).first()
#     return user     

# @app.delete("/blog/{id}")
# def userdata(id,db:Session = Depends(get_db)):
#     db.query(UserBlog).filter(UserBlog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "done"     
                

# @app.put("/blog/{id}")
# def userdata(id,request:Blog ,db:Session = Depends(get_db)):
#     db.query(UserBlog).filter(UserBlog.id == id).update(request.dict())
#     db.commit()
#     return "done"
                   
# # @app.post("/blog")
# # def product(request:schemas.Blog,db:Session = Depends(get_db)):
# #     new_product = models.Blog(id = request.id,title=request.title,body = request.body)
# #     db.add(new_product)
# #     db.commit()
# #     db.refresh(new_product)
# #     return new_product

