from fastapi import APIRouter,Depends

from models.user_model import Token, UserLogin,User
from services.user_service import login_user_service
from utils.session import get_session
# presentation Layer

router = APIRouter(prefix="/api")


@router.post('/login',response_model=Token)
def login(login_data:UserLogin,session = Depends(get_session)):
    # print(login_data)
    # data = User(**login_data.model_dump())
    return login_user_service(login_data=login_data,session=session)
    # return "login_user_service(login_data=login_data,session=session)"