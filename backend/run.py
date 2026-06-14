from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

try:
    client = MongoClient(MONGO_URI, tls=True)
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Error:", e)

@app.route("/")
def home():
    return {
        "message": "Hello from MediBot Backend"
    }

if __name__ == "__main__":
    app.run(debug=True)