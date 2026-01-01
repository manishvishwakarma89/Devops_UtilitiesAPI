import boto3
from datetime import datetime, timezone,timedelta

def get_bucket_info():
    s3_client = boto3.client('s3')
    buckets = s3_client.list_buckets()['Buckets']
    current_date= datetime.now(timezone.utc).astimezone()
    new_buckets = []
    old_buckets = []
    for bucket in buckets:
        creation_date = bucket['CreationDate'].astimezone()
        age_days = (current_date - creation_date).days
        bucket_info = {
            "name": bucket['Name'],
            "creation_date": creation_date.isoformat(),
            "age_days": age_days
        }
        if age_days <= 30:
            new_buckets.append(bucket_info)
        else:
            old_buckets.append(bucket_info)
    return {
        "total_buckets": len(buckets),
        "new_buckets": len(new_buckets),
        "old_buckets": len(old_buckets) ,
        "new_buckets_details": new_buckets,
        "old_buckets_details": old_buckets
    }

def get_ec2_instance_info():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()