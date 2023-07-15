
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
    query  = """ 	with ctehl as (select *,ROW_NUMBER() OVER (PARTITION BY enrollment_id ORDER BY load_timestamp desc) AS row_number from
					(SELECT event, 
		event_json::json->>'event' as payment_event,
		event_json::json->'payload'->>'product_id' as product_id,
		event_json::json->'payload'->>'bill_payment_id' as bill_payment_id,	
		event_json::json->'payload'->>'amount_due' as amount_due,
		event_json::json->'payload'->>'amount_paid' as amount_paid,
		event_json::json->'payload'->>'user_id' as user_id,
		event_json::json->>'occurred_at' as occurred_at,
		load_timestamp,
		event_json::json->'payload'->>'enrollment_id' as enrollment_id
		FROM citrisfinancial_report.hl_events_candidate  where event in ('bills', 'bill_payments')
					--   and event = 'completed'
		--and event_json::json->'payload'->>'enrollment_id' = 'KDRD2886OINP')
		) abc where  payment_event = 'completed'
					)
	
	select hevent.*, pday.*, bobj.id, bobj.month as month, bobj.months_left as months_left, 
		bobj.payment_number as payment_number
	FROM (select * from ctehl where row_number = 1 )  hevent
	inner join 
	citrisfinancial_report.highline_paydays pday on 
	(hevent.enrollment_id = pday.enrollment_id)
	inner join 
	citrisfinancial_report.highline_bill_object as bobj 
	on bobj.enrollment_id = pday.enrollment_id
	
	"""
	
	# Define the table and column names for insertion
    insert_table = 'citrisfinancial_report.plp_payments'
    insert_columns = ['id', 'product_id', 'enrollment_id','payment_number','month','payment_amount'] 
	
	
    try:
		# Execute the query with the provided condition value
        cursor.execute(query)
	
		# Fetch all the rows that satisfy the condition
        rows = cursor.fetchall()
        payment_not_matching_condition = []
		
        if rows:
            current_date = datetime.now()
            print("Rows found with payment details")
            for row in rows:
                payment_event = row[1]
                product_id = row[2]
                amount_due = row[4]  # Assuming event_status is in the 4th column (index 3)
                enrollment_id = row[12]
                payment_amount = row[15]
                id=row[18]
                month = row[19]
                payment_number = row[21]
				
				#print(event_status)
				#print(current_date - load_timestamp)
                print(amount_due)
                print(payment_amount)
                print(payment_event)
							
                #if int(amount_due) == int(payment_amount):
                if int(payment_amount) != 0:
                    print(row)
					
                    '''        
				
					# Query to retrieve the maximum id value
					max_id_query = f"SELECT MAX(id) FROM {insert_table}"
					# Execute the query to retrieve the maximum id value
					cursor.execute(max_id_query)
					# Fetch the maximum id value
					max_id = cursor.fetchone()[0]
					
					# Increment the max_id value by one
					new_id = max_id + 1
					
					'''
					
					# Prepare the INSERT statement
                    insert_query = f"""INSERT INTO {insert_table} ({', '.join(insert_columns)})
									VALUES (%s, %s, %s, %s, %s, %s)"""  # Replace with the actual column names
				
				# Provide the values for the INSERT statement
                    insert_values = (id, product_id, enrollment_id,payment_number,month,payment_amount)  # Replace with the actual values
					
				
				# Execute the INSERT statement
                    cursor.execute(insert_query, insert_values)
                    print("Inserted a row into the plp table.")
                
                # Commit the transaction
                    conn.commit()
                
                # Get the number of rows inserted
                    rows_inserted = cursor.rowcount

                # Check if any rows were inserted
                    if rows_inserted > 0:
                       print(f"Inserted {rows_inserted} row(s) into the plp table.")
                    else:
                       print("No rows were inserted.")
				
                else:
                    #enrollment_id = row[1]  # Assuming enrollment_id is in the 2nd column (index 1)
                    print("PAYMENT NOT MATCHING")
                    print(row)
                    payment_not_matching_condition.append([payment_event, id, product_id, amount_due, enrollment_id, payment_amount, month, payment_number])
        else:
            print("No rows found with the provided condition.")

        if payment_not_matching_condition:
        
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            # Specify the filename for the CSV file
            csv_filename = f'payment_notmade_{timestamp}.csv'
        
            # Specify the header row
            header = ['event', 'id', 'product_id', 'amount_due', 'enrollment_id', 'payment_amount', 'month', 'payment_number']
            
            # Create a file-like object in memory
            csv_file = io.StringIO()
            
            # Create a CSV writer using the file-like object
            #writer = csv.writer(csv_fileobj)
            
            # Create a CSV writer
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(payment_not_matching_condition)          
            
               # Encode the CSV data as bytes
            #csv_data_bytes = csv_file.getvalue().encode()
        

            print(f"Rows not matching the condition written to {csv_filename}.")
			
			# Upload the CSV file to S3
            s3 = boto3.client('s3')
            s3_filename = f'{s3_folder_name}/{csv_filename}'
            
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
            conn.close()
