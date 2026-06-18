from app import create_app

app = create_app()

if __name__ == "__main__":
    print("\n===================================")
    print("🚀 MediBot Backend Started")
    print("===================================")

    print("🏠 Home    : http://127.0.0.1:5000/")
    print("❤️ Health  : http://127.0.0.1:5000/api/v1/health")
    print("❌ Error   : http://127.0.0.1:5000/api/v1/health/error")

    print("👤 Patient : http://127.0.0.1:5000/api/v1/patients/")
    print("📊 P Count : http://127.0.0.1:5000/api/v1/patients/count")
    print("➕ P Create: http://127.0.0.1:5000/api/v1/patients/test-create")
    print("🗑 P Delete: http://127.0.0.1:5000/api/v1/patients/delete/1")

    print("🩺 Doctor  : http://127.0.0.1:5000/api/v1/doctors/")
    print("📊 D Count : http://127.0.0.1:5000/api/v1/doctors/count")
    print("➕ D Create: http://127.0.0.1:5000/api/v1/doctors/test-create")
    print("🗑 D Delete: http://127.0.0.1:5000/api/v1/doctors/delete/1")

    print("===================================\n")

    app.run(debug=False)