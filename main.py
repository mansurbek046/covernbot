from credentials import api_hash, api_id, bot_token
from pyrogram import Client, filters

app=Client('mussaid_bot', api_hash=api_hash, api_id=api_id, bot_token=bot_token)

@app.on_message(filters.command('start'))
async def welcome(client, message):
  chat_id=message.chat.id
  await client.send_message(chat_id=chat_id, text="Welcome! Send me message whichever  you want.."


