import os
from dotenv import load_dotenv

load_dotenv()

VK_GROUP_TOKEN = os.getenv('VK_GROUP_TOKEN')
VK_USER_TOKEN = os.getenv('VK_USER_TOKEN')
DB_CONFIG = {
    'host': os.getenv('DB_HOST'), 
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    }
