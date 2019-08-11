
#import libraries 

import io
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwaise import cosine_similarity 

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular',quiet =True)
#nltk.download('pukt')
#nltk.download('wordnet')


#read the corpus file
with open('InterveiwBot.txt','r',errors='ignore') as fin:
raw =fin.read().lower()
	
#convert to sentences
sent_tokens = nltk.sent_tokenize(raw) 
	
# convert to list of words
word_tokens = nltk.word_tokenize(raw)
	
	
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
	remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
	def LemNormalize(text)
	  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
   
   GREET_INPUT =("hello","hi","how are you?","how are you doing today?")
   
   GREET_RESPONSE =["hello","How are you?"]
   
   
   #to get response from what you want bot to say
   
   def greet(sentence):
   
   for word in sentence.split():
    if word.lower() in GREET_INPUT:
	  return random.choice(GREET_RESPONSE)
	  
	  def response(user_response):
	      bot_response = ''
		  sent_tokens.append(user_response)
		  
	TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
	tfidf =TfidfVec.fit_transform(sent_tokens)
	vals = cosine_similarity(tfidf[-1],tfidf)
	idx=vals.argsort()[0][-2]
	flat = vals.flatten()
	flat.sort()
	req_tfidf = flat[-2]
	
	   if(req_tfidf == 0):
	     bot_response + " I do not Understand"
		 return bot_ response
   
   
   else:
   
   bot_response = bot_response + sent_tokens[idx]
   return bot_response
   
   # line for the chatbot
 
flag = True
print("ALEC: My name is Alec.")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
if(user_response != 'good bye' or user_response != 'bye'):
   if(user_response == 'Thank you' or user_response == 'thanks for your time'):
     flag = False
     print("ALEC:You are welcome..")
   else:
     if(greet(user_response)!=None):
       print("ALEC: " +greet(user_response))   
else: 
    print("ALEC: ",end=" ")
    print(response(user_response))
    sent_tokens.remove(user_response)

    flag = False
    print("ALEC:Good Bye.")	
			
			
