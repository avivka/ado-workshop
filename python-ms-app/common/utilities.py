def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def validate_data(data, schema):
    """Validates the given data against a schema."""
    # Placeholder for validation logic
    return True

def format_response(data, status_code=200):
    """Formats the response to be returned from the services."""
    return {
        "status": status_code,
        "data": data
    }