from telethon.tl.types import InputWebDocument

from jmthon import tgbot
from jmthon.decorators.asstbot import tgbot_cmd, callback, in_pattern

from .. import Button, inline_pic, inline_mention, up_catbox

AST_PLUGINS = {}

def get_back_button(name):
    return [Button.inline("رجوع", data=f"{name}")]


@in_pattern(owner=True, func=lambda x: not x.text)
async def inline_alive(o):
    TLINK = inline_pic() or "https://graph.org/file/45bd809c97cf4e1666b99.jpg"
    MSG = "• ** سورس محمد •**"
    WEB0 = InputWebDocument(
        "https://graph.org/file/45bd809c97cf4e1666b99.jpg", 0, "image/jpg", []
    )
    RES = [
        await o.builder.article(
            type="photo",
            text=MSG,
            include_media=True,
            buttons=[
                [
                    Button.url(
                        "قناة السورس", url="https://T.me/Jmthon"
                    ),
                    Button.url("مجموعة المساعدة", url="t.me/@x_7RP_99"),
                ],
            ],
            title="سورس محمد",
            description="Mohamed | محمد",
            url=TLINK,
            thumb=WEB0,
            content=InputWebDocument(TLINK, 0, "image/jpg", []),
        )
    ]
    await o.answer(
        RES,
        private=True,
        cache_time=300,
        switch_pm="👥 Mohamed",
        switch_pm_param="start",
    )
