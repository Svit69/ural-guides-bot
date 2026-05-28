from src.messages.default_posts import DEFAULT_START_MESSAGE, START_POST_NUMBER
from src.repositories.post_repository import PostRepository


class StartMessageProvider:
    def __init__(self, post_repository: PostRepository) -> None:
        self.__post_repository = post_repository

    def get_start_post(self) -> dict[str, str | None]:
        stored_post = self.__post_repository.get_post(START_POST_NUMBER)
        if stored_post is None:
            return {"text": DEFAULT_START_MESSAGE, "photo_file_id": None}
        return {
            "text": stored_post["text"],
            "photo_file_id": stored_post["photo_file_id"],
        }
