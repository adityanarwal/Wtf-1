from pyrogram import Client
from pyrogram.types import Message

from config import BOT_USERNAME
from driver.filters import command
from driver.convert_to_image import convert_to_image
from driver.get_arg import get_arg


@nexaub.on_cmd(command=["telegraph", "tgraph"])
async def telegraph_up(_, message: Message):
    tgraph_msg = await e_or_r(nexaub_message=message, msg_text="`Processing...`")
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
      return await tgraph_msg.edit("Reply to a message that contains `text`/`image` or `mp4 file`!")
