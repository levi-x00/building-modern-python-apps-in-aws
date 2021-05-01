'''
	You must replace <bucket-name> with your bucket name and <region> with your own region
'''
import boto3
import json
import os

S3API = boto3.client("s3", region_name="<region>") 
bucket_name = "<bucket-name>"

policy_file = open(f"{os.getcwd()}/bucket_policy.json", "r")

S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")