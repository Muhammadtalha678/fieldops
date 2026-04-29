from datetime import datetime, timedelta,UTC
from typing import Optional
from jose import jwt,JWTError
from configs.config import secret_key
def create_token(data:dict,expires_delta:Optional[timedelta] = None):
    """create a signed jwt token"""
    to_encode = data.copy()
    
    exp =  datetime.now(UTC) + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp":exp})

    return jwt.encode(to_encode,secret_key,algorithm="HS256")


def decode_token(token:str):
    """Decode adn validate the JWT token"""
    try:
        return jwt.decode(token=token,key=secret_key,algorithms=["HS256"])
    except JWTError:
        return None    

# # token = create_token(data={})

# # print(token)
# token = decode_token("")
# print(token)