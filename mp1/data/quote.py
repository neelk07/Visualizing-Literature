import nltk
#from nltk.book import *
from nltk.draw import tree
from nltk.tree import *


chp = open('ofk_chap_c.txt').read()

sentences = nltk.sent_tokenize(chp)
tokenized_sentences = [nltk.word_tokenize(s) for s in sentences]
tagged_sentences = [nltk.pos_tag(s) for s in tokenized_sentences]
chunked_sentences = nltk.batch_ne_chunk(tagged_sentences)
entity_types = ['ORGANIZATION',	'PERSON','LOCATION','DATE','TIME','MONEY','PERCENT','FACILITY','GPE']

def extract_entities(t):
    entity_names = []
                          
    if hasattr(t, 'label') and t.label():
        if t.label() in entity_types:
            entity_names.append((t.label(),' '.join([child[0] for child in t])))
        else:
            for child in t:
                  entity_names.extend(extract_entities(child))
    return entity_names

enames = []
for tree in chunked_sentences:
    enames.extend(extract_entities(tree))

print enames
