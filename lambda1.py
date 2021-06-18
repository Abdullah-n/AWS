import json
import boto3

client = boto3.client("lambda")

def lambda_handler(event, context):
    message = {"message":"Hello from Lambda 1"}

    response = client.invoke(
        FunctionName='arn:aws:lambda:us-east-2:491031845645:function:lambda2',
        InvocationType='RequestResponse',
        Payload=json.dumps(message),
        
    )   

    print(response)
    return {
        'statusCode':200,
        'body': json.dumps('Hello from Lambda!')
    }