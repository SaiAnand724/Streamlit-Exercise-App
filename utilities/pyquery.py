"""
Working with MySQL Workbench
- Set up SQL server with credentials

Either command line should work:
pip3 install mysql-connector-python
pip3 install mysql-connector-python-rf
"""
# Import mysql-connector module 
import mysql.connector

# Import Utilities module from util.py
from utils import Utilities as sql_utils

# Import json module for storing and fetching information
import json

# Create a class 'sqlpy' that inherits the properties of the 'Utilities' class
class sqlpy(sql_utils):
    def __init__(self):
        super().__init__()
        
    # Function to connect to database
    def connect_to_db():
        global mycursor
        global mydb
        # Connecting to/Setting up database
        """
        Basic Doc Source: https://www.psycopg.org/docs/module.html#psycopg2.connect
        MySQL Doc Source: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
        Create a new database session and return a new connection object.
        The basic connection parameters are:

        dbname – the database name (database is a deprecated alias)

        user – user name used to authenticate

        password – password used to authenticate

        host – database host address (defaults to UNIX socket if not provided)

        port – connection port number (defaults to 5432 if not provided)
        """

        """
        mydb = mysql.connector.connect(
            host = "localhost",
            # Username for connection - default (root)
            user = "root", 
            # Password for connection - User generated password
            password = "User-Password",
            # Create a database first, then fill field with info
            # Field to determine which database to start/work with
            database = "Any_Database"
        )
        """
        mydb = mysql.connector.connect(
            host = "localhost",
            # Username for connection - default (root)
            # user = "root"
            user = "saiSQL", 
            # Password for connection - User generated password
            # passwd = "User-Password"
            password = "",
            # Create a database first, then fill field with info
            # Field to determine which database to start/work with
            database = "python_test_db"
        )

        print("Database connection point: ", mydb) # - Lets you know the connection works
        # Output should look like: <mysql.connector.connection.MySQLConnection object at 0x00000**********0>

        # Initialize cursor
        """
        Doc Source: https://www.psycopg.org/docs/cursor.html
        Cursors are created by the connection. cursor() method: 
            they are bound to the connection for the entire lifetime and all the commands 
            are executed in the context of the database session wrapped by the connection.

        """
        # Create cursor object using the mydb connection
        mycursor = mydb.cursor()
    def use_database():
        global mycursor
        global database
        # Use MySQL database in python
        use_db_form = sql_utils.mysql_use_db(database)
        mycursor.execute(use_db_form)

    def create_table():
        global mycursor
        # Create MySQL table in python
        columns_tb = ["stud_id INTEGER(10) PRIMARY KEY", "name VARCHAR(50)", "age INTEGER(10)", "gender VARCHAR(1)"]
        create_tb_form = sql_utils.mysql_create_tb(table_name1, columns_tb)
        mycursor.execute(create_tb_form)
        
    def populate_tb():
        global mycursor
        # Add values to MySQL table in python
        values_arr = (1, "He-mothy", 18, "M")
        addto_tb_form = sql_utils.mysql_addto_tb(table_name1, values_arr)
        mycursor.execute(addto_tb_form) # needs to get commented once it is run, should fix in util.py later
