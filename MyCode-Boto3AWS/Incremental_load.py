import boto3
import re


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

    source= { 'Bucket' : 'bktaws146','Key':js["Key"]}
    dest ={ 'Bucket' : 'bkt146','Key':js["Key"]}
    copy_source = {
        'Bucket': 'bktaws146',
        'Key': js["Key"]
    }
    if js['LastModified'] >=obj['LastModified']:
        s3 = boto3.client('s3')
        a,b= js["Key"].split("-")
        print a
        print b
        m = re.search("file2-[0-9]",js["Key"])
        if m is not None:
            s3.put_object(Body=b, Bucket='bkt146', Key=js["Key"]+ ".Done")
            print js["Key"] + "   has been copied from source to target bucket"
        else:
            print "File of given format is not available"