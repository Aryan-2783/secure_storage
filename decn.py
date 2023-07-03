import boto3
from botocore.client import Config 
import os, random, struct
from Cryptodome.Cipher import AES 
import cgi,os 
def decrypt_file(key, nin_filename, out_filename=None, chunksize=24*1024):
    bname='scstorage'
    BUCKET_NAME ='scstorage'
    NEW_NAME='download1.pdf'
    s3 = boto3.client( service_name='s3',
        aws_access_key_id='AKIA2R2GTHU2XVOPT7UK',
        aws_secret_access_key='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',
        config=Config(signature_version='s3v4'))
    s3.download_file(BUCKET_NAME,nin_filename,NEW_NAME)
    if not out_filename:
        out_filename = os.path.splitext(NEW_NAME)[0]

    with open(NEW_NAME, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        mode = AES.MODE_CBC
        iv='0123456789abcdef'
        iv=iv.encode('utf8')
        decryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    print("downloaded")