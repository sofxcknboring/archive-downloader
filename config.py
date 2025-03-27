import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# uvicorn settings
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# Путь к папкам для архивации
BASE_DIR = Path(os.getenv("BASE_DIR"))
# Путь к папке, где будут лежать архивы
ARCHIVE_DIR = Path(os.getenv("ARCHIVE_DIR"))

SECRET_JWT_KEY = os.getenv("SECRET_JWT_KEY")
# Время жизни токена
TOKEN_EXPIRATION_TIME = os.getenv("TOKEN_EXPIRATION_TIME")

API_KEY = os.getenv("API_KEY")

