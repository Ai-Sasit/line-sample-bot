# line-sample-bot
## Project Description
  - This is a local bot for play music on computer with command via smart phone
## Required modules
  - Flask
  - Linebot
  - Youtube_search
  - Pydub
  - Pygame
  - Pafy
## How To Run!
  - add `Channel secret` and `Channel access token` It's received from LINE Developers
  - open `ngrok`
  ```
  ngrok http 3000
  ```
  - set `Webhook URL` in LINE Developers with `https://************.ngrok.io/webhook`
  - run line bot
  ```
  python bot.py
  ```
