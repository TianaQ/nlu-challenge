"""
Testing utterances for the Linguistics Challenge

1st argument - grammar text file name 
2nd argument - text file with a list of utterances (each on a new line) to test
"""

import sys
from jsgf import parse_grammar_string

try:
	grammar_file = sys.argv[1] 
except IndexError:
	print("No grammar text file provided.")
	sys.exit(1)

with open(grammar_file, 'r') as file:
	s = file.read()

try:
	grammar = parse_grammar_string(s)
except:
	print("Impossible to process the grammar file")
	sys.exit(1)


try:
	utt_file = sys.argv[2]
except IndexError:
	print("Please, provide a list of utterances in a text file.")
	sys.exit(1)

with open(utt_file, 'r') as file:
	s = file.read()
utterances = s.split('\n')


def check_utterance(utt, grammar):
	"""
	Gets the rule that matches the utterance
	"""
	try:
		rule = grammar.find_matching_rules(utt)[0]
		return True
	except:
		return False

for utt in utterances:
	assert check_utterance(utt, grammar), utt 