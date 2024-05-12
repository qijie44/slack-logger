<h3 align="center">Slack Logger</h3>
<p align="center">
  A python logger that logs directly back to slack bot via sockets
<p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a logger that extends python logging to log onto slack

### Built With

* python==3.8.10
* slack-bolt==1.18.1
* slack-sdk==3.27.1

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
Install the requirements with
```sh
python3 -m pip install -r requirements.txt
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/qijie44/slack-logger.git
   ```
2. Go to https://api.slack.com/apps and hit the Create New App button
3. Configure the app
  * Go to Socket Mode, and check Enable Socket Mode
  * Go to OAuth & Permissions, scroll to Scopes, and add permissions for app_mentions:read and chat:write.
  * Go to Event Subscriptions, under Subscribe to bot events, click Add Bot User Event and select app_mention.
4. Copy the AppToken, BotToken and SlackSignature into bot.ini
5. Test the connection using slackbot.py, mentioning it in the channel you want it to broadcast to. It should reply with the channel id
6. Copy the channel id into bot.ini
7. Import the library and set the handlers (example given in logging_test.py)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

This project is provided as it is. Please do not contact me.