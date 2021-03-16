"""
Test cases for Linguistics Challenge, Task 1
"""

from jsgf import parse_grammar_string

filename = 'JSGF_en_ext.txt'

with open(filename, 'r') as file:
    s = file.read()

grammar = parse_grammar_string(s)


def check_utterance(utt, grammar):
	"""
	Gets the rule that matches the utterance
	"""
	try:
		rule = grammar.find_matching_rules(utt)[0]
		return True
	except:
		return False

# test utterances
utterances = ['can you play beatles', 
				'can you put on paranoid android', 
				'i want to listen to jazz music', 
				'play me ummagumma by pink floyd',
				'we d like to hear let it be',
				'put on some rock',
				'could you play some classic please']

for utt in utterances:
	assert check_utterance(utt, grammar), utt 