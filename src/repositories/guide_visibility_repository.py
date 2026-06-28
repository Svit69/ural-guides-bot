from src.database.connection_factory import SqliteConnectionFactory
from src.guides.guide_ids import ALL_GUIDES, DEFAULT_VISIBLE_GUIDES


class GuideVisibilityRepository:
    def __init__(self, connection_factory: SqliteConnectionFactory) -> None:
        self.__connections = connection_factory

    def get_visible_guide_ids(self) -> set[str]:
        with self.__connections.open_connection() as connection:
            rows = connection.execute("select * from guide_visibility").fetchall()
        return {str(row["guide_id"]) for row in rows if int(row["is_visible"]) == 1}

    def get_visibility_map(self) -> dict[str, bool]:
        visible_guides = self.get_visible_guide_ids()
        return {guide_id: guide_id in visible_guides for guide_id in ALL_GUIDES}

    def toggle_visibility(self, guide_id: str) -> bool:
        current_visibility = self.get_visibility_map().get(guide_id, False)
        next_visibility = not current_visibility
        with self.__connections.open_connection() as connection:
            connection.execute(
                "update guide_visibility set is_visible = ? where guide_id = ?",
                (1 if next_visibility else 0, guide_id),
            )
        return next_visibility

    def get_default_visible_guides(self) -> set[str]:
        return set(DEFAULT_VISIBLE_GUIDES)
