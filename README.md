# SentimentRecognizer

**Instrukcja instalacji i uruchomienia aplikacji**

1. Sklonuj repozytorium:

```
git clone https://github.com/Walu064/SentimentRecognizer
```
2. Przejdź do katalogu głownego repozytorium, a następnie do katalogu chatbot_api

3. Poleceniem terminala utwórz środowisko wirtualne:
```
python -m venv .venv
```
4. Zainstaluj wymagane moduły:
```
pip install requirements.txt
```
5. Przejdź do katalogu /app/, uruchom skrypt "main.py":
```
python main.py
```
6. W środowisku Visual Studio otwórz projekt za pomocą pliku rozwiązania (SentimentRecognizer.sln)

7. Za pomocą menadżera pakietów NuGet zainstaluj pakiet Newtonsoft.json, następnie skompiluj i uruchom aplikację.

8. Korzystaj z aplikacji wpisując frazy w pole tekstowe. Obserwuj log po stronie API, by widzieć komunikację pomiędzy dwoma warstwami.
