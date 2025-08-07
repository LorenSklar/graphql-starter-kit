"""
Database connection and utilities for SQLite

This module provides direct SQLite database operations without SQLAlchemy.
Uses sqlite3 for direct SQL queries and pandas for CSV data loading.
"""

import sqlite3
import pandas as pd
import os
from pathlib import Path

# Database file path
DB_PATH = "logs.db"

def get_db_connection():
    """Create and return a SQLite database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_database():
    """Initialize the database with the logs table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create logs table with the actual CSV schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TIMESTAMP TEXT NOT NULL,
            REQUEST_ID TEXT,
            METHOD TEXT,
            PATH TEXT,
            QUERY_PARAMETERS TEXT,
            PROTOCOL TEXT,
            SOURCE_IP TEXT,
            USER_AGENT TEXT,
            REFERER TEXT,
            USER_ID TEXT,
            SESSION_ID TEXT,
            REQUEST_HEADERS TEXT,
            REQUEST_BODY TEXT,
            CONTENT_LENGTH INTEGER,
            STATUS_CODE INTEGER,
            RESPONSE_TIME_MS INTEGER,
            RESPONSE_HEADERS TEXT,
            RESPONSE_BODY TEXT,
            LOG_LEVEL TEXT,
            SERVICE_NAME TEXT,
            ENV TEXT,
            ERROR_MESSAGE TEXT,
            STACK_TRACE TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"✅ Database initialized: {DB_PATH}")

def load_csv_data(csv_file_path):
    """
    Load CSV data into the SQLite database
    
    Args:
        csv_file_path (str): Path to the CSV file
    """
    if not os.path.exists(csv_file_path):
        print(f"❌ CSV file not found: {csv_file_path}")
        return False
    
    try:
        # Read CSV with pandas
        df = pd.read_csv(csv_file_path)
        
        # Connect to database
        conn = get_db_connection()
        
        # Insert data into logs table
        df.to_sql('logs', conn, if_exists='append', index=False)
        
        conn.close()
        print(f"✅ Loaded {len(df)} records from {csv_file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error loading CSV data: {e}")
        return False

def get_logs(limit=100, offset=0, log_level=None, service_name=None, status_code=None, env=None):
    """
    Get logs with optional filtering and pagination
    
    Args:
        limit (int): Number of records to return
        offset (int): Number of records to skip
        log_level (str): Filter by log level
        service_name (str): Filter by service name
        status_code (int): Filter by status code
        env (str): Filter by environment
    
    Returns:
        list: List of log records as dictionaries
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Build query with optional filters
    query = "SELECT * FROM logs WHERE 1=1"
    params = []
    
    if log_level:
        query += " AND LOG_LEVEL = ?"
        params.append(log_level)
    
    if service_name:
        query += " AND SERVICE_NAME = ?"
        params.append(service_name)
    
    if status_code:
        query += " AND STATUS_CODE = ?"
        params.append(status_code)
    
    if env:
        query += " AND ENV = ?"
        params.append(env)
    
    query += " ORDER BY TIMESTAMP DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    # Convert to list of dictionaries
    logs = []
    for row in rows:
        logs.append(dict(row))
    
    conn.close()
    return logs

def get_log_count(log_level=None, service_name=None, status_code=None, env=None):
    """
    Get total count of logs with optional filtering
    
    Args:
        log_level (str): Filter by log level
        service_name (str): Filter by service name
        status_code (int): Filter by status code
        env (str): Filter by environment
    
    Returns:
        int: Total count of matching records
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT COUNT(*) FROM logs WHERE 1=1"
    params = []
    
    if log_level:
        query += " AND LOG_LEVEL = ?"
        params.append(log_level)
    
    if service_name:
        query += " AND SERVICE_NAME = ?"
        params.append(service_name)
    
    if status_code:
        query += " AND STATUS_CODE = ?"
        params.append(status_code)
    
    if env:
        query += " AND ENV = ?"
        params.append(env)
    
    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    
    conn.close()
    return count 