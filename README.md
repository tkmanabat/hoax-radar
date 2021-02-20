
<p align="center"> 
<img src="/static/assets/logo.png" class="center">
</p>

# Hoax Radar  :bulb:
Hoax Radar is an implementation of a Fake News Detection Flask Web Application using Natural Language Processing and Machine Learning with Python

## Background  :newspaper:
Fake news has been one of the hardest problems to solve in recent times. It has been an important talk recently in the general public due to online media outlets such as social media and blogs. According to a BBC survey, almost 79% of internet users are worried since anything online can be real or fake news. Fake news can be used as a weapon in manipulating people and initiating fake propagandas when the problem is not addressed.

## Website Snippets
### Home Page 
![](/static/assets/page1.PNG)
### Results Page
![](/static/assets/page2.PNG)
### News Feed Page
- The application gets the latest news with the help of the NewsAPI and tries to prediect the article 

![](/static/assets/page3.png)

## Dataset used in training the ML Model :iphone:
<ul>
    <li>The open source dataset that we collected consists of 40,000 news articles consisting of fake as well as real news.</li>
    <li>The news articles in the dataset were gathered u from various news outlets from March 31, 2015 up to February 13, 2018</li>
    <li>The dataset was derived from [Kaggle](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset) which is an open-source data science community</li>
</ul>


## Technology Stack Used :desktop_computer:
This web application was built on the Python programming language.
<ul>
    <li>Backend Stack: Flask</li>
    <li>Frontend Stack: Bootstrap</li>
    <li>External Libraries:</li>
        <ul>
            <li>Sklearn Library</li>
            <li>NLTK Library</li>
            <li>Newspaper3k Library</li>
        </ul>
</ul>

## Machine Learning and Natural Language Processing Techniques :mage:
 The machine learning algorithm used here is the `Passive Aggressive Classifier`. By using our dataset and the `TF-IDF Vectorizer`, it gave these results
<p align="center"> 
<img src="/static/assets/matrix.png" class="center">
</p>

Feel free to clone and improve on this end to end ML application!
Reach me at my email for any further inquiries.











