import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    """Singleton class to handle MySQL database connection."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._instance.conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_DATABASE"),
                    port=os.getenv("DB_PORT")
                )
                cls._instance.cursor = cls._instance.conn.cursor()
                cls._instance.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS search_history (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        artist_name VARCHAR(255),
                        search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                cls._instance.conn.commit()
                print("Connected to Cloud MySQL")
            except Error as e:
                print("Database connection error:", e)
        return cls._instance

    def insert_artist(self, artist_name):
        # Insert artist search history into the database.
        try:
            query = "INSERT INTO search_history (artist_name) VALUES (%s);"
            self.cursor.execute(query, (artist_name,))
            self.conn.commit()
        except Error as e:
            print("Insert error:", e)

    def fetch_history(self, limit=10):
        # Fetch recent artist searches.
        self.cursor.execute("""
            SELECT id, artist_name, search_time 
            FROM search_history 
            ORDER BY id DESC LIMIT %s;
        """, (limit,))
        return self.cursor.fetchall()

    def close(self):
        # Close database connection.
        self.cursor.close()
        self.conn.close()
