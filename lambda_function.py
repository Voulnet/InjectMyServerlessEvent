
# Author: Mohammed Aldoub (@Voulnet)
import boto3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)


def lambda_handler(event, context):
    logger.setLevel(logging.DEBUG)
	eventname = event['detail']['eventName']
	requestParameters = event['detail']['requestParameters']

	bucketName = requestParameters.get('bucketName','')
	bucketPolicy = requestParameters.get('bucketPolicy','')
	statement = bucketPolicy.get('Statement', 'nothing')
	Sid = statement[0].get('Sid','nothing')

	logger.debug("Event Name is--- %s" %eventname)
	logger.debug("bucketName is -- %s" %bucketName)
	logger.debug("statement is -- %s" %statement)
	logger.debug("Sid is -- %s" %Sid)
	logger.debug("bucketPolicy is -- %s" %bucketPolicy)
	logger.debug("md5sum of new policy sid: " + os.system("echo "+Sid+" | md5sum"))
