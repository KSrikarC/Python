from Custom_Func import cls
import mysql.connector
cls()

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='c361cohort',
                                        user='root',
                                        password='root')

    if connection:
        print('Connected Successfully..!!!\n')

    cursor = connection.cursor()      

    create_query = 'CREATE TABLE IF NOT EXISTS PYTHON_DB (id INT, name VARCHAR(20))'  
    cursor.execute(create_query)
    connection.commit()

    query = "SHOW TABLES LIKE 'python_db' "
    cursor.execute(query)
    tables = cursor.fetchone()
    print(f'Created table : {(tables[0])}\n')
    connection.commit()

    query = """INSERT INTO PYTHON_DB(id,name) VALUES(%s,%s)"""
    data = (1,'Srikar')
    cursor.execute(query,data)
    print('DB updated successfully ! ')
    connection.commit()


except Exception as e:
    print(str(e))



