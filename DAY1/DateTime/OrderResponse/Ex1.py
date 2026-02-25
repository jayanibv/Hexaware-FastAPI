import os
from dotenv import load_dotenv
#load environment variables from .env file
load_dotenv()

print("App Name:", os.getenv("APP_NAME"))
print("Version:", os.getenv("VERSION"))
print("Debug:", os.getenv("DEBUG"))