from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.message_chunks import MessageChunks
from src.admin.user_list_presenter import UserListPresenter
from src.repositories.admin_repository import AdminRepository
from src.repositories.viz_access_repository import VizAccessRepository


class AdminVizBuyersHandler:
    def __init__(self, admins: AdminRepository, access: VizAccessRepository) -> None:
        self.__guard = AdminAccessGuard(admins)
        self.__access = access
        self.__chunks = MessageChunks()
        self.__presenter = UserListPresenter()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_viz_buyers, F.data == AdminCallbackData.VIZ_BUYERS
        )

    async def __send_viz_buyers(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        text = self.__presenter.build_viz_buyer_list_text(
            self.__access.get_users_with_access()
        )
        for chunk in self.__chunks.split_text(text):
            await callback.message.answer(chunk)
