import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix



#Read the data
df=pd.read_csv('dataset/news.csv')

#Get shape and head
df.shape
df.head()

# Get the labels
labels=df.label
labels.head()

# Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

# Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
# tfidf_test=tfidf_vectorizer.transform(x_test)


# Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

# Predict on the test set and calculate accuracy
# y_pred=pac.predict(tfidf_test)

def askLocal(data):
    analysis_result = []
    for i in data:
        transformed_txt = tfidf_vectorizer.transform([i["text"]])
        prediction = pac.predict(transformed_txt)
        confidence = pac.decision_function(transformed_txt)
        result = {
            "id": i["id"],
            "text": i["text"],
            "result":{
                "sentiment_analysis": "Anger, Anxiety",
                "extra_comment": "Extra comment that AI wanted to say.",
                "accuracy": round(abs(confidence[0]) * 100, 2), 
                "is_fake": True if prediction[0] == "FAKE" else False,
                "sources": [
                "https://www.cinestaan.com/articles/27754/krunal-pandya-the-cricketer-was-not-in-pushpa-the-rule",
                "https://www.republicworld.com/sports-news/cricket-news/ipl-2023-krunal-pandya-reveals-all-about-his-pushpa-celebration-after-dismissing-virat-kohli-articles-119234",
                "https://www.news18.com/cricketnext/news/krunal-pandyas-pushpa-celebration-after-virat-kohlis-wicket-goes-viral-7529279.html"
                ]
            }
        }
        analysis_result.append(result)
    
    return analysis_result
