import boto3
myec2 = boto3.resource(
			service_name = "ec2",
			region_name = "region_name",
			aws_access_key_id = "access-key",
			aws_secret_access_key = "secret-key"
)

def os_launch():
	myec2.create_instances(
		InstanceType = "t2.micro",
		ImageId = "ami-id",
		MaxCount = 1,
		MinCount = 1
	)


os_launch()