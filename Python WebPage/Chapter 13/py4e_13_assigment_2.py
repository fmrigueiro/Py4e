import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
for i in range(4):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	count = 0
	for tag in tags:
		count = count + 1
		# make it stop at position 3#
		if count > 3:
			break
		url = tag.get('href', None)
	print(url)

url = "http://py4e-data.dr-chuck.net/known_by_Avya.html"
print('Enter url: ', url)
print('Enter count: ', 7)
print('Enter position: ', 8)
for i in range(7):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	count = 0
	for tag in tags:
		count = count + 1
		# make it stop at position 3#
		if count > 18:
			break
		url = tag.get('href', None)
	print(url)