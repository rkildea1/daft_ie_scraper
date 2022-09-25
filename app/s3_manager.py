import boto3
import variables as myvars


# s3_photo_folder_path = myvars.s3_photo_folder_path
s3client = boto3.client('s3', aws_access_key_id=myvars.awsid, aws_secret_access_key=myvars.awskey)




def upload_json_to_s3(): #called from the ad_detail_scraper and gets passed the cleaned dataframe
    """
    upload the json to s3
    """
    s3client.upload_file(myvars.json_output_path, Bucket=myvars.s3_bucket_name, Key=myvars.s3_json_file_path )
    print(f'.......Successfully uploaded cleaned json file `{myvars.json_file_name}` to s3 bucket: `{myvars.s3_bucket_name}` at location: `{myvars.s3_json_file_path}` ' )



def upload_image_to_s3(local_image, destination_img_name,s3_photo_folder_path):
    """
    upload the images at location image_source to s3 under name aws_image_name
    """
    folder_path_and_name = (s3_photo_folder_path+destination_img_name)
    s3client.upload_file(local_image, Bucket=myvars.s3_bucket_name, Key=folder_path_and_name )


