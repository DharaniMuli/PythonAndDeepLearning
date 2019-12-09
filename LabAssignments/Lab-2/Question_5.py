import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import keras
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.wrappers.scikit_learn import KerasClassifier
import re
import tensorflow as tf

from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('train.tsv',sep='\t')
# Keeping only the neccessary columns
data = data[['Phrase','Sentiment']]

# data = data[data.sentiment != 'Neutral']

data['Phrase'] = data['Phrase'].apply(lambda x: x.lower())
data['Phrase'] = data['Phrase'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

print(data[data['Sentiment'] == 0].size)
print(data[data['Sentiment'] == 1].size)
print(data[data['Sentiment'] == 2].size)
print(data[data['Sentiment'] == 3].size)
print(data[data['Sentiment'] == 4].size)


max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split='\t')
tokenizer.fit_on_texts(data['Phrase'].values)
X = tokenizer.texts_to_sequences(data['Phrase'].values)
print(X)
X = pad_sequences(X)
print(X)
embed_dim = 128
lstm_out = 196

# tbCallBack= keras.callbacks.TensorBoard(log_dir='./MovieSentimentGraph', write_graph=True, write_images=True)


def createmodel():
    model = Sequential()
    model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
    model.add(SpatialDropout1D(0.4))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(5,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
    return model
    print(model.summary())

labelencoder = LabelEncoder()
integer_encoded = labelencoder.fit_transform(data['Sentiment'])
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

model = createmodel()
history = model.fit(X_train, Y_train, epochs = 4, batch_size=40, verbose = 2)
# twt = ['A lot of good things are happening. We are respected again throughout the world, and that\'s a great thing']

score,acc = model.evaluate(X_test,Y_test,verbose=2,batch_size=40)
print(score)
print(acc)

#save to disk
model1_json = model.to_json()
with open('model1.json', 'w') as json_file:
    json_file.write(model1_json)
model.save_weights('model1.h5')

epoch_count = range(1, len(history.history['loss']) + 1)
import matplotlib.pyplot as plt
plt.plot(epoch_count, history.history['loss'], 'r--')
plt.plot(epoch_count, history.history['val_loss'], 'b-')
plt.legend(['Training Loss', 'Validation Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
