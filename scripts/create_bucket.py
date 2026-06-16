import boto3

s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'mycap-project-4-bucket'

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print(f"Bucket {bucket_name} created successfully!")
