import psycopg2
import csv
import boto3
import io
from datetime import datetime, timedelta

def lambda_handler(event, context):
    
	# Specify your AWS S3 bucket details
    s3_bucket_name = 'data-enrollment-payment'
    s3_folder_name = 'enrollments'

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
    query = """ select * FROM citrisfinancial_report.highline_enrollment  where event = 'enrollments' 
    --and status = 'complete'  
    """

    try:
        # Execute the query with the provided condition value
        cursor.execute(query)
        
        # Fetch all the rows that satisfy the condition
        rows = cursor.fetchall()
        enrollment_complete = []
        unenroll_stale_file = []
        unenroll_complete = []

        print(rows)
    
        if rows:
            current_date = datetime.now()
            print("Rows found with event_status = 'complete'")
            for row in rows:
                id = row[0]
                topic = row[1]
                event = row[2]  # Assuming event_status is in the 4th column (index 3)
                occured_at = row[3]
                enrollment_id = row[4]
                user_id = row[5] 
                event_status = row[6]
                #print(event_status)
                #print(current_date - load_timestamp)
                print(current_date)
                print(occured_at)
                print(current_date - occured_at > timedelta(days=10))
            
                if event_status == 'complete' and (current_date - occured_at) < timedelta(days=10):
                    print(row)
                    print("enrollment file created")
                    enrollment_complete.append([id, topic, event, occured_at, enrollment_id, user_id, event_status])
                elif event_status == 'complete' and (current_date - occured_at) > timedelta(days=10):
                    print("stale file sent to unenroll")
                    unenroll_stale_file.append([id, topic, event, occured_at, enrollment_id, user_id, event_status])
                else:
                    enrollment_id = row[1]  # Assuming enrollment_id is in the 2nd column (index 1)
                    print(f"Sending notification for ID: {enrollment_id}")
                    unenroll_complete.append([id, topic, event, occured_at, enrollment_id, user_id, event_status])
        else:
            print("No rows found with the provided condition.")
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        if enrollment_complete:
        
            # Specify the filename for the CSV file
            csv_filename_enroll = f'enrollment_complete_{timestamp}.csv'
        
            # Specify the header row
            header = ['id', 'topic', 'event', 'occured_at', 'enrollment_id', 'user_id', 'event_status']
        
            # Create a file-like object in memory
            csv_file_enroll = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file_enroll)
            writer.writerow(header)
            writer.writerows(enrollment_complete)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows  matching the condition written to {csv_filename_enroll}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename_enroll}'
            
            #with open(csv_filename, 'fb', newline='') as csvfile:
            #s3.upload_file(csv_fileobj, s3_bucket_name, s3_filename)
            #s3.upload_fileobj(csv_file.getvalue().encode(), s3_bucket_name, s3_filename)
            s3.put_object(Body=csv_file_enroll.getvalue(), Bucket=s3_bucket_name, Key=s3_filename)
            print(f"CSV file uploaded to S3 bucket: {s3_bucket_name}/{s3_filename}")
            
        if unenroll_stale_file:
        
            # Specify the filename for the CSV file
            csv_filename_stale = f'unenroll_stale_{timestamp}.csv'
        
            # Specify the header row
            header = ['id', 'topic', 'event', 'occured_at', 'enrollment_id', 'user_id', 'event_status']
        
            # Create a file-like object in memory
            csv_file = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(unenroll_stale_file)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows not matching the condition written to {csv_filename_stale}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename_stale}'
            
            #with open(csv_filename, 'fb', newline='') as csvfile:
            #s3.upload_file(csv_fileobj, s3_bucket_name, s3_filename)
            #s3.upload_fileobj(csv_file.getvalue().encode(), s3_bucket_name, s3_filename)
            s3.put_object(Body=csv_file.getvalue(), Bucket=s3_bucket_name, Key=s3_filename)
            print(f"CSV file uploaded to S3 bucket: {s3_bucket_name}/{s3_filename}") 
            
        if unenroll_complete:
        
            # Specify the filename for the CSV file
            csv_filename_unenroll = f'unenroll_complete_{timestamp}.csv'
        
            # Specify the header row
            header = ['id', 'topic', 'event', 'occured_at', 'enrollment_id', 'user_id', 'event_status']
        
            # Create a file-like object in memory
            csv_file = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(unenroll_complete)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows not matching the condition written to {csv_filename_unenroll}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename_unenroll}'
            
            #with open(csv_filename, 'fb', newline='') as csvfile:
            #s3.upload_file(csv_fileobj, s3_bucket_name, s3_filename)
            #s3.upload_fileobj(csv_file.getvalue().encode(), s3_bucket_name, s3_filename)
            s3.put_object(Body=csv_file.getvalue(), Bucket=s3_bucket_name, Key=s3_filename)
            print(f"CSV file uploaded to S3 bucket: {s3_bucket_name}/{s3_filename}")            
        else:
            print("No rows found not matching the condition.")            
            
    except (Exception, psycopg2.Error) as error:
        print("Error while executing the query:", error)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()``
