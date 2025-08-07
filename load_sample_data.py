"""
Utility script to load sample CSV data into the database

Run this script to populate the database with sample log data for testing.
"""

from app.db import init_database, load_csv_data

def main():
    print("🔄 Initializing database...")
    init_database()
    
    print("📊 Loading sample data...")
    success = load_csv_data("sample_logs.csv")
    
    if success:
        print("✅ Sample data loaded successfully!")
        print("🚀 You can now start the server with: python main.py")
    else:
        print("❌ Failed to load sample data")

if __name__ == "__main__":
    main() 