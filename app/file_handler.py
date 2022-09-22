'''
Get csv
get ad details
get photos
store locally
'''



"""
Used to capture all the information from the specific_ad_url
Puts all the information scraped into a json on the application root folder
it downloads all images from the specific_ad_urls and then stores them in a folder on the root

"""
import os
import pandas as pd
import variables as myvars
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class LOCALFILESHANDLER: 
    

    def __init__(self):
        pass

    def read_csv_link_list_as_series(self):
        """
        method to read link_link csv output and return as a series 
        """
        links_of_individual_adverts = []
        df = pd.read_csv(myvars.csv_output_path,index_col=0) #source file
        series_of_all_ad_urls_captured = df.iloc[:, 0]
        for ad_url in series_of_all_ad_urls_captured:
            links_of_individual_adverts.append(ad_url) 
        return links_of_individual_adverts #this list is used to iterate over individual adverts by the ad_detail_scraper

#OLD
      #     Function summary: this is the function which reads in all of the links captured from the ad-link crawler
    #     - read as a csv to a df
    #     - write it to a list 
    #     """
    #     df = pd.read_csv(sourcecsv,index_col=0) #source file
    #     series_of_all_ad_urls_captured = df.iloc[:, 0]
    #     for ad_url in series_of_all_ad_urls_captured:
    #         links_of_individual_adverts.append(ad_url) #moved from get_ad_details module as dont think it was in use there
    
    def extract_df_and_write_locally_as_json(self):
        """
        Function summary: Write the results to a .json
        create a directory to store the json
        write the dataframe to a .json
        """
        try:
            os.makedirs(myvars.json_file_path,exist_ok=True)
        except:
            pass 
        finally:
            # get_details.df.to_json(myvars.json_output_path) #filename for json
            pass

#OLD

    # def extract_df_and_write_locally_as_json():
    #     """
    #     Function summary: Write the results to a .json
    #     create a directory to store the json
    #     write the dataframe to a .json
    #     """
    #     json_file_path = myvars.json_file_path
    #     json_file_name = myvars.json_file_name
    #     try:
    #         os.makedirs(json_file_path,exist_ok=True)
    #     except:
    #         pass #if no file path entered just pass
    #     finally:
    #         get_details.df.to_json(json_file_path+json_file_name) #filename for json

    def store_images_locally(self):

        os.makedirs(myvars.local_image_folder_path,exist_ok=True)

