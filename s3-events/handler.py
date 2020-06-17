import json
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')

def hello(event, context):

    files =[]
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        files.append(key)
        # tmpkey = key.replace('/', '')
        # download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        # upload_path = '/tmp/resized-{}'.format(tmpkey)
        # s3_client.download_file(bucket, key, download_path)
        # s3_client.upload_file(upload_path, '{}-resized'.format(bucket), key)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": files
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
