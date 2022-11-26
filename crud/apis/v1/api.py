from fastapi import APIRouter

from crud.apis.v1.endpoints import article, comment, user

api_router = APIRouter(prefix="/v1")
api_router.include_router(article.router, prefix="/articles", tags=["articles"])
api_router.include_router(comment.router, prefix="/comments", tags=["comments"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
