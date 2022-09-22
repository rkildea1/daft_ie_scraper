
import load_env as load_env_vars

#referenced in all_advert_urls_scraper.py
# num_of_pages_input = input('how many pages of ads do you want to scrape for property urls?: ')
num_of_pages = 1 
output_files_folder_name = 'output_files'
all_links_csv_name = 'mycsvexport.csv' #what do you want to call the output csv which stores all hrefs (i.e., all the actual property advertisement links)






##privateVariables
#used in ['storage_managers/rds_connector']
RDSTABLENAME = load_env_vars.RDSTABLENAME
RDSPASS = load_env_vars.RDSPASS
RDSHOST = load_env_vars.RDSHOST
RDSUSER = load_env_vars.RDSUSER
RDSDATABASENAME = load_env_vars.RDSDATABASENAME
