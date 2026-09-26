import boto3

s3 = boto3.client("s3")
# s3 = boto3.resource("s3")
# both work the same but now updated is client keyword

bucket_name = "my-pyt3ndd-devops-bucket-12345"

response = s3.create_bucket(
    Bucket=bucket_name,
)

print(response)