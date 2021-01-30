from flask import Flask, render_template, request
import xmodel
from xmodel import get_headlines

app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    url = request.form['url']
    predict = xmodel.predict(url)
    value = predict[1]
    text = predict[2]
    article_title = predict[0]
    image=predict[3]
    return render_template('result.html',
                          value = value,
                          text = text,
                          article_title=article_title,
                          url=url,
                          image=image)
  else:
    return render_template('home.html')

@app.route('/newsfeed')
def news_feed():
    headlines=get_headlines()
    return render_template('news_feed.html',headlines=headlines)

@app.route('/aboutus')
def about_us():
    return render_template('about_us.html')



if __name__=='__main__':
    app.run(debug=True)