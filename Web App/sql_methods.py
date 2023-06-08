import mysql.connector
try:
    def start_connection():
        connection = mysql.connector.connect(host='localhost',
                                            database='c361cohort',
                                            user='root',
                                            password='root')
        
        return connection
    
    def fetch_records(connection):
        







except Exception as e:
    print('Error : ',str(e))   

