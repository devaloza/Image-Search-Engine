# Import API class from pexels_api package
from pexels_api import API
import os
import math
import argparse
import requests
from pathlib import Path
import mysql.connector

import mysql.connector
from mysql.connector import errorcode


config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ca6005',
  'raise_on_warnings': True
}

try:
  #cnx = mysql.connector.connect(user='scott',
  #                              database='employ')
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  #cnx.close()
  cursor = cnx.cursor()


TABLES = {}
TABLES['categories'] = (
    "CREATE TABLE `categories` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `category_id` varchar(100) NOT NULL,"
    "  `category_name` varchar(500) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['images'] = (
    "CREATE TABLE `images` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `image_id` int(11) NOT NULL,"
    "  `category_id` int(11) NOT NULL,"
    "  `description` varchar(500),"
    "  `alt` varchar(500),"
    "  `url` text NOT NULL,"
    "  `local_url` text NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`category_id`) "
    "     REFERENCES `categories` (`id`)"    
    ") ENGINE=InnoDB")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

add_category = ("INSERT INTO categories "
               "(category_id, category_name) "
               "VALUES (%s, %s)")

add_image = ("INSERT INTO images "
               "(image_id, category_id, description, alt, url, local_url) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

# Type your Pexels API
PEXELS_API_KEY = '563492ad6f9170000100000114de4bd3ff64467e8a28c8828e5f8ac1'
# Create API object
api = API(PEXELS_API_KEY)

#save_dir = 'scrapped_image/'
#save_dir = "E:/DCU/CA6005_2022-20220126T235030Z-001/assignment-2/pexels-api/pexels-api/scrapped_image/"
save_dir = "E:/DCU/CA6005_2022-20220126T235030Z-001/angular/angular-11-image-upload-preview/src/assets"
img_names = []
api.collection(page=1, results_per_page=80)
collection = api.get_collection()
for coll in collection:
  print (coll.title)
  data_category = (coll.id, coll.title)
  # Insert new employee
  cursor.execute(add_category, data_category)
  cat_id = cursor.lastrowid
  cnx.commit()
  # Search five 'kitten' photos
  page = 1
  while page < 3:
    api.search(coll.title, page=f"{page}", results_per_page=80)
    # Get photo entries
    photos = api.get_entries()
    # Loop the five photos
    i = 0
    for photo in photos:

      # Insert salary information
      imageurl = photo.original
      # Filename
      name = str(photo.id) + '.' + imageurl.rsplit('.',1)[-1]
      print (save_dir+os.sep+name)
      #data_image = (photo.id,cat_id,photo.description,photo.alt,photo.medium,save_dir+os.sep+name)
      data_image = (photo.id,cat_id,photo.description,photo.alt,photo.medium,'/assets/'+name)
      cursor.execute(add_image, data_image)

      # Make sure data is committed to the database
      cnx.commit()
      # Print photographer
      print("Photo description: ", photo.description)
      print("Photo alt: ", photo.alt)
      img_names.append({'id':photo.id, 'description':photo.description, 'url':photo.medium})
      #print(photo)
      print("Photo description: ", photo.description)
      print("Photo id: ", photo.id)
      print("Photo width: ", photo.width)
      print("Photo height: ", photo.height)
      print("Photo url: ", photo.url)
      print("Photographer: ", photo.photographer)
      print("Photo description: ", photo.description)
      print("Photo extension: ", photo.extension)
      print("Photo sizes:")
      print("\toriginal: ", photo.original)
      print("\tcompressed: ", photo.compressed)
      print("\tlarge2x: ", photo.large2x)
      print("\tlarge: ", photo.large)
      print("\tmedium: ", photo.medium)
      print("\tsmall: ", photo.small)
      print("\ttiny: ", photo.tiny)
      print("\tportrait: ", photo.portrait)
      print("\tlandscape: ", photo.landscape)
      # Get image and write
      response = requests.get(photo.medium)
      if response.status_code == 200:
          with open(save_dir+os.sep+name, 'wb') as f:
              f.write(response.content)
    page+=1
print(i)
cursor.close()
cnx.close()

with open('E:/DCU/CA6005_2022-20220126T235030Z-001/assignment-2/pexels-api/pexels-api/response.txt', 'w') as w:
    w.writelines(f"{img_names} \n")