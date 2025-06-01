




cs2370 Notes: 36 Word Game · Classes with Prof. Nat Tuck






















[↓Skip to main content](#main-content)

[Classes with Prof. Nat Tuck](/)

[Home](/)
[cs2370](/classes/2025-01/cs2370/)
[cs2470](/classes/2025-01/cs2470/)
[cs4310](/classes/2025-01/cs4310/)
[Inkfish](https://inkfish.homework.quest/)









* [Home](/)
* [cs2370](/classes/2025-01/cs2370/)
* [cs2470](/classes/2025-01/cs2470/)
* [cs4310](/classes/2025-01/cs4310/)
* [Inkfish](https://inkfish.homework.quest/)





1. </>/
2. [/classes](/classes/)/
3. [Classes, Spring 2024](/classes/2024-01/)/
4. [CS 2370 Spring 2024: Course Site](/classes/2024-01/cs2370/)/
5. [cs2370 Notes: 36 Word Game](/classes/2024-01/cs2370/notes/36-word-game/)/

cs2370 Notes: 36 Word Game
==========================

28 April 2024·157 words·1 min·





Word game: <https://words.homework.quest/>

Word list: <https://github.com/NatTuck/word-game/tree/03-high-scores/priv/data>

Setup:

```
py -m pip install git+https://github.com/NatTuck/realtime-py.git

```

Code:

```
from realtime.connection import Socket
import asyncio
from random import randint
import sys
NAME = "Orange"
URL = "wss://words.homework.quest/socket/websocket?vsn=2.0.0"
loop = asyncio.get_event_loop()
channel = None
done = False
def letters():
    return set("abcdefghijklmnopqrstuvwxyz")
async def on_view(msg):
    global done
    
    print("\nmsg =", msg)
    puzzle = msg['puzzle']
    
    if not "-" in puzzle:
        done = True
        print("Game done.\n")
        return
    
    guesses = set(msg['guesses'])
    options = letters() - guesses
    print("options:", options)
    guess = list(options)[0]
    print("Guessing:", guess)
    await channel.send("guess", {"ch": guess}, "")
    
async def main():
    global channel
    client = Socket(URL, False, {"name": NAME})
    # connect to the server
    await client.connect()
    # fire and forget the listening routine
    listen_task = asyncio.ensure_future(client.listen())
    # join the channel
    channel = client.set_channel("game:practice" + str(randint(1, 1000)))
    await channel.join()
    channel.on("view", None, on_view)
    # we give it some time to complete
    while not done:
        await asyncio.sleep(1)
    # proper shut down
    listen_task.cancel()
    
if __name__ == '__main__':
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loop.stop()
        exit(0)

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 34 Artificial Intelligence
23 April 2024](/classes/2024-01/cs2370/notes/34-ai/)

[cs2370 Notes: 37 Practice Exam
30 April 2024


→
←](/classes/2024-01/cs2370/notes/37-practice-exam/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













