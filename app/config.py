import os
from dotenv import load_dotenv
load_dotenv()
database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_pass = os.getenv('DATABASE_PASSWORD')
