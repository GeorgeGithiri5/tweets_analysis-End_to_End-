from flask import Flask,url_for,render_template,request,redirect
from joblib import load
from GetTweets import get_related_tweets

pipeline = load("text_classification.joblib")

def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    data =str(tweets.predction.value_counts()) + '\n\n'
    return data + str(tweets)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=['POST','GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success',name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "

if __name__ == '__main__':
    app.run(debug=True)