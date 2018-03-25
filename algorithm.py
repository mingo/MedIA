import json
import numpy as np
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json
import tensorflow as tf
import requests
from bs4 import BeautifulSoup

max_words = 5000


# Load model and weights
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights('model.h5')


# Load the tokenizer trained on the dictionary
tokenizer = Tokenizer(num_words=max_words)

# Load the dictionary
with open('dictionary.json', 'r') as dictionary_file:
    dictionary = json.load(dictionary_file)
    

def convert_text_to_index_array(text, verbal=False):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
        elif verbal:
            print("'%s' not in training corpus; ignoring." %(word))
    return wordIndices


def algorithm(evalSentence):
    if len(evalSentence) == 0:
        return [-1,-1.]

    testArr = convert_text_to_index_array(evalSentence)
    data = tokenizer.sequences_to_matrix([testArr], mode='binary')
    
    pred = model.predict(data)
    
    result = [int(np.argmax(pred)), float(pred[0][np.argmax(pred)])]
    
    return result


def parse_media_press(url):
    """ Only works with http://www.medias-presse.info"""
    
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    paragraphs_ls = []

    for paragraph in soup.find_all('p', style="text-align: justify;"):
        paragraphs_ls.append(paragraph.text)

    paragraphs = "\n".join(paragraphs_ls)
    
    if paragraphs == "":
        return ""
    
    return paragraphs
    
    
