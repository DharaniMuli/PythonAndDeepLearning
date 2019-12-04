import keras
from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

twt = ['the heart and the funnybone thanks']
json_file = open('model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model1.h5')

max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(twt)

#vectorizing the tweet by the pre-fitted tokenizer instance
twt = tokenizer.texts_to_sequences(twt)

#padding the tweet to have exactly the same shape as `embedding_2` input
twt = pad_sequences(twt, maxlen=6, dtype='int32', value=0)
print(twt)
sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
print(sentiment)
if(np.argmax(sentiment) == 0):
    print("negative")
elif (np.argmax(sentiment) == 1):
    print("somewhat negative")
elif (np.argmax(sentiment) == 2):
    print("neutral")
elif (np.argmax(sentiment) == 3):
    print("somewhat positive")
elif (np.argmax(sentiment) == 4):
    print("positive")
