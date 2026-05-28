from src.messages.default_posts import START_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class StartMessageProvider:
    def __init__(
        self, post_repository: PostRepository, media_repository: PostMediaRepository
    ) -> None:
        self.__post_provider = PostProvider(post_repository, media_repository)

    def get_start_post(self) -> dict[str, object]:
        return self.__post_provider.get_post(START_POST_NUMBER)
