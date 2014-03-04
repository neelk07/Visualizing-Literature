# Code modified from original posting here
# http://stackoverflow.com/questions/14364762/counting-n-gram-frequency-in-python-nltk
import nltk
import vl_cleanup
from nltk.corpus import wordnet
from nltk.util import ngrams

n = 5

f = open('data/ofk.txt')
raw = f.read()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
tokenize_sent = tokenizer.tokenize(raw) 




#tokenize the text
#tokens = vl_cleanup.clean_up(raw)
#
#tokens = vl_cleanup.mostFreqTokens(tokens)

#tokens = tokens[:20]

#pos_dict = vl_cleanup.get_POS(tokens)




'''
#Create your bigrams
bgs = nltk.bigrams(tokens)

#compute frequency distribution for all the bigrams in the text
bigramdist = nltk.FreqDist(bgs)
worddist = nltk.FreqDist(tokens)




#characters = ["Ector", "Grummore", "Merlyn", "Kay", "Pellinore"]
#actions = ["stood", "look", "say", "go", "fight"]
characters = pos_dict['NN']
actions = pos_dict['VB']

for char1 in characters:
    for char2 in characters:
        char1 = wordnet.synset(char1)
        char2 = wordnet.synset(char2)
        print char1,' and ', char2,': ', char1.path_similarity(char2)


#print the counts for the bigrams
print "Bigram counts"
for firstword in characters:
    for secondword in actions:
        flag = bigramdist.get(firstword,secondword)
        if flag == 0:
            continue
        else:
            print firstword + " " + secondword + ": " + str( bigramdist.get( (firstword, secondword) ) )

#print the counts for the words alone
print "Individual word counts"
for word in words:
    print word + ": " + str( worddist.get( word ) )
    
#print word total
print "Number of distinct words"
print worddist.N()
'''

