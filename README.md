# Reddit Flair Detector for r/india
### How to run
1. Clone the git repository
2. In the app.py file replace client_id, client_secret and user_agent.
3. Install the necessary requirements using the command pip install requirements.txt
4. Run app.py

## The Process
### 1. Data Scraping
For data scraping I used praw python library. I scraped 200 posts each for 13 selected flairs:'AMA', 'AskIndia', 'Business/Finance', 'Coronavirus', 'Food', 'Non-Political', 'Photography', 'Policy/Economy', 'Politics', 'Scheduled', 'Science/Technology', 'Sports', '[R]eddiquette'.
I selected these flairs by first testing on how many posts do all the reddit flairs have and selected the prominent ones.
I saved the data I scraped in a csv format file.

### 2. Extrapolatory Data Analysis and Preprocessing
Next, I analysed the data I extracted. I checked for how many posts had null values and plotted a graph for the number of posts with no body flair-wise.
I also plotted a heat map for seeing correlation between the int/float type data like upvotes, number of comments, etc.
I checked for the most occuring words in the data, which I was not surprised had all the stop words. This gave me the notion that there is a need to remove stop words.
So, I went on with cleaning my data and then I checked for the most occuring words flair wise. And the flairs had related most occuring words like Business/Finance had bank.
And finally saved my now cleaned data as csv.

### 3. Training and Testing the Models
I trained my data using these 5 algorithms - Multinomial Naive Bayes, Logistic Regression, Random Forest, Multilayer Perceptron and Linear SVM.
The model with highest accuracy was Logistic Regression on Title+Comments+Body+URL+AuthorOfPost with 68.07% accuracy.

### 4. Web app
Made the web app using HTML and Flask. (app.py)

### 5. Deploying the Heroku App
App link :- https://r-india-flair-predictor.herokuapp.com/

##Tree Structure
.
├── app.py
├── Data
│   ├── cleaned_scrapedData.csv
│   ├── scrapedData2.csv
│   └── scrapedData.csv
├── Model
│   └── finalModel.joblib
├── nltk.txt
├── Procfile
├── __pycache__
│   └── app.cpython-37.pyc
├── requirements.txt
├── scrapedData.csv
├── Scripts
│   ├── DataScraping - Task1.ipynb
│   ├── EDA and preprocessing - Task 2.ipynb
│   └── Making and Training Model - Task 3.ipynb
└── templates
    ├── main2.html
    └── main.html
