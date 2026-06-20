from aiogram.types import Message

from src.guides.keyboards import GuideKeyboardFactory
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.viz_access_repository import VizAccessRepository


class GuideListSender:
    def __init__(
        self,
        viz_access_repository: VizAccessRepository,
        city_access_repository: CityAccessRepository,
        viz_price_rub: str,
        city_price_rub: str,
    ) -> None:
        self.__city_access_repository = city_access_repository
        self.__keyboard_factory = GuideKeyboardFactory()
        self.__viz_access_repository = viz_access_repository
        self.__viz_price_rub = viz_price_rub
        self.__city_price_rub = city_price_rub

    async def send_guide_list(
        self, message: Message, text: str, user_id: int | None = None
    ) -> None:
        user_id = user_id or (message.from_user.id if message.from_user else 0)
        await message.answer(text, reply_markup=self.__build_keyboard(user_id))

    def __build_keyboard(self, user_id: int):
        has_viz_access = self.__viz_access_repository.has_access(user_id) if user_id else False
        has_city_access = self.__city_access_repository.has_access(user_id) if user_id else False
        return self.__keyboard_factory.build_guide_selection_keyboard(
            self.__viz_price_rub,
            has_viz_access,
            self.__city_price_rub,
            has_city_access,
        )
