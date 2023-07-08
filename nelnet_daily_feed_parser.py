"""
It will parse the NelNet daily feed and insert records in
nelnet_daily_feed table under citrisfinancial_report database
"""

import psycopg2

def get_database_connection():
    """
    It rerutns connection string of the citris dev database
    """
    return psycopg2.connect(
        host='citris-app-aurora-pg-dev.cluster-cf5khejaiz0c.us-west-1.rds.amazonaws.com',
        database='citrisappdb',
        user='appdev_admin',
        password='Nhguh67gdT6gtakA3ncs7JK', 
        port='5432'
    )

def nelnet_file_to_table(conn, cursor):
    """
    it will read nelnet daily feed file and return dataframe
    """
    skip_row = True
    with open("data/V_Data_Feed_Daily_CitrisTRAIN", 'r') as f:
        for data in f.readlines():
            fields = data.strip("\n").split("|")
            formatted_field = ['NULL'  if data=="" else data for data in fields ]
            value = "', '".join(formatted_field)
            if skip_row:
                skip_row = False
                continue
            else:
                
                insert_into_nelnet_table(conn, cursor, value, fields[0], fields[1])
                

def insert_into_nelnet_table(conn, cursor, value, loan_number, externalref_id):
    """
    It will insert records in table one by one
    """
    
    # build insert query

    query = "INSERT INTO citrisfinancial_report.nelnet_daily_feed VALUES ('" \
            + value + "');"
    
    query = query.replace("'NULL'", "NULL")
    
    
    
    try:
        cursor.execute(query)
        print("record inserted successfully for loan number - {} and external reference - {}".format(loan_number, externalref_id))
        
    except (Exception, psycopg2.Error) as error:
        cursor.execute("ROLLBACK")
        print(query)
        print("Error {} while executing the query, hence skipping record for loan number - {} and external reference - {}".format(error, loan_number, externalref_id))




if __name__ == "__main__":
    conn = get_database_connection()
    cursor = conn.cursor()
    nelnet_file_to_table(conn, cursor)
    conn.commit()
    cursor.close()
    conn.close()
