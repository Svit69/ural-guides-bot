from src.database.connection_factory import SqliteConnectionFactory
from src.messages.post_provider import PostProvider
from src.repositories.admin_repository import AdminRepository
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.repositories.viz_access_repository import VizAccessRepository


class RepositoryBundle:
    def __init__(self, connections: SqliteConnectionFactory) -> None:
        self.admins = AdminRepository(connections)
        self.feedback = FeedbackRepository(connections)
        self.media = PostMediaRepository(connections)
        self.posts = PostRepository(connections)
        self.users = UserRepository(connections)
        self.viz_access = VizAccessRepository(connections)
        self.city_access = CityAccessRepository(connections)
        self.post_provider = PostProvider(self.posts, self.media)

    def build_user_context(self) -> dict[str, object]:
        return {
            "admins": self.admins,
            "feedback": self.feedback,
            "media": self.media,
            "posts": self.posts,
            "users": self.users,
            "viz_access": self.viz_access,
            "city_access": self.city_access,
        }
