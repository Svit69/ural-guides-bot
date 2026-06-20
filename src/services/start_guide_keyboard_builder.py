from aiogram.types import InlineKeyboardMarkup

from src.guides.keyboards import GuideKeyboardFactory
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.viz_access_repository import VizAccessRepository


class StartGuideKeyboardBuilder:
    def __init__(
        self,
        viz_access_repository: VizAccessRepository,
        city_access_repository: CityAccessRepository,
        viz_price_rub: str,
        city_price_rub: str,
    ) -> None:
        self.__city_access = city_access_repository
        self.__factory = GuideKeyboardFactory()
        self.__viz_access = viz_access_repository
        self.__viz_price_rub = viz_price_rub
        self.__city_price_rub = city_price_rub

    def build_for_user(self, user_id: int) -> InlineKeyboardMarkup:
        has_viz_access = self.__viz_access.has_access(user_id) if user_id else False
        has_city_access = self.__city_access.has_access(user_id) if user_id else False
        return self.__factory.build_guide_selection_keyboard(
            self.__viz_price_rub,
            has_viz_access,
            self.__city_price_rub,
            has_city_access,
        )
