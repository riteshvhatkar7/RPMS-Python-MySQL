import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Ritesh@123",  # Change as per your MySQL setup
    "database": "recruitment_portal"
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as exc:
        raise RuntimeError(f"Database connection failed: {exc}") from exc
