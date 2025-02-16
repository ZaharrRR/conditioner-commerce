import os
import sys

from loguru import logger

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level}</level> | "
    "<yellow>{message}</yellow>"
)

logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format=LOG_FORMAT,
    level="DEBUG",
)

logger.add(
    f"{LOG_DIR}/app.log",
    rotation="10 MB",
    retention="15 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    enqueue=True,
)
