from src.messages.default_posts import DEFAULT_START_MESSAGE
from src.repositories.post_repository import PostRepository


class AdminPostEditor:
    def __init__(self, post_repository: PostRepository) -> None:
        self.__post_repository = post_repository

    def get_editable_post(self, post_number: int) -> dict[str, str | None]:
        stored_post = self.__post_repository.get_post(post_number)
        if stored_post is not None:
            return stored_post
        return {"text": DEFAULT_START_MESSAGE, "photo_file_id": None}

    def save_post_with_existing_photo(self, post_number: int, text: str) -> None:
        current_post = self.get_editable_post(post_number)
        self.__post_repository.save_post(
            post_number, text, current_post.get("photo_file_id")
        )

    def save_post_with_new_photo(
        self, post_number: int, text: str, photo_file_id: str
    ) -> None:
        self.__post_repository.save_post(post_number, text, photo_file_id)
