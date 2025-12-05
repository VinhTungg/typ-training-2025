from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.post import PostCreate, PostResponse
from app.api import deps
from app.models.user import User
from app.crud import post as crud_post

router = APIRouter()

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post_in: PostCreate,
    db: Session = Depends(deps.get_db),
    cur_user: User = Depends(deps.get_current_user)
):
    return crud_post.create_post(db=db, post_in=post_in, user_id=cur_user.id)

@router.get("/", response_model=List[PostResponse])
def read_posts(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db)
):
    posts = crud_post.get_multi(db=db, skip=skip, limit=limit)
    return posts

@router.get("/{slug}", response_model=PostResponse)
def read_post_by_slug(
    slug: str,
    db: Session = Depends(deps.get_db)
):
    post = crud_post.get_by_slug(db=db, slug=slug)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bài viết không tồn tại")
    return post