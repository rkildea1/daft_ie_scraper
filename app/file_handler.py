
import os
import pandas as pd
import variables as myvars
import uuid
import shutil


"""
Used to capture all the information from the specific_ad_url
Puts all the information scraped into a json on the application root folder
it downloads all images from the specific_ad_urls and then stores them in a folder on the root

"""


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

  
    def write_json_locally(self,df):
        """
        create a directory to store the json
        read in a dataframe and and a UUID column
        write the dataframe to a .json
        """
        uuid_list = []
        countUUID = 0
        while countUUID < len(df.index): #create a list of UUIDs the length of the dataframe index
            uuid_list.append(str(uuid.uuid4()))
            countUUID += 1
        try: #create a directory if it doesn't exist
            os.makedirs(myvars.json_file_path,exist_ok=True) 
        except:
            pass 
        finally:
            df.insert(0, 'UUID', uuid_list)#Add the UUID to the dataframe to the first column
            df.to_json(myvars.json_output_path) #filename+path for json
            pass


    def create_and_return_local_image_drectory(self):
        """
        Create a storage location for images and return the location 
        """
        os.makedirs(myvars.local_image_folder_path,exist_ok=True)
        return myvars.local_image_folder_path


    def delete_local_files(self):
        """clear all local files"""
        # location
        location = "."
        # directory
        dir = "output_files"
        # path
        path = os.path.join(location, dir)
        # removing directory
        shutil.rmtree(path, ignore_errors=False)
        print('......Locally stored files have been removed successfully')


