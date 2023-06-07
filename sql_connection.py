import mysql.connector


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
    data = ((2,'Chandu'))
    #cursor.execute(query,data)
    print('DB updated successfully ! ')
    connection.commit()

    query = f'show columns from c361cohort.{tables[0]}'
    cursor.execute(query)
    columns = cursor.fetchall()
    connection.commit()

    cols = []
    for _ in columns:
        cols.append(_[0])

    for val in cols:
        print(val,end='\t')
    print()
    query = 'SELECT * FROM PYTHON_DB'
    cursor.execute(query)
    records = cursor.fetchall()
    
    for _ in records:
        print(_[0],_[1],sep='\t')

    
except Exception as e:
    print('Identified Error is : ',str(e))



