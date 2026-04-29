from datetime import datetime, timedelta,UTC
from typing import Optional
from jose import jwt,JWTError

def create_token(data:dict,expires_delta:Optional[timedelta] = None):
    """create a signed jwt token"""
    to_encode = data.copy()
    
    exp =  datetime.now(UTC) + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp":exp})

    return jwt.encode(to_encode,"aadsdsdsdsdsdsdsfdfeffwdwrew",algorithm="HS256")


def decode_token(token:str):
    """Decode adn validate the JWT token"""
    try:
        return jwt.decode(token=token,key="aadsdsdsdsdsdsdsfdfeffwdwrew",algorithms=["HS256"])
    except JWTError:
        return None    

# # token = create_token(data={"name":"Muhammad Talha","email":"muhammadtalha0110@gmail.com","role":"admin"})

# # print(token)
# token = decode_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3Nzc0NTQ5ODh9.Tt2G5bL4bmQZFv2s2LuK2gEX60vaOizx95Jd1cu0lXo")
# print(token)