


import pandas as pd
import regex as re
import datetime as date
import variables as myvars

class CLEANER_ITERATOR:

    """        
    Some transformer Try/Accepts rules for iterating over the columns to clean the data
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


class CLEANER:
    """
    Cleaner class
    """
    def __init__(self,df):
        self.df = df

    def clean_price(self,df):
        #clean price column
        self.df['Rent_Frequency'] = self.df['Price'].apply(CLEANER_ITERATOR.return_weekly_or_monthly_from_price)
        #create new column with Price of rent 
        self.df['Rent_Price'] = self.df['Price'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
        #create new column with cleaned Advert page views 
        self.df['views_cleaned'] = self.df['Advert_Views'].astype('str').str.replace(',','')
        #drop Advert Views as no longer needed 
        self.df = self.df.drop(['Advert_Views'], axis =1)
        return self.df

    def clean_beds_and_baths(self,df):
        #clean BEDS and BATHS columns to remove strings and leave as digit values
        self.df['Beds'] = self.df['Beds'].astype('str').str.replace(' Bed','')
        self.df['Baths'] = self.df['Baths'].astype('str').str.replace(' Bath','')
        # Create a TEMP column of adverts that do not have beds and are not final ads
        # delete the rows without valid ads, and then drop the column again
        self.df['Beds_check'] = self.df['Beds'].apply(CLEANER_ITERATOR.additional_no_details_beds)
        self.df = self.df.loc[self.df['Beds_check'] != 'Remove']
        self.df = self.df.drop(['Beds_check'], axis =1)
        return self.df
        
    def remove_useless_rows(self, df):
        #Create a TEMP column of adverts that do not have prices and are not final ads
        #delete the rows without valid ads, and then drop the column again
        #drop Price as no longer needed
        self.df['Valid_Advert'] = self.df['Price'].apply(CLEANER_ITERATOR.find_ads_with_no_details)
        self.df = self.df[self.df['Valid_Advert'].str.contains('No')==False]
        # self.df = self.df.drop(['Valid_Advert'], axis =1)
        # self.df = self.df.drop(['Price'], axis =1)
        self.df = self.df.drop(['Valid_Advert'], axis =1)
        self.df = self.df.drop(['Price'], axis =1)
        return self.df


    def long_lat_spitting(self,df):
        #Split Latitude_Longitude into seperate columns
        #create lat and long tables and remove the base table. Format them as floats
        self.df['Latitudes'] = self.df['Latitude_Longitude'].apply(CLEANER_ITERATOR.add_latitudes).astype(float)
        self.df['Longitudes'] = self.df['Latitude_Longitude'].apply(CLEANER_ITERATOR.add_longitudes).astype(float)
        self.df = self.df.drop(['Latitude_Longitude'], axis =1)
        return self.df

    def typecasting(self, df):
        #carry out any outstanding typecasting
        self.df['Address'] = self.df['Address'].astype('str')
        self.df['Beds'] = self.df['Beds'].astype('int')
        self.df['Baths'] = self.df['Baths'].astype('int')
        self.df['Date_Entered'] = self.df['Date_Entered'].astype({'Date_Entered': 'datetime64[ns]'})
        self.df['Rent_Frequency'] = self.df['Rent_Frequency'].astype('category')
        self.df['views_cleaned'] = self.df['views_cleaned'].astype('int')
        self.df['Rent_Price'] = self.df['Rent_Price'].astype('int')
        return self.df



def kick_off_etl(df):
    """
    function which kicks off the cleaning tasks and returns a cleaned dataframe
    """
    kick_off_class = CLEANER(df)
    kick_off_class.clean_price(df)
    kick_off_class.clean_beds_and_baths(df)
    kick_off_class.remove_useless_rows(df)
    kick_off_class.long_lat_spitting(df)
    kick_off_class.typecasting(df)
    return kick_off_class.df #return the cleaned dataframe from the class


def create_df_for_cleaning(): #gets called from ad_detail_scraper
    """
    Function which is called outside the script to return the cleaned dataframe
    """ 
    df = pd.read_json(myvars.json_output_path,orient='UUID')
    return kick_off_etl(df)  ##return the cleaned dataframe from the class call


# create_df_for_cleaning()