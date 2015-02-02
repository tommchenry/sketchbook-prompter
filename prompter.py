#!/usr/bin/env python

"""
Sketchbook Prompter: A script to provide randomized prompts of common objects,
locations, fictional characters and celebrities to draw when feeling sketchbook
doldrums. 

PAO? 
"""
import random
import string
PROMPT_FILENAME = "prompts.txt"

def importPrompts(allPrompts):
	'''
	Opens the prompt file and appends each line to allPrompts.
	'''
	inFile = open(PROMPT_FILENAME, 'r', 0)
	prompts_raw = inFile.read()
	prompts_raw = prompts_raw.splitlines()
	for prompt in prompts_raw:
		allPrompts.append(prompt)

def createPrompt():
	'''
	Takes user input to produce a random prompt from a list.
	'''
	allPrompts = []
	importPrompts(allPrompts)
	print "\nSketchbook Prompter v.0.1" 
	print "---------" 
	print "Draw:", allPrompts[random.randrange(0, len(allPrompts))]

createPrompt()
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
