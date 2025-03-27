Архивирует файлы, генерирует временную ссылку по которой можно скачать архив.

<b>how to</b>

Пример .env перед сборкой.
- SECRET_JWT_KEY и API_KEY сгенерировать самостоятельно.
- TOKEN_EXPIRATION_TIME - указал в 2 недели.

Оставить как есть:
- BASE_DIR=/app/source
- ARCHIVE_DIR=/app/archives

```
HOST=0.0.0.0
PORT=8000

BASE_DIR=/app/source
ARCHIVE_DIR=/app/archives

TOKEN_EXPIRATION_TIME=20160

SECRET_JWT_KEY=
API_KEY=
```
По docker-compose.yml.
- Если нужно изменить папку для хранения архивов:
- volumes:
  - /mnt/photosync:/app/source
  - /mnt/photosync/archives:/app/archives

- ports: "8000:8000"

```
docker-compose up --build -d
```
