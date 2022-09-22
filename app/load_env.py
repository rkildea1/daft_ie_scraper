from dotenv import load_dotenv
import os
load_dotenv()
"""
Used for leveraging a .env file with the following variables: 

* aws_access_key_id=YOUR_AWS_ACCESS_KEY_ID
* aws_secret_access_key=YOUR_AWS_SECRET_ACCESS_KEY
* s3_bucket_name=S3_BUCKET_NAME_YOU_WANT_TO_CREATE
* pgdbname=DATABASE_NAME
* pgdbnamepassword=DATABASE_PASSWORD
* databasename=DATABASE_NAME
* DBHOST=DATABASE_HOST
* DBUSER=DATABASE_USER
"""


s3_bucket_name = os.getenv("s3_bucket_name")
RDSTABLENAME = os.getenv("RDS_TABLENAME")
RDSPASS = os.getenv("RDS_PASSWORD")
RDSHOST = os.getenv("RDS_HOST")
RDSUSER = os.getenv("RDS_USER")
awskey = os.getenv('aws_secret_access_key')
awsid = os.getenv('aws_access_key_id')
RDSDATABASENAME = os.getenv('RDS_DATABASENAME')
   

