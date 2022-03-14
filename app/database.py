
import sqlite3
import os
from enum import Enum, unique
from collections import OrderedDict
from app.error import SQLException

# Add data as needed
MOCK_PRODUCT_DATA = [
    OrderedDict({"id": "4011", "name": "banana", "names": "bananas", "price": "0.67",
                 "price_scale": "per kg", "in_stock": True}),
    OrderedDict({"id": "3022", "name": "strawberry", "names": "strawberries", "price": "3.99",
                 "price_scale": "per box", "in_stock": True}),
    OrderedDict({"id": "2011", "name": "apple", "names": "apples", "price": "0.49",
                 "price_scale": "per kg", "in_stock": True}),
    OrderedDict({"id": "5044", "name": "pear", "names": "pears", "price": "0.87",
                 "price_scale": "per kg", "in_stock": False}),
    OrderedDict({"id": "8088", "name": "bread", "names": "bread", "price": "2.99",
                 "price_scale": "per loaf", "in_stock": True}),
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
    """Class to interact with the database.
    """

    def __init__(self, type: DatabaseType, **kwargs):
        # Initialize the information for the database
        self.database_config = ":memory:" if type is DatabaseType.MEMORY else os.path.join(
            os.getcwd(), "mock.db")
        self.conn = None

    def init_database(self):
        """
        Initialize the database.
        """
        if not self.conn:
            raise SQLException("Connection is not initialized yet!")

        # Create the table for product information
        create_table_sql = """
            CREATE TABLE product (
                id CHAR(4) PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                names VARCHAR(55) NOT NULL,
                price DECIMAL(8,2),
                price_scale VARCHAR(10),
                in_stock INTEGER NOT NULL
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

        # Create a table for concerns/complaints
        create_table_sql = """
            CREATE TABLE concerns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id CHAR(10) NOT NULL, 
                phone_num CHAR(10) NOT NULL, 
                desc VARCHAR(1000) NOT NULL, 
                date_created DATETIME NOT NULL,
                status INT NOT NULL
            );
        """
        self.execute_update(create_table_sql)

    def connect(self):
        self.conn = sqlite3.connect(self.database_config)

    def close(self):
        """
        Close the connection to the database.
        """
        self.conn.close()
        self.conn = None

    def execute_query(self, query):
        """
        Execute a select query.

        Parameters
        ----------
        query: str
            The select query to execute.
        """
        return self.conn.cursor().execute(query)

    def execute_update(self, update_query):
        """
        Execute an update query.

        Parameters
        ----------
        update_query: str
            The update query to execute.
        """
        return self.conn.cursor().execute(update_query)

    def get_product(self, attr: str, value=None) -> list:
        """
        Method to get the first product that has a matching attribute value.

        This is equivalent to SELECT * WHERE attr = value.

        Parameters
        ----------

        attr: str
            The attribute name.

        value: any
            The value to match for specified attribute.


        Returns
        ----------

        product: dict
            The information about the product.
        """

        # Define a list
        products = []

        # Create a query statement
        query = f"SELECT * FROM product WHERE {attr} = '{value}'"

        # Execute the query
        cursor = self.execute_query(query)

        for row in cursor:
            # Create a dictionary representing a product
            product = OrderedDict(
                {
                    "id": row[0],
                    "name": row[1],
                    "names": row[2],
                    "price": row[3],
                    "price_scale": row[4],
                    "in_stock": True if row[5] > 0 else False
                }
            )

            # Add to the list
            products.append(product)

        return products

    def save_concern(self, session_id, phone_num, desc, status=False):
        """
        Method to save concern request into the database.

        Parameters
        ----------

        session_id: str
            The session id for the concern request.

        phone_num: str
            The phone number to contact the sender.

        desc: str
            The content of the request (maximum 1000 characters).

        status: boolean
            Whether the request is resolved.
        """
        insert_sql = f"INSERT INTO concerns (session_id, phone_num, desc, date_created, status) VALUES ('{session_id}', '{phone_num}', '{desc}', datetime('now'), {1 if status else 0});"
        self.execute_update(insert_sql)
    
def main():
    db = SQLiteDatabase(DatabaseType.MEMORY)
    db.connect()
    db.init_database()

    def print_result(cursor):
        print(tuple([desc[0] for desc in cursor.description])) # Print column names
        cursor.description
        for row in cursor:
            print(row)

    # Checking product info
    print_result(cursor=db.execute_query("SELECT * FROM product"))
    print("\n-------------------\n")
    # Checking complains info
    db.save_concern(session_id="ABC123DEF0", phone_num="1234567890", desc="Something is wrong", status = True)
    print_result(cursor=db.execute_query("SELECT * FROM concerns"))
    db.close()

# Use for testing
if __name__ == "__main__":
    main()
