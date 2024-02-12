from .database import base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, DateTime, text
from sqlalchemy.orm import relationship


class Post(base):
    __tablename__ = "posts"

    id = Column(type_=Integer, primary_key=True)
    owner_id = Column(ForeignKey("users.id", ondelete="CASCADE"), type_=Integer, nullable=False)
    title = Column(type_=String, nullable=False)
    content = Column(type_=String, nullable=False)
    timestamp = Column(type_=TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    owner = relationship("User")


class User(base):
    __tablename__ = "users"

    id = Column(type_=Integer, primary_key=True)
    username = Column(type_=String, nullable=False, unique=True)
    password = Column(type_=String, nullable=False)
    timestamp = Column(type_=TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Like(base):
    __tablename__ = "likes"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), type_=Integer, primary_key=True)
    post_id = Column(ForeignKey("posts.id", ondelete="CASCADE"), type_=Integer, primary_key=True)
