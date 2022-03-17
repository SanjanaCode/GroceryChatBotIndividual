import pytest
from app.database import MOCK_PRODUCT_DATA, Database, DatabaseType
from app.products.product_info import ProductInfoHandler
from datetime import datetime, timezone

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
class TestDatabase:

    # This will run for all tests defined in this module
    # Scope: function (run all test functions)
    @pytest.fixture()
    def db(self):
        # Set up
        db = Database.instance()
        db.connect()
        db.init_database()

        # Pass the database entry point to tests
        # Test runs here
        yield db

        # Teadown
        # Close the connection
        db.close()

    # Test if singleton pattern is correctly implemented
    # The object db is default to be in memory.
    def test_get_instance(self, db: Database):
        assert db == Database.instance()

    # Test database initialization
    def test_init_database(self, db: Database):
        # Get the cursor
        cursor = db.execute_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        
        # Parse the result set to string
        result_str = ConvertUtilities.metadata_to_str(cursor)
        expected_str = "concerns\nproduct\nsqlite_sequence"

        # Checking
        assert result_str == expected_str

    # Test select all with databse in memory
    def test_get_all_products_memory(self, db: Database):
        # Get the cursor
        cursor = db.execute_query("SELECT * FROM product;")

        # Parse the result set to str
        result_str = ConvertUtilities.query_result_to_str(cursor)
        expected_str = ConvertUtilities.all_data_to_str()

        # Checking
        assert result_str == expected_str

    # Test select all with database as a data file
    def test_get_all_products_datafile(self, db: Database):
        # Get the cursor
        cursor = db.execute_query("SELECT * FROM product;")

        # Parse the result set to str
        result_str = ConvertUtilities.query_result_to_str(cursor)
        expected_str = ConvertUtilities.all_data_to_str()

        # Checking
        assert result_str == expected_str

    # Test select a product base on id
    def test_get_product(self, db: Database):
        # Make a sample request for record with id 4011
        list_prod = db.get_product("id", "4011")

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
 
    # Test save a complain into the database
    def test_save_concern(self, db: Database):
        # Get the information
        current_time = datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds")
        current_time = current_time[0: current_time.index("+")] # Remove timezone offset

        # Call insert into the database
        db.save_concern(session_id="ABC123DEF0", phone_num="1234567890", desc="Something is wrong", datetime= current_time ,status = True)

        # Get the number of row
        cursor = db.execute_query("SELECT COUNT(*) FROM concerns;")
        num_of_row = cursor.fetchone()[0] # Fetch a row and extract its first field

        assert num_of_row == 1  # Check the number of rows

        # Select the first concern from the database
        cursor = db.execute_query("SELECT * FROM concerns;")

        result_str = ConvertUtilities.query_result_to_str(cursor=cursor)
        expected_str = f"1,ABC123DEF0,1234567890,Something is wrong,{current_time},1"

        assert result_str == expected_str