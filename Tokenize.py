from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_sent="Hey there! I am new to NLTK and python programming. Hope you can help me."

#print(sent_tokenize(example_sent))

#print(word_tokenize(example_sent))

#for i in word_tokenize(example_sent):
#	print(i)

stop_words=set(stopwords.words("english"))
print(stop_words)
words= word_tokenize(example_sent);
filtered_sent=[]
for w in words:
	if w not in stop_words:
		filtered_sent.append(w)

print(filtered_sent)

