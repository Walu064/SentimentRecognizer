import os
import pickle

def get_classification_model():
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_path, '..', 'model', 'model.pkl')
    with open(file_path, 'rb') as f:
        clf = pickle.load(f)
    return clf