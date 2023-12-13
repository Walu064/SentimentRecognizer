import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from preprocessing import preprocess_text

def save_model_to_file(clf : MultinomialNB, vectorizer : CountVectorizer, output_mod_file_path : str ,output_vec_file_path : str):
    
    with open(output_mod_file_path, 'wb') as f:
        pickle.dump(clf, f)
        print("zapis modelu do pliku...")

    with open(output_vec_file_path, 'wb') as f:
        pickle.dump(vectorizer, f)
        print("zapis modelu do pliku...")
    
def train_classification_model(train_data_file_path : str):
    
    train_data = pd.read_csv(train_data_file_path)

    texts = train_data['review'].tolist()
    texts_prep = []

    for text in texts:
        texts_prep.append(preprocess_text(text))

    labels = train_data['sentiment'].map({"negative" : 0, "positive" : 1}).tolist()
    print("pobieranie danych z pliku...")

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts_prep)
    print("wektoryzacja dancyh treningowych...")

    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.5, random_state=42)
    print("podział zbioru na dane treningowe i testowe...")

    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    print("trenowanie modelu...")

    predictions = clf.predict(X_test)

    report = classification_report(y_test, predictions)
    print("Classification Report:\n", report)

    save_model_to_file(clf, vectorizer, "model/model.pkl", "model/vectorizer.pkl")


if __name__ ==  "__main__":
    train_classification_model("data/reviews.csv")
