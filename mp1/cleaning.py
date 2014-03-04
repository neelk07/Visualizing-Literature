#  2/4 script
from __future__ import division

import nltk
import json
import re, pprint
# nltk.download()
from nltk.book import *
from nltk.corpus import PlaintextCorpusReader

def dump_json(tokens_in,state,size):
     tokens_freq = FreqDist(tokens_in)
     tokens_table = [dict(word=w, freq=tokens_freq[w]) for w in tokens_freq]
     tokens_table_short = tokens_table[:size]

     with open("tokens_"+ state + str(size) + ".json",'w') as outfile:
          json.dump(tokens_table_short,outfile, sort_keys = True, indent = 4,
ensure_ascii=False)

raw_text = open('ofk_chap_b.txt').read()
type(raw_text)

#tokenize raw text
tokens_raw = nltk.word_tokenize(raw_text) #show link
type(tokens_raw)
tokens_raw[:50]  # talk about apostrophes "'s" vs "eat." vs "n't"
dump_json(tokens_raw,"raw",30)

#convert everything to lower case
tokens_lower = [w.lower() for w in tokens_raw] #change to lower case
dump_json(tokens_lower,"lower",30)

#remove period from end of sentences
tokens_punct = [re.sub('\.','',w) for w in tokens_lower] #remove periods
dump_json(tokens_punct,"punct",30)


#only keep alphabetic strings
tokens_word = [w for w in tokens_punct if w.isalpha()] #just keep words
dump_json(tokens_word,"word",30)


#remove stop words
from nltk.corpus import stopwords

tokens_imp = [w for w in tokens_word if not w in stopwords.words('english')]
dump_json(tokens_imp,"imp",20)

#do stemming "goes" => "go"
tokens_stem = [nltk.PorterStemmer().stem(t) for t in tokens_imp]
dump_json(tokens_stem,"stem",20)

