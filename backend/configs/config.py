from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
admin_email = os.getenv('admin_email')
admin_password = os.getenv('admin_password')
secret_key = os.getenv('secret_key')
URL=None
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    URL= DATABASE_URL.replace("postgresql://","postgresql+psycopg://")
    
    