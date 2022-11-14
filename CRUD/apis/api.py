from fastapi import APIRouter

from CRUD.apis import articles, comments, users

api_router = APIRouter()
api_router.include_router(articles.router, prefix="/articles", tags=["articles"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
