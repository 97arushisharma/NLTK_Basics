import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

traintxt=state_union.raw("2005-GWBush.txt")
maintxt=state_union.raw("2006-GWBush.txt")

cust_txt_tokenizer=PunkSentenceTokenizer(traintxt)
tokenized=cust_txt_tokenizer.tokenize(maintxt)

def process_content():
  try:
      for i in tokenized:
	words=nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)

  except Exception as e:
	print(str(e))


process_content()
