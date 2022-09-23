import time
import load_env as load_env_vars

#referenced in all_advert_urls_scraper.py
# num_of_pages_input = input('how many pages of ads do you want to scrape for property urls?: ')
num_of_pages = 1 
output_files_folder_name = 'output_files'
all_links_csv_name = 'mycsvexport.csv' #what do you want to call the output csv which stores all hrefs (i.e., all the actual property advertisement links)
csv_output_path = (output_files_folder_name+'/'+all_links_csv_name) #prints `output_files/mycsvexport.csv`



timestamp = time.strftime("%Y%m%d-%H%M%S")
json_file_path = (output_files_folder_name+'/'+'ad_details_raw')
json_file_name = ('data'+timestamp+'.json')
json_output_path = (json_file_path+'/'+json_file_name)

local_image_folder_path = (output_files_folder_name+'/'+'ad_details_photos/') #which directory on your machine should you store the photos 
s3_photo_folder_path = 'ad_details_photos/' #which directory on s3 should you store the photos


##privateVariables
#used in ['storage_managers/rds_connector']
RDSTABLENAME = load_env_vars.RDSTABLENAME
RDSPASS = load_env_vars.RDSPASS
RDSHOST = load_env_vars.RDSHOST
RDSUSER = load_env_vars.RDSUSER
RDSDATABASENAME = load_env_vars.RDSDATABASENAME

#s3 details
awskey = load_env_vars.awskey
awsid = load_env_vars.awsid
s3_bucket_name = load_env_vars.s3_bucket_name
