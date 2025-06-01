#!/usr/local/bin/python3
from markdownify import markdownify as md
import os

# Get the list of all files in a directory\
files = os.listdir(os.getcwd() + "/notes")

# Print the files
for file in files:
	f0 = open(os.getcwd() + "/design-recipe", "r")
	f1 = open(os.getcwd() + "/design-recipe.md", "w")
	text = md(f0.read())
	f1.write(text)
	print(text)
	f0.close()
	f1.close() # <-
