from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_id = os.getenv("admin_id")
DATA_PATH = os.getenv("DATA_PATH")
