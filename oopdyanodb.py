import os
import sys
import datetime
import time
import boto3

class MyDB(object):
    def __init__(self,Table_name='Teachers'):
        self.Table_name=Table_name
        self.db=boto3.resource('dynamodb')
        self.table=self.db.Table(Table_name)
        self.client=boto3.client('dynamodb')
    
    def get(self):
        response=self.table.get_item(
            Key={
                'id':"2"
            }
        )
        print(response)
    
    def put(self):
        self.table.put_item(
            Item={
                'id':"2",
                'name':"Saad Iqbal",
                'age':"24"
            }
        )
    
    @property
    def delete(self):
        self.table.delete_item(
            Key={
                'id':"2"
            }
        )
    
    def describe_table(self):
        response = self.client.describe_table(
            TableName='Teachers'
        )
        return response
    
obj=MyDB()
print(obj.describe_table())
obj.put()
obj.get()