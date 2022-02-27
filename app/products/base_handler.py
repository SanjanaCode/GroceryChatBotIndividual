from abc import abstractmethod
import os
from app.products.database import DatabaseType, SQLiteDatabase


class BaseHandler:
    """
    The base class for Handlers.

    Attributes
    ----------
    runtime_mode : str
        The environment that the bot is running in (i.e. DEV or PRODUCTION).

    db: SQLiteDatabase
        The entry point to interact with SQLite database.

    Methods
    -------
    create_match_paterns(message: str)
        Initialize regex patterns.

    handle(message: str)
        Handle the message and return the proper response.

    parse(message: str):
        Parse the message to extract keywords.

    dispose():
        Clean up resources used by this minibot.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the ProductHandler object.
        """
        # Set the operation mode (i.e. DEV or PRODUCTION)
        self.runtime_mode = os.getenv("PYTHON_ENV", "DEV")

        # Create pattern matches
        self.create_match_paterns()

        # Initialize a mock database if development environment
        if self.runtime_mode == "DEV":
            self.db = SQLiteDatabase(DatabaseType.MEMORY)
            self.db.connect()  # Start a connection
            self.db.init_database()  # Initialize the database
        else:
            self.db = None

    def dispose(self):
        """
        Call this methods to release any resources with this minibot (i.e. database connection).
        """
        if self.db:
            self.db.close()

    @abstractmethod
    def create_match_paterns(self) -> None:
        """
        This method is called when the class is initialized.
        """
        pass

    @abstractmethod
    def handle(self, message: str) -> str:
        """
        The entry point of the mini-bot.

        Main bot will call this method to pass in the message to process.

        Parameters
        ----------

        message: str
            The message that the user sends to the bot.


        Returns
        ----------
        response: str
            The response string to the request message
        """
        pass

    @abstractmethod
    def parse(self, message: str) -> dict:
        """
        Parse the message into keywords for the handler.

        Parameters
        ----------

        message: str
            The message that the user sends to the bot.


        Returns
        ----------
        parse_result: dict
            The arguments to handler as a dictionary.
        """
        pass
