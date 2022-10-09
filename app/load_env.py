from dotenv import load_dotenv
import os
load_dotenv()


s3_bucket_name = os.getenv("s3_bucket_name")
RDSTABLENAME = os.getenv("RDS_TABLENAME")
RDSPASS = os.getenv("RDS_PASSWORD")
RDSHOST = os.getenv("RDS_HOST")
RDSUSER = os.getenv("RDS_USER")
awskey = os.getenv('aws_secret_access_key')
awsid = os.getenv('aws_access_key_id')
RDSDATABASENAME = os.getenv('RDS_DATABASENAME')
   

