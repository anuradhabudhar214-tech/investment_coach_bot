print(">>> telegram_bot.py started")

import os
from pathlib import Path
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


# Load environment variables from .env

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("BOT_TOKEN loaded:", bool(BOT_TOKEN))
print("OPENAI_API_KEY loaded:", bool(OPENAI_API_KEY))


# Load prompt files

def load_prompt(file_name):
    path = os.path.join("prompts", file_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

coach_prompt = load_prompt("coach.txt")
commentary_prompt = load_prompt("commentary.txt")

# Track user mode (coach / commentary)

user_mode = {}  # user_id -> "coach" or "commentary"


# Bot commands

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Hello! Welcome to the Investment Bot.\n\n"
        "Choose a mode:\n"
        "/coach - Learn investing concepts\n"
        "/commentary - Market commentary and trends"
    )
    await update.message.reply_text(text)

async def coach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_mode[update.effective_user.id] = "coach"
    await update.message.reply_text(
        "Coach mode activated.\nAsk about investment concepts."
    )

async def commentary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_mode[update.effective_user.id] = "commentary"
    await update.message.reply_text(
        "Commentary mode activated.\nAsk about market movements."
    )


# Safety check (no financial advice)

def is_advice_request(text: str) -> bool:
    keywords = [
        "buy", "sell", "recommend", "best stock",
        "which stock", "should i", "invest in"
    ]
    text = text.lower()
    return any(keyword in text for keyword in keywords)


# Dynamic “fake” OpenAI response (for submission)

def fake_openai_response(user_text, mode):
    if is_advice_request(user_text):
        return (
            "I can’t provide investment advice or recommendations.\n"
            "I can explain concepts or discuss general market trends.\n"
            "This is for educational purposes only."
        )

    if mode == "coach":
        return (
            f"{coach_prompt}\n\n"
            f"Example answer for your question '{user_text}': "
            "This is an educational explanation based on your question."
        )
    else:
        return (
            f"{commentary_prompt}\n\n"
            f"Example answer for your question '{user_text}': "
            "This is a general market commentary based on your question."
        )


# Handle user messages

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id
    mode = user_mode.get(user_id, "coach")

    try:
        # Use dynamic fake response
        reply = fake_openai_response(user_text, mode)
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text(
            "Sorry, I’m unable to generate a response right now."
        )
        print("Error:", e)


# Main

def main():
    print("Bot is running...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("coach", coach))
    app.add_handler(CommandHandler("commentary", commentary))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
