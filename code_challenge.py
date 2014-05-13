import nltk
from nltk.corpus import *


''' RETURNS A LIST OF LISTS OF WORDS --> WHERE LISTS OF WORDS IS EACH SENTENCE '''
def paragraph_tokenize(filename):
	corpus = PlaintextCorpusReader("",filename)
	paragraphs = [sum(para,[]) for para in corpus.paras(filename)]
	return paragraphs







