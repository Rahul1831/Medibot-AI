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
    print("📊 Count   : http://127.0.0.1:5000/api/v1/patients/count")
    print("➕ Create  : http://127.0.0.1:5000/api/v1/patients/test-create")
    print("🗑 Delete  : http://127.0.0.1:5000/api/v1/patients/delete/1")
    print("===================================\n")

    app.run(debug=False)