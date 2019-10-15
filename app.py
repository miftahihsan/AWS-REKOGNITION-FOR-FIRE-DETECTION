#!/usr/bin/env python
aws_access_key_id=""
aws_secret_access_key=""
aws_session_token=""

import boto3

class AWS():

    def __rekog__(self, photo):
        # photo = "Kitchen.jpg"

        client = boto3.client('rekognition',
                                aws_access_key_id = aws_access_key_id,
                                aws_secret_access_key = aws_secret_access_key,
                                aws_session_token = aws_session_token)

        with open(photo, 'rb') as source_image:
            final_image = source_image.read()

        response = client.detect_labels(Image={
                'Bytes': final_image
            })

        personFound = False
        personConfidence = 100

        fireFound = False
        fireConfidence = 100

        for x in response["Labels"]:
            
            if(x["Name"] == 'Person'):
                personFound = True
                personConfidence = x["Confidence"]
                if(fireFound):  break
            
            if(x["Name"] == "Bonfire" or x["Name"] == "Fire"):
                fireFound = True
                fireConfidence = x["Confidence"]
                if(personFound): break
        

        return personFound, personConfidence, fireFound, fireConfidence
