import pandas as pd
import operator

from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten, LSTM
from keras.layers import GlobalMaxPooling1D
from keras.models import Model
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.layers import Input
from keras.layers.merge import Concatenate
from keras.callbacks import ModelCheckpoint
import sys
import numpy as np
import re

import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)
df = pd.read_csv('./ted_main.csv')
df2 = pd.read_csv('./transcripts.csv')

df3 = pd.merge(left=df,right=df2, how='left', left_on='url', right_on='url')

def preprocess_text(sen):
    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sen)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence

X=[]
y=[]
key = {
    "Funny":0,
    "Beautiful":1,
    "Ingenious":2,
    "Courageous":3,
    "Longwinded":4,
    "Confusing":5,
    "Informative":6,
    "Inspiring":7,
    "Fascinating":8,
    "Unconvincing":9,
    "Persuasive":10,
    "Jaw-dropping":11,
    "OK":12,
    "Obnoxious":13
    


}

for i,row in df3.iterrows():
    string = str(row['transcript'])
    X.append(preprocess_text(string))
    total = 0
    counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for rating in eval(row['ratings']):
        total+=rating['count']
        counts[key[rating['name']]]=rating['count']
        
    #later get top 3 and train with that
    #USE ALL OF THEM AND PUT EACH OF THEM AS PERCENTAGE DECIMAL AND OUTPUT WITH PERCENTAGES ON EACH SECTION
    #Funny, Beautiful
    
    percentages = [x/total for x in counts]
    y.append(percentages)
y=array(y)




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
X_test=[preprocess_text(open('speech.txt', 'r').read())]


tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

vocab_size = len(tokenizer.word_index) + 1
maxlen=1000

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

embeddings_dictionary = dict()

glove_file = open('glove.6B.100d.txt', encoding="utf8")

for line in glove_file:
    records = line.split()
    word = records[0]
    vector_dimensions = np.asarray(records[1:], dtype='float32')
    embeddings_dictionary[word] = vector_dimensions
glove_file.close()

embedding_matrix = np.zeros((vocab_size, 100))
for word, index in tokenizer.word_index.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector

deep_inputs = Input(shape=(maxlen,))
embedding_layer = Embedding(vocab_size, 100, weights=[embedding_matrix], trainable=False)(deep_inputs)
LSTM_Layer_1 = LSTM(128)(embedding_layer)
dense_layer_1 = Dense(14, activation='sigmoid')(LSTM_Layer_1)
model = Model(inputs=deep_inputs, outputs=dense_layer_1)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
model.load_weights('all_ratings_1000.hdf5')
""" filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-tedtalk.hdf5"    
checkpoint = ModelCheckpoint(
    filepath, monitor='loss', 
    verbose=0,        
    save_best_only=True,        
    mode='min' 
)

callbacks_list = [checkpoint]      
history = model.fit(X_train, y_train, batch_size=128, epochs=250, verbose=1, validation_split=0.2, callbacks=callbacks_list)

score = model.evaluate(X_test, y_test, verbose=1)

print("Test Score:", score[0])
print("Test Accuracy:", score[1]) """

def keyByValue(value):
    for name, index in key.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if value == index:
            return name

arr=model.predict(X_test)
print(arr)
dictionary = {}
for i in range(0,len(arr[0])-1):
    dictionary[keyByValue(i)]=arr[0][i]
dictionary=dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))
print(dictionary)

#train with full text>