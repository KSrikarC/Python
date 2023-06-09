def extract_csv(file_name):
    import csv
    insert_data=[]
    with open(file_name,'r') as file:
        records = csv.reader(file)
        for line in records:
            #print(line)
            insert_data.append((line[0],line[1],line[2]))
    file.close()   
    print(insert_data) 
    return insert_data
     


extract_csv('flights.csv')    



 



    