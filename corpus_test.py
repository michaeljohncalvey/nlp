# import nltk
# nltk.download('wordnet')

from nltk.corpus import wordnet as wn
poses = { 'n': 'noun', 'v': 'verb', 's': 'adj (s)', 'a': 'adj', 'r': 'adv'}
for synset in wn.synsets("banter"):
	print("{}: {}".format(poses[synset.pos()],
		", ".join([l.name() for l in synset.lemmas()])))