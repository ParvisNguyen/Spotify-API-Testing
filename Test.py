
import mysql.connector
from mysql.connector import Error

HOST = "35.238.159.19"
USER = "root"
PASSWORD = "Tubby101."
DATABASE = "music_data_explorer"
PORT = 3306

try:
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        port=PORT
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            artist_name VARCHAR(255),
            search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Insert a sample record
    cursor.execute("INSERT INTO search_history (artist_name) VALUES (%s);", ("The Weeknd",))
    conn.commit()

    # Fetch and print the inserted record
    cursor.execute("SELECT id, artist_name, search_time FROM search_history ORDER BY id DESC LIMIT 10;")
    rows = cursor.fetchall()

    # Print fetched records
    print("Rows fetched:", rows)

    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    print("Connected and inserted data.")
except Error as e:
    print("Database error:", e)
