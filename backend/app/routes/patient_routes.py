from flask import Blueprint, jsonify
from app.services.patient_service import (
    get_all_patients,
    get_patient_by_id,
    create_patient,
    get_patient_count,
    delete_patient
)

patient_bp = Blueprint("patient", __name__)


@patient_bp.route("/", methods=["GET"])
def get_patients():

    patients = get_all_patients()

    return jsonify({
        "success": True,
        "message": "Patients Retrieved Successfully",
        "data": patients
    }), 200


@patient_bp.route("/count", methods=["GET"])
def patient_count():

    count = get_patient_count()

    return jsonify({
        "success": True,
        "message": "Patient Count Retrieved",
        "data": {
            "count": count
        }
    }), 200


@patient_bp.route("/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):

    patient = get_patient_by_id(patient_id)

    if not patient:
        return jsonify({
            "success": False,
            "message": "Patient Not Found",
            "data": None
        }), 404

    return jsonify({
        "success": True,
        "message": "Patient Retrieved Successfully",
        "data": patient
    }), 200


@patient_bp.route("/delete/<int:patient_id>", methods=["GET"])
def remove_patient(patient_id):

    patient = delete_patient(patient_id)

    if not patient:
        return jsonify({
            "success": False,
            "message": "Patient Not Found",
            "data": None
        }), 404

    return jsonify({
        "success": True,
        "message": "Patient Deleted Successfully",
        "data": patient
    }), 200


@patient_bp.route("/test-create", methods=["GET"])
def test_create_patient():

    patient = create_patient(
        "David",
        35,
        "Male"
    )

    return jsonify({
        "success": True,
        "message": "Patient Created Successfully",
        "data": patient
    }), 201