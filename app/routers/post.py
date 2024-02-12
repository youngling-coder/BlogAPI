from typing import List, Optional
from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit=limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Like.post_id).label("likes")).join(models.Like, models.Like.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit=limit).offset(skip).all()

    return posts

@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):

    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Like.post_id).label("likes")).join(models.Like, models.Like.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post not found! Requested ID: {id}")

    return post

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):

    post_q = db.query(models.Post).filter(models.Post.id == id)
    post = post_q.first()

    if post == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found! Requested ID: {id}")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action!")

    post_q.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.CreatePost, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):

    post_q = db.query(models.Post).filter(models.Post.id == id)
    post = post_q.first()

    if post == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found! Requested ID: {id}")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action!")

    post_q.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()


    return post_q.first()
