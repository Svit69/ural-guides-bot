from aiogram.types import InlineKeyboardButton

from src.admin.callbacks import AdminCallbackData


class AdminMainKeyboardRows:
    def build_rows(self) -> list[list[InlineKeyboardButton]]:
        return [
            [self.__button("Пользователи", AdminCallbackData.USERS)],
            [self.__button("Купили гайд по ВИЗу", AdminCallbackData.VIZ_BUYERS)],
            [self.__button("Купили прогулку по Екатеринбургу", AdminCallbackData.CITY_BUYERS)],
            [self.__button("Показать все отзывы", AdminCallbackData.FEEDBACK)],
            [self.__button("Почистить отзывы", AdminCallbackData.CLEAR_FEEDBACK)],
            [self.__button("Редактировать контент", AdminCallbackData.EDIT_CONTENT)],
            [self.__button("Добавить администратора", AdminCallbackData.ADD_ADMIN)],
        ]

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
