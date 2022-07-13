from fastapi import Response, status, HTTPException, Depends, APIRouter
from app import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id)
    found_post = post_query.first()

    if found_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {vote.post_id} does not exsist.")

    elif (vote.dir == 1) and (found_vote is not None):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user {current_user.id} has already voted on post {vote.post_id}")

    elif (vote.dir == 1) and (found_vote is None):
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote."}

    elif (vote.dir != 1) and (found_vote is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Vote does not exsist.")

    elif (vote.dir != 1) and (found_vote is not None):
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "vote successfully deleted."}
