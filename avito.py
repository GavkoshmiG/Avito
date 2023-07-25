from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

app = FastAPI(title = "Avito")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"













# async def common_parameters(
#         q: Union[str , None] = None, skip: int = 0, limit: int = 100
#         ):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons





# app = FastAPI(title = "Avito")

# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )

# avito_users = [
#     {"id": 1, "role": "admin", "name": ["Bob"]},
#     {"id": 2, "role": "investor", "name": "John"},
#     {"id": 3, "role": "trader", "name": "Matt"},
#     {"id": 4, "role": "investor", "name": "Homer", "degree": [
#         {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
#     ]},
# ]


# class DegreeType(Enum):
#     newbie = "newbie"
#     expert = "expert"


# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType


# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[List[Degree]] = []

# @app.get("/users/{user_id}", response_model=List[User]) 
# def get_user(user_id: int):
#     return [user for user in avito_users if user.get("id") == user_id]


# avito_trades = [
#     {"id": 1, "user_id": 1, "currency": "USD", "condition": "buy", "price": 123, "amount": 45780},
#     {"id": 2, "user_id": 1, "currency": "RUB", "condition": "sell", "price": 125, "amount": 20013},
# ]

# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currency: str = Field(max_length=5)
#     condition: str
#     price: float = Field(ge=0)
#     amount: float

# @app.post("/trades")
# def add_trades(trades: List[Trade]):
#     avito_trades.extend(trades)
#     return {"status": 200, "data": avito_trades}


# @app.get("/trades")
# def get_trades(limit: int = 1, offset: int = 0):
#     return fake_trades[offset:][:limit]

# avito_users2 = [
#     {"id": 1, "role": "buyer", "name": "Vasiliy Pupkin"},
#     {"id": 2, "role": "seller", "name": "Torgash Kakashich"},
# ]

# @app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, avito_users2))[0]
#     current_user["name"] = new_name
#     return {"status": 200, "data": current_user}