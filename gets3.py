import boto3
import pandas as pd

client = boto3.client('s3')

path = 's3://abdullahnaeem/business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv'

df = pd.read_csv(path)

df.to_csv('new.csv', encoding='utf-8')