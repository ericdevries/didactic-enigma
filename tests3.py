import boto3

BUCKET_NAME = ''



s3 = boto3.client('s3')
x = s3.generate_presigned_url(
	'put_object', 
	Params={'Bucket': BUCKET_NAME, 'Key':'uploads/5', 'ContentType': 'image/png' }, 
	ExpiresIn=3600, 
)


print(x)
