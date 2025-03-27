import shutil
from datetime import datetime, timedelta
from pathlib import Path

import jwt

from config import BASE_DIR, ARCHIVE_DIR, SECRET_JWT_KEY, TOKEN_EXPIRATION_TIME

def create_archive(folder_name: str) -> str:
    """
    :param folder_name: Имя папки для архивации
    :return: путь к архиву
    """
    src_folder = BASE_DIR / folder_name

    if not src_folder.exists():
        raise FileNotFoundError("File not found")

    archive_name = f"{folder_name}.zip"
    archive_path = ARCHIVE_DIR / archive_name

    shutil.make_archive(str(archive_path.with_suffix("")), 'zip', root_dir=src_folder)

    return str(archive_path)

def generate_download_token(file_name: str) -> str:
    """
    :param file_name: Имя файла для которого будет сгенерирован токен
    :return: закодированный JWT
    """
    payload = {
        "file_name": file_name,
        "exp": datetime.now() + timedelta(minutes=int(TOKEN_EXPIRATION_TIME))
    }
    return jwt.encode(payload, SECRET_JWT_KEY, algorithm="HS256")