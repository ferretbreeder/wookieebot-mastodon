# Wookieebot (now with 100% more Mastodon)
The only Star Wars bot you'll ever need! Wookieebot grabs a random article from the Wookieepedia (the [Star Wars wiki](https://antifandom.com/starwars/wiki/Main_Page), proxied here through [Breezewiki](https://breezewiki.com/)) and posts it to a Mastodon account at regular intervals. "Mastodon" is in the name because this bot used to exist on Twitter many moons ago, but we know what happened there. Thankfully Mastodon is just as easy to develop for! This started as a proof of concept idea, but has since grown into a greater exercise in web scraping and playing around with the data that comes from that.

My instance of the bot is hosted on my Mastodon instance <a rel="me" href="https://skyhoppers.club/@wookieebot">skyhoppers.club</a>.

Currently, Wookieebot provides:

- A link to the random article
- A tag indicating whether that article is part of the Legends continuity, Canon continuity, or about a real-world subject (person, location on Earth, etc.)
- A brief preview of the article (well, some of the time)

## Installation

Installation is as simple as cloning the repo...

```git clone https://github.com/ferretbreeder/wookieebot-mastodon.git && cd wookieebot-mastodon```

...setting up virtual environment inside the repo folder...

```python3 -m venv .```

...and then creating a ```token.secret``` file. This will be populated with only your unique access token that you get when you create an application on the Mastodon account that houses your bot.

![image](https://github.com/user-attachments/assets/f5f3e193-ce08-4ef3-9bf0-2708871110e6)

## Usage

Once installation is completed, just run ```wookieebot-mastodon.py``` inside your virtual environment and you should be good to go!

As far as automation goes, I run mine with a cron job that posts at half past every hour.

## Issues and Planned Features

There's only so many things I could reasonably do with a bot this simple, but currently the code is in need of refactoring and linting and the descriptions appear in posts irregularly. This is a symptom of how I'm parsing the wiki pages, but Fandom wiki pages are pretty nasty. I'm sure there's a way to grab article previews more cleanly and consistently, so that's next on my to-do list.

## Contributing

Feel free to propose any changes or improvements as you see fit. It's a pretty simple program, but I'd love to get some other people involved! :D
