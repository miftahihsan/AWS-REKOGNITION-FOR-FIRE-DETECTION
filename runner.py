#!/usr/bin/env python
from app import AWS

aws = AWS()

photo = "KitchenFlame/humanAndFire.jpg"

personFound, personConfidence, fireFound, fireConfidence = aws.__rekog__(photo)

print("Person found = " + str(personFound))
print("Person Confidence = " + str(personConfidence))

print("Fire found = " + str(fireFound))
print("Fire Confidence = " + str(fireConfidence))
