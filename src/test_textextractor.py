""" Test online ocr img2txt code.

 This uses two events with objects that has text and other does not.

 author: ashraf minhaj
 mail  : ashraf_minhaj@yahoo.com
"""

# importlib, because python has issues with dash '-' in module names
import importlib
img2txt = importlib.import_module("img2txt-textextractor")

event_with_txt = {
    'Records': [{
        'eventVersion': '2.0', 
        'eventSource': 'aws:s3', 
        'awsRegion': 'ap-south-1', 
        'eventTime': '1970-01-01T00:00:00.000Z', 
        'eventName': 'ObjectCreated:Put', 
        'userIdentity': {
            'principalId': 'EXAMPLE'
            }, 
        'requestParameters': {
            'sourceIPAddress': '127.0.0.1'
            }, 
        'responseElements': {
            'x-amz-request-id': 'EXAMPLE123456789', 
            'x-amz-id-2': 'EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH'
            }, 
        's3': {
            's3SchemaVersion': '1.0', 
            'configurationId': 'testConfigRule', 
            'bucket': {
                'name': 'img2txt-images', 
                'ownerIdentity': {
                    'principalId': 'EXAMPLE'
                    }, 
                'arn': 'arn:aws:s3:::img2txt-images'
                }, 
        'object': {
            'key': 'test_img.png', 
            'size': 1024, 
            'eTag': '0123456789abcdef0123456789abcdef', 
            'sequencer': '0A1B2C3D4E5F678901'
            }
        }
    }
]}

event_with_no_txt = {
    'Records': [{
        'eventVersion': '2.0', 
        'eventSource': 'aws:s3', 
        'awsRegion': 'ap-south-1', 
        'eventTime': '1970-01-01T00:00:00.000Z', 
        'eventName': 'ObjectCreated:Put', 
        'userIdentity': {
            'principalId': 'EXAMPLE'
            }, 
        'requestParameters': {
            'sourceIPAddress': '127.0.0.1'
            }, 
        'responseElements': {
            'x-amz-request-id': 'EXAMPLE123456789', 
            'x-amz-id-2': 'EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH'
            }, 
        's3': {
            's3SchemaVersion': '1.0', 
            'configurationId': 'testConfigRule', 
            'bucket': {
                'name': 'img2txt-images', 
                'ownerIdentity': {
                    'principalId': 'EXAMPLE'
                    }, 
                'arn': 'arn:aws:s3:::img2txt-images'
                }, 
        'object': {
            'key': 'test_img2.png', 
            'size': 1024, 
            'eTag': '0123456789abcdef0123456789abcdef', 
            'sequencer': '0A1B2C3D4E5F678901'
            }
        }
    }
]}


def test_detected_text():
    response = img2txt.handler(event=event_with_txt, context='')
    assert response["body"] == '"Detect Me If You Can. Detect Me If You Can. "'
    # print(response)

def test_no_text():
    response = img2txt.handler(event=event_with_no_txt, context='')
    assert response["body"] == '"unable to find anything"'
    # print(response)
