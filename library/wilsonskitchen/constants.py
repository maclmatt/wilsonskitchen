import logging

LOG_FORMAT = logging.Formatter(
    "%(asctime)-15s %(levelname)-5s  %(module)s -- %(message)s"
)
LOGGER = logging.getLogger("wilsons kitchen")
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(LOG_FORMAT)
FILE_HANDLER = logging.FileHandler("wilsons_kitchen.log")
FILE_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(CONSOLE_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.setLevel(logging.INFO)

DB_NAME = "wilsons_kitchen.db"