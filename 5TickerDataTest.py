import os
import google.cloud
import pandas as pd
import requests
from google.cloud import bigquery
from google.cloud import storage as stg
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/Users/francois/Desktop/Google Could API/connectapiproject-17992e7f655b.json')

project_id = 'connectapiproject'
client = bigquery.Client(credentials = credentials, project = project_id)

query_job = client.query("""
    SELECT *
    FROM fivetickertest.testticker
    LIMIT 1000 """)

results = query_job.result()

print(results)

dataframe = (
    client.query(query_job)
    .result()
)
print(dataframe.head())