#from the book, ch 6
#define a feature extractor -> encoding relevent features in a dictionary
def gender_features(word):
    return {
    'last_letter': word[-1],
    'last_three' : word[-3:],
    'last_is_vowel' : (word[-1] in 'aeiouy')}


gender_features('Shrek')




#now prepare a list of examples and corresponding class labels

import nltk
import collections
from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] +
    [(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(names)

#use the feature extractor to process the names data, and divide the resulting list of feature sets into a training set and test set. Use the training set to train a naive Bayes classifier
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

#let's test it out on some names that did not appear in its training data:
classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Trinity'))

#check the accuracy of our classifier trained on the first 500 names by comparing to the gold standard of the last 500 names as the test set
print nltk.classify.accuracy(classifier, test_set)

#check several kinds of precision and recall (does so over the entire test set)
pos_gold_standard = set()
neg_gold_standard = set()
pos_train_labelled = set()
neg_train_labelled = set()
for i, (feats, label) in enumerate(test_set):
   #adds identifier to appropriate labelled set
   if (label == 'male'): pos_gold_standard.add(i)
   else: neg_gold_standard.add(i)
   #finds the label the classifier would give
   observed = classifier.classify(feats)
   #puts the identifier under that label
   if (observed == 'male'): pos_train_labelled.add(i)
   else: neg_train_labelled.add(i)

print 'pos precision:', nltk.metrics.precision(pos_gold_standard, pos_train_labelled)
print 'pos recall:', nltk.metrics.recall(pos_gold_standard, pos_train_labelled)
print 'pos F-measure:', nltk.metrics.f_measure(pos_gold_standard, pos_train_labelled)
print 'neg precision:', nltk.metrics.precision(neg_gold_standard, neg_train_labelled)
print 'neg recall:', nltk.metrics.recall(neg_gold_standard, neg_train_labelled)
print 'neg F-measure:', nltk.metrics.f_measure(neg_gold_standard, neg_train_labelled)

# the numbers are the likelihood ratios
classifier.show_most_informative_features(5)

#when constructing a single list that contains the features of every instance, use this which returns an object that acts like a list but does not store all the feature sets in memory:
from nltk.classify import apply_features

train_set = apply_features(gender_features, names[500:])
test_set = apply_features(gender_features, names[:500])
