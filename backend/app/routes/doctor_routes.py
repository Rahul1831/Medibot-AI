from flask import Blueprint, jsonify
from app.services.doctor_service import (
    get_all_doctors,
    get_doctor_by_id,
    create_doctor,
    get_doctor_count,
    delete_doctor
)

doctor_bp = Blueprint("doctor", __name__)


@doctor_bp.route("/", methods=["GET"])
def get_doctors():

    doctors = get_all_doctors()

    return jsonify({
        "success": True,
        "message": "Doctors Retrieved Successfully",
        "data": doctors
    }), 200


@doctor_bp.route("/count", methods=["GET"])
def doctor_count():

    count = get_doctor_count()

    return jsonify({
        "success": True,
        "message": "Doctor Count Retrieved",
        "data": {
            "count": count
        }
    }), 200


@doctor_bp.route("/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):

    doctor = get_doctor_by_id(doctor_id)

    if not doctor:
        return jsonify({
            "success": False,
            "message": "Doctor Not Found",
            "data": None
        }), 404

    return jsonify({
        "success": True,
        "message": "Doctor Retrieved Successfully",
        "data": doctor
    }), 200


@doctor_bp.route("/delete/<int:doctor_id>", methods=["GET"])
def remove_doctor(doctor_id):

    doctor = delete_doctor(doctor_id)

    if not doctor:
        return jsonify({
            "success": False,
            "message": "Doctor Not Found",
            "data": None
        }), 404

    return jsonify({
        "success": True,
        "message": "Doctor Deleted Successfully",
        "data": doctor
    }), 200


@doctor_bp.route("/test-create", methods=["GET"])
def test_create_doctor():

    doctor = create_doctor(
        "Dr. Kumar",
        "Orthopedic",
        10
    )

    return jsonify({
        "success": True,
        "message": "Doctor Created Successfully",
        "data": doctor
    }), 201