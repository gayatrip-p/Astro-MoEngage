import boto3
import json

s3 = boto3.client(
    's3',
    region_name='ap-south-1',
    aws_access_key_id='YOUR_KEY',
    aws_secret_access_key='YOUR_SECRET'
)

bucket_name = "your-bucket-name"
file_key = "path/to/your/file.json"

response = s3.get_object(
    Bucket=bucket_name,
    Key=file_key
)

data = response['Body'].read().decode('utf-8')

# Convert JSON string → Python object
records = json.loads(data)

print("Total records:", len(records))