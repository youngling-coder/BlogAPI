from datetime import datetime
from typing import Optional
from pydantic import BaseModel, conint # EmailStr


class BaseUser(BaseModel):
    username: str
    password: str


class CreateUser(BaseUser):
    pass


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class BasePost(BaseModel):
    title: str
    content: str


class CreatePost(BasePost):
    pass


class Post(BasePost):
    id: int
    timestamp: datetime
    owner: UserResponse

    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    Post: Post
    likes: int



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]


class CreateLike(BaseModel):
    post_id: int
    dir: conint(le=1)
