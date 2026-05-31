from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class AdminMediaUploadMixin:
    async def _save_without_new_media(self, callback, state) -> None:
        await callback.answer()
        if not self._guard.is_admin_callback(callback) or callback.message is None:
            return
        data = await state.get_data()
        self._post_editor.save_post_with_existing_media(data["post_number"], data["text"])
        await state.clear()
        await callback.message.answer("Пост сохранен без новых медиа.")

    async def _collect_uploaded_media(self, message: Message, state: FSMContext) -> None:
        if not self._guard.is_admin_message(message):
            await state.clear()
            return
        media_item = self._media_extractor.extract_media_item(message)
        data = await state.get_data()
        media_items = [*data.get("media_items", []), media_item]
        await state.update_data(media_items=media_items)
        await message.answer(
            f"Медиа добавлено: {len(media_items)}. Еще или напишите: готово"
        )

    async def _finish_media_upload(self, message: Message, state: FSMContext) -> None:
        if not self._guard.is_admin_message(message):
            await state.clear()
            return
        data = await state.get_data()
        self._post_editor.save_post_with_new_media(data["post_number"], data["text"], data.get("media_items", []))
        await state.clear()
        await message.answer("Пост сохранен с новыми медиа.")
