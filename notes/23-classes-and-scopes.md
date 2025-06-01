




cs2370 Notes: 23 More Classes and Scopes · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 23 More Classes and Scopes](/classes/2024-01/cs2370/notes/23-classes-and-scopes/)/

cs2370 Notes: 23 More Classes and Scopes
========================================

24 March 2024·216 words·2 mins·





**Operator overloading**

ref: <https://web.mit.edu/fluids-modules/www/exper_techniques/2.Propagation_of_Uncertaint.pdf>

```

from numbers import Number
from functools import total_ordering
@total_ordering
class NumErr:
    """Represents a number with uncertainty (val +- err)"""
    def __init__(self, val, err=0):
        if isinstance(val, NumErr):
            self.val = val.val
            self.err = val.err + err
        else:
            self.val = val
            self.err = err
    def __add__(self, yy):
        if isinstance(yy, Number):
            yy = NumErr(yy, 0)
        return NumErr(self.val + yy.val, self.err + yy.err)
    def __sub__(self, yy):
        if isinstance(yy, Number):
            yy = NumErr(yy, 0)
        return NumErr(self.val - yy.val, self.err + yy.err)
    def frac_err(self):
        return self.err / abs(self.val)
    def __mul__(self, yy):
        if isinstance(yy, Number):
            yy = NumErr(yy, 0)
        val = self.val * yy.val
        err = abs(val * (self.frac_err() + yy.frac_err()))
        return NumErr(val, err)
    def __div__(self, yy):
        if isinstance(yy, Number):
            yy = NumErr(yy, 0)
        val = self.val * yy.val
        err = abs(val * (self.frac_err() + yy.frac_err()))
        return NumErr(val, err)
    def __eq__(self, yy):
        err = self.err + yy.err
        return self.val + err >= yy.val and self.val - err <= yy.val 
    def __lt__(self, yy):
        return self.val < yy.val
    #def __gt__(self, yy):
    #    return self.val > yy.val
    def __repr__(self):
        return f"NumErr({self.val}, {self.err})"
    
    def __str__(self):
        return f"{self.val}±{self.err}"

```

**Objects and Scopes**

Let’s try to figure out the values of names in the following
scenarios:

* A global variable that is changed.
* Global variable after local variable set
  + With “global” keyword
* Nested functions: global, nonlocal
* Nested classes

![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 21 Flappy Bat
19 March 2024](/classes/2024-01/cs2370/notes/21-flappy-bat/)

[cs2370 Notes: 24 Introducing the Web
26 March 2024


→
←](/classes/2024-01/cs2370/notes/24-the-web/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













