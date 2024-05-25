from pydantic import BaseModel, EmailStr


class Users(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserReturn(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserReturn]
