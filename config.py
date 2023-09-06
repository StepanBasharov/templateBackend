from dotenv import load_dotenv
import os


class DefaultConfig:
    """ Get DataBase URL from .env file"""
    load_dotenv()
    db_url = os.getenv("DB_URL")


