import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s--*--%(name)s--*--%(levelname)s--*--%(message)s",
    datefmt="%Y/%m/%d--*--%H/%M/%S",
    handlers=[
        logging.FileHandler("inform.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("APP_RUNNING")