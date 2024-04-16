from credentials import api_hash, api_id, bot_token, telegraph_access_token
from pyrogram import Client, filters
from telegraph import Telegraph
import os
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

telegraph = Telegraph(telegraph_access_token)
telegraph.create_account(short_name='covernbot')

app=Client('covernbot', api_hash=api_hash, api_id=api_id, bot_token=bot_token)

@app.on_message(filters.command('start'))
async def welcome(client, message):
  chat_id=message.chat.id
  await client.send_message(chat_id=chat_id, text="Welcome! Send me message whichever you want..")

@app.on_message()
async def incoming(client, message):
    chat_id=message.chat.id
    if message.document:
        mime_type = message.document.mime_type.lower()
        if mime_type == "application/pdf" or mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            await client.send_message(chat_id=chat_id, text="You sent right document..")
            # document=await client.download_media(message, block=True)
            # doc_name=document.split('/')[-1].split('.')[0]
        else:
            await client.send_message(chat_id=chat_id, text="Bot only accepts with .pdf or .docx documents.")
    else:
        urls=message.text.split()
        for url in urls:
            if url.startswith('http'):
                if not url.startswith('https'):
                    url=url.replace('http','https')
            elif len(url.split('.'))>=2:
                url=f'https://{url}'
            else:
                url=f"https://duckduckgo.com?q={message.text.lower().replace(' ','%20')}"
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Results', web_app=WebAppInfo(url=url))]])
                await client.send_message(chat_id=chat_id, text='DuckDuckGo search!', reply_markup=reply_markup)
                break
            print(url)
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Click me!', web_app=WebAppInfo(url=url))]])
            await client.send_message(chat_id=chat_id, text='Click button:', reply_markup=reply_markup)

            
if __name__=='__main__':
    app.run()

