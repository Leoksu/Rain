# Rain
<p align="center">
    <b>Is an Telegram A.I Chat bot written in python with pyrogram library, and make brain using Brainshop.ai APi
    </b>
</p>
<img src="" alt="" />
<p align="center">
<a href="https://t.me/GhostWebs" alt="Telegram"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://github.com/Leoksu" alt="Leoksu"> <img src="https://img.shields.io/badge/Built%20by-Leoksu-blue.svg" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Written%20in-Python-ffdb2282.svg?style=modern&logo=python&color=blue" /> </a>
<a href="https://github.com/Leoksu/Rain/blob/main/LICENSE" alt="GPLv3 license"> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" /> </a>
</p>

# Features

- [x] Free, like, totally free ☺️.
- [x] Generate human-like text response.
- [x] Ability to remember past dialogue.
> Will forget user in several days. In work with this.
- [x] Ability to understand human feelings. ie, when you angry, happy, etc.
- [x] Totally customable, see [here](#customize-your-brain).
- [x] Listener for group, able to reply whenever you call it's name (see [here](#editing-code)).
- [x] Easy and fast deployment.
- [x] And more, demo in telegram **[Rain](https://t.me/RainRbot)**.

---
# Setup

- First you need to create account at [Brainshop](https://brainshop.ai/user/register).
> Strongly recommend to use real mail for backup purpose.
> Domain name can be anything, such as google.com or yours since it's not useable (active domain required).
- After register, You will receive mail to complete your registration.
- If you done with account, then create new brain by click [this](https://brainshop.ai/brain/add/brain).
> Recommended to enable semantic engine and default cells, so you don't need to built brain manually. (unless you know to do it)
> Application can be anything, it's only matter to your bot response since you enable semantic engine and default cells.
- Save your brain, and go to your brain settings.
<summary>
    <img src="" alt="" />
</summary>
- Copy Brain ID and API Key, it will be used in [variables](#variables).

---
# Customize your brain

- You can customize your bot name, age, even band and music favorite.
- See example attribute at default attribute in settings menu.

<summary>
    <img src="" alt="" />
</summary>
- Click that wrench icon, Click attribute and add attribute based on default attribute with your own value.
> It's not required to add all attribute, you can add only what you need.

---
# Variables

- `BOT_TOKEN` - Visit [@BotFather](https://t.me/BotFather) and send `/newbot`. You will see instructions to create a new bot.
- `API_URL` & `BRAIN_ID` - Your brainshop configuration ([# Setup](#setup)).
- `USERNAME` - Your bot username without @.

# Deployment

## Deploy locally (Linux based os):
- Update first.
```sh
apt update && apt upgrade
```
- Install `git` and `python`, skip if you have rhis.
```sh
apt install git python3
```
- Clone this repository.
```sh
git clone https://github.com/Leoksu/Rain && cd Rain
```
- Install requirements.
```sh
pip3 install -r requirements.txt
```
- Copy sample.env to .env and fill your [variables](#variables).
```sh
cp sample.env .env
nano .env
```
- Finnaly run your bot.
```sh
python3 rain.py
```
- If you want to run your bot on background of your server
- run this before `python3 rain.py`.
```sh
apt intall screen && screen -S chatbot
```
- And run `python3 rain.py`, after done press `CTRL+A` & `D` to detach from screen
- To check logs or stop bot run `screen -r chatbot`
- and press `CTRL+C` if you want to stop the bot

---
# Credit and thanks ♥️
- [AsmSafone](https://github.com/AsmSafone) for `InlineKeyboardButton` design inspiration
- [Dan](https://github.com/delivrance) for his awesome [Pyrogram](https://github.com/pyrogram/pyrogram) library.
- Feel free to open pull request if there something gonna wrong
- or create an issue if you want to report bugs or request feature.