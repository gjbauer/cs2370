




cs2370 Notes: 21 Flappy Bat · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 21 Flappy Bat](/classes/2024-01/cs2370/notes/21-flappy-bat/)/

cs2370 Notes: 21 Flappy Bat
===========================

19 March 2024·42 words·1 min·





**Classes and Methods**

Inheritence

```
from math import pi
class LawnShape:
    def area(self):
        raise Exception("not implemented")
    
    def cost(self, grassPrice):
        return self.area() * grassPrice
class Circle(LawnShape):
    def __init__(self, radius, cost):
        self.radius = radius
    
    def area(self):
        return pi * pow(self.radius, 2)

```

Example:

[flappy bat v2](../code/flappy-bat-v2.py)


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 22 Going too Far with Objects
19 March 2024](/classes/2024-01/cs2370/notes/22-animal-objects/)

[cs2370 Notes: 23 More Classes and Scopes
24 March 2024


→
←](/classes/2024-01/cs2370/notes/23-classes-and-scopes/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













