import pandas as pd
from nltk.corpus import stopwords
import string
import nltk
import re

def remove_stopwords(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)

    return ' '.join([word for word in nopunc.split() if word.lower() not in stopwords.words('english')])
def tokenize(mess):
  return mess.split()

# def slang_to_english(mess):
#     mess = mess.split()
#     dictionary = {'u': 'you', 'ppl': 'people', 'bc': 'because', 'bs': 'bullshit', 'cya': 'see you', 'omg': 'oh my god',
#                   'hf': 'have fun', 'gl': 'good luck',
#                   'w/o': 'without', 'luv': 'love', 'prob': 'probably', 'wp': 'well played', 'gg': 'good game',
#                   'yg': 'young gunner', 'fud': 'food',
#                   'btw': 'by the way', 'omw': 'on my way', 'y\'all': 'you all', 'f**king': 'fucking', 'cud': 'could',
#                   'f***ing': 'fucking', 'kul': 'cool',
#                   'a**hole': 'asshole', 'fyn': 'fine', 'f***': 'fuck', 'yur': 'your', 'gr8': 'great', 'pdx': 'portland',
#                   'govt': 'government',
#                   'yr': 'your', 'wud': 'would', 'lyk': 'like', 'wateva': 'whatever', 'ttyl': 'talk to you later',
#                   'fam': 'family', 'ty': 'thank you',
#                   'omg': 'oh my god', 'blvd': 'boulevard', 'bruh': 'brother', 'hv': 'have', 'dy': 'day',
#                   'bihday': 'birthday', 'impoant': 'important',
#                   'nutshel': 'nutshell', 'exactli': 'exactly', 'fishi': 'fishy', 'easili': 'easily',
#                   'Ima': 'i am going to',
#                   'Y’all': 'you all', 'urd': 'agree', 'wkly': 'weekly', 'dunno': 'don\'t know', 'alr': 'already',
#                   '2': 'to', '4': 'for'}
#     for idx, word in enumerate(mess):
#         if word in dictionary:
#             mess[idx] = dictionary[word]
#     return ' '.join(mess)

from nltk.stem import PorterStemmer
def stemming(mess):
  return ' '.join([ PorterStemmer().stem(word) for word in mess.split()])

def remove_puntuaction(mess):
    mess.translate(None, string.punctuation)

def clear_notunicode(mess):
  return re.sub(r'\W|\b\w*\d\b', ' ', mess)

def lower_message(mess):
  return mess.lower()
def preprocess(sms):
    sms = [sms]
    d = {'message': sms}
    df = pd.DataFrame(data=d)

    nltk.download('stopwords')
    #df['message'] = df['message'].apply(lower_message)
    df['message'] = df['message'].apply(remove_stopwords)
    df['message'] = df['message'].apply(stemming)
    df['message'] = df['message'].apply(tokenize)
    #df['message'] = df['message'].apply(slang_to_english)
    return df
