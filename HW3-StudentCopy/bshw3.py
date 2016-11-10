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
    new_word = str(word).replace('student', 'AMAZING student')
    word.replace_with(new_word)
#iterates through each word in 'x,' which compiled all mentions of word 'student' and replaces it with 'AMAZING student'

for item in soup.find_all('iframe'):
	item['src'] = "/Users/tmadhani/desktop/SI206/HW3-StudentCopy/media/propic.jpg"
#finds iframe/video in the html page and replaces it with an image of me from my folder

for item in soup.find_all('img'):
	item['src'] = "/Users/tmadhani/desktop/SI206/HW3-StudentCopy/media/logo.png"
#finds all images in the html page and replaces it with the UMSI logo Colleen provided

f = open("bshw3.html", "w")
f.write(str(soup))
f.close()
print('Success!')
#creates new html file and writes all code from above into said file
