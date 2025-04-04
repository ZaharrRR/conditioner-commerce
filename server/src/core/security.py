from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader

from core import settings, logger

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    logger.info(f"{api_key}")
    if api_key != settings.api.admin_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing X-API-KEY",
        )
    return api_key