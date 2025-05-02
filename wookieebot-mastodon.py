import sys
import re
import requests
from mastodon import Mastodon
from bs4 import BeautifulSoup

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://skyhoppers.club/'
)

# grab the article
r = requests.get('https://starwars.fandom.com/wiki/Special:Random', allow_redirects=False)

tootStr = r.headers['Location']

content = requests.get(tootStr)

timeline = ""

if "Category:Legends articles" in content.text:
    timeline = "Legends"
elif "Category:Canon articles" in content.text:
    timeline = "Canon"
elif "Category:Real-world" in content.text:
    timeline = "Real world"

soup = BeautifulSoup(content.text, 'html.parser')

text = soup.find_all('p')

print(tootStr)

CLEANR = re.compile('<.*?>') 

desc = ""

for item in text:
    if "class=" in str(item):
        if "/aside" in str(item):
            desc = re.sub(CLEANR, '', str(item).split("/aside")[1].split("\n")[1])

if desc == "":
    finalTootStr = tootStr + "\n\n" + timeline + "\n\n" + "#StarWars"
else:
    finalTootStr = tootStr + "\n\n" + timeline + "\n\n" + desc + "\n\n" + "#StarWars"

print(finalTootStr)

#put that shit out there!
mastodon.status_post(finalTootStr + " #StarWars")
