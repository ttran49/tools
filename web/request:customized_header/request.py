#!/usr/bin/python

import requests

url="http://165.227.106.113/header.php"

'''
Resources: https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
'''

#headers={'user-agent': 'Sup3rS3cr3tAg3nt', 'referer': 'awesomesauce.com'}

re = requests.get(url, headers={'user-agent': 'Sup3rS3cr3tAg3nt','referer': 'awesomesauce.com'})

print re.text
