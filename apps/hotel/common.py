import os
from py4web import DAL
from py4web.core import required_folder

APP_FOLDER = os.path.dirname(__file__)
DB_FOLDER = required_folder(APP_FOLDER, "databases")

db = DAL(
    "sqlite://storage.db",
    folder=DB_FOLDER,
    migrate=True,
)