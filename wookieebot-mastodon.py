import sys
import requests
from mastodon import Mastodon

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://skyhoppers.club/'
)

# grab the article
r = requests.get('https://starwars.fandom.com/wiki/Special:Random', allow_redirects=False)

tootStr = r.headers['Location']

#put that shit out there!
mastodon.status_post(tootStr + "#StarWars")
