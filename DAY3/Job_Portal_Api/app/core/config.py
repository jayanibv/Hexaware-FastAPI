import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://postgres:root@localhost:5432/job_db"
SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
