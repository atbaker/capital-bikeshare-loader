capital-bikeshare-loader
========================

Loads data from Capital Bikeshare ride data .csv files into a MySQL database with a Python script.

Capital Bikeshare .csv files are available at: http://capitalbikeshare.com/trip-history-data

# Get started

1. Use the `ride_ddl.sql` script to add the `ride` table to your database
1. Update the `MySQL settings` section in `bikeshare_loader.py` to work with your connection
1. Run `**python bikeshare_loader.py** 2013-1st-quarter.csv`, with the path to your CSV file

The script will commit after every 500 rows inserted. Enjoy!

# Implementation details

- This script will always add rows to the `ride` table - useful for loading multiple CSV files
- The `duration` field is converted into seconds on import
- The table includes an auto-incremented `id` field as the primary key, and an index on `bike_number`
