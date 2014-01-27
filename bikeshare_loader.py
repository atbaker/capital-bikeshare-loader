#!/usr/bin/python

import argparse
import time
import csv
import MySQLdb

# MySQL settings
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = 49158
MYSQL_DATABASE = 'bikeshare'

parser = argparse.ArgumentParser(description='Insert data from Capital Bikeshare ride data .csv files into a MySQL database')
parser.add_argument('csvfile', metavar='csvfile', type=file,
                   help='Capital Bikeshare data .csv file')

def load_mysql_data(csv_file):

    reader = csv.reader(csv_file)

    mydb = MySQLdb.connect(host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        port=MYSQL_PORT,
        db=MYSQL_DATABASE)
    cursor = mydb.cursor()

    # Discard the header rows
    reader.next()

    counter = 0

    for row in reader:
        # Fix the start
        start = row[1]
        start = time.strptime(start, "%m/%d/%Y %H:%M")
        row[1] = time.strftime("%Y-%m-%d %H:%M", start)

        # Fix the end
        end = row[4]
        end = time.strptime(end, "%m/%d/%Y %H:%M")
        row[4] = time.strftime("%Y-%m-%d %H:%M", end)

        # Fix the duration
        duration = row[0].split()
        hours = int(duration[0][:-1])
        minutes = int(duration[1][:-1])
        seconds = int(duration[2][:-1])
        duration = (hours * 60 * 60) + (minutes * 60) + seconds
        row[0] = str(duration)

        values = '"' + '", "'.join(row) + '"'

        try:
            cursor.execute("INSERT INTO ride (duration, start_date, start_station, start_terminal, end_date, end_station, end_terminal, bike_number, subscription_type) VALUES (%s)" % values)
        except Exception:
            import pdb; pdb.set_trace()

        counter += 1

        if counter % 500 == 0:
            print "Processed %s records. Committing." % counter
            mydb.commit()

    mydb.commit()
    cursor.close()
    csv_file.close()

    return counter

if __name__ == "__main__":
    args = parser.parse_args()
    counter = load_mysql_data(args.csvfile)
    print "Inserted %s rows" % counter

