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
import json

from elasticsearch import Elasticsearch

from flask import Flask, jsonify
from flask_cors import CORS
from flask import request


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])

def index():
    return "Welcome to CodezUp"

weather = {
     "data": [
     {
         "day": "1/6/2019",
         "temperature": "23",
         "windspeed": "16",
         "event": "Sunny"
     }
     ]
    }
@app.route('/weatherReport', methods=['GET'])

def weatherReport():
     global weather
     username = request.args.get('query')
     from_record = request.args.get('page')
    
     es = Elasticsearch(
            cloud_id='****',
            http_auth=('****', '****')
        )
     result = es.search(
        index='image_index',
        size = 15,
        from_=from_record,
        query={
            'match': {'description': username}
        }

        )
     print (result['hits']['hits'])
     return jsonify(result['hits']['hits'])
     #return jsonify([weather])

if __name__ == '__main__':
    app.run(debug=True)


exit()


""" My sql connections"""
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ca6005',
  'raise_on_warnings': True
}


es = Elasticsearch(
        cloud_id='My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDBhY2NiZDQzNDIwNjQwN2ZhZTM5YWVmMzMwOGQ2NTMzJDY1N2M3YTMwNmJhMDQzM2Q4N2JiOWZkYmI5NTJjNDY4',
        http_auth=('elastic', '9kDhcs5V3NBkDO0nQNerD9qh')
    )

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
  cursor = cnx.cursor(buffered=True)

"""
result = es.search(
 index='image_index',
  query={
    'match': {'description': 'woman'}
  }

 )
print (result['hits']['hits'])
"""
"""

result = es.search(
 index='image_index',
 match = {
    "query":'woman',
    "fields":['description', 'category', 'alt']
 }
  
 )
print (result['hits']['hits'])

exit()


 document={
  'character': 'Gandalf',
  'quote': 'A wizard is never late, nor is he early.'
 }
"""

query = ("SELECT img.id, img.image_id, cat.category_name, img.description, img.alt, img.url, img.local_url FROM images as img join categories as cat on img.category_id = cat.id")


cursor.execute(query)
records = cursor.fetchall()
documents = []
#save_dir = "E:/DCU/CA6005_2022-20220126T235030Z-001/assignment-2/pexels-api/pexels-api/scrapped_image"
save_dir = "E:/DCU/CA6005_2022-20220126T235030Z-001/angular/angular-11-image-upload-preview/src/assets"

for data in records:
    print (data[0])
    #documents.append({'image_id':data[1], 'category':data[2], 'description':data[3], 'alt':data[4], 'url':data[5]})
    name = str(data[1]) + '.' + data[6].rsplit('.',1)[-1]
    print(name)
    #response = requests.get(data[5])
    #print(response.content)
    #if response.status_code == 200:
    #    with open(save_dir+os.sep+name, 'wb') as f:
    #        f.write(response.content)
    #local = '/assets/'+name
    #sql = "UPDATE images SET local_url = %s WHERE id = %s"
    #val = (local, data[0])
    #cursor.execute(sql, val)
    #cnx.commit()
    #exit()
    
    print(es.index(
         index='image_index',
         document={'image_id':data[1],
            'category':data[2],
            'description':data[3],
            'alt':data[4],
            'url':data[5],
            'local_url':data[6]}))

"""
    
"""
"""

# Type your Pexels API
PEXELS_API_KEY = '563492ad6f9170000100000114de4bd3ff64467e8a28c8828e5f8ac1'
# Create API object
api = API(PEXELS_API_KEY)

save_dir = 'scrapped_image/'
img_names = []
api.collection(page=1, results_per_page=1)
collection = api.get_collection()
for coll in collection:
  print (coll.title)
  data_category = (coll.id, coll.title)
  # Insert new employee
  cursor.execute(add_category, data_category)
  cat_id = cursor.lastrowid
  cnx.commit()
  # Search five 'kitten' photos
  api.search(coll.title, page=1, results_per_page=3)
  # Get photo entries
  photos = api.get_entries()
  # Loop the five photos
  i = 0
  for photo in photos:

        # Insert salary information
    data_image = (photo.id,cat_id,photo.description,photo.alt,photo.original)
    cursor.execute(add_image, data_image)

    # Make sure data is committed to the database
    cnx.commit()
    # Print photographer
    print("Photo description: ", photo.description)
    print("Photo alt: ", photo.alt)
    img_names.append({'id':photo.id, 'description':photo.description, 'url':photo.original})
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
    imageurl = photo.original
    # Filename
    name = str(photo.id) + '.' + imageurl.rsplit('.',1)[-1]
    # Get image and write
    response = requests.get(imageurl)
    if response.status_code == 200:
        with open(save_dir+os.sep+name, 'wb') as f:
            f.write(response.content)
  i+=1
print(i)
cursor.close()
cnx.close()

with open('E:/DCU/CA6005_2022-20220126T235030Z-001/assignment-2/pexels-api/pexels-api/response.txt', 'w') as w:
    w.writelines(f"{img_names} \n")
    """
