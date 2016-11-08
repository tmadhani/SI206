# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
import re
from bs4 import BeautifulSoup


base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

x = soup.find_all(text = re.compile('student'))
for word in x:
    new_txt = str(word).replace('student', 'AMAZING student')
    word.replace_with(new_txt)

for item in soup.findAll('iframe'):
	item['src'] = "/Users/tmadhani/desktop/SI206/HW3-StudentCopy/LilBub.jpg"

for item in soup.findAll('img'):
	item['src'] = "/Users/tmadhani/desktop/SI206/HW3-StudentCopy/media/logo.png"

text_file = open("bshw3.html", "w")
text_file.write(str(soup))
text_file.close()
print('Done')

# <a href="http://example.com/">I linked to <b>example.net</b></a>
