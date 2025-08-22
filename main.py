import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ChatMemberHandler

# Bot token
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # example: -100123456789

# Start command
async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🚀 Join Channel", url="https://t.me/YourChannelLink")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.ibb.co/pXyY2Px/sample.jpg",  # apna image link dalna
        caption="👋 Welcome to our bot!\n\n✅ Join our channel to stay updated.",
        reply_markup=reply_markup
    )

# User leave detect
async def track_chat_member(update: Update, context: CallbackContext):
    result = update.chat_member
    status = result.new_chat_member.status
    user = result.from_user

    # Agar user left karta hai channel
    if status == "left":
        try:
            await context.bot.send_message(
                chat_id=user.id,
                text="⚠️ You left the channel! Please rejoin to continue."
            )
        except:
            pass

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMemberHandler(track_chat_member, ChatMemberHandler.CHAT_MEMBER))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
