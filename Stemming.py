from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import state_union

ps=PorterStemmer()

example_sent="Hey there! I am writing a code using python pythonaly"

words=word_tokenize(example_sent)

for w in words:
	print(ps.stem(w))
