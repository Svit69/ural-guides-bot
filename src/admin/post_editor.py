from src.messages.default_posts import DEFAULT_START_MESSAGE
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class AdminPostEditor:
    def __init__(
        self, post_repository: PostRepository, media_repository: PostMediaRepository
    ) -> None:
        self.__post_repository = post_repository
        self.__media_repository = media_repository

    def get_editable_post(self, post_number: int) -> dict[str, object]:
        stored_post = self.__post_repository.get_post(post_number)
        if stored_post is not None:
            stored_post["media"] = self.__media_repository.get_post_media(post_number)
            return stored_post
        return {"text": DEFAULT_START_MESSAGE, "media": []}

    def save_post_with_existing_media(self, post_number: int, text: str) -> None:
        self.__post_repository.save_post(post_number, text)

    def save_post_with_new_media(
        self, post_number: int, text: str, media_items: list[dict[str, str]]
    ) -> None:
        self.__post_repository.save_post(post_number, text)
        self.__media_repository.replace_post_media(post_number, media_items)
