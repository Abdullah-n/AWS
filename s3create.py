import boto3
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime

d= datetime.datetime.now()

current_time="{}{}{}".format(d.month,d.day,d.year)

client=boto3.client('s3')

with open("image.png",'rb') as f:
    data = f.reead()

#creating buckets
bucket = s3.create_bucket(
    ACL='private',
    Bucket='string',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)

#putting objects in buckets
response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='abdullahnaeem',
    Key= 'image.png'
)

#delete objects from bucket
response = bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'image.png',
            },
        ],
        'Quiet': True|False
    },
   
)

#list the objects in the bucket 
response = client.list_objects(
    Bucket='abdullahnaeem',
    Delimiter='string',
    EncodingType='url',
    Marker='string',
    MaxKeys=123,
    Prefix='string',
    RequestPayer='requester',
    ExpectedBucketOwner='string'
)
for x in response.get("Contents,None"):
    print(x.get("Key",None))



#list the buckets 
response = client.list_buckets()
for x in response.get("Buckets",None):
    print (x.get("Name",None))
    
    