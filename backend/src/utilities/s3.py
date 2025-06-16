import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os


load_dotenv()
bucketName = os.getenv("bucket")


def uploadFileToS3(fileObject, fileName):
    extension = fileName.split(".")[-1]

    objectName = os.urandom(15).hex()
    objectName = f"test/{objectName}.{extension}"

    s3Client = boto3.client('s3')

    try:
        response = s3Client.upload_fileobj(fileObject, bucketName, objectName)
    except ClientError as err:
        print("Failed to upload file to S3: ", err)
        return False
    return objectName