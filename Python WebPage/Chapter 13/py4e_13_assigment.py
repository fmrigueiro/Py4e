import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
sum=0
for span in spans:
    sum=sum+int(span.contents[0])
print(sum)