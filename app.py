import flask
import joblib
import praw
import re
import nltk
import json
nltk.download("stopwords")
from nltk.corpus import stopwords
app = flask.Flask(__name__, template_folder='templates')

def cleanData(s):
	s=str(s).lower()
	s=re.compile(r'https?:\/\/\S+').sub(' ',s)
	s=re.compile(r'[0-9@#$&%\n\*()!\+-]').sub(' ',s)
	s=re.compile(r'[\/.,\[\];{}|:"<>\?!]').sub(' ',s)
	stopwordsSet=set(stopwords.words('english'))
	temp=""
	for i in s.split(' '):
		if i not in stopwordsSet:
			temp=temp+i+" "
	s=temp
	return s

def predict(inputURL):
	model = joblib.load("Model/finalModel.joblib")
	reddit = praw.Reddit(client_id='client_id', client_secret='client_secret', user_agent='user_agent')
	try:
		inputSubmission = reddit.submission(url=inputURL)
	except:
		return ""
	commentsConcatenated=""
	temp=""
	count=0
	inputSubmission.comments.replace_more(limit=0)
	for eachComment in inputSubmission.comments:
		temp+=" "+str(eachComment.body)
		count+=1
		if(count>20):
			break
	cleanPost=cleanData(str(inputSubmission.url)+" "+str(inputSubmission.author)+" "+str(inputSubmission.title)+" "+str(inputSubmission.selftext)+" "+temp)
	flair=model.predict([cleanPost])[0]
	return str(flair)

@app.route('/', methods=['POST','GET'])
def main():
	if(flask.request.method=="POST"):
		inputURL = str(flask.request.form['postURL'])
		predictedFlair=predict(inputURL)
		if(predictedFlair==""):
			return flask.render_template("main.html", flair="You've Entered Wrong URL")
		else:
			return flask.render_template("main.html", flair=predictedFlair)
	if(flask.request.method=="GET"):
		return(flask.render_template('main.html'))

@app.route('/automated_testing', methods=['POST'])
def automateTest():
	a=flask.request.files["upload_file"]
	b=a.read().decode("utf-8").split('\n')
	d={}
	for i in b:
		d[i]=predict(i)
	return json.dumps(d)

if __name__ == '__main__':
	app.run(debug=True)
