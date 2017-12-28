
import boto3
import botocore

# Create bucket
s3 = boto3.client('s3')
s3.create_bucket(Bucket='bktaws146')

s3 = boto3.client('s3')

filename = 'runtime_script.txt'
bucket_name = 'bktaws146'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)

result = s3.get_bucket_acl(Bucket='bktaws146')
print "result -  " + str(result)


#BUCKET_NAME = 'bktaws146'  # replace with your bucket name
#KEY = 'runtime_script.txt'  # replace with your object key

s3 = boto3.resource('s3')
try:
    s3.Bucket(bucket_name).download_file(filename, 'runtime_script.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

print "Executed Successfully"
exit(0)