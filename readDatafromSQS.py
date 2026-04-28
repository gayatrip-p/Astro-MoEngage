import boto3 #Import Library

queue_url = "https://sqs.ap-south-1.amazonaws.com/957614586613/moengage-astro-sqs-dev" #Queue URL

sqs = boto3.client('sqs', region_name='ap-south-1') #Connects to SQS service

message_count = 0 #Stores total number of messages

while True: #Keep checking queue until empty
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )   #Get max 10 messages at a time, Wait up to 2 seconds

    messages = response.get("Messages", []) #If messages exist → store, If not → empty list

    if not messages:
        break #If messages exist → store, If not → empty list

    message_count += len(messages) #Add number of messages received

    # Delete messages after reading (optional)
    #Removes message from queue after reading
    #Prevents reading same message again
    for msg in messages:
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=msg['ReceiptHandle']
        )

print("Total messages received:", message_count) #Shows total messages count