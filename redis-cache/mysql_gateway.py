# declares he mysql driver for python to communicate with MySQL sever
import mysql.connector

# loads configuration
import config

class MysqlGateway:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=config.mysql_host,
                user=config.mysql_user,
                password=config.mysql_password,
                database=config.mysql_database
            )

            """_summary_
                Creates a cursor that will execute the SQL statement
                The dictionary = True value, instructs Python to return the SQL result as key-value pairs (dictionary). 
                The dictionary format allows us to format the response to JSON format when displaying the data.
            """
            self.cursor = self.connection.cursor(dictionary=True)
        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None
            self.cursor = None

    def query_mysql(self, query_string):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
            
        if self.connection and self.connection.is_connected() and self.cursor:
            try:
                # Execute the SQL statement against the query
                self.cursor.execute(query_string)
                
                # Fetch and return the results
                return self.cursor.fetchall()
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print(f"Connection to MySQL failed: {self.cursor}")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()