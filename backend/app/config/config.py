import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "medibot-secret-key")
    MONGO_URI = os.getenv("MONGO_URI")