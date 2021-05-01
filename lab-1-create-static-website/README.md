# Lab-1 Deploy S3 Static Website

## Setup
Setup AWS CLI profile, for this case we setup default profile, furthermore check this link:
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

Create S3 bucket with the following command.
```sh
aws s3api create-bucket --bucket <bucket-name> --region <region> --create-bucket-configuration LocationConstraint=<region>
```
Create json file (e.g bucket_policy.json) Use the following for bucket policy. Use whatismyip.com to get your public IP address.
```json
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::<bucket-name>/*",
                "arn:aws:s3:::<bucket-name>"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": [
                        "<your-public-ip>/32"
                    ]
                }
            }
        },
        {
            "Sid": "DenyOneObjectIfRequestNotSigned",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<bucket-name>/report.html",
            "Condition": {
                "StringNotEquals": {
                    "s3:authtype": "REST-QUERY-STRING"
                }
            }
        }
    ]
}
```
Install the dependencies.
```sh
sudo pip3 install boto3
```
Update the permissions.py script.
```python
.......
S3API = boto3.client("s3", region_name="<region>") 
bucket_name = "<bucket-name>"
.......
```

Put the bucket permission.

```sh
python permissions.py
```
Update the upload_items.py script.
```python
.......
S3API = boto3.client("s3", region_name="<region>") 
bucket_name = "<bucket-name>"
.......
```

Upload the website.

```sh
python upload_items.py
```

Try to access the website.
```sh
https://<bucket-name>.s3-<region>.amazonaws.com/index.html
```
Lab complete :)
