from html import escape


def escape_telegram_html(value: str) -> str:
    return escape(value, quote=False)


def wrap_bold(value: str) -> str:
    return f"<b>{value}</b>"


def wrap_link(text: str, url: str) -> str:
    return f'<a href="{escape(url, quote=True)}">{text}</a>'


def wrap_blockquote(value: str) -> str:
    return f"<blockquote>{value}</blockquote>"
