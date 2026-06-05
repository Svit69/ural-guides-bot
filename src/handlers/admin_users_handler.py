from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.message_chunks import MessageChunks
from src.admin.user_list_presenter import UserListPresenter
from src.repositories.admin_repository import AdminRepository
from src.repositories.user_repository import UserRepository
from src.repositories.viz_access_repository import VizAccessRepository


class AdminUsersHandler:
    def __init__(
        self,
        admin_repository: AdminRepository,
        user_repository: UserRepository,
        viz_access_repository: VizAccessRepository,
    ) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__user_repository = user_repository
        self.__viz_access_repository = viz_access_repository
        self.__presenter = UserListPresenter()
        self.__chunks = MessageChunks()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_registered_users, F.data == AdminCallbackData.USERS
        )

    async def __send_registered_users(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        users = self.__user_repository.get_all_registered_users()
        buyer_count = self.__viz_access_repository.count_users_with_access()
        text = self.__presenter.build_user_list_text(users, buyer_count)
        for chunk in self.__chunks.split_text(text):
            await callback.message.answer(chunk)
