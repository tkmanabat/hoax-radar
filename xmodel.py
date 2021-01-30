from newspaper import Article
import pandas as pd
import pickle
from newsapi import NewsApiClient



newsapi=NewsApiClient(api_key='7d125ba012bc447681da91239d255267')

passiveaggressive_model=pickle.load(open("model.pickle","rb"))
tfidf_vectorizer=pickle.load(open("vectorizer.pickle","rb"))

def predict_fake(title,text):
    
    data={"Unnamed: 0":["0000"], "title":[title], "text":[text], "label":["FAKE/REAL"]}
    frame=pd.DataFrame(data, columns= ["Unnamed: 0", "title","text","label"])
    frame.drop("label",axis=1)
    tfidf_test=tfidf_vectorizer.transform(frame['text'])
    pred = passiveaggressive_model.predict(tfidf_test)
    return pred[0]

def predict(url):
    
    try:
        article=Article(url)
        article.download()
        article.parse()
        
        if len(article.text)<=500:
            return[str(article.title)]+(["INVALID"]*3)

        article.nlp()
        
        return [str(article.title), predict_fake(str(article.title),str(article.text)),str(article.summary),article.top_image]
    except ValueError:
        return(["INVALID"]*4)
    finally:
        if len(article.text)<=500:
            return[str(article.title)] + (["INVALID"]*4)
        return  [str(article.title), predict_fake(str(article.title), str(article.text)),  str(article.summary),article.top_image] 

def get_headlines():
    final=[]
    top_headlines= newsapi.get_top_headlines(language='en')
    
    for i in top_headlines['articles']:
        k=predict(i['url'])
        final.append([i['url'], i['title'], i['description'], i['source']['name'], i['urlToImage'], k[1],i['publishedAt']])
        
    return final

#link="https://clickhole.com/body-positivity-win-dove-has-changed-the-name-of-their-company-to-fat-people-soap/"

#print(predict(link))

