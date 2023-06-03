import joblib
import numpy as np
from keras.utils import pad_sequences

tokenizer = joblib.load('./models/tokenizer_gen.joblib')
model = joblib.load('./models/model_gerador.joblib')

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

def gen(seq,max_len = 10):
    tokenized_sent = tokenizer.texts_to_sequences([seq])
    max_len = max_len+len(tokenized_sent[0])

    while len(tokenized_sent[0]) < max_len:
        padded_sentence = pad_sequences(tokenized_sent[-19:],maxlen=19)
        op = model.predict(np.asarray(padded_sentence).reshape(1,-1))
        tokenized_sent[0].append(op.argmax()+1)
        
    return " ".join(map(lambda x : reverse_word_map[x],tokenized_sent[0]))