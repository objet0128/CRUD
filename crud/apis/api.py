from fastapi import APIRouter

from crud.apis import article, comment, user

api_router = APIRouter()
api_router.include_router(article.router, prefix="/articles", tags=["articles"])
api_router.include_router(comment.router, prefix="/comments", tags=["comments"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
