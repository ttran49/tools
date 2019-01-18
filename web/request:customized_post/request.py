#! /usr/bin/python

import requests

url="http://165.227.106.113/post.php"


re= requests.post(url, data={'username':'admin','password':'71urlkufpsdnlkadsf'})

print re.text