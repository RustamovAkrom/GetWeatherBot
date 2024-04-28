from dotenv import load_dotenv
import os

load_dotenv()


TELEGRAM_BOT_SECRET_KEY = os.getenv("SECRET_KEY")
OPEN_WEATHER_SECRET_KEY = os.getenv("OPEN_WEATHER_KEY")
