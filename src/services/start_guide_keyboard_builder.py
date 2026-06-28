from aiogram.types import InlineKeyboardMarkup

from src.guides.keyboards import GuideKeyboardFactory
from src.repositories.admin_repository import AdminRepository
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.guide_visibility_repository import GuideVisibilityRepository
from src.repositories.viz_access_repository import VizAccessRepository


class StartGuideKeyboardBuilder:
    def __init__(
        self,
        viz_access_repository: VizAccessRepository,
        city_access_repository: CityAccessRepository,
        admin_repository: AdminRepository,
        visibility_repository: GuideVisibilityRepository,
        viz_price_rub: str,
        city_price_rub: str,
    ) -> None:
        self.__city_access = city_access_repository
        self.__factory = GuideKeyboardFactory()
        self.__admins = admin_repository
        self.__visibility = visibility_repository
        self.__viz_access = viz_access_repository
        self.__viz_price_rub = viz_price_rub
        self.__city_price_rub = city_price_rub

    def build_for_user(self, user_id: int) -> InlineKeyboardMarkup:
        has_viz_access = self.__viz_access.has_access(user_id) if user_id else False
        has_city_access = self.__city_access.has_access(user_id) if user_id else False
        visible_guides = self.__get_visible_guides(user_id)
        return self.__factory.build_guide_selection_keyboard(
            self.__viz_price_rub,
            has_viz_access,
            self.__city_price_rub,
            has_city_access,
            visible_guides,
        )

    def __get_visible_guides(self, user_id: int) -> set[str]:
        if user_id and self.__admins.is_admin(user_id):
            from src.guides.guide_ids import ALL_GUIDES
            return set(ALL_GUIDES)
        return self.__visibility.get_visible_guide_ids()
