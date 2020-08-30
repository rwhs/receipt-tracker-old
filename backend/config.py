import os
from dotenv import load_dotenv
load_dotenv()

POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")