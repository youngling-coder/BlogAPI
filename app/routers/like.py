from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2


router = APIRouter(
    prefix="/like",
    tags=["Likes"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.CreateLike, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):

    post_exists = db.query(models.Post).filter(models.Post.id == like.post_id).first()

    if not post_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found! ID: {like.post_id}")

    like_q = db.query(models.Like).filter(models.Like.post_id == like.post_id, models.Like.user_id == current_user.id)

    found_like = like_q.first()
    if like.dir == 1:
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Like already exists!")
        new_like = models.Like(post_id=like.post_id, user_id=current_user.id)
        db.add(new_like)
        db.commit()

        return {"message": "Liked!"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Like doesn't exist!")

        like_q.delete(synchronize_session=False)
        db.commit()

        return {"message": "Unliked!"}
