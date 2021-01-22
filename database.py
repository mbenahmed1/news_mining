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
        self.is_connected = False
        self.cnx = self.connect()
        self.connection_established = datetime.now()
        self.connection_lost = datetime.now()

    def __del__(self):
        """Closes connection if database object gets deleted."""
        self.disconnect()

    def disconnect(self):
        """Closes connection to the database."""
        if self.is_connected:
            print('Connection closed.')
            self.connection_lost = datetime.now()
            self.is_connected = False
            try:
                self.cnx.close()
            except:
                pass
        else:
            print('Connection is closed already.')

    def __str__(self) -> str:
        """Method that prints the server status"""
        if self.is_connected:
            return f'[Connected]: to {confidential.SQLHOSTNAME} since {self.connection_established}.'
        else:
            return f'[Disconnected]: since {self.connection_lost}.'

    def connect(self):
        """Method that trys to establish a sql connection."""

        if not self.is_connected:
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
                                                  port=confidential.SQLPORT)
                    connection_established = datetime.now()
                    self.is_connected = True
                    print(
                        f'Connection to {confidential.SQLDATABASENAME}@{confidential.SQLHOSTNAME} established.')

                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Identity could not be verified.")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist.")
                    else:
                        print(err)
                        self.is_connected = False
                        print("Could not establish connection. Connection closed.")
                        cnx.close()

                else:
                    # try again in some time
                    if not connection_established:
                        time.sleep(constants.SQLCONNECTIONSLEEP)

            # return the connection and set connection to true
            return cnx
        else:
            print('Already connected.')
            return False


# testing implementation
db = Database()


time.sleep(5)
db.disconnect()
