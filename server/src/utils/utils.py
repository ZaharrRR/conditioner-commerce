import uuid

from fastapi import UploadFile, HTTPException

ALLOWED_CONTENT_TYPES = {"image/png", "image/jpeg", "image/jpg"}
MAX_FILE_SIZE = 3 * 1024 * 1024  # 3 МБ

async def validate_logo(upload_file: UploadFile, entity_prefix: str) -> tuple[str, bytes]:
    if upload_file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Неверный тип файла. Разрешены только PNG и JPEG.")

    content = await upload_file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Размер файла превышает 3 МБ.")

    extension = upload_file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"

    object_key = f"{entity_prefix}/{unique_filename}"
    return object_key, content
