


import pandas as pd
import regex as re
import datetime as date
import variables as myvars

class TRANSFORMER:

    """        
    ETL tool for scraped data from daft for-rent advertisements
    """

    def __init__(self):
        pass

    def return_weekly_or_monthly_from_price(self):
        """
        clean the price column. Search for payment rate and 
        create new categorical column for monthly or weekly payments
        """
        if 'per week' in self:
            return 'Weekly'
        elif 'per month' in self:
            return 'Monthly'
        else:
            return '*** no value found ***'


    def find_ads_with_no_details(self):
        """
        Find  cells without valid critera and tag to remove
        """
        if '***' in self:
            return 'No Advert Details'
        else:
            return 'Details Found'

    def additional_no_details_beds(self):
        """
        Find  cells without valid critera and tag to remove.
        Useful in cases where entry should be a single char e.g., '1' instead of '1 bed'
        """
        if len(self) >1:
            return "Remove"
        else:
            return "Keep"


    def add_latitudes(self):
        """return latitude from list"""
        try:
            return self[0]
        except:
            return 'None_found'

    def add_longitudes(self):
        """return longitude from list"""
        try:
            return self[1]
        except:
            return 'None_found'




def clean_price(df):
    #clean price column
    df['Rent_Frequency'] = df['Price'].apply(TRANSFORMER.return_weekly_or_monthly_from_price)
    #create new column with Price of rent 
    df['Rent_Price'] = df['Price'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
    #create new column with cleaned Advert page views 
    df['views_cleaned'] = df['Advert_Views'].astype('str').str.replace(',','')
    #drop Advert Views as no longer needed 
    df = df.drop(['Advert_Views'], axis =1)
    clean_beds_and_baths(df)

def clean_beds_and_baths(df):
    #clean BEDS and BATHS columns to remove strings and leave as digit values
    df['Beds'] = df['Beds'].astype('str').str.replace(' Bed','')
    df['Baths'] = df['Baths'].astype('str').str.replace(' Bath','')
    # Create a TEMP column of adverts that do not have beds and are not final ads
    # delete the rows without valid ads, and then drop the column again
    df['Beds_check'] = df['Beds'].apply(TRANSFORMER.additional_no_details_beds)
    df = df.loc[df['Beds_check'] != 'Remove']
    df = df.drop(['Beds_check'], axis =1)
    remove_useless_rows(df)
    
def remove_useless_rows(df):
    #Create a TEMP column of adverts that do not have prices and are not final ads
    #delete the rows without valid ads, and then drop the column again
    #drop Price as no longer needed
    df['Valid_Advert'] = df['Price'].apply(TRANSFORMER.find_ads_with_no_details)
    df = df[df['Valid_Advert'].str.contains('No')==False]
    df = df.drop(['Valid_Advert'], axis =1)
    df = df.drop(['Price'], axis =1)
    long_lat_spitting(df)


def long_lat_spitting(df):
    #Split Latitude_Longitude into seperate columns
    #create lat and long tables and remove the base table. Format them as floats
    df['Latitudes'] = df['Latitude_Longitude'].apply(TRANSFORMER.add_latitudes).astype(float)
    df['Longitudes'] = df['Latitude_Longitude'].apply(TRANSFORMER.add_longitudes).astype(float)
    df = df.drop(['Latitude_Longitude'], axis =1)
    typecasting(df)

def typecasting(df):
    #carry out any outstanding typecasting
    df['Address'] = df['Address'].astype('str')
    df['Beds'] = df['Beds'].astype('int')
    df['Baths'] = df['Baths'].astype('int')
    df['Date_Entered'] = df['Date_Entered'].astype({'Date_Entered': 'datetime64[ns]'})
    df['Rent_Frequency'] = df['Rent_Frequency'].astype('category')
    df['views_cleaned'] = df['views_cleaned'].astype('int')
    df['Rent_Price'] = df['Rent_Price'].astype('int')
    # connect_to_database(df)
    return df



def kick_off_etl(df):
    """
    function which kicks off all the cleaning tasks
    """
    clean_price(df)
    return df




def create_df_for_cleaning(): #gets called from ad_detail_scraper
    """
    Function which is called outside the script to return the cleaned dataframe
    """ 
    df = pd.read_json(myvars.json_output_path,orient='UUID')
    return kick_off_etl(df)  #this returns the cleaned dataframe

    
