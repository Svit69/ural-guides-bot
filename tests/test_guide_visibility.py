from pathlib import Path

from src.database.connection_factory import SqliteConnectionFactory
from src.database.guide_visibility_schema_initializer import GuideVisibilitySchemaInitializer
from src.guides.guide_ids import GUIDE_CHEKISTS
from src.repositories.guide_visibility_repository import GuideVisibilityRepository


def test_chekists_guide_is_hidden_by_default(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    GuideVisibilitySchemaInitializer(connections).initialize_schema()
    repository = GuideVisibilityRepository(connections)

    assert GUIDE_CHEKISTS not in repository.get_visible_guide_ids()
    assert repository.get_visibility_map()[GUIDE_CHEKISTS] is False


def test_toggles_chekists_guide_visibility(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    GuideVisibilitySchemaInitializer(connections).initialize_schema()
    repository = GuideVisibilityRepository(connections)

    assert repository.toggle_visibility(GUIDE_CHEKISTS) is True
    assert GUIDE_CHEKISTS in repository.get_visible_guide_ids()
