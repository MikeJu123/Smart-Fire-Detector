import json
import boto3
import time
import os

def lambda_handler(event, context):
	key = 'testdata.txt'
	# key = 'labnofiredata/sensordata'+  str(time.time())+ '.txt'
	writeToS3(key, event)
	return True

def writeToS3(key,value):
	s3 = boto3.resource('s3')
	s3.Bucket('ee542temperatureflowdata').put_object(Key=key,Body=value)
	return