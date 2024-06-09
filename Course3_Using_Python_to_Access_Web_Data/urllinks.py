# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    # Check if the position is valid
    if len(tags) < position:
        print("Position out of range. Exiting.")
        break

    for tag in tags:
        # Find the link at the specified position (1-based index)
        tag = tags[position - 1]
        url = tag.get('href', None)

        # Extract the name (contents) of the link
        name = tag.contents[0]
        
    print(f"Retrieving: {url} (name: {name})")

print(f"The final URL is: {url}")
print(f"The final name found is: {name}")