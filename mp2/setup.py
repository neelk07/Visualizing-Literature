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

####    GLOBAL VARIABLES    ####
TS_URL = 'http://text-processing.com/api/sentiment'
allChaps = []
chp_words = []
total_tokens = []
tokens_POS = dict()
pos_list = ['NN', 'JJ', 'VB']
pos_title = ['Nouns', 'Adjectives', 'Verbs']
chap_title = ['THE SWORD IN THE STONE - CHP 1', 'THE QUEEN OF AIR AND DARKNESS - CHP 2', 'THE ILL-MADE KNIGHT - CHP 3', 'THE CANDLE IN THE WIND - CHP 4']
chap_title_short = ['CHP 1', 'CHP 2', 'CHP 3', 'CHP 4']
            
for f in sys.argv[1:]:            
    #the file given as input is analyzed
    filename = f
    
    raw_text = open(filename).read()

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
    
    tokenize_sent = tokenizer.tokenize(raw) 
    
    for sent in tokenize_sent:
    
        #tokenize sentence
        tokens_raw = nltk.word_tokenize(sent) 
        
        #convert everything to lowercase for
        tokens_lower = [w.lower() for w in tokens_raw] #change to lower case
        
        #remove period from end of sentences
        tokens_punct = [re.sub('\.','',w) for w in tokens_lower] 
                
        #only keep alphabetic strings
        tokens_word = [w for w in tokens_punct if w.isalpha()] #just keep words
        
        #remove stop words
        tokens_imp = [w for w in tokens_word if not w in stopwords.words('english')]
        
        #save tokens
        total_tokens.append(tokens_imp)
    
        #get part of speech for each work
        tokens_POS.update(dict(nltk.pos_tag(tokens_imp)))
        
    
    
    #get dictionary of freq
    tokens_freq = FreqDist(total_tokens)
    
    #get top tokens
    top_tokens = [token for token in tokens_freq]
     
    #look at the 50 most frequently used words    
    top_tokens = top_tokens[:75]    
    
    #save tokens from each chp
    chp_words.append(top_tokens)
    
    #delete unnecessary from pos list
    for token in tokens_POS.keys() if not in top_tokens:
        del tokens_POS[token]    
    
    
    #lets filter by POS
    
    nn_dict = {}
    jj_dict = {}
    vb_dict = {}
    
    for p in pos_list:
        for word in tokens_POS:
            if tokens_POS[word] == 'NNP' or tokens_POS[word] == 'NN': #or 'NNS' or 'NNP'):
                nn_dict[word] = tokens_freq[word]
            if tokens_POS[word] == 'JJ' or tokens_POS[word] == 'JJR':# or 'JJS'):
                jj_dict[word] = tokens_freq[word]
            if tokens_POS[word] == 'VB' or tokens_POS[word] == 'VBP':# or 'VBD' or 'VBZ' or 'RB'):
                vb_dict[word] = tokens_freq[word]
    
    #generate the dictionary for each of the types
    table_nn = [dict(name=w,size=tokens_freq[w]) for w in nn_dict]
    
    table_jj = [dict(name=w,size=tokens_freq[w]) for w in jj_dict]
    
    table_vb = [dict(name=w,size=tokens_freq[w]) for w in vb_dict]
    
    pos_table_list = [table_nn, table_jj, table_vb]
    
    table_chp = [dict(name=pos_title[i],children=pos_table_list[i]) for i in range(0,len(pos_list))]
        
    allChaps.append(table_chp)
                
table_final = {'name':'OFK', 'children':dict(name=chap_title_short[i], children=allChaps[i]) for i in range(0,len(sys.argv[1:]))]

#table_unique = list(  (((set(chp_words[0])-set(chp_words[1]))-set(chp_words[2]))-set(chp_words[3]))  )

#print table_unique


#table_final = dict(table_final)

with open("final" + ".json",'w') as outfile:
          json.dump(table_final,outfile, sort_keys = True, indent = 4,
ensure_ascii=False)
     
   
#print "Analyzing:", filename        
#print "Nouns:", (Nouns/tW)*100
#print "Adjectives:", (Adjectives/tW)*100
#print "Verb-Related:", (VerbR/tW)*100



#### SENTIMENT ANALYSIS REQUEST ######

#data = urllib2.urlencode({"text":word})
#serialized_data = urllib2.urlopen(TS_URL,data).read()
#data = json.loads(serialized_data)





