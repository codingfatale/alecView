import ntlk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re

#scraping the website
web_data = urllib.request.urlopen('https://www.monster.com/career-advice/article/top-10-interview-questions-prep')
web_data = web_data.read()

article_html = bs.BeautifulSout(raw_html, 'lxml')
article_paragraphs = article_html.find_all('p')
article_text = ' '

for para in article_paragraphs:
 article_text += para.text

 article_text = article_text.lower()

 sentence_list = nltk.sent_tokenize(article_text)
 sentence_list = ntlk.word_tokenize(article_text)

 #lemmatization and remove punctuation
 lemmatizer = ntlk.stem.WordNetLemmatizer()
 def LemmatizeWords(words):
     return [lemmatizer.lemmatize(word) for word in words]

 remove_punct = dict((ord(punctuation), None) for punctuation in string.punctuation)

 def RemovePunct(text):
     return LemmatizeWords(ntlk.word_tokenize(text.lower().translate(remove_punct)))

 #greetings

 greeting_input = ("hello", "my name is Alec")
 greeting_output = ("hello", "nice to meet you")

 def reply_greeting(text):
     for word in text.split():
         if word.lower() in greeting_input:
             return random.choice(greeting_output)