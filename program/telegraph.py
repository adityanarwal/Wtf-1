import os

from telegraph import Telegraph
from pyrogram.types import Message


from pyrogram import Client
from pyrogram.types import Message

from config import BOT_USERNAME
from driver.filters import command
from driver.error import nexaub, e_or_r
from driver.convert_to_image import convert_to_image
from driver.get_arg import get_arg
from config import Config


# Telegraph client
telegraph = Telegraph()
telegraph.create_account(short_name="Nexa-Userbot")

# Paste text to telegraph
async def paste_text_to_tgraph(title, text):
  try:
    nexaub_usr = await NEXAUB.get_me()
    f_name = nexaub_usr.first_name
    u_name = nexaub_usr.username
    if not title:
      title = f_name if f_name is not None else "By Nexa Userbot"
    t_response = telegraph.create_page(title=title, html_content=text, author_name=f_name if f_name is not None else "Nexa-Userbot", author_url=f"https://t.me/{u_name}" if u_name is not None else "https://github.com/Itz-fork/Nexa-Userbot")
    return f"{t_response['url']}"
  except Exception as e:
    return f"𝐄𝐫𝐫𝐨𝐫 𝟒𝟎𝟒 !! Something went wrong, Please wait for developers to Fix It."

# Upload media to telegraph
async def upload_to_tgraph(file):
  try:
    t_response = telegraph.upload_file(file)[0]["src"]
    return f"https://telegra.ph/{t_response}"
  except Exception as e:
    return f"𝐄𝐫𝐫𝐨𝐫 𝟒𝟎𝟒 !! Something went wrong, Please wait for developers to Fix It."


@nexaub.on_message(command(["telegraph", f"telegraph@{BOT_USERNAME}"]))
async def telegraph_up(_, message: Message):
    tgraph_msg = await e_or_r(nexaub_message=message, msg_text="𝟎% ■■■■■■■■■■ 𝟏𝟎𝟎%\n\nGenerating TeleGraph Link. Please wait !!")
    r_msg = message.reply_to_message
    arg_txt = get_arg(message)
    if r_msg:
      # Photo / Video or Video note
      if r_msg.photo or r_msg.video or r_msg.video_note:
        r_content = await r_msg.download()
      # Stickers
      elif r_msg.sticker:
        r_content = await convert_to_image(message=r_msg, client=NEXAUB)
      # Text messages
      elif r_msg.text:
        r_content = r_msg.text
        # Set title if provided by user
        if arg_txt:
          t_title = arg_txt
        else:
          t_title = None
        # Paste text to telegraph
        t_pasted = await paste_text_to_tgraph(title=t_title, text=r_content)
      else:
        tgraph_msg.edit("`No Supported Media or Text to paste!`")
      # Paste media to telegraph
      t_pasted = await upload_to_tgraph(r_content)
      # Edit message with the telegraph link
      await tgraph_msg.edit(f"**Telegraph Link:** {t_pasted}")
    else:
      return await tgraph_msg.edit("**Reply to a message that contains Text or Media.**")
