class GuideButtonTextFactory:
    def build_viz_text(self, price_rub: str, has_access: bool) -> str:
        price = self.__format_price(price_rub)
        return "ВИЗ" if has_access else self.__build_paid_text("ВИЗ", price)

    def build_city_text(self, price_rub: str, has_access: bool) -> str:
        title = "Прогулка по Екатеринбургу"
        price = self.__format_price(price_rub)
        return title if has_access else self.__build_paid_text(title, price)

    def __format_price(self, raw_price: str) -> str:
        normalized_price = raw_price.removesuffix(".00")
        return f"{normalized_price} ₽" if normalized_price else ""

    def __build_paid_text(self, title: str, price: str) -> str:
        return f"{title} {price} 💳" if price else f"{title} 💳"
