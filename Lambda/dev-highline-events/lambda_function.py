import json
import boto3
from datetime import datetime
import psycopg2 as pg

def lambda_handler(event, context):
    print("Received event: " , json.loads(json.dumps(event)))
    
    object_content = json.loads(json.dumps(event))
    print(json.loads((object_content['body'])))
    _json_body = json.loads((object_content['body']))
    _event_user_id = f"hl_{_json_body['payload']['user_id']}"
    _event_topic = f"{_json_body['topic']}"
    _event_ts = f"{_json_body['occurred_at']}.json"
    _event_scenario = 1
    
    _host_name='citris-app-aurora-pg-dev.cluster-cf5khejaiz0c.us-west-1.rds.amazonaws.com'

    connection = pg.connect(
        database="citrisappdb",
        user='appdev_admin',
        password='Nhguh67gdT6gtakA3ncs7JK',
        host=_host_name,
        port='5432'
    )
    cursor = connection.cursor()


    # postgres_insert_query = "INSERT INTO citrisfinancial_report.hl_events_candidate VALUES(1,1,'{'a':'1'}',1,1)"
    postgres_insert_query = f"INSERT INTO citrisfinancial_report.hl_events_candidate(user_id, event, event_json, verification_scenario, load_timestamp) VALUES('{_event_user_id}','{_event_topic}','{json.dumps(_json_body)}','1','{datetime.now()}')"
    
    # postgres_insert_query = "insert into citrisfinancial_report.hl_events_candidate(user_id, event, event_json, verification_scenario, load_timestamp) values(%s ,%s, %s, %d, %s)", (player1, player2, player1_result, player2_result))
    cursor.execute(postgres_insert_query)

    connection.commit()
    connection.close()


    s3 = boto3.client('s3')

    # Write output to S3 bucket
    bucket_name = 'test-highline-webhook-events'
    
    dt = datetime.fromtimestamp(_json_body['occurred_at'])
    directory_name = f"y_{str(dt.year)}/m_{str(dt.month)}/d_{str(dt.day)}/h_{str(dt.hour)}/"
    object_key = (directory_name+_event_user_id + '_' + _event_topic + '_' + _event_ts)

    s3.put_object(
        Bucket=bucket_name, Key=object_key, Body=object_content['body']
    )


    return {
        'statusCode': 200,
        'body': json.dumps('Output uploaded to S3')
    }