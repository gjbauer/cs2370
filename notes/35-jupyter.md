




cs2370 Notes: 35 Jupyter Notebook · Classes with Prof. Nat Tuck






















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
5. [cs2370 Notes: 35 Jupyter Notebook](/classes/2024-01/cs2370/notes/35-jupyter/)/

cs2370 Notes: 35 Jupyter Notebook
=================================

23 April 2024·364 words·2 mins·





This semester we’ve written a bunch of python code. We’ve primarily
written and run our programs in IDLE, but we’ve also tried running our
programs from the command line. This makes a lot of sense when the
point of the program is primarily to create a completed program that
can then be run repeatedly.

Today I want to demonstrate another way to look at writing Python
programs that makes sense for situations where:

* A core purpose of the program is to have other people look at the
  code in order to communicate (e.g. a scientific paper).
* The code will produce one output and the only reason to re-run it
  is to confirm that output.
* You’re exploring in a way that interactive programming is useful.

New tool: [Jupyter Notebook](https://jupyter.org/)

To get this set up easily, you might want to try [Anaconda](https://www.anaconda.com/download/success) or
[Miniconda](https://docs.anaconda.com/free/miniconda/).

If you use Anaconda, then Jupyter is installed by default but you need
to dodge some trick payware nonsense when you try to run it. Any sort
of “cloud” thing is probably a scam.

If you use Miniconda, you can install Jupyter with

```
conda install jupyter

```

Once you have it installed, open up Jupyter Labs. This will pop up a
browser window - note that this isn’t an external web site, it’s
running on your machine (with a local web server, much like what we
played with earlier this semester).

Let’s create a new notebook.

* Cell -> Markdown: # Hello Notebook
* Cell -> Code
  + x = 10 + 20
* Cell -> Code
  + x
* Cell -> Code

```
from PIL import Image
image = Image.open("duck1.jpg")
image

```

Exporting as PDF / HTML:

* File -> Export as: PDF
* This requires some packages to be installed.
  + conda install pandoc
  + LaTeX
    - Linux: apt-get install texlive texlive-xetex
    - Windows: choco install texlive
    - Mac: brew install texlive
* File -> Export as: HTML

And another cell:

```
image.rotate(180)

```

More Examples

[#](#more-examples)
==================================

From: <https://github.com/StrikingLoo/pandas_workshop>

```
import pandas as pd
import random
names = ["Albert","John","Richard","Henry","William"]
surnames = ["Goodman","Black","White","Green","Joneson"]
salaries = [500*random.randint(10,30) for _ in range(10)]
def generate_random_person(names, surnames, salaries):
    return {"name":random.sample(names,1)[0],
            "surname":random.sample(surnames,1)[0],
            "salary":random.sample(salaries,1)[0]}
def generate_people(k):
    return [generate_random_person(names, surnames, salaries) for _ in range(k)]
generate_random_person(names, surnames, salaries)
{'name': 'Richard', 'salary': 7500, 'surname': 'Joneson'}
df = pd.DataFrame(generate_people(50),columns=["name","surname","salary"])
df

```


![Nat Tuck](/img/author_hu_995db18b97553af7.jpg)
Author

Nat Tuck











---


[←
→
cs2370 Notes: 33 Binary Tree
22 April 2024](/classes/2024-01/cs2370/notes/33-binary-tree/)

[cs2370 Notes: 34 Artificial Intelligence
23 April 2024


→
←](/classes/2024-01/cs2370/notes/34-ai/)





[↑](#the-top "Scroll to top")

©
2025
Nat Tuck

Powered by [Hugo](https://gohugo.io/) & [Blowfish](https://blowfish.page/)













