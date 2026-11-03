def login(username, password):
    # Hardcoded secret
    JWT_SECRET = "super_secret_12345"

    # Critical SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return query
