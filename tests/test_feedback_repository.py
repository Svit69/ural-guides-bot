from pathlib import Path

from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.repositories.feedback_repository import FeedbackRepository


def test_feedback_repository_deletes_selected_feedback(tmp_path: Path) -> None:
    connection_factory = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    DatabaseSchemaInitializer(connection_factory).initialize_schema()
    feedback_repository = FeedbackRepository(connection_factory)
    feedback_repository.save_feedback({"user_id": 1, "full_name": "Аня", "text": "Первый"})
    feedback_repository.save_feedback({"user_id": 2, "full_name": "Оля", "text": "Второй"})
    feedback_ids = [int(item["id"]) for item in feedback_repository.get_all_feedback()]

    deleted_count = feedback_repository.delete_feedback_by_ids([feedback_ids[0]])

    remaining = feedback_repository.get_all_feedback()
    assert deleted_count == 1
    assert len(remaining) == 1
    assert int(remaining[0]["id"]) == feedback_ids[1]
