import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-0f58b397bc5c1f2e8',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro'
)

print("EC2 Instance Created")
print("Instance ID:", instances[0].id)