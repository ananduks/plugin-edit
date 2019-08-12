# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.sruthy", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("പൊട്ടി ശ്രുതി മണ്ടി ശ്രുതി അഡ്മിനെ കണ്ടാൽ ചൊറിയും ശ്രുതി😂😂🤣🤣😭😭"))
	for _ in range(100):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
