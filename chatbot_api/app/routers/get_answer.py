from fastapi import APIRouter, Body
from langdetect import detect
from deep_translator import GoogleTranslator
from nlp import preprocess_text, get_vectorizer, get_classification_model
from models import TextFromUser, ConsoleColors

answer_router = APIRouter()

@answer_router.post("/get-answer")
async def get_answer(textFromUser : TextFromUser):
    if not textFromUser.textFromUser.strip():
        print(ConsoleColors.BLUE + "NLP:\t  "+ ConsoleColors.RESET + "Request text is empty. API returns value [2].")
        return {"sentiment" : "[2]"}
    else:
        #language detection and translating
        text = textFromUser.textFromUser
        lang = detect(text)
        translated_text = GoogleTranslator(source=lang, target='english').translate(text)
        
        # preprocessing
        print(ConsoleColors.BLUE + "NLP:\t  " + ConsoleColors.RESET +"Translated text:\t  "+ translated_text)
        preprocessed_text = preprocess_text(translated_text)
        print(ConsoleColors.BLUE + "NLP:\t  " + ConsoleColors.RESET +"Preprocessed text:\t  "+ preprocessed_text)
        
        # vectorizing
        vectorizer = get_vectorizer()
        vectorized_text = vectorizer.transform([preprocessed_text])
        
        # classification
        clf = get_classification_model()
        message_sentiment = clf.predict(vectorized_text)
        if str(message_sentiment) == "[0]":
            print(ConsoleColors.BLUE + "NLP:\t  "+ ConsoleColors.RESET + "Predicted Sentiment:\t  NEGATIVE")
        elif str(message_sentiment) == "[1]":
            print(ConsoleColors.BLUE + "NLP:\t  "+ ConsoleColors.RESET + "Predicted Sentiment:\t  POSITIVE")
        
        return {"sentiment" : str(message_sentiment)}

