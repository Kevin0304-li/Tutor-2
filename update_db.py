import sqlite3
import os

# Database file path
db_path = 'instance/database.db'

try:
    # Connect to the SQLite database
    print(f"Connecting to database at {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if profile_image column exists in the user table
    cursor.execute("PRAGMA table_info(user);")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    if 'profile_image' not in column_names:
        print("Adding 'profile_image' column to the user table...")
        # Add the profile_image column to the user table
        cursor.execute("ALTER TABLE user ADD COLUMN profile_image VARCHAR(200) DEFAULT 'default_profile.jpg';")
        conn.commit()
        print("Database schema updated successfully!")
    else:
        print("The 'profile_image' column already exists in the user table.")
    
    # Close the connection
    conn.close()
    print("Database connection closed.")
    print("You can now restart the Flask application.")
    
except sqlite3.Error as e:
    print(f"SQLite error: {e}")
except Exception as e:
    print(f"Error: {e}") 