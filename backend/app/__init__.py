from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from app.routes.health_routes import health_bp
from app.routes.patient_routes import patient_bp
from app.config.config import Config
from app.database.mongodb import connect_db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    connect_db()

    @app.route("/")
    def home():
        return {
            "message": "Welcome to MediBot Backend"
        }

    app.register_blueprint(
        health_bp,
        url_prefix="/api/v1"
    )

    app.register_blueprint(
        patient_bp,
        url_prefix="/api/v1/patients"
    )

    return app