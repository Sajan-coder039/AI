import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    LOG_LEVEL = str(os.getenv("LOG_LEVEL"))
    PORT = int(os.getenv("PORT"))
