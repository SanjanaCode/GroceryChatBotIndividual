
import sqlite3
import os
from enum import Enum, unique
from collections import OrderedDict

# Add data as needed
MOCK_PRODUCT_DATA = [
    OrderedDict({"id": "4011", "name": "banana", "names": "bananas", "price": "0.67", "price_scale": "per kg", "in_stock": True,
                 "calories": "89", "protein": "1.1 g", "carbs": "22.8 g", "sugar": "12.2 g", "fat": "0.3 g"}),
    OrderedDict({"id": "3022", "name": "strawberry", "names": "strawberries", "price": "3.99", "price_scale": "per box", "in_stock": True,
                 "calories": "11", "protein": "0.2 g", "carbs": "2.6 g", "sugar": "1.6 g", "fat": "0.1 g"}),
    OrderedDict({"id": "2011", "name": "apple", "names": "apples", "price": "0.49", "price_scale": "per kg", "in_stock": True,
                 "calories": "52", "protein": "0.3 g", "carbs": "13.8 g", "sugar": "10.4 g", "fat": "0.2 g"}),
    OrderedDict({"id": "5044", "name": "pear", "names": "pears", "price": "0.87", "price_scale": "per kg", "in_stock": False,
                 "calories": "101", "protein": "0.6 g", "carbs": "27.0 g", "sugar": "17.0 g", "fat": "0.3 g"}),
    OrderedDict({"id": "8088", "name": "bread", "names": "bread", "price": "2.99", "price_scale": "per loaf", "in_stock": True,
                 "calories": "82", "protein": "4.0 g", "carbs": "13.8 g", "sugar": "1.4 g", "fat": "1.1 g"}),
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
                in_stock INT NOT NULL,
                calories INT NOT NULL,
                protein VARCHAR(10) NOT NULL,
                carbs VARCHAR(10) NOT NULL,
                sugar VARCHAR(10) NOT NULL,
                fat VARCHAR(10) NOT NULL
            );
        """
        self.execute_update(create_table_sql)

        # Insert sample product information

        for prod in MOCK_PRODUCT_DATA:
            insert_sql = f"""
            INSERT INTO product VALUES ("{prod['id']}", "{prod['name']}", "{prod['names']}", {prod['price']}, "{prod['price_scale']}", {prod['in_stock']}, {prod['calories']}, "{prod['protein']}", "{prod['carbs']}", "{prod['sugar']}", "{prod['fat']}");
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

    # @Thuan @Paul @Quan
    # TODO: Once database is improved for use, we can have a more flexible way to retrieve data.
    # For now, only 1 attribute can be matched at a time.
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
                    "in_stock": True if row[5] > 0 else False,
                    "calories": row[6],
                    "protein": row[7],
                    "carbs": row[8],
                    "sugar": row[9],
                    "fat": row[10]
                }
            )

            # Add to the list
            products.append(product)

        return products


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
