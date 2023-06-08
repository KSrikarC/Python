import mysql.connector
try:
    def start_connection():
        connection = mysql.connector.connect(host='localhost',
                                            database='c361cohort',
                                            user='root',
                                            password='root')
        
        return connection
    
    def fetch_records(connection):
        cursor = connection.cursor()                             
        query = 'SELECT * FROM PYTHON_DB'
        cursor.execute(query)
        records = cursor.fetchall()    
        return records







except Exception as e:
    print('Error : ',str(e))   

