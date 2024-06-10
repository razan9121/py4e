import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
comments = info.get('comments', [])
print('Count:', len(comments))

total = 0
for comment in comments:
    total += comment['count']

print('Sum:', total)