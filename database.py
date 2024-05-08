#PACKAGES
import mysql.connector
from mysql.connector import Error

#FILES
import sec_api_interaction



def main():


    def try_connect(db:str = '') -> mysql.connector.connection_cext.CMySQLConnection:
        """

        """
        if db == '':
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='99LA180025s!'
                )

            
                print(f'User: {connection.user} has successfully connected to the MySQL server hosted at {connection._host}')
                
                return connection
        
            except Exception as e:
                print('Error could not connect to MySQL Server')
                print(str(e))


            
        else:
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='99LA180025s!',
                    database=db
                )

                print(f'User: {connection.user} has successfully connected to the MySQL server hosted at {connection._host} to access the database: {connection._database}')
            
                return connection


            except Error as e:
                if e.errno == 1049:
                    print(f"Database, '{db}', does not exist.")

                else:
                    print(f"Could not connect to database: {db}")
                    print("Error listed below: ")
                    print(str(e))

        
    def create_db(db:str) -> None:
        """
        """
        
        try:
            cursor.execute(f"CREATE DATABASE {db}")
        
        except Exception as e:

            print(str(e))

    def create_tbl(tbl_name: str, col_name_x_col_type: dict) -> None:
        """
        """
        
        sql_string = f"""CREATE TABLE IF NOT EXITSTS {tbl_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    """
                           
        for key, value in col_name_x_col_type.items():
            sql_string = sql_string + key + " " + value + ", \n"

        sql_string = sql_string + ")"


        try:
            cursor.execute(sql_string)
        
        except Exception as e:

            print(str(e))

    #Establish connection to a desired database / or establish a general connection if no argument is passed
    connection = try_connect()
    
    if connection:

        #Get a cursor to execute SQL Commands
        cursor = connection.cursor()





        #close connections and cursor
        cursor.close()
        connection.close()

    
main()