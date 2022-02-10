# Python script to call AWS SageMaker inference endpoint

from time import sleep
import boto3
import csv
import json

# Inline payload for inference.
payload_inline = '''10844
8000
6210''' 

client = boto3.client('sagemaker-runtime')

endpoint_name = "jumpstart-example-randomforest-2022-02-10-17-48-10"# Endpoint name.
content_type = "text/csv"  # The MIME type of the input data in the request body.
accept = "application/json" # The desired MIME type of the inference in the response.
response = client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType=content_type,
    Accept=accept,
    Body=payload_inline
    )

data = json.loads(response['Body'].read().decode("utf-8"))

print('***Anomaly Scores***')
for d in data['scores']:
    print(d['score'])