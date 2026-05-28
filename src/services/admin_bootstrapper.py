from src.repositories.admin_repository import AdminRepository


class AdminBootstrapper:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__admin_repository = admin_repository

    def seed_initial_admins(self, telegram_ids: tuple[int, ...]) -> None:
        for telegram_id in telegram_ids:
            self.__admin_repository.add_admin(telegram_id)
