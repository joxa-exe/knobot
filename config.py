import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    # Bot - os.getenv ichiga VARIABLE NOMI yoziladi
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "6513975219:AAGYkY2pFPGyttgOKKWaCLrGwL43aT6IbHw")
    ADMIN_ID: int = int(os.getenv("ADMIN_ID", "1179710266"))

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:TUBRGikqczkWdvbVOYpuaquDbxvamQoE@yamabiko.proxy.rlwy.net:59015/railway")

    # Qolganlari
    CHANNEL_USERNAME: str = os.getenv("CHANNEL_USERNAME", "")
    MAX_CHANNELS: int = 5
    ENABLE_STATISTICS: bool = True
    ENABLE_RATINGS: bool = True
    ENABLE_SEARCH: bool = True
    CACHE_TTL: int = 3600
    MAX_BROADCAST_RATE: float = 0.03
    MAX_MOVIE_SIZE_MB: int = 2000
    WELCOME_MESSAGE: str = "🎬 Xush kelibsiz! Premium kino botiga marhamat!"

config = Config()
