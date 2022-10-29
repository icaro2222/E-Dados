
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
    
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(query):
    connection = None

    connection = mysql.connector.connect(
        host="localhost",
        user="icaro",
        passwd='tatakae',
        database='e_dados'
    )
    print("MySQL Database connection successful")
    # Connect to the Database
        
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    
    return result



        # server = 'myserver' 
        # database = 'e_dados' 
        # username = 'icaro' 
        # password = 'tatakae'  
        # cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        # cursor = cnxn.cursor()
        # # select 26 rows from SQL table to insert in dataframe.
        # query = "SELECT NO_MUNICIPIO_RESIDENCIA FROM enem LIMIT 100;"
        # df = pd.read_sql(query, cnxn)
        # print(df.head(26))