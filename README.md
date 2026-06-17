# Ural Guides Bot

Telegram bot for a travel guide around the Bolshoy Konny peninsula.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN="your-token"
$env:ADMIN_TELEGRAM_IDS="265485424"
$env:YOOKASSA_SHOP_ID="your-shop-id"
$env:YOOKASSA_SECRET_KEY="your-secret-key"
$env:VIZ_GUIDE_PRICE_RUB="500.00"
$env:CITY_GUIDE_PRICE_RUB="700.00"
$env:YOOKASSA_RETURN_URL="https://t.me/nast_bar_bot"
python -m src.main
```

The bot expects `TELEGRAM_BOT_TOKEN` in the environment. Admin IDs and database path can be configured with `ADMIN_TELEGRAM_IDS` and `BOT_DATABASE_PATH`.
The subscription channel defaults to `@nast_bar`; override it with `SUBSCRIPTION_CHANNEL_USERNAME`.

Open the admin panel with `/admin`.

For subscription checks, add the bot to the channel as an administrator.

Paid guides are available only after YooKassa confirms a successful payment.
Keep YooKassa credentials in environment variables or a local `.env` file.
Use a persistent path or mounted volume for `BOT_DATABASE_PATH`; paid guide access is stored in SQLite.
