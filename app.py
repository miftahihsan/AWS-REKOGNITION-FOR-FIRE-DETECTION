#!/usr/bin/env python
aws_access_key_id="ASIAVKUIDNMSYJ46LL3I"
aws_secret_access_key="oL1rK12ZkSwjenrOy2FojYQAuCnKwgrxlHIEWF4L"
aws_session_token="FQoGZXIvYXdzEKz//////////wEaDHFN7pYV9xHe2n5veSKUA/ECua9wBOht2rQpcUnuKx1L3Omwcrnkj5mqxD+s8LLl9pAjePUjvJmaV0gq38XuL5KOlxrSi9KzGP6ULcZSG6B0xgJx+EWL+LxcMqrrntNYd+PIz150zN+yak36SgHNGBarl/CJqoktyr6SF43oydWE7cAYK6uvgu1b/ue4pyAZruJjmcrSybLDUm26WlUCZBtR+n9Fcy34ibCjevsgcAF11Ge7GGvK2RFwsEzkXarC7hDxw+/gYBLdMV9Z4QE5vrdELJbpTejt6J9KF79cwxbAdZ8FvZk6kW76224+NFGK3wQmhOShNtpXCmYMRGUgSumTWGpaO1xXjUgA5fvqDwTqQrdLer2EujCY9H8DLjEGuvKwVF5cXtK53Bmd0Y191NmNllPel/eqjGi7mmcgoJbmmwCZQ7mTjpItZSzMjuiHenZ8qjG+FlwphT/KM21+hwIhGQDyDBj28/zbWqLI1qBOXaKDFMW18V4qRoMIS7NGweb86BEpKkosdZiT/WLbBDCGFYDI8rUpFDB8oGkEHh0opOSvKNfmrekF"


import boto3

photo = "Kitchen.jpg"

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

for x in response["Labels"]:
    if(x["Name"] == 'Person'):
        personFound = True
        print(x['Name'])
        print(x['Confidence'])
        break

if not personFound:
    print("No Person Found")


print("HELLO")