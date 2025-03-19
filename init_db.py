from app import app, db
import os

# First check if database file exists and rename it if it does
if os.path.exists('instance/database.db'):
    if os.path.exists('instance/database.db.bak'):
        os.remove('instance/database.db.bak')
    try:
        os.rename('instance/database.db', 'instance/database.db.bak')
        print("Backed up existing database to database.db.bak")
    except:
        print("Could not rename database file, it might be in use.")
        print("Please stop the Flask server and run this script again.")
        exit(1)

# Create all tables with the updated schema
with app.app_context():
    db.create_all()
    print("Database created successfully with the new schema!")
    print("You can now start the Flask server again.") 