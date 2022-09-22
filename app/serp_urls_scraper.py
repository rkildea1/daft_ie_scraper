"""
Capture the url of every for-rent advertisement on the website search engine results page (SERP)
Works by 
- opening the first page of daft.ie/for-rent/
- then goes through every followon SERP (page 2, page 3 etc)
- captures all urls that contain `for-rent` in the url and writes them to a pandas series
- checks if any url exists already in the database
- if the url does not exist in the database it gets written to a csv file and stored on the root.
"""

import os
from re import M
# from webbrowser import Chrome #don't think these are used anywhere
# from selenium import webdriver #don't think these are used anywhere
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import rds_connector
import variables as myvars
from selenium.webdriver.chrome.options import Options



all_links_csv_name = myvars.all_links_csv_name
num_of_pages = myvars.num_of_pages  #how many pages of adverts should be scanned for specific property urls? 
                                    #Can change this to an input using var 'myvars.num_of_pages_input'

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")

class DAFTFORRENTCRAWLER:
    list_of_individual_advert_links = []
    #if exists, will return an array of the values
    list_of_all_db_rows = rds_connector.return_existing_db_urls() #this is called outside of the function so it only gets called once. 


    def __init__(self):
        pass
   
    def open_site(self): 
        """
        Opens the site and accepts the cookies notice
        """
        global driver #globalise driver
        url = "https://www.daft.ie/property-for-rent/ireland"
        driver = Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
        driver.get(url)
        try: 
            time.sleep(4)#accept the cookie banner
            cookiexpath = '/html/body/div[1]/div/div/main/div/button[2]' #cookie-accept xpath
            accept_cookies_button = driver.find_element(by=By.XPATH, value=cookiexpath) #To make the driver point to the element
            accept_cookies_button.click() #make the driver click on the element

        except:
            print('the scraper was not able to accept cookies and has failed')


    def get_all_individual_advert_links(self):
        """
        Grab all hrefs on page. if the href includes 'daft.ie/for-rent/' put them in a list 
        """
        elems = driver.find_elements_by_xpath("//a[@href]") # xpath for hrefs on the page
        for elem in elems: #for every href xpath
            x = elem.get_attribute("href") #x = value of the href
            if 'daft.ie/for-rent/' in x: #if the value of the link contains '___' then ..
                DAFTFORRENTCRAWLER.list_of_individual_advert_links.append(x) #append the global list


    def move_to_next_page(self):
        """
        Find the 'Next' button and click it to move to the next page
        """
        try:
            next_page = '//*[@aria-label="Next >"]' #NEXT button 
            next_page_button = driver.find_element(by=By.XPATH, value=next_page) #To make the driver point to the element
            next_page_button.click() #make the driver click on the element
            print('moving to next page')
        except:
            print('no more pages')
            pass

    def remove_links_already_in_database(self):
        for csv_link in DAFTFORRENTCRAWLER.list_of_individual_advert_links:
            if csv_link in DAFTFORRENTCRAWLER.list_of_all_db_rows:
                DAFTFORRENTCRAWLER.list_of_individual_advert_links.remove(csv_link)
            else:
                pass

    def get_add_links_on_all_pages(self):
        """
        Go through each serp page, and run the two methods to capture all hrefs, and hit the next button
        When `count` meets `num_of_pages` var, move to ELSE and write all links to a csv
        then close the driver
        """
        
        count = 0 #count for a while loop
        while count < num_of_pages:
            count = count + 1
            print(f'count = {count}') #test can remove
            time.sleep(4)
            self.get_all_individual_advert_links() #make list of all for-sale links
            time.sleep(4)
            self.move_to_next_page() #move to the next page of adverts
            print(f"currently on results page number: {count}")
            print(f'So far we have collected this many adverts: {len(DAFTFORRENTCRAWLER.list_of_individual_advert_links)}')
        else:
            first_scrape_question = input('Is this your first scrape?[y]/[n]: ')
            if first_scrape_question.lower() == 'n':
                # since its not the first crawl, there will be links already stored in the database and we want to check them for duplciates to prevent recrawling
                print('Got it - lets check the database incase you have already crawled some of these links.......')
                print(f'the count of urls before cross-referencing the database is: {len(DAFTFORRENTCRAWLER.list_of_individual_advert_links)}')
                self.remove_links_already_in_database()
                print(f'the count of urls after cross-referencing the database is: {len(DAFTFORRENTCRAWLER.list_of_individual_advert_links)}')
            else:
                pass # pass as there is no database list to already compare the crawl to
            os.makedirs(myvars.output_files_folder_name,exist_ok=True) #create a directory to store the crawl locally
            adverts_series = pd.Series(DAFTFORRENTCRAWLER.list_of_individual_advert_links)
            csv_storage_location =(myvars.output_files_folder_name+'/'+all_links_csv_name)
            adverts_series.to_csv(csv_storage_location) #write the series to a csv file
            print(f'All source links captured and stored in: {csv_storage_location}')
            # import group_get_ad_details_c2 as gad #queing the import
            driver.close()
            print(f'last count is: {count}')
            # gad.run_get_details_crawler(all_links_csv_name) #kick off the main crawler
            
def run_crawler():
    start_crawl_class = DAFTFORRENTCRAWLER()
    start_crawl_class.open_site()
    start_crawl_class.get_add_links_on_all_pages()


