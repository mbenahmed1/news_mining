import mysql.connector
from mysql.connector import errorcode
import confidential
import constants
import time
from datetime import datetime


class Database:
    """A class that represents a database connection.

    This class represents a database connection and manages all
    querries to the database.

    Attributes:
        csx:    The sql connection object.
    """

    def __init__(self):
        """Inits Database class"""

        self.connection_established = False
        self.cnx = self.connect()

    def __del__(self):
        """Closes connection after work is done."""
        print('Connection closed.')
        self.cnx.close()
        self.connection_established = False

    def connect(self):
        """Method that trys to establish a sql connection."""

        number_of_trys = 0
        connection_established = False

        # try connecting a few times and wait in between trys
        while number_of_trys < constants.SQLCONNECTIONTRYS and not connection_established:
            # trying to connect to the database
            try:
                number_of_trys += 1
                cnx = mysql.connector.connect(user=confidential.SQLUSERNAME,
                                              database=confidential.SQLDATABASENAME,
                                              host=confidential.SQLHOSTNAME,
                                              password=confidential.SQLPASSWORD,
                                              port=3306)
                connection_established = True
                print(
                    f'Connection to {confidential.SQLDATABASENAME}@{confidential.SQLHOSTNAME} established.')

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Identity could not be verified.")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist.")
                else:
                    print(err)
                    self.connection_established = False
                    print("Could not establish connection. Connection closed.")
                    cnx.close()

            else:
                # try again in some time
                if not connection_established:
                    time.sleep(constants.SQLCONNECTIONSLEEP)

        # return the connection and set connection to true
        self.connection_established = True
        return cnx


# testing implementation
db = Database()
time.sleep(5)
