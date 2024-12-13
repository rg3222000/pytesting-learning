import os
from dotenv import load_dotenv

config = load_dotenv('pytesting.env')

port = os.getenv("PORT")
host = os.getenv("HOST")
