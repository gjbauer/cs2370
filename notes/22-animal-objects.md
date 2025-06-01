




cs2370 Notes: 22 Going too Far with Objects · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 22 Going too Far with Objects](/classes/2024-01/cs2370/notes/22-animal-objects/)/

cs2370 Notes: 22 Going too Far with Objects
===========================================

19 March 2024·38 words·1 min·





**Interfaces vs Inheritence**

Animals:

```
class Bat:
    image = "bat.png"
    
    def __init__(self):
        self.sprite = ... construct sprite
    
    def moveTo(self, x, y):
        self.sprite.update(...)
    def draw(self):
        self.sprite.draw()
    
    def hit(self, x, y):
        # circle as bounding box
    
    def tick(self, x, y):
        pass

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 20 Classes and Methods
14 March 2024](/classes/2024-01/cs2370/notes/20-classes-methods/)

[cs2370 Notes: 21 Flappy Bat
19 March 2024


→
←](/classes/2024-01/cs2370/notes/21-flappy-bat/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













