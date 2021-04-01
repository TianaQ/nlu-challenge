"""
This script generating utterances for the Linguistics Challenge 
and writes them to a text file

1st argument - grammar text file name 
2nd argument - index of the grammar rule to test (the first rule by default)
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

# printing the grammar rules with names for reference
print("The names of rules in " + grammar_file)
for count, rule in enumerate(grammar.rules):
	print(count, rule.name)

# check if the rule index is provided
try:
	rule_index = int(sys.argv[2])
except:
	rule_index = 0

# get unique utterances from 1000 generations
gen_utt = []
for i in range(1000):
	gen_utt.append(grammar.rules[rule_index].generate())
print(*set(gen_utt), sep='\n')

# write the utterances to a file
with open(grammar_file + "_utterances.txt", 'w') as f:
    for item in gen_utt:
        f.write("%s\n" % item)