from pymongo import MongoClient
from app.config.config import Config

client = None


def connect_db():
    global client

    try:
        print("MONGO_URI =", Config.MONGO_URI)
        
        client = MongoClient(
            Config.MONGO_URI,
            serverSelectionTimeoutMS=5000
        )

        client.admin.command("ping")

        print("✅ MongoDB Connected Successfully")

    except Exception as e:
        print("❌ MongoDB Connection Error:", e)

    return client