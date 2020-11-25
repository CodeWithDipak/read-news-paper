import requests
import json


def speak(str):
    """This function basically read the input string which is given as an argument."""
    from win32com.client import Dispatch
    speak1 = Dispatch("SAPI.SpVoice")
    speak1.speak(str)


if __name__ == '__main__':
    speak("News for today...Let news start...")
    url = f"http://newsapi.org/v2/everything?q=bitcoin&from=2020-10-04" \
          f"&sortBy=publishedAt&apiKey=eeb9330590604c42943a37e6a431c5e1 "
    news = requests.get(url)
    text = news.text
    news_dict = json.loads(text)
    arts = news_dict["articles"]
    for articles in arts:
        print(articles["title"])
        speak(articles["title"])
        print(articles["description"])
        speak(articles["description"])
        speak("Next news is...")
