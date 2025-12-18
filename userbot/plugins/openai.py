# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Free GPT Plugin using g4f library
# No API Key required.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import g4f
from userbot import catub
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "tools"

@catub.cat_cmd(
    pattern="fgpt(?:\s|$)([\s\S]*)",
    command=("fgpt", plugin_category),
    info={
        "header": "Free GPT without API Key",
        "description": "Uses g4f library to generate text response for free.",
        "usage": [
            "{tr}fgpt <text/reply>",
        ],
        "examples": [
            "{tr}fgpt write a poem about cat",
        ],
    },
)
async def free_gpt_response(event):
    "Generate a GPT response using g4f (No API Key)"
    
    # گرفتن متن از ورودی یا ریپلای
    text = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    
    if not text and reply:
        text = reply.text
    
    if not text:
        return await edit_delete(event, "**لطفاً متنی بنویسید یا روی پیامی ریپلای کنید.**")

    catevent = await edit_or_reply(event, "**Wait... (Connecting to Free Providers)**")

    try:
        # استفاده از g4f برای دریافت پاسخ
        # این بخش به صورت خودکار بین پروایدرهای رایگان می‌چرخد
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_3_5_turbo,
            messages=[{"role": "user", "content": text}],
        )
        
        if not response:
            return await edit_or_reply(catevent, "**خطا: پاسخی دریافت نشد.**")

        # ارسال پاسخ نهایی
        await edit_or_reply(catevent, response)

    except Exception as e:
        await edit_or_reply(catevent, f"**Error:**\n`{str(e)}`")

