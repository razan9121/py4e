import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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

tree = ET.fromstring(data)
counts = tree.findall('.//count')

count = len(counts)
total = 0

# Iterate over each 'count' element
for item in counts:
    # Directly access the 'text' of 'item'
    count_text = item.text
    if count_text is not None:
        total += int(count_text)

print('Count:', count)
print('Sum:', total)