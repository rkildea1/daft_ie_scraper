# daft_ie_scraper

Files Summary: 

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


## **Run-Flow**
```
Running order
├── main.py
│   ├── link_list_generator.py
│   │   ├── rds_connector.py
│   │   │   ├── variables.py
│   │   │   │   ├──load-env.py
│   │   │   │   │   ├──.env
│   │   │   │   │   │


```