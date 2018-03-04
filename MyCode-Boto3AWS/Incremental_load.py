import boto3
import json
from datetime import datetime
import pandas as pd


s3 = boto3.client('s3')
s4 = boto3.resource('s3')
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
objs = s3.list_objects_v2(Bucket='bktaws146')['Contents']

nlast = s3.list_objects_v2(Bucket='bkt146')['Contents']
[obj['Key'] for obj in sorted(nlast, key=get_last_modified)]
print obj
print obj['LastModified']

print "---------------"

for js in objs:
    #print js['LastModified']
    source= { 'Bucket' : 'bktaws146','Key':js["Key"]}
    dest ={ 'Bucket' : 'bkt146','Key':js["Key"]}
    copy_source = {
        'Bucket': 'bktaws146',
        'Key': js["Key"]
    }
#    print pd.to_datetime('2018-03-04 09:30:13+00:00')
#    latestTime=str(pd.to_datetime('2018-03-04 09:30:13+00:00'))+ "+00:00"

    print "Murali"
    print pd.to_datetime(obj['LastModified'])
    print pd.to_datetime(js['LastModified'])
    print "ABC"
    if js['LastModified'] >=obj['LastModified']:
        s3 = boto3.client('s3')
        s3.put_object(Bucket='bkt146', Key=js["Key"]+ ".Done")
        #s4.meta.client.copy(copy_source,'bkt146',split(js["Key"]+".Done")
        print js["Key"] + "   has been copied from source to target bucket"

#bkt146