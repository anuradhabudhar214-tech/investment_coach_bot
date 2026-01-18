# Investment Coach Bot (Telegram)

This project was built as a take-home assignment for the AI/ML internship at PineOS.ai.

It is a Telegram bot that provides:
- Educational investment coaching
- Neutral market commentary
- Safety filtering to avoid personalized financial advice

Features:
- /coach command for investment education
- /commentary command for market insights
- Rule-based filtering using Python
- Environment-based secret management

Project Structure:
investment_coach_bot/
telegram_bot.py
advice_filter.py
coach.txt
commentary.txt
requirements.txt
.env.example
README.md

Requirements:
- Python 3.10 or higher
- Telegram Bot Token
- OpenAI API Key

Setup & Run:
1. Clone the repository
git clone https://github.com/anuradhabudhar214-tech/investment_coach_bot.git
cd investment_coach_bot

2. Install dependencies
pip install -r requirements.txt

3. Create a .env file
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key

4. Run the bot
python telegram_bot.py

Notes:
- This bot provides educational content only
- No personalized financial advice is given
