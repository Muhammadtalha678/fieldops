from sqlmodel import Session,select
from lib.hash_lib import verify_password
from models.user_model import User, UserLogin, UserRead
from fastapi import HTTPException,status
from lib.token_lib import create_token
def login_user_service(login_data:UserLogin,session:Session):
        # check user emil exists
        user = session.exec(select(User).where(User.email == login_data.email)).first()
        session.commit()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid email address")
        
        # check user password is valid
        if not verify_password(login_data.password,user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")

        # create token
        token = create_token(UserRead(**user.model_dump()).model_dump())
        return {
             "access_token":token,
             "user":user
        }
    
    # check if the email exists first
