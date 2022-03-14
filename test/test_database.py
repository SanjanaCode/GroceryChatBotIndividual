import pytest
from app.database import MOCK_PRODUCT_DATA, SQLiteDatabase, DatabaseType
from app.products.product_info import ProductInfoHandler


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

    # Utility method to convert a single record (dict) into string
    @staticmethod
    def record_to_str(record: dict):
        if record:
            result = []
            for _, v in record.items():
                result.append(str(v))

            result[-1] = "1" if result[-1] else "0"

            return ",".join(result)
        else:
            return ""

    # Utility method to convert a set of metadata to string
    @staticmethod
    def metadata_to_str(schema):
        buffer = [] # A string buffer
        for table in schema:
            inner_buffer = []
            for metadata in table:
                inner_buffer.append(str(metadata))
            buffer.append(",".join(inner_buffer))
        return "\n".join(buffer)

@pytest.mark.database
class TestSQLiteDatabase:

    # This will run for all tests defined in this module
    @pytest.fixture()
    def db(self):
        # Set up
        db = SQLiteDatabase.instance()
        db.connect()
        db.init_database()

        # Pass the database entry point to tests
        # Test runs here
        yield db

        # Teadown
        # Close the connection
        db.close()

    # Test database initialization
    def test_init_database(self, db: SQLiteDatabase):
        # Get the cursor
        cursor = db.execute_query("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;")
        
        # Parse the result set to string
        result_str = ConvertUtilities.metadata_to_str(cursor)
        expected_str = "concerns\nproduct\nsqlite_sequence"

        # Checking
        assert result_str == expected_str

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


@pytest.mark.database
class TestSQLiteOnHandler:

    @pytest.fixture()
    def mini_bot(self):
        # Set up
        mini_bot = ProductInfoHandler()

        # Run tests
        yield mini_bot

        # Clean up
        mini_bot.dispose()

    # Test get_product method on ProductInfoHandler
    def test_get_product(self, mini_bot: ProductInfoHandler):
        # Make a sample request for record with id 4011
        list_prod = mini_bot.db.get_product("id", "4011")

        # Extract product
        return_prod = list_prod[0] if len(list_prod) > 0 else None

        # Get the data from MOCK_PRODUCT_DATA
        expect_prod = None
        for item in MOCK_PRODUCT_DATA:
            if item["id"] == "4011":
                expect_prod = item
                break

        # Check on id so there is either none or 1 product in list
        assert ConvertUtilities.record_to_str(
            return_prod) == ConvertUtilities.record_to_str(expect_prod)
