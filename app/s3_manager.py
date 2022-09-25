import boto3
import variables as myvars


# s3_photo_folder_path = myvars.s3_photo_folder_path
s3client = boto3.client('s3', aws_access_key_id=myvars.awsid, aws_secret_access_key=myvars.awskey)




def upload_json_to_s3(): #called from the ad_detail_scraper and gets passed the cleaned dataframe
    """
    upload the json to s3
    """
    s3client.upload_file(myvars.json_output_path, Bucket=myvars.s3_bucket_name, Key=myvars.s3_json_file_path )
