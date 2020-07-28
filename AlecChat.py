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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# responding to user
def generate_response(user_input):
    Alec_response = ' '
    sentence_list. append(user_input)
    word_vectorizer = TfidVectorizer(tokenizer=RemovePunct, stop_words='english')
    vecrorized_words = word_vectorizer.fit_transform(sentence_list)
    similar_vector = cosine_similarity(vectorvecrorized_words[-1], vecrorized_words)
    similar_sentence = similar_vector.argsort()[0][-2]
    match_vector = similar_vector.flatten()
    match_vector.sort()
    vectored_matched = match_vector[-2]
if vector_matched == 0:
   Alec_response = Alec_response+ "Can you repeat the question"
   return Alec_response
else:
   Alec_response = Alec_response + sentence_list[similar_sentence]
   return Alec_response

continue_chat = True
print("Hello, my name is Alec")
while(continue_chat ==True):
    user_input()
    user_input = user_input.lower()
    if(user_input != 'good bye'):
        if(user_input == 'thanks' or user_input =='thank you'):
            continue_chat=Flase
            print("Alec: Your'e Welcome")
        else:
             if(reply_greeting(user_input)!=None):
                 print("Alec:" +reply_greeting(user_input))
             else:
                print("Alec: ", end=" ")
                print(generate_response(user_input))
                sentence_list.remove(user_input)
else:
    continue_chat=False
    print("Alec: Good bye")