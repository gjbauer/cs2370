




cs2370 Notes: 20 Classes and Methods · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 20 Classes and Methods](/classes/2024-01/cs2370/notes/20-classes-methods/)/

cs2370 Notes: 20 Classes and Methods
====================================

14 March 2024·53 words·1 min·





**Classes and Methods**

Calculating the area of a circle:

```
from math import pi
def circle_area(radius):
    return pi * pow(self.radius, 2)
class Circle:
    def area(self):
        return pi * pow(self.radius, 2)

```

Constructor

```
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * pow(self.radius, 2)

```

Example:

[flappy bat v1](../code/flappy-bat-v1.py)


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 19 Palindromes
8 March 2024](/classes/2024-01/cs2370/notes/19-palindromes/)

[cs2370 Notes: 22 Going too Far with Objects
19 March 2024


→
←](/classes/2024-01/cs2370/notes/22-animal-objects/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













