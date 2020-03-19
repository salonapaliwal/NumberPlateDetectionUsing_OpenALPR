#!/usr/bin/python
import requests
import base64
import json
import sys


# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
IMAGE_PATH = 'D:\PROJECT(NUMBER_PLATE)/image1.jpg'
SECRET_KEY = 'sk_cd9c6a7e2d71bb1e1aa57590'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=ind&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data=img_base64)
# nump = urllib2.urlopen(url)
jdata = json.dumps(r.json(), indent=1)
jdata1 = str(json.loads(jdata))
s = []
s = jdata1.split('[')
s4 = []
s4 = s[1].split(']')
if (s4[0] == ''):
    print("number plate not detected")
# print(s[1])
else:
    s1 = []
    s1 = s[1].split(':')
    # print(s1[1])
    s2 = []
    s5 = []
    s6 = []
    s2 = s1[1].split(',')
    s3 = s2[0].split("'")
    s5 = s1[2].split(",")
    con = s5[0]
    confidence = float(con)
    if (confidence >= 65.0):
        # print(s3[1])
        # numdata.Insert(13,s3[1],"img.jpg",numdata.st1,numdata.st,"n")

        print(str(s3[1]) + " " + str(confidence))