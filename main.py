import jwt
from pathlib import Path
from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.responses import FileResponse
from utils import create_archive, generate_download_token
from config import API_KEY, SECRET_JWT_KEY, ARCHIVE_DIR

app = FastAPI()


@app.get("/archive/{folder_name}")
def archive_folder(folder_name: str, x_api_key: str = Header(None)):
    """ Архивирует нужную папку, если передан правильный API-ключ. """
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="not authorized")

    try:
        archive_path = create_archive(folder_name)
        archive_name = Path(archive_path).name
        token = generate_download_token(archive_name)

        download_url = f"/download?token={token}"
        return {"message": "Completed", "download_url": download_url}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/download")
def download_archive(token: str = Query(...)):
    try:
        payload = jwt.decode(token, SECRET_JWT_KEY, algorithms=["HS256"])
        file_name = payload["file_name"]
        file_path = ARCHIVE_DIR / file_name

        if not file_path.exists():
            raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(path=file_path, filename=file_name, media_type='application/zip')

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token is expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token is invalid")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)