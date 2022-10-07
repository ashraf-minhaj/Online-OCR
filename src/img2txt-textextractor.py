""" detect texts in an image using AWS Rekognition
 
 author: asrhaf minhaj
 mail  : ashraf_minhaj@yahoo.com

doc: https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html 
"""

import json
import boto3
import logging

# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):

    texts = 'unable to find anything'
    stat = 422

    # log event
    logger.info(event)

    # image object
    # get input bucket
    input_bucket_name = event['Records'][0]['s3']['bucket']['name']
    logger.info("Input bucket:")
    logger.info(input_bucket_name)

    # get file/object name
    media_object = event['Records'][0]['s3']['object']['key']
    logger.info('media object:')
    logger.info(media_object)

    # create Reokognition client
    logger.info("Connecting with rekognition..")
    rekognition_client = boto3.client('rekognition', region_name='ap-south-1')
    logger.info("..success")

    # get image: aws example code
    response = rekognition_client.detect_text(
        Image={
            'S3Object':{
                'Bucket':input_bucket_name,
                'Name':media_object
                }
            }
        )
                        
    textDetections = response['TextDetections']
    # logger.info('Detected text\n----------')

    logger.info(textDetections)
    if textDetections:
        logger.info("Text Found")
        texts = ''

        for text in textDetections:
                # print ('Detected text:' + text['DetectedText'])
                texts +=  text['DetectedText'] + ' '
                # print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                # print ('Id: {}'.format(text['Id']))
                # if 'ParentId' in text:
                #     print ('Parent Id: {}'.format(text['ParentId']))
                # print ('Type:' + text['Type'])
                # print()

    logger.info("Detected text: ")
    logger.info(texts)

    return {
        'statusCode': stat,
        'body': json.dumps(texts)
    }
