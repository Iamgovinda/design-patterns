class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        print("Connecting to database...")

    def disconnect(self):
        print("Disconnecting from database...")


# Usage
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.connect()
    db2.disconnect()

    print("Same instance?", db1 is db2)  # True
