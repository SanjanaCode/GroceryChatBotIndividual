import pytest
from app.products.database import MOCK_PRODUCT_DATA, SQLiteDatabase, DatabaseType
from app.products.product_info import StoreProductHandler


class ConvertUtilities:
    # Utility method to convert result set into string
    @staticmethod
    def query_result_to_str(cursor):
        result = []
        for row in cursor:
            row_data = []
            for attr in row:
                row_data.append(str(attr))

            # Convert last attr
            row_data[-1] = "1" if row_data[-1] else "0"
            result.append(",".join(row_data))

        return "\n".join(result)

    # Utility method to convert result (pre-defined) set into string
    @staticmethod
    def all_data_to_str():
        all_data = []
        for row in MOCK_PRODUCT_DATA:
            row_data = []
            for _, v in row.items():
                row_data.append(str(v))
            # Convert last attr
            row_data[-1] = "1" if row_data[-1] else "0"
            all_data.append(",".join(row_data))

        return "\n".join(all_data)


@pytest.mark.database
class TestSQLiteDatabase:

    # This will run for all tests defined in this module
    @pytest.fixture()
    def db(self):
        # Set up
        db = SQLiteDatabase(DatabaseType.MEMORY)
        db.connect()
        db.init_database()

        # Pass the database entry point to tests
        # Test runs here
        yield db

        # Teadown
        # Close the connection
        db.close()

    # Test select all with databse in memory
    def test_get_all_products_memory(self, db: SQLiteDatabase):
        # Get the cursor
        cursor = db.execute_query("SELECT * FROM product;")

        # Parse the result set to str
        result_str = ConvertUtilities.query_result_to_str(cursor)
        expected_str = ConvertUtilities.all_data_to_str()

        # Checking
        assert result_str == expected_str

    # Test select all with database as a data file
    def test_get_all_products_datafile(self, db: SQLiteDatabase):
        # Get the cursor
        cursor = db.execute_query("SELECT * FROM product;")

        # Parse the result set to str
        result_str = ConvertUtilities.query_result_to_str(cursor)
        expected_str = ConvertUtilities.all_data_to_str()

        # Checking
        assert result_str == expected_str
