Investment Coach Bot (Telegram)

This project is created as a take-home assignment for the AI/ML internship at PineOS.ai.

It is a simple Telegram bot that gives educational investment guidance and general market commentary.
The bot is designed to avoid giving personal financial advice and focuses only on learning purposes.

What this bot does:

Gives basic investment related guidance using the /coach command

Provides market commentary using the /commentary command

Uses simple Python logic for filtering responses

Uses environment variables for API keys

Project files:
telegram_bot.py – main file to run the Telegram bot
advice_filter.py – logic for filtering responses
coach.txt – investment coaching content
commentary.txt – market commentary content
requirements.txt – required Python libraries
.env.example – example environment file

Requirements:
Python 3.10 or above
Telegram Bot Token
OpenAI API Key

How to run the project:

Clone the repository
git clone https://github.com/anuradhabudhar214-tech/investment_coach_bot.git

Go to the project folder
cd investment_coach_bot

Install required packages
pip install -r requirements.txt

Create a .env file and add your keys
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key

Run the bot
python telegram_bot.py

Note:
This project is for educational purposes only and does not provide personalized financial advice.
