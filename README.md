# Ural Guides Bot

Telegram bot for a travel guide around the Bolshoy Konny peninsula.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN="your-token"
python -m src.main
```

The bot expects `TELEGRAM_BOT_TOKEN` in the environment. Local `.env` files are ignored by git.
