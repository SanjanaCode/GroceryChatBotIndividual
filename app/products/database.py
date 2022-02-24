
import sqlite3
import os
from enum import Enum, unique
from collections import OrderedDict

# Add data as needed
MOCK_PRODUCT_DATA = [
    OrderedDict({"id": "4011", "name": "banana", "names": "bananas", "price": "0.67",
                 "price_scale": "per kg", "in_stock": True}),
    OrderedDict({"id": "3022", "name": "strawberry", "names": "strawberries", "price": "3.99",
                 "price_scale": "per box", "in_stock": True}),
]


STORE_INFO = {
    "name": "Walmart",
    "address": "123 Main St",
    "city": "Toronto",
    "province": "ON",
    "postal_code": "M5V 2K7",
    "country": "Canada",
    "phone": "416-555-1234",
    "website": "https://www.walmart.ca",
    "opening_hours": "Mon-Fri: 9am-5pm",
    "price": "0.99 - 5.99 cad",
}


@unique
class DatabaseType(Enum):
    MEMORY = 0
    DATAFILE = 1


class SQLiteDatabase:
    """
    Class to interact with the database.
    """

    def __init__(self, type: DatabaseType, **kwargs):
        # Initialize the information for the database
        self.database_config = ":memory:" if type is DatabaseType.MEMORY else os.path.join(
            os.getcwd(), "mock.db")

    def init_database(self):
        """
        Initialize the database.
        """
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

        for prod in MOCK_PRODUCT_DATA:
            insert_sql = f"""
            INSERT INTO product VALUES ("{prod['id']}", "{prod['name']}", "{prod['names']}", {prod['price']}, "{prod['price_scale']}", {prod['in_stock']});
            """
            self.execute_update(insert_sql)
        self.conn.commit()

    def connect(self):
        self.conn = sqlite3.connect(self.database_config)

    def close(self):
        """
        Close the connection to the database.
        """
        self.conn.close()

    def execute_query(self, query):
        """
        Execute a select query.

        Parameters
        ----------
        query: str
            The select query to execute.
        """
        return self.conn.execute(query)

    def execute_update(self, update_query):
        """
        Execute an update query.

        Parameters
        ----------
        update_query: str
            The update query to execute.
        """
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
