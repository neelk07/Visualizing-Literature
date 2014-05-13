from __future__ import division
import nltk
import json
import copy
import re, pprint
from nltk.book import FreqDist
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
import urllib2
import json
import sys
import fileinput
import vl_cleanup
import csv

mc_hp1 = ["Harry", "Hermione", "Ron", "Dumbledore", "Hagrid", "Snape", "Draco", "Quirrell", "Eaters", "Voldemort"]
mc_hp2 = ["Harry", "Hermione", "Ron", "Ginny", "Dobby", "Snape", "Draco", "Riddle", "Eaters", "Voldemort"]
mc_hp3 = ["Harry", "Hermione", "Ron", "Dumbledore", "Lupin", "Sirius", "Fudge", "Pettigrew","Eaters", "Voldemort"]
mc_hp4 = ["Harry", "Hermione", "Ron", "Dumbledore", "Sirius", "Snape", "Moody", "Riddle","Eaters", "Voldemort"]
mc_hp5 = ["Harry", "Hermione", "Ron", "Dumbledore", "Sirius", "Snape", "Fudge", "Umbridge","Eaters", "Voldemort"]
mc_hp6 = ["Harry", "Hermione", "Ron", "Dumbledore", "Slughorn", "Snape", "Half-Blood", "Draco","Eaters", "Voldemort"]
mc_hp7 = ["Harry", "Hermione", "Ron", "Weasley", "Hagrid", "Snape", "Severus", "Bellatrix","Eaters", "Voldemort"]
c_list = [mc_hp1,mc_hp2,mc_hp3,mc_hp4,mc_hp5,mc_hp6,mc_hp7]
csv_file_names = ["data_hp1.csv", "data_hp2.csv", "data_hp3.csv", "data_hp4.csv", "data_hp5.csv", "data_hp6.csv", "data_hp7.csv"]
books = ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows"]

def main():
	'''
	text_file = "Harry Potter and the Sorcerer's Stone"
	raw_text = open('data/text/' + text_file + '.txt').read()
	hp_tokens = clean_up(raw_text)
	book = separate_chps(hp_tokens)
	print ("%s,%s,%s" % ("key", "value", "date"))
	for n in csv_file_names:
		retrieve_character_occurence(book,"test/"+n)
	'''
	retrieveAllInfo()
	#top_tokens = FreqDist(hp_tokens)
	#get top tokens
	#top_tokens = [token for token in top_tokens]
	#harry = retrieve_character_occurence("Harry", book)
	#hermione = retrieve_character_occurence("Hermione", book)
	#ron = retrieve_character_occurence("Ron", book)
	#for i in range(len(harry)):
	#	print ("%d,%d,%d,%d" % (i+1,harry[i], hermione[i], ron[i]))

def retrieveAllInfo():
	for i in range(len(books)):
		text_file = books[i]
		raw_text = open('data/text/' + text_file + '.txt').read()
		hp_tokens = clean_up(raw_text)
		book = separate_chps(hp_tokens)
		characters = c_list[i]
		print ("%s,%s,%s" % ("key", "value", "date"))
		retrieve_character_occurence(characters,book,"data/character_mentions/"+csv_file_names[i])
	


'''@description: cleans up text and returns a list of tokens
   @returns: list of tokenized text'''
def clean_up(raw_text):    
    #tokenize raw text
    tokens_raw = nltk.word_tokenize(raw_text) 
    #remove period from end of sentences
    tokens_punct = [re.sub('\.','',w) for w in tokens_raw] 
    #only keep alphabetic strings
    tokens_word = [w for w in tokens_punct if w.isalpha() or w.isdigit()]
    #remove stop words
    #tokens_imp = [w for w in tokens_word if not w in stopwords.words('english')]
    return tokens_word


'''@description: returns a list of lists of which each list will be a chapter
   @returns: list of lists of tokenized text of which each list is a chapter
   @important: needs markers in textfile such as ex: "Chapter 1"		'''
def separate_chps(tokens):
	#will be the list that holds lists of tokenized words from each chapter
	book = []
	chp_list = []
	for i in range(0,len(tokens)):
		if tokens[i] == "Chapter" and tokens[i+1].isdigit():
			#we need to empty list and start populating again
			c_list = list(chp_list)
			book.append(c_list)
			chp_list = []
		else:
			chp_list.append(tokens[i])

	book.append(chp_list)
	return book


'''@description: returns percentage for new words/total words for each chapter
   @returns: list of floats'''
def chp_diff(book):
	json_list = [[], []]
	#print "%s\t%s" % ("Chapter", "Frequency")
	total = 0
	diff_list = []
	book_set = set()
	for i in range(1,len(book)):
		chp = book[i]
		#get important named entities in chapter
		chp = retrieve_named_entities(FreqDist(chp))
		chapter = set(chp)

		#retrieve total number of named entities in the chp
		chp_named_entities = len(chapter)

		#retrieves unique number of named entities in the chp
		chp = chapter.difference(book_set)
		imp_chp = len(chp)

		y = chp_named_entities - imp_chp
		per = imp_chp/chp_named_entities

		json_list[0].append(dict(time=i,y=per))
		json_list[1].append(dict(time=i,y=1-per))


		book_set.update(chapter)
		#imp_book = len(book_set)
		per = imp_chp/chp_named_entities
		diff_list.append(per)
		total = total + per
		#print "%d\t%f" % (i, per)

		#print "Chapter ", i , ": ", per

	#print "Total: ", total
	print json.dumps(json_list)
	return diff_list


'''@description: returns list of named entities for each chapter
   @param: chp -> freq dist for chapter, top -> number of top entities 
   @returns: list of strings'''
def retrieve_named_entities(chp):
	#list to return at the end
	chp_list = []
	top_tokens = [token for token in chp]  

    #retrieve part of speech
	tokens_pos = nltk.pos_tag(top_tokens)

	for (k,v) in tokens_pos:
		if v == 'NNP' or v == 'NN' or 'NNPS' or 'FW':
			chp_list.append(k)

	return chp_list

'''@description: returns csv_file for character occurance per chapter
   @param: character -> name of string of character, book -> list of tokenized words separated by chapter
   @returns: creates csv file of frequency of character and chapter'''
def retrieve_character_occurence(characters,book,csv_file):
	myfile = open(csv_file, 'wb')
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	row = ['key','value','date']
	wr.writerow(row)
	i = 0
	for character in characters:
		i = i + 1
		match = 0
		count = 0
		l = []
		#print ("%s\t%s\t%s" % ("chapter", "frequency", "character")) 
		for chp in book:
			for word in chp:
				if word == character:
					match = match + 1
			l.append(match)
			#print ("%s,%d,%d" % (character,match,count))
			row = []
			row.append(character)
			row.append(match)
			row.append(count)
			wr.writerow(row)
			match = 0
			count = count + 1
	return l


'''@description: prints out chapters and their lengths'''
def print_chp_lens(book):
	for i in range(0, len(book)):
		print "Chapter ", i, ": ", len(book[i])


if __name__ == "__main__":
    main()
		
	







