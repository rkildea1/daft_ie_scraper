import pandas as pd
import regex as re
import time
import uuid
from file_handler import LOCALFILESHANDLER
lfh = LOCALFILESHANDLER() 
from link_list_generator import DAFTFORRENTCRAWLER
from selenium.webdriver.common.by import By
import string
import variables as myvars
import s3_manager as s3
prop_url_list = []

class SCRAPER:
    """
    includes all methods for capturing the ad related text information 
    """

    prop_address_list = []
    prop_type_list = []
    prop_price_list = []
    prop_beds_list = []
    prop_baths_list = []
    prop_desc_list = []
    prop_lat_long_list = []
    date_entered_list = []
    views_list = []
    prop_main_photo_list = []

    def __init__(self):
        pass

    def get_prop_address(self): 
        """
        Method Summary: Gets the address of the property
        """   
        try:
            address = driver.find_element(by=By.XPATH, value='//*[@class="TitleBlock__Address-sc-1avkvav-8 dzihxK"]').text
            SCRAPER.prop_address_list.append(address)
            
        except:
            address = '*** no value found ***'
            SCRAPER.prop_address_list.append(address)
        finally:
            print(SCRAPER.prop_address_list)

    def get_prop_type(self):
        """
        Method Summary: gets the property type e.g., house/ apartment
        """
        try:
            prop_type = driver.find_element(by=By.XPATH, value='//*[@class="TitleBlock__CardInfoItem-sc-1avkvav-9 cKZYAr"]').text
            SCRAPER.prop_type_list.append(prop_type)

        except:
            prop_type = '*** no value found ***'
            SCRAPER.prop_type_list.append(prop_type)
        pass


    def get_prop_price(self):
        """
        Method Summary: Gets advert price
        """
        try:
            price = driver.find_element(by=By.XPATH, value='//*[@class="TitleBlock__StyledSpan-sc-1avkvav-5 fKAzIL"]').text
            SCRAPER.prop_price_list.append(price)
        except:
            price = '*** no value found ***'
            SCRAPER.prop_price_list.append(price)
            pass

    def get_prop_beds(self):
        """
        Method Summary: Gets the count of bedrooms in the property
        """
        try:
            beds = driver.find_element(by=By.XPATH, value='//*[@class="TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"]').text
            SCRAPER.prop_beds_list.append(beds)
        except:
            beds = '*** no value found ***'
            SCRAPER.prop_beds_list.append(beds)
            pass


    def get_prop_baths(self):
        """
        Method Summary: Gets the count of baths in the property
        """
        try:
            baths = driver.find_element(by=By.XPATH, value='//*[@class="TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"][2]').text
            SCRAPER.prop_baths_list.append(baths)
        except:
            baths = '*** no value found ***'
            SCRAPER.prop_baths_list.append(baths)
            pass


    def get_prop_date_entered(self):
        """
        Method Summary: gets the date of ad creation/ renewal
        """
        try:
            date_entered = driver.find_element(by=By.XPATH, value="(//*[contains(@class,'Statistics__StyledLabel-sc-15tgae4-1')])[1]").text
            SCRAPER.date_entered_list.append(date_entered)

        except:
            date_entered = '*** no value found ***'
            SCRAPER.date_entered_list.append(date_entered)
            pass


    def get_prop_views(self):
        """
        Method Summary: Gets the total advert views if it exists
        """
        try:#first XPATH type
            views = driver.find_element(by=By.XPATH, value="(//*[contains(@class,'Statistics__StyledLabel-sc-15tgae4-1')])[2]").text
            SCRAPER.views_list.append(views)
        except:
            views = '*** no value found ***'
            SCRAPER.views_list.append(views)
            pass                                           


    def get_prop_description(self):
        """
        Method Summary: Gets the description section of each advert
        """
        try:
            property_description = driver.find_element(by=By.XPATH, value='//*[@class="styles__StandardParagraph-sc-15fxapi-8 eMCuSm"]').text
            SCRAPER.prop_desc_list.append(property_description)
        except:
            property_description = '*** no value found ***'
            SCRAPER.prop_desc_list.append(property_description)
            pass


    def get_prop_lat_long(self):
        """
        Method Summary: Gets the Lat and Long of each advert
        """
        try:
            maps_link = driver.find_element_by_partial_link_text('Satellite View').get_attribute('href')
            regex_pattern = "([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?"
            result = re.findall(regex_pattern, maps_link )
            latitude_long = (result[0][0], result[1][0])
            # print(latitude_long)
            SCRAPER.prop_lat_long_list.append(latitude_long)
        except:
            latitude_long = '*** no value found ***'
            SCRAPER.prop_lat_long_list.append(latitude_long)
            pass


    def get_prop_main_photo(self):
        """
        Method Summary: Gets the link for the ads main image
        """
        try:
            main_photo = driver.find_element(by=By.XPATH, value="(//*[contains(@class,'HeaderImage__StyledHeaderImage')])/*").get_attribute('srcset')
            SCRAPER.prop_main_photo_list.append(main_photo)

        except:
            main_photo = '*** no value found ***'
            SCRAPER.prop_main_photo_list.append(main_photo)
        pass


    pass

def start_driver():
    """
    Uses method from link_list_generator to create the driver
    """
    start_driver = DAFTFORRENTCRAWLER() # calls class from link_list_generator
    global driver
    driver = start_driver.start_driver() #calls method from link_list_generator.DAFTFORRENTCRAWLER
    return driver 

def stop_driver():
    driver.close()

def open_site(url): 
    """
    Method Summary: Opens the site and accepts the cookies notice
    """
    # driver = start_driver() commenting out to see can i stop restarting driver on each iteration
    driver.get(url)
    prop_url_list.append(url)
    time.sleep(4)
    try: 
        cookiexpath = '/html/body/div[1]/div/div/main/div/button[2]' #cookie-accept xpath
        accept_cookies_button = driver.find_element(by=By.XPATH, value=cookiexpath) #To make the driver point to the element
        accept_cookies_button.click() #make the driver click on the element
        print('cookies accepted')
    except:
        'accept_cookies fails'

def check_page_is_not_parent_dev():
        """
        Method Summary: Parent-ad pages are those that contain sub ads. This method checks that the current url is actually an ad page and not a parent-ad using XPATH
        """
        try:
            development_text_class = '//*[@class="styles__H3-sc-15fxapi-6 styles__SpacedH3-sc-15fxapi-24 kOciVj bYxUpy"]'
            development_text_class_text = driver.find_element(by=By.XPATH, value=development_text_class).text
            while 'in this Development' in development_text_class_text:
                return
        except:
            try:
                time.sleep(2)
                no_results_class = '//*[@class="ZeroResults__HeaderText-sc-193ko9u-3 cnKCru"]'
                no_results_class_text = driver.find_element(by=By.XPATH, value=no_results_class).text
                while "We didn't find any properties" in no_results_class_text:
                    break
            except:
                return
        finally:
            return


                


def create_dataframe_from_lists():
    """
    Method Summary: creates a DF from all the scraped data. 
    create a dict from all the lists
    write the dict to a df. 
    """

    dict_for_df = { 
        'Ad_link':prop_url_list,
        'Address':SCRAPER.prop_address_list,
        'Type':SCRAPER.prop_type_list,
        'Price':SCRAPER.prop_price_list,
        'Beds':SCRAPER.prop_beds_list,
        'Baths':SCRAPER.prop_baths_list,
        'Description':SCRAPER.prop_desc_list,
        'Latitude_Longitude':SCRAPER.prop_lat_long_list,
        'Advert_Views':SCRAPER.views_list,
        'Date_Entered':SCRAPER.date_entered_list,
        'Main Photo': SCRAPER.prop_main_photo_list
    }
    df = pd.DataFrame(dict_for_df)
    return df




def image_downloader():
    """
    Download a screenshot of the main image from the advert url
    """
    print('......Starting image downloader')
    zip_of_photo_url_and_prop_address = zip(SCRAPER.prop_main_photo_list, SCRAPER.prop_address_list) #create a zip_iterable of the image URL and prop_address
    
    target_image_folder = lfh.create_and_return_local_image_drectory() #create and return the target image folder


    
    for image_url,prop_address in zip_of_photo_url_and_prop_address:
        
        cleaned_name = (prop_address.translate(str.maketrans('', '', string.punctuation)))
        save_name = cleaned_name.replace(" ", "")
        ftype = '.png'
        if 'novaluefound' in save_name: #images without a description (i.e., images which are parent-ad adverts can be skipped as they are cleaned from the dataframe anyways)
            pass
        else:
            try:
                driver.get(image_url)
                time.sleep(3)
                print('......Starting image download')
                driver.save_screenshot(target_image_folder+save_name+ftype)
                aws_image_name = save_name+ftype
                local_image_location= target_image_folder+save_name+ftype 
                print('......Starting upload to s3')
                s3.upload_image_to_s3(local_image_location, aws_image_name, myvars.s3_photo_folder_path)
                print('......upload complete - moving to next image...')
            except:
                print('not reaching image download try')
                pass
    print('......All images downloaded & passed to S3 successfully')
        
    