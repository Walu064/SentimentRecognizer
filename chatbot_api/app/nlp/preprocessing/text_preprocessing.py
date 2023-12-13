import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokenized = word_tokenize(text)
    tokenized = [word for word in tokenized if not word in stop_words]
    pos = pos_tag(tokenized)
    nouns_adjectives = [word for word, pos in pos if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS']]
    return ' '.join(nouns_adjectives)