import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
print('Retrieving ', url)
urls_read = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(urls_read)
print('Retrieved ', len(urls_read), ' characters')

lst = tree.findall('.//comment')
print('Count: ', len(lst))

numbers = []
for item in lst:
    number = int(item.find('count').text)
    numbers.append(number)
print('Sum: ', sum(numbers))