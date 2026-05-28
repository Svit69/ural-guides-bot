from pathlib import Path

from aiogram.types import User

from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.user_repository import UserRepository


def test_admin_and_user_repositories_persist_data(tmp_path: Path) -> None:
    connection_factory = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    DatabaseSchemaInitializer(connection_factory).initialize_schema()

    admin_repository = AdminRepository(connection_factory)
    user_repository = UserRepository(connection_factory)
    media_repository = PostMediaRepository(connection_factory)
    admin_repository.add_admin(265485424)
    media_repository.replace_post_media(1, [{"media_type": "video", "file_id": "abc"}])
    user_repository.save_registered_user(
        User(id=1, is_bot=False, first_name="Настя", username="nast_bar")
    )

    users = user_repository.get_all_registered_users()

    assert admin_repository.is_admin(265485424)
    assert users[0]["telegram_id"] == 1
    assert users[0]["username"] == "nast_bar"
    assert media_repository.get_post_media(1)[0]["media_type"] == "video"
