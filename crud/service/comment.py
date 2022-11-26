from crud.apis.request.comment import CommentCreateDTO
from crud.repository.comment import CommentRepository
from crud.schema.comment import CommentSchema


class CommentService:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def create_comment(self, user_id: int, article_id: int, request: CommentCreateDTO) -> CommentSchema:
        comment_entity = CommentSchema(**request.dict())
        return self.repository.create_comment(comment=comment_entity, user_id=user_id, article_id=article_id)

    def get_comments_by_author(self, author_id: int) -> list[CommentSchema] | None:
        return self.repository.get_comments_by_author(author_id=author_id)
