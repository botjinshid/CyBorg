try:
    from userbot import bot
    from userbot.events import register
except:
    pass
from userbot.__main__ import test
from uniborg.util import admin_cmd

if borg:
    @borg.on(admin_cmd(pattern="ppe"))
    async def switch_ppe(event):
        try:
            await test()
            await event.delete
        except Exception as e:
            await event.edit(str(e))
elif bot:
    @register(outgoing=True, pattern="^.borg")
    async def switch_borg(event):
        try:
            import stdborg
            await event.delete
        except Exception as e:
            await event.edit(str(e))
