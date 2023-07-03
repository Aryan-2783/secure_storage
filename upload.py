import boto3
from botocore.client import Config 

bname='scstorage'
def fileonaws(file_name): 
    data =open(file_name, 'rb')
    s3=boto3.resource(
        service_name='s3',
        aws_access_key_id='AKIA2R2GTHU2XVOPT7UK',
        aws_secret_access_key='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',
        config=Config(signature_version='s3v4')
        )
    s3.Bucket(bname).put_object(Key=file_name,Body=data)  
fileonaws('Amazon_6_months.pdf')