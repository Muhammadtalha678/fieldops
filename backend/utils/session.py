from fastapi import Request
from sqlmodel import Session
def get_session(request:Request):
    print(request.app.state.engine)
    with Session(request.app.state.engine) as session:
        yield session
    # try:
    # except:
    #     # print(e)
    #     session.rollback()
    #     raise