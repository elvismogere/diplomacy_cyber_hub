import sqlite3
from datetime import datetime
import json
from config import DB_CONFIG

class Database:
    def __init__(self):
        self.db_name = DB_CONFIG['name']
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.create_tables()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()

    def create_tables(self):
        """Create all necessary database tables"""
        try:
            # Create tables for each model
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS organizations (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    country TEXT,
                    address TEXT,
                    contact_email TEXT,
                    contact_phone TEXT,
                    security_level TEXT,
                    subscription_status TEXT,
                    max_users INTEGER,
                    features_enabled TEXT,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    is_active BOOLEAN
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    organization_id TEXT,
                    role TEXT,
                    last_login TIMESTAMP,
                    mfa_enabled BOOLEAN,
                    failed_login_attempts INTEGER,
                    password_changed_at TIMESTAMP,
                    is_locked BOOLEAN,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    is_active BOOLEAN,
                    FOREIGN KEY (organization_id) REFERENCES organizations (id)
                )
            ''')

            # Add more table creation statements for other models...

            self.connection.commit()
            return True
        except Exception as e:
            print(f"Table creation error: {e}")
            return False

    def execute_query(self, query, params=None):
        """Execute a database query"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Query execution error: {e}")
            return False

    def fetch_one(self, query, params=None):
        """Fetch a single record"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Fetch error: {e}")
            return None

    def fetch_all(self, query, params=None):
        """Fetch all records"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Fetch error: {e}")
            return []
