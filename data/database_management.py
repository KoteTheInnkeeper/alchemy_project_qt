"""
    This file aims to work over the database. It creates a 'Database' object with it's own methods to getting the
    info we want.
"""
from data.database_connection import DatabaseConnection as DatabaseConnect


class Database:
    def __init__(self, host: str):
        self.host = host
