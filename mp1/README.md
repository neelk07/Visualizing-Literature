What is this?
=============

This is a D3.js visualization of the first four chapters of "The Once and Future King". Something such as this can provide valuable information about the content of the story and also the important aspects such as characters and adjectives. The code is available on github!

How data was obtained?
======================

Using the publicly available data, the Python NLTK library, and D3.JS Javascript library, this visualization was created.

1) Text files were parsed and tokenized

2) Unnecessary tokens were removed such as commas, stop words, and non-alphabetic symbols

3) Used NLTK to take frequencies of all tokens and only saved top 50 from each chapter

4) Fed these remaining tokens in the Part of Speech tagger in NLTK

5) Result = top 50 most frequent words from each chapter sorted by part of speech and also number of times used

Most of data cleaning method is available in setup.py!
