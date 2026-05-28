# Ural Guides Bot

Telegram bot for a travel guide around the Bolshoy Konny peninsula.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN="your-token"
$env:ADMIN_TELEGRAM_IDS="265485424"
python -m src.main
```

The bot expects `TELEGRAM_BOT_TOKEN` in the environment. Admin IDs and database path can be configured with `ADMIN_TELEGRAM_IDS` and `BOT_DATABASE_PATH`.
The subscription channel defaults to `@nast_bar`; override it with `SUBSCRIPTION_CHANNEL_USERNAME`.

Open the admin panel with `/admin`.

For subscription checks, add the bot to the channel as an administrator.
