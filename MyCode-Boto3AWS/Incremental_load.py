import boto3
import re
import os

import subprocess


fistfile=os.utime('firstFile.init',(1330712280, 1330712292))
print fistfile

s3 = boto3.client('s3')
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
OrigBucketExtract = s3.list_objects_v2(Bucket='bktaws146')['Contents']

try:
    nlast = s3.list_objects_v2(Bucket='bkt146')['Contents']
except Exception, e:
    print e
    s3 = boto3.client('s3')
    s3.put_object(Body="InitFile", Bucket='bkt146', Key='firstFile.init')
    nlast = s3.list_objects_v2(Bucket='bkt146')['Contents']


[doneBucketobj['Key'] for doneBucketobj in sorted(nlast, key=get_last_modified)]

print doneBucketobj
print doneBucketobj['LastModified']

DoneFile=doneBucketobj['Key']
Splitfile=DoneFile.split('.Done')
print "Split file to match with orig bucket file" + str(Splitfile)

print "---------------"

for OrigBucket in OrigBucketExtract:

    if OrigBucket['LastModified'] >=doneBucketobj['LastModified'] and OrigBucket["Key"]!=Splitfile:
        s3 = boto3.client('s3')
        if re.search("file1-[0-9]", OrigBucket["Key"]):
            a,b= OrigBucket["Key"].split("-")
            s3.put_object(Body=b, Bucket='bkt146', Key=OrigBucket["Key"]+ ".Done")
            print OrigBucket["Key"] + "   has been copied from source to target bucket"
        else:
            print "File does not have the correct format - Please check"
    else:
        print "File has already been copied Or File format does not match"
