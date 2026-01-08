import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Data:
    # LOGIN = "Admin"
    # PASSWORD = "admin123"

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
