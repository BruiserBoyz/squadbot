# squadbot
(Fun) Squad tools for discord. Currently boasting a two player fightbot and soon to have some rewards and ranks.

## Features
- Two player fightbot.
- (more coming but won't be listed until implemented)

## Getting Started
### Prerequisites
- Hosted Server (ie AWS or local)
- Discord Bot Token
- ~~Python 3.6.+~~

### Installation
- install docker and git
```bash
sudo install docker.io
sudo install git
```
- load the image
```bash
sudo docker load < image_folder/squadbot_save.tar
```
- navigate to the git folder and clone this repo
```bash
cd home/ubuntu/sb
git clone https://github.com/BruiserBoyz/squadbot.git
```
- issue: need to manually create temp images folder (for now)
```bash
mkdir squadbot/cogs/assets/temp_imgs
```
- contact @jayarghargh for the .env file requirements
- use docker to run the container and the bot. should. work.
```bash
sudo docker run -ti -v [path to git]:/usr/sb image:version bash "usr/sb/squadbot/run.sh"
```
- ie :)
```bash
sudo docker run -ti -v /home/ubuntu/sb/:/usr/sb squadbot:v0.03 bash "usr/sb/squadbot/run.sh"
```

#### Database Requirements
- currently none, about to implement postgresql which will make this a little more complex

## Built With
- [Discord.py](https://discordpy.readthedocs.io/en/latest/)
```
python3 -m pip install -U discord.py
python-dotenv
pillow
cogs
```
## Contributing
<!--Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.-->
Branch, fix bugs, pull request. Thanks :D

## Versioning
We use SemVer for versioning.

## Authors
- Justin Reid [JayaArghArgh](https://github.com/JayArghArgh)
- Tim Power [Tpow90](https://github.com/timpower90)
