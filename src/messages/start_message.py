from src.messages.default_posts import DEFAULT_START_MESSAGE, START_POST_NUMBER
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class StartMessageProvider:
    def __init__(
        self, post_repository: PostRepository, media_repository: PostMediaRepository
    ) -> None:
        self.__post_repository = post_repository
        self.__media_repository = media_repository

    def get_start_post(self) -> dict[str, object]:
        stored_post = self.__post_repository.get_post(START_POST_NUMBER)
        if stored_post is None:
            return {"text": DEFAULT_START_MESSAGE, "media": []}
        return {
            "text": stored_post["text"],
            "media": self.__media_repository.get_post_media(START_POST_NUMBER),
        }
