from __future__ import division
import nltk
import json
import re, pprint
from nltk.book import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
import urllib2
import json
import sys
import fileinput

####    FUNCTIONS TO CLEAN UP THE DATA    ####


#input:   raw text
#output:  cleaned tokenized text
def clean_up(raw_text,sentence):    

    #tokenize raw text
    tokens_raw = nltk.word_tokenize(raw_text) 
    
    #remove period from end of sentences
    tokens_punct = [re.sub('\.','',w) for w in tokens_raw] 
    
    #only keep alphabetic strings
    tokens_word = [w for w in tokens_punct if w.isalpha()]
    
    #remove stop words
    tokens_imp = [w for w in tokens_word if not w in stopwords.words('english')]
       
    return tokens_imp


#input:  tokenized text  
#output: returns an dict with list for NN, JJ, VB  
def get_POS(tokenized_text):
    
    #get part of speech for each work
    tokens_POS = nltk.pos_tag(tokenized_text)
        
    #convert to dict
    tokens_POS = dict(tokens_POS)
    
    #lets filter by POS
    
    nn_list = []
    jj_list = []
    vb_list = []
    
    for word in tokens_POS:
            if tokens_POS[word] == 'NNP': #or tokens_POS[word] == 'NN': #or 'NNS' or 'NNP'):
                nn_list.append(word)
            if tokens_POS[word] == 'JJ' or tokens_POS[word] == 'JJR':# or 'JJS'):
                jj_list.append(word)
            if tokens_POS[word] == 'VB' or tokens_POS[word] == 'VBP':# or 'VBD' or 'VBZ' or 'RB'):
                vb_list.append(word)
    
    
    pos_dict = {'NN':nn_list, 'JJ':jj_list, 'VB':vb_list}
    return pos_dict


#input:  tokenized text
#output: list of top tokens in order
def mostFreqTokens(tokenized_text):
    
    #get dictionary of freq
    tokens_freq = FreqDist(tokenized_text)
    
    #get top tokens
    top_tokens = [token for token in tokens_freq]
    
    return top_tokens
     
    
    
    
    
   
#print "Analyzing:", filename        
#print "Nouns:", (Nouns/tW)*100
#print "Adjectives:", (Adjectives/tW)*100
#print "Verb-Related:", (VerbR/tW)*100



#### SENTIMENT ANALYSIS REQUEST ######

#data = urllib2.urlencode({"text":word})
#serialized_data = urllib2.urlopen(TS_URL,data).read()
#data = json.loads(serialized_data)





