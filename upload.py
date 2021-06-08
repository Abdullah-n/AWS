import os
import sys
import datetime
import time
import boto3

db = boto3.resource('dynamodb')
table=db.Table("employees")



table.put_item(
    Item={
        'emp_id':"1",
        'name':"Saad Iqbal",
        'age':"23"
    }
)
