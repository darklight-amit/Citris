

import psycopg2
import csv
import boto3
import io
from datetime import datetime, timedelta

def lambda_handler(event, context):

	# Specify your AWS S3 bucket details
    s3_bucket_name = 'data-enrollment-payment'
    s3_folder_name = 'payments'
    
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host='citris-app-aurora-pg-dev.cluster-cf5khejaiz0c.us-west-1.rds.amazonaws.com',
        database='citrisappdb',
        user='appdev_admin',
        password='Nhguh67gdT6gtakA3ncs7JK',
        port='5432'
        )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    #condition_value = 'enrollments'

    # Build the SQL query
    query  = """ select pp.*,bo.*,
    CASE WHEN pp.payment_amount = bo.payment_amount THEN '1' ELSE '0' END AS plp_ind 
    from citrisfinancial_report.plp_payments pp
    inner join
    citrisfinancial_report.highline_bill_object bo
    on pp.id = bo.id
    and pp.enrollment_id = bo.enrollment_id
    and pp.month = bo.month

      """
      


    try:
        # Execute the query with the provided condition value
        cursor.execute(query)

        # Fetch all the rows that satisfy the condition
        rows = cursor.fetchall()
        
        partial_payment = []
        settled_payment = []

        if rows:
            current_date = datetime.now()
            print("Rows found with payment details")
            for row in rows:
                payment_event = row[1]
                product_id = row[2]
                amount_due = row[4]  # Assuming event_status is in the 4th column (index 3)
                enrollment_id = row[11]
                payment_amount = row[14]
                plp_ind = row[17]
              
                #print(event_status)
                #print(current_date - load_timestamp)
                print(plp_ind)
                print(payment_amount)
                print(payment_event)
                        
                if int(plp_ind) == 1:
                    print("Settlement")
                    print(row)
                    settled_payment.append([payment_event, product_id, amount_due, enrollment_id, payment_amount, plp_ind])
             
              
                else:
                
                 #enrollment_id = row[1]  # Assuming enrollment_id is in the 2nd column (index 1)
                     print("plp partial payments")
                     print(row)
                     partial_payment.append([payment_event, product_id, amount_due, enrollment_id, payment_amount, plp_ind])
        else:
            print("No rows found with the provided condition.")
            
                # Get the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        if partial_payment:
        
            # Specify the filename for the CSV file
            csv_filename_pp = f'partial_payment_{timestamp}.csv'
        
            # Specify the header row
            header = ['event', 'product_id', 'amount_due', 'enrollment_id', 'payment_amount', 'plp_ind']
        
            # Create a file-like object in memory
            csv_file_pp = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file_pp)
            writer.writerow(header)
            writer.writerows(partial_payment)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows  matching the condition written to {csv_filename_pp}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename_pp}'
            
            #with open(csv_filename, 'fb', newline='') as csvfile:
            #s3.upload_file(csv_fileobj, s3_bucket_name, s3_filename)
            #s3.upload_fileobj(csv_file.getvalue().encode(), s3_bucket_name, s3_filename)
            s3.put_object(Body=csv_file_pp.getvalue(), Bucket=s3_bucket_name, Key=s3_filename)
            print(f"partial payment csv file uploaded to S3 bucket: {s3_bucket_name}/{s3_filename}")
            
        if settled_payment:
        
            # Specify the filename for the CSV file
            csv_filename_sp = f'settled_payment_{timestamp}.csv'
        
            # Specify the header row
            header = ['event', 'product_id', 'amount_due', 'enrollment_id', 'payment_amount', 'plp_ind']
        
            # Create a file-like object in memory
            csv_file_sp = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file_sp)
            writer.writerow(header)
            writer.writerows(settled_payment)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows  matching the condition written to {csv_filename_sp}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename_sp}'
            
            #with open(csv_filename, 'fb', newline='') as csvfile:
            #s3.upload_file(csv_fileobj, s3_bucket_name, s3_filename)
            #s3.upload_fileobj(csv_file.getvalue().encode(), s3_bucket_name, s3_filename)
            s3.put_object(Body=csv_file_sp.getvalue(), Bucket=s3_bucket_name, Key=s3_filename)
            print(f"Settled file uploaded to S3 bucket: {s3_bucket_name}/{s3_filename}")
            
        else:
            print("No rows found not matching the condition.")

    except (Exception, psycopg2.Error) as error:
        print("Error while executing the query:", error)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

