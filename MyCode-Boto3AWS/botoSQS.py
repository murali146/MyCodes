import boto3
queue_url = 'https://queue.amazonaws.com/691354845604/SQS_QUEUE_NAME'


# Create SQS client
sqs = boto3.client('sqs')

# SQS list all queues
#sqs = boto3.resource('sqs')
#for queue in sqs.queues.all():
#    print(queue.url)



# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])

#3d32decf-89bc-4f49-8ffa-510078630302
