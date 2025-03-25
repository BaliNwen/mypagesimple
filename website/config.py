import os
from werkzeug.security import generate_password_hash

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a_very_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///waitlist.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Pre-hashed admin password. (Use generate_password_hash("Rose823") to get this value.)
    ADMIN_PASSWORD_HASH = generate_password_hash("Rose823")
