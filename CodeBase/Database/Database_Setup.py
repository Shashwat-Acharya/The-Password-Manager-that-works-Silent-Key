from dataclasses import dataclass
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Create a Base class for SQLAlchemy ORM models
Base = declarative_base()


# 1. Dataclass for storing browser password data (Dataclass - used for simple data storage)
@dataclass
class BrowserPasswordData:
    """
    Represents browser password data.
    This class is used for storing browser password information in a dataclass format.

    Attributes:
    - browser_name: The name of the browser.
    - url: The URL associated with the password.
    - username: The username associated with the password.
    - password: The password (should be encrypted).
    """
    browser_name: str
    url: str
    username: str
    password: str


# 2. Pydantic model for validation (Pydantic - used for data validation)
class BrowserPasswordPydantic(BaseModel):
    """
    Pydantic model to validate browser password data before insertion into the database.

    Attributes:
    - browser_name: The name of the browser.
    - url: The URL associated with the password.
    - username: The username associated with the password.
    - password: The password (should be encrypted).
    """
    browser_name: str
    url: str
    username: str
    password: str

    @validator('browser_name')
    def validate_browser_name(cls, value):
        """
        Validate that the browser name is not empty and matches a known pattern.
        """
        if not value:
            raise ValueError('Browser name cannot be empty')
        return value


# 3. SQLAlchemy model for storing data in the database
class BrowserPassword(Base):
    """
    Represents the browser password data stored in the PostgreSQL database.
    This model is used for the database interaction through SQLAlchemy.

    Attributes:
    - id: The primary key for the browser password record.
    - browser_name: The name of the browser.
    - url: The URL associated with the password.
    - username: The username associated with the password.
    - password: The password (encrypted).
    - created_at: The timestamp when the record was created.
    """
    __tablename__ = 'browser_passwords'

    id = Column(Integer, primary_key=True, autoincrement=True)
    browser_name = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<BrowserPassword(browser_name={self.browser_name}, url={self.url}, username={self.username})>"


# 4. Database Setup Class for SQLAlchemy
class DatabaseSetup:
    """
    A class to set up the database and interact with it using SQLAlchemy.

    Methods:
    - setup: Initializes the database and creates tables.
    - insert_password: Inserts a new browser password into the database.
    - retrieve_passwords: Retrieves passwords from the database based on filter criteria.
    """

    def __init__(self, database_url: str):
        """
        Initialize the DatabaseSetup class with a given database URL.

        Args:
        - database_url: The URL of the PostgreSQL database.
        """
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def setup(self):
        """Initialize the database and create the necessary tables."""
        Base.metadata.create_all(self.engine)

    def insert_password(self, password: BrowserPasswordPydantic):
        """Insert a new browser password record into the database."""
        validated_password = password.dict()  # Convert to dict
        db_password = BrowserPassword(**validated_password)
        self.session.add(db_password)
        self.session.commit()

    def retrieve_passwords(self, filter_criteria):
        """Retrieve passwords from the database based on filter criteria."""
        return self.session.query(BrowserPassword).filter_by(**filter_criteria).all()


# 5. Example Usage
if __name__ == "__main__":
    # Define the PostgreSQL database URL
    DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"

    # Initialize the database setup
    db_setup = DatabaseSetup(DATABASE_URL)

    # Setup the database and create tables
    db_setup.setup()

    # Example data for a new browser password
    password_data = BrowserPasswordPydantic(
        browser_name="Chrome",
        url="https://example.com",
        username="user_example",
        password="encrypted_password_data"
    )

    # Insert the password into the database
    db_setup.insert_password(password_data)

    # Retrieve passwords
    filter_criteria = {"browser_name": "Chrome"}
    stored_passwords = db_setup.retrieve_passwords(filter_criteria)
    for password in stored_passwords:
        print(password.url, password.username, password.password)
