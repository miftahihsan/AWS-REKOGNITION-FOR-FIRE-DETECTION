#!/usr/bin/env python
aws_access_key_id="ASIAVKUIDNMS4LMWXOAW"
aws_secret_access_key="uvVkF4gW7k9d0Smdx/prGMleB7avvzOegMFgU23R"
aws_session_token="FQoGZXIvYXdzEOz//////////wEaDCokCNQmJ3FyEHqiVCKUAwNbtNkSgFhkjkSFQUvE3A6F+KndjuVGiu+4i0oa1Y7ajMGd7jL7SLKb93OM0ejdqQn4RhTDKHNFBrX51VfFbUCKUuJmatCDhNTYBSJPq5J2pUCp/bJ5bPphicNrmDmRv+xn7JDBiHOoRp8+KsCwq5x0yxZjvGwpsN819eU02Olj/AqOaxAwfktUBxSuGXOsQ42XRu8OjgJOT+qH+KP7pHQ0CwK/RmA3MKjIzjg8aEVZ2opLmVPxa/XjHVo/LuVl/Xr+d4n3Xsvo+gFJpx+dtn1BUxe61EiQLH004Wx/5VnsPRuu4NWMWb0w+FXFfhKU+6u9afjqasqk+R/9osCaEDBFXjMskxkc3COygil8tTLFp/YwYwXHiyGCIQEa2VIuI5bebf4cY5ZrdKnArnxaOGry4p3n+FTXTjn4035NUuIhFSQtK35zAQ7wofXMfTxStBIy1mdcFlY5JiRj3fNPpmIUCAwFfomZe/96I16Qvmxx5KqkJIXU4Ki04WMLCvhy8E6LTjvtgdL3U58nPx8nN1lPC34WKPbyu+kF"


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