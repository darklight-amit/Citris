"""
It will dump all the tables data in excel workbook
"""

import psycopg2
import openpyxl

from xlsxwriter.workbook import Workbook


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


def writeWorkSheet(workbook, database_name, table_name, cursor):
    worksheet_name =""
    if database_name.endswith('staging'):
        worksheet_name = ('S'+"."+ table_name)[0:31]
    if database_name.endswith('report'):
        worksheet_name = ('R'+"."+ table_name)[0:31]
    if database_name.endswith('wordpress'):
        worksheet_name = ('W'+"."+ table_name)[0:31]
    worksheet = workbook.add_worksheet(worksheet_name)
    cursor.execute(f"SELECT * FROM {database_name}.{table_name} limit 100")
    cols = [i[0] for i in cursor.description]
    for c, col in enumerate(cols):
        worksheet.write(0, c, col)

    results  = cursor.fetchall()
    for r, row in enumerate(results):
        for c, col in enumerate(row):
            worksheet.write(r+1, c, str(col))
    

if __name__ == "__main__":

    conn = get_database_connection()
    cursor = conn.cursor()

    query  = "SELECT * FROM pg_catalog.pg_tables;;"
    cursor.execute(query)
    table_info = []

    for info in cursor.fetchall():
        temp =[]
        if info[0].startswith('citris'):
            temp.append(info[0])
            temp.append(info[1])
            table_info.append(temp)
    
    workbook = Workbook('citrisDevData.xlsx')  
    for data in table_info:
        print(f"{data[0]}.{data[1]} table reading....")
        writeWorkSheet(workbook, data[0], data[1], cursor)
        print(f"{data[1]} data written successfully")
    cursor.close()
    conn.close()
    workbook.close()
