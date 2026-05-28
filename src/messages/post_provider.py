from src.messages.default_post_catalog import DefaultPostCatalog
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class PostProvider:
    def __init__(
        self, post_repository: PostRepository, media_repository: PostMediaRepository
    ) -> None:
        self.__post_repository = post_repository
        self.__media_repository = media_repository
        self.__default_catalog = DefaultPostCatalog()

    def get_post(self, post_number: int) -> dict[str, object]:
        stored_post = self.__post_repository.get_post(post_number)
        if stored_post is None:
            return {
                "text": self.__default_catalog.get_default_text(post_number),
                "media": [],
            }
        return {
            "text": stored_post["text"],
            "media": self.__media_repository.get_post_media(post_number),
        }
