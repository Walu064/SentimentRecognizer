import os
import pickle

def get_vectorizer():
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, '..', 'model', 'vectorizer.pkl')
    with open(file_path, 'rb') as f:
        vectorizer = pickle.load(f)
    return vectorizer
