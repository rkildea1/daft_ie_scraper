# daft_ie_scraper


## App Summary

- App goes to the `for-rent` section of daft and grabs various datapoints from each of the advertised properties. Cleans the datapoints and loads them into an RDS MySQL database. Takes the original datapoints and loads them into an S3 bucket. It also captures the primary photo from all advetisements and stores them in an S3 bucket. Repo includes a docker  docker compose 



## Files Summary: 

- ad_detail_scraper.py
    - This scripts is the central ETL script which triggers the other scripts
- file_handler.py
    - Various methods for extracting/ writing files
- link_list_generator.py
     - Collect all SERP hrefs with `for-rent` in the url and store locally in a csv  
- load_env.py
    - Used in default manner to leverage .env hidden variables
- rds_connector.py
    - Various methods to connect and manage a MySQL database
- s3_manager.py
    - Connect to and manage s3 
- scraper_configurations.py 
    - Includes the configurations for scraping the various datapoints    
- transformer.py
    - Cleaning methods and function
- variables.py
    - Reference to shared variables



## **Required .env File Variables**
    * aws_access_key_id=YOUR_AWS_ACCESS_KEY_ID
    * aws_secret_access_key=YOUR_AWS_SECRET_ACCESS_KEY
    * s3_bucket_name=S3_BUCKET_NAME_YOU_WANT_TO_CREATE
    * RDS_TABLENAME=RDS_TABLENAME
    * RDS_PASSWORD=RDS_PASSWORD
    * RDS_HOST=RDS_HOST
    * RDS_USER=RDS_USER
    * RDS_DATABASENAME=RDS_DATABASENAME


