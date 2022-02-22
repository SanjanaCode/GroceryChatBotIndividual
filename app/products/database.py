
import sqlite3
import os
from enum import Enum, unique

mock_product_data = [
    {"id": "4011", "name": "banana", "names": "bananas", "price": "0.67",
     "price_scale": "per kg", "in_stock": True},
    {"id": "3022", "name": "strawberry", "names": "strawberries", "price": "3.99",
     "price_scale": "per box", "in_stock": True},
]


@unique
class DatabaseType(Enum):
    MEMORY = 0
    DATAFILE = 1


class SQLiteDatabase:

    def __init__(self, type: DatabaseType, **kwargs):
        # Initialize the information for the database
        self.database_config = ":memory:" if type is DatabaseType.MEMORY else os.path.join(
            os.getcwd(), "mock.db")

    def init_database(self):
        if not self.conn:
            return

        # Create the table
        create_table_sql = """
            CREATE TABLE product (
                id CHAR(4) PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                names VARCHAR(55) NOT NULL,
                price DECIMAL(8,2),
                price_scale VARCHAR(10),
                in_stock INT NOT NULL
            );
        """
        self.execute_update(create_table_sql)

        # Insert sample product information

        for prod in mock_product_data:
            insert_sql = f"""
            INSERT INTO product VALUES ("{prod['id']}", "{prod['name']}", "{prod['names']}", {prod['price']}, "{prod['price_scale']}", {prod['in_stock']});
            """
            self.execute_update(insert_sql)
        self.conn.commit()

    def connect(self):
        self.conn = sqlite3.connect(self.database_config)

    def close(self):
        self.conn.close()

    def execute_query(self, query):
        return self.conn.execute(query)

    def execute_update(self, update_query):
        self.conn.execute(update_query)


def main():
    db = SQLiteDatabase(DatabaseType.MEMORY)
    db.connect()
    db.init_database()
    cursor = db.execute_query("SELECT * FROM product")
    for row in cursor:
        print(row)
    db.close()


# Use for testing
if __name__ == "__main__":
    main()
