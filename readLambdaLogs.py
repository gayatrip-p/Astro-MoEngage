import boto3

client = boto3.client('logs', region_name='ap-south-1')

log_group = '/aws/lambda/moengage-astro-ingest_sqs_lambda_s3-dev'

response = client.describe_log_streams(
    logGroupName=log_group,
    orderBy='LastEventTime',
    descending=True,
    limit=1
)

log_stream = response['logStreams'][0]['logStreamName']

events = client.get_log_events(
    logGroupName=log_group,
    logStreamName=log_stream,
    limit=10
)

for event in events['events']:
    print(event['message'])