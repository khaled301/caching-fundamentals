# declares he mysql driver for python to communicate with MySQL sever
import mysql.connector

# loads configuration
import config

class MysqlGateway:
    def __init__(self):
        try: 
            db_con = mysql.connector.connect(
                host=config.mysql_host,
                user=config.mysql_user,
                password=config.mysql_password,
                database=config.mysql_database,
            )
            
            """_summary_
                Creates a cursor that will execute the SQL statement
                The dictionary = True value, instructs Python to return the SQL result as key-value pairs (dictionary). 
                The dictionary format allows us to format the response to JSON format when displaying the data.
            """
            self.db_cursor = db_con.cursor(dictionary=True)
            
        except Exception as e:
            print(e)
            self.db_cursor = None
            
    def db_cursor_close(self):
        if self.db_cursor:
            self.db_cursor.close()
            self.db_cursor = None

    def query_mysql(self, query_string):
        if self.db_cursor:
            try:
                # Execute the SQL statement against the query
                self.db_cursor.execute(query_string)
                
                # Fetch and return the results
                return self.db_cursor.fetchall()
            except Exception as e:
                print(e)
                return None
        else:
            print(f"Invalid db_cursor: {self.db_cursor}")
            return None