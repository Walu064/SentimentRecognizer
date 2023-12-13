import nltk
import uvicorn
from fastapi import FastAPI
from routers import answer_router

app = FastAPI()
app.include_router(answer_router)

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    uvicorn.run(app, host="0.0.0.0", port=8000)

