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



""" Elasticsearch connection"""
es = Elasticsearch(
    cloud_id='My_deployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDBhY2NiZDQzNDIwNjQwN2ZhZTM5YWVmMzMwOGQ2NTMzJDY1N2M3YTMwNmJhMDQzM2Q4N2JiOWZkYmI5NTJjNDY4',
    http_auth=('elastic', '9kDhcs5V3NBkDO0nQNerD9qh')
)



""" My sql connections"""
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'ca6005',
  'raise_on_warnings': True
}

result = es.search(
 index='image_index',
  query={
    'match': {'description': 'woman'}
  }

 )
print (result['hits']['hits'])
exit()




