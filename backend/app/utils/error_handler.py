def error_response(message, status_code=400):
    return {
        "success": False,
        "message": message,
        "data": None
    }, status_code