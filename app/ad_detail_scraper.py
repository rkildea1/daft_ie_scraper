import time
from file_handler import LOCALFILESHANDLER
import scraper_configurations as get_details
import transformer
lfh = LOCALFILESHANDLER() 

"""
runs the scraper configuration to capture all individual advert details
"""

def pass_in_list_of_individual_ad_links():
    """
    Simple function to in the list of indivudal ads to the run_get_details_crawler method
    """
    links_of_individual_adverts = lfh.read_csv_link_list_as_series() # referencing the file_handler to pull in the link_list
    return links_of_individual_adverts

    

def run_get_details_crawler():
    links_of_individual_adverts = pass_in_list_of_individual_ad_links()
    count = 0 #only really used to monitor the progress of the script. #can be removed. 
    get_details.start_driver() #start up the driver
    capture_data = get_details.SCRAPER() #start the sraper configuration class
    for specific_ad_url in links_of_individual_adverts[0:3]: #added slicing for testing purposes
        count = count + 1 #only really used to monitor the progress of the script. #can be removed. 
        print(specific_ad_url) #prints the current advert to console #can be removed
        print(f'Currently on Ad Number: {count}') #only really used to monitor the progress of the script. #can be removed.
        
        #introduce the scraper_configuration file
        get_details.open_site(specific_ad_url) #open the site and accept cookies 
        get_details.check_page_is_not_parent_dev() # Check that the page is not a paent-ad page
        time.sleep(4)
        #start capturing the data
        capture_data.get_prop_address() #Gets the address of the property
        capture_data.get_prop_description() #Gets the description section of each advert
        capture_data.get_prop_baths() #Gets the count of baths in the property
        capture_data.get_prop_beds() #Gets the count of bedrooms in the property
        capture_data.get_prop_price() #Gets advert price
        capture_data.get_prop_type() #Gets the property type e.g., house/ apartment
        capture_data.get_prop_date_entered() #Gets the date of ad creation/ renewal
        capture_data.get_prop_views() #Gets the total advert views if it exists
        capture_data.get_prop_lat_long() #Gets the Lat and Long of each advert
        capture_data.get_prop_main_photo() #Grabs the url of the main photo
    else:
        df_of_captured_data = get_details.create_dataframe_from_lists() #Creates a DF from all the scraped data. Also assigns each record with a UUID(v4)
        lfh.write_json_locally(df_of_captured_data)
        print(f'complete. Captured {count} ads') #prints a total count of ads captured. Can remove this
        transformed_df = transformer.create_df_for_cleaning() #returns cleaned dataframe
        print(transformed_df)
        #clean the data and return




        # aws_s3_image_writer.upload_json_to_s3() #upload the json to s3
#         download_images_and_write_to_s3() #Downloads images of each ad, using the link catptured from the crawl
#         get_details.driver.close() #closes the browser window 


# if __name__ == '__main__':
#     run_get_details_crawler()

run_get_details_crawler()
