"""
Test cases for Linguistics Challenge, Task 2
"""

from jsgf import parse_grammar_string

filename = 'JSGF_ru_ext.txt'

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
utterances = ['включи radio head', 
				'я хочу послушать paranoid android', 
				'поставь что-нибудь из джаза', 
				'поставь пожалуйста какой-нибудь рок',
				'мы хотим послушать джазовую музыку',
				'включи какую-нибудь рок музыку пожалуйста',
				'поставь let it be битлз',
				'включи что-нибудь из битлов',
				'я хочу послушать умагуму пинк флойд',
				'мы хотим послушать что-нибудь из группы cake']

for utt in utterances:
	assert check_utterance(utt, grammar), utt 


