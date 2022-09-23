import boto3
import variables as myvars

s3_bucket_name = myvars.s3_bucket_name
# s3_photo_folder_path = myvars.s3_photo_folder_path
s3client = boto3.client('s3', aws_access_key_id=myvars.awsid, aws_secret_access_key=myvars.awskey)




def upload_json_to_s3(): #called from the ad_detail_scraper and gets passed the cleaned dataframe
    """
    upload the json to s3
    """
    json_local_location = myvars.json_local_location
    import transformer as etl
    etl.create_df_for_cleaning(json_local_location)

    folder_path = myvars.folder_path
    # folder_path = str(input(f'Enter the filename on the s3 bucket "{s3_bucket_name}" where you want to store the json. E.g., "myjson/ZIP_2_data.json": '))
    s3client.upload_file(json_local_location, Bucket=s3_bucket_name, Key=folder_path )
