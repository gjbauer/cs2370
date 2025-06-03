




Design Recipe · Classes with Prof. Nat Tuck






















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
3. [Classes, Spring 2025](/classes/2025-01/)/
4. [CS 2370 Spring 2025: Course Site](/classes/2025-01/cs2370/)/
5. [Design Recipe](/classes/2025-01/cs2370/design-recipe/)/

Design Recipe
=============

15 January 2025·1100 words·6 mins·





Recipe Steps

[#](#recipe-steps)
--------------------------------

1. Purpose statement
2. Stub with Names
3. Type Signature
4. Examples
5. Standard pattern
6. Write the body
7. Tests

Purpose Statement

[#](#purpose-statement)
------------------------------------------

This should be a one line docstring stating the purpose of the function.

Examples:

```
def sqrt(xx):
    """Calculate the square root of a number."""
    ...
def count_ones(xs):
    """How many times does 1 appear in a list?"""
    ...

```

Stub

[#](#stub)
----------------

The function stub is the “def” line, including the names of all the
parameters.

```
def sqrt(xx):
    pass
def count_ones(xs):
    pass

```

Signature

[#](#signature)
--------------------------

Annotate your function stub to include types for each parameter and a
return value. This should be checkable by
[mypy](https://mypy.readthedocs.io/en/stable/).

Examples:

```

# number -> float
def sqrt(xx: float) -> float:
    pass
    
# [int] -> int
def count_ones(xs: list[int]) -> int:
    pass

```

The `sqrt` function takes one argument which must a float
(probably int or float) and returns an int.

The `count_ones` function takes one argument which must be a list
of int and returns an int.

Examples

[#](#examples)
------------------------

Try to come up with at least two examples of inputs and outputs
for your function. These will become tests later, so you can either
write them as comments now or write them directly as tests.

You can write them any way that’s clear, although starting with ‘==’
makes it easier to translate into tests.

For example:

```
def sqrt(xx):
    pass
# sqrt(9) == 3.0
# sqrt(25) == 5.0
def count_ones(xs):
    pass
# count_ones([2, 1]) == 1
# count_ones([]) == 0

```

Standard Pattern

[#](#standard-pattern)
----------------------------------------

Based on the argument type or the return value, we can make a good
guess as to the general pattern the function is likely to follow.

These patterns combine in different ways, but we generally can guess
the most straightforward combination as a starting point.

A standard pattern may include “…” to indicate that it’s not completed
code, or may not to allow the program to run while testing other code.

Not all fuctions look anything like a standard pattern, but if you’re
not sure what to do the standard pattern is a good place to start.

Write the Body

[#](#write-the-body)
------------------------------------

Actually write code to implement the function fully.

Tests

[#](#tests)
------------------

Convert your examples to tests following the
[pytest](https://docs.pytest.org/en/stable/) conventions.

For example:

```
def count_ones(xs):
    pass
def test_count_ones():
    assert count_ones([2, 1]) == 1
    assert count_ones([]) == 0
from pytest import approx
def sqrt(xx):
    pass
def test_sqrt():
    assert sqrt(9) == approx(3.0)
    assert sqrt(25) == approx(5.0)

```

More on Standard Patterns

[#](#more-on-standard-patterns)
==========================================================

### Patterns for Simple Values [#](#patterns-for-simple-values)

Simple values include things like numbers, booleans, and strings if we
don’t intend to manipulate individual characters.

**Standard pattern for a simple value argument**

```
def process(xx: int):
    ... xx ...

```

If we have a simple value as an argument, we probably use it for something.

**Standard pattern for two simple value argument**

```
def process2(xx: int, yy: int):
    ... xx ... yy ...

```

If we have simple values as arguments, we probably use them for something.

**Standard pattern for returning a simple value**

```
def produce() -> int:
    return ... 5 ...

```

If we need to return a simple value, we probably return some value of that type.

**Combined pattern for a simple argument and a simple return type**

```
def funkify(xx: int) -> int:
    return ... xx ...

```

If we have a simple value argument and we return a simple value, then the function
return value is probably a function of the input.

### Patterns for Lists [#](#patterns-for-lists)

A string should use the standard pattern for a list if it’s being treated
as a sequence of characters.

**Standard patterns for a list argument**

```
def process(xs: list[int]):
    for xx in xs:
       ... xx ... 

```

If we have a list of things, we want to loop through the list and do
something with each thing.

```
def mutate_list(xs: list[int]):
    """Change the elements of the list in place."""
    for ii in range(0, len(xs))
        xx = xs[ii]
        xs[ii] = ... xx ...

```

If you need to alter the elements an existing list, this pattern gives
you the list indices which are nesisary to do that.

**Standard pattern for returning a list**

```
def produce() -> list[int]:
    ys = []
    return ys

```

To return a list, we want to first build a list and then return it.

```
def rabbit(xx: int) -> list[int]:
    ys = []
    ys.append(xx)
    return ys

```

If we have an argument, we probably use that argument in producing the
list. If the argument is of the same type as the items in the list,
the simplest thing to do is to stick the argument on our return list.

**Standard pattern for list to list functions**

```
def funkify(xs: list[int]) -> list[int]:
    ys = []
    for xx in xs:
        ys.append(... xx ...)
    return ys

```

A function that takes a list and return a list probably builds the new
list based on the elements of the old one.

### Patterns for tuples: [#](#patterns-for-tuples)

**Argument**

```
def wumpus(name: tuple[str, str]):
    (first, last) = name

```

If there’s an input tuple, unpack it.

```
def wumpus() -> tuple[str, str]:
    return ('blue', 'jay')

```

If there’s an output tuple, build it with appropriate values.

### Patterns for Dictionaries [#](#patterns-for-dictionaries)

**Standard patterns for a dictionary argument**

```
def process(noises: dict[str, str]):
    ... noises['walrus'] ...

```

When we have a dictionary, the most obvious thing to do with it is to
look up one value by key.

```
def process(noises: dict[str, str]):
    for key in noises.keys():
        ... noises[key] ...

```

Sometimes we want to process every element in a dictionary. The
standard pattern is to loop through the keys and then use them to look
up each associated value.

**Standard pattern for returning a dictionary**

```
def produce() -> dict[str, str]:
    info = {}
    info['color'] = 'blue'
    return info

```

In a function that produces a dictionary, first we need to build the dictionary
then we can return it.

**Standard pattern for dictionary to dictionary functions**

```
def giraffize(things: dict[str, str]) -> dict[str, str]:
    info = {}
    for key in things.keys():
        info[key] = things[key] 
    return info

```
### Mixing Patterns [#](#mixing-patterns)

**Take a list and produces a dictionary**

```
# Takes a list
def process(xs: list[int]):
    for xx in xs:
       ... xx ... 

```
```
# Produces a dictionary
def produce() -> dict[str, str]:
    info = {}
    info['color'] = 'blue'
    return info

```

Combined

```
def list_to_dict(xs: list[str]) -> dict[str, str]:
    info = {}
    for xx in xs:
        info[xx] = xx
    return info

```

**Take two lists and produce a list**

A list-to-list function:

```
# [int] -> [int]
def funkify(xs: list[int]) -> list[int]:
    zs = []
    for xx in xs:
        zs.append(... xx ...)
    return zs

```

Add a second list argument:

```
# [int], [int] -> [int]
def funkify(xs, ys):
    zs = []
    # Are the loops sequential or nested?
    for xx in xs:
        for yy in ys:
            zs.append(... xx ... yy ...)
    return zs

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
Required Software for cs2370
8 January 2025](/classes/2025-01/cs2370/required-software/)

[CS 2370 Spring 2025: Syllabus
17 January 2025


→
←](/classes/2025-01/cs2370/syllabus/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













