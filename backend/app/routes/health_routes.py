from flask import Blueprint, jsonify
from app.utils import success_response

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():

    response = success_response(
        message="MediBot Backend Running"
    )

    print("\nHealth API Called")
    print(response)

    return jsonify(response), 200


@health_bp.route("/health/error", methods=["GET"])
def health_error():

    error_response = {
        "success": False,
        "message": "Sample Error",
        "data": None
    }

    print("\nError API Called")
    print(error_response)

    return jsonify(error_response), 400