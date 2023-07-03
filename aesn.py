import os, random, struct
from Cryptodome.Cipher import AES 
import boto3
from botocore.client import Config 
import cgi ,os
def encrypt_file( in_filename, key, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv='0123456789abcdef'
    mode = AES.MODE_CBC
    iv=iv.encode('utf8')
    encryptor = AES.new(key.encode('utf8'), mode,iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
    data =open(out_filename, 'rb')
    bname='scstorage'
    s3=boto3.resource(
        service_name='s3',
        aws_access_key_id='AKIA2R2GTHU2XVOPT7UK',
        aws_secret_access_key='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',
        config=Config(signature_version='s3v4')
        )
    s3.Bucket(bname).put_object(Key=in_filename,Body=data)
    print("Your File is Stored ")